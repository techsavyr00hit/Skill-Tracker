"""A Transaction records a buy or sell event. Used to detect wash sales."""

from datetime import datetime

BUY = "BUY"
SELL = "SELL"


class Transaction:
    def __init__(self, txn_date, symbol, action, quantity, price):
        if isinstance(txn_date, str):
            self.date = datetime.strptime(txn_date, "%Y-%m-%d").date()
        else:
            self.date = txn_date

        self.symbol = symbol
        self.action = action.upper()
        self.quantity = float(quantity)
        self.price = float(price)

    def __repr__(self):
        return f"Transaction({self.date}, {self.action}, {self.symbol}, {self.quantity})"
