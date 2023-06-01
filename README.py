#!/usr/bin/env python
# coding: utf-8

# # Rysk Client
# 
# ## Installation
# 
# ### Dev
# 
# dependencies are managed with poetry. 
# 
# For dev build.

# In[1]:


get_ipython().system('pip install rysk-client')


# # Usage
# 

# In[2]:


from rysk_client.src.utils import get_web3

web3 = get_web3()
web3.isConnected()


# ## Creating a Client 
# 
# Clients can be created from the rysk client module.

# In[3]:


from rysk_client.client import RyskClient

client = RyskClient()
client


# ## Fetching Markets
# 
# The client can fetch markets as so;
# 

# In[4]:


markets = client.fetch_markets()
markets[0]


# ## Fetching Tickers
# 
# Tickers can be fetched from the client as so;

# In[5]:


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
# #TODO
# 
# 
# 

# In[6]:


positions = client.fetch_positions()
positions


# # Tests

# In[7]:


get_ipython().system('make test')


# In[8]:


get_ipython().system('make fmt lint')

