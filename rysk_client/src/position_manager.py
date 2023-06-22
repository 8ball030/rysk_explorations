"""
Position Manager
"""
from typing import Dict, List, Optional

from rysk_client.src.position import Position


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
