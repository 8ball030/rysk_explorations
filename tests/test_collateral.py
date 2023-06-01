"""
Test whether we can get the collateral of a given address
"""
import pytest

from rysk_client.src.collateral import Collateral
from rysk_client.src.utils import get_contract, get_web3


@pytest.mark.parametrize("name", ["usdc", "weth"])
def test_get_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    web3 = get_web3()
    get_contract(name, web3)


@pytest.mark.parametrize("name", ["usdc", "weth"])
def test_supported_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    assert Collateral.from_symbol(name) is not None


@pytest.mark.parametrize("name", ["btc", "doge"])
def test_unsupported_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    with pytest.raises(ValueError):
        Collateral.from_symbol(name)
