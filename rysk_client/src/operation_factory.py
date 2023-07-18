"""
Rysk Client Operation Manager
"""


from dataclasses import dataclass
from enum import Enum

from rysk_client.src.action_type import ActionType, RyskActionType
from rysk_client.src.collateral import CollateralFactory
from rysk_client.src.constants import (EMPTY_SERIES, NULL_ADDRESS, NULL_DATA,
                                       WETH_MULTIPLIER, Chain)
from rysk_client.src.rysk_option_market import MarketFactory, RyskOptionMarket
from rysk_client.src.utils import from_wei_to_opyn


class OperationType(Enum):
    """Distinguish between operations for the rysk and opyn contracts."""

    OPYN_ACTION = 0
    RYSK_ACTION = 1


@dataclass
class OperationFactory:
    """Create operations for the rysk and opyn contracts."""

    chain: Chain

    def __init__(self, chain: Chain):
        self.chain = chain
        self.collateral_factory = CollateralFactory(chain)
        self.market_factory = MarketFactory(chain)

    def buy(
        self,
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
                    "optionSeries": self.market_factory.to_series(option_market),
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
                "optionSeries": self.market_factory.to_series(option_market),
                "indexOrAcceptablePremium": acceptable_premium,
                "data": NULL_ADDRESS,
            }
        )
        return {
            "operation": OperationType.RYSK_ACTION.value,
            "operationQueue": operations,
        }

    def close_long(
        self,
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

    def sell(
        self,
        acceptable_premium: int,
        owner_address: str,
        exchange_address: str,
        otoken_address: str,
        amount: int,
        vault_id: int,
        collateral: int,
        rysk_option_market: RyskOptionMarket,
        issue_new_vault: bool = False,
    ):
        """Create the operation to sell an option."""
        if rysk_option_market.is_put:
            # here we retrieve how much collateral we get for the amount of options
            # we basically need strike * amount
            eth = collateral / WETH_MULTIPLIER
            strike = rysk_option_market.strike / WETH_MULTIPLIER
            _amount = from_wei_to_opyn(amount) / 1e2
            collateral_amount = int(eth * strike * _amount)
            collateral = self.collateral_factory.USDC

        else:
            collateral_amount = amount
            collateral = self.collateral_factory.WETH

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
        if issue_new_vault:
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
                            "expiration": int(rysk_option_market.expiration),
                            "strike": int(rysk_option_market.strike),
                            "isPut": rysk_option_market.is_put,
                            "underlying": self.collateral_factory.WETH,
                            "strikeAsset": self.collateral_factory.USDC,
                            "collateral": self.collateral_factory.WETH
                            if not rysk_option_market.is_put
                            else self.collateral_factory.USDC,
                        },
                        "indexOrAcceptablePremium": int(acceptable_premium),
                        "data": NULL_DATA,
                    }
                ],
            },
        ]

    def close_short(
        self,
        acceptable_premium: int,
        owner_address: str,
        otoken_address: str,
        amount: int,
        collateral_amount: int,
        collateral_asset: str,
        vault_id: int,
        rysk_option_market: RyskOptionMarket,
    ):
        """
        Create the operation to close a short options
        """
        if rysk_option_market.is_put:
            # here we retrieve how much collateral we get for the amount of options
            # we basically need strike * amount
            eth = collateral_amount / WETH_MULTIPLIER
            strike = rysk_option_market.strike / WETH_MULTIPLIER
            _amount = from_wei_to_opyn(amount) / 1e2
            collateral_amount = int(eth * strike * _amount)

        tx_data = [
            {
                "operation": OperationType.RYSK_ACTION.value,
                "operationQueue": [
                    {
                        "actionType": RyskActionType.BUY_OPTION.value,
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
            },
            {
                "operation": OperationType.OPYN_ACTION.value,
                "operationQueue": [
                    {
                        "actionType": ActionType.BURN_SHORT_OPTION.value,
                        "owner": owner_address,
                        "secondAddress": owner_address,
                        "asset": otoken_address,
                        "vaultId": vault_id,
                        "amount": from_wei_to_opyn(amount),
                        "optionSeries": EMPTY_SERIES,
                        "indexOrAcceptablePremium": 0,
                        "data": NULL_DATA,
                    },
                    {
                        "actionType": ActionType.WITHDRAW_COLLATERAL.value,
                        "owner": owner_address,
                        "secondAddress": owner_address,
                        "asset": collateral_asset,
                        "vaultId": vault_id,
                        "amount": collateral_amount,
                        "optionSeries": EMPTY_SERIES,
                        "indexOrAcceptablePremium": 0,
                        "data": NULL_DATA,
                    },
                ],
            },
        ]
        return tx_data
