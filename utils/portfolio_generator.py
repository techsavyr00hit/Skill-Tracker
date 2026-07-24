"""
Creates sample csv data files so the program can be run and tested
without needing real brokerage data.
"""

import os
import random
from datetime import date, timedelta

SYMBOLS = ["VTI", "VOO", "VXUS", "BND", "AAPL", "MSFT", "GOOG"]


def generate_sample_data(data_folder, num_lots=12, seed=42):
    """Only creates the files if they do not already exist."""
    os.makedirs(data_folder, exist_ok=True)

    portfolio_path = os.path.join(data_folder, "portfolio.csv")
    prices_path = os.path.join(data_folder, "prices.csv")
    transactions_path = os.path.join(data_folder, "transactions.csv")

    all_exist = (
        os.path.exists(portfolio_path)
        and os.path.exists(prices_path)
        and os.path.exists(transactions_path)
    )
    if all_exist:
        return  # sample data already there, no need to regenerate

    random.seed(seed)
    today = date.today()

    # 1. portfolio.csv: some tax lots for random symbols
    with open(portfolio_path, "w") as file:
        file.write("lot_id,symbol,quantity,purchase_price,purchase_date\n")
        for i in range(1, num_lots + 1):
            symbol = random.choice(SYMBOLS)
            quantity = random.randint(1, 50)
            purchase_price = round(random.uniform(50, 400), 2)
            days_ago = random.randint(10, 800)
            purchase_date = today - timedelta(days=days_ago)
            file.write(f"L{i:03d},{symbol},{quantity},{purchase_price},{purchase_date}\n")

    # 2. prices.csv: one current price per symbol
    with open(prices_path, "w") as file:
        file.write("symbol,price\n")
        for symbol in SYMBOLS:
            price = round(random.uniform(50, 400), 2)
            file.write(f"{symbol},{price}\n")

    # 3. transactions.csv: a small buy/sell history, mostly buys
    with open(transactions_path, "w") as file:
        file.write("date,symbol,action,quantity,price\n")
        for i in range(10):
            symbol = random.choice(SYMBOLS)
            action = random.choice(["BUY", "BUY", "SELL"])
            quantity = random.randint(1, 20)
            price = round(random.uniform(50, 400), 2)
            days_ago = random.randint(0, 60)
            txn_date = today - timedelta(days=days_ago)
            file.write(f"{txn_date},{symbol},{action},{quantity},{price}\n")
