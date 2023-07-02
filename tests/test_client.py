"""
Test the rysk client.
"""
import pytest
import responses


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
        "https://api.studio.thegraph.com/query/45686/rysk/version/latest",
        json={"data": {"longPositions": [], "shortPositions": []}},
    )
    positions = client.fetch_positions()
    assert len(positions) == 0


@pytest.mark.parametrize(
    "market,block_number",
    [
        ("ETH-28JUL23-1900-C", 28983125),
        ("ETH-28JUL23-1900-P", 28983125),
    ],
)
def test_create_buy_order(local_fork, client, market, block_number):
    """Test creating a buy order."""
    local_fork.restart_from_block(block_number)
    order = client.create_order(market, 1, "buy")
    assert order


def test_create_sell_order(client):
    """Test creating a sell order."""
    market = client.fetch_markets()[0]
    order = client.create_order(market["id"], 1, "sell")
    assert order
