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
# 

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
# Clients can be created from the rysk client module.

# In[1]:





# ### Markets
# We can fetch data about the markets as so;

# In[1]:


get_ipython().system(' rysk markets fetch')


# In[ ]:





# # Positions
# 
# We can view the current positions, along with those which are expired.

# In[2]:


get_ipython().system('rysk positions list')


# ## Expired positions
# 
# We can use the `--expired` flag in order to filter for the expired positions

# In[3]:


from rysk_client.client import RyskClient
from tests.conftest import DEFAULT_ADDRESS

auth = {
    "address": DEFAULT_ADDRESS,
}

print(auth)

client = RyskClient(**auth)
client


# ## Fetching Markets
# 
# The client can fetch markets as so;
# 

# In[4]:


markets = client.fetch_markets()
markets[0]


# In[5]:


get_ipython().system('rysk positions list --expired')


# ## Settling Positions
# We are able to settle the positions based on the vault id

# ## Fetching Tickers
# 
# Tickers can be fetched from the client as so;

# In[6]:


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

# In[7]:


positions = client.fetch_positions()
positions[0]


# # Tests

# In[8]:


get_ipython().system('make test')


# In[9]:


get_ipython().system('make fmt lint')


# In[ ]:





# ## Dev & Contributing
# 
# Dependencies are managed with poetry.
# 
# For dev build.
# 
# ```bash
# pip install -U .
# ```

# # Releasing
# Git ops is used to enable automated releases via pypi.
# 
# ```bash
# export NEW_VERSION=0.2.11
# git checkout -b v$NEW_VERSION &&
#     bumpversion  rysk_client/ --new-version $NEW_VERSION && 
# git push && git push --tag
# 
# ```
