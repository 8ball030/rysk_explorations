#!/usr/bin/env python
# coding: utf-8

# # Rysk Client
# 
# The rysk python client offers a programatic means by which to interact with the (Rysk Finance Protocol).
# 
# The DHV is a hybrid AMM and RFQ options protocol, generating uncorrelated returns for its liquidity providers whilst enabling anyone to trade (buy and sell) options with a wide range of strike prices and expiry dates. The DHV uses a dynamic approach in hedging risk to generate market-neutral uncorrelated returns for liquidity providers.
# 
# The Rysk client is a python client that allows users to interact with the [Rysk protocol](https://app.rysk.finance). The client is built on top of the web3.py and the [Open-Aea](https://github.com/valory-xyz/open-aea) python libraries. The client allows users to interact with the Rysk protocol in a programatic manner.
# 
# 
# 
# ## Installation
# 
# The application is available on pypi and can be installed as so
# 
# ```bash
# pip install rysk-client
# ```

# ## Cli Tool
# 
# The application is also bundled as cli tool to allow users to interact with the protocol from the cli.
# 

# 
# 
# ![alt text](demo.gif "Title")
# 

# ## Creating a Client 
# 
# Clients can be created from the rysk client module using python code.

# In[1]:


from rysk_client.client import RyskClient
from tests.conftest import DEFAULT_ADDRESS

auth = {
    "address": DEFAULT_ADDRESS,
}

client = RyskClient(**auth)
client


# ### Markets
# We can fetch data about the markets as so;

# In[2]:


markets = client.fetch_markets()
markets[0]


# ## Fetching Tickers
# 
# Tickers can be fetched from the client as so;

# In[3]:


tickers = client.fetch_tickers()
tickers[0]


# ## Fetching Positions
# Positions are fetched from the client such that a user can retrieve their positions.
# 
# Positions are indicated by a vault id.
# 
# The vaultid iterates when a new position is created. 
# 
# Vaultid can be retrieved from;
# 
# 
# 
# 

# In[4]:


positions = client.fetch_positions()
positions[0]


# ## Dev & Contributing
# 
# Dependencies are managed with poetry.
# 
# For dev build.
# 
# ```bash
# poetry install 
# poetry shell 
# ```

# # Tests

# In[5]:


get_ipython().system('poetry run pytest tests')


# ## Formating and linting

# In[6]:


get_ipython().system('make fmt lint')


# # Releasing
# Git ops is used to enable automated releases via pypi.
# 
# ```bash
# export NEW_VERSION=0.2.11
# git checkout -b v$NEW_VERSION &&
#     bumpversion  rysk_client/ --new-version $NEW_VERSION && 
# git push --set-upstream origin (git rev-parse --abbrev-ref HEAD) && git push --tag
# 
# ```
