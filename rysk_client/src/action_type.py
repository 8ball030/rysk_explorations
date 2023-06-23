"""
This file contains the ActionType enum, which is used to specify the type of action to be performed by the client.
"""
from enum import Enum


class ActionType(Enum):
    """Enum to specify the type of action to be performed by the client."""

    OPEN_VAULT = 0
    MINT_SHORT_OPTION = 1
    BURN_SHORT_OPTION = 2
    DEPOSIT_LONG_OPTION = 3
    WITHDRAW_LONG_OPTION = 4
    DEPOSIT_COLLATERAL = 5
    WITHDRAW_COLLATERAL = 6
    SETTLE_VAULT = 7
    REDEEM = 8
    CALL = 9
    LIQUIDATE = 10


class RyskActionType(Enum):
    """
    Enum to specify the type of action to be performed by the client.
    """

    ISSUE = 0
    BUY_OPTION = 1
    SELL_OPTION = 2
    CLOSE_OPTION = 3
