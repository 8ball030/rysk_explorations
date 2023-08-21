"""
Command line interface for rysk_client
"""

import csv
import os
import sys

import rich_click as click
from dotenv import load_dotenv

from rysk_client.client import RyskClient
from rysk_client.src.constants import (ARBITRUM, ARBITRUM_GOERLI,
                                       DEFAULT_ENCODING, NULL_ADDRESS)
from rysk_client.src.position_side import PositionSide
from rysk_client.src.utils import get_logger, render_table


def set_logger(ctx, level):
    """Set the logger."""
    if not hasattr(ctx, "logger"):
        ctx.logger = get_logger()
        ctx.logger.setLevel(level)
    return ctx.logger


def set_client(ctx):
    """Set the client."""
    # we use dotenv to load the env vars from DIRECTORY where the cli tool is executed
    _path = os.getcwd()
    env_path = os.path.join(_path, ".env")
    load_dotenv(dotenv_path=env_path)
    if not hasattr(ctx, "client"):
        auth = {
            "address": os.environ.get("ETH_ADDRESS"),
            "private_key": os.environ.get("ETH_PRIVATE_KEY"),
            "logger": ctx.logger,
            "verbose": ctx.logger.level == "DEBUG",
        }
        chain = os.environ.get("CHAIN")
        if chain == "arbitrum":
            chain = ARBITRUM
        else:
            chain = ARBITRUM_GOERLI
        ctx.client = RyskClient(**auth, chain=chain)
        if not ctx.client.web3_client.web3.isConnected():
            raise ConnectionError("Web3 client not connected.")
    return ctx.client


@click.group("Rysk client")
@click.option(
    "--log-level",
    "-l",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    help="Logging level.",
)
@click.pass_context
def cli(ctx, log_level):
    """Rysk client command line interface."""
    ctx.ensure_object(dict)
    ctx.obj["logger"] = set_logger(ctx, log_level)
    ctx.obj["client"] = set_client(ctx)


@cli.group("markets")
def markets():
    """Interact with markets."""


@cli.group("tickers")
def tickers():
    """Interact with tickers."""


@cli.group("positions")
def positions():
    """Interact with positions."""


@cli.group("trades")
def trades():
    """Interact with trades."""


@cli.group("balances")
@click.pass_context
def balances(ctx):  # pylint: disable=unused-argument
    """Interact with balances."""


@balances.command("fetch")
@click.pass_context
def fetch_balances(ctx):
    """Fetch balances."""
    client = ctx.obj["client"]
    columns = [
        "symbol",
        "balance",
    ]
    current_balances = [
        {"symbol": k, "balance": v} for k, v in client.fetch_balances().items()
    ]

    render_table("Balances", current_balances, columns)


@markets.command("fetch")
@click.option("--sort", "-s", default="expiration", help="Sort by column.")
@click.option("--is_active", "-a", default=True, help="Filter by active.")
@click.pass_context
def fetch_markets(ctx, sort, is_active):
    """Fetch markets."""
    client = ctx.obj["client"]
    markets = client.fetch_markets()
    if is_active:
        markets = [market for market in markets if market["active"]]

    columns = [
        "id",
        "expiration",
        "strike",
        "bid",
        "ask",
        "delta",
    ]
    sorted_markets = sorted(markets, key=lambda x: int(x[sort]))
    render_table("Markets", sorted_markets, columns)


@tickers.command("fetch")
@click.option("--sort", "-s", default="expiration", help="Sort by column.")
@click.option("--market", "-m", default=None, help="Filter by market.")
@click.pass_context
def fetch_tickers(ctx, sort, market):
    """Fetch tickers."""
    client = ctx.obj["client"]
    tickers = client.fetch_tickers(market)
    sorted_tickers = sorted(tickers, key=lambda x: int(x[sort]))
    columns = ["id", "expiration", "bid", "ask"]
    render_table("Tickers", sorted_tickers, columns)


@positions.command("list")
@click.option("--expired", "-e", is_flag=True, help="Include expired positions.")
@click.option("--market", "-m", default=None, help="Filter by market.")
@click.option("--is_open", "-o", is_flag=True, help="Filter by open positions")
@click.pass_context
def list_positions(ctx, expired, market, is_open):
    """List positions retriueved fromt the lens contract."""
    client = ctx.obj["client"]
    logger = ctx.obj["logger"]
    logger.info(
        f"Fetching positions for {client._crypto.address}"  # pylint: disable=protected-access
    )
    positions = client.fetch_positions(expired=expired)
    columns = [
        "symbol",
        "side",
        "entryPrice",
        "id",
        "size",
        "unrealizedPnl",
        "realizedPnl",
    ]
    if market:
        positions = [p for p in positions if p["symbol"] == market]
    if is_open:
        positions = [p for p in positions if p["size"] != 0]

    render_table("Positions", positions, columns)


@trades.command("watch")
@click.pass_context
def watch(ctx):
    """Watch trades as they occur on the contract."""
    client = ctx.obj["client"]
    client.watch_trades()


