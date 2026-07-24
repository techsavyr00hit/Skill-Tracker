"""Functions for reading the csv files into our model objects."""

import csv

from models.tax_lot import TaxLot
from models.transaction import Transaction


def load_portfolio(path):
    """
    Reads portfolio.csv with columns:
    lot_id, symbol, quantity, purchase_price, purchase_date
    """
    lots = []
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lot = TaxLot(
                lot_id=row["lot_id"],
                symbol=row["symbol"],
                quantity=row["quantity"],
                purchase_price=row["purchase_price"],
                purchase_date=row["purchase_date"],
            )
            lots.append(lot)
    return lots


def load_prices(path):
    """
    Reads prices.csv with columns: symbol, price
    Returns a dictionary: {symbol: price}
    """
    prices = {}
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            prices[row["symbol"]] = float(row["price"])
    return prices


def load_transactions(path):
    """
    Reads transactions.csv with columns:
    date, symbol, action, quantity, price
    """
    transactions = []
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            txn = Transaction(
                txn_date=row["date"],
                symbol=row["symbol"],
                action=row["action"],
                quantity=row["quantity"],
                price=row["price"],
            )
            transactions.append(txn)
    return transactions
