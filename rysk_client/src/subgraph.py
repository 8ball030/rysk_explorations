"""
Module to interact with the Rysk subgraph.
"""
import json
from dataclasses import dataclass
from typing import Any, Dict, List

import requests

from rysk_client.src.constants import DEFAULT_TIMEOUT

MARKET_SUBGRAPH_QUERY = """
{series (
  where: {
    or:[
    {
            isBuyable: true
        },
        {
            isSellable: true
        }
    ]
  }
)
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
            amount
            transactionHash
        }
        optionsBoughtTransactions {
            amount
            premium
            transactionHash
        }
        optionsSoldTransactions {
            amount
            premium
            transactionHash
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
            payoutAmount
            transactionHash
        }
        optionsBoughtTransactions {
            amount
            premium
            transactionHash
        }
        optionsSoldTransactions {
            amount
            premium
            transactionHash
        }
  }
}
"""


INDEX_QUERY = """
{
  stat(id: 0 block: {number: %s}) {
    id
  }
}
"""


class BlockNotIndexed(Exception):
    """Block not indexed."""


@dataclass
class SubgraphClient:
    """Simple client to interact with the Rysk subgraph."""

    url: str

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
        if response.status_code != 200 or response.content == b"404":
            raise ValueError(
                f"Subgraph query failed with status code {response.status_code}."
            )
        return json.loads(response.content)["data"]

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

    def query_index(self, block: int) -> Dict[str, Any]:
        """Query the subgraph for index."""
        query = INDEX_QUERY % block
        try:
            result = self._query(query)
            return result["stat"]
        except KeyError as err:
            raise BlockNotIndexed(f"Block {block} not indexed.") from err
