"""
Web3 client for RyskFinance.
"""
import json
import logging
from collections import deque
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

import websocket
from web3 import HTTPProvider
from web3.contract import Contract

from rysk_client.src.action_type import ActionType
from rysk_client.src.collateral import CollateralFactory
from rysk_client.src.constants import (ARBITRUM_GOERLI, NULL_ADDRESS,
                                       NULL_DATA, Chain)
from rysk_client.src.crypto import EthCrypto
from rysk_client.src.operation_factory import OperationFactory
from rysk_client.src.order import Order
from rysk_client.src.order_side import OrderSide
from rysk_client.src.rysk_option_market import RyskOptionMarket
from rysk_client.src.utils import (get_contract, get_logger, get_web3,
                                   print_operate_tuple)


class Balances(Enum):
    """
    Class to represent the balances of an address.
    """


class Web3Client:  # pylint: disable=too-many-instance-attributes
    """Client for the RyskFinance protocol."""

    beyond_pricer: Contract
    opyn_controller: Contract
    option_exchange: Contract
    option_registry: Contract

    # lenses
    dhv_lens_mk1: Contract
    user_position_lens_mk1: Contract

    # collateral
    usdc: Contract
    weth: Contract

    def __init__(
        self,
        logger: Optional[logging.Logger] = None,
        crypto: Optional[EthCrypto] = None,
        chain: Chain = ARBITRUM_GOERLI,
        verbose: bool = True,
    ):
        """
        Initialize the client with the web3 provider.
        """
        self.chain = chain
        self.web3: HTTPProvider = get_web3(chain)
        self.beyond_pricer = get_contract("beyond_pricer", self.web3, self.chain)
        self.opyn_controller = get_contract("opyn_controller", self.web3, self.chain)
        self.option_exchange = get_contract("option_exchange", self.web3, self.chain)
        self.option_registry = get_contract(
            "opyn_option_registry", self.web3, self.chain
        )

        self.user_position_lens_mk1 = get_contract(
            "user_position_lens", self.web3, self.chain
        )
        self.dhv_lens_mk1 = get_contract("d_h_v_lens", self.web3, self.chain)

        self.usdc = get_contract("usdc", self.web3, self.chain)
        self.weth = get_contract("weth", self.web3, self.chain)
        # is this an artifact of the testnet?
        self.settlement_usdc = get_contract("usdc", self.web3, self.chain)
        self.settlement_weth = get_contract("weth", self.web3, self.chain)

        self._logger = logger or get_logger()
        self._processed_tx: deque = deque(maxlen=100)
        self._crypto = crypto
        self._verbose = verbose
        self._operation_factory = OperationFactory(self.chain)
        self._collateral_factory = CollateralFactory(self.chain)

    def get_otoken_contract(self, otoken_address: str) -> Contract:
        """
        Get the otoken contract.
        """
        return get_contract(
            "o_token", self.web3, chain=self.chain, address=otoken_address
        )

    def get_options_prices(
        self,
        option_data,
        dhv_exposure,
        amount=1000000000000000000,
        side="buy",
        collateral="weth",
        strike_asset="usdc",
    ):
        """,
        We call the beyond pricer to determine the prices for a market
        huge thanks to 0xPawel2 and Jib &&
        """
        if side not in ["buy", "sell"]:
            raise ValueError("Side must be buy or sell")

        if not self._collateral_factory.is_supported(collateral):
            raise TypeError(f"Collateral {collateral} is not supported")
        # here we call the contract functions

        option_series = (
            int(option_data["expiration"]),
            int(option_data["strike"]),
            bool(option_data["isPut"]),
            self._collateral_factory.from_symbol(collateral),
            self._collateral_factory.from_symbol(strike_asset),
            self._collateral_factory.from_symbol(strike_asset),
        )

        try:
            result = self.beyond_pricer.functions.quoteOptionPrice(
                option_series,
                int(amount),
                side == "sell",
                int(dhv_exposure),
            ).call()
        except Exception as error:  # pylint: disable=broad-except
            self._logger.error(
                f"Error calling beyond pricer: {error} with {option_series}"
            )

            return 0
        return result[0]

    def get_balances(self):
        """
        Get the balances for an address
        """
        safe_address = self.web3.toChecksumAddress(self._crypto.address)
        return {
            "weth": self.settlement_weth.functions.balanceOf(safe_address).call()
            / 1e18,
            "usdc": self.settlement_usdc.functions.balanceOf(safe_address).call() / 1e6,
            "eth": self.web3.eth.get_balance(self._crypto.address) / 1e18,
        }

    def watch_trades(self):
        """
        Subscribe to boeht pending trades and completed trades.
        """
        ws_connection = websocket.WebSocketApp(
            self.chain.wss_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        ws_connection.run_forever()

    def on_message(self, websocket, message):  # pylint: disable=unused-argument
        """On new message, process the message."""
        data = json.loads(message)
        if set(data.keys()) == {"id", "result", "jsonrpc"}:
            return

        tx_hash = data["params"]["result"]["transactionHash"]
        if tx_hash in self._processed_tx:
            return
        self._logger.info(f"New Transaction hash: {tx_hash}")
        tx_receipt = self.web3.eth.get_transaction_receipt(tx_hash)
        self._logger.info(f"Sender: {tx_receipt['from']}")
        tx_args, error = self._get_tx_args(tx_receipt)

        if not error:
            order = self.parse_args(tx_args, tx_receipt)
            self._logger.info(order)

        self._processed_tx.append(tx_hash)

    def parse_args(self, args, tx_hash):
        """
        parse the args from the options exchange into an order.
        """
        return Order(
            order_id=tx_hash,
            price=args["premium"] / 1e10,
            amount=args["optionAmount"] / 1e18,
            order_side=OrderSide("buy") if "buyer" in args else OrderSide("sell"),
        )

    def on_error(self, websocket, error):  # pylint: disable=unused-argument
        """On error from the websocket."""
        self._logger.error(error)

    def on_close(self, websocket, *args):  # pylint: disable=unused-argument
        """On closing the connection to the websocket."""
        self._logger.info(f"Connection closed. {args}")

    def on_open(self, websocket):
        """On opening the connection to the websocket."""
        self._logger.info(
            f"Opening connection to Option Exchange at {self.option_exchange.address}"
        )
        subscription_msg_template = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_subscribe",
            "params": ["logs", {"address": self.option_exchange.address}],
        }
        websocket.send(json.dumps(subscription_msg_template))

    def _get_tx_args(self, tx_receipt: str) -> Tuple[Dict, bool]:
        """Get the transaction arguments."""
        try:
            rich_logs = self.option_exchange.events.OptionsSold().processReceipt(tx_receipt)  # type: ignore
            return dict(rich_logs[0]["args"]), False

        except Exception:  # pylint: disable=W0718
            rich_logs = self.option_exchange.events.OptionsBought().processReceipt(tx_receipt)  # type: ignore
            return dict(rich_logs[0]["args"]), False

    def is_approved(
        self, contract: Contract, spender: str, owner: str, amount: int
    ) -> bool:
        """
        Check if the spender is approved to spend the owner's tokens.
        """
        allowance = contract.functions.allowance(owner, spender).call()
        return allowance >= amount

    def create_approval(
        self, contract: Contract, spender: str, owner: str, amount: int
    ) -> dict:
        """
        Create an approval transaction.
        """
        transaction = contract.functions.approve(
            spender, int(amount)
        ).build_transaction(
            {
                **{
                    "from": owner,
                    "nonce": self.web3.eth.get_transaction_count(owner),
                },
                **self._default_tx_params,
            }
        )
        return transaction

    @property
    def _default_tx_params(self) -> dict:
        """
        Default transaction parameters.
        """
        return {
            "gasPrice": int(self.web3.eth.gas_price * 1.5),
        }

    def fetch_user_vaults(self, address: str) -> List[Dict[str, Any]]:  # noqa: W0613
        """
        Fetch the user's positions from the options exchange.
        """
        return self.user_position_lens_mk1.functions.getVaultsForUser(
            str(self._crypto.address)  # type: ignore
        ).call()

    def get_option_chain(self):
        """
        Call the dhv_lens contract to retrieve the options chain.
        """
        return self.dhv_lens_mk1.functions.getOptionChain().call()

    def get_otoken(self, series: Dict[str, Any]):
        """
        Call the option registry to retrieve the otoken.
        underlying: address, underlying asset address is weth lower
        strikeAsset: address,
        expiration: unit256,
        isPut: bool (true if put, false if call)
        strike: unit256 (1e18)
        collateral: address Collateral asset address
        """
        arguments = (
            self._collateral_factory.WETH,
            self._collateral_factory.USDC,
            series["expiration"],
            series["isPut"],
            series["strike"],
            series["collateral"],
        )
        return self.option_registry.functions.getOtoken(*arguments).call()

    def settle_vault(self, vault_id: int):
        """Build the transaction to settle the vault."""
        operate_tuple = [
            {
                "actionType": ActionType.SETTLE_VAULT.value,
                "amount": 0,
                "asset": NULL_ADDRESS,
                "data": NULL_ADDRESS,
                "index": 0,
                "owner": self._crypto.address,  # type: ignore
                "secondAddress": self._crypto.address,  # type: ignore
                "vaultId": vault_id,
            },
        ]
        return self._operate(operate_tuple, self.opyn_controller)

    def redeem_otoken(
        self,
        otoken_id: str,
        amount: int,
    ):
        """
        Build the transaction to redeem the otoken.
        """
        self._logger.info(
            f"Redeeming {amount} of {self.web3.toChecksumAddress(otoken_id)}"
        )
        amount = int(amount * 1e8)
        operate_tuple = [
            {
                "actionType": 8,
                "owner": NULL_ADDRESS,
                "secondAddress": self._crypto.address,  # type: ignore
                "asset": otoken_id,
                "vaultId": 0,
                "amount": amount,
                "index": 0,
                "data": NULL_DATA,
            }
        ]

        return self._operate(operate_tuple, self.opyn_controller)

    def get_otoken_balance(self, otoken_id: str):
        """
        Get the otoken balance.
        """
        otoken = get_contract("o_token", self.web3, chain=self.chain, address=otoken_id)
        return otoken.functions.balanceOf(self._crypto.address).call()  # type: ignore

    def close_long(
        self,
        acceptable_premium: int,
        amount: int,
        otoken_address: str,
    ):
        """
        Build the transaction to close a long position.
        """
        operate_tuple = self._operation_factory.close_long(
            acceptable_premium=acceptable_premium,
            owner_address=self._crypto.address,  # type: ignore
            otoken_address=otoken_address,
            amount=int(amount),
        )
        return self._operate(operate_tuple, self.option_exchange)

    def get_series_info(self, otoken_address: str) -> Dict[str, Any]:
        """
        Returns the series info.
        """
        return self.option_registry.functions.getSeriesInfo(otoken_address).call()

    def close_short(
        self,
        acceptable_premium: int,
        amount: int,
        otoken_address: str,
        collateral_amount: int,
        collateral_asset: str,
        vault_id: int,
        rysk_option_market: RyskOptionMarket,
    ):
        """
        Build the transaction to close a short position.
        """
        operate_tuple = self._operation_factory.close_short(
            acceptable_premium=acceptable_premium,
            owner_address=self._crypto.address,  # type: ignore
            otoken_address=self.web3.toChecksumAddress(otoken_address),
            amount=int(amount),
            collateral_amount=int(collateral_amount),
            collateral_asset=collateral_asset,
            vault_id=vault_id,
            rysk_option_market=rysk_option_market,
        )
        return self._operate(operate_tuple, self.option_exchange)

    def _operate(
        self,
        operate_tuple: List[Dict[str, Any]],
        contract: Contract,
    ):
        if self._verbose:
            print_operate_tuple(operate_tuple)
        return contract.functions.operate(operate_tuple).build_transaction(
            {
                **{
                    "from": self._crypto.address,  # type: ignore
                    "nonce": self.web3.eth.get_transaction_count(self._crypto.address),  # type: ignore
                },
                **self._default_tx_params,
            }
        )
