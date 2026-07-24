"""
Simple tests for the engine. These use plain assert statements
instead of a testing framework, to keep things easy to read.
"""

import sys
import os
from datetime import date, timedelta

# make sure we can import from the project folders
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.tax_lot import TaxLot
from models.transaction import Transaction
from models.portfolio import Portfolio
from engine.wash_sale import WashSaleChecker
from engine.portfolio_analyzer import PortfolioAnalyzer
from algorithms.lot_selection import select_fifo, select_lifo, select_hifo
from algorithms.scoring import score_opportunity


def test_gain_loss_calculation():
    lot = TaxLot("L1", "AAPL", 10, 100.0, date(2024, 1, 1))
    gain_loss = lot.unrealized_gain_loss(90.0)
    assert gain_loss == -100.0, "Should show a 100 dollar loss"
    print("test_gain_loss_calculation passed")


def test_long_term_flag():
    old_lot = TaxLot("L2", "AAPL", 1, 100.0, date.today() - timedelta(days=400))
    new_lot = TaxLot("L3", "AAPL", 1, 100.0, date.today() - timedelta(days=10))
    assert old_lot.is_long_term(date.today()) is True
    assert new_lot.is_long_term(date.today()) is False
    print("test_long_term_flag passed")


def test_wash_sale_detected():
    sell_date = date.today()
    buy_date = sell_date - timedelta(days=5)
    transactions = [Transaction(buy_date, "AAPL", "BUY", 10, 120.0)]
    checker = WashSaleChecker(transactions)
    assert checker.would_violate_wash_sale("AAPL", sell_date) is True
    print("test_wash_sale_detected passed")


def test_wash_sale_not_triggered():
    sell_date = date.today()
    buy_date = sell_date - timedelta(days=60)
    transactions = [Transaction(buy_date, "AAPL", "BUY", 10, 120.0)]
    checker = WashSaleChecker(transactions)
    assert checker.would_violate_wash_sale("AAPL", sell_date) is False
    print("test_wash_sale_not_triggered passed")


def test_lot_selection_order():
    lot_old = TaxLot("L1", "AAPL", 5, 100.0, date(2023, 1, 1))
    lot_new = TaxLot("L2", "AAPL", 5, 200.0, date(2024, 1, 1))
    lots = [lot_new, lot_old]

    fifo_result = select_fifo(lots)
    assert fifo_result[0] == lot_old, "FIFO should return the oldest lot first"

    lifo_result = select_lifo(lots)
    assert lifo_result[0] == lot_new, "LIFO should return the newest lot first"

    hifo_result = select_hifo(lots)
    assert hifo_result[0] == lot_new, "HIFO should return the highest cost lot first"

    print("test_lot_selection_order passed")


def test_portfolio_analyzer():
    portfolio = Portfolio()
    lot = TaxLot("L1", "AAPL", 10, 100.0, date(2024, 1, 1))
    portfolio.add_lot(lot)

    prices = {"AAPL": 80.0}
    analyzer = PortfolioAnalyzer(portfolio, prices)
    analyzer.analyze(date.today())

    losers = analyzer.get_losing_lots(min_loss_threshold=50)
    assert len(losers) == 1, "Should find exactly one losing lot"
    print("test_portfolio_analyzer passed")


def test_scoring_short_vs_long_term():
    short_term_lot = TaxLot("L1", "AAPL", 1, 100.0, date.today() - timedelta(days=10))
    long_term_lot = TaxLot("L2", "AAPL", 1, 100.0, date.today() - timedelta(days=400))

    short_score = score_opportunity(short_term_lot, -100.0, date.today())
    long_score = score_opportunity(long_term_lot, -100.0, date.today())

    assert short_score > long_score, "Short term losses should have a higher tax savings rate"
    print("test_scoring_short_vs_long_term passed")


def run_all_tests():
    test_gain_loss_calculation()
    test_long_term_flag()
    test_wash_sale_detected()
    test_wash_sale_not_triggered()
    test_lot_selection_order()
    test_portfolio_analyzer()
    test_scoring_short_vs_long_term()
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_all_tests()
