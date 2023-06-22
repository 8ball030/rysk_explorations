"""
This module contains the Order class, which is used to represent an order.
"""
from dataclasses import dataclass

from rysk_client.src.order_side import OrderSide


@dataclass
class Order:
    """Class to represent an order"""

    price: float
    amount: float
    order_id: str
    order_side: OrderSide
    order_type: str = "market"

    def __str__(self) -> str:
        return f"Order({self.order_side}, {self.amount}, {self.price})"

    def __repr__(self) -> str:
        return self.__str__()
