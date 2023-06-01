from enum import Enum


class ActionType(Enum):
    OpenVault = 0
    MintShortOption = 1
    BurnShortOption = 2
    DepositLongOption = 3
    WithdrawLongOption = 4
    DepositCollateral = 5
    WithdrawCollateral = 6
    SettleVault = 7
    Redeem = 8
    Call = 9
    Liquidate = 10
