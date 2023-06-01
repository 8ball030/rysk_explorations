"""
Test the subgraph module.
"""


def test_fetch_markets(subgraph_client):
    """Test fetching markets."""
    markets = subgraph_client.query_markets()
    assert len(markets) > 0
