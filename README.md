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

    Processing /home/tom/Desktop/Fun/rysk_explorations
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hRequirement already satisfied: web3==6.4.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rysk-client==0.1.8) (6.4.0)
    Requirement already satisfied: ccxt<4.0.0,>=3.1.15 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rysk-client==0.1.8) (3.1.17)
    Requirement already satisfied: rich-click<2.0.0,>=1.6.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rysk-client==0.1.8) (1.6.1)
    Requirement already satisfied: jsonschema>=4.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (4.17.3)
    Requirement already satisfied: requests>=2.16.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (2.28.1)
    Requirement already satisfied: eth-abi>=4.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (4.0.0)
    Requirement already satisfied: eth-account>=0.8.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (0.9.0)
    Requirement already satisfied: aiohttp>=3.7.4.post0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (3.8.4)
    Requirement already satisfied: eth-hash[pycryptodome]>=0.5.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (0.5.2)
    Requirement already satisfied: hexbytes>=0.1.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (0.3.0)
    Requirement already satisfied: lru-dict>=1.1.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (1.1.8)
    Requirement already satisfied: eth-typing>=3.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (3.4.0)
    Requirement already satisfied: eth-utils>=2.1.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (2.1.1)
    Requirement already satisfied: protobuf>=4.21.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (4.23.2)
    Requirement already satisfied: websockets>=10.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from web3==6.4.0->rysk-client==0.1.8) (11.0.3)
    Requirement already satisfied: cryptography>=2.6.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (39.0.1)
    Requirement already satisfied: aiodns>=1.1.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (3.0.0)
    Requirement already satisfied: certifi>=2018.1.18 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (2022.6.15)
    Requirement already satisfied: yarl>=1.7.2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (1.7.2)
    Requirement already satisfied: setuptools>=60.9.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (67.8.0)
    Requirement already satisfied: rich>=10.7.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rich-click<2.0.0,>=1.6.1->rysk-client==0.1.8) (13.3.1)
    Requirement already satisfied: click>=7 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rich-click<2.0.0,>=1.6.1->rysk-client==0.1.8) (8.0.2)
    Requirement already satisfied: pycares>=4.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiodns>=1.1.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (4.2.2)
    Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (2.1.1)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (1.3.1)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (4.0.2)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (1.2.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (6.0.2)
    Requirement already satisfied: attrs>=17.3.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from aiohttp>=3.7.4.post0->web3==6.4.0->rysk-client==0.1.8) (22.1.0)
    Requirement already satisfied: cffi>=1.12 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (1.15.1)
    Requirement already satisfied: parsimonious<0.10.0,>=0.9.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-abi>=4.0.0->web3==6.4.0->rysk-client==0.1.8) (0.9.0)
    Requirement already satisfied: eth-rlp>=0.3.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.8) (0.3.0)
    Requirement already satisfied: rlp>=1.0.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.8) (3.0.0)
    Requirement already satisfied: eth-keys>=0.4.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.8) (0.4.0)
    Requirement already satisfied: eth-keyfile>=0.6.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.8) (0.6.1)
    Requirement already satisfied: bitarray>=2.4.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-account>=0.8.0->web3==6.4.0->rysk-client==0.1.8) (2.7.4)
    Requirement already satisfied: pycryptodome<4,>=3.6.6 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-hash[pycryptodome]>=0.5.1->web3==6.4.0->rysk-client==0.1.8) (3.15.0)
    Requirement already satisfied: cytoolz>=0.10.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from eth-utils>=2.1.0->web3==6.4.0->rysk-client==0.1.8) (0.12.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from jsonschema>=4.0.0->web3==6.4.0->rysk-client==0.1.8) (0.18.1)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from requests>=2.16.0->web3==6.4.0->rysk-client==0.1.8) (1.26.12)
    Requirement already satisfied: idna<4,>=2.5 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from requests>=2.16.0->web3==6.4.0->rysk-client==0.1.8) (3.3)
    Requirement already satisfied: markdown-it-py<3.0.0,>=2.1.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.8) (2.2.0)
    Requirement already satisfied: pygments<3.0.0,>=2.14.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.8) (2.14.0)
    Requirement already satisfied: pycparser in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cffi>=1.12->cryptography>=2.6.1->ccxt<4.0.0,>=3.1.15->rysk-client==0.1.8) (2.21)
    Requirement already satisfied: toolz>=0.8.0 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from cytoolz>=0.10.1->eth-utils>=2.1.0->web3==6.4.0->rysk-client==0.1.8) (0.11.2)
    Requirement already satisfied: mdurl~=0.1 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from markdown-it-py<3.0.0,>=2.1.0->rich>=10.7.0->rich-click<2.0.0,>=1.6.1->rysk-client==0.1.8) (0.1.2)
    Requirement already satisfied: regex>=2022.3.15 in /home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages (from parsimonious<0.10.0,>=0.9.0->eth-abi>=4.0.0->web3==6.4.0->rysk-client==0.1.8) (2023.6.3)
    Building wheels for collected packages: rysk-client
      Building wheel for rysk-client (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for rysk-client: filename=rysk_client-0.1.8-py3-none-any.whl size=502097 sha256=b11b92629c38b8e9e13c79cb02a87a28104d78d7262ae3662c364ba00ad48441
      Stored in directory: /tmp/pip-ephem-wheel-cache-47uzb13y/wheels/85/5d/62/83b40ae2d2c1fc31bec44436912ab30c592085539d92f35254
    Successfully built rysk-client
    [33mWARNING: Error parsing requirements for vulture: [Errno 2] No such file or directory: '/home/tom/.pyenv/versions/3.10.4/lib/python3.10/site-packages/vulture-2.5.dist-info/METADATA'[0m[33m
    [0mInstalling collected packages: rysk-client
      Attempting uninstall: rysk-client
        Found existing installation: rysk-client 0.1.8
        Uninstalling rysk-client-0.1.8:
          Successfully uninstalled rysk-client-0.1.8
    Successfully installed rysk-client-0.1.8
    [33mWARNING: You are using pip version 22.0.4; however, version 23.1.2 is available.
    You should consider upgrading via the '/home/tom/.pyenv/versions/3.10.4/bin/python3.10 -m pip install --upgrade pip' command.[0m[33m
    [0m

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

