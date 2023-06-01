"""
This module contains the RyskOptionMarket class.
"""
from dataclasses import dataclass
from datetime import datetime

from rysk_client.src.utils import get_contract


@dataclass
class RyskOptionMarket:
    """Rysk option market."""

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
        return f"RyskOptionMarket({self.name})"


class RyskOptionMarketManager:
    """Class to represent the RyskOptionMarketManager."""

    def fetch_option_markets(self):
        """Fetches the option markets from the API"""
        markets = []
        for expiration in self._fetch_expirations():
            put_strikes = self.option_catalogue.functions.getOptionDetails(
                expiration, True
            ).call()
            call_strikes = self.option_catalogue.functions.getOptionDetails(
                expiration, False
            ).call()

            for strike in put_strikes:
                markets.append(RyskOptionMarket(expiration, strike, True))

            for strike in call_strikes:
                markets.append(RyskOptionMarket(expiration, strike, False))
        self.option_markets = markets
        return markets

    def __init__(self, web3):
        self.web3 = web3
        self.option_markets = {}
        self.option_catalogue = get_contract("option_catalogue", web3)
        self.fetch_option_markets()

    def fetch_option_market(self, name):
        """
        Fetches a specific option market from the smart contract.
        """

    def _fetch_expirations(self):
        """Returns the expirations from the smart contract."""
        return self.option_catalogue.functions.getExpirations().call()
