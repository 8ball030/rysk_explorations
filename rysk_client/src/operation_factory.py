"""
Rysk Client Operation Manager
"""


from enum import Enum

from rysk_client.src.action_type import RyskActionType
from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import NULL_ADDRESS
from rysk_client.src.rysk_option_market import RyskOptionMarket


class OperationType(Enum):
    """Distinguish between operations for the rysk and opyn contracts."""

    OPYN_ACTION = 0
    RYSK_ACTION = 1


def buy(
    acceptable_premium: int,
    owner_address: str,
    amount: int,
    option_market: RyskOptionMarket,
):
    """Create the operation to buy an option."""
    collateral = Collateral.USDC if option_market.is_put else Collateral.WETH
    operations = []
    if collateral != Collateral.WETH:
        operations.append(
            {
                "actionType": RyskActionType.ISSUE.value,
                "owner": NULL_ADDRESS,
                "secondAddress": NULL_ADDRESS,
                "asset": NULL_ADDRESS,
                "vaultId": 0,
                "amount": 0,
                "optionSeries": option_market.to_series(),
                "indexOrAcceptablePremium": 0,
                "data": NULL_ADDRESS,
            }
        )
    operations.append(
        {
            "actionType": RyskActionType.BUY_OPTION.value,
            "owner": NULL_ADDRESS,
            "secondAddress": owner_address,
            "asset": NULL_ADDRESS,
            "vaultId": 0,
            "amount": amount,
            "optionSeries": option_market.to_series(),
            "indexOrAcceptablePremium": acceptable_premium,
            "data": NULL_ADDRESS,
        }
    )
    return {
        "operation": OperationType.RYSK_ACTION.value,
        "operationQueue": operations,
    }
