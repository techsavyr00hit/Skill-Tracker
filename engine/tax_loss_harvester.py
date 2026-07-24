"""
The main engine. It ties everything together:
1. Find lots that are losing money.
2. Make sure selling them will not violate the wash sale rule.
3. Score and rank the opportunities.
4. Suggest a replacement asset to buy.
"""

from engine.portfolio_analyzer import PortfolioAnalyzer
from engine.wash_sale import WashSaleChecker
from engine.replacement_selector import ReplacementSelector
from algorithms.scoring import rank_opportunities


class HarvestRecommendation:
    """A simple container that holds one harvesting suggestion."""

    def __init__(self, lot, gain_loss, tax_savings, replacement_symbol):
        self.lot = lot
        self.gain_loss = gain_loss
        self.tax_savings = tax_savings
        self.replacement_symbol = replacement_symbol

    def __repr__(self):
        return (
            f"Sell {self.lot.symbol} lot {self.lot.lot_id} "
            f"(loss {self.gain_loss:.2f}) -> buy {self.replacement_symbol}"
        )


class TaxLossHarvester:
    def __init__(self, portfolio, prices, transactions, min_loss_threshold=0.0):
        self.portfolio = portfolio
        self.prices = prices
        self.transactions = transactions
        self.min_loss_threshold = min_loss_threshold

        self.analyzer = PortfolioAnalyzer(portfolio, prices)
        self.wash_sale_checker = WashSaleChecker(transactions)
        self.replacement_selector = ReplacementSelector()

    def find_harvesting_opportunities(self, as_of_date):
        # step 1: figure out gains/losses for every lot
        self.analyzer.analyze(as_of_date)
        losing_lots = self.analyzer.get_losing_lots(self.min_loss_threshold)

        # step 2: remove any lot that would trigger a wash sale if sold today
        eligible_lots = []
        for lot, gain_loss in losing_lots:
            violates = self.wash_sale_checker.would_violate_wash_sale(lot.symbol, as_of_date)
            if not violates:
                eligible_lots.append((lot, gain_loss))

        # step 3: rank the remaining opportunities by estimated tax savings
        ranked = rank_opportunities(eligible_lots, as_of_date)

        # step 4: build the final recommendations with a suggested replacement
        recommendations = []
        for lot, gain_loss, score in ranked:
            replacement = self.replacement_selector.select_replacement(lot.symbol)
            recommendation = HarvestRecommendation(lot, gain_loss, score, replacement)
            recommendations.append(recommendation)

        return recommendations
