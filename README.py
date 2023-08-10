#!/usr/bin/env python
# coding: utf-8

# # Rysk Client
# 
# The rysk python client offers a programatic means by which to interact with the (Rysk Finance Protocol)
# 
# ## Installation
# 
# The application is availale on pypi and can be installed as so
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
# pip install -U .
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
