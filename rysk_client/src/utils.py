"""
Helper functions for the rysk_client package.
"""
import json
import os
from copy import deepcopy

from web3 import Web3

from rysk_client.src.constants import ADDRESSES, DEFAULT_ENCODING, RPC_URL


def get_contract(name, web3):
    """Returns a web3 contract instance for the given contract name"""
    path = os.path.join(os.path.dirname(__file__), "..")
    spec = ADDRESSES[name]
    with open(f"{path}/{spec['path']}", "r", encoding=DEFAULT_ENCODING) as abi:
        abi = json.loads(abi.read())["abi"]
    res = deepcopy(spec)
    del res["path"]
    res["abi"] = abi
    return web3.eth.contract(**res)


def get_web3() -> Web3:
    """Returns a web3 instance connected to RPC_URL"""
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    return web3
