"""
This module contains the RyskOptionMarket class.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from rysk_client.src.collateral import CollateralFactory
from rysk_client.src.constants import USDC_MULTIPLIER, WETH_MULTIPLIER, Chain

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
    series_collateral_exchange_balance_usdc: Optional[int] = None
    series_collateral_exchange_balance_weth: Optional[int] = None


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
        if len(option_data[0]) == 5:
            cols = [
                "strike",
                "sell_trading_specs",
                "buy_trading_specs",
                "delta",
                "exposure",
            ]
        elif len(option_data[0]) == 7:
            cols = [
                "strike",
                "sell_trading_specs",
                "buy_trading_specs",
                "delta",
                "exposure",
                "series_collateral_exchange_balance_usdc",
                "series_collateral_exchange_balance_weth",
            ]
        else:
            raise ValueError("Option data has unexpected length. is not beta or prod.")

        for row in option_data:
            params = {}
            for k, val in zip(cols, row):
                if k in ["sell_trading_specs", "buy_trading_specs"]:
                    params[k.split("_")[0]] = TradingSpec(*val)
                else:
                    params[k] = val
            markets.append(OptionStrikeDrill(**params))
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
        return self._raw_data[1][-1][-1] / WETH_MULTIPLIER


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
    _collateral: Optional[str] = None

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
        _strike = int(self.strike / WETH_MULTIPLIER)
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
        if self.bid and self.ask and self.dhv is not None:
            market_data = {
                "bid": self.bid / USDC_MULTIPLIER,
                "ask": self.ask / USDC_MULTIPLIER,
                "dhv": self.dhv / WETH_MULTIPLIER,
            }
        result = {
            "id": self.name,
            "strike": self.strike / WETH_MULTIPLIER,
            "expiration": self.expiration,
            "optionType": "put" if self.is_put else "call",
            "active": self.active,
        }
        if self.delta:
            result["delta"] = self.delta / WETH_MULTIPLIER
        result.update(**market_data)
        return result

    @classmethod
    def from_json(cls, json):
        """Returns a RyskOptionMarket from a json"""
        return cls(
            strike=json["strike"] * WETH_MULTIPLIER,
            expiration=json["expiration"],
            is_put=json["optionType"] == "put",
            active=json["active"],
            bid=json.get("bid") * USDC_MULTIPLIER,
            ask=json.get("ask") * USDC_MULTIPLIER,
            dhv=json.get("dhv") * WETH_MULTIPLIER,
            delta=json.get("delta"),
        )

    @classmethod
    def from_str(cls, name: str):
        """Returns a RyskOptionMarket from a name"""
        _name = name.split("-")
        expiration_date = datetime.strptime(
            f"{_name[1]}T{EXPIRATION_TIME}+00:00",
            "%d%b%yT%H:%M:%S%z",
        )
        _expiration = int(expiration_date.timestamp())

        _strike = int(_name[2]) * WETH_MULTIPLIER
        _is_put = _name[3] == "P"
        return cls(_strike, _expiration, _is_put)

    @property
    def collateral(self):
        """Returns the collateral of the option market"""
        if self._collateral is None:
            raise ValueError("Collateral not set")
        return self._collateral

    @collateral.setter
    def collateral(self, collateral):
        """Sets the collateral of the option market"""
        self._collateral = collateral


@dataclass
class MarketFactory:
    """Class to generate option markets."""

    chain: Chain

    def __init__(self, chain: Chain, covered: bool = True):
        """
        Markets factory will generate option markets for the given chain.
        If covered is True, it will generate markets for the covered options.
        I.e. for a given strike and expiration, it will generate a call and a put.
        If called with covered=False, it will generate markets for the naked options.
        """
        self.chain = chain
        self.collateral_factory = CollateralFactory(chain)
        self._covered = covered

    def to_series(self, rysk_option_market: RyskOptionMarket):
        """Returns the series of the option market
        effectively, we are adding the appriate contract addresses to the option market.
        """
        return {
            "strike": int(rysk_option_market.strike),
            "expiration": int(rysk_option_market.expiration),
            "isPut": rysk_option_market.is_put,
            "underlying": self.collateral_factory.WETH,
            "strikeAsset": self.collateral_factory.USDC,
            "collateral": rysk_option_market.collateral,
        }
