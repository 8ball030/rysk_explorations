"""
Module for the conftest
"""
import socket

import pytest

from rysk_client.client import RyskClient
from rysk_client.src.constants import ARBITRUM_GOERLI, CHAINS_TO_SUBGRAPH_URL
from rysk_client.src.subgraph import SubgraphClient
from tests.constants import (DEFAULT_ADDRESS, DEFAULT_FORK_BLOCK_NUMBER,
                             DEFAULT_PRIVATE_KEY, TESTNET_RPC_URL)
from tests.test_contract_calls import LocalFork


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
    return SubgraphClient(CHAINS_TO_SUBGRAPH_URL[ARBITRUM_GOERLI])


@pytest.fixture
def local_fork():
    """Use a local fork to test contract calls."""
    fork = LocalFork(TESTNET_RPC_URL, DEFAULT_FORK_BLOCK_NUMBER, port=get_unused_port())
    fork.run()
    yield fork
    fork.stop()


@pytest.fixture
def client(local_fork, default_address, default_private_key):
    """Get the rysk client."""

    crypto = {
        "address": default_address,
        "private_key": default_private_key,
        "verbose": True,
    }
    client = RyskClient(**crypto)
    client.web3_client.web3.provider.endpoint_uri = (
        f"{local_fork.host}:{local_fork.port}"
    )
    return client


def get_unused_port():
    """Get an unused port."""
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(("localhost", 0))
    port = new_socket.getsockname()[1]
    new_socket.close()
    return port
