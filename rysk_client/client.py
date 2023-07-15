"""
Simple client for the rysk contracts implemented in python.
"""
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

import web3

from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import (ARBITRUM_GOERLI, CHAINS_TO_SUBGRAPH_URL,
                                       Chain)
from rysk_client.src.crypto import EthCrypto
from rysk_client.src.operation_factory import buy, sell
from rysk_client.src.order_side import OrderSide
from rysk_client.src.pnl_calculator import PnlCalculator, Trade
from rysk_client.src.position_side import PositionSide
from rysk_client.src.rysk_option_market import OptionChain, RyskOptionMarket
from rysk_client.src.subgraph import SubgraphClient
from rysk_client.src.utils import get_contract, get_logger
from rysk_client.web3_client import Web3Client, print_operate_tuple

PRICE_DEVISOR = 1_000_000_000_000_000_000
EXPOSURE_DEVISOR = 1_000_000_000_000_000_000

ALLOWED_SLIPPAGE = 0.15

NULL_SERIES = (
    0,
    0,
    False,
    "0x0000000000000000000000000000000000000000",
    "0x0000000000000000000000000000000000000000",
    "0x0000000000000000000000000000000000000000",
)


class ApprovalException(Exception):
    """
    Exception raised when the approval fails.
    """


def from_timestamp(date_string):
    """Parse a timestamp. 2023-05-31T08:00:00.000Z"""
    return datetime.fromtimestamp(int(date_string)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def to_human_format(row):
    """
    Format the row to align to the ccxt unified client.
    'ETH-16MAY23-1550-C'
    """

    month_code = row["expiration_datetime"].strftime("%b").upper()
    day = row["expiration_datetime"].strftime("%d")
    year = str(row["expiration_datetime"].year)[2:]
    strike_price = str(int(int(row["strike"]) / PRICE_DEVISOR))

    return f"ETH-{day}{month_code}{year}-{strike_price}-{'P' if row['isPut'] else 'C'}"


DEFAULT_MARKET = {
    "base": "ETH",
    "baseId": "ETH",
    "contract": True,
    "contractSize": 1.0,
    "spot": False,
    "swap": False,
    "future": False,
    "type": "option",
    "linear": False,
    "inverse": True,
    "maker": 0.0003,
    "taker": 0.0003,
}


@dataclass
class RyskClient:  # noqa: R0902
    """
    Client for the rysk contracts.
    """

    _markets: List[RyskOptionMarket]
    _tickers: List[Dict[str, Any]]
    _otokens: Dict[str, Dict[str, Any]]
    web3_client: Web3Client

    def __init__(
        self,
        address: Optional[str] = None,
        private_key: Optional[str] = None,
        logger=None,
        chain: Chain = ARBITRUM_GOERLI,
        verbose: bool = True,
    ):
        self._markets: List[RyskOptionMarket] = []
        self._tickers = []
        self._otokens = {}
        self._option_chain: OptionChain
        self._crypto = EthCrypto(address, private_key)
        self._logger = logger or get_logger()
        self.web3_client = Web3Client(
            self._logger,
            self._crypto,
            chain=chain,
            verbose=verbose,
        )
        self.subgraph_client = SubgraphClient(CHAINS_TO_SUBGRAPH_URL[chain])
        self._logger.info(
            f"Rysk client initialized and connected to the blockchain at {self.web3_client.web3.provider}"
        )
        self._verbose = verbose

    def _sign_and_sumbit(self, txn, retries=3, backoff=2):
        """
        Sign and submit transaction.

        retries: number of retries
        backoff: backoff in seconds

        """
        try:
            txn["nonce"] = self.web3_client.web3.eth.get_transaction_count(
                self._crypto.address
            )
            signed_txn = self.web3_client.web3.eth.account.sign_transaction(
                txn, private_key=self._crypto.private_key
            )
            tx_hash = self.web3_client.web3.eth.send_raw_transaction(
                signed_txn.rawTransaction
            )
            self._logger.debug(f"Transaction hash: {tx_hash.hex()}")
            receipt = self.web3_client.web3.eth.wait_for_transaction_receipt(
                tx_hash, 180
            )
            # we need to check the receipt to see if the transaction was successful
            if receipt["status"] == 0:
                self._logger.error(f"Transaction failed: {receipt}")
                raise ValueError("Transaction Failed!")
            self._logger.debug(f"Transaction successful: {receipt}")
            return tx_hash.hex()

        except ValueError as error:
            if retries > 0:
                self._logger.warning(
                    f"Error {error} while submitting transaction. Retrying..."
                )
                time.sleep(backoff)
                return self._sign_and_sumbit(
                    txn, retries=retries - 1, backoff=backoff * 2
                )
            raise error

    def fetch_markets(self) -> List[Dict[str, Any]]:
        """
        Fetchs the markets from the subgraph.
        """

        raw_data = self.web3_client.get_option_chain()
        self._option_chain = OptionChain(raw_data)
        self._markets = [
            RyskOptionMarket.from_option_drill(*data)
            for data in self._option_chain.active_markets
        ]
        return [market.to_json() for market in self._markets]  # type: ignore

    def to_checksum_address(self, address):
        """Convert an address to a checksum address."""
        return self.web3_client.web3.toChecksumAddress(address)

    def fetch_tickers(
        self, market: Optional[str] = None, is_active: Optional[bool] = True
    ) -> List[Dict[str, Any]]:
        """
        Fetchs the ticker from the beyond pricer smart contract.
        """

        if not self._markets:
            self.fetch_markets()

        tradeable = filter(lambda x: x["active"] is is_active, self._markets)  # type: ignore

        if market:
            tradeable = filter(lambda x: x["id"] == market, tradeable)  # type: ignore

        return [market.to_json() for market in self._markets]  # type: ignore

    @property
    def otokens(self) -> Dict[str, Dict[str, Any]]:
        """
        Returns a dictionary of the otokens.
        """
        if not self._otokens:
            self.fetch_tickers()
        self._otokens = {ticker["info"]["id"]: ticker for ticker in self._tickers}
        return self._otokens

    def fetch_positions(self, expired=False) -> List[Dict[str, Any]]:
        """
        Fetchs the positions from the subgraph.
        """

        if self._crypto.address is None:
            raise ValueError("No account address was provided.")

        longs = self.subgraph_client.query_longs(address=self._crypto.address)
        shorts = self.subgraph_client.query_shorts(address=self._crypto.address)

        parsed_short = [self._parse_position(pos, PositionSide.SHORT) for pos in shorts]
        parsed_longs = [self._parse_position(pos, PositionSide.LONG) for pos in longs]

        if expired:
            positions = filter(
                lambda x: x["datetime"] <= datetime.now(),
                parsed_longs + parsed_short,
            )
        else:
            positions = filter(
                lambda x: x["datetime"] > datetime.now(),
                parsed_longs + parsed_short,
            )
        return list(positions)

    def _parse_position(
        self, position: Dict[str, Any], side: PositionSide
    ) -> Dict[str, Any]:
        """
        Parse the position data from the subgraph into a unified format.
        """
        position["expiration_datetime"] = datetime.fromtimestamp(
            int(position["oToken"]["expiryTimestamp"])
        )
        position["strike"] = float(position["oToken"]["strikePrice"]) * 1e10
        position["isPut"] = position["oToken"]["isPut"]

        pnl_calculator = PnlCalculator()

        buys = [
            Trade(int(order["amount"]) / 1e18, total_cost=int(order["premium"]) / -1e6)
            for order in position["optionsBoughtTransactions"]
        ]
        sells = [
            Trade(-int(order["amount"]) / 1e18, total_cost=-int(order["premium"]) / 1e6)
            for order in position["optionsSoldTransactions"]
        ]

        pnl_calculator.add_trades(buys + sells)

        symbol = to_human_format(position)

        if symbol in self.otokens:
            self._logger.debug(f"Found `{symbol}` in the otokens list.")
            book_side = "ask" if side == PositionSide.LONG else "bid"
            price = self.otokens[symbol][book_side]
            pnl_calculator.update_price(price)
        else:
            self._logger.debug(
                f"Could not find `{symbol}` in the otokens list. Maket is probably not active."
            )
        result = {
            "id": position["id"],
            "symbol": symbol,
            "timestamp": int(position["oToken"]["expiryTimestamp"]) * 1000,
            "datetime": datetime.fromtimestamp(
                int(position["oToken"]["expiryTimestamp"])
            ),
            "initialMarginPercentage": None,
            "realizedPnl": pnl_calculator.realised_pnl,
            "unrealizedPnl": pnl_calculator.unrealised_pnl,
            "contractSize": pnl_calculator.position_size,
            "side": side.value,
            "size": pnl_calculator.position_size,
            "info": position,
            "entryPrice": pnl_calculator.average_price,
        }
        return result

    def create_order(
        self,
        symbol: str,
        amount: float,
        side: str = "buy",
    ) -> Dict[str, Any]:
        """Create a market order."""
        if side.upper() not in OrderSide.__members__:
            raise ValueError("Invalid order side")

        if side == OrderSide.BUY.value:
            transaction = self.buy_option(symbol, amount)
        else:
            transaction = self.sell_option(symbol, amount)
        # we can now submit it to the chain;
        # we can also confirm the otoken balance
        market = self.get_market(symbol)
        otoken_address = self.web3_client.get_otoken(market.to_series())

        old_balance = self.web3_client.get_otoken_balance(otoken_address)

        self._logger.info(f"Otken balance: {old_balance}")
        block_number = self.web3_client.web3.eth.block_number
        submitted = self._sign_and_sumbit(transaction)
        # block until the transaction is mined
        wait = 10
        while self.web3_client.web3.eth.block_number <= block_number:
            time.sleep(1)
            wait -= 1
            if wait == 0:
                raise TimeoutError("Transaction was not mined in time.")

        self._logger.info(f"Submitted transaction with hash: {submitted}")
        new_balance = self.web3_client.get_otoken_balance(otoken_address)
        self._logger.info(f"Otken balance: {new_balance}")
        if new_balance == old_balance and side == OrderSide.BUY.value:
            self._logger.error(
                f"Transaction failed to execute. Balance is still {new_balance}"
            )

        return {
            "id": submitted,
            "symbol": symbol,
            "datetime": datetime.now(),
        }

    def get_market(self, symbol: str) -> RyskOptionMarket:
        """
        Returns the market information.
        """
        if not self._markets:
            self.fetch_markets()

        for market in self._markets:
            if market.name == symbol:
                return market
        raise ValueError(f"Could not find market {symbol}.")

    def buy_option(  # noqa: R0914
        self,
        market: str,
        amount: float,
        collateral_asset: str = "USDC",
        leverage: float = 1,
    ):
        """
        Create a buy option order.
        """
        # now we can try to buy the option
        if not self._markets:
            self._logger.info("Fetching Tickers.")
            self.fetch_tickers()  # type: ignore

        self._logger.info(f"Fetching acceptable premium for {market}")
        rysk_option_market = self.get_market(market)
        rysk_option_market.collateral = Collateral.from_symbol(collateral_asset)
        self._logger.info(
            f"Buying {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )
        # we first check the approval amount of the collateral asset
        if not Collateral.is_supported(collateral_asset):
            raise ValueError(
                f"Collateral asset {collateral_asset} is not supported by the protocol."
            )
        collateral_asset_name = f"{rysk_option_market.collateral.name.lower()}"
        collateral_contract = get_contract(
            collateral_asset_name, self.web3_client.web3, self.web3_client.chain
        )
        collateral_approved = self.web3_client.is_approved(
            collateral_contract,
            self.web3_client.option_exchange.address,
            str(self._crypto.address),
            int(amount * 1e18),
        )
        self._logger.info(f"Collateral approved: {collateral_approved}.")

        if not collateral_approved:
            self._logger.info(
                f"Approving {collateral_asset} collateral for {self.web3_client.option_exchange.address}"
            )

            txn = self.web3_client.create_approval(
                collateral_contract,
                self.web3_client.option_exchange.address,
                str(self._crypto.address),
                collateral_approved + int(amount * 1e18),
            )
            # we submit and sign the transaction
            result = self._sign_and_sumbit(txn)
            self._logger.info(f"Transaction successful with hash: {result}")

        otoken_address = self.web3_client.get_otoken(rysk_option_market.to_series())
        balance = self.web3_client.get_otoken_balance(otoken_address)
        self._logger.info(f"Balance of {otoken_address}: {balance}")

        self._logger.info(
            f"Fetching market data for {market}. Otoken address: {otoken_address}"
        )
        _amount = amount * 1_000_000_000_000_000_000
        acceptable_premium = self.web3_client.get_options_prices(  # type: ignore
            rysk_option_market.to_series(),
            rysk_option_market.dhv,
            side=OrderSide.BUY.value,
            amount=_amount,
        )  # pylint: disable=E1120

        # we format 2 decimal places
        self._logger.info(f"Acceptable premium: ${acceptable_premium / 1e6:.2f}")

        # we check if we need to issue the option
        issuance_required = self.is_issuance_required(otoken_address)

        operate_tuple = buy(
            int(acceptable_premium),
            owner_address=self._crypto.address,  # pylint: disable=E1120
            amount=int(_amount),
            option_market=rysk_option_market,
            issuance_required=issuance_required,
        )

        if self._verbose:
            print_operate_tuple([operate_tuple])

        try:
            txn = self.web3_client.option_exchange.functions.operate(
                [operate_tuple]
            ).build_transaction({"from": self._crypto.address})
        except web3.exceptions.ContractCustomError as error:  # pylint: disable=E1101
            self._logger.error("Transaction failed due to incorrect parameters.")
            raise ValueError(error) from error

        return txn

    def is_issuance_required(self, otoken_address: str) -> bool:
        """
        Returns True if an issuance is required.
        """
        result = self.web3_client.get_series_info(otoken_address)
        return result == NULL_SERIES

    def sell_option(  # noqa
        self,
        market: str,
        amount: float,
        collateral_asset: str = "weth",
        leverage: float = 1,
    ):
        """
        Create a sell option order.
        """
        self._logger.info(
            f"Selling {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )

        if not self._markets:
            self._logger.info("Fetching Tickers.")
            self.fetch_tickers()
        _amount = amount * 1e18

        rysk_option_market = self.get_market(market)

        acceptable_premium = self.web3_client.get_options_prices(
            rysk_option_market.to_series(),
            dhv_exposure=rysk_option_market.dhv,
            amount=_amount,
            side=OrderSide.SELL.value,
            collateral=collateral_asset,
        )

        self._logger.info(f"Acceptable premium: ${acceptable_premium:.2f}")

        user_vaults = self.web3_client.fetch_user_vaults(self._crypto.address)
        otoken_id = self.web3_client.get_otoken(rysk_option_market.to_series())
        self._logger.info(f"Option Otoken id is {otoken_id}")

        issue_new_vault = False
        if otoken_id not in set(i[1] for i in user_vaults):
            new_vault_id = len(user_vaults) + 1
            self._logger.info(
                f"Necessary to create a vault for the user. New vault id is {new_vault_id}"
            )
            vault_id = new_vault_id
            issue_new_vault = True

        else:
            # we need to use the vault
            vault_id = [f[1] for f in user_vaults].index(otoken_id) + 1
            self._logger.info(f"Using existing vault id user_vaults {vault_id}")

        if rysk_option_market.is_put:
            collateral_asset = Collateral.USDC
            amount_to_approve = int(
                self._option_chain.current_price
                * amount
                * (1 + ALLOWED_SLIPPAGE)
                * 1e18
            )
            contract = self.web3_client.usdc
        else:
            collateral_asset = Collateral.WETH
            amount_to_approve = int(_amount * (1 + ALLOWED_SLIPPAGE))
            contract = self.web3_client.settlement_weth

        # we check the approval of the amount
        self._logger.info(
            f"Checking approval of {amount_to_approve / 1e18} of {collateral_asset}"
        )
        allowance = contract.functions.allowance(
            self._crypto.address,
            self.web3_client.option_exchange.address,
        ).call()
        self._logger.info(f"Allowance is {allowance}")
        if allowance < amount_to_approve:
            self._logger.info("Need to approve more collateral.")
            approve_tx = self.web3_client.create_approval(
                contract=contract,
                spender=self.web3_client.option_exchange.address,
                owner=self._crypto.address,
                amount=amount_to_approve,
            )

            self._logger.debug(f"Approve tx is {approve_tx}")
            tx_hash = self._sign_and_sumbit(approve_tx)
            self._logger.info(f"Tx hash is {tx_hash}")

        # has allowcance incremented
        allowance = contract.functions.allowance(
            self._crypto.address,
            self.web3_client.option_exchange.address,
        ).call()
        self._logger.info(f"Allowance is {allowance}")
        otoken_address = self.web3_client.get_otoken(rysk_option_market.to_series())

        operate_tuple = sell(
            int(acceptable_premium * 0.95 * 1e2),
            owner_address=self._crypto.address,  # pylint: disable=E1120
            exchange_address=self.web3_client.option_exchange.address,
            otoken_address=otoken_address,
            amount=int(_amount),
            vault_id=int(vault_id),
            collateral=_amount,
            rysk_option_market=rysk_option_market,
            issue_new_vault=issue_new_vault,
        )
        if self._verbose:
            self._logger.info("Operate tuple is:")
            print_operate_tuple(operate_tuple)

        operate_txn = self.web3_client.option_exchange.functions.operate(
            operate_tuple
        ).build_transaction(
            {
                **{
                    "from": self._crypto.address,
                },
                **self.web3_client._default_tx_params,  # pylint: disable=W0212
            }
        )
        return operate_txn

    def watch_trades(self):
        """Watch trades."""
        self._logger.info("Watching trades...")
        self.web3_client.watch_trades()

    def fetch_balances(self):
        """Fetch balances."""
        self._logger.info("Fetching balances...")
        return self.web3_client.get_balances()

    def settle_vault(self, vault_id):
        """Settle options."""
        self._logger.info(f"Settling vault {vault_id}...")
        txn = self.web3_client.settle_vault(vault_id=vault_id)
        return self._sign_and_sumbit(txn)

    def redeem_otoken(self, otoken_id: str, amount: int):
        """Redeem otoken."""
        self._logger.info(f"Redeeming otoken {otoken_id}...")
        txn = self.web3_client.redeem_otoken(otoken_id=otoken_id, amount=amount)
        return self._sign_and_sumbit(txn)

    def redeem_market(self, market: str):
        """Redeem otoken."""
        self._logger.info(f"Redeeming market {market}...")
        rysk_option_market = RyskOptionMarket.from_str(market)
        otoken_address = self.web3_client.get_otoken(rysk_option_market.to_series())
        amount = self.web3_client.get_otoken_balance(otoken_address) / 10**8
        return self.redeem_otoken(otoken_address, amount)

    @property
    def active_markets(self):
        """Get active markets."""
        if not self._markets:
            self.fetch_markets()
        return {market.name: market for market in self._markets}

    def close_long(self, market: str, size: float):
        """Close long."""
        self._logger.info(f"Closing long {market}...")
        # as we are long, we use usdc as collateral
        collateral_asset = Collateral.USDC
        _market = self.get_market(market)
        _market.collateral = collateral_asset
        otoken_address = self.web3_client.get_otoken(_market.to_series())
        if size is None:
            _amount = self.web3_client.get_otoken_balance(otoken_address) * 10**10
        else:
            _amount = size * 1e18
        if _market.name not in self.active_markets:
            raise ValueError(f"{market} is not an active market...")
        acceptable_premium = int(_market.ask * (1 - ALLOWED_SLIPPAGE))
        # we check the approval
        otoken_contract = self.web3_client.get_otoken_contract(otoken_address)

        # we get the balance
        balance = self.web3_client.get_otoken_balance(otoken_address)

        self._logger.info(f"Balance for {market} is {balance / 10**8}")

        if balance == 0:
            raise ValueError(f"Nothing to close for {market}...")

        if not self.web3_client.is_approved(
            otoken_contract,
            self.web3_client.option_exchange.address,
            self._crypto.address,
            int(10**8 * _amount),
        ):
            self._logger.info(f"Approving {market}...")
            txn = self.web3_client.create_approval(
                otoken_contract,
                self.web3_client.option_exchange.address,
                self._crypto.address,  # type: ignore
                int(10**8 * _amount),
            )
            self._sign_and_sumbit(
                txn,
            )

        if _amount == 0:
            raise ValueError(f"Nothing to close for {market}...")

        txn = self.web3_client.close_long(
            acceptable_premium=acceptable_premium,
            amount=_amount,
            otoken_address=self.web3_client.web3.toChecksumAddress(otoken_address),
        )
        return self._sign_and_sumbit(txn)

    def close_short(self, market: str, size: float):
        """
        CLose short.
        """
        self._logger.info(f"Closing short {market}...")
        # as we are short, we ensure we are covered
        rysk_option_market = self.active_markets[market]
        otoken_address = self.web3_client.get_otoken(rysk_option_market.to_series())

        if size is None:
            raise NotImplementedError(
                "Closing short with no size is not implemented yet"
            )
        _amount = size * 1e18
        if rysk_option_market.name not in self.active_markets:
            raise ValueError(f"{market} is not an active market...")
        acceptable_premium = int(rysk_option_market.bid * (1 + ALLOWED_SLIPPAGE) * size)

        user_vaults = self.web3_client.fetch_user_vaults(self._crypto.address)
        otoken_id = self.web3_client.get_otoken(rysk_option_market.to_series())
        self._logger.info(f"Option Otoken id is {otoken_id}")

        positions = [f for f in user_vaults if f[1] == otoken_id]
        if len(positions) == 0:
            raise ValueError(f"Nothing to close for {market}...")
        if len(positions) > 1:
            raise ValueError(f"Multiple positions for {market}...")
        vault_id = positions[0][0]

        txn = self.web3_client.close_short(
            acceptable_premium=acceptable_premium,
            amount=int(_amount),
            otoken_address=self.web3_client.web3.toChecksumAddress(otoken_address),
            collateral_asset=rysk_option_market.collateral,
            collateral_amount=int(_amount),
            vault_id=vault_id,
            rysk_option_market=rysk_option_market,
        )
        return self._sign_and_sumbit(txn)
