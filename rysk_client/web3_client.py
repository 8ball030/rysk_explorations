"""
Web3 client for RyskFinance.
"""
from enum import Enum
from typing import Any, Dict

from web3 import Web3, contract

from rysk_client.src.collateral import Collateral
from rysk_client.src.utils import get_contract, get_logger, get_web3

w3 = Web3(Web3.HTTPProvider("https://arbitrum-goerli.rpc.thirdweb.com"))


class Balances(Enum):
    """
    Class to represent the balances of an address.
    """


class Web3Client:
    """Client for the RyskFinance protocol."""

    beyond_pricer: contract.Contract
    opyn_controller: contract.Contract
    option_exchange: contract.Contract

    def __init__(self):
        """
        Initialize the client with the web3 provider.
        """
        self.web3 = get_web3()
        self.beyond_pricer = get_contract("beyond_pricer", self.web3)
        self.opyn_controller = get_contract("opyn_controller", self.web3)
        self.option_exchange = get_contract("option_exchange", self.web3)
        self.logger = get_logger()

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
            self.logger.error(
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
