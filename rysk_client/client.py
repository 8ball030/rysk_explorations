"""
Simple client for the rysk contracts implemented in python.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

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


@dataclass
class RyskClient:
    """
    Client for the rysk contracts.
    """

    _markets: List[Dict[str, Any]]
    _tickers: List[Dict[str, Any]]

    def __init__(
        self, address: Optional[str] = None, private_key: Optional[str] = None
    ):
        self.subgraph_client = SubgraphClient()
        self.web3_client = Web3Client()
        self.verbose = True
        self._markets = []
        self._tickers = []
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
                "strike": int(raw_data["strike"]) / PRICE_DEVISOR,
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

    def fetch_tickers(self) -> List[Dict[str, Any]]:
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

        tickers = map(self._fetch_ticker, self._markets)

        self._tickers = list(tickers)
        return self._tickers

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
        input:
        {
            "id": "0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x3fa148f692e516654283c9ff4cbe3b15355f48f5-s-0",
            "netAmount": "-20000000000000000000",
            "buyAmount": "0",
            "sellAmount": "20000000000000000000",
            "active": true,
            "realizedPnl": "1744192333",
            "oToken": {
              "id": "0x3fa148f692e516654283c9ff4cbe3b15355f48f5",
              "symbol": "oWETHUSDC/USDC-19MAY23-2000C",
              "expiryTimestamp": "1684483200",
              "strikePrice": "200000000000",
              "isPut": false,
              "underlyingAsset": {
                "id": "0x3b3a1de07439eeb04492fa64a889ee25a130cdd3"
              },
              "createdAt": "1683555260"
              },
        },
        output:
        {
                'info': {
                        'vega': '-1.35589',
                        'total_profit_loss': '-0.001586671',
                        'theta': '1.66193',
                        'size': '-1.0',
                        'settlement_price': '0.013858',
                        'realized_profit_loss': '0.0',
                        'open_orders_margin': '0.0',
                        'mark_price': '0.014587',
                        'maintenance_margin': '0.089586671',
                        'kind': 'option',
                        'instrument_name': 'ETH-16JUN23-1950-C',
                        'initial_margin': '0.13466616',
                        'index_price': '1893.35',
                        'gamma': '-0.00293',
                        'floating_profit_loss_usd': '-3.950784',
                        'floating_profit_loss': '-0.000728879',
                        'direction': 'sell',
                        'delta': '-0.34205',
                        'average_price_usd': '23.66689',
                        'average_price': '0.013'
                },
                'id': None,
                'symbol': 'ETH/USD:ETH-230616-1950-C',
                'timestamp': 1685704039684,
                'datetime': '2023-06-02T11:07:19.684Z',
                'lastUpdateTimestamp': None,
                'initialMargin': 0.13466616,
                'initialMarginPercentage': None,
                'maintenanceMargin': 0.089586671,
                'maintenanceMarginPercentage': None,
                'entryPrice': 0.013,
                'notional': None,
                'leverage': None,
                'unrealizedPnl': -0.000728879,
                'contracts': None,
                'contractSize': 1.0,
                'marginRatio': None,
                'liquidationPrice': None,
                'markPrice': 0.014587,
                'lastPrice': None,
                'collateral': None,
                'marginMode': None,
                'side': 'short',
                'percentage': None
        }
        """
        position["expiration_datetime"] = datetime.fromtimestamp(
            int(position["oToken"]["expiryTimestamp"])
        )
        position["strike"] = float(position["oToken"]["strikePrice"]) * 1e10
        position["isPut"] = position["oToken"]["isPut"]

        symbol = to_human_format(position)

        result = {
            "id": position["id"],
            "symbol": symbol,
            "timestamp": int(position["oToken"]["expiryTimestamp"]) * 1000,
            "datetime": datetime.fromtimestamp(
                int(position["oToken"]["expiryTimestamp"])
            ),
            "initialMarginPercentage": None,
            "realizedPnl": float(position["realizedPnl"]) / 1e10,
            "contractSize": position["netAmount"],
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
