from enum import Enum

from web3 import Web3


class Collateral(Enum):
    weth = Web3.toChecksumAddress("0x3b3a1de07439eeb04492fa64a889ee25a130cdd3")
    usdc = Web3.toChecksumAddress("0x408c5755b5c7a0a28d851558ea3636cfc5b5b19d")

    @classmethod
    def is_supported(cls, collateral):
        """Is the sset supported"""
        try:
            cls(collateral)
        except ValueError:
            return False
        return True

    @classmethod
    def from_symbol(cls, symbol):
        """Returns the address of the collateral from its symbol"""
        if symbol == "weth":
            return cls.weth
        elif symbol == "usdc":
            return cls.usdc
        else:
            raise ValueError("Collateral not supported")
