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
from tests.conftest import default_address

client = RyskClient()
client

```




    RyskClient(_markets=[])



## Fetching Markets

The client can fetch markets as so;



```python
client.fetch_markets()
```




    [{'base': 'ETH',
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
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x01f460be7389b109cc3599941166ea851d0b7c787badf04b1f276d3ce9269a34',
       'expiration': '1688112000',
       'netDHVExposure': '-312750000000000000000',
       'strike': '1700000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-1700-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1950-P',
      'strike': 1950.0,
      'optionType': 'put',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0x05f8c15b4c2035f26b6ce515ff68aea1ab2780d0aabe526541b3b9dc143be89a',
       'expiration': '1686297600',
       'netDHVExposure': '-87000000000000000000',
       'strike': '1950000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1950-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-02JUN23-1850-P',
      'strike': 1850.0,
      'optionType': 'put',
      'expiry': 1685692800000,
      'expiryDatetime': '2023-06-02T10:00:00.000000Z',
      'info': {'id': '0x24672f24043e48ec96074384886d388e0818fbf8c38cc9e554d284f699603ada',
       'expiration': '1685692800',
       'netDHVExposure': '-522140000000000000000',
       'strike': '1850000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
      'symbol': 'ETH-02JUN23-1850-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-2200-C',
      'strike': 2200.0,
      'optionType': 'call',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x2ae92346e1d10998372d1a93e925148c8b4d701042cf3ebf5154681f31bcc8d5',
       'expiration': '1688112000',
       'netDHVExposure': '-535900000000000000000',
       'strike': '2200000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-2200-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-02JUN23-1900-C',
      'strike': 1900.0,
      'optionType': 'call',
      'expiry': 1685692800000,
      'expiryDatetime': '2023-06-02T10:00:00.000000Z',
      'info': {'id': '0x392c9c6d0785b938cb75eaef191743ab0b65d08be8acae3c3dbe57ee2e20eb50',
       'expiration': '1685692800',
       'netDHVExposure': '-253000000000000000000',
       'strike': '1900000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
      'symbol': 'ETH-02JUN23-1900-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-2100-C',
      'strike': 2100.0,
      'optionType': 'call',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x5d21bef5417a93bc8df49c3e6adc965368641f8cc2146d82ba2d69383deebc51',
       'expiration': '1688112000',
       'netDHVExposure': '-401000000000000000000',
       'strike': '2100000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-2100-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1900-C',
      'strike': 1900.0,
      'optionType': 'call',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0x6917d0216681aaca73e12b6e196634976ad93881eee440b2539a9e58207f2706',
       'expiration': '1686297600',
       'netDHVExposure': '-198000000000000000000',
       'strike': '1900000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1900-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1850-C',
      'strike': 1850.0,
      'optionType': 'call',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0x6c18acd213c7606d5f43ea297174945d525ab23a07380ec3734e761865ee7ae3',
       'expiration': '1686297600',
       'netDHVExposure': '-102000000000000000000',
       'strike': '1850000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1850-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1850-P',
      'strike': 1850.0,
      'optionType': 'put',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0x6d7fdfcdbb640348bebab61e2bd9bf01575caaabc038e1c4ed358acd35d78eca',
       'expiration': '1686297600',
       'netDHVExposure': '-54000000000000000000',
       'strike': '1850000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1850-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-1900-P',
      'strike': 1900.0,
      'optionType': 'put',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x6fef5b4d3ba580cb569020fb1085b27b439b1a971ebfc32ca95446fe88966a28',
       'expiration': '1688112000',
       'netDHVExposure': '-62000000000000000000',
       'strike': '1900000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-1900-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-1800-P',
      'strike': 1800.0,
      'optionType': 'put',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x71ef2d74c07d74df0b56af1ee1bae3bf1db892b711e6803b48fa0b19f77188a6',
       'expiration': '1688112000',
       'netDHVExposure': '-226000000000000000000',
       'strike': '1800000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-1800-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-02JUN23-1900-P',
      'strike': 1900.0,
      'optionType': 'put',
      'expiry': 1685692800000,
      'expiryDatetime': '2023-06-02T10:00:00.000000Z',
      'info': {'id': '0x80a5505e2ad615e62d78a3fa58559ac79d57e40248e5a09fe3e80eb820db4ed1',
       'expiration': '1685692800',
       'netDHVExposure': '-296600000000000000000',
       'strike': '1900000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
      'symbol': 'ETH-02JUN23-1900-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-02JUN23-1950-C',
      'strike': 1950.0,
      'optionType': 'call',
      'expiry': 1685692800000,
      'expiryDatetime': '2023-06-02T10:00:00.000000Z',
      'info': {'id': '0x837dbfde8a60c23a25ddd015a16115f3e815edfed2f20601a254f8609d7b9428',
       'expiration': '1685692800',
       'netDHVExposure': '-446250000000000000000',
       'strike': '1950000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
      'symbol': 'ETH-02JUN23-1950-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-2000-C',
      'strike': 2000.0,
      'optionType': 'call',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0x99e2fe8cc986a281b8288410fa541add3b31dadc2e95549541628500fa342115',
       'expiration': '1688112000',
       'netDHVExposure': '-299500000000000000000',
       'strike': '2000000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-2000-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-2050-C',
      'strike': 2050.0,
      'optionType': 'call',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0xabc1eaa1dd5db3c797b18dafb73bf5148b35066ec0feacb775027e2222925542',
       'expiration': '1686297600',
       'netDHVExposure': '-530000000000000000000',
       'strike': '2050000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-2050-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1950-C',
      'strike': 1950.0,
      'optionType': 'call',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0xb2387a146721aaa3b4c603b11c4b3fb941f995aa69d2a6a513691391f99f9d2d',
       'expiration': '1686297600',
       'netDHVExposure': '-266000000000000000000',
       'strike': '1950000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1950-C',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-30JUN23-1600-P',
      'strike': 1600.0,
      'optionType': 'put',
      'expiry': 1688112000000,
      'expiryDatetime': '2023-06-30T10:00:00.000000Z',
      'info': {'id': '0xb359d82225bf43504d30f857f62271a57a401c1716fa5d7a80fff7698ac35e64',
       'expiration': '1688112000',
       'netDHVExposure': '-454000000000000000000',
       'strike': '1600000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
      'symbol': 'ETH-30JUN23-1600-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-1900-P',
      'strike': 1900.0,
      'optionType': 'put',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0xb646a4c7715e05bf260c67e2c856a662448cee8d833fd48d96e5250cfaa9f665',
       'expiration': '1686297600',
       'netDHVExposure': '-198000000000000000000',
       'strike': '1900000000000000000000',
       'isPut': True,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-1900-P',
      'maker': 0.0003,
      'taker': 0.0003},
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
      'id': 'ETH-09JUN23-2100-C',
      'strike': 2100.0,
      'optionType': 'call',
      'expiry': 1686297600000,
      'expiryDatetime': '2023-06-09T10:00:00.000000Z',
      'info': {'id': '0xb8757847f588771bba842e8e85417b32fb304283205bed38b9ed3cbf43590ceb',
       'expiration': '1686297600',
       'netDHVExposure': '0',
       'strike': '2100000000000000000000',
       'isPut': False,
       'isBuyable': True,
       'isSellable': True,
       'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
      'symbol': 'ETH-09JUN23-2100-C',
      'maker': 0.0003,
      'taker': 0.0003}]



## Fetching Tickers

Tickers can be fetched from the client as so;


```python
tickets = client.fetch_tickers()
tickets
```




    [{'ask': 72.819391,
      'bid': 69.393398,
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
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x01f460be7389b109cc3599941166ea851d0b7c787badf04b1f276d3ce9269a34',
        'expiration': '1688112000',
        'netDHVExposure': '-312750000000000000000',
        'strike': '1700000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-1700-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 95.241591,
      'bid': 93.306821,
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
       'id': 'ETH-09JUN23-1950-P',
       'strike': 1950.0,
       'optionType': 'put',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0x05f8c15b4c2035f26b6ce515ff68aea1ab2780d0aabe526541b3b9dc143be89a',
        'expiration': '1686297600',
        'netDHVExposure': '-87000000000000000000',
        'strike': '1950000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1950-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 33.60556,
      'bid': 33.335265,
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
       'id': 'ETH-02JUN23-1850-P',
       'strike': 1850.0,
       'optionType': 'put',
       'expiry': 1685692800000,
       'expiryDatetime': '2023-06-02T10:00:00.000000Z',
       'info': {'id': '0x24672f24043e48ec96074384886d388e0818fbf8c38cc9e554d284f699603ada',
        'expiration': '1685692800',
        'netDHVExposure': '-522140000000000000000',
        'strike': '1850000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
       'symbol': 'ETH-02JUN23-1850-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 107.671024,
      'bid': 104.41948,
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
       'id': 'ETH-30JUN23-2200-C',
       'strike': 2200.0,
       'optionType': 'call',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x2ae92346e1d10998372d1a93e925148c8b4d701042cf3ebf5154681f31bcc8d5',
        'expiration': '1688112000',
        'netDHVExposure': '-535900000000000000000',
        'strike': '2200000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-2200-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 60.38051,
      'bid': 59.923901,
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
       'id': 'ETH-02JUN23-1900-C',
       'strike': 1900.0,
       'optionType': 'call',
       'expiry': 1685692800000,
       'expiryDatetime': '2023-06-02T10:00:00.000000Z',
       'info': {'id': '0x392c9c6d0785b938cb75eaef191743ab0b65d08be8acae3c3dbe57ee2e20eb50',
        'expiration': '1685692800',
        'netDHVExposure': '-253000000000000000000',
        'strike': '1900000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
       'symbol': 'ETH-02JUN23-1900-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 112.884477,
      'bid': 109.222633,
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
       'id': 'ETH-30JUN23-2100-C',
       'strike': 2100.0,
       'optionType': 'call',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x5d21bef5417a93bc8df49c3e6adc965368641f8cc2146d82ba2d69383deebc51',
        'expiration': '1688112000',
        'netDHVExposure': '-401000000000000000000',
        'strike': '2100000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-2100-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 96.079912,
      'bid': 94.58646,
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
       'id': 'ETH-09JUN23-1900-C',
       'strike': 1900.0,
       'optionType': 'call',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0x6917d0216681aaca73e12b6e196634976ad93881eee440b2539a9e58207f2706',
        'expiration': '1686297600',
        'netDHVExposure': '-198000000000000000000',
        'strike': '1900000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1900-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 114.596411,
      'bid': 112.792414,
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
       'id': 'ETH-09JUN23-1850-C',
       'strike': 1850.0,
       'optionType': 'call',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0x6c18acd213c7606d5f43ea297174945d525ab23a07380ec3734e761865ee7ae3',
        'expiration': '1686297600',
        'netDHVExposure': '-102000000000000000000',
        'strike': '1850000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1850-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 31.153475,
      'bid': 30.046058,
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
       'id': 'ETH-09JUN23-1850-P',
       'strike': 1850.0,
       'optionType': 'put',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0x6d7fdfcdbb640348bebab61e2bd9bf01575caaabc038e1c4ed358acd35d78eca',
        'expiration': '1686297600',
        'netDHVExposure': '-54000000000000000000',
        'strike': '1850000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1850-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 107.913758,
      'bid': 102.406854,
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
       'id': 'ETH-30JUN23-1900-P',
       'strike': 1900.0,
       'optionType': 'put',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x6fef5b4d3ba580cb569020fb1085b27b439b1a971ebfc32ca95446fe88966a28',
        'expiration': '1688112000',
        'netDHVExposure': '-62000000000000000000',
        'strike': '1900000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-1900-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 98.805695,
      'bid': 94.446677,
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
       'id': 'ETH-30JUN23-1800-P',
       'strike': 1800.0,
       'optionType': 'put',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x71ef2d74c07d74df0b56af1ee1bae3bf1db892b711e6803b48fa0b19f77188a6',
        'expiration': '1688112000',
        'netDHVExposure': '-226000000000000000000',
        'strike': '1800000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-1800-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 48.980709,
      'bid': 48.541962,
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
       'id': 'ETH-02JUN23-1900-P',
       'strike': 1900.0,
       'optionType': 'put',
       'expiry': 1685692800000,
       'expiryDatetime': '2023-06-02T10:00:00.000000Z',
       'info': {'id': '0x80a5505e2ad615e62d78a3fa58559ac79d57e40248e5a09fe3e80eb820db4ed1',
        'expiration': '1685692800',
        'netDHVExposure': '-296600000000000000000',
        'strike': '1900000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
       'symbol': 'ETH-02JUN23-1900-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 36.1539,
      'bid': 35.879782,
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
       'id': 'ETH-02JUN23-1950-C',
       'strike': 1950.0,
       'optionType': 'call',
       'expiry': 1685692800000,
       'expiryDatetime': '2023-06-02T10:00:00.000000Z',
       'info': {'id': '0x837dbfde8a60c23a25ddd015a16115f3e815edfed2f20601a254f8609d7b9428',
        'expiration': '1685692800',
        'netDHVExposure': '-446250000000000000000',
        'strike': '1950000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 2, 10, 0)},
       'symbol': 'ETH-02JUN23-1950-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 136.762863,
      'bid': 132.430117,
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
       'id': 'ETH-30JUN23-2000-C',
       'strike': 2000.0,
       'optionType': 'call',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0x99e2fe8cc986a281b8288410fa541add3b31dadc2e95549541628500fa342115',
        'expiration': '1688112000',
        'netDHVExposure': '-299500000000000000000',
        'strike': '2000000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-2000-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 57.951742,
      'bid': 57.119575,
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
       'id': 'ETH-09JUN23-2050-C',
       'strike': 2050.0,
       'optionType': 'call',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0xabc1eaa1dd5db3c797b18dafb73bf5148b35066ec0feacb775027e2222925542',
        'expiration': '1686297600',
        'netDHVExposure': '-530000000000000000000',
        'strike': '2050000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-2050-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 70.869248,
      'bid': 69.683233,
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
       'id': 'ETH-09JUN23-1950-C',
       'strike': 1950.0,
       'optionType': 'call',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0xb2387a146721aaa3b4c603b11c4b3fb941f995aa69d2a6a513691391f99f9d2d',
        'expiration': '1686297600',
        'netDHVExposure': '-266000000000000000000',
        'strike': '1950000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1950-C',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 65.030149,
      'bid': 62.204251,
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
       'id': 'ETH-30JUN23-1600-P',
       'strike': 1600.0,
       'optionType': 'put',
       'expiry': 1688112000000,
       'expiryDatetime': '2023-06-30T10:00:00.000000Z',
       'info': {'id': '0xb359d82225bf43504d30f857f62271a57a401c1716fa5d7a80fff7698ac35e64',
        'expiration': '1688112000',
        'netDHVExposure': '-454000000000000000000',
        'strike': '1600000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 30, 10, 0)},
       'symbol': 'ETH-30JUN23-1600-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 81.743668,
      'bid': 80.187648,
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
       'id': 'ETH-09JUN23-1900-P',
       'strike': 1900.0,
       'optionType': 'put',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0xb646a4c7715e05bf260c67e2c856a662448cee8d833fd48d96e5250cfaa9f665',
        'expiration': '1686297600',
        'netDHVExposure': '-198000000000000000000',
        'strike': '1900000000000000000000',
        'isPut': True,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-1900-P',
       'maker': 0.0003,
       'taker': 0.0003}},
     {'ask': 7.231614,
      'bid': 6.641992,
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
       'id': 'ETH-09JUN23-2100-C',
       'strike': 2100.0,
       'optionType': 'call',
       'expiry': 1686297600000,
       'expiryDatetime': '2023-06-09T10:00:00.000000Z',
       'info': {'id': '0xb8757847f588771bba842e8e85417b32fb304283205bed38b9ed3cbf43590ceb',
        'expiration': '1686297600',
        'netDHVExposure': '0',
        'strike': '2100000000000000000000',
        'isPut': False,
        'isBuyable': True,
        'isSellable': True,
        'expiration_datetime': datetime.datetime(2023, 6, 9, 10, 0)},
       'symbol': 'ETH-09JUN23-2100-C',
       'maker': 0.0003,
       'taker': 0.0003}}]



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
    [2K[2;36m[23:14:12][0m[2;36m [0m[34mINFO    [0m [1m[[0m[33m1m[0m============================= test     ]8;id=242770;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py\[2mcli_executor.py[0m]8;;\[2m:[0m]8;id=10279;file:///home/tom/.cache/pypoetry/virtualenvs/rysk-client-O5czFfvY-py3.10/lib/python3.10/site-packages/auto_dev/cli_executor.py#36\[2m36[0m]8;;\
    [2;36m           [0m         session starts                            [2m                  [0m
    [2;36m           [0m         ==============================[1m[[0m0m         [2m                  [0m
    [2;36m           [0m         platform linux -- Python [1;36m3.10[0m.[1;36m0[0m,          [2m                  [0m
    [2;36m           [0m         pytest-[1;36m7.3[0m.[1;36m1[0m, pluggy-[1;36m1.0[0m.[1;36m0[0m                [2m                  [0m
    [2;36m           [0m         rootdir:                                  [2m                  [0m
    [2;36m           [0m         [35m/home/tom/Desktop/Fun/[0m[95mrysk_examples[0m       [2m                  [0m
    [2;36m           [0m         configfile: pytest.ini                    [2m                  [0m
    [2;36m           [0m         plugins: cov-[1;36m3.0[0m.[1;36m0[0m, web3-[1;36m5.31[0m.[1;36m4[0m,          [2m                  [0m
    [2;36m           [0m         pylama-[1;36m8.4[0m.[1;36m1[0m                              [2m                  [0m
    [2;36m           [0m         collected [1;36m19[0m items                        [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         tests/test_client.py [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m10[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_collateral.py                  [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m                      [2m                  [0m
    [2;36m           [0m                        [1m[[0m [1;36m42[0m%[1m][0m[1m[[0m0m                  [2m                  [0m
    [2;36m           [0m         tests/test_rysk_option_market.py          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m                      [2m                  [0m
    [2;36m           [0m         [1m[[0m [1;36m52[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m         tests/test_utils.py                       [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m          [2m                  [0m
    [2;36m           [0m         [1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m[1m[[0m32m.[1m[[0m0m  [2m                  [0m
    [2;36m           [0m         [1m[[0m32m                                      [2m                  [0m
    [2;36m           [0m         [1m[[0m[1;36m100[0m%[1m][0m[1m[[0m0m                                 [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2;36m           [0m         [1m[[0m[33m32m[0m=============================         [2m                  [0m
    [2;36m           [0m         [1m[[0m32m[1m[[0m1m19 passed[1m[[0m0m[1m[[0m32m in [1;36m38.[0m24s[1m[[0m0m[1m[[0m32m  [2m                  [0m
    [2;36m           [0m         ==============================[1m[[0m0m         [2m                  [0m
    [2;36m           [0m                                                   [2m                  [0m
    [2KTesting... [38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [35m100%[0m [33m0:00:44[0m
    [?25hTesting completed successfully!



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
