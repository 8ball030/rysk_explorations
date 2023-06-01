"""
This file contains all the constants used in the rysk_client package.
"""
DEFAULT_TIMEOUT = 10
DEFAULT_ENCODING = "utf-8"
SUBGRAPH_URL = "https://api.goldsky.com/api/public/project_clhf7zaco0n9j490ce421agn4/subgraphs/devey/0.0.2/gn"
NULL_ADDRESS = "0x0000000000000000000000000000000000000000"
SUPPORTED_LEVERAGES = [1, 1.5, 2, 3]

raw_data = {
    "localhost": {},
    "arbitrum": {
        "OpynController": "0x594bD4eC29F7900AE29549c140Ac53b5240d4019",
        "OpynAddressBook": "0xCa19F26c52b11186B4b1e76a662a14DA5149EA5a",
        "OpynOracle": "0xBA1880CFFE38DD13771CB03De896460baf7dA1E7",
        "OpynNewCalculator": "0x749a3624ad2a001F935E3319743f53Ecc7466358",
        "OpynOptionRegistry": "0x04706DE6cE851a284b569EBaE2e258225D952368",
        "priceFeed": "0xA5a095f2a2Beb2d53382293b0FfE0f520dDEC297",
        "volFeed": "0x3099900e3E9Fa62B291586f5046A09CF5b0Bccb9",
        "optionProtocol": "0x08674f64DaC31f36828B63A4468A3AC3C68Db5B2",
        "liquidityPool": "0xC10B976C671Ce9bFf0723611F01422ACbAe100A5",
        "authority": "0x0c83E447dc7f4045b8717d5321056D4e9E86dCD2",
        "portfolioValuesFeed": "0x14eF340B33bD4f64C160E3bfcD2B84D67E9b33dF",
        "optionHandler": "0xA802795269588bf33739816f76B53fD6cd099b27",
        "opynInteractions": "0x048603543a0FD41B56B831B80981Addb19C1Ea30",
        "normDist": "0xee4CfA50123109DF8DBA8CeB37d3eA94addC4A02",
        "BlackScholes": "0x2c215B6BaC6a4871C2e58669F0437853Da500020",
        "optionsCompute": "0x303956BCC420B3b74b861874d39BaD5d5eE341f0",
        "accounting": "0xd527BE017Be2C3d3d14D6bdF5C796E26bA0c5EE8",
        "uniswapV3HedgingReactor": "0x933589C46233Efa8cCDe8287E077cA6CC51Bec17",
        "perpHedgingReactor": "0xDd418b4Ec8396191D08957bD42F549e215B8e89a",
        "USDC": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    },
    "arbitrumGoerli": {
        "OpynController": "0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2",
        "OpynAddressBook": "0xd6e67bF0b1Cdb34C37f31A2652812CB30746a94A",
        "OpynOracle": "0x35578F5A49E1f1Cf34ed780B46A0BdABA23D4C0b",
        "OpynNewCalculator": "0xcD270e755C2653e806e16dD3f78E16C89B7a1c9e",
        "OpynOptionRegistry": "0x48A74b742bd97545ace8B0876F5BA7ED19DF6579",
        "priceFeed": "0xDcA6c35228acb82363406CB2e7eee81B40c692aE",
        "volFeed": "0x9Fc909273C6aF5b6fFd389Fa2B44492ff88a3be6",
        "optionProtocol": "0x865Bd85b7275a33C87E8a7E31a125DD6338e6747",
        "liquidityPool": "0x2ceDe96cd46C9B751EeB868A57FEDeD060Dbe6Bf",
        "authority": "0xA524f4F9046a243c67A07dDE2D9477bf320Ed89E",
        "portfolioValuesFeed": "0xbFC1eDc5c07ada83e0244b37A784486633910cD7",
        "optionHandler": "0x8a265fa22aa5AF86fa763dC2cF04661bf06A52E6",
        "opynInteractions": "0x5e5A98E2F7c71B159B9Ed771E4138d4B2464708c",
        "normDist": "0xf63395764CAA20a54bF33fdCCdbC03b2BDc67453",
        "BlackScholes": "0x8D3ac248d2598c0C43e1D48e5ad59093F9Cb1d40",
        "optionsCompute": "0x8090b463afd758B59089905dc956300824cb2388",
        "accounting": "0xCCc6ebF870aCcD83043e8dafaeB4366A4D1a2836",
        "uniswapV3HedgingReactor": "0xE5b8F3b414a80b8C40ba438292Eb37918324d285",
        "perpHedgingReactor": "0x34f5c89fC6b053728F264cd7f9F1cdFB887AEf86",
        "USDC": "0x6775842ae82bf2f0f987b10526768ad89d79536e",
        "WETH": "0x53320bE2A35649E9B2a0f244f9E9474929d3B699",
    },
}

ADDRESSES = {
    "beyond_pricer": {
        "path": "./contracts/BeyondPricer.sol/BeyondPricer.json",
        "address": "0xc939df369C0Fc240C975A6dEEEE77d87bCFaC259",
    },
    "opyn_controller": {
        "path": "contracts/packages/opyn/core/Controller.sol/Controller.json",
        "address": "0x11a602a5F5D823c103bb8b7184e22391Aae5F4C2",
    },
    "option_exchange": {
        "path": "contracts/OptionExchange.sol/OptionExchange.json",
        "address": "0xb672fE86693bF6f3b034730f5d2C77C8844d6b45",
    },
    "option_registry": {
        "path": "contracts/OptionRegistry.sol/OptionRegistry.json",
        "address": "0x48A74b742bd97545ace8B0876F5BA7ED19DF6579",
    },
    "option_catalogue": {
        "path": "contracts/OptionCatalogue.sol/OptionCatalogue.json",
        "address": "0xde458dD32651F27A8895D4a92B7798Cdc4EbF2f0",
    },
    "usdc": {
        "path": "contracts/interfaces/I_ERC20.sol/I_ERC20.json",
        "address": "0x6775842AE82BF2F0f987b10526768Ad89d79536E",
    },
    "weth": {
        "path": "contracts/interfaces/I_ERC20.sol/I_ERC20.json",
        "address": "0x53320bE2A35649E9B2a0f244f9E9474929d3B699",
    },
}

RPC_URL = "https://arbitrum-goerli.rpc.thirdweb.com"
