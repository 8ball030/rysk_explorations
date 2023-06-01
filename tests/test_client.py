"""
Test the rysk client.
"""

import pytest

from rysk_client.client import RyskClient


@pytest.fixture
def client(default_address):
    """Get the rysk client."""
    private_key = {
        "address": default_address,
    }
    return RyskClient(**private_key)


def test_fetch_markets(client):
    """Test fetching markets."""
    markets = client.fetch_markets()
    assert len(markets) > 0


def test_fetch_tickers(client):
    """Test fetching tickers."""
    tickers = client.fetch_tickers()
    assert len(tickers) > 0


@pytest.mark.skip(reason="Not implemented yet.")
def test_fetch_positions(client):
    """Test fetching positions."""
    positions = client.fetch_positions()
    assert len(positions) > 0
