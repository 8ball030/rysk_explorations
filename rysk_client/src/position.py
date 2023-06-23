"""
Module to manage positions.
"""
from dataclasses import dataclass
from typing import List, Optional

from rysk_client.src.collateral import Collateral
from rysk_client.src.order import Order
from rysk_client.src.position_side import PositionSide
from rysk_client.src.rysk_option_market import RyskOptionMarket


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
