"""
Module to test the deribit exchange
"""
import os
from pprint import pprint

from ccxt import deribit

secret = {
    "apiKey": os.environ.get("API_KEY"),
    "secret": os.environ.get("SECRET"),
}

exchange = deribit(secret)


markets = exchange.fetchMarkets()
market = markets[100]
pprint(market)

# we now print the ticker for the market

ticker = exchange.fetchTicker(market["id"])
pprint(ticker)


# we get the ticket
