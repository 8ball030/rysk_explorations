"""
Collection of tests to check known contract calls against a fork.
"""
import subprocess
import time
from dataclasses import dataclass
from multiprocessing import Process
from typing import Optional

import psutil
import pytest
import requests

from rysk_client.src.rysk_option_market import RyskOptionMarket
from tests.constants import DEFAULT_FORK_BLOCK_NUMBER


@dataclass
class LocalFork:
    """Use a local fork to test contract calls."""

    fork_url: str
    fork_block_number: int

    host: str = "http://0.0.0.0"
    port: int = 8545
    process: Optional[Process] = None

    def stop(self):
        """Stop the local fork."""
        for child in psutil.Process(self.process.pid).children(recursive=True):
            child.kill()
        self.process.kill()
        self.process.terminate()

    def is_ready(self):
        """Check if the local fork is ready."""
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
        if res.status_code != 200:
            return False
        return int(res.json()["result"], 16) == self.fork_block_number

    def run(self):
        """Run the local fork in a background process."""
        run_command = f"anvil --fork-url {self.fork_url} --fork-block-number {self.fork_block_number}"
        self.process = Process(
            target=subprocess.run,
            args=(run_command,),
            kwargs={
                "shell": True,
                "check": True,
                "stdout": subprocess.PIPE,
                "stderr": subprocess.STDOUT,
            },
            daemon=True,
        )
        self.process.start()
        wait = 0
        while not self.is_ready():
            time.sleep(1)
            wait += 1
            if wait > 10:
                raise TimeoutError("Local fork did not start in time.")


def test_local_fork(local_fork):
    """Test that the local fork is running."""
    assert local_fork.process.is_alive()


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
