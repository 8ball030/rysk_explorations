"""
Module to interact with the Rysk subgraph.
"""
import json
from dataclasses import dataclass
from typing import Any, Dict, List

import requests

from rysk_client.src.constants import DEFAULT_TIMEOUT, SUBGRAPH_URL

MARKET_SUBGRAPH_QUERY = """
{series 
  {   
    id 
    expiration 
    netDHVExposure 
    strike
    isPut
    isBuyable
    isSellable
  }
}
"""

SHORT_SUBGRAPH_QUERY = """
{
  shortPositions(
    first: 1000,
    where: {
         account: "%s",
         oToken_: {expiryTimestamp_gte: "1683273600"}
         }
    ){
        id
        netAmount
        buyAmount
        sellAmount
        active
        realizedPnl
        oToken {
            id
            symbol
            expiryTimestamp
            strikePrice
            isPut
            underlyingAsset {
                id
            }
            createdAt
        }
        settleActions {
            id
        }
        optionsBoughtTransactions {
            amount
            premium
        }
        optionsSoldTransactions {
            amount
            premium
        }
  }
}
"""

LONG_SUBGRAPH_QUERY = """
{
  longPositions(
    first: 1000,
    where: {
         account: "%s",
         oToken_: {expiryTimestamp_gte: "1683273600"}
         }
    ){
        id
        netAmount
        buyAmount
        sellAmount
        active
        realizedPnl
        oToken {
            id
            symbol
            expiryTimestamp
            strikePrice
            isPut
            underlyingAsset {
                id
            }
            createdAt
        }
        redeemActions {
            id
        }
        optionsBoughtTransactions {
            amount
            premium
        }
        optionsSoldTransactions {
            amount
            premium
        }
  }
}
"""


@dataclass
class SubgraphClient:
    """Simple client to interact with the Rysk subgraph."""

    url: str = SUBGRAPH_URL

    def _query(self, query):
        """Simple function to call a subgraph query."""
        headers = {"Content-Type": "application/json"}
        subgraph_query = {"query": query}
        response = requests.post(
            url=self.url,
            headers=headers,
            data=json.dumps(subgraph_query),
            timeout=DEFAULT_TIMEOUT,
        )
        data = json.loads(response.content)["data"]
        return data

    def query_markets(self):
        """Query the subgraph for markets."""
        return self._query(MARKET_SUBGRAPH_QUERY)["series"]

    def query_longs(self, address: str) -> List[Dict[str, Any]]:
        """Query the subgraph for longs."""
        query = LONG_SUBGRAPH_QUERY % address.lower()
        result = self._query(query)
        return result["longPositions"]

    def query_shorts(self, address: str) -> List[Dict[str, Any]]:
        """Query the subgraph for shorts."""
        query = SHORT_SUBGRAPH_QUERY % address.lower()
        result = self._query(query)
        return result["shortPositions"]
