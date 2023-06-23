"""
Rysk Client Operation Manager
"""

import logging
from typing import Optional

import pytest

from rysk_client.src.action_type import ActionType
from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import NULL_ADDRESS
from rysk_client.src.order import Order
from rysk_client.src.order_side import OrderSide
from rysk_client.src.position import Position
from rysk_client.src.position_side import PositionSide
from rysk_client.src.rysk_option_market import RyskOptionMarket
from rysk_client.src.utils import get_logger


def does_otoken_exist(rysk_option_market: RyskOptionMarket, collateral: Collateral):
    """
    Check if an otoken exists for a given collateral
    """
    print(rysk_option_market)
    print(collateral)
    raise NotImplementedError


class Operation:
    """
    Operation to be executed by the client
    """

    def __init__(self, action_type: ActionType, collateral: Collateral):
        self.action_type = action_type
        self.collateral = collateral

        self.owner = NULL_ADDRESS

    def to_json(self):
        """Convert the operation to json"""
        return {
            "operation": self.action_type.value,
            "operationQueue": {
                "actionType": self.action_type.value,
                "owner": self.action_type.value,
            },
        }


class OperationFactory:
    """
    Create the operations to be executed by the client
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the operation factory"""
        self.logger = logger or get_logger()

    def create_operation_tuple(
        self,
        collateral: Collateral,
        order: Order,
        position: Position,
        option_market: RyskOptionMarket,
    ):
        """Create an operation"""
        # if we are long and and we are buying we need to increase the position;
        queue = OperationQueue()

        if position.size == 0:
            self.logger.info(f"Creating new position for {option_market} {order}")
            # The buy operation queue consists of an issue and then a buy.
            # The issue action is to create the oToken if it doesn’t already exist,
            # as well as add it to the options registry storage.
            # If the oToken already exists, we just run the buy which mints the oTokens
            # for sending to you.
            if order.order_side == OrderSide.BUY:
                # we need to check if we need to issue the option
                if not does_otoken_exist(option_market, collateral):
                    queue.add_operation(Operation(ActionType.OPEN_VAULT, collateral))
                queue.add_operation(
                    Operation(ActionType.DEPOSIT_LONG_OPTION, collateral)
                )

            else:
                # Issuance isn’t required for selling.
                # We simply get the oToken address and then check to see if you already have a matching vault
                # for that address.
                # If you have a vault, the operation queue consists of a deposit and then mint short
                # on the Opyn side, followed by a sell action on the Rysk side.
                # If you do not have a vault,
                # we prepend the Opyn queue with an action to open a new vault.
                if not does_otoken_exist(option_market, collateral):
                    queue.add_operation(Operation(ActionType.OPEN_VAULT, collateral))
                queue.add_operation(
                    Operation(ActionType.DEPOSIT_COLLATERAL, collateral)
                )
                queue.add_operation(Operation(ActionType.MINT_SHORT_OPTION, collateral))

        # increase the existing positions
        if any(
            [
                (position.size < 0 and order.order_side == OrderSide.SELL),
                (position.size > 0 and order.order_side == OrderSide.BUY),
            ]
        ):
            self.logger.info(f"Increasing position for {option_market} {order}")
            # Longs
            # At this point, the oToken has already been issued so we simply operate a buy action.
            # In our code though, we re-use the same buy queue for issued and unissued as the issue
            # is just skipped when not required.
            if position.side == PositionSide.LONG:
                queue.add_operation(
                    Operation(ActionType.DEPOSIT_LONG_OPTION, collateral)
                )

            # Shorts
            # As mentioned above, we will see that you have a vault already,
            # run the Opyn deposit and mint actions and then the Rysk sell action.
        return queue.to_json()


class OperationQueue:
    """
    Manage the operations to be executed by the client
    """

    def __init__(self):
        """Initialize the operation queue."""
        self.operations = []

    def add_operation(self, operation: Operation):
        """add an operation to the queue"""
        self.operations.append(operation)

    def get_operations(self):
        """get the operations in the queue"""
        return self.operations

    @classmethod
    def from_json(cls, json):
        """Create an OperationQueue from a JSON object"""
        queue = cls()
        for operation in json:
            queue.add_operation(Operation(**operation))
        return queue

    def to_json(self):
        """Create a JSON object from an OperationQueue"""
        return [operation.__dict__ for operation in self.operations]


@pytest.fixture
def operation_factory():
    """Create an operation factory."""
    return OperationFactory()


@pytest.fixture
def option_market():
    """Create an option market."""
    return RyskOptionMarket(
        strike=100,
        expiration=100,
        is_put=True,
    )


@pytest.fixture
def order():
    """Create an order."""
    return Order(
        price=100,
        amount=100,
        order_id="test",
        order_side=OrderSide.BUY,
    )


@pytest.fixture
def position(option_market):
    """Create a position."""
    return Position(option_market, [], PositionSide.LONG)


POSITION_SIDES = [PositionSide.LONG, PositionSide.SHORT]
ORDER_SIDES = [OrderSide.BUY, OrderSide.SELL]


@pytest.mark.parametrize("position_side", POSITION_SIDES)
@pytest.mark.parametrize("order_side", ORDER_SIDES)
def test_create_long_short(
    operation_factory: OperationFactory,
    position: Position,
    order: Order,
    option_market: RyskOptionMarket,
    position_side: PositionSide,
    order_side: OrderSide,
):
    """Test that we can create a long / short position."""
    position.side = position_side
    order.order_side = order_side
    position.size += order.amount if order_side == OrderSide.BUY else -order.amount
    operation_tuple = operation_factory.create_operation_tuple(
        Collateral.USDC, order, position, option_market
    )
    # we check this valid on the chain
    assert operation_tuple[0] == ActionType.OPEN_VAULT


# we test that we can create an operation that increases long / short positions
@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("position_side", POSITION_SIDES)
@pytest.mark.parametrize("order_side", ORDER_SIDES)
def test_create_operation_increase_long_short(
    operation_factory, position, order, option_market, position_side, order_side
):
    """Test that we can create an operation that increases long / short positions."""
    position.side = position_side
    order.order_side = order_side
    position.size = 1
    operation_tuple = operation_factory.create_operation(
        Collateral.USDC, order, position, option_market
    )
    # we check this valid on the chain
    assert operation_tuple[0] == ActionType.DEPOSIT_LONG_OPTION


#


class OperateTxArgs:
    """Operation arguments for a transaction."""

    def __init__(self, tx_args):
        self.tx_args = tx_args

    def from_raw_args(self):
        """Create an OperateTxArgs from raw args"""
        return OperateTxArgs.from_raw_args(self.tx_args)

    def to_raw_args(self):
        """Create raw args from OperateTxArgs"""
        return self.tx_args
