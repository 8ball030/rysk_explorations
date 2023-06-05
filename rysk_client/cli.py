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


@markets.command("fetch")
@click.option("--sort", "-s", default="expiration", help="Sort by column.")
@click.option("--is_active", "-a", default=True, help="Filter by active.")
def fetch_markets(sort, is_active):
    """Fetch markets."""
    client = RyskClient()
    markets = client.fetch_markets()
    if is_active:
        markets = [market for market in markets if market["active"]]

    def parse_dhv(market):
        """Get the dhv from the info."""
        market["dhv"] = int(int(market["info"]["netDHVExposure"]) / 1e18)

    for market in markets:
        parse_dhv(market)
    columns = ["symbol", "expiry", "strike", "dhv"]
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
    columns = ["symbol", "expiration", "bid", "ask"]
    render_table("Tickers", sorted_tickers, columns)


@positions.command("fetch")
def fetch_positions():
    """Fetch positions."""
    if "ETH_ADDRESS" not in os.environ:
        raise ValueError("ETH_ADDRESS environment variable not set.")
    if "ETH_PRIVATE_KEY" not in os.environ:
        raise ValueError("ETH_PRIVATE_KEY environment variable not set.")
    auth = {
        "address": os.environ["ETH_ADDRESS"],
        "private_key": os.environ["ETH_PRIVATE_KEY"],
        "logger": logger,
    }

    client = RyskClient(**auth)
    positions = client.fetch_positions()
    columns = ["symbol", "size", "price", "expiration"]
    render_table("Positions", positions, columns)


@trades.command("watch")
def watch():
    """Allows the user to watch trades as they occur on the contract."""
    client = RyskClient(logger=logger)
    client.watch_trades()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
