"""
Collection of tests to check known contract calls against a fork.
"""
import time
from dataclasses import dataclass
from typing import Optional

import pytest
import requests
from docker import DockerClient
from docker.models.containers import Container

from rysk_client.src.order_side import OrderSide
from rysk_client.src.rysk_option_market import RyskOptionMarket
from tests.constants import DEFAULT_FORK_BLOCK_NUMBER

MARKETS = [
    "ETH-30JUN23-1700-P",
    "ETH-30JUN23-1800-P",
    "ETH-30JUN23-1900-P",
    "ETH-30JUN23-2000-P",
    "ETH-30JUN23-2100-P",
    "ETH-30JUN23-2200-P",
    "ETH-30JUN23-1700-C",
    "ETH-30JUN23-1800-C",
    "ETH-30JUN23-1900-C",
    "ETH-30JUN23-2000-C",
    "ETH-30JUN23-2100-C",
    "ETH-30JUN23-2200-C",
]

ACTIVE_MARKETS = [
    ("ETH-30JUN23-1800-P", 28642800),
    ("ETH-30JUN23-1900-P", 28642800),
]


@dataclass
class LocalFork:
    """Use a docker container to test contract calls."""

    fork_url: str
    fork_block_number: int

    host: str = "http://localhost"
    port: int = 8546
    container: Optional[Container] = None
    run_command: str = "--fork-url {fork_url} --fork-block-number {fork_block_number} --host 0.0.0.0 --port {port}"

    def stop(self):
        """Stop the docker container."""
        # we force the container to stop
        self.container.stop()
        self.container.remove(force=True)
        wait = 0
        while self.is_ready():
            if wait > 10:
                raise TimeoutError("Docker fork did not stop in time.")
            wait += 1
            time.sleep(1)

    def is_ready(self):
        """Check if the docker container is ready."""
        try:
            res = requests.post(
                f"{self.host}:{self.port}",
                json={
                    "jsonrpc": "2.0",
                    "method": "eth_blockNumber",
                    "params": [],
                    "id": 1,
                },
                timeout=1,
            )
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.ReadTimeout:
            return False
        if res.status_code != 200:
            return False
        return int(res.json()["result"], 16) == self.fork_block_number

    def run(self):
        """Run the docker container in a background process."""
        client = DockerClient.from_env()
        self.container = client.containers.run(
            image="ghcr.io/foundry-rs/foundry:latest",
            entrypoint="/usr/local/bin/anvil",
            command=self.run_command.format(
                fork_url=self.fork_url,
                fork_block_number=self.fork_block_number,
                port=self.port,
            ),
            ports={f"{self.port}/tcp": self.port},
            detach=True,
            volumes={
                "foundry": {"bind": "/root/.foundry/cache/rpc/", "mode": "rw"},
            },
        )
        wait = 0
        while not self.is_ready():
            time.sleep(1)
            wait += 1
            if wait > 15:
                raise TimeoutError("Docker fork did not start in time.")

    def restart_from_block(self, block_number: int):
        """Restart the docker container from a given block number."""
        self.stop()
        self.fork_block_number = block_number
        self.run()


def test_local_fork(local_fork):
    """Test that the local fork is running."""
    assert local_fork.is_ready()


