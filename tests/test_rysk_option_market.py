"""
Test the rysk option market class.
"""
import pytest

from rysk_client.src.rysk_option_market import RyskOptionMarket


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
