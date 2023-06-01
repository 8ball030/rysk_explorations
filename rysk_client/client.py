"""
Simple client for the rysk contracts implemented in python.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

from rysk_client.src.subgraph import SubgraphClient
from rysk_client.web3_client import Web3Client

price_devisor = 1_000_000_000_000_000_000
exposure_devisor = 100_000_000_000_000_0000


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
    strike_price = str(int(int(row["strike"]) / price_devisor))

    return f"ETH-{day}{month_code}{year}-{strike_price}-{'P' if row['isPut'] else 'C'}"


@dataclass
class EthCrypto:
    address: str
    private_key: str


@dataclass
class RyskClient:
    """
    Client for the rysk contracts.
    """

    _markets: []

    def __init__(self, address: str = None, private_key: str = None):
        self.subgraph_client = SubgraphClient()
        self.web3_client = Web3Client()
        self.verbose = True
        self._markets = []
        self._crypto = EthCrypto(address, private_key)

    def fetch_markets(self) -> Dict[str, Any]:
        """
        Fetchs the markets from the subgraph.
        """

        raw_data = self.subgraph_client.query_markets()
        data = map(self._parseMarket, raw_data)

        data = filter(lambda x: x["active"], data)
        self._markets = list(data)
        return self._markets

    def _parseMarket(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parses the raw data from the subgraph into a market
        {'active': True,
         'base': 'ETH',
         'baseId': 'ETH',
         'contract': True,
         'contractSize': 1.0,
         'expiry': 1685520000000,
         'expiryDatetime': '2023-05-31T08:00:00.000Z',
         'future': False,
         'id': 'ETH-31MAY23-1950-P',
         'info': {'base_currency': 'ETH',
                  'block_trade_commission': '0.0003',
                  'block_trade_min_trade_amount': '250',
                  'block_trade_tick_size': '0.0001',
                  'contract_size': '1.0',
                  'counter_currency': 'USD',
                  'creation_timestamp': '1685260860000',
                  'expiration_timestamp': '1685520000000',
                  'instrument_id': '258005',
                  'instrument_name': 'ETH-31MAY23-1950-P',
                  'instrument_type': 'reversed',
                  'is_active': True,
                  'kind': 'option',
                  'maker_commission': '0.0003',
                  'min_trade_amount': '1',
                  'option_type': 'put',
                  'price_index': 'eth_usd',
                  'quote_currency': 'ETH',
                  'rfq': False,
                  'settlement_currency': 'ETH',
                  'settlement_period': 'day',
                  'strike': '1950.0',
                  'taker_commission': '0.0003',
                  'tick_size': '0.0005'},
         'inverse': True,
         'limits': {'amount': {'max': None, 'min': 1.0},
                    'cost': {'max': None, 'min': None},
                    'leverage': {'max': None, 'min': None},
                    'price': {'max': None, 'min': 0.0005}},
         'linear': False,
         'maker': 0.0003,
         'margin': False,
         'option': True,
         'optionType': 'put',
         'precision': {'amount': 1.0, 'price': 0.0005},
         'quote': 'USD',
         'quoteId': 'USD',
         'settle': 'ETH',
         'settleId': 'ETH',
         'spot': False,
         'strike': 1950.0,
         'swap': False,
         'symbol': 'ETH/USD:ETH-230531-1950-P',
         'taker': 0.0003,
         'type': 'option'}
        """
        default = {
            "base": "ETH",
            "baseId": "ETH",
            "contract": True,
            "contractSize": 1.0,
            "spot": False,
            "swap": False,
            "future": False,
            "type": "option",
            "contractSize": 0.1,
            "contract": True,
            "linear": False,
            "inverse": True,
        }
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

        default.update(
            {
                "active": active,
                "id": to_human_format(raw_data),
                "strike": int(raw_data["strike"]) / price_devisor,
                "optionType": "put" if raw_data["isPut"] else "call",
                "expiry": int(raw_data["expiration"]) * 1000,
                "expiryDatetime": expiration_datetime,
                "info": raw_data,
                "symbol": to_human_format(raw_data),
                "maker": 0.0003,
                "taker": 0.0003,
            }
        )
        return default

    def fetch_tickers(self) -> Dict[str, Any]:
        """
        Fetchs the ticker from the beyond pricer smart contract.
            {'ask': None,
             'askVolume': 0.0,
             'average': None,
             'baseVolume': None,
             'bid': 0.03,
             'bidVolume': 2.0,
             'change': None,
             'close': None,
             'datetime': '2023-05-28T19:48:46.855Z',
             'high': None,
             'info': {'ask_iv': '0.0',
                      'best_ask_amount': '0.0',
                      'best_ask_price': '0.0',
                      'best_bid_amount': '2.0',
                      'best_bid_price': '0.03',
                      'bid_iv': '0.0',
                      'estimated_delivery_price': '1847.72',
                      'greeks': {'delta': '-0.90958',
                                 'gamma': '0.00225',
                                 'rho': '-0.12269',
                                 'theta': '-2.34938',
                                 'vega': '0.24977'},
                      'index_price': '1847.72',
                      'instrument_name': 'ETH-31MAY23-1950-P',
                      'interest_rate': '0.0',
                      'last_price': None,
                      'mark_iv': '47.17',
                      'mark_price': '0.0561',
                      'max_price': '0.0925',
                      'min_price': '0.0245',
                      'open_interest': '0.0',
                      'state': 'open',
                      'stats': {'high': None,
                                'low': None,
                                'price_change': None,
                                'volume': '0.0',
                                'volume_usd': '0.0'},
                      'timestamp': '1685303326855',
                      'underlying_index': 'SYN.ETH-31MAY23',
                      'underlying_price': '1849.1787'},
             'last': None,
             'low': None,
             'open': None,
             'percentage': None,
             'previousClose': None,
             'quoteVolume': 0.0,
             'symbol': 'ETH/USD:ETH-230531-1950-P',
             'timestamp': 1685303326855,
             'vwap': None}

        """

        if not self._markets:
            self.fetch_markets()

        tickers = map(self._fetchTicker, self._markets)

        self._tickers = list(tickers)
        return self._tickers

    def _fetchTicker(self, market: Dict[str, Any]) -> Dict[str, Any]:
        """
        interact with the web3 api to fetch the ticker data
        """
        ask = self.web3_client.get_options_prices(market["info"])
        bid = self.web3_client.get_options_prices(market["info"], side="sell")
        return {"ask": ask, "bid": bid, "info": market}

    def fetch_positions(self) -> List[Dict[str, Any]]:
        """
        Fetchs the positions from the opyn smart contract.
        """
        return []
