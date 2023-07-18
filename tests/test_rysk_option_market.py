"""
Test the rysk option market class.
"""

import pytest

from rysk_client.src.collateral import CollateralFactory
from rysk_client.src.constants import ARBITRUM_GOERLI
from rysk_client.src.rysk_option_market import (MarketFactory,
                                                OptionStrikeDrill,
                                                RyskOptionMarket, TradingSpec)

OPTION_DRILL_DATA = (
    1688112000,
    "call",
    OptionStrikeDrill(
        strike=1800000000000000000000,
        sell=TradingSpec(
            iv=368092714837837288,
            quote=112270427,
            fee=500000,
            disabled=False,
            premium_too_small=False,
        ),
        buy=TradingSpec(
            iv=368092714837837288,
            quote=115080725,
            fee=500000,
            disabled=False,
            premium_too_small=False,
        ),
        delta=701550808961229697,
        exposure=9500000000000000000,
    ),
)


@pytest.mark.parametrize(
    "name, strike, expiration, is_put",
    [
        ("ETH-12MAY23-1725-P", 1725000000000000000000, 1683878400, True),
        ("ETH-12MAY23-1850-C", 1850000000000000000000, 1683878400, False),
    ],
)
def test_rysk_option_market(name, strike, expiration, is_put):
    """
    Test instatiation of RyskOptionMarket from the data returned by the API
        RyskMarket(expiration=1683878400, strike=1975000000000000000000, is_put=True),
    """

    series = {"strike": strike, "expiration": expiration, "isPut": is_put}
    rysk_option_market = RyskOptionMarket.from_series(series)
    assert rysk_option_market.name == name
    assert rysk_option_market.strike == strike
    assert rysk_option_market.expiration == expiration
    assert rysk_option_market.is_put == is_put


def test_from_option_drill():
    """
    Test instatiation of RyskOptionMarket from the data returned by the API
    """

    rysk_option_market = RyskOptionMarket.from_option_drill(*OPTION_DRILL_DATA)
    assert rysk_option_market.name == "ETH-30JUN23-1800-C"
    assert rysk_option_market.strike == 1800000000000000000000
    assert rysk_option_market.expiration == 1688112000
    assert not rysk_option_market.is_put


def test_from_str():
    """
    Test that RyskOptionMarket can be instantiated from a string
    """
    rysk_option_market = RyskOptionMarket.from_str("ETH-30JUN23-1800-C")
    assert rysk_option_market.name == "ETH-30JUN23-1800-C"
    assert rysk_option_market.strike == 1800000000000000000000
    assert rysk_option_market.expiration == 1688112000
    assert not rysk_option_market.is_put


def test_to_series_match():
    """
    Test that RyskOptionMarket can be instantiated from a string and that to series matches
    the to series of the original series
    """
    rysk_option_market_1 = RyskOptionMarket.from_str("ETH-30JUN23-1800-C")
    rysk_option_market_2 = RyskOptionMarket.from_option_drill(*OPTION_DRILL_DATA)
    market_factory = MarketFactory(ARBITRUM_GOERLI)
    collateral_factory = CollateralFactory(ARBITRUM_GOERLI)
    rysk_option_market_1.collateral = collateral_factory.WETH
    rysk_option_market_2.collateral = collateral_factory.WETH
    series_1 = market_factory.to_series(rysk_option_market_1)
    series_2 = market_factory.to_series(rysk_option_market_2)
    assert series_1 == series_2
