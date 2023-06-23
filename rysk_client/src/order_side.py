"""
This module contains the OrderSide enum.
"""

from enum import Enum


class OrderSide(Enum):
    """Enum to represent the side of an order."""

    BUY = "buy"
    SELL = "sell"
