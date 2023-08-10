# Rysk Client

The rysk python client offers a programatic means by which to interact with the (Rysk Finance Protocol).

The DHV is a hybrid AMM and RFQ options protocol, generating uncorrelated returns for its liquidity providers whilst enabling anyone to trade (buy and sell) options with a wide range of strike prices and expiry dates. The DHV uses a dynamic approach in hedging risk to generate market-neutral uncorrelated returns for liquidity providers.

The Rysk client is a python client that allows users to interact with the [Rysk protocol](https://app.rysk.finance). The client is built on top of the web3.py and the [Open-Aea](https://github.com/valory-xyz/open-aea) python libraries. The client allows users to interact with the Rysk protocol in a programatic manner.



## Installation

The application is available on pypi and can be installed as so

```bash
pip install rysk-client
```

## Cli Tool

The application is also bundled as cli tool to allow users to interact with the protocol from the cli.




![alt text](demo.gif "Title")


## Creating a Client 

Clients can be created from the rysk client module using python code.


```python
from rysk_client.client import RyskClient
from tests.conftest import DEFAULT_ADDRESS

auth = {
    "address": DEFAULT_ADDRESS,
}

client = RyskClient(**auth)
client

```

    {'address': '0x9B8a204636a7aa9c33053d9C3A828720d32212e8'}
    Rysk client initialized and connected to the blockchain at RPC connection https://arbitrum-goerli.rpc.thirdweb.com





    RyskClient(_markets=[], _tickers=[], _otokens={}, web3_client=<rysk_client.web3_client.Web3Client object at 0x7f1df5ff0670>)



### Markets
We can fetch data about the markets as so;


```python
markets = client.fetch_markets()
markets[0]
```




    {'id': 'ETH-29SEP23-1800-C',
     'strike': 1800.0,
     'expiration': 1695974400,
     'optionType': 'call',
     'active': True,
     'delta': 0.6189098962288028,
     'bid': 121.382234,
     'ask': 130.231078,
     'dhv': 0.1}



## Fetching Tickers

Tickers can be fetched from the client as so;


```python
tickers = client.fetch_tickers()
tickers[0]
```




    {'id': 'ETH-29SEP23-1800-C',
     'strike': 1800.0,
     'expiration': 1695974400,
     'optionType': 'call',
     'active': True,
     'delta': 0.6189098962288028,
     'bid': 121.382234,
     'ask': 130.231078,
     'dhv': 0.1}



## Fetching Positions
Positions are fetched from the client such that a user can retrieve their positions.

Positions are indicated by a vault id.

The vaultid iterates when a new position is created. 

Vaultid can be retrieved from;






```python
positions = client.fetch_positions()
positions[0]
```




    {'id': '0x9b8a204636a7aa9c33053d9c3a828720d32212e8-0x5c82b8d5a5306c48e9ac5fc07559a6961bd1ad1e-l-0',
     'symbol': 'ETH-29SEP23-1800-C',
     'timestamp': 1695974400000,
     'datetime': datetime.datetime(2023, 9, 29, 9, 0),
     'initialMarginPercentage': None,
     'realizedPnl': -0.9503399999999971,
     'unrealizedPnl': 0.0,
     'contractSize': 0.0,
     'side': 'long',
     'size': 0.0,
     'info': {'id': '0x9b8a204636a7aa9c33053d9c3a828720d32212e8-0x5c82b8d5a5306c48e9ac5fc07559a6961bd1ad1e-l-0',
      'netAmount': '0',
      'buyAmount': '200000000000000000',
      'sellAmount': '200000000000000000',
      'active': False,
      'realizedPnl': '-1150340',
      'oToken': {'id': '0x5c82b8d5a5306c48e9ac5fc07559a6961bd1ad1e',
       'symbol': 'oWETHUSDC/USDC-29SEP23-1800C',
       'expiryTimestamp': '1695974400',
       'strikePrice': '180000000000',
       'isPut': False,
       'underlyingAsset': {'id': '0x3b3a1de07439eeb04492fa64a889ee25a130cdd3'},
       'createdAt': '1689849479'},
      'redeemActions': [],
      'optionsBoughtTransactions': [{'amount': '100000000000000000',
        'premium': '12841201'},
       {'amount': '100000000000000000', 'premium': '13438848'}],
      'optionsSoldTransactions': [{'amount': '200000000000000000',
        'premium': '25329709'}],
      'expiration_datetime': datetime.datetime(2023, 9, 29, 9, 0),
      'strike': 1.8e+21,
      'isPut': False},
     'entryPrice': 0}



## Dev & Contributing

Dependencies are managed with poetry.

For dev build.

```bash
poetry install 
poetry shell 
```

# Tests


```python
!poetry run pytest tests
```

    [1m============================= test session starts ==============================[0m
    platform linux -- Python 3.10.4, pytest-7.2.1, pluggy-1.2.0
    rootdir: /home/tom/Desktop/Fun/rysk/rysk_explorations, configfile: pytest.ini
    plugins: cov-3.0.0, web3-5.31.0, anyio-3.7.1, pylama-8.4.1, rerunfailures-11.1.2
    collected 78 items                                                             [0m
    
    tests/test_client.py::test_fetch_markets [32mPASSED[0m[32m                          [  1%][0m
    tests/test_client.py::test_fetch_tickers [32mPASSED[0m[32m                          [  2%][0m
    tests/test_client.py::test_fetch_positions [32mPASSED[0m[32m                        [  3%][0m
    tests/test_client.py::test_create_buy_order[ETH-28JUL23-1900-C] [32mPASSED[0m[32m   [  5%][0m
    tests/test_client.py::test_create_buy_order[ETH-28JUL23-1900-P] [32mPASSED[0m[32m   [  6%][0m
    tests/test_client.py::test_create_sell_order [32mPASSED[0m[32m                      [  7%][0m
    tests/test_collateral.py::test_get_collateral[usdc] [32mPASSED[0m[32m               [  8%][0m
    tests/test_collateral.py::test_get_collateral[weth] [32mPASSED[0m[32m               [ 10%][0m
    tests/test_collateral.py::test_supported_collateral[usdc] [32mPASSED[0m[32m         [ 11%][0m
    tests/test_collateral.py::test_supported_collateral[weth] [32mPASSED[0m[32m         [ 12%][0m
    tests/test_collateral.py::test_unsupported_collateral[btc] [32mPASSED[0m[32m        [ 14%][0m
    tests/test_collateral.py::test_unsupported_collateral[doge] [32mPASSED[0m[32m       [ 15%][0m
    tests/test_contract_calls.py::test_local_fork [32mPASSED[0m[32m                     [ 16%][0m
    tests/test_contract_calls.py::test_get_block_number [32mPASSED[0m[32m               [ 17%][0m
    tests/test_contract_calls.py::test_settle_vault[6] [33mSKIPPED[0m (Pending ...)[32m [ 19%][0m
    tests/test_contract_calls.py::test_settle_vault[9] [33mSKIPPED[0m (Pending ...)[32m [ 20%][0m
    tests/test_contract_calls.py::test_settle_vault[15] [33mSKIPPED[0m (Pending...)[32m [ 21%][0m
    tests/test_contract_calls.py::test_fails_to_settle_vault [32mPASSED[0m[32m          [ 23%][0m
    tests/test_contract_calls.py::test_redeems_o_token [33mSKIPPED[0m (Pending ...)[32m [ 24%][0m
    tests/test_contract_calls.py::test_retieve_and_redeem[ETH-02JUN23-1900-P-30] [33mSKIPPED[0m[32m [ 25%][0m
    tests/test_contract_calls.py::test_retieve_and_redeem[ETH-09JUN23-1900-P-360] [33mSKIPPED[0m[32m [ 26%][0m
    tests/test_contract_calls.py::test_redeem_market_from_str[ETH-02JUN23-1900-P] [33mSKIPPED[0m[32m [ 28%][0m
    tests/test_contract_calls.py::test_client_can_buy[ETH-28JUL23-1900-C-5] [32mPASSED[0m[32m [ 29%][0m
    tests/test_contract_calls.py::test_client_can_buy[ETH-28JUL23-2000-C-5] [32mPASSED[0m[32m [ 30%][0m
    tests/test_contract_calls.py::test_client_can_buy[ETH-28JUL23-1800-P-5] [32mPASSED[0m[32m [ 32%][0m
    tests/test_contract_calls.py::test_client_can_buy[ETH-28JUL23-1900-P-5] [32mPASSED[0m[32m [ 33%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-2000-C-1] [32mPASSED[0m[32m [ 34%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-1900-C-2] [32mPASSED[0m[32m [ 35%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-1800-P-3] [32mPASSED[0m[32m [ 37%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-2000-C-4] [32mPASSED[0m[32m [ 38%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-1900-C-5] [32mPASSED[0m[32m [ 39%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-1800-P-6] [32mPASSED[0m[32m [ 41%][0m
    tests/test_contract_calls.py::test_client_can_buy_differing_amounts[ETH-28JUL23-2000-C-7] [32mPASSED[0m[32m [ 42%][0m

## Formating and linting


```python
!make fmt lint
```

    poetry run black tests rysk_client && poetry run isort tests rysk_client 
    [1mreformatted tests/conftest.py[0m
    [1mreformatted tests/test_rysk_option_market.py[0m
    [1mreformatted rysk_client/packages/eightballer/contracts/user_position_lens/contract.py[0m
    [1mreformatted rysk_client/src/utils.py[0m
    [1mreformatted rysk_client/src/operation_factory.py[0m
    [1mreformatted rysk_client/packages/eightballer/contracts/option_exchange/contract.py[0m
    [1mreformatted rysk_client/packages/eightballer/contracts/opyn_controller/contract.py[0m
    [1mreformatted rysk_client/packages/eightballer/contracts/opyn_option_registry/contract.py[0m
    [1mreformatted rysk_client/web3_client.py[0m
    [1mreformatted rysk_client/client.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m10 files [0m[1mreformatted[0m, [34m39 files [0mleft unchanged.
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/tests/test_rysk_option_market.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/tests/conftest.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/client.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/web3_client.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/packages/eightballer/contracts/user_position_lens/contract.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/packages/eightballer/contracts/opyn_option_registry/contract.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/packages/eightballer/contracts/option_exchange/contract.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/packages/eightballer/contracts/opyn_controller/contract.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/src/operation_factory.py
    Fixing /home/tom/Desktop/Fun/rysk/rysk_explorations/rysk_client/src/utils.py
    Skipped 9 files
    poetry run adev -v -n 0 lint -p tests
    [2;36m[19:16:04][0m[2;36m [0m[32mDEBUG   [0m Consider installing rusty-rlp to improve pyrlp   ]8;id=871982;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/rlp/codec.py\[2mcodec.py[0m]8;;\[2m:[0m]8;id=423867;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/rlp/codec.py#26\[2m26[0m]8;;\
    [2;36m           [0m         performance with a rust based backend            [2m           [0m
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Starting Auto Dev v0.[1;36m2.6[0m [33m...[0m                      ]8;id=777441;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=390191;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#72\[2m72[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Verbose mode enabled                              ]8;id=656669;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=690015;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#75\[2m75[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Using [1;36m32[0m processes for processing                 ]8;id=300635;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=723439;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#77\[2m77[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Setting log level to INFO                         ]8;id=59445;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=408112;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#79\[2m79[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Linting Open Autonomy Packages                    ]8;id=656444;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=861569;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#37\[2m37[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Linting [1;36m12[0m files[33m...[0m                               ]8;id=422140;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=648455;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#39\[2m39[0m]8;;\
    [2;36m[19:16:09][0m[2;36m [0m[34mINFO    [0m Linting completed with [1;36m12[0m passed and [1;36m0[0m failed     ]8;id=16054;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=321483;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#46\[2m46[0m]8;;\
    poetry run adev -v -n 0 lint -p rysk_client
    [2;36m[19:16:10][0m[2;36m [0m[32mDEBUG   [0m Consider installing rusty-rlp to improve pyrlp   ]8;id=924141;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/rlp/codec.py\[2mcodec.py[0m]8;;\[2m:[0m]8;id=620693;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/rlp/codec.py#26\[2m26[0m]8;;\
    [2;36m           [0m         performance with a rust based backend            [2m           [0m
    [2;36m[19:16:11][0m[2;36m [0m[34mINFO    [0m Starting Auto Dev v0.[1;36m2.6[0m [33m...[0m                      ]8;id=109749;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=900199;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#72\[2m72[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Verbose mode enabled                              ]8;id=607608;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=519072;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#75\[2m75[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Using [1;36m32[0m processes for processing                 ]8;id=302243;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=356880;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#77\[2m77[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Setting log level to INFO                         ]8;id=822518;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py\[2mbase.py[0m]8;;\[2m:[0m]8;id=634619;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/base.py#79\[2m79[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Linting Open Autonomy Packages                    ]8;id=550306;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=189039;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#37\[2m37[0m]8;;\
    [2;36m          [0m[2;36m [0m[34mINFO    [0m Linting [1;36m37[0m files[33m...[0m                               ]8;id=733237;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=406955;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#39\[2m39[0m]8;;\
    [2;36m[19:16:19][0m[2;36m [0m[34mINFO    [0m Linting completed with [1;36m37[0m passed and [1;36m0[0m failed     ]8;id=571940;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py\[2mlint.py[0m]8;;\[2m:[0m]8;id=671018;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-Q6-gVAE8-py3.10/lib/python3.10/site-packages/auto_dev/commands/lint.py#46\[2m46[0m]8;;\


# Releasing
Git ops is used to enable automated releases via pypi.

```bash
export NEW_VERSION=0.2.11
git checkout -b v$NEW_VERSION &&
    bumpversion  rysk_client/ --new-version $NEW_VERSION && 
git push --set-upstream origin (git rev-parse --abbrev-ref HEAD) && git push --tag

```
