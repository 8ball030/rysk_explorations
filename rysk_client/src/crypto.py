"""
Crypto module.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class EthCrypto:
    """Represents a crypto wallet."""

    address: Optional[str]
    private_key: Optional[str]
