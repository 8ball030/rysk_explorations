"""
This module contains the RyskOptionMarket class.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from rysk_client.src.collateral import Collateral
from rysk_client.src.utils import get_contract

HUMAN_NUMBER_FMT = 1e18
HUMAN_NUMBER_FMT_USDC = 1e6
EXPIRATION_TIME = "08:00:00"


@dataclass
class TradingSpec:
    """
    Class to represent the trading spec.
    """

    iv: int  # noqa: C0103
    quote: int
    fee: int
    disabled: bool
    premium_too_small: bool


@dataclass
class OptionStrikeDrill:
    """
    Class to represent the option strike drill.
    """

    strike: int
    sell: TradingSpec
    buy: TradingSpec
    delta: int
    exposure: int


class OptionChain:
    """Class to represent the option chain."""

    _raw_data: tuple
    expirations: List[int]
    strikes: Dict[int, List[int]]

    def __init__(self, raw_data: tuple) -> None:
        self._raw_data = raw_data
        self.parse_expirations()
        self.parse_strikes()

    def parse_expirations(self):
        """Parse and set the expirations."""
        self.expirations = self._raw_data[0]

    def parse_strikes(self):
        """Parse and set the strikes."""
        self.strikes = {}
        for index, expiration_1 in enumerate(self.expirations):
            expiration_data = self._raw_data[1][index]
            (
                expiration_3,  # noqa: F841
                call_strikes,  # noqa: F841
                call_data,
                put_strikes,  # noqa: F841
                put_data,
                underlying_value,  # noqa: F841
            ) = expiration_data

            call_option_drill = self._parse_option_data(call_data)
            put_option_drill = self._parse_option_data(put_data)

            self.strikes[expiration_1] = {
                "call": call_option_drill,
                "put": put_option_drill,
            }

    def _parse_option_data(self, option_data: tuple):
        """
        Parse the option data.
        """
        markets = []
        for (
            strike,
            sell_trading_specs,
            buy_trading_specs,
            delta,
            net_dhv_exposure,
        ) in option_data:
            sell_trading_specs = TradingSpec(*sell_trading_specs)
            buy_trading_specs = TradingSpec(*buy_trading_specs)
            markets.append(
                OptionStrikeDrill(
                    strike,
                    sell_trading_specs,
                    buy_trading_specs,
                    delta,
                    net_dhv_exposure,
                )
            )
        return markets

    @property
    def active_markets(self):
        """Return the active strikes for the active markets, where option drill is not disabled."""
        active_markets = []
        for expiration, option_drill in self.strikes.items():
            for option_type, option_type_drill in option_drill.items():
                for option_market in option_type_drill:
                    if (
                        not option_market.sell.disabled
                        or not option_market.buy.disabled
                    ):
                        active_markets.append((expiration, option_type, option_market))
        return active_markets

    @property
    def current_price(self):
        """
        Return the underlying price from the oracle.
        """
        return self._raw_data[1][-1][-1] / 1e18


class OptionType(Enum):
    """Option type enum."""

    CALL = "call"
    PUT = "put"


@dataclass
class RyskOptionMarket:  # pylint: disable=too-many-instance-attributes
    """Rysk option market."""

    strike: float
    expiration: int
    is_put: bool
    active: bool = True
    # market data
    bid: Optional[int] = None
    ask: Optional[int] = None
    dhv: Optional[int] = None
    delta: Optional[int] = None

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

    @classmethod
    def from_option_drill(
        cls, expiration: int, option_type: str, option_drill: OptionStrikeDrill
    ):
        """Returns a RyskOptionMarket from an option drill"""
        return cls(
            strike=option_drill.strike,
            expiration=expiration,
            is_put=option_type == "put",
            ask=option_drill.buy.quote,
            bid=option_drill.sell.quote,
            dhv=option_drill.exposure,
            delta=option_drill.delta,
        )

    def to_json(self):
        """Returns the option market as a json"""
        market_data = {}
        if self.bid and self.ask and self.dhv:
            market_data = {
                "bid": self.bid / HUMAN_NUMBER_FMT_USDC,
                "ask": self.ask / HUMAN_NUMBER_FMT_USDC,
                "dhv": self.dhv / HUMAN_NUMBER_FMT,
            }
        result = {
            "id": self.name,
            "strike": self.strike / HUMAN_NUMBER_FMT,
            "expiration": self.expiration,
            "optionType": "put" if self.is_put else "call",
            "active": self.active,
        }
        if self.delta:
            result["delta"] = self.delta / HUMAN_NUMBER_FMT
        result.update(**market_data)
        return result

    def to_series(self):
        """
        creates a json series object compatible with the rysk contracts.
        """
        return {
            "strike": self.strike,
            "expiration": self.expiration,
            "isPut": self.is_put,
            "underlying": Collateral.WETH.value,
            "strikeAsset": Collateral.USDC.value,
            "collateral": Collateral.USDC.value
            if self.is_put
            else Collateral.WETH.value,
        }

    @classmethod
    def from_str(cls, name: str):
        """Returns a RyskOptionMarket from a name"""
        _name = name.split("-")
        expiration_date = datetime.strptime(
            f"{_name[1]}T{EXPIRATION_TIME}+00:00",
            "%d%b%yT%H:%M:%S%z",
        )
        _expiration = int(expiration_date.timestamp())

        _strike = int(_name[2]) * 10**18
        _is_put = _name[3] == "P"
        return cls(_strike, _expiration, _is_put)


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
