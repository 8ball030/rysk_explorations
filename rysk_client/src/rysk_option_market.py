from dataclasses import dataclass
from datetime import datetime


@dataclass
class RyskOptionMarket:
    """"""

    strike: float
    expiration: int
    is_put: bool

    @classmethod
    def from_series(cls, series):
        """Returns a RyskOptionMarket from a series"""
        return cls(
            strike=series["strike"],
            expiration=series["expiration"],
            is_put=series["isPut"],
        )

    def _parse_name(self):
        """Returns the name of the option market into the following format.

        NAME = "ETH-30JUN23-2200-C"
        """
        _type = "P" if self.is_put else "C"
        _expiration = datetime.fromtimestamp(self.expiration).strftime("%d%b%y").upper()
        _strike = int(self.strike / 10**18)
        return f"ETH-{_expiration}-{_strike}-{_type}"

    @property
    def name(self):
        """Returns the name of the option market"""
        return self._parse_name()

    def __str__(self):
        return "RyskOptionMarket(name={} strike={}, expiration={}, is_put={})".format(
            self.name, self.strike, self.expiration, self.is_put
        )


class RyskOptionMarketManager:
    """Class to represent the RyskOptionMarketManager."""

    def fetch_option_markets(self):
        """Fetches the option markets from the API"""
        markets = []
        for expiration in expirations:
            put_strikes = self.option_catalogue.functions.getOptionDetails(
                expiration, True
            ).call()
            call_strikes = self.option_catalogue.functions.getOptionDetails(
                expiration, False
            ).call()

            for strike in put_strikes:
                markets.append(RyskMarket(expiration, strike, True))

            for strike in call_strikes:
                markets.append(RyskMarket(expiration, strike, False))
        markets

    def __init__(self, web3):
        self.web3 = web3
        self.option_markets = {}
        self.fetch_option_markets()
        self.option_catalogue = get_contract("option_catalogue", web3)

    def fetch_option_market(self, name):
        """
        Fetches a specific option market from the smart contract.
        """


# tests/test_rysk_option_market_manager.py
import pytest

from rysk_client.src.rysk_option_market import RyskOptionMarket, RyskOptionMarketManager
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
