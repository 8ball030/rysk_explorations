# Rysk Client

## Installation

### Dev

dependencies are managed with poetry. 

For dev build.


```python
!pip install rysk-client
```

    Requirement already satisfied: rysk-client in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (0.1.3)
    Requirement already satisfied: web3<6.0.0,>=5.4.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rysk-client) (5.25.0)
    Requirement already satisfied: ccxt<4.0.0,>=3.1.15 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rysk-client) (3.1.17)
    Requirement already satisfied: requests>=2.18.4 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (2.28.1)
    Requirement already satisfied: cryptography>=2.6.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (39.0.1)
    Requirement already satisfied: setuptools>=60.9.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (67.8.0)
    Requirement already satisfied: aiodns>=1.1.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (3.0.0)
    Requirement already satisfied: certifi>=2018.1.18 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (2022.6.15)
    Requirement already satisfied: aiohttp>=3.8 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (3.8.4)
    Requirement already satisfied: yarl>=1.7.2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client) (1.7.2)
    Requirement already satisfied: protobuf<4,>=3.10.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (3.20.3)
    Requirement already satisfied: eth-typing<3.0.0,>=2.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (2.3.0)
    Requirement already satisfied: hexbytes<1.0.0,>=0.1.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (0.3.0)
    Requirement already satisfied: eth-utils<2.0.0,>=1.9.5 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (1.9.5)
    Requirement already satisfied: websockets<10,>=9.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (9.1)
    Requirement already satisfied: lru-dict<2.0.0,>=1.1.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (1.1.8)
    Requirement already satisfied: eth-account<0.6.0,>=0.5.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (0.5.6)
    Requirement already satisfied: eth-hash[pycryptodome]<1.0.0,>=0.2.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (0.5.0)
    Requirement already satisfied: ipfshttpclient==0.8.0a2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (0.8.0a2)
    Requirement already satisfied: jsonschema<4.0.0,>=3.2.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (3.2.0)
    Requirement already satisfied: eth-abi<3.0.0,>=2.0.0b6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3<6.0.0,>=5.4.0->rysk-client) (2.2.0)
    Requirement already satisfied: multiaddr>=0.0.7 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client) (0.0.9)
    Requirement already satisfied: pycares>=4.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiodns>=1.1.1->ccxt<4.0.0,>=3.1.15->rysk-client) (4.2.2)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (6.0.2)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (4.0.2)
    Requirement already satisfied: attrs>=17.3.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (22.1.0)
    Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (2.1.1)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (1.3.1)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.8->ccxt<4.0.0,>=3.1.15->rysk-client) (1.2.0)
    Requirement already satisfied: cffi>=1.12 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client) (1.15.1)
    Requirement already satisfied: parsimonious<0.9.0,>=0.8.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-abi<3.0.0,>=2.0.0b6->web3<6.0.0,>=5.4.0->rysk-client) (0.8.1)
    Requirement already satisfied: rlp<3,>=1.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.6->web3<6.0.0,>=5.4.0->rysk-client) (2.0.1)
    Requirement already satisfied: eth-rlp<2,>=0.1.2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.6->web3<6.0.0,>=5.4.0->rysk-client) (0.2.1)
    Requirement already satisfied: bitarray<1.3.0,>=1.2.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.6->web3<6.0.0,>=5.4.0->rysk-client) (1.2.2)
    Requirement already satisfied: eth-keyfile<0.6.0,>=0.5.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.6->web3<6.0.0,>=5.4.0->rysk-client) (0.5.1)
    Requirement already satisfied: eth-keys!=0.3.2,<0.4.0,>=0.2.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account<0.6.0,>=0.5.6->web3<6.0.0,>=5.4.0->rysk-client) (0.3.4)
    Requirement already satisfied: pycryptodome<4,>=3.6.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-hash[pycryptodome]<1.0.0,>=0.2.0->web3<6.0.0,>=5.4.0->rysk-client) (3.15.0)
    Requirement already satisfied: cytoolz<1.0.0,>=0.10.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-utils<2.0.0,>=1.9.5->web3<6.0.0,>=5.4.0->rysk-client) (0.12.0)
    Requirement already satisfied: pyrsistent>=0.14.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from jsonschema<4.0.0,>=3.2.0->web3<6.0.0,>=5.4.0->rysk-client) (0.18.1)
    Requirement already satisfied: six>=1.11.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from jsonschema<4.0.0,>=3.2.0->web3<6.0.0,>=5.4.0->rysk-client) (1.16.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from requests>=2.18.4->ccxt<4.0.0,>=3.1.15->rysk-client) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from requests>=2.18.4->ccxt<4.0.0,>=3.1.15->rysk-client) (1.26.12)
    Requirement already satisfied: pycparser in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client) (2.21)
    Requirement already satisfied: toolz>=0.8.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cytoolz<1.0.0,>=0.10.1->eth-utils<2.0.0,>=1.9.5->web3<6.0.0,>=5.4.0->rysk-client) (0.11.2)
    Requirement already satisfied: netaddr in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client) (0.8.0)
    Requirement already satisfied: base58 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client) (2.1.1)
    Requirement already satisfied: varint in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3<6.0.0,>=5.4.0->rysk-client) (1.0.2)
    [33mWARNING: Error parsing requirements for vulture: [Errno 2] No such file or directory: '/home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages/vulture-2.5.dist-info/METADATA'[0m[33m
    [0m[33mWARNING: You are using pip version 22.0.4; however, version 23.1.2 is available.    You should consider upgrading via the '/home/tom/.pyenv/versions/3.10.4/bin/python3.10 -m pip install --upgrade pip' command.[0m[33m
    [0m

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
from tests.conftest import DEFAULT_ADDRESS

auth = {
    "address": DEFAULT_ADDRESS,
}

client = RyskClient(**auth)
client

```




    RyskClient(_markets=[], _tickers=[])



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
      'netDHVExposure': '-250750000000000000000',
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




    {'ask': 48.491057,
     'bid': 45.859793,
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
       'netDHVExposure': '-250750000000000000000',
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
positions
```




    [{'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x1c10ac5fa8fd1e33ea5aeb457e44cf68ec3038db-l-0',
      'symbol': 'ETH-26MAY23-1900-C',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 6.91313142e-10,
      'realizedPnl': 6.91313142e-10,
      'contractSize': '0',
      'markPrice': 1.9e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x703e6bc2e1541d603ff9fdb26216617e1687b8d6-l-0',
      'symbol': 'ETH-19MAY23-1900-C',
      'timestamp': 1684483200000,
      'datetime': datetime.datetime(2023, 5, 19, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.079670014e-09,
      'realizedPnl': 1.079670014e-09,
      'contractSize': '0',
      'markPrice': 1.9e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x782b21d4061a1953a667a15b9c82c53abfd6173e-l-0',
      'symbol': 'ETH-30JUN23-1800-P',
      'timestamp': 1688112000000,
      'datetime': datetime.datetime(2023, 6, 30, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': -1.348442599e-09,
      'realizedPnl': -1.348442599e-09,
      'contractSize': '10000000000000000000',
      'markPrice': 1.8e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x804a8b8f14860cda487aa8ad98cd13d68510be54-l-0',
      'symbol': 'ETH-30JUN23-1700-P',
      'timestamp': 1688112000000,
      'datetime': datetime.datetime(2023, 6, 30, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 7.69341062e-10,
      'realizedPnl': 7.69341062e-10,
      'contractSize': '0',
      'markPrice': 1.7e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xc803a30a9c0f74c934c1731c6d85d862bbfbe1ef-l-0',
      'symbol': 'ETH-26MAY23-1650-P',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.768679112e-09,
      'realizedPnl': 1.768679112e-09,
      'contractSize': '0',
      'markPrice': 1.65e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xc803a30a9c0f74c934c1731c6d85d862bbfbe1ef-l-1',
      'symbol': 'ETH-26MAY23-1650-P',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': -1.81703236e-09,
      'realizedPnl': -1.81703236e-09,
      'contractSize': '30000000000000000000',
      'markPrice': 1.65e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xcbb60ce369853f41953d2d494490bfb0370e8ea3-l-0',
      'symbol': 'ETH-26MAY23-1950-C',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.337283147e-09,
      'realizedPnl': 1.337283147e-09,
      'contractSize': '0',
      'markPrice': 1.95e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xd025a593885cfe807e31e8b0eb7fd0a4d21bcd77-l-0',
      'symbol': 'ETH-26MAY23-2000-C',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.03734548e-09,
      'realizedPnl': 1.03734548e-09,
      'contractSize': '0',
      'markPrice': 2e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xd025a593885cfe807e31e8b0eb7fd0a4d21bcd77-l-1',
      'symbol': 'ETH-26MAY23-2000-C',
      'timestamp': 1685088000000,
      'datetime': datetime.datetime(2023, 5, 26, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': -2.620062691e-09,
      'realizedPnl': -2.620062691e-09,
      'contractSize': '45000000000000000000',
      'markPrice': 2e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xe634f92a80bad9dc255711b3834af8d56172e43d-l-0',
      'symbol': 'ETH-19MAY23-1800-P',
      'timestamp': 1684483200000,
      'datetime': datetime.datetime(2023, 5, 19, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 6.103186586e-09,
      'realizedPnl': 6.103186586e-09,
      'contractSize': '0',
      'markPrice': 1.8e-07,
      'side': 'long'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x3fa148f692e516654283c9ff4cbe3b15355f48f5-s-0',
      'symbol': 'ETH-19MAY23-2000-C',
      'timestamp': 1684483200000,
      'datetime': datetime.datetime(2023, 5, 19, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.744192333e-09,
      'realizedPnl': 1.744192333e-09,
      'contractSize': '-20000000000000000000',
      'markPrice': 2e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x752734d923d4a9de4ae6cc0287ae47f71385a5b9-s-0',
      'symbol': 'ETH-30JUN23-1600-P',
      'timestamp': 1688112000000,
      'datetime': datetime.datetime(2023, 6, 30, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 8.375450512e-09,
      'realizedPnl': 8.375450512e-09,
      'contractSize': '-30000000000000000000',
      'markPrice': 1.6e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x77d9fecf81257174918716795ba800dc1e2d1a0b-s-0',
      'symbol': 'ETH-12MAY23-1900-C',
      'timestamp': 1683878400000,
      'datetime': datetime.datetime(2023, 5, 12, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 8.45899975e-10,
      'realizedPnl': 8.45899975e-10,
      'contractSize': '-8000000000000000000',
      'markPrice': 1.9e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0x8106b5dd2c7be79f2e0cf428b4ac9a64e8c33c25-s-0',
      'symbol': 'ETH-12MAY23-1900-C',
      'timestamp': 1683878400000,
      'datetime': datetime.datetime(2023, 5, 12, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 9.91711253e-10,
      'realizedPnl': 9.91711253e-10,
      'contractSize': '0',
      'markPrice': 1.9e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xd71166f45adff0e89d156025368988f6b9412ce7-s-0',
      'symbol': 'ETH-19MAY23-2000-C',
      'timestamp': 1684483200000,
      'datetime': datetime.datetime(2023, 5, 19, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 3.723067361e-09,
      'realizedPnl': 3.723067361e-09,
      'contractSize': '-25000000000000000000',
      'markPrice': 2e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xe634f92a80bad9dc255711b3834af8d56172e43d-s-0',
      'symbol': 'ETH-19MAY23-1800-P',
      'timestamp': 1684483200000,
      'datetime': datetime.datetime(2023, 5, 19, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 5.6730516e-10,
      'realizedPnl': 5.6730516e-10,
      'contractSize': '0',
      'markPrice': 1.8e-07,
      'side': 'short'},
     {'id': '0x588d91abf5192a0f0dc026bf05f510253bd1cf51-0xf321adea24fe24c94389078f561011adbd789ed8-s-0',
      'symbol': 'ETH-12MAY23-1800-P',
      'timestamp': 1683878400000,
      'datetime': datetime.datetime(2023, 5, 12, 9, 0),
      'initialMarginPercentage': None,
      'unrealizedPnl': 1.343280484e-09,
      'realizedPnl': 1.343280484e-09,
      'contractSize': '-10000000000000000000',
      'markPrice': 1.8e-07,
      'side': 'short'}]



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

