"""
Module to interact with the Rysk subgraph.
"""
import json
from dataclasses import dataclass

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
