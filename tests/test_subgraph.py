"""
Test the subgraph module.
"""


import pytest
import responses

from rysk_client.src.subgraph import BlockNotIndexed
from tests.constants import DEFAULT_FORK_BLOCK_NUMBER


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


@responses.activate
def test_query_index_fails(subgraph_client):
    """Test querying the index fails."""
    responses.add(
        responses.POST,
        subgraph_client.url,
        json={"errors": {"error": None}},
        status=200,
    )

    with pytest.raises(BlockNotIndexed):
        subgraph_client.query_index(0)


@responses.activate
def test_query_index(subgraph_client):
    """Test querying the index."""
    responses.add(
        responses.POST,
        subgraph_client.url,
        json={"data": {"stat": {"id": "0"}}},
        status=200,
    )
    index = subgraph_client.query_index(DEFAULT_FORK_BLOCK_NUMBER)
    assert index["id"] == "0"
