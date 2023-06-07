"""
Command line interface for rysk_client
"""

import os

import rich_click as click

from rysk_client.client import RyskClient
from rysk_client.src.utils import get_logger, render_table

global logger  # pylint: disable=W0604
logger = get_logger()


@click.group("Rysk client")
@click.option(
    "--log-level",
    "-l",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    help="Logging level.",
)
def cli(log_level):
    """Rysk client command line interface."""
    logger.setLevel(log_level)


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
def balances():
    """Interact with balances."""


@markets.command("fetch")
@click.option("--sort", "-s", default="expiration", help="Sort by column.")
@click.option("--is_active", "-a", default=True, help="Filter by active.")
def fetch_markets(sort, is_active):
    """Fetch markets."""
    client = RyskClient()
    markets = client.fetch_markets()
    if is_active:
        markets = [market for market in markets if market["active"]]

    columns = [
        "id",
        "expiration",
        "strike",
        "bid",
        "ask",
    ]
    sorted_markets = sorted(markets, key=lambda x: int(x[sort]))
    render_table("Markets", sorted_markets, columns)


@tickers.command("fetch")
@click.option("--sort", "-s", default="expiration", help="Sort by column.")
@click.option("--market", "-m", default=None, help="Filter by market.")
def fetch_tickers(sort, market):
    """Fetch tickers."""
    client = RyskClient()
    tickers = client.fetch_tickers(market)
    sorted_tickers = sorted(tickers, key=lambda x: int(x[sort]))
    columns = ["id", "expiration", "bid", "ask"]
    render_table("Tickers", sorted_tickers, columns)


@positions.command("list")
def list_positions():
    """List positions."""
    if "ETH_ADDRESS" not in os.environ:
        raise ValueError("ETH_ADDRESS environment variable not set.")
    if "ETH_PRIVATE_KEY" not in os.environ:
        raise ValueError("ETH_PRIVATE_KEY environment variable not set.")
    auth = {
        "address": os.environ["ETH_ADDRESS"],
        "private_key": os.environ["ETH_PRIVATE_KEY"],
        "logger": logger,
    }
    logger.info(f"Fetching positions for {auth['address']}")

    client = RyskClient(**auth)
    positions = client.fetch_positions()
    columns = [
        "symbol",
        "side",
        "entryPrice",
        "id",
        "size",
        "unrealizedPnl",
        "realizedPnl",
    ]
    render_table("Positions", positions, columns)


@trades.command("watch")
def watch():
    """Watch trades as they occur on the contract."""
    client = RyskClient(logger=logger)
    client.watch_trades()


@positions.command("close")
def close():
    """Close a position."""
    client = RyskClient(logger=logger)
    assert client.web3_client.web3.isConnected()
    raise NotImplementedError


@positions.command("settle")
def settle():
    """Settle a position."""
    client = RyskClient(logger=logger)
    assert client.web3_client.web3.isConnected()
    raise NotImplementedError


@positions.command("redeem")
def redeem():
    """Redeem a position."""
    client = RyskClient(logger=logger)
    assert client.web3_client.web3.isConnected()
    raise NotImplementedError


@positions.command("collateralize")
def collateralize():
    """Collateralize a position."""
    client = RyskClient(logger=logger)
    assert client.web3_client.web3.isConnected()
    raise NotImplementedError


@trades.command("list")
def list_trades():
    """List trades."""
    client = RyskClient(logger=logger)
    assert client.web3_client.web3.isConnected()
    raise NotImplementedError  # disable=raising-to-general-error


@trades.command("create")
@click.option("--market", "-m", required=True, help="Market to trade.")
@click.option("--side", "-s", required=True, help="Buy or sell.")
@click.option(
    "--amount", "-a", required=True, type=click.FLOAT, help="Size of the trade."
)
def create_trade(market, side, amount):
    """Create a trade."""
    auth = {
        "address": os.environ["ETH_ADDRESS"],
        "private_key": os.environ["ETH_PRIVATE_KEY"],
        "logger": logger,
    }

    logger.info(f"Creating trade for {auth['address']} on {market} for {amount} {side}")
    client = RyskClient(**auth)
    trade = client.create_order(market, amount, side)
    logger.info(f"Created trade: {trade}")


@balances.command("fetch")
def fetch_balances():
    """Fetch balances."""
    auth = {
        "address": os.environ["ETH_ADDRESS"],
        "logger": logger,
    }
    client = RyskClient(**auth)

    columns = [
        "symbol",
        "balance",
    ]
    current_balances = [
        {"symbol": k, "balance": v} for k, v in client.fetch_balances().items()
    ]

    render_table("Balances", current_balances, columns)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
