"""
Rysk Client Operation Manager
"""


from enum import Enum

from rysk_client.src.action_type import ActionType, RyskActionType
from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import NULL_ADDRESS, NULL_DATA
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
    issuance_required: bool = False,
):
    """Create the operation to buy an option."""
    operations = []

    if issuance_required:
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


EMPTY_SERIES = {
    "expiration": 1,
    "strike": 1,
    "isPut": True,
    "collateral": NULL_ADDRESS,
    "underlying": NULL_ADDRESS,
    "strikeAsset": NULL_ADDRESS,
}


def close_long(
    acceptable_premium: int,
    owner_address: str,
    otoken_address: str,
    amount: int,
):
    """Create the operation to buy an option."""
    return [
        {
            "operation": OperationType.RYSK_ACTION.value,
            "operationQueue": [
                {
                    "actionType": RyskActionType.CLOSE_OPTION.value,
                    "owner": NULL_ADDRESS,
                    "secondAddress": owner_address,
                    "asset": otoken_address,
                    "vaultId": 0,
                    "amount": amount,
                    "optionSeries": EMPTY_SERIES,
                    "indexOrAcceptablePremium": acceptable_premium,
                    "data": NULL_DATA,
                }
            ],
        }
    ]


def from_wei_to_opyn(amount: int):
    """Convert amount from wei to opyn."""
    return int(amount / 10**10)


def sell(
    acceptable_premium: int,
    owner_address: str,
    exchange_address: str,
    otoken_address: str,
    amount: int,
    vault_id: int,
    collateral: int,
    rysk_option_market: RyskOptionMarket = None,
):
    """Create the operation to sell an option."""
    if rysk_option_market.is_put:
        # here we retrieve how much collateral we get for the amount of options
        # we basically need strike * amount
        eth = collateral / 1e18
        strike = rysk_option_market.strike / 1e18
        _amount = from_wei_to_opyn(amount) / 1e2
        collateral_amount = int(eth * strike * _amount)
        collateral = Collateral.USDC.value

    else:
        collateral_amount = amount
        collateral = Collateral.WETH.value

    required_data = [
        {
            "actionType": ActionType.DEPOSIT_COLLATERAL.value,
            "owner": owner_address,
            "secondAddress": exchange_address,
            "asset": collateral,
            "vaultId": vault_id,
            "amount": collateral_amount,
            "optionSeries": EMPTY_SERIES,
            "indexOrAcceptablePremium": 0,
            "data": NULL_DATA,
        },
        {
            "actionType": ActionType.MINT_SHORT_OPTION.value,
            "owner": owner_address,
            "secondAddress": exchange_address,
            "asset": otoken_address,
            "vaultId": vault_id,
            "amount": from_wei_to_opyn(amount),
            "optionSeries": EMPTY_SERIES,
            "indexOrAcceptablePremium": 0,
            "data": NULL_DATA,
        },
    ]
    if vault_id == 0:
        # we need to open a vault
        required_data = [
            {
                "actionType": ActionType.OPEN_VAULT.value,
                "owner": owner_address,
                "secondAddress": owner_address,
                "asset": NULL_ADDRESS,
                "vaultId": vault_id,
                "amount": 0,
                "optionSeries": EMPTY_SERIES,
                "indexOrAcceptablePremium": 0,
                "data": NULL_DATA,
            }
        ] + required_data
    return [
        {
            "operation": OperationType.OPYN_ACTION.value,
            "operationQueue": required_data,
        },
        {
            "operation": OperationType.RYSK_ACTION.value,
            "operationQueue": [
                {
                    "actionType": RyskActionType.SELL_OPTION.value,
                    "owner": NULL_ADDRESS,
                    "secondAddress": owner_address,
                    "asset": NULL_ADDRESS,
                    "vaultId": 0,
                    "amount": amount,
                    "optionSeries": {
                        "expiration": rysk_option_market.expiration,
                        "strike": rysk_option_market.strike,
                        "isPut": rysk_option_market.is_put,
                        "underlying": Collateral.WETH.value,
                        "strikeAsset": Collateral.USDC.value,
                        "collateral": Collateral.WETH.value
                        if not rysk_option_market.is_put
                        else Collateral.USDC.value,
                    },
                    "indexOrAcceptablePremium": int(acceptable_premium * 1e-2),
                    "data": NULL_DATA,
                }
            ],
        },
    ]