@positions.command("close")
@click.pass_context
@click.option("--market", "-m", required=True, help="Market to close.")
@click.option(
    "--size",
    "-s",
    required=False,
    help="Size to close. Default is All.",
    default=None,
    type=click.FLOAT,
)
def close(ctx, market, size):
    """Close a position."""
    client = ctx.obj["client"]
    logger = ctx.obj["logger"]
    user_address = client._crypto.address  # pylint: disable=protected-access
    positions = client.fetch_positions()
    if market not in (f["symbol"] for f in positions):
        raise ValueError(
            f"User {user_address} does not have an open position in {market}"
        )
    positions = [p for p in positions if p["symbol"] == market]
    position = [f for f in positions if f["size"] != 0]
    if len(position) > 1:
        raise ValueError(
            f"User {user_address} has multiple open positions in {market}. Please visit the Rysk UI to close positions."
        )
    if len(position) == 0:
        raise ValueError(
            f"User {user_address} does not have an open position in {market}"
        )
    position = position.pop()
    logger.info(f"Closing position for {user_address}")

    if position["side"] == PositionSide.LONG.value:
        txn = client.close_long(market, size)
    else:
        txn = client.close_short(market, size)

    if txn:
        logger.info(f"Transaction hash: {txn}")
    else:
        logger.info("No transaction hash returned. Check logs for errors.")


@positions.command("settle")
@click.option(
    "--vault_ids",
    "-v",
    required=True,
    type=click.STRING,
)
@click.pass_context
def settle(ctx, vault_ids):
    """Settle a position."""
    logger = ctx.obj["logger"]
    client = ctx.obj["client"]
    vault_ids_list = [int(vault_id) for vault_id in vault_ids.split(",")]
    user_address = client._crypto.address  # pylint: disable=protected-access

    logger.info(f"Settling vault {vault_ids} for {user_address}")
    if not client.web3_client.web3.is_connected():
        raise ConnectionError("Web3 client not connected.")
    vaults = dict(client.web3_client.fetch_user_vaults(user_address))
    for vault_id in vault_ids_list:

        if vault_id not in vaults:
            raise ValueError(f"Vault {vault_id} not found for {user_address}")
        if vaults[vault_id] == NULL_ADDRESS:
            raise ValueError(
                f"Vault {vault_id} has already been settled for {user_address}"
            )
    for vault_id in vault_ids_list:
        result = client.settle_vault(int(vault_id))
        if result:
            logger.info(f"Successfully settled vault {vault_id}. Transaction: {result}")
        else:
            logger.error(f"Failed to settle vault {vault_id}.")


# we pass a list of markets to redeem
@positions.command("redeem")
@click.option(
    "--markets",
    "-m",
    required=True,
    type=click.STRING,
    help="Comma separated list of markets to redeem. For example: ETH-02JUN23-1900-P, ETH-02JUN23-2000-P",
)
@click.pass_context
def redeem(ctx, markets):
    """Redeem a position."""
    logger = ctx.obj["logger"]
    client = ctx.obj["client"]
    markets_list = markets.split(",")
    user_address = client._crypto.address  # pylint: disable=protected-access
    logger.info(f"Redeeming {markets} for {user_address}")
    for market in markets_list:
        result = client.redeem_market(market)
        if result:
            logger.info(f"Successfully redeemed {market}. Transaction: {result}")
        else:
            logger.error(f"Failed to redeem {market}.")
            raise ValueError(f"Failed to redeem {market}.")


@positions.command("collateralize")
def collateralize():
    """Collateralize a position."""
    raise NotImplementedError


@trades.command("list")
@click.pass_context
@click.option("--to-csv", "-c", is_flag=True, help="Output to csv.", default=False)
def list_trades(ctx, to_csv):
    """List trades."""
    client = ctx.obj["client"]
    logger = ctx.obj["logger"]
    trades = client.fetch_trades()
    trades_list = []
    for trade in trades:
        trades_list.append(
            {
                "id": trade.id,
                "market": trade.market,
                "amount": trade.quantity,
                "price": trade.price,
            }
        )
    columns = [
        "id",
        "market",
        "amount",
        "price",
    ]
    render_table("Trades", trades_list, columns)
    if to_csv:
        with open("trades.csv", "w", encoding=DEFAULT_ENCODING) as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            for trade in trades_list:
                writer.writerow(trade.values())
        logger.info("Wrote trades to trades.csv")
    logger.info(f"Total trades: {len(trades)}")


@trades.command("create")
@click.option("--market", "-m", required=True, help="Market to trade.")
@click.option("--side", "-s", required=True, help="Buy or sell.")
@click.option(
    "--amount", "-a", required=True, type=click.FLOAT, help="Size of the trade."
)
@click.pass_context
def create_trade(ctx, market, side, amount):
    """Create a trade."""
    client = ctx.obj["client"]
    logger = ctx.obj["logger"]
    trade = client.create_order(market, amount, side)
    if not trade:
        logger.error("Failed to create trade.")
        sys.exit(1)
    logger.info(f"Created trade: {trade}")


if __name__ == "__main__":
    # we load the .env from the path of the directory we execute the command
    cli()  # pylint: disable=no-value-for-parameter
