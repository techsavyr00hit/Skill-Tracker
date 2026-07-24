"""
Looks at the whole portfolio and figures out which lots
are winners (gain) and which are losers (loss).
"""


class PortfolioAnalyzer:
    def __init__(self, portfolio, prices):
        self.portfolio = portfolio
        self.prices = prices
        self.results = []  # list of (lot, gain_loss)

    def analyze(self, as_of_date):
        """Calculate gain/loss for every lot in the portfolio."""
        self.results = []
        for lot in self.portfolio.all_lots():
            price = self.prices.get(lot.symbol, lot.purchase_price)
            gain_loss = lot.unrealized_gain_loss(price)
            self.results.append((lot, gain_loss))
        return self.results

    def get_losing_lots(self, min_loss_threshold=0.0):
        """Return lots that are currently losing more than the threshold amount."""
        losers = []
        for lot, gain_loss in self.results:
            if gain_loss < 0 and abs(gain_loss) >= min_loss_threshold:
                losers.append((lot, gain_loss))
        return losers

    def get_winning_lots(self):
        winners = []
        for lot, gain_loss in self.results:
            if gain_loss > 0:
                winners.append((lot, gain_loss))
        return winners

    def total_unrealized_gain_loss(self):
        total = 0.0
        for lot, gain_loss in self.results:
            total += gain_loss
        return total
