# Rysk Client

## Installation

### Dev

dependencies are managed with poetry. 

For dev build.


```python
!poetry install && poetry run pip install -e .
```

    [34mInstalling dependencies from lock file[39m
    
    No dependencies to install or update
    
    [39;1mInstalling[39;22m the current project: [36mrysk_client[39m ([39;1m0.1.0[39;22m)[1G[2K[39;1mInstalling[39;22m the current project: [36mrysk_client[39m ([32m0.1.0[39m)
    Obtaining file:///home/tom/Desktop/Fun/rysk_examples
      Installing build dependencies ... [?25ldone
    [?25h  Checking if build backend supports build_editable ... [?25ldone
    [?25h  Getting requirements to build editable ... [?25ldone
    [?25h  Preparing editable metadata (pyproject.toml) ... [?25ldone
    [?25hRequirement already satisfied: web3<6.0.0,>=5.4.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from rysk-client==0.1.0) (5.31.4)
    Requirement already satisfied: ccxt<4.0.0,>=3.1.15 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from rysk-client==0.1.0) (3.1.15)
    Requirement already satisfied: certifi>=2018.1.18 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (2023.5.7)
    Requirement already satisfied: aiohttp>=3.8 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (3.8.4)
    Requirement already satisfied: yarl>=1.7.2 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (1.9.2)
    Requirement already satisfied: aiodns>=1.1.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (3.0.0)
    Requirement already satisfied: requests>=2.18.4 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (2.31.0)
    Requirement already satisfied: cryptography>=2.6.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (40.0.2)
    Requirement already satisfied: setuptools>=60.9.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (67.8.0)
    Requirement already satisfied: lru-dict<2.0.0,>=1.1.6 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (1.2.0)
    Requirement already satisfied: eth-utils<2.0.0,>=1.9.5 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (1.10.0)
    Requirement already satisfied: jsonschema<5,>=3.2.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (4.17.3)
    Requirement already satisfied: protobuf==3.19.5 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (3.19.5)
    Requirement already satisfied: websockets<10,>=9.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (9.1)
    Requirement already satisfied: ipfshttpclient==0.8.0a2 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.8.0a2)
    Requirement already satisfied: hexbytes<1.0.0,>=0.1.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.3.0)
    Requirement already satisfied: eth-typing<3.0.0,>=2.0.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (2.3.0)
    Requirement already satisfied: eth-abi<3.0.0,>=2.2.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (2.2.0)
    Requirement already satisfied: eth-hash[pycryptodome]<1.0.0,>=0.2.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.3.3)
    Requirement already satisfied: eth-rlp<0.3 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.2.1)
    Requirement already satisfied: eth-account<0.6.0,>=0.5.9 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.5.9)
    Requirement already satisfied: multiaddr>=0.0.7 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.0.9)
    Requirement already satisfied: pycares>=4.0.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiodns>=1.1.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (4.3.0)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (4.0.2)
    Requirement already satisfied: attrs>=17.3.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (23.1.0)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (1.3.1)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (1.3.3)
    Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (3.1.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (6.0.4)
    Requirement already satisfied: cffi>=1.12 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (1.15.1)
    Requirement already satisfied: parsimonious<0.9.0,>=0.8.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-abi<3.0.0,>=2.2.0->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.8.1)
    Requirement already satisfied: rlp<3,>=1.0.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.9->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (2.0.1)
    Requirement already satisfied: eth-keys<0.4.0,>=0.3.4 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.9->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.3.4)
    Requirement already satisfied: eth-keyfile<0.6.0,>=0.5.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.9->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.5.1)
    Requirement already satisfied: bitarray<3,>=1.2.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.9->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (2.7.3)
    Requirement already satisfied: pycryptodome<4,>=3.6.6 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-hash[pycryptodome]<1.0.0,>=0.2.0->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (3.18.0)
    Requirement already satisfied: cytoolz<1.0.0,>=0.10.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from eth-utils<2.0.0,>=1.9.5->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.12.1)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from jsonschema<5,>=3.2.0->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.19.3)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from requests>=2.18.4->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (2.0.2)
    Requirement already satisfied: idna<4,>=2.5 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from requests>=2.18.4->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (3.4)
    Requirement already satisfied: pycparser in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.0) (2.21)
    Requirement already satisfied: toolz>=0.8.0 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from cytoolz<1.0.0,>=0.10.1->eth-utils<2.0.0,>=1.9.5->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.12.0)
    Requirement already satisfied: netaddr in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (0.8.0)
    Requirement already satisfied: six in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (1.16.0)
    Requirement already satisfied: base58 in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (2.1.1)
    Requirement already satisfied: varint in /home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client==0.1.0) (1.0.2)
    Building wheels for collected packages: rysk-client
      Building editable for rysk-client (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for rysk-client: filename=rysk_client-0.1.0-py3-none-any.whl size=1115 sha256=302ea12484ef8ca6e503f752bea324ec0937cfed1189ddf795bd971f6ea5953e
      Stored in directory: /tmp/pip-ephem-wheel-cache-iidmqn1u/wheels/d0/5d/c5/06071ec2d9be7dfabf83e13d497e7bd4b06d0041d896c67705
    Successfully built rysk-client
    Installing collected packages: rysk-client
      Attempting uninstall: rysk-client
        Found existing installation: rysk-client 0.1.0
        Uninstalling rysk-client-0.1.0:
          Successfully uninstalled rysk-client-0.1.0
    Successfully installed rysk-client-0.1.0
    
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip available: [0m[31;49m22.2.2[0m[39;49m -> [0m[32;49m23.1.2[0m
    [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip install --upgrade pip[0m


# Usage



```python
from rysk_client.src.utils import get_web3

web3 = get_web3()
web3.isConnected()
```




    True



## Creating a Client 

Clients can be created from the rysk client module.


```python
from rysk_client.client import RyskClient

client = RyskClient()
client

```




    RyskClient(_markets=[])



## Fetching Markets

The client can fetch markets as so;



```python
markets = client.fetch_markets()
markets[0]
```




    {'base': 'ETH',
     'baseId': 'ETH',
     'contract': True,
     'contractSize': 0.1,
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
      'netDHVExposure': '-302750000000000000000',
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




    {'ask': 79.375856,
     'bid': 75.910889,
     'info': {'base': 'ETH',
      'baseId': 'ETH',
      'contract': True,
      'contractSize': 0.1,
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
       'netDHVExposure': '-302750000000000000000',
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

#TODO





```python
positions = client.fetch_positions()
positions
```




    []



# Tests


```python
!make test
```

    poetry run adev test -v -p tests
    Testing Open Autonomy Packages
    [2K[2;36m[10:34:59][0m[2;36m [0m[34mINFO    [0m [1m[[0m[33m1m[0m============================= test     ]8;id=171191;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py\[2mcli_executor.py[0m]8;;\[2m:[0m]8;id=497266;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py#36\[2m36[0m]8;;\
    [2;36m           [0m         session starts                            [2m                  [0m
    [2;36m           [0m         ==============================[1m[[0m0m         [2m                  [0m
    [2;36m           [0m         platform linux -- Python [1;36m3.10[0m.[1;36m4[0m,          [2m                  [0m
    [2;36m           [0m         pytest-[1;36m7.3[0m.[1;36m1[0m, pluggy-[1;36m1.0[0m.[1;36m0[0m                [2m                  [0m
    [2;36m           [0m         rootdir:                                  [2m                  [0m
    [2;36m           [0m         [35m/home/tom/Desktop/Fun/[0m[95mrysk_explorations[0m   [2m                  [0m
    [2;36m           [0m         configfile: pytest.ini                    [2m                  [0m
    [2;36m           [0m         plugins: cov-[1;36m3.0[0m.[1;36m0[0m, pylama-[1;36m8.4[0m.[1;36m1[0m,         [2m                  [0m
    [2;36m           [0m         web3-[1;36m5.31[0m.[1;36m4[0m, anyio-[1;36m3.7[0m.[1;36m0[0m                  [2m                  [0m
    [2;36m           [0m         collected [1;36m21[0m items                        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         tests/test_client.py                      [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m31mF[1m[[0m0m[1m[[0m31m              [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m14[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_collateral.py                  [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m31m                      [2m                  [0m
    [2;36m           [0m                        [1m[[0m [1;36m42[0m%[1m][0m[1m[[0m0m                  [2m                  [0m
    [2;36m           [0m         tests/test_rysk_option_market.py          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m31m                      [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m52[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_subgraph.py [1m[[0m32m.[1m[[0m0m[1m[[0m31m       [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m57[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_utils.py                       [2m                  [0m
    [2;36m           [0m         [1m[[0m31mF[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m31mF[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m  [2m                  [0m
    [2;36m           [0m         [1m[[0m31m                                      [2m                  [0m
    [2;36m           [0m         [1m[[0m[1;36m100[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         ===================================       [2m                  [0m
    [2;36m           [0m         FAILURES                                  [2m                  [0m
    [2;36m           [0m         ===================================       [2m                  [0m
    [2;36m           [0m         [1m[[0m31m[1m[[0m1m_____________________________      [2m                  [0m
    [2;36m           [0m         test_fetch_positions                      [2m                  [0m
    [2;36m           [0m         _____________________________[1m[[0m0m          [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         client = [1;35mRyskClient[0m[1m([0m[33m_markets[0m=[1m[[0m[1m][0m[1m)[0m          [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m             [1m[[0m94mdef[1m[[0m[1;36m39[0m;[1;36m49[0m;00m                     [2m                  [0m
    [2;36m           [0m         [1m[[0m92mtest_fetch_positions[1m[[0m[1;36m39[0m;[1;36m49[0m;[1;35m00m[0m[1m([0mclient [2m                  [0m
    [2;36m           [0m         :[1m[[0m90m[1m[[0m[1;36m39[0m;[1;36m49[0m;00m                           [2m                  [0m
    [2;36m           [0m             [1m[[0m90m    [1m[[0m[1;36m39[0m;[1;36m49[0m;00m[1m[[0m33m"[32m""[0mTest         [2m                  [0m
    [2;36m           [0m         fetching                                  [2m                  [0m
    [2;36m           [0m         positions.[32m""[0m"[1m[[0m[1;36m39[0m;[1;36m49[0m;00m[1m[[0m90m[1m[[0m[1;36m39[0m;[1;36m49[0m;00m     [2m                  [0m
    [2;36m           [0m                 positions =                       [2m                  [0m
    [2;36m           [0m         [1;35mclient.fetch_positions[0m[1m([0m[1m)[0m[1m[[0m90m[1m[[0m[1;36m39[0m;[1;36m49[0m;00m    [2m                  [0m
    [2;36m           [0m         >       [1m[[0m94massert[1m[[0m[1;36m39[0m;[1;36m49[0m;00m              [2m                  [0m
    [2;36m           [0m         [1m[[0m96mlen[1m[[0m[1;36m39[0m;[1;36m49[0m;[1;35m00m[0m[1m([0mpositions[1m)[0m >            [2m                  [0m
    [2;36m           [0m         [1m[[0m94m0[1m[[0m[1;36m39[0m;[1;36m49[0m;00m[1m[[0m90m[1m[[0m[1;36m39[0m;[1;36m49[0m;00m             [2m                  [0m
    [2;36m           [0m         [1m[[0m1m[1m[[0m31mE       assert [1;36m0[0m > [1;36m0[0m[1m[[0m0m            [2m                  [0m
    [2;36m           [0m         [1m[[0m1m[1m[[0m31mE        +  where [1;36m0[0m = [1;35mlen[0m[1m([0m[1m[[0m[1m][0m[1m)[0m[1m[[0m0m   [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [1m[[0m1m[1m[[0m31mtests/test_client.py[1m[[0m0m:[1;36m34[0m:        [2m                  [0m
    [2;36m           [0m         AssertionError                            [2m                  [0m
    [2;36m           [0m         [1m[[0m31m[1m[[0m1m______________________________     [2m                  [0m
    [2;36m           [0m         test_get_contract                         [2m                  [0m
    [2;36m           [0m         _______________________________[1m[[0m0m        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         web3 = [1m<[0m[1;95mweb3.main.Web3[0m[39m object at [0m         [2m                  [0m
    [2;36m           [0m         [1;36m0x7f189d5c16f0[0m[39m>[0m                           [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m94mdef[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m                    [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m92mtest_get_contract[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m[39mweb3[0m[1;39m)[0m[39m:[0m[1;39m[[0m[39m90[0m [2m                  [0m
    [2;36m           [0m         [39mm[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m                               [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m90m    [0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[32m""[0m[39mTest whether[0m [2m                  [0m
    [2;36m           [0m         [39mwe can get a contract [0m                    [2m                  [0m
    [2;36m           [0m         [39minstance.[0m[32m""[0m[39m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m      [2m                  [0m
    [2;36m           [0m         [39m>       contract = [0m                       [2m                  [0m
    [2;36m           [0m         [1;35mget_contract[0m[1;39m([0m[39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33mopyn_cont[0m [2m                  [0m
    [2;36m           [0m         [39mroller[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m, [0m         [2m                  [0m
    [2;36m           [0m         [39mweb3[0m[1;39m)[0m[39m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m                       [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mtests/test_utils.py[0m[1;39m[[0m[39m0m:[0m[1;36m19[0m[39m: [0m        [2m                  [0m
    [2;36m           [0m         [39m_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _[0m [2m                  [0m
    [2;36m           [0m         [39m_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ [0m    [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39mname = [0m[32m'opyn_controller'[0m[39m, w3 = [0m           [2m                  [0m
    [2;36m           [0m         [39m<web3.main.Web3 object at [0m[1;36m0x7f189d5c16f0[0m[39m>[0m [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m94mdef[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m                    [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m92mget_contract[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m[39mname, [0m         [2m                  [0m
    [2;36m           [0m         [39mw3[0m[1;39m)[0m[39m:[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m                        [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m90m    [0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[32m""[0m[39mReturns a[0m    [2m                  [0m
    [2;36m           [0m         [39mweb3 contract instance for the given [0m     [2m                  [0m
    [2;36m           [0m         [39mcontract name"[0m[32m""[0m[39m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m  [2m                  [0m
    [2;36m           [0m         [39m        spec = ADDRESSES[0m[39m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m    [2m                  [0m
    [2;36m           [0m         [39m>       [0m[1;39m[[0m[39m94mwith[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m               [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m96mopen[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m[39mspec[0m[1;39m[[0m[39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m  [2m                  [0m
    [2;36m           [0m         [39m33mpath[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m][0m[39m, [0m       [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33mr[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m   [2m                  [0m
    [2;36m           [0m         [1;36m49[0m[39m;00m[0m[1;39m)[0m[39m [0m[1;39m[[0m[39m94mas[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m abi:[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;0[0m [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mE       FileNotFoundError: [0m[1;39m[[0m[39mErrno[0m  [2m                  [0m
    [2;36m           [0m         [1;36m2[0m[1;39m][0m[39m No such file or directory: [0m            [2m                  [0m
    [2;36m           [0m         [32m'contracts/tmp_controller.json'[0m[39m[0m[1;39m[[0m[39m0m[0m        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mrysk_client/src/utils.py[0m[1;39m[[0m[39m0m:[0m[1;36m12[0m[39m:[0m    [2m                  [0m
    [2;36m           [0m         [39mFileNotFoundError[0m                         [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m31m[0m[1;39m[[0m[39m1m__________________ [0m                [2m                  [0m
    [2;36m           [0m         [39mtest_get_contract_address[0m[39m [0m                [2m                  [0m
    [2;36m           [0m         [39m__________________[0m[1;39m[[0m[39m0m[0m                     [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39maddress = [0m[32m'opyn_controller'[0m[39m, web3 = [0m      [2m                  [0m
    [2;36m           [0m         [39m<web3.main.Web3 object at [0m[1;36m0x7f189d5c16f0[0m[39m>[0m [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m37m@pytest[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m.mark.parametriz[0m [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33maddress[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33[0m   [2m                  [0m
    [2;36m           [0m         [39mm"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m, [0m                            [2m                  [0m
    [2;36m           [0m         [1;35mADDRESSES.keys[0m[1;39m([0m[1;39m)[0m[1;39m)[0m[39m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m           [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m94mdef[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m                    [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m92mtest_get_contract_address[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m  [2m                  [0m
    [2;36m           [0m         [39maddress, web3[0m[1;39m)[0m[39m:[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m             [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m90m    [0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[32m""[0m[39mTest whether[0m [2m                  [0m
    [2;36m           [0m         [39mwe can get the contract address for a [0m    [2m                  [0m
    [2;36m           [0m         [39mgiven contract [0m                           [2m                  [0m
    [2;36m           [0m         [39mname"[0m[32m""[0m[39m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m           [2m                  [0m
    [2;36m           [0m         [39m>       contract = [0m[1;35mget_contract[0m[1;39m([0m[39maddress, [0m [2m                  [0m
    [2;36m           [0m         [39mweb3[0m[1;39m)[0m[39m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m                       [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mtests/test_utils.py[0m[1;39m[[0m[39m0m:[0m[1;36m31[0m[39m: [0m        [2m                  [0m
    [2;36m           [0m         [39m_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _[0m [2m                  [0m
    [2;36m           [0m         [39m_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ [0m    [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39mname = [0m[32m'opyn_controller'[0m[39m, w3 = [0m           [2m                  [0m
    [2;36m           [0m         [39m<web3.main.Web3 object at [0m[1;36m0x7f189d5c16f0[0m[39m>[0m [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m94mdef[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m                    [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m92mget_contract[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m[39mname, [0m         [2m                  [0m
    [2;36m           [0m         [39mw3[0m[1;39m)[0m[39m:[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m                        [2m                  [0m
    [2;36m           [0m         [39m    [0m[1;39m[[0m[39m90m    [0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[32m""[0m[39mReturns a[0m    [2m                  [0m
    [2;36m           [0m         [39mweb3 contract instance for the given [0m     [2m                  [0m
    [2;36m           [0m         [39mcontract name"[0m[32m""[0m[39m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m  [2m                  [0m
    [2;36m           [0m         [39m        spec = ADDRESSES[0m[39m[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m    [2m                  [0m
    [2;36m           [0m         [39m>       [0m[1;39m[[0m[39m94mwith[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m [0m               [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m96mopen[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;[0m[1;35m00m[0m[1;39m([0m[39mspec[0m[1;39m[[0m[39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m  [2m                  [0m
    [2;36m           [0m         [39m33mpath[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m][0m[39m, [0m       [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33mr[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m[0m[1;39m[[0m[39m33m"[0m[1;39m[[0m[1;36m39[0m[39m;[0m   [2m                  [0m
    [2;36m           [0m         [1;36m49[0m[39m;00m[0m[1;39m)[0m[39m [0m[1;39m[[0m[39m94mas[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;00m abi:[0m[1;39m[[0m[39m90m[0m[1;39m[[0m[1;36m39[0m[39m;[0m[1;36m49[0m[39m;0[0m [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mE       FileNotFoundError: [0m[1;39m[[0m[39mErrno[0m  [2m                  [0m
    [2;36m           [0m         [1;36m2[0m[1;39m][0m[39m No such file or directory: [0m            [2m                  [0m
    [2;36m           [0m         [32m'contracts/tmp_controller.json'[0m[39m[0m[1;39m[[0m[39m0m[0m        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m1m[0m[1;39m[[0m[39m31mrysk_client/src/utils.py[0m[1;39m[[0m[39m0m:[0m[1;36m12[0m[39m:[0m    [2m                  [0m
    [2;36m           [0m         [39mFileNotFoundError[0m                         [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m36m[0m[1;39m[[0m[33m1m[0m[39m=========================== short[0m  [2m                  [0m
    [2;36m           [0m         [39mtest summary info [0m                        [2m                  [0m
    [2;36m           [0m         [39m============================[0m[1;39m[[0m[39m0m[0m           [2m                  [0m
    [2;36m           [0m         [39m[0m[1;39m[[0m[39m31mFAILED[0m[1;39m[[0m[39m0m [0m                            [2m                  [0m
    [2;36m           [0m         [39mtests/test_client.py::[0m[1;39m[[0m[39m1mtest_fetch_posit[0m [2m                  [0m
    [2;36m           [0m         [39mons[0m[1;39m[[0m[39m0m - assert [0m[1;36m0[0m[39m [0m[1m>[0m [1;36m0[0m                     [2m                  [0m
    [2;36m           [0m         [1m[[0m31mFAILED[1m[[0m0m                             [2m                  [0m
    [2;36m           [0m         tests/test_utils.py::[1m[[0m1mtest_get_contract [2m                  [0m
    [2;36m           [0m         [1m[[0m0m - FileNotFoundError: [1m[[0mErrno [1;36m2[0m[1m][0m No     [2m                  [0m
    [2;36m           [0m         such file or directory:                   [2m                  [0m
    [2;36m           [0m         'contracts/tmp_cont[33m...[0m                    [2m                  [0m
    [2;36m           [0m         [1m[[0m31mFAILED[1m[[0m0m                             [2m                  [0m
    [2;36m           [0m         tests/test_utils.py::[1m[[0m1mtest_get_contract [2m                  [0m
    [2;36m           [0m         address[1m[[0m0m - FileNotFoundError: [1m[[0mErrno    [2m                  [0m
    [2;36m           [0m         [1;36m2[0m[1m][0m No such file or directory:             [2m                  [0m
    [2;36m           [0m         'contracts/tmp_cont[33m...[0m                    [2m                  [0m
    [2;36m           [0m         [1m[[0m[33m31m[0m======================== [1m[[0m31m[1m[[0m1m3     [2m                  [0m
    [2;36m           [0m         failed[1m[[0m0m, [1m[[0m32m18 passed[1m[[0m0m[1m[[0m31m in        [2m                  [0m
    [2;36m           [0m         [1;36m12.[0m59s[1m[[0m0m[1m[[0m31m                             [2m                  [0m
    [2;36m           [0m         =========================[1m[[0m0m              [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2K[2;36m          [0m[2;36m [0m[1;31mERROR   [0m Command failed with return code: [1;36m1[0m        ]8;id=829203;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py\[2mcli_executor.py[0m]8;;\[2m:[0m]8;id=73972;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O72xupT4-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py#42\[2m42[0m]8;;\
    [2KTesting... [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [35m100%[0m [33m0:00:14[0m
    [?25h[31m╭─[0m[31m Error [0m[31m─────────────────────────────────────────────────────────────────────[0m[31m─╮[0m
    [31m│[0m Testing failed!                                                              [31m│[0m
    [31m╰──────────────────────────────────────────────────────────────────────────────╯[0m
                                                                                    
    make: *** [Makefile:48: test] Error 1



```python
!make fmt lint
```

    poetry run isort tests rysk_client && poetry run black tests rysk_client
    Fixing /home/tom/Desktop/Fun/rysk_examples/rysk_client/src/rysk_option_market.py
    [1mreformatted rysk_client/src/rysk_option_market.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m1 file [0m[1mreformatted[0m, [34m15 files [0mleft unchanged.
    poetry run adev lint -v -p tests
    [2;36m[23:54:34][0m[2;36m [0m[34mINFO    [0m Linting Open Autonomy Packages                     ]8;id=796249;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli.py\[2mcli.py[0m]8;;\[2m:[0m]8;id=193368;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli.py#47\[2m47[0m]8;;\
    [2KLinting... [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [35m100%[0m [33m0:00:14[0m
    [?25h[2;36m[23:54:48][0m[2;36m [0m[34mINFO    [0m Linting completed successfully!                    ]8;id=997455;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli.py\[2mcli.py[0m]8;;\[2m:[0m]8;id=911636;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli.py#66\[2m66[0m]8;;\



```python
!make build
```

    poetry run isort tests rysk_client && poetry run black tests rysk_client
    Fixing /home/tom/Desktop/Fun/rysk_examples/rysk_client/src/rysk_option_market.py
    [1mreformatted rysk_client/src/rysk_option_market.py[0m
    
    [1mAll done! ✨ 🍰 ✨[0m
    [34m[1m1 file [0m[1mreformatted[0m, [34m15 files [0mleft unchanged.
    poetry run jupyter-nbconvert README.ipynb --to markdown && poetry run jupyter-nbconvert README.ipynb --to python
    [NbConvertApp] Converting notebook README.ipynb to markdown
    [NbConvertApp] Writing 53191 bytes to README.md
    [NbConvertApp] Converting notebook README.ipynb to python
    [NbConvertApp] Writing 1179 bytes to README.py



```python

```
