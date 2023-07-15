"""
Helper functions for the rysk_client package.
"""
import json
import logging
import sys
from dataclasses import asdict
from typing import List, Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from web3 import Web3

from rysk_client.src.constants import (ARBITRUM_GOERLI, DEFAULT_ENCODING,
                                       PROTOCOL_DEPLOYMENTS)


def get_logger():
    """Get the logger."""
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter("%(message)s")

    # we check if the logger already has a handler
    # to avoid adding multiple handlers
    if logger.hasHandlers():
        return logger
    if sys.stdout.isatty():

        handler = RichHandler(
            markup=False,
            rich_tracebacks=True,
            locals_max_string=None,
            locals_max_length=None,
        )
    else:
        handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def get_contract(name, web3, chain, address=None):
    """Returns a web3 contract instance for the given contract name"""
    spec = PROTOCOL_DEPLOYMENTS[chain.name].contracts[name]

    with open(spec.path, "r", encoding=DEFAULT_ENCODING) as abi:
        abi = json.loads(abi.read())["abi"]
    res = asdict(spec)
    del res["path"]
    res["abi"] = abi
    if address is not None:
        res["address"] = address
    return web3.eth.contract(**res)


def get_web3(chain=ARBITRUM_GOERLI) -> Web3:
    """Returns a web3 instance connected to RPC_URL"""

    web3 = Web3(Web3.HTTPProvider(chain.rpc_url))
    return web3


def render_table(title: str, data, cols: Optional[List[str]] = None):
    """Render a table from a dynamic input."""
    table = Table(title=title)
    # we first create the columns

    if cols is None:
        columns = []
        for row in data:
            for column in row.keys():
                if column not in columns:
                    columns.append(column)
    else:
        columns = cols

    for column in columns:
        table.add_column(column)
    # then we add the rows
    for row in data:
        table.add_row(*[str(row.get(column, "")) for column in columns])
    console = Console()
    console.print(table)
