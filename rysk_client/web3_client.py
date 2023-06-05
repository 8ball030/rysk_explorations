"""
Web3 client for RyskFinance.
"""
import json
import logging
from collections import deque
from enum import Enum
from typing import Any, Dict, Optional, Tuple

import websocket
from web3.contract import Contract

from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import WSS_URL
from rysk_client.src.position import Order, OrderSide
from rysk_client.src.utils import get_contract, get_logger, get_web3


class Balances(Enum):
    """
    Class to represent the balances of an address.
    """


class Web3Client:
    """Client for the RyskFinance protocol."""

    beyond_pricer: Contract
    opyn_controller: Contract
    option_exchange: Contract

    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the client with the web3 provider.
        """
        self.web3 = get_web3()
        self.beyond_pricer = get_contract("beyond_pricer", self.web3)
        self.opyn_controller = get_contract("opyn_controller", self.web3)
        self.option_exchange = get_contract("option_exchange", self.web3)
        self._logger = logger or get_logger()
        self._processed_tx: deque = deque(maxlen=100)

    def get_options_prices(
        self,
        option_data,
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

        if not Collateral.is_supported(collateral):
            raise TypeError(f"Collateral {collateral} is not supported")
        # here we call the contract functions

        option_series = (
            int(option_data["expiration"]),
            int(option_data["strike"]),
            bool(option_data["isPut"]),
            Collateral.from_symbol(collateral).value,
            Collateral.from_symbol(strike_asset).value,
            Collateral.from_symbol(strike_asset).value,
        )

        try:
            result = self.beyond_pricer.functions.quoteOptionPrice(
                option_series,
                int(amount),
                side == "sell",
                int(option_data["netDHVExposure"]),
            ).call()
        except Exception as error:  # pylint: disable=broad-except
            self._logger.error(
                f"Error calling beyond pricer: {error} with {option_series}"
            )

            return 0
        return result[0] / 1_000_000

    def get_balances(self):
        """
        Get the balances for an address
        """
        raise NotImplementedError

    def fetch_ticker(self, market: Dict[str, Any]) -> Dict[str, Any]:
        """
        interact with the web3 api to fetch the ticker data
        """
        ask = self.get_options_prices(market["info"])
        bid = self.get_options_prices(market["info"], side="sell")
        return {
            "ask": ask,
            "bid": bid,
            "info": market,
            "symbol": market["symbol"],
            "expiration": market["info"]["expiration"],
        }

    def watch_trades(self):
        """
        Subscribe to boeht pending trades and completed trades.
        """
        ws_connection = websocket.WebSocketApp(
            WSS_URL,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        ws_connection.run_forever()

    def on_message(self, websocket, message): # pylint: disable=unused-argument
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

        except Exception as exc:  # pylint: disable=W0718,W0705
            self._logger.error(
                f"An exception occurred while trying to get the transaction arguments for {tx_receipt}: {exc}"
            )
            return {}, True
