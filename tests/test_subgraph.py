"""
Test the subgraph module.
"""


def test_fetch_markets(subgraph_client):
    """Test fetching markets."""
    markets = subgraph_client.query_markets()
    assert len(markets) > 0


def test_fetch_longs(subgraph_client, default_address):
    """Test fetching longs."""
    longs = subgraph_client.query_longs(default_address)
    assert isinstance(longs, list)


def test_fetch_shorts(subgraph_client, default_address):
    """Test fetching shorts."""
    shorts = subgraph_client.query_shorts(default_address)
    assert isinstance(shorts, list)
