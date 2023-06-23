#!/usr/bin/env python
# coding: utf-8

# # Rysk Client
# 
# ## Installation
# 
# The application is availale on pypi and can be installed as so;
# 
#     ```bash
#     pip install rysk-client
#     ```
# 
# ### Dev & Contributing
# 
# Dependencies are managed with poetry.
# 
# For dev build.

# In[1]:


get_ipython().system('pip install -U .')


# In[ ]:





# In[ ]:





# ## Cli Tool
# 
# The application is also bundled as cli tool to allow users to interact with the protocol from the cli.
# 

# In[2]:


get_ipython().system(' rysk')


# ### Markets
# We can fetch data about the markets as so;

# In[3]:


get_ipython().system(' rysk markets fetch')


# # Positions
# 
# We can view the current positions, along with those which are expired.

# In[4]:


get_ipython().system(' export ETH_ADDRESS=0x9B8a204636a7aa9c33053d9C3A828720d32212e8 &&    export ETH_PRIVATE_KEY=0x75cc9212e9e1243b9a3e5db5012f39469254088e33363324ad94dd0b212d7efa &&      rysk positions list')


# In[5]:


get_ipython().system(' export ETH_ADDRESS=0x9B8a204636a7aa9c33053d9C3A828720d32212e8 &&    export ETH_PRIVATE_KEY=0x75cc9212e9e1243b9a3e5db5012f39469254088e33363324ad94dd0b212d7efa &&      rysk positions list --expired')


# In[ ]:





# ## Creating a Client 
# 
# Clients can be created from the rysk client module.

# In[6]:


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

# In[7]:


markets = client.fetch_markets()
markets[0]


# ## Fetching Tickers
# 
# Tickers can be fetched from the client as so;

# In[8]:


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

# In[9]:


positions = client.fetch_positions()
positions[0]


# # Tests

# In[10]:


get_ipython().system('make test')


# In[11]:


get_ipython().system('make fmt lint')

