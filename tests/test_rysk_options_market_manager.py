"""
Tests for the RyskOptionMarketManager class
"""
import pytest

from rysk_client.src.rysk_option_market import RyskOptionMarketManager
from rysk_client.src.utils import get_web3


@pytest.fixture
def rysk_option_market_manager():
    """Returns a RyskOptionMarketManager"""

    web3 = get_web3()
    return RyskOptionMarketManager(web3)


def test_rysk_option_market_manager(rysk_option_market_manager):
    """Tests the RyskOptionMarketManager class"""
    assert isinstance(rysk_option_market_manager, RyskOptionMarketManager)


def test_fetch_option_markets(rysk_option_market_manager):
    """Tests the fetch_option_markets method"""
    rysk_option_market_manager.fetch_option_markets()
    assert len(rysk_option_market_manager.option_markets) > 0
