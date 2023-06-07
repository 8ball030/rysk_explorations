"""
Test the rysk option market class.
"""

import pytest

from rysk_client.src.rysk_option_market import (OptionStrikeDrill,
                                                RyskOptionMarket, TradingSpec)


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
    data = (
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

    rysk_option_market = RyskOptionMarket.from_option_drill(*data)
    assert rysk_option_market.name == "ETH-30JUN23-1800-C"
    assert rysk_option_market.strike == 1800000000000000000000
    assert rysk_option_market.expiration == 1688112000
    assert not rysk_option_market.is_put
