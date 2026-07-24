"""
Dynamic Tax Loss Harvesting Engine
Main entry point of the program.
"""

from datetime import date

from utils.csv_loader import load_portfolio, load_prices, load_transactions
from utils.portfolio_generator import generate_sample_data
from models.portfolio import Portfolio
from engine.portfolio_analyzer import PortfolioAnalyzer
from engine.tax_loss_harvester import TaxLossHarvester
from utils.report import print_report

DATA_FOLDER = "data"


def build_portfolio(lots):
    """Put all tax lots into one Portfolio object."""
    portfolio = Portfolio()
    for lot in lots:
        portfolio.add_lot(lot)
    return portfolio


def main():
    # Step 1: make sure we have some sample data to work with
    generate_sample_data(DATA_FOLDER)

    # Step 2: load data from the csv files
    lots = load_portfolio(DATA_FOLDER + "/portfolio.csv")
    prices = load_prices(DATA_FOLDER + "/prices.csv")
    transactions = load_transactions(DATA_FOLDER + "/transactions.csv")

    # Step 3: build the portfolio object out of the tax lots
    portfolio = build_portfolio(lots)

    # Step 4: analyze the portfolio (find gains and losses)
    analyzer = PortfolioAnalyzer(portfolio, prices)
    analyzer.analyze(date.today())

    # Step 5: run the tax loss harvesting engine
    harvester = TaxLossHarvester(portfolio, prices, transactions, min_loss_threshold=50.0)
    recommendations = harvester.find_harvesting_opportunities(date.today())

    # Step 6: show the final report
    print_report(recommendations, portfolio, prices)


if __name__ == "__main__":
    main()
