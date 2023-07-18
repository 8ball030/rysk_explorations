"""
This file contains all the constants used in the rysk_client package.
"""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


def from_camel_case_to_snake_case(string: str):
    """Convert a string from camel case to snake case.
    Note: If the string is all uppercase, it will be converted to lowercase.
    """
    if string.isupper():
        return string.lower()
    return "".join("_" + c.lower() if c.isupper() else c for c in string).lstrip("_")


DEFAULT_TIMEOUT = 10
DEFAULT_ENCODING = "utf-8"
NULL_ADDRESS = "0x0000000000000000000000000000000000000000"
NULL_DATA = "0x0000000000000000000000000000000000000000"
SUPPORTED_LEVERAGES = [1, 1.5, 2, 3]
EMPTY_SERIES = {
    "expiration": 1,
    "strike": 1,
    "isPut": True,
    "collateral": NULL_ADDRESS,
    "underlying": NULL_ADDRESS,
    "strikeAsset": NULL_ADDRESS,
}


CONTRACT_ADDRESSES = {
    "arbitrum": {
        "OpynController": "0x594bD4eC29F7900AE29549c140Ac53b5240d4019",
        "OpynOracle": "0xBA1880CFFE38DD13771CB03De896460baf7dA1E7",
        "OpynNewCalculator": "0x749a3624ad2a001F935E3319743f53Ecc7466358",
        "OpynOptionRegistry": "0x8Bc23878981a207860bA4B185fD065f4fd3c7725",
        "priceFeed": "0x7f86AC0c38bbc3211c610abE3841847fe19590A4",
        "liquidityPool": "0x217749d9017cB87712654422a1F5856AAA147b80",
        "portfolioValuesFeed": "0x7f9d820CFc109686F2ca096fFA93dd497b91C073",
        "optionHandler": "0xc63717c4436043781a63C8c64B02Ff774350e8F8",
        "optionExchange": "0xC117bf3103bd09552F9a721F0B8Bce9843aaE1fa",
        "beyondPricer": "0xeA5Fb118862876f249Ff0b3e7fb25fEb38158def",
        "d_h_v_lens": "0x10779CAE21C91897a5AdD1831Ffb813803c7fcf1",
        "UserPositionLens": "0x02eFd4e61C1883A0FfF1044ACd61c9100859336c",
        "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "weth": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "o_token": "0x1d96E828e0Aa743783919B24ccDB971504a96C77",
    },
    "arbitrum-goerli": {
        "OpynController": "0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2",
        "OpynOracle": "0x35578F5A49E1f1Cf34ed780B46A0BdABA23D4C0b",
        "OpynNewCalculator": "0xcD270e755C2653e806e16dD3f78E16C89B7a1c9e",
        "OpynOptionRegistry": "0x4E89cc3215AF050Ceb63Ca62470eeC7C1A66F737",
        "priceFeed": "0xf7B1e3a7856067BEcee81FdE0DD38d923b99554D",
        "liquidityPool": "0x0B1Bf5fb77AA36cD48Baa1395Bc2B5fa0f135d8C",
        "portfolioValuesFeed": "0x84fbb7C0a210e5e3A9f7707e1Fb725ADcf0CF528",
        "optionHandler": "0x1F63F3B37f818f05ebefaCa11086e5250958e0D8",
        "optionExchange": "0xb672fE86693bF6f3b034730f5d2C77C8844d6b45",
        "beyondPricer": "0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259",
        "UserPositionLens": "0xa6e2ebD13Cbb085659fB8Ce87fAFdF052066017f",
        "d_h_v_lens": "0xFC2245435e38C6EAd5Cb05ac4ef536A6226eCacb",
        "usdc": "0x408c5755b5c7a0a28D851558eA3636CfC5b5b19d",
        "weth": "0x3b3a1dE07439eeb04492Fa64A889eE25A130CDd3",
        "o_token": "0xB19d2eA6f662b13F530CB84B048877E5Ed0bD8FE",
    },
}


@dataclass
class Contract:
    """Contract dataclass."""

    path: str
    address: str


@dataclass
class Chain:
    """Chain dataclass."""

    name: str
    chain_id: int
    rpc_url: str
    wss_url: str

    def __hash__(self) -> int:
        """Hash the chain."""
        return hash(self.chain_id)


@dataclass
class ProtocolDeployment:
    """Protocol deployment dataclass."""

    name: str
    contracts: Dict[str, Contract]
    chain: Chain
    subgraph_url: Optional[str] = None


WS_URL = "wss://quaint-billowing-morning.arbitrum-goerli.discover.quiknode.pro/def6c4c783fc626cb8a07d38f845b76b458e6e84"
ARBITRUM = Chain(
    name="arbitrum",
    chain_id=42161,
    rpc_url="https://arbitrum.public-rpc.com",
    wss_url="wss://arb1.arbitrum.io/ws",
)
ARBITRUM_GOERLI = Chain(
    name="arbitrum-goerli",
    chain_id=421613,
    rpc_url="https://arbitrum-goerli.rpc.thirdweb.com",
    wss_url=WS_URL,
)

LOCAL_FORK = Chain(
    name="local-fork",
    chain_id=421611,
    rpc_url="http://localhost:8545",
    wss_url="ws://localhost:8545",
)


PROTOCOL_DEPLOYMENTS = {}
SUPPORTED_CHAINS = [ARBITRUM, ARBITRUM_GOERLI]


CHAINS_TO_SUBGRAPH_URL = {
    ARBITRUM: "https://api.goldsky.com/api/public/project_clhf7zaco0n9j490ce421agn4/subgraphs/arbitrum-one/0.1.17/gn",
    ARBITRUM_GOERLI: "https://api.goldsky.com/api/public/project_clhf7zaco0n9j490ce421agn4/subgraphs/devey/0.1.17/gn",
}

for chain in SUPPORTED_CHAINS:
    for name, address in CONTRACT_ADDRESSES[chain.name].items():
        PROTOCOL_DEPLOYMENTS[chain.name] = ProtocolDeployment(
            name=name,
            contracts={
                from_camel_case_to_snake_case(name): Contract(
                    path=Path(os.path.dirname(__file__))
                    / ".."
                    / "packages"
                    / "eightballer"
                    / "contracts"
                    / from_camel_case_to_snake_case(name)
                    / "build"
                    / f"{from_camel_case_to_snake_case(name)}.json",
                    address=address,
                )
                for name, address in CONTRACT_ADDRESSES[chain.name].items()
            },
            chain=chain,
            subgraph_url=CHAINS_TO_SUBGRAPH_URL[chain],
        )


CHAIN_ID_TO_DEPLOYMENT = {
    deploy.chain.chain_id: deploy for deploy in PROTOCOL_DEPLOYMENTS.values()
}

WETH_MULTIPLIER = 1e18
USDC_MULTIPLIER = 1e6
