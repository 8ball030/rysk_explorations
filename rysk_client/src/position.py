"""
Module to manage positions.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

from rysk_client.src.collateral import Collateral
from rysk_client.src.rysk_option_market import RyskOptionMarket


class OrderSide(Enum):
    """Enum to represent the side of an order."""

    BUY = "buy"
    SELL = "sell"


@dataclass
class Order:
    """Class to represent an order"""

    price: float
    amount: float
    order_id: str
    order_side: OrderSide
    order_type: str = "market"

    def __str__(self) -> str:
        return f"Order({self.order_side}, {self.amount}, {self.price})"

    def __repr__(self) -> str:
        return self.__str__()


class PositionSide(Enum):
    """Enum to represent the side of a position."""

    LONG = "long"
    SHORT = "short"


@dataclass
class Position:
    """Class to represent a position."""

    option_market: RyskOptionMarket
    orders: List[Order]
    side: PositionSide
    size: float = 0
    pnl: float = 0
    collateral: Collateral = Collateral.USDC
    owner_address: Optional[str] = None


class PositionManager:
    """Class to manage positions"""

    positions: List[Position]
    collateral: Dict[str, float]

    def __init__(self):
        self.positions = []
        self.collateral = {}
        self.pnl = {}
        self.collateral_value = 0
        self.collateral_value_usd = 0

    def add_position(self, position: Position):
        """Adds a position to the position manager"""

    def update_position(self, position: Position):
        """Updates a position in the position manager"""

    def get_positions(self, address: Optional[str] = None) -> List[Position]:
        """Returns a list of positions"""
        if address:
            return [
                position
                for position in self.positions
                if position.owner_address == address
            ]
        return self.positions

    def _fetch_positions(self):
        """Fetches the positions from the API"""

    def _fetch_orders(self):
        """Fetches the orders from the API"""
