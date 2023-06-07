"""
Test the utils module.
"""

import pytest

from rysk_client.src.constants import ADDRESSES
from rysk_client.src.utils import get_contract, get_web3


@pytest.fixture(scope="module")
def web3():
    """Get a web3 instance."""
    return get_web3()


def test_get_contract(web3):
    """Test whether we can get a contract instance."""
    contract = get_contract("opyn_controller", web3)
    assert contract.address == ADDRESSES["opyn_controller"]["address"]


def test_get_web3(web3):
    """Test whether we can get a web3 instance."""
    assert web3.is_connected()


@pytest.mark.parametrize("address", ADDRESSES.keys())
def test_get_contract_address(address, web3):
    """Test whether we can get the contract address for a given contract name"""
    contract = get_contract(address, web3)
    assert contract.address == ADDRESSES[address]["address"]
