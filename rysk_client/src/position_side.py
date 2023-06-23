"""
This module contains the PositionSide enum.
"""
from enum import Enum


class PositionSide(Enum):
    """Enum to represent the side of a position."""

    LONG = "long"
    SHORT = "short"
