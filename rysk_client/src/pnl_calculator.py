"""
PnlCalculator class is used to calculate the PnL of a position.
"""


class Trade:
    """Class to represent a trade."""

    def __init__(
        self,
        quantity=None,
        price=None,
        total_cost=None,
        market=None,
        side=None,
        fee=None,
        trade_id=None,
    ):
        if sum([quantity is None, price is None, total_cost is None]) != 1:
            raise ValueError(
                "2 out of 3 of quantity, price, total_cost must be provided"
            )

        if quantity is not None and price is not None:
            self._total_cost = quantity * price
            self._quantity = quantity
            self._price = price
        elif quantity is not None and total_cost is not None:
            self._price = total_cost / quantity
            self._quantity, self._total_cost = quantity, total_cost

        elif price is not None and total_cost is not None:
            self._quantity = total_cost / price
            self._price, self._total_cost = price, total_cost
        self.market = market
        self.side = side
        self.fee = fee
        self.trade_id = trade_id

    @property
    def quantity(self):
        """Return the quantity of the trade."""
        return self._quantity

    @property
    def price(self):
        """Return the price of the trade."""
        return self._price

    @property
    def total_cost(self):
        """Return the total cost of the trade."""
        return self._total_cost

    def __str__(self) -> str:
        """Format the trade as a string."""
        return f"Trade(quantity={self.quantity}, price={self.price})"

    def __repr__(self) -> str:
        """Format the trade as a string."""
        return str(self)


class PnlCalculator:
    """Class to calculate the PnL of a position."""

    def __init__(self):
        """A PnlCalculator is initialised with no trades."""
        self.current_price = 0
        self.position_size = 0
        self.total_cost = 0
        self.realised_pnl_total = 0
        self.trades = []

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

    def add_trades(self, trades):
        """Add a list of trades to the PnlCalculator."""
        for trade in trades:
            self.add_trade(trade)

    def add_trade(self, trade):
        """
        add a trade to the PnlCalculator.
        positions can be short
        trades can be added in any order

        buy_trade = Trade(1, 1000)
        sell_trade = Trade(-1, 1010)
        pnl_calculator.add_trade(buy_trade)
        pnl_calculator.add_trade(sell_trade)
        assert pnl_calculator.position_size == 0
        assert pnl_calculator.realised_pnl == 10

        """
        self.trades.append(trade)
        # handle open
        if self.position_size == 0:
            self.position_size = trade.quantity
            self.total_cost = trade.total_cost
            return

        # handle partial close
        if self.position_size * trade.quantity < 0:
            # we are closing part of the position
            # we need to calculate the realised pnl
            # and update the position size and total cost
            realised_pnl = -self.position_size * (trade.price - self.average_price)
            self.realised_pnl_total -= realised_pnl
            self.position_size += trade.quantity
            self.total_cost += trade.total_cost
            return

        # handle full close
        if self.position_size + trade.quantity == 0:
            # we are closing the position
            # we need to calculate the realised pnl
            # and update the position size and total cost
            realised_pnl = -self.position_size * (trade.price - self.average_price)
            self.realised_pnl_total -= realised_pnl
            self.position_size = 0
            self.total_cost = 0
            return

        # handle increase position
        if self.position_size * trade.quantity > 0:
            # we are increasing the position
            # we need to update the position size and total cost
            self.position_size += trade.quantity
            self.total_cost += trade.total_cost
            return
