# Rysk Client

The rysk python client offers a programatic means by which to interact with the (Rysk Finance Protocol)

## Installation

The application is availale on pypi and can be installed as so

```bash
pip install rysk-client
```


## Cli Tool

The application is also bundled as cli tool to allow users to interact with the protocol from the cli.




![alt text](demo.gif "Title")


## Creating a Client 

Clients can be created from the rysk client module.


```python

```

### Markets
We can fetch data about the markets as so;


```python
! rysk markets fetch
```

    Traceback (most recent call last):
      File "/home/tom/.pyenv/versions/3.9.9/bin/rysk", line 8, in <module>
        sys.exit(cli())
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1126, in __call__
        return self.main(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rich_click/rich_group.py", line 21, in main
        rv = super().main(*args, standalone_mode=False, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1051, in main
        rv = self.invoke(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1654, in invoke
        super().invoke(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1393, in invoke
        return ctx.invoke(self.callback, **ctx.params)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 752, in invoke
        return __callback(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/decorators.py", line 26, in new_func
        return f(get_current_context(), *args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py", line 55, in cli
        ctx.obj["client"] = set_client(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py", line 32, in set_client
        "address": os.environ["ETH_ADDRESS"],
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/os.py", line 679, in __getitem__
        raise KeyError(key) from None
    KeyError: 'ETH_ADDRESS'



```python

```

# Positions

We can view the current positions, along with those which are expired.


```python
!rysk positions list
```

    Traceback (most recent call last):
      File "/home/tom/.pyenv/versions/3.9.9/bin/rysk", line 8, in <module>
        sys.exit(cli())
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1126, in __call__
        return self.main(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rich_click/rich_group.py", line 21, in main
        rv = super().main(*args, standalone_mode=False, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1051, in main
        rv = self.invoke(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1654, in invoke
        super().invoke(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1393, in invoke
        return ctx.invoke(self.callback, **ctx.params)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 752, in invoke
        return __callback(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/decorators.py", line 26, in new_func
        return f(get_current_context(), *args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py", line 55, in cli
        ctx.obj["client"] = set_client(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py", line 32, in set_client
        "address": os.environ["ETH_ADDRESS"],
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/os.py", line 679, in __getitem__
        raise KeyError(key) from None
    KeyError: 'ETH_ADDRESS'


## Expired positions

We can use the `--expired` flag in order to filter for the expired positions


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

    {'address': '0x9B8a204636a7aa9c33053d9C3A828720d32212e8'}
    Rysk client initialized and connected to the blockchain at RPC connection https://arbitrum-goerli.rpc.thirdweb.com





    RyskClient(_markets=[], _tickers=[], _otokens={}, web3_client=<rysk_client.web3_client.Web3Client object at 0x7f4e7769eb00>)



## Fetching Markets

The client can fetch markets as so;



```python
markets = client.fetch_markets()
markets[0]
```




    {'id': 'ETH-29SEP23-1800-C',
     'strike': 1800.0,
     'expiration': 1695974400,
     'optionType': 'call',
     'active': True,
     'delta': 0.6261148870195038,
     'bid': 124.475362,
     'ask': 133.443211,
     'dhv': 0.1}




```python

!rysk positions list --expired
```

    [2;36m[08/10/23 16:07:55][0m[2;36m [0m[34mINFO    [0m Rysk client initialized and connected ]8;id=441140;file:///home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/client.py\[2mclient.py[0m]8;;\[2m:[0m]8;id=455202;file:///home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/client.py#110\[2m110[0m]8;;\
    [2;36m                    [0m         to the blockchain at RPC connection   [2m             [0m
    [2;36m                    [0m         [4;94mhttps://arbitrum-goerli.rpc.thirdweb.[0m [2m             [0m
    [2;36m                    [0m         [4;94mcom[0m                                   [2m             [0m
    [2;36m[08/10/23 16:07:56][0m[2;36m [0m[34mINFO    [0m Fetching positions for [3;35mNone[0m              ]8;id=199407;file:///home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py\[2mcli.py[0m]8;;\[2m:[0m]8;id=621441;file:///home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py#144\[2m144[0m]8;;\
    Traceback (most recent call last):
      File "/home/tom/.pyenv/versions/3.9.9/bin/rysk", line 8, in <module>
        sys.exit(cli())
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1126, in __call__
        return self.main(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rich_click/rich_group.py", line 21, in main
        rv = super().main(*args, standalone_mode=False, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1051, in main
        rv = self.invoke(ctx)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1657, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1657, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 1393, in invoke
        return ctx.invoke(self.callback, **ctx.params)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/core.py", line 752, in invoke
        return __callback(*args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/click/decorators.py", line 26, in new_func
        return f(get_current_context(), *args, **kwargs)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/cli.py", line 147, in list_positions
        positions = client.fetch_positions(expired=expired)
      File "/home/tom/.pyenv/versions/3.9.9/lib/python3.9/site-packages/rysk_client/client.py", line 208, in fetch_positions
        raise ValueError("No account address was provided.")
    ValueError: No account address was provided.


## Settling Positions
We are able to settle the positions based on the vault id

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



```python

```

## Dev & Contributing

Dependencies are managed with poetry.

For dev build.

```bash
pip install -U .
```

# Releasing
Git ops is used to enable automated releases via pypi.

```bash
export NEW_VERSION=0.2.11
git checkout -b v$NEW_VERSION &&
    bumpversion  rysk_client/ --new-version $NEW_VERSION && 
git push && git push --tag

```
