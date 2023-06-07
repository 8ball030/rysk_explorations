"""
Tests for the PNL calculation.
"""

import pytest

from rysk_client.src.pnl_calculator import PnlCalculator, Trade


@pytest.fixture
def pnl_calculator():
    """Returns a PnlCalculator instance."""
    return PnlCalculator()


def test_pnl_calculator_nets_to_zero(pnl_calculator):
    """We make a buy and a sell order, and check the pnl"""
    buy_trade = Trade(quantity=1, price=1000)
    sell_trade = Trade(quantity=-1, price=1000)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.add_trade(sell_trade)
    assert pnl_calculator.position_size == 0
    assert pnl_calculator.realised_pnl == 0


def test_pnl_calculator_calculates_profit(pnl_calculator):
    """
    We make a buy and a sell order, and check the pnl
    """
    buy_trade = Trade(1, 1000)
    sell_trade = Trade(-1, 1010)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.add_trade(sell_trade)
    assert pnl_calculator.position_size == 0
    assert pnl_calculator.realised_pnl == 10


def test_pnl_calculator_calculates_loss(pnl_calculator):
    """
    We make a buy and a sell order, and check the pnl
    """
    buy_trade = Trade(1, 1000)
    sell_trade = Trade(-1, 990)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.add_trade(sell_trade)
    assert pnl_calculator.position_size == 0
    assert pnl_calculator.realised_pnl == -10


def test_calculates_unrealised_pnl(pnl_calculator):
    """
    We make a buy and a sell order, and check the pnl
    """
    buy_trade = Trade(1, 1000)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.update_price(1010)
    assert pnl_calculator.unrealised_pnl == 10


def test_calculates_unrealised_pnl_with_multiple_trades(pnl_calculator):
    """
    We make a number of buy and a sell order, and check the pnl
    """
    buy_trade = Trade(1, 1000)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.update_price(1010)
    assert pnl_calculator.unrealised_pnl == 10
    sell_trade = Trade(-1, 1010)
    pnl_calculator.add_trade(sell_trade)
    pnl_calculator.update_price(1020)
    assert pnl_calculator.unrealised_pnl == 0
    assert pnl_calculator.realised_pnl == 10
    buy_trade = Trade(1, 1020)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.update_price(1030)
    buy_trade = Trade(1, 1030)
    pnl_calculator.add_trade(buy_trade)
    pnl_calculator.update_price(1040)
    assert pnl_calculator.unrealised_pnl == 30
    assert pnl_calculator.realised_pnl == 10


def test_add_trades_method(pnl_calculator):
    """
    Test the add_trades method.
    """
    pnl_calculator.add_trades([Trade(1, 1000), Trade(-1, 1010)])
    assert pnl_calculator.position_size == 0
    assert pnl_calculator.realised_pnl == 10


def test_average_price_for_sells_only(pnl_calculator):
    """
    Test the average_price method.
    """
    pnl_calculator.add_trades([Trade(-1, 1000), Trade(-1, 1010)])
    assert pnl_calculator.average_price == 1005


def test_average_price_for_buys_only(pnl_calculator):
    """
    Test the average_price method.
    """
    pnl_calculator.add_trades([Trade(1, 1000), Trade(1, 1010)])
    assert pnl_calculator.average_price == 1005


def test_buy_trades_from_quantity(pnl_calculator):
    """Test if trades can be caluclated from the total_quantity"""

    pnl_calculator.add_trades([Trade(1, total_cost=1000), Trade(2, total_cost=1900)])
    assert pnl_calculator.position_size == 3
    assert pnl_calculator.average_price == 2900 / 3


def test_sell_trades_from_quantity(pnl_calculator):
    """Test if trades can be caluclated from the total_quantity"""

    pnl_calculator.add_trades(
        [Trade(-1, total_cost=-1000), Trade(-2, total_cost=-1900)]
    )
    assert pnl_calculator.position_size == -3
    assert pnl_calculator.average_price == 2900 / 3
    # as we are only shorting, we get paid the total cost
