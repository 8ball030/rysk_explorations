"""
Test whether we can get the collateral of a given address
"""
import pytest

from rysk_client.src.collateral import CollateralFactory
from rysk_client.src.constants import ARBITRUM_GOERLI
from rysk_client.src.utils import get_contract, get_web3


@pytest.mark.parametrize("name", ["usdc", "weth"])
def test_get_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    web3 = get_web3(ARBITRUM_GOERLI)
    get_contract(name, web3, ARBITRUM_GOERLI)


@pytest.mark.parametrize("name", ["usdc", "weth"])
def test_supported_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    collateral = CollateralFactory(ARBITRUM_GOERLI)
    assert collateral.from_symbol(name) is not None


@pytest.mark.parametrize("name", ["btc", "doge"])
def test_unsupported_collateral(name):
    """Test the collateral class can be instantiated with supported collateral"""
    collateral = CollateralFactory(ARBITRUM_GOERLI)
    with pytest.raises(ValueError):
        collateral.from_symbol(name)
