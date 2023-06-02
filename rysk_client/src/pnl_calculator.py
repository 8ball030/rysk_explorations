"""
PnlCalculator class is used to calculate the PnL of a position.
"""


class Trade:
    """Clas to represent a trade."""

    def __init__(self, quantity, price):
        """initialise a trade with a quantity and price."""
        self.quantity = quantity
        self.price = price


class PnlCalculator:
    """Class to calculate the PnL of a position."""

    def __init__(self):
        """A PnlCalculator is initialised with no trades."""
        self.current_price = 0
        self.position_size = 0
        self.total_cost = 0
        self.realised_pnl_total = 0

    def add_trade(self, trade):
        """Add a trade to the PnlCalculator."""
        if (self.position_size * trade.quantity) < 0:  # Reducing position
            realised_quantity = min(abs(self.position_size), abs(trade.quantity))
            self.realised_pnl_total += (
                realised_quantity
                * (self.average_price - trade.price)
                * (-1 if trade.quantity < 0 else 1)
            )
            self.position_size += trade.quantity
            self.total_cost = self.average_price * self.position_size
        else:  # Increasing position
            self.position_size += trade.quantity
            self.total_cost += trade.quantity * trade.price
        # If the position size is 0 (i.e., all trades are closed), reset the total cost
        if self.position_size == 0:
            self.total_cost = 0

    def update_price(self, price):
        """Update the current price of the PnlCalculator."""
        self.current_price = price

    @property
    def average_price(self):
        """Calculate the average price of the open position."""
        if self.position_size == 0:
            return 0
        return self.total_cost / self.position_size

    @property
    def unrealised_pnl(self):
        """Calculate the unrealised PnL of the PnlCalculator."""
        return self.position_size * (self.current_price - self.average_price)

    @property
    def realised_pnl(self):
        """Return the realised PnL of the PnlCalculator."""
        return self.realised_pnl_total
