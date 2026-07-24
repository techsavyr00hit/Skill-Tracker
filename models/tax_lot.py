"""
A Tax Lot is a single purchase of an asset.
Example: buying 10 shares of AAPL on a certain date at a certain price.
"""

from datetime import datetime

LONG_TERM_DAYS = 365


class TaxLot:
    def __init__(self, lot_id, symbol, quantity, purchase_price, purchase_date):
        self.lot_id = lot_id
        self.symbol = symbol
        self.quantity = float(quantity)
        self.purchase_price = float(purchase_price)

        # allow purchase_date to be given as a string or as a date object
        if isinstance(purchase_date, str):
            self.purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d").date()
        else:
            self.purchase_date = purchase_date

    def cost_basis(self):
        """Total amount originally paid for this lot."""
        return self.quantity * self.purchase_price

    def market_value(self, current_price):
        """What this lot is worth today."""
        return self.quantity * current_price

    def unrealized_gain_loss(self, current_price):
        """Positive number = gain, negative number = loss."""
        return self.market_value(current_price) - self.cost_basis()

    def holding_period_days(self, as_of_date):
        return (as_of_date - self.purchase_date).days

    def is_long_term(self, as_of_date):
        return self.holding_period_days(as_of_date) >= LONG_TERM_DAYS

    def __repr__(self):
        return f"TaxLot({self.lot_id}, {self.symbol}, qty={self.quantity})"
