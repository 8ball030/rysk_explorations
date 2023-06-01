"""
Web3 client for RyskFinance.
"""
from web3 import Web3, contract

from rysk_client.src.collateral import Collateral
from rysk_client.src.utils import get_contract, get_web3

w3 = Web3(Web3.HTTPProvider("https://arbitrum-goerli.rpc.thirdweb.com"))

addresses = {
    "beyond_pricer": {
        "path": "./contracts/BeyondPricer.sol/BeyondPricer.json",
        "address": "0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259",
    },
    "opyn_controller": {
        "path": "contracts/packages/opyn/core/Controller.sol/Controller.json",
        "address": "0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2",
    },
    "option_exchange": {
        "path": "contracts/OptionExchange.sol/OptionExchange.json",
        "address": "",
    },
}


def filter_by_human_format(data_frame, human_format):
    """
    Filter the DataFrame based on the human-readable format and return a single row.
    """

    filtered_option = data_frame[data_frame["human_strike"] == human_format]
    if len(filtered_option) > 0:
        return filtered_option.iloc[0]  # Return the first row if found
    return None  # Return None if no matching row is found


class Web3Client:
    """Client for the RyskFinance protocol."""

    beyond_pricer: contract.Contract = get_contract("beyond_pricer", get_web3())
    opyn_controller: contract.Contract = get_contract("opyn_controller", get_web3())

    def get_options_prices(
        self, option_data, amount=1000000000000000000, side="buy", collateral="weth"
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
            "0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3",
            "0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d",
            "0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d",
        )
        result = self.beyond_pricer.functions.quoteOptionPrice(
            option_series,
            int(amount),
            side == "sell",
            int(option_data["netDHVExposure"]),
        ).call()
        return result[0] / 1_000_000

    def get_positions(self, address):
        """
        Get the positions for an address
        """
        return self.opyn_controller.functions.getAccountPositions(address).call()
