"""
Module for the conftest
"""
import pytest

from rysk_client.client import RyskClient
from rysk_client.src.subgraph import SubgraphClient
from tests.test_contract_calls import LocalFork

DEFAULT_ADDRESS = "0x9B8a204636a7aa9c33053d9C3A828720d32212e8"
DEFAULT_PRIVATE_KEY = (
    "0x75cc9212e9e1243b9a3e5db5012f39469254088e33363324ad94dd0b212d7efa"
)
DEFAULT_FORK_BLOCK_NUMBER = 27433769
TESTNET_RPC_URL = "https://arbitrum-goerli.rpc.thirdweb.com"


@pytest.fixture()
def default_address():
    """Get the default address."""
    return DEFAULT_ADDRESS


@pytest.fixture()
def default_private_key():
    """Get the default private key."""
    return DEFAULT_PRIVATE_KEY


@pytest.fixture
def subgraph_client():
    """Get the subgraph client."""
    return SubgraphClient()


@pytest.fixture
def local_fork():
    """Use a local fork to test contract calls."""
    fork = LocalFork(TESTNET_RPC_URL, DEFAULT_FORK_BLOCK_NUMBER)
    fork.run()
    yield fork
    fork.stop()


@pytest.fixture
def client(local_fork, default_address, default_private_key):
    """Get the rysk client."""

    crypto = {
        "address": default_address,
        "private_key": default_private_key,
    }
    client = RyskClient(**crypto)
    client.web3_client.web3.provider.endpoint_uri = (
        f"{local_fork.host}:{local_fork.port}"
    )
    return client
