"""
Collateral supported by the protocol.
"""
from enum import Enum

from web3 import Web3


class Collateral(Enum):
    """Collateral supported by the protocol"""

    WETH = Web3.toChecksumAddress("0x3b3a1de07439eeb04492fa64a889ee25a130cdd3")
    USDC = Web3.toChecksumAddress("0x408c5755b5c7a0a28d851558ea3636cfc5b5b19d")

    @classmethod
    def is_supported(cls, collateral):
        """Is the sset supported"""
        try:
            cls.from_symbol(collateral)
        except ValueError:
            return False
        return True

    @classmethod
    def from_symbol(cls, symbol):
        """Returns the address of the collateral from its symbol"""
        if symbol.upper() == "WETH":
            return cls.WETH
        if symbol.upper() == "USDC":
            return cls.USDC
        raise ValueError(f"Collateral {symbol} not supported")
