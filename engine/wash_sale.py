"""
IRS Wash Sale Rule:
If you sell a security at a loss, and buy the SAME (or a "substantially
identical") security within 30 days BEFORE or AFTER the sale, the loss
is disallowed for tax purposes.

This module checks that rule using the transaction history.
"""

from datetime import timedelta

WASH_SALE_WINDOW_DAYS = 30


class WashSaleChecker:
    def __init__(self, transactions):
        self.transactions = transactions

    def would_violate_wash_sale(self, symbol, sell_date):
        """
        Check if selling `symbol` on `sell_date` would trigger a wash sale,
        based on buy transactions within the 30-day window before or after.
        """
        window_start = sell_date - timedelta(days=WASH_SALE_WINDOW_DAYS)
        window_end = sell_date + timedelta(days=WASH_SALE_WINDOW_DAYS)

        for txn in self.transactions:
            if txn.symbol != symbol:
                continue
            if txn.action != "BUY":
                continue
            if window_start <= txn.date <= window_end and txn.date != sell_date:
                return True
        return False

    def find_violations(self, candidate_sells):
        """
        Given a list of (symbol, sell_date) pairs, return the ones that
        would violate the wash sale rule.
        """
        violations = []
        for symbol, sell_date in candidate_sells:
            if self.would_violate_wash_sale(symbol, sell_date):
                violations.append((symbol, sell_date))
        return violations
