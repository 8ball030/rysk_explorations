"""
Test the rysk client.
"""
import pytest
import responses

from rysk_client.src.constants import ARBITRUM_GOERLI, CHAINS_TO_SUBGRAPH_URL


def test_fetch_markets(client):
    """Test fetching markets."""
    markets = client.fetch_markets()
    assert len(markets) > 0


def test_fetch_tickers(client):
    """Test fetching tickers."""
    tickers = client.fetch_tickers()
    assert len(tickers) > 0


@responses.activate
def test_fetch_positions(client):
    """Test fetching positions."""
    responses.add(
        responses.POST,
        CHAINS_TO_SUBGRAPH_URL[ARBITRUM_GOERLI],
        json={"data": {"longPositions": [], "shortPositions": []}},
    )
    positions = client.fetch_positions()
    assert len(positions) == 0


@pytest.mark.parametrize(
    "market",
    [
        "ETH-28JUL23-1900-C",
        "ETH-28JUL23-1900-P",
    ],
)
@pytest.mark.flaky(reruns=3)  # why this is the case i am not yet sure.
def test_create_buy_order(
    client,
    market,
):
    """Test creating a buy order."""
    order = client.create_order(market, 1, "buy")
    assert order


@pytest.mark.flaky(reruns=3)  # why this is the case i am not yet sure.
def test_create_sell_order(client):
    """Test creating a sell order."""
    market = client.fetch_markets()[0]
    order = client.create_order(market["id"], 1, "sell")
    assert order
