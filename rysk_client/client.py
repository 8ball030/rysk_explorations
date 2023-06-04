"""
Simple client for the rysk contracts implemented in python.
"""
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from rysk_client.src.action_types import ActionType
from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import NULL_ADDRESS
from rysk_client.src.pnl_calculator import PnlCalculator, Trade
from rysk_client.src.position import OrderSide, PositionSide
from rysk_client.src.subgraph import SubgraphClient
from rysk_client.src.utils import get_logger
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


def parse_market(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parses the raw data from the subgraph into a market
    """
    active = all(
        [
            any(
                [
                    raw_data["isBuyable"],
                    raw_data["isSellable"],
                ]
            ),
            # we can get also filter out the expired options int(raw_data["expiration"]) > datetime.now().timestamp(),
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
        self._markets = []
        self._tickers = []
        self._otokens = {}
        self._crypto = EthCrypto(address, private_key)
        self.logger = get_logger()

    def fetch_markets(self) -> List[Dict[str, Any]]:
        """
        Fetchs the markets from the subgraph.
        """

        raw_data = self.subgraph_client.query_markets()
        data = map(parse_market, raw_data)

        self._markets = list(data)
        return self._markets

    def fetch_tickers(self, market: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Fetchs the ticker from the beyond pricer smart contract.
        """

        if not self._markets:
            self.fetch_markets()

        tradeable = filter(lambda x: x["active"], self._markets)

        if market:
            if not list(filter(lambda x: x["id"] == market, tradeable)):
                raise ValueError(f"Market {market} not found")

        workers = multiprocessing.cpu_count()
        with ThreadPoolExecutor(max_workers=workers) as pool:
            self._tickers = [
                pool.submit(self.web3_client.fetch_ticker, market).result()
                for market in tradeable
            ]

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

    def fetch_positions(self, expired=False) -> List[Dict[str, Any]]:
        """
        Fetchs the positions from the subgraph.
        """

        if self._crypto.address is None:
            raise ValueError("No account address was provided.")

        longs = self.subgraph_client.query_longs(address=self._crypto.address)
        shorts = self.subgraph_client.query_shorts(address=self._crypto.address)

        parsed_short = [self._parse_position(pos, PositionSide.SHORT) for pos in shorts]
        parsed_longs = [self._parse_position(pos, PositionSide.LONG) for pos in longs]

        if expired:
            positions = filter(
                lambda x: x["datetime"] <= datetime.now(),
                parsed_longs + parsed_short,
            )
        else:
            positions = filter(
                lambda x: x["datetime"] > datetime.now(),
                parsed_longs + parsed_short,
            )
        return list(positions)

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

    def create_order(
        self,
        symbol: str,
        amount: float,
        side: str = "buy",
    ) -> Dict[str, Any]:
        """Create a market order."""
        if side.upper() not in OrderSide.__members__:
            raise ValueError("Invalid order side")

        if side == OrderSide.BUY.value:
            transaction = self.buy_option(symbol, amount)
        else:
            transaction = self.sell_option(symbol, amount)
        return transaction

    def buy_option(
        self,
        market: str,
        amount: float,
        collateral_asset: str = "weth",
        leverage: float = 1,
    ):
        """
        Create a buy option order.
        """
        self.logger.info(
            f"Buying {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )
        return {
            "market": market,
        }

    def sell_option(
        self,
        market: str,
        amount: float,
        collateral_asset: str = "weth",
        leverage: float = 1,
    ):
        """
        Create a sell option order.
        """
        self.logger.info(
            f"Selling {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )

        rysk_option_market = [f for f in self._markets if f["symbol"] == market][0]

        _amount = amount * 1e18

        acceptable_premium = self.web3_client.get_options_prices(
            market, amount=_amount, side=OrderSide.SELL.value, collateral="eth"
        )

        position_id = 7
        vault_id = position_id

        # is this the option series??
        option_otoken = "JUN30_call_weth_collateral"

        underlying = Collateral.WETH.value

        strike_asset = Collateral.USDC.value

        operate_tuple = [
            {
                "operation": 0,
                "operationQueue": [
                    {
                        "actionType": ActionType.DEPOSIT_COLLATERAL.value,
                        "owner": self._crypto.address,
                        "secondAddress": self.web3_client.option_exchange.address,
                        "asset": Collateral.from_symbol(collateral_asset).value,
                        "vaultId": vault_id,
                        "amount": _amount,
                        "optionSeries": {
                            "expiration": 1,
                            "strike": 1,
                            "isPut": True,
                            "underlying": NULL_ADDRESS,
                            "strikeAsset": NULL_ADDRESS,
                            "collateral": NULL_ADDRESS,
                        },
                        "indexOrAcceptablePremium": 0,
                        "data": "0x0000000000000000000000000000000000000000",
                    },
                    {
                        "actionType": ActionType.MINT_SHORT_OPTION.value,
                        "owner": self._crypto.address,
                        "secondAddress": self.web3_client.option_exchange.address,
                        "asset": option_otoken,
                        "vaultId": vault_id,
                        "amount": 100000000,
                        "optionSeries": {
                            "expiration": 1,
                            "strike": 1,
                            "isPut": True,
                            "underlying": NULL_ADDRESS,
                            "strikeAsset": NULL_ADDRESS,
                            "collateral": NULL_ADDRESS,
                        },
                        "indexOrAcceptablePremium": 0,
                        "data": "0x0000000000000000000000000000000000000000",
                    },
                ],
            },
            {
                "operation": 1,
                "operationQueue": [
                    {
                        "actionType": ActionType.BURN_SHORT_OPTION.value,
                        "owner": NULL_ADDRESS,
                        "secondAddress": self._crypto.address,
                        "asset": NULL_ADDRESS,
                        "vaultId": 0,
                        "amount": _amount,
                        "optionSeries": {
                            "expiration": rysk_option_market["expiration"],
                            "strike": rysk_option_market["strike"],
                            "isPut": rysk_option_market["is_put"],
                            "underlying": underlying,
                            "strikeAsset": strike_asset,
                            "collateral": Collateral.from_symbol(
                                collateral_asset
                            ).value,
                        },
                        "indexOrAcceptablePremium": int(acceptable_premium * 0.9),
                        "data": "0x0000000000000000000000000000000000000000",
                    }
                ],
            },
        ]

        func = self.web3_client.opyn_controller.functions.operate(
            operate_tuple
        ).buildTransaction({"from": self._crypto.address})
        return func
