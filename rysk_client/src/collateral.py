"""
Collateral supported by the protocol.
"""
from dataclasses import dataclass

from rysk_client.src.constants import PROTOCOL_DEPLOYMENTS, Chain


@dataclass
class CollateralFactory:
    """Class to return the collateral enum from the deployment."""

    chain: Chain

    @property
    def WETH(self):  # pylint: disable=invalid-name
        """Returns the WETH address"""
        return PROTOCOL_DEPLOYMENTS[self.chain.name].contracts["weth"].address

    @property
    def USDC(self):  # pylint: disable=invalid-name
        """Returns the USDC address"""
        return PROTOCOL_DEPLOYMENTS[self.chain.name].contracts["usdc"].address

    def from_symbol(self, symbol):
        """Returns the address of the collateral from its symbol"""
        if symbol.upper() == "WETH":
            return self.WETH
        if symbol.upper() == "USDC":
            return self.USDC
        raise ValueError(f"Collateral {symbol} not supported")

    def is_supported(self, collateral):
        """Is the sset supported"""
        try:
            self.from_symbol(collateral)
        except ValueError:
            return False
        return True
