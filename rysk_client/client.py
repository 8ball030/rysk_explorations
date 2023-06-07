"""
Simple client for the rysk contracts implemented in python.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from rysk_client.src.action_types import ActionType
from rysk_client.src.collateral import Collateral
from rysk_client.src.constants import NULL_ADDRESS, NULL_DATA
from rysk_client.src.crypto import EthCrypto
from rysk_client.src.pnl_calculator import PnlCalculator, Trade
from rysk_client.src.position import OrderSide, PositionSide
from rysk_client.src.rysk_option_market import OptionChain, RyskOptionMarket
from rysk_client.src.subgraph import SubgraphClient
from rysk_client.src.utils import get_contract, get_logger
from rysk_client.web3_client import Web3Client

PRICE_DEVISOR = 1_000_000_000_000_000_000
EXPOSURE_DEVISOR = 1_000_000_000_000_000_000

ALLOWED_SLIPPAGE = 0.1


class ApprovalException(Exception):
    """
    Exception raised when the approval fails.
    """


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
class RyskClient:  # noqa: R0902
    """
    Client for the rysk contracts.
    """

    _markets: List[RyskOptionMarket]
    _tickers: List[Dict[str, Any]]
    _otokens: Dict[str, Dict[str, Any]]

    def __init__(
        self,
        address: Optional[str] = None,
        private_key: Optional[str] = None,
        logger=None,
    ):
        self._markets: List[RyskOptionMarket] = []
        self._tickers = []
        self._otokens = {}
        self._option_chain: OptionChain
        self._crypto = EthCrypto(address, private_key)
        self._logger = logger or get_logger()
        self.web3_client = Web3Client(self._logger, self._crypto)
        self.subgraph_client = SubgraphClient()

    def fetch_markets(self) -> List[Dict[str, Any]]:
        """
        Fetchs the markets from the subgraph.
        """

        raw_data = self.web3_client.get_option_chain()
        self._option_chain = OptionChain(raw_data)
        self._markets = [
            RyskOptionMarket.from_option_drill(*data)
            for data in self._option_chain.active_markets
        ]
        return [market.to_json() for market in self._markets]  # type: ignore

    def to_checksum_address(self, address):
        """Convert an address to a checksum address."""
        return self.web3_client.web3.to_checksum_address(address)

    def fetch_tickers(self, market: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Fetchs the ticker from the beyond pricer smart contract.
        """

        if not self._markets:
            self.fetch_markets()

        tradeable = filter(lambda x: x["active"], self._markets)

        if market:
            tradeable = filter(lambda x: x["id"] == market, tradeable)

        return [market.to_json() for market in self._markets]  # type: ignore

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
        # use the lens

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
            Trade(int(order["amount"]) / 1e18, total_cost=int(order["premium"]) / -1e6)
            for order in position["optionsBoughtTransactions"]
        ]
        sells = [
            Trade(-int(order["amount"]) / 1e18, total_cost=-int(order["premium"]) / 1e6)
            for order in position["optionsSoldTransactions"]
        ]

        pnl_calculator.add_trades(buys + sells)

        symbol = to_human_format(position)

        if symbol in self.otokens:
            self._logger.debug(f"Found `{symbol}` in the otokens list.")
            book_side = "ask" if side == PositionSide.LONG else "bid"
            price = self.otokens[symbol][book_side]
            pnl_calculator.update_price(price)
        else:
            self._logger.debug(
                f"Could not find `{symbol}` in the otokens list. Maket is probably not active."
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
            "size": pnl_calculator.position_size,
            "info": position,
            "entryPrice": pnl_calculator.average_price,
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
        # we can now submit it to the chain;
        transaction["nonce"] = self.web3_client.web3.eth.get_transaction_count(
            self._crypto.address
        )
        submitted = self.web3_client.sign_and_sumbit(
            transaction, self._crypto.private_key
        )
        if submitted:
            self._logger.info(f"Order for {amount} {symbol} Successfully created!")
            self._logger.info(f"Transaction hash: {submitted}")
        else:
            self._logger.error(f"Order for {amount} {symbol} failed to create!")
            raise ValueError("Order failed to create.")
        return {
            "id": submitted,
            "symbol": symbol,
            "datetime": datetime.now(),
        }

    def buy_option(  # noqa: R0914
        self,
        market: str,
        amount: float,
        collateral_asset: str = "usdc",
        leverage: float = 1,
    ):
        """
        Create a buy option order.
        """
        self._logger.info(
            f"Buying {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )
        # we first check the approval amount of the collateral asset
        if not Collateral.is_supported(collateral_asset):
            raise ValueError(
                f"Collateral asset {collateral_asset} is not supported by the protocol."
            )
        collateral_contract = get_contract(collateral_asset, self.web3_client.web3)
        collateral_approved = self.web3_client.is_approved(
            collateral_contract,
            self.web3_client.option_exchange.address,
            str(self._crypto.address),
            int(amount * 1e18),
        )
        if not collateral_approved:
            self._logger.info(
                f"Approving {collateral_asset} collateral for {self.web3_client.option_exchange.address}"
            )

            txn = self.web3_client.create_approval(
                collateral_contract,
                self.web3_client.option_exchange.address,
                str(self._crypto.address),
                int(amount * 1e18),
            )
            # we submit and sign the transaction
            result = self.web3_client.sign_and_sumbit(txn, self._crypto.private_key)  # type: ignore
            if result is not None:
                self._logger.info(f"Transaction successful with hash: {result}")
            else:
                self._logger.error(f"Transaction failed: {result}")

        # now we can try to buy the option
        if not self._markets:
            self._logger.info("Fetching Tickers.")
            self.fetch_tickers()  # type: ignore

        # type: ignore
        rysk_option_market: RyskOptionMarket = [f for f in self._markets if f.name == market][0]  # type: ignore
        _amount = amount * 1000000000000000000
        acceptable_premium = self.web3_client.get_options_prices(  # type: ignore
            rysk_option_market.to_series(),
            rysk_option_market.dhv,
            side=OrderSide.BUY.value,
            amount=_amount,
        )  # pylint: disable=E1120

        # we format 2 decimal places
        self._logger.info(f"Acceptable premium: ${acceptable_premium:.2f}")

        series = rysk_option_market.to_series()  # type: ignore

        vault_id = 20
        user_vaults = self.web3_client.fetch_user_vaults(
            self._crypto.address
        )  # pylint: disable=E1120

        if not user_vaults:
            self._logger.info("No vaults found. Creating one.")
            raise NotImplementedError("No vaults found. Creating one.")
        # do we need to use an alternative aorder of operations?

        operate_tuple = [
            {
                "operation": 0,
                "operationQueue": [
                    {
                        "actionType": ActionType.DEPOSIT_COLLATERAL.value,
                        "owner": self._crypto.address,
                        "secondAddress": self.web3_client.option_exchange.address,
                        "asset": Collateral.from_symbol("weth").value,
                        "vaultId": vault_id,
                        "amount": 0,
                        "optionSeries": {
                            "expiration": 1,
                            "strike": 1,
                            "isPut": bool(series["isPut"]),
                            "underlying": NULL_ADDRESS,
                            "strikeAsset": NULL_ADDRESS,
                            "collateral": NULL_ADDRESS,
                        },
                        "indexOrAcceptablePremium": 0,
                        "data": "0x0000000000000000000000000000000000000000",
                    },
                    {
                        "actionType": ActionType.MINT_SHORT_OPTION.value,
                        "owner": NULL_ADDRESS,
                        "secondAddress": str(self._crypto.address),
                        "asset": NULL_ADDRESS,
                        "vaultId": 0,
                        "amount": int(_amount),
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
                        "amount": int(_amount),
                        "optionSeries": {
                            "expiration": int(series["expiration"]),
                            "strike": int(series["strike"]),
                            "isPut": True,
                            "underlying": Collateral.from_symbol("weth").value,
                            "strikeAsset": Collateral.from_symbol("usdc").value,
                            "collateral": Collateral.from_symbol("weth").value,
                        },
                        "indexOrAcceptablePremium": int(_amount),
                        "data": NULL_DATA,
                    },
                ],
            },
        ]

        # buy tx
        self._logger.info(f"Passing:\n{operate_tuple}")

        func = self.web3_client.option_exchange.functions.operate(
            operate_tuple
        ).buildTransaction({"from": self._crypto.address})
        return func

    def sell_option(  # pylint: disable=too-many-locals
        self,
        market: str,
        amount: float,
        collateral_asset: str = "weth",
        leverage: float = 1,
    ):
        """
        Create a sell option order.
        """
        self._logger.info(
            f"Selling {amount} of {market} with {collateral_asset} collateral @ {leverage}x leverage."
        )

        if not self._markets:
            self._logger.info("Fetching Tickers.")
            self.fetch_tickers()
        _amount = amount * 1e18

        rysk_option_market: RyskOptionMarket = [
            f for f in self._markets if f.name == market
        ][
            0
        ]  # type: ignore

        acceptable_premium = self.web3_client.get_options_prices(
            rysk_option_market.to_series(),
            dhv_exposure=rysk_option_market.dhv,
            amount=_amount,
            side=OrderSide.SELL.value,
            collateral=collateral_asset,
        )

        self._logger.info(f"Acceptable premium: ${acceptable_premium:.2f}")

        user_vaults = self.web3_client.fetch_user_vaults(self._crypto.address)
        otoken_id = self.web3_client.get_otoken(rysk_option_market.to_series())
        self._logger.info(f"Option Otoken id is {otoken_id}")

        if otoken_id not in set(i[1] for i in user_vaults):
            new_vault_id = len(user_vaults) + 1
            self._logger.info(
                f"Necessary to create a vault for the user. New vault id is {new_vault_id}"
            )
            vault_id = new_vault_id

        else:
            # we need to use the vault
            vault_id = [f[1] for f in user_vaults].index(otoken_id) + 1
            self._logger.info(f"Using existing vault id user_vaults {vault_id}")

        if rysk_option_market.is_put:
            collateral_asset = Collateral.USDC
            amount_to_approve = int(
                self._option_chain.current_price
                * amount
                * (1 + ALLOWED_SLIPPAGE)
                * 1e18
            )
            contract = self.web3_client.usdc
        else:
            collateral_asset = Collateral.WETH
            amount_to_approve = int(_amount * (1 + ALLOWED_SLIPPAGE))
            contract = self.web3_client.weth

        # we check the approval of the amount
        self._logger.info(
            f"Checking approval of {amount_to_approve / 1e18} of {collateral_asset}"
        )
        allowance = contract.functions.allowance(
            self._crypto.address,
            self.web3_client.option_exchange.address,
        ).call()
        self._logger.info(f"Allowance is {allowance}")
        if allowance < amount_to_approve:
            self._logger.info("Need to approve more collateral.")
            approve_tx = self.web3_client.create_approval(
                contract=contract,
                spender=self.web3_client.option_exchange.address,
                owner=self._crypto.address,
                amount=amount_to_approve,
            )

            self._logger.debug(f"Approve tx is {approve_tx}")
            tx_hash = self.web3_client.sign_and_sumbit(
                approve_tx, self._crypto.private_key
            )
            self._logger.info(f"Tx hash is {tx_hash}")
            if not tx_hash:
                raise ApprovalException("Approval failed.")
        # we need to create a vault

        underlying = Collateral.WETH.value
        strike_asset = Collateral.USDC.value

        operate_tuple = [
            {
                "operation": 0,
                "operationQueue": [
                    {
                        "actionType": ActionType.DEPOSIT_COLLATERAL.value,
                        "owner": self.to_checksum_address(self._crypto.address),
                        "secondAddress": self.to_checksum_address(
                            self.web3_client.option_exchange.address
                        ),
                        "asset": underlying,
                        "vaultId": vault_id,
                        "amount": int(_amount),
                        "optionSeries": {
                            "expiration": 1,
                            "strike": int(rysk_option_market.strike),
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
                        "owner": self.to_checksum_address(self._crypto.address),
                        "secondAddress": self.to_checksum_address(
                            self.web3_client.option_exchange.address
                        ),
                        "asset": self.to_checksum_address(otoken_id),
                        "vaultId": int(vault_id),
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
                        "actionType": int(ActionType.BURN_SHORT_OPTION.value),
                        "owner": NULL_ADDRESS,
                        "secondAddress": self.to_checksum_address(self._crypto.address),
                        "asset": NULL_ADDRESS,
                        "vaultId": int(0),
                        "amount": int(_amount),
                        "optionSeries": {
                            "expiration": int(rysk_option_market.expiration),
                            "strike": int(rysk_option_market.strike),
                            "isPut": bool(rysk_option_market.is_put),
                            "underlying": self.to_checksum_address(
                                underlying  # type: ignore
                            ),
                            "strikeAsset": self.to_checksum_address(
                                strike_asset  # type: ignore
                            ),
                            "collateral": self.to_checksum_address(
                                collateral_asset.value  # type: ignore
                            ),
                        },
                        "indexOrAcceptablePremium": int(
                            rysk_option_market.ask * (1 - ALLOWED_SLIPPAGE)
                        ),
                        "data": "0x0000000000000000000000000000000000000000",
                    }
                ],
            },
        ]

        self._logger.debug("Operate tuple is:")
        self._logger.debug(operate_tuple)

        operate_txn = self.web3_client.option_exchange.functions.operate(
            operate_tuple
        ).build_transaction({"from": self._crypto.address})
        return operate_txn

    def watch_trades(self):
        """Watch trades."""
        self._logger.info("Watching trades...")
        self.web3_client.watch_trades()

    def fetch_balances(self):
        """Fetch balances."""
        self._logger.info("Fetching balances...")
        return self.web3_client.get_balances()