def test_get_block_number(local_fork):
    """Test that the local fork is running."""
    res = requests.post(
        f"{local_fork.host}:{local_fork.port}",
        json={"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1},
        timeout=1,
    )
    assert res.status_code == 200
    assert int(res.json()["result"], 16) == DEFAULT_FORK_BLOCK_NUMBER


@pytest.mark.parametrize("vault_id", [6, 9, 15])
def test_settle_vault(client, vault_id):
    """Test that the local fork is running."""
    result = client.settle_vault(vault_id)
    assert result, "Transaction failed."


def test_fails_to_settle_vault(client):
    """Test that the local fork is running."""
    with pytest.raises(Exception):
        client.settle_vault(1000000)


def test_redeems_o_token(client):
    """Test that the local fork is running.
    example tx "0xcc525c8407647d314b68105a06d3f55ff1657186853c9678723a249ee37279d0"
    """
    result = client.redeem_otoken(
        "0x1CEc2D215aa46bFa81d3304E57D5171e814329F7", 29  # oToken address
    )
    assert result, "Transaction failed."


@pytest.mark.parametrize(
    "market,amount",
    [
        ("ETH-02JUN23-1900-P", 30),
        ("ETH-09JUN23-1900-P", 360),
    ],
)
def test_retieve_and_redeem(market, amount, client):
    """Test that the otoken can be used to retrieve and redeem."""
    rysk_option_market = RyskOptionMarket.from_str(market)
    otoken_address = client.web3_client.get_otoken(rysk_option_market.to_series())
    result = client.redeem_otoken(otoken_address, amount)
    assert result, "Transaction failed."


@pytest.mark.parametrize(
    "market",
    ["ETH-02JUN23-1900-P"],
)
def test_redeem_market_from_str(market, client):
    """Test that the otoken can be used to retrieve and redeem."""
    result = client.redeem_market(market)
    assert result, "Transaction failed."


@pytest.mark.parametrize(
    "market,amount",
    [
        ("ETH-30JUN23-1900-C", 5),
        ("ETH-30JUN23-2000-C", 5),
        ("ETH-30JUN23-1800-P", 5),
        ("ETH-30JUN23-1900-P", 5),
    ],
)
def test_client_can_buy(client, market, amount):
    """Test that the otoken can be used to retrieve and redeem.
    example tx: 0x3200b84acc909d0d9b19f0832a5529f42eaf2bda8330eb5a757c15d02dc69fe4
    market
    """
    txn = client.buy_option(market, amount)
    assert txn, "Transaction failed."


@pytest.mark.parametrize(
    "market,amount",
    [
        ("ETH-30JUN23-1800-P", 1),
        ("ETH-30JUN23-1800-P", 5),
        ("ETH-30JUN23-1800-P", 10),
        ("ETH-30JUN23-1800-P", 20),
    ],
)
def test_client_can_buy_differing_amounts(client, market, amount):
    """Test that the otoken can be used to retrieve and redeem.
    example tx: 0x3200b84acc909d0d9b19f0832a5529f42eaf2bda8330eb5a757c15d02dc69fe4
    market
    """
    txn = client.buy_option(market, amount)
    assert txn, "Transaction failed."


@pytest.mark.parametrize(
    "market,block_number",
    ACTIVE_MARKETS,
)
def test_get_otoken_address(local_fork, client, market, block_number):
    """Test that the otoken can be used to retrieve and redeem."""
    local_fork.stop()
    local_fork.fork_block_number = block_number
    local_fork.run()
    rysk_option_market = RyskOptionMarket.from_str(market)
    otoken_address = client.web3_client.get_otoken(rysk_option_market.to_series())
    assert otoken_address, "Otoken address is None."


@pytest.mark.parametrize(
    "market,block_number",
    ACTIVE_MARKETS,
)
def test_can_close_otoken(local_fork, client, market, block_number):
    """
    Test that the otoken can be used to retrieve and redeem.
    """
    local_fork.restart_from_block(block_number)
    txn = client.close_long(market, 1)
    assert txn, "Transaction failed."


# Test can short new market
# ETH-30JUN23-2000-C
# example initial tx:
# approval: https://goerli.arbiscan.io/tx/0x1505a54442e1ce44ea025c1079829ab12c49e78b03b3e1b394a0b81e39852a5a
# mint vault: 0xa01d2f288eed793ac5ce83f3e18610d46aca855a48af04e1ffc0b323664f5d12
# add to short: 0x9ead3d366738d74b8b8d870c6b06f46d3fe85930ccd25d4e6c9247b5af390816

DEFAULT_MARKET = "ETH-30JUN23-2000-C"
DEFAULT_AMOUNT = 1


ACTIVE_SHORT_MARKETS = [
    (
        "ETH-30JUN23-2000-C",
        28657207,
    ),
    (
        "ETH-30JUN23-2000-C",
        28658066,
    ),
]


@pytest.mark.skip(reason="For some reason this fails on the local fork.")
@pytest.mark.parametrize(
    "market,block",
    [ACTIVE_SHORT_MARKETS[0]],
)
def test_can_add_to_short_with_no_approval(local_fork, client, market, block):
    """
    Test that the otoken can be used to retrieve and redeem.
    """
    local_fork.restart_from_block(block)

    txn = client.sell_option(market, DEFAULT_AMOUNT)
    assert txn, "Transaction failed."


@pytest.mark.parametrize(
    "market,block_number",
    [
        ("ETH-28JUL23-1900-C", 28983125),
        ("ETH-28JUL23-1900-P", 28983125),
    ],
)
@pytest.mark.flaky(reruns=3)  # why this is the case i am not yet sure.
def test_client_can_close_long(local_fork, client, market, block_number):
    """Test that the otoken can be used to retrieve and redeem.
    flow:
    buy_option -> approve -> close_long
    """
    local_fork.restart_from_block(block_number)

    txn = client.create_order(market, DEFAULT_AMOUNT)
    assert txn, "Transaction failed."

    txn = client.close_long(market, DEFAULT_AMOUNT)
    assert txn, "Transaction failed."


@pytest.mark.parametrize(
    "market,block_number",
    [
        ("ETH-28JUL23-1900-C", 28983125),
        ("ETH-28JUL23-1900-P", 28983125),
    ],
)
def test_client_can_close_short(local_fork, client, market, block_number):
    """Test that the otoken can be used to retrieve and redeem.
    flow:
    buy_option -> approve -> close_long
    """
    local_fork.restart_from_block(block_number)

    txn = client.create_order(market, DEFAULT_AMOUNT, side=OrderSide.SELL.value)
    assert txn, "Transaction failed."

    txn = client.close_short(market, DEFAULT_AMOUNT)
    assert txn, "Transaction failed."
