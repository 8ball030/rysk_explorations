"""
Test the rysk client.
"""

import pytest

from rysk_client.client import RyskClient


@pytest.fixture
def client(default_address):
    """Get the rysk client."""
    crypto = {
        "address": default_address,
    }
    return RyskClient(**crypto)


def test_fetch_markets(client):
    """Test fetching markets."""
    markets = client.fetch_markets()
    assert len(markets) > 0


def test_fetch_tickers(client):
    """Test fetching tickers."""
    tickers = client.fetch_tickers()
    assert len(tickers) > 0


def test_fetch_positions(client):
    """Test fetching positions."""
    positions = client.fetch_positions()
    assert len(positions) > 0


@pytest.mark.skip(reason="Not currently working.")
def test_create_buy_order(client):
    """Test creating a buy order."""
    market = client.fetch_markets()[0]
    order = client.create_order(market["id"], 1, "buy")
    assert order


@pytest.mark.skip(reason="Not currently working.")
def test_create_sell_order(client):
    """Test creating a sell order."""
    market = client.fetch_markets()[0]
    order = client.create_order(market["id"], 1, "sell")
    assert order
