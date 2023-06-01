from dataclasses import dataclass
from enum import Enum
from typing import Dict

from ryk_client.src.collateral import Collateral
from ryk_client.src.rysk_option_market import RyskOptionMarket


class OrderSide(Enum):
    buy = "buy"
    sell = "sell"


class Order:
    """Class to represent an order"""

    price: float
    amount: float
    order_id: str
    order_side: OrderSide
    order_type: str = "market"


class PositionSide(Enum):
    long = "long"
    short = "short"


@dataclass
class Position:
    side: PositionSide
    size: float = 0
    pnl: float = 0
    collateral: str = "usdc"
    option_market: RyskOptionMarket
    orders: List[Order]


class PositionManager:
    positions: Dict[str, Position]
    collateral: Dict[str, float]

    def __init__(self):
        self.positions = {}
        self.collateral = {}
        self.pnl = {}
        self.collateral_value = 0
        self.collateral_value_usd = 0

    def add_position(self, position: Position):
        """Adds a position to the position manager"""

    def add_order(self, order: Order):
        """Adds an order to the position manager"""

    def update_position(self, position: Position):
        """Updates a position in the position manager"""

    def update_order(self, order: Order):
        """Updates an order in the position manager"""

    def get_positions(self, address: str) -> List[Position]:
        """Returns a list of positions"""
        return self.positions

    def _fetch_positions(self):
        """Fetches the positions from the API"""
        pass

    def _fetch_orders(self):
        """Fetches the orders from the API"""
        pass
