"""
Module for the conftest
"""
import pytest

from rysk_client.src.subgraph import SubgraphClient

DEFAULT_ADDRESS = "0x9B8a204636a7aa9c33053d9C3A828720d32212e8"


@pytest.fixture()
def default_address():
    """Get the default address."""
    return DEFAULT_ADDRESS


@pytest.fixture
def subgraph_client():
    """Get the subgraph client."""
    return SubgraphClient()
