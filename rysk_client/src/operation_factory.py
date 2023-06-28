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
    return amount / 10**8


def sell(
    acceptable_premium: int,
    owner_address: str,
    exchange_address: str,
    otoken_address: str,
    amount: int,
    vault_id: int,
    collateral: int,
):
    """Create the operation to sell an option.

          {
        actionType: BigNumber.from(OpynActionType.DepositCollateral),
        owner: addresses.user,
        secondAddress: addresses.exchange,
        asset: addresses.token,
        vaultId,
        amount: collateral,
        optionSeries: EMPTY_SERIES,
        indexOrAcceptablePremium: BigNumber.from(0),
        data: ZERO_ADDRESS,
      },
      {
        actionType: BigNumber.from(OpynActionType.MintShortOption),
        owner: addresses.user,
        secondAddress: addresses.exchange,
        asset: oTokenAddress,
        vaultId,
        amount: fromWeiToOpyn(amount),
        optionSeries: EMPTY_SERIES,
        indexOrAcceptablePremium: BigNumber.from(0),
        data: ZERO_ADDRESS,
      },
    ];
        const vaultId = hasVault
      ? BigNumber.from(vaults[vaultKey])
      : BigNumber.from(vaults.length + 1);

    const openVaultData = {
      actionType: BigNumber.from(OpynActionType.OpenVault),
      owner: addresses.user,
      secondAddress: addresses.user,
      asset: ZERO_ADDRESS,
      vaultId,
      amount: BigNumber.from(0),
      optionSeries: EMPTY_SERIES,
      indexOrAcceptablePremium: BigNumber.from(0),
      data: utils.hexZeroPad(
        utils.hexlify([OpenVaultCollateralType.Partially]),
        32
      ) as HexString,
    };

      const txData = [
      {
        operation: OperationType.OpynAction,
        operationQueue: hasVault
          ? requiredData
          : [openVaultData, ...requiredData],
      },
      {
        operation: OperationType.RyskAction,
        operationQueue: [
          {
            actionType: BigNumber.from(RyskActionType.SellOption),
            owner: ZERO_ADDRESS,
            secondAddress: addresses.user,
            asset: ZERO_ADDRESS,
            vaultId: BigNumber.from(0),
            amount,
            optionSeries,
            indexOrAcceptablePremium: acceptablePremium,
            data: ZERO_ADDRESS,
          },
        ],
      },
    ];


    """
    required_data = [
        {
            "actionType": ActionType.DEPOSIT_COLLATERAL.value,
            "owner": owner_address,
            "secondAddress": exchange_address,
            "asset": otoken_address,
            "vaultId": vault_id,
            "amount": collateral,
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
                    "optionSeries": EMPTY_SERIES,
                    "indexOrAcceptablePremium": acceptable_premium,
                    "data": NULL_DATA,
                }
            ],
        },
    ]
