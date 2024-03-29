"""
Test the utils module.
"""

import pytest

from rysk_client.src.constants import ARBITRUM_GOERLI, PROTOCOL_DEPLOYMENTS
from rysk_client.src.utils import get_contract, get_web3


@pytest.fixture(scope="module")
def web3():
    """Get a web3 instance."""
    return get_web3()


def test_get_contract(web3):
    """Test whether we can get a contract instance."""
    contract = get_contract("opyn_controller", web3, ARBITRUM_GOERLI)
    assert (
        contract.address
        == PROTOCOL_DEPLOYMENTS[ARBITRUM_GOERLI.name]
        .contracts["opyn_controller"]
        .address
    )


def test_get_web3(web3):
    """Test whether we can get a web3 instance."""
    assert web3.isConnected()


@pytest.mark.parametrize(
    "address", [list(PROTOCOL_DEPLOYMENTS[ARBITRUM_GOERLI.name].contracts.keys()).pop()]
)
def test_get_contract_address(address, web3):
    """Test whether we can get the contract address for a given contract name"""
    contract = get_contract(address, web3, ARBITRUM_GOERLI)
    assert (
        contract.address
        == PROTOCOL_DEPLOYMENTS[ARBITRUM_GOERLI.name].contracts[address].address
    )
