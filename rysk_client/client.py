"""
Simple client for the rysk contracts implemented in python.
"""
import multiprocessing
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from rysk_client.src.pnl_calculator import PnlCalculator, Trade
from rysk_client.src.position import PositionSide
from rysk_client.src.subgraph import SubgraphClient
from rysk_client.web3_client import Web3Client

PRICE_DEVISOR = 1_000_000_000_000_000_000
EXPOSURE_DEVISOR = 1_000_000_000_000_000_000


def from_timestamp(date_string):
    """Parse a timestamp. 2023-05-31T08:00:00.000Z"""
    return datetime.fromtimestamp(int(date_string)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def to_human_format(row):
    """
    Format the row to align to the ccxt unified client.
    'ETH-16MAY23-1550-C'
    """

    month_code = row["expiration_datetime"].strftime("%b").upper()
    day = row["expiration_datetime"].strftime("%d")
    year = str(row["expiration_datetime"].year)[2:]
    strike_price = str(int(int(row["strike"]) / PRICE_DEVISOR))

    return f"ETH-{day}{month_code}{year}-{strike_price}-{'P' if row['isPut'] else 'C'}"


@dataclass
class EthCrypto:
    """Represents a crypto wallet."""

    address: Optional[str]
    private_key: Optional[str]


DEFAULT_MARKET = {
    "base": "ETH",
    "baseId": "ETH",
    "contract": True,
    "contractSize": 1.0,
    "spot": False,
    "swap": False,
    "future": False,
    "type": "option",
    "linear": False,
    "inverse": True,
    "maker": 0.0003,
    "taker": 0.0003,
}


@dataclass
class RyskClient:
    """
    Client for the rysk contracts.
    """

    _markets: List[Dict[str, Any]]
    _tickers: List[Dict[str, Any]]
    _otokens: Dict[str, Dict[str, Any]]

    def __init__(
        self, address: Optional[str] = None, private_key: Optional[str] = None
    ):
        self.subgraph_client = SubgraphClient()
        self.web3_client = Web3Client()
        self.verbose = True
        self._markets = []
        self._tickers = []
        self._otokens = {}
        self._crypto = EthCrypto(address, private_key)

    def fetch_markets(self) -> List[Dict[str, Any]]:
        """
        Fetchs the markets from the subgraph.
        """

        raw_data = self.subgraph_client.query_markets()
        data = map(self._parse_market, raw_data)

        filtered_data = filter(lambda x: x["active"], data)
        self._markets = list(filtered_data)
        return self._markets

    def _parse_market(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses the raw data from the subgraph into a market
        """
        active = all(
            [
                raw_data["isBuyable"],
                raw_data["isSellable"],
                int(raw_data["expiration"]) > datetime.now().timestamp(),
            ]
        )
        expiration_datetime = from_timestamp(raw_data["expiration"])
        raw_data.update(
            {
                "expiration_datetime": datetime.strptime(
                    expiration_datetime, "%Y-%m-%dT%H:%M:%S.%fZ"
                )
            }
        )
        market = deepcopy(DEFAULT_MARKET)

        market.update(
            {
                "active": active,
                "id": to_human_format(raw_data),
                "strike": int(raw_data["strike"]) / PRICE_DEVISOR,
                "optionType": "put" if raw_data["isPut"] else "call",
                "expiry": int(raw_data["expiration"]) * 1000,
                "expiryDatetime": expiration_datetime,
                "info": raw_data,
                "symbol": to_human_format(raw_data),
            }
        )
        return market

    def fetch_tickers(self) -> List[Dict[str, Any]]:
        """
        Fetchs the ticker from the beyond pricer smart contract.
        """

        if not self._markets:
            self.fetch_markets()

        cores = multiprocessing.cpu_count()

        with multiprocessing.Pool(cores) as pool:
            self._tickers = list(pool.map(self._fetch_ticker, self._markets))  # type: ignore

        return self._tickers

    @property
    def otokens(self) -> Dict[str, Dict[str, Any]]:
        """
        Returns a dictionary of the otokens.
        """
        if not self._otokens:
            self.fetch_tickers()
        self._otokens = {ticker["info"]["id"]: ticker for ticker in self._tickers}
        return self._otokens

    def _fetch_ticker(self, market: Dict[str, Any]) -> Dict[str, Any]:
        """
        interact with the web3 api to fetch the ticker data
        """
        ask = self.web3_client.get_options_prices(market["info"])
        bid = self.web3_client.get_options_prices(market["info"], side="sell")
        return {"ask": ask, "bid": bid, "info": market}

    def fetch_positions(self) -> List[Dict[str, Any]]:
        """
        Fetchs the positions from the subgraph.
        """

        if self._crypto.address is None:
            raise ValueError("No account address was provided.")

        longs = self.subgraph_client.query_longs(address=self._crypto.address)
        parsed_longs = [self._parse_position(pos, PositionSide.LONG) for pos in longs]
        shorts = self.subgraph_client.query_shorts(address=self._crypto.address)
        parsed_short = [self._parse_position(pos, PositionSide.SHORT) for pos in shorts]

        return parsed_longs + parsed_short

    def _parse_position(
        self, position: Dict[str, Any], side: PositionSide
    ) -> Dict[str, Any]:
        """
        Parse the position data from the subgraph into a unified format.
        """
        position["expiration_datetime"] = datetime.fromtimestamp(
            int(position["oToken"]["expiryTimestamp"])
        )
        position["strike"] = float(position["oToken"]["strikePrice"]) * 1e10
        position["isPut"] = position["oToken"]["isPut"]

        pnl_calculator = PnlCalculator()

        buys = [
            Trade(int(order["amount"]) / 1e18, int(order["premium"]) / -1e10)
            for order in position["optionsBoughtTransactions"]
        ]
        sells = [
            Trade(-int(order["amount"]) / 1e18, int(order["premium"]) / 1e10)
            for order in position["optionsSoldTransactions"]
        ]

        pnl_calculator.add_trades(buys + sells)

        symbol = to_human_format(position)

        if symbol in self.otokens:
            book_side = "ask" if side == PositionSide.LONG else "bid"
            price = self.otokens[symbol][book_side]
            pnl_calculator.update_price(price)
        else:
            print(
                f"Could not find {symbol} in the otokens list. Maket is probably not active."
            )
        result = {
            "id": position["id"],
            "symbol": symbol,
            "timestamp": int(position["oToken"]["expiryTimestamp"]) * 1000,
            "datetime": datetime.fromtimestamp(
                int(position["oToken"]["expiryTimestamp"])
            ),
            "initialMarginPercentage": None,
            "realizedPnl": pnl_calculator.realised_pnl,
            "unrealizedPnl": pnl_calculator.unrealised_pnl,
            "contractSize": pnl_calculator.position_size,
            "side": side.value,
            "info": position,
            "contracts": None,
            "marginRatio": None,
            "liquidationPrice": None,
            "lastPrice": None,
            "collateral": None,
            "marginMode": None,
            "initialMargin": None,
            "maintenanceMargin": None,
            "maintenanceMarginPercentage": None,
            "entryPrice": None,
            "notional": None,
            "leverage": None,
            "percentage": None,
        }
        return result
