# Rysk Client

## Installation

The application is availale on pypi and can be installed as so;

    ```bash
    pip install rysk-client
    ```

### Dev & Contributing

Dependencies are managed with poetry.

For dev build.


```python
!pip install -U .
```

    Processing /home/tom/Desktop/Fun/rysk_examples
    [33m  DEPRECATION: A future pip version will change local packages to be built in-place without first copying to a temporary directory. We recommend you use --use-feature=in-tree-build to test your packages with this new behavior before it becomes the default.
       pip 21.3 will remove support for this functionality. You can find discussion regarding this at https://github.com/pypa/pip/issues/7555.[0m
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h    Preparing wheel metadata ... [?25ldone
    [?25hCollecting ccxt<4.0.0,>=3.1.15
      Downloading ccxt-3.1.31-py2.py3-none-any.whl (3.9 MB)
    [K     |████████████████████████████████| 3.9 MB 3.8 MB/s eta 0:00:01
    [?25hCollecting web3==6.4.0
      Downloading web3-6.4.0-py3-none-any.whl (574 kB)
    [K     |████████████████████████████████| 574 kB 8.9 MB/s eta 0:00:01
    [?25hRequirement already satisfied: rich-click<2.0.0,>=1.6.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from rysk-client==0.1.9) (1.6.1)
    Collecting eth-abi>=4.0.0
      Downloading eth_abi-4.1.0-py3-none-any.whl (27 kB)
    Requirement already satisfied: hexbytes>=0.1.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.9) (0.3.0)
    Collecting protobuf>=4.21.6
      Downloading protobuf-4.23.2-cp37-abi3-manylinux2014_x86_64.whl (304 kB)
    [K     |████████████████████████████████| 304 kB 8.2 MB/s eta 0:00:01
    [?25hRequirement already satisfied: lru-dict>=1.1.6 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.9) (1.1.8)
    Collecting eth-typing>=3.0.0
      Downloading eth_typing-3.4.0-py3-none-any.whl (6.0 kB)
    Collecting eth-account>=0.8.0
      Downloading eth_account-0.9.0-py3-none-any.whl (101 kB)
    [K     |█████████████████████████████   | 92 kB 8.2 MB/s eta 0:00:01     |████████████████████████████████| 101 kB 4.6 MB/s 
    [?25hCollecting jsonschema>=4.0.0
      Using cached jsonschema-4.17.3-py3-none-any.whl (90 kB)
    Collecting websockets>=10.0.0
      Downloading websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)
    [K     |████████████████████████████████| 129 kB 6.8 MB/s eta 0:00:01
    [?25hCollecting eth-utils>=2.1.0
      Downloading eth_utils-2.1.1-py3-none-any.whl (23 kB)
    Collecting eth-hash[pycryptodome]>=0.5.1
      Downloading eth_hash-0.5.2-py3-none-any.whl (8.6 kB)
    Requirement already satisfied: aiohttp>=3.7.4.post0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.9) (3.8.4)
    Requirement already satisfied: requests>=2.16.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.9) (2.30.0)
    Requirement already satisfied: yarl<2.0,>=1.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (1.9.2)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (1.3.1)
    Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (3.1.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (6.0.4)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (1.3.3)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (4.0.2)
    Requirement already satisfied: attrs>=17.3.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.9) (23.1.0)
    Requirement already satisfied: certifi>=2018.1.18 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (2022.12.7)
    Requirement already satisfied: cryptography>=2.6.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (40.0.2)
    Requirement already satisfied: setuptools>=60.9.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (67.7.2)
    Requirement already satisfied: aiodns>=1.1.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (3.0.0)
    Requirement already satisfied: pycares>=4.0.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from aiodns>=1.1.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (4.3.0)
    Requirement already satisfied: cffi>=1.12 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (1.15.1)
    Requirement already satisfied: pycparser in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.9) (2.21)
    Collecting parsimonious<0.10.0,>=0.9.0
      Using cached parsimonious-0.9.0.tar.gz (48 kB)
    Collecting eth-keyfile>=0.6.0
      Downloading eth_keyfile-0.6.1-py3-none-any.whl (6.5 kB)
    Requirement already satisfied: rlp>=1.0.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.9) (1.2.0)
    Collecting eth-rlp>=0.3.0
      Using cached eth_rlp-0.3.0-py3-none-any.whl (5.0 kB)
    Requirement already satisfied: bitarray>=2.4.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.9) (2.7.3)
    Collecting eth-keys>=0.4.0
      Downloading eth_keys-0.4.0-py3-none-any.whl (21 kB)
    Requirement already satisfied: pycryptodome<4,>=3.6.6 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from eth-hash[pycryptodome]>=0.5.1->web3==6.4.0->rysk-client==0.1.9) (3.17)
    Requirement already satisfied: cytoolz>=0.10.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from eth-utils>=2.1.0->web3==6.4.0->rysk-client==0.1.9) (0.12.1)
    Requirement already satisfied: toolz>=0.8.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from cytoolz>=0.10.1->eth-utils>=2.1.0->web3==6.4.0->rysk-client==0.1.9) (0.12.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from jsonschema>=4.0.0->web3==6.4.0->rysk-client==0.1.9) (0.19.3)
    Requirement already satisfied: regex>=2022.3.15 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from parsimonious<0.10.0,>=0.9.0->eth-abi>=4.0.0->web3==6.4.0->rysk-client==0.1.9) (2023.5.5)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from requests>=2.16.0->web3==6.4.0->rysk-client==0.1.9) (1.26.15)
    Requirement already satisfied: idna<4,>=2.5 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from requests>=2.16.0->web3==6.4.0->rysk-client==0.1.9) (3.4)
    Requirement already satisfied: rich>=10.7.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from rich-click<2.0.0,>=1.6.1->rysk-client==0.1.9) (13.3.5)
    Requirement already satisfied: click>=7 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from rich-click<2.0.0,>=1.6.1->rysk-client==0.1.9) (8.0.2)
    Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.9) (2.15.1)
    Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.9) (2.2.0)
    Requirement already satisfied: mdurl~=0.1 in /home/tom/.pyenv/versions/3.10.0/lib/python3.10/site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.9) (0.1.2)
    Collecting rlp>=1.0.0
      Downloading rlp-3.0.0-py2.py3-none-any.whl (20 kB)
    Using legacy 'setup.py install' for parsimonious, since package 'wheel' is not installed.
    Building wheels for collected packages: rysk-client
      Building wheel for rysk-client (PEP 517) ... [?25ldone
    [?25h  Created wheel for rysk-client: filename=rysk_client-0.1.9-py3-none-any.whl size=502646 sha256=621ed06d3ca35b970ee5caa17eb02563c0fa04441893b495f3591a1e2324a484
      Stored in directory: /tmp/pip-ephem-wheel-cache-1mjy9fwl/wheels/d0/5d/c5/06071ec2d9be7dfabf83e13d497e7bd4b06d0041d896c67705
    Successfully built rysk-client
    Installing collected packages: eth-typing, eth-hash, eth-utils, rlp, parsimonious, eth-keys, eth-rlp, eth-keyfile, eth-abi, websockets, protobuf, jsonschema, eth-account, web3, ccxt, rysk-client
      Attempting uninstall: eth-typing
        Found existing installation: eth-typing 2.3.0
        Uninstalling eth-typing-2.3.0:
          Successfully uninstalled eth-typing-2.3.0
      Attempting uninstall: eth-hash
        Found existing installation: eth-hash 0.3.3
        Uninstalling eth-hash-0.3.3:
          Successfully uninstalled eth-hash-0.3.3
      Attempting uninstall: eth-utils
        Found existing installation: eth-utils 1.10.0
        Uninstalling eth-utils-1.10.0:
          Successfully uninstalled eth-utils-1.10.0
      Attempting uninstall: rlp
        Found existing installation: rlp 1.2.0
        Uninstalling rlp-1.2.0:
          Successfully uninstalled rlp-1.2.0
      Attempting uninstall: parsimonious
        Found existing installation: parsimonious 0.8.1
        Uninstalling parsimonious-0.8.1:
          Successfully uninstalled parsimonious-0.8.1
        Running setup.py install for parsimonious ... [?25ldone
    [?25h  Attempting uninstall: eth-keys
        Found existing installation: eth-keys 0.3.4
        Uninstalling eth-keys-0.3.4:
          Successfully uninstalled eth-keys-0.3.4
      Attempting uninstall: eth-rlp
        Found existing installation: eth-rlp 0.2.1
        Uninstalling eth-rlp-0.2.1:
          Successfully uninstalled eth-rlp-0.2.1
      Attempting uninstall: eth-keyfile
        Found existing installation: eth-keyfile 0.5.1
        Uninstalling eth-keyfile-0.5.1:
          Successfully uninstalled eth-keyfile-0.5.1
      Attempting uninstall: eth-abi
        Found existing installation: eth-abi 2.2.0
        Uninstalling eth-abi-2.2.0:
          Successfully uninstalled eth-abi-2.2.0
      Attempting uninstall: websockets
        Found existing installation: websockets 9.1
        Uninstalling websockets-9.1:
          Successfully uninstalled websockets-9.1
      Attempting uninstall: protobuf
        Found existing installation: protobuf 3.20.3
        Uninstalling protobuf-3.20.3:
          Successfully uninstalled protobuf-3.20.3
      Attempting uninstall: jsonschema
        Found existing installation: jsonschema 3.2.0
        Uninstalling jsonschema-3.2.0:
          Successfully uninstalled jsonschema-3.2.0
      Attempting uninstall: eth-account
        Found existing installation: eth-account 0.5.9
        Uninstalling eth-account-0.5.9:
          Successfully uninstalled eth-account-0.5.9
      Attempting uninstall: web3
        Found existing installation: web3 5.25.0
        Uninstalling web3-5.25.0:
          Successfully uninstalled web3-5.25.0
      Attempting uninstall: ccxt
        Found existing installation: ccxt 3.0.104
        Uninstalling ccxt-3.0.104:
          Successfully uninstalled ccxt-3.0.104
      Attempting uninstall: rysk-client
        Found existing installation: rysk-client 0.1.0
        Uninstalling rysk-client-0.1.0:
          Successfully uninstalled rysk-client-0.1.0
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    py-ecc 5.2.0 requires eth-typing<3.0.0,>=2.1.0, but you have eth-typing 3.4.0 which is incompatible.
    py-ecc 5.2.0 requires eth-utils<2,>=1.3.0, but you have eth-utils 2.1.1 which is incompatible.
    ethereum 2.3.2 requires rlp<2.0.0,>=1.0.1, but you have rlp 3.0.0 which is incompatible.[0m
    Successfully installed ccxt-3.1.31 eth-abi-4.1.0 eth-account-0.9.0 eth-hash-0.5.2 eth-keyfile-0.6.1 eth-keys-0.4.0 eth-rlp-0.3.0 eth-typing-3.4.0 eth-utils-2.1.1 jsonschema-4.17.3 parsimonious-0.9.0 protobuf-4.23.2 rlp-3.0.0 rysk-client-0.1.9 web3-6.4.0 websockets-11.0.3
    [33mWARNING: You are using pip version 21.2.3; however, version 23.1.2 is available.
    You should consider upgrading via the '/home/tom/.pyenv/versions/3.10.0/bin/python3.10 -m pip install --upgrade pip' command.[0m



```python

```


```python

```

## Cli Tool

The application is also bundled as cli tool to allow users to interact with the protocol from the cli.



```python
! rysk
```

    [1m                                                                                [0m
    [1m [0m[1;33mUsage: [0m[1mrysk [[0m[1;36mOPTIONS[0m[1m] [0m[1;36mCOMMAND[0m[1m [[0m[1;36mARGS[0m[1m]...[0m[1m                                       [0m[1m [0m
    [1m                                                                                [0m
     Rysk client command line interface.                                            
                                                                                    
    [2m╭─[0m[2m Options [0m[2m───────────────────────────────────────────────────────────────────[0m[2m─╮[0m
    [2m│[0m [1;36m-[0m[1;36m-log[0m[1;36m-level[0m  [1;32m-l[0m  [1;2;33m[[0m[1;33mDEBUG[0m[1;2;33m|[0m[1;33mINFO[0m[1;2;33m|[0m[1;33mWARNING[0m[1;2;33m|[0m[1;33mERROR[0m[1;2;33m|[0m[1;33mCR[0m  Logging level.                [2m│[0m
    [2m│[0m                  [1;33mITICAL[0m[1;2;33m][0m[1;33m                     [0m                                [2m│[0m
    [2m│[0m [1;36m-[0m[1;36m-help[0m           [1;33m                            [0m  Show this message and exit.   [2m│[0m
    [2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
    [2m╭─[0m[2m Commands [0m[2m──────────────────────────────────────────────────────────────────[0m[2m─╮[0m
    [2m│[0m [1;36mbalances             [0m[1;36m [0m Interact with balances.                               [2m│[0m
    [2m│[0m [1;36mmarkets              [0m[1;36m [0m Interact with markets.                                [2m│[0m
    [2m│[0m [1;36mpositions            [0m[1;36m [0m Interact with positions.                              [2m│[0m
    [2m│[0m [1;36mtickers              [0m[1;36m [0m Interact with tickers.                                [2m│[0m
    [2m│[0m [1;36mtrades               [0m[1;36m [0m Interact with trades.                                 [2m│[0m
    [2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
    


### Markets
We can fetch data about the markets as so;


```python
! rysk markets fetch
```

    [3m                              Markets                               [0m
    ┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃[1m [0m[1mid                [0m[1m [0m┃[1m [0m[1mexpiration[0m[1m [0m┃[1m [0m[1mstrike[0m[1m [0m┃[1m [0m[1mbid      [0m[1m [0m┃[1m [0m[1mask      [0m[1m [0m┃
    ┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━┩
    │ ETH-16JUN23-1950-C │ 1686902400 │ 1950.0 │ 11.360294 │ 11.771131 │
    │ ETH-16JUN23-1900-C │ 1686902400 │ 1900.0 │ 36.081166 │ 36.704213 │
    │ ETH-16JUN23-1850-C │ 1686902400 │ 1850.0 │ 42.817191 │ 43.6451   │
    │ ETH-16JUN23-1800-C │ 1686902400 │ 1800.0 │ 68.25092  │ 69.147332 │
    │ ETH-16JUN23-1900-P │ 1686902400 │ 1900.0 │           │           │
    │ ETH-16JUN23-1850-P │ 1686902400 │ 1850.0 │ 59.724482 │ 60.813081 │
    │ ETH-16JUN23-1800-P │ 1686902400 │ 1800.0 │ 13.625934 │ 14.111028 │
    │ ETH-16JUN23-1750-P │ 1686902400 │ 1750.0 │ 17.433291 │ 17.957708 │
    │ ETH-30JUN23-1800-C │ 1688112000 │ 1800.0 │           │           │
    │ ETH-30JUN23-1900-C │ 1688112000 │ 1900.0 │ 81.221422 │ 83.880381 │
    │ ETH-30JUN23-2000-C │ 1688112000 │ 2000.0 │ 36.841275 │ 38.798264 │
    │ ETH-30JUN23-2100-C │ 1688112000 │ 2100.0 │ 44.43844  │ 46.112509 │
    │ ETH-30JUN23-1700-P │ 1688112000 │ 1700.0 │ 39.223424 │ 41.326081 │
    │ ETH-30JUN23-1800-P │ 1688112000 │ 1800.0 │ 60.720471 │ 63.676246 │
    │ ETH-30JUN23-1900-P │ 1688112000 │ 1900.0 │ 88.051645 │ 90.799835 │
    │ ETH-30JUN23-1600-P │ 1688112000 │ 1600.0 │ 33.600252 │ 35.223619 │
    └────────────────────┴────────────┴────────┴───────────┴───────────┘


# Usage



```python
from rysk_client.src.utils import get_web3

web3 = get_web3()
web3.is_connected()
```




    True



## Creating a Client 

Clients can be created from the rysk client module.


```python
from rysk_client.client import RyskClient
from tests.conftest import DEFAULT_ADDRESS

auth = {
    "address": DEFAULT_ADDRESS,
}

print(auth)

client = RyskClient(**auth)
client

```




    RyskClient(_markets=[], _tickers=[], _otokens={})



## Fetching Markets

The client can fetch markets as so;



```python
markets = client.fetch_markets()
markets[0]
```




    {'base': 'ETH',
     'baseId': 'ETH',
     'contract': True,
     'contractSize': 1.0,
     'spot': False,
     'swap': False,
     'future': False,
     'type': 'option',
     'linear': False,
     'inverse': True,
     'active': True,
     'id': 'ETH-30JUN23-1700-P',
     'strike': 1700.0,
     'optionType': 'put',
     'expiry': 1688112000000,
     'expiryDatetime': '2023-06-30T09:00:00.000000Z',
     'info': {'id': '0x01f460be7389b109cc3599941166ea851d0b7c787badf04b1f276d3ce9269a34',
      'expiration': '1688112000',
      'netDHVExposure': '-60750000000000000000',
      'strike': '1700000000000000000000',
      'isPut': True,
      'isBuyable': True,
      'isSellable': True,
      'expiration_datetime': datetime.datetime(2023, 6, 30, 9, 0)},
     'symbol': 'ETH-30JUN23-1700-P',
     'maker': 0.0003,
     'taker': 0.0003}



## Fetching Tickers

Tickers can be fetched from the client as so;


```python
tickers = client.fetch_tickers()
tickers[0]
```




    {'ask': 27.510602,
     'bid': 24.958423,
     'info': {'base': 'ETH',
      'baseId': 'ETH',
      'contract': True,
      'contractSize': 1.0,
      'spot': False,
      'swap': False,
      'future': False,
      'type': 'option',
      'linear': False,
      'inverse': True,
      'active': True,
      'id': 'ETH-30JUN23-1700-P',
      'strike': 1700.0,
      'optionType': 'put',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T09:00:00.000000Z',
      'info': {'id': '0x01f460be7389b109cc3599941166ea851d0b7c787badf04b1f276d3ce9269a34',
       'expiration': '1688112000',
       'netDHVExposure': '-60750000000000000000',
       'strike': '1700000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 9, 0)},
      'symbol': 'ETH-30JUN23-1700-P',
      'maker': 0.0003,
      'taker': 0.0003}}



## Fetching Positions
Positions are fetched from the client such that a user can retrieve their positions.

Positions are indicated by a vault id.

The vaultid iterates when a new position is created. 

Vaultid can be retrieved from;






```python
positions = client.fetch_positions()
positions[0]
```




    {'id': '0x9b8a204636a7aa9c33053d9c3a828720d32212e8-0x1c8b898ada9e994d67d86b1a1a15f5cdbaf6da08-l-0',
     'symbol': 'ETH-09JUN23-1900-P',
     'timestamp': 1686297600000,
     'datetime': datetime.datetime(2023, 6, 9, 9, 0),
     'initialMarginPercentage': None,
     'realizedPnl': -4.4852716768,
     'contractSize': '360000000000000000000',
     'side': 'long',
     'info': {'id': '0x9b8a204636a7aa9c33053d9c3a828720d32212e8-0x1c8b898ada9e994d67d86b1a1a15f5cdbaf6da08-l-0',
      'netAmount': '360000000000000000000',
      'buyAmount': '360000000000000000000',
      'sellAmount': '0',
      'active': True,
      'realizedPnl': '-44852716768',
      'oToken': {'id': '0x1c8b898ada9e994d67d86b1a1a15f5cdbaf6da08',
       'symbol': '',
       'expiryTimestamp': '1686297600',
       'strikePrice': '190000000000',
       'isPut': True,
       'underlyingAsset': {'id': '0x3b3a1de07439eeb04492fa64a889ee25a130cdd3'},
       'createdAt': '1685191086'},
      'redeemActions': [],
      'optionsBoughtTransactions': [{'amount': '1000000000000000000',
        'premium': '85411979'},
       {'amount': '2000000000000000000', 'premium': '148982158'},
       {'amount': '5000000000000000000', 'premium': '568595995'},
       {'amount': '2000000000000000000', 'premium': '147232776'},
       {'amount': '1000000000000000000', 'premium': '80345856'},
       {'amount': '5000000000000000000', 'premium': '754623020'},
       {'amount': '5000000000000000000', 'premium': '577098533'},
       {'amount': '5000000000000000000', 'premium': '456388925'},
       {'amount': '5000000000000000000', 'premium': '795314771'},
       {'amount': '5000000000000000000', 'premium': '812900950'},
       {'amount': '1000000000000000000', 'premium': '75740402'},
       {'amount': '5000000000000000000', 'premium': '789065184'},
       {'amount': '1000000000000000000', 'premium': '81192329'},
       {'amount': '5000000000000000000', 'premium': '498482650'},
       {'amount': '5000000000000000000', 'premium': '680790621'},
       {'amount': '5000000000000000000', 'premium': '527928890'},
       {'amount': '5000000000000000000', 'premium': '449675922'},
       {'amount': '5000000000000000000', 'premium': '521162730'},
       {'amount': '1000000000000000000', 'premium': '85918506'},
       {'amount': '1000000000000000000', 'premium': '86428248'},
       {'amount': '5000000000000000000', 'premium': '491147819'},
       {'amount': '1000000000000000000', 'premium': '85664952'},
       {'amount': '2000000000000000000', 'premium': '149865819'},
       {'amount': '5000000000000000000', 'premium': '631534398'},
       {'amount': '2000000000000000000', 'premium': '144646675'},
       {'amount': '5000000000000000000', 'premium': '732499858'},
       {'amount': '5000000000000000000', 'premium': '470114108'},
       {'amount': '5000000000000000000', 'premium': '690987987'},
       {'amount': '1000000000000000000', 'premium': '84286070'},
       {'amount': '5000000000000000000', 'premium': '876032718'},
       {'amount': '5000000000000000000', 'premium': '551961448'},
       {'amount': '5000000000000000000', 'premium': '771994153'},
       {'amount': '1000000000000000000', 'premium': '84535732'},
       {'amount': '1000000000000000000', 'premium': '84279477'},
       {'amount': '1000000000000000000', 'premium': '82253448'},
       {'amount': '2000000000000000000', 'premium': '146365342'},
       {'amount': '5000000000000000000', 'premium': '543830397'},
       {'amount': '1000000000000000000', 'premium': '80583215'},
       {'amount': '4000000000000000000', 'premium': '305184177'},
       {'amount': '5000000000000000000', 'premium': '640987152'},
       {'amount': '2000000000000000000', 'premium': '145503388'},
       {'amount': '5000000000000000000', 'premium': '443062676'},
       {'amount': '5000000000000000000', 'premium': '622220354'},
       {'amount': '5000000000000000000', 'premium': '741154995'},
       {'amount': '5000000000000000000', 'premium': '840881177'},
       {'amount': '1000000000000000000', 'premium': '82552807'},
       {'amount': '5000000000000000000', 'premium': '535822355'},
       {'amount': '5000000000000000000', 'premium': '604018230'},
       {'amount': '5000000000000000000', 'premium': '765931819'},
       {'amount': '1000000000000000000', 'premium': '80108544'},
       {'amount': '5000000000000000000', 'premium': '831627246'},
       {'amount': '5000000000000000000', 'premium': '749361360'},
       {'amount': '5000000000000000000', 'premium': '777415411'},
       {'amount': '1000000000000000000', 'premium': '84037211'},
       {'amount': '5000000000000000000', 'premium': '701339627'},
       {'amount': '1000000000000000000', 'premium': '83288180'},
       {'amount': '5000000000000000000', 'premium': '513492797'},
       {'amount': '5000000000000000000', 'premium': '670742921'},
       {'amount': '1000000000000000000', 'premium': '80952540'},
       {'amount': '5000000000000000000', 'premium': '585733695'},
       {'amount': '1000000000000000000', 'premium': '82010604'},
       {'amount': '5000000000000000000', 'premium': '863083930'},
       {'amount': '5000000000000000000', 'premium': '613043431'},
       {'amount': '5000000000000000000', 'premium': '800892781'},
       {'amount': '4000000000000000000', 'premium': '315514106'},
       {'amount': '2000000000000000000', 'premium': '150754579'},
       {'amount': '1000000000000000000', 'premium': '80713635'},
       {'amount': '5000000000000000000', 'premium': '660851337'},
       {'amount': '5000000000000000000', 'premium': '483918272'},
       {'amount': '4000000000000000000', 'premium': '311802564'},
       {'amount': '4000000000000000000', 'premium': '308813822'},
       {'amount': '5000000000000000000', 'premium': '436553406'},
       {'amount': '1000000000000000000', 'premium': '83782490'},
       {'amount': '5000000000000000000', 'premium': '807240638'},
       {'amount': '5000000000000000000', 'premium': '594497886'},
       {'amount': '1000000000000000000', 'premium': '81768992'},
       {'amount': '1000000000000000000', 'premium': '84030699'},
       {'amount': '5000000000000000000', 'premium': '825093045'},
       {'amount': '5000000000000000000', 'premium': '837468476'},
       {'amount': '5000000000000000000', 'premium': '853495586'},
       {'amount': '5000000000000000000', 'premium': '651099941'},
       {'amount': '1000000000000000000', 'premium': '83042247'},
       {'amount': '5000000000000000000', 'premium': '889176821'},
       {'amount': '1000000000000000000', 'premium': '83534965'},
       {'amount': '5000000000000000000', 'premium': '722507695'},
       {'amount': '5000000000000000000', 'premium': '711843975'},
       {'amount': '5000000000000000000', 'premium': '560217431'},
       {'amount': '5000000000000000000', 'premium': '760595165'},
       {'amount': '5000000000000000000', 'premium': '819344684'},
       {'amount': '1000000000000000000', 'premium': '82796990'},
       {'amount': '1000000000000000000', 'premium': '85159819'},
       {'amount': '5000000000000000000', 'premium': '463202872'},
       {'amount': '1000000000000000000', 'premium': '80821894'},
       {'amount': '5000000000000000000', 'premium': '476798780'},
       {'amount': '2000000000000000000', 'premium': '148104491'},
       {'amount': '5000000000000000000', 'premium': '743479150'},
       {'amount': '5000000000000000000', 'premium': '783569359'},
       {'amount': '5000000000000000000', 'premium': '848702420'},
       {'amount': '1000000000000000000', 'premium': '86173174'},
       {'amount': '5000000000000000000', 'premium': '505931893'}],
      'optionsSoldTransactions': [],
      'expiration_datetime': datetime.datetime(2023, 6, 9, 9, 0),
      'strike': 1.9e+21,
      'isPut': True},
     'contracts': None,
     'marginRatio': None,
     'liquidationPrice': None,
     'lastPrice': None,
     'collateral': None,
     'marginMode': None,
     'initialMargin': None,
     'maintenanceMargin': None,
     'maintenanceMarginPercentage': None,
     'entryPrice': None,
     'notional': None,
     'leverage': None,
     'percentage': None}



# Tests


```python
!make test
```

    poetry run adev test -v -p tests
    Testing Open Autonomy Packages
    [2K[2;36m[14:13:41][0m[2;36m [0m[34mINFO    [0m [1m[[0m[33m1m[0m============================= test     ]8;id=536186;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py\[2mcli_executor.py[0m]8;;\[2m:[0m]8;id=447753;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py#36\[2m36[0m]8;;\
    [2;36m           [0m         session starts                            [2m                  [0m
    [2;36m           [0m         ==============================[1m[[0m0m         [2m                  [0m
    [2;36m           [0m         platform linux -- Python [1;36m3.10[0m.[1;36m4[0m,          [2m                  [0m
    [2;36m           [0m         pytest-[1;36m7.3[0m.[1;36m1[0m, pluggy-[1;36m1.0[0m.[1;36m0[0m                [2m                  [0m
    [2;36m           [0m         rootdir:                                  [2m                  [0m
    [2;36m           [0m         [35m/home/tom/Desktop/Fun/[0m[95mrysk_explorations[0m   [2m                  [0m
    [2;36m           [0m         configfile: pytest.ini                    [2m                  [0m
    [2;36m           [0m         plugins: cov-[1;36m3.0[0m.[1;36m0[0m, pylama-[1;36m8.4[0m.[1;36m1[0m,         [2m                  [0m
    [2;36m           [0m         web3-[1;36m5.31[0m.[1;36m4[0m, anyio-[1;36m3.7[0m.[1;36m0[0m                  [2m                  [0m
    [2;36m           [0m         collected [1;36m23[0m items                        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         tests/test_client.py                      [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m33ms[1m[[0m0m[1m[[0m32m              [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m13[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_collateral.py                  [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m                      [2m                  [0m
    [2;36m           [0m                        [1m[[0m [1;36m39[0m%[1m][0m[1m[[0m0m                  [2m                  [0m
    [2;36m           [0m         tests/test_rysk_option_market.py          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m                      [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m47[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_rysk_options_market_manager.py [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m                      [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m56[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_subgraph.py [1m[[0m32m.[1m[[0m0m[1m[[0m32m       [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m60[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_utils.py                       [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m  [2m                  [0m
    [2;36m           [0m         [1m[[0m32m                                      [2m                  [0m
    [2;36m           [0m         [1m[[0m[1;36m100[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [1m[[0m[33m32m[0m======================== [1m[[0m32m[1m[[0m1m22    [2m                  [0m
    [2;36m           [0m         passed[1m[[0m0m, [1m[[0m33m1 skipped[1m[[0m0m[1m[[0m32m in        [2m                  [0m
    [2;36m           [0m         [1;36m25.[0m17s[1m[[0m0m[1m[[0m32m ========================[1m[[0m0m [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2KTesting... [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [35m100%[0m [33m0:00:26[0m
    [?25hTesting completed successfully!



```python
!make fmt lint
```

    poetry run isort tests rysk_client && poetry run black tests rysk_client
    [1mAll done! ✨ 🍰 ✨[0m
    [34m19 files [0mleft unchanged.
    poetry run adev lint -v -p tests
    [2;36m[14:13:44][0m[2;36m [0m[34mINFO    [0m Linting Open Autonomy Packages                     ]8;id=281004;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli.py\[2mcli.py[0m]8;;\[2m:[0m]8;id=265993;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli.py#47\[2m47[0m]8;;\
    [2KLinting... [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [35m100%[0m [33m0:00:03[0m
    [?25h[2;36m[14:13:48][0m[2;36m [0m[34mINFO    [0m Linting completed successfully!                    ]8;id=864081;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli.py\[2mcli.py[0m]8;;\[2m:[0m]8;id=992553;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli.py#66\[2m66[0m]8;;\

