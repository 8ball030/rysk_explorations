import json
from copy import deepcopy

from web3 import Web3

from rysk_client.src.constants import ADDRESSES, RPC_URL


def get_contract(name, w3):
    """Returns a web3 contract instance for the given contract name"""
    spec = ADDRESSES[name]
    with open(spec["path"], "r") as abi:
        abi = json.loads(abi.read())["abi"]
    res = deepcopy(spec)
    del res["path"]
    res["abi"] = abi
    return w3.eth.contract(**res)


def get_web3():
    """Returns a web3 instance connected to RPC_URL"""
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    return w3
