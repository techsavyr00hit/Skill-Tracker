# Dynamic Tax Loss Harvesting Engine

This is a small Python project that pretends to be a simplified version of
the kind of tool robo-advisors (like Wealthfront or Betterment) use to save
their users money on taxes. It's built for learning, so the code is kept
simple on purpose.

## What is "tax loss harvesting"?

When you own stocks or ETFs, some of them go up in value and some go down.
If you sell one that has gone down, you get to record a "loss," which you
can use to lower the taxes you owe. Smart investors sell their losers on
purpose, just to get this tax benefit, and then buy something similar so
their portfolio doesn't really change.

There's one catch: the **wash sale rule**. If you sell something at a loss
and then buy the same (or a very similar) thing back within 30 days, the
IRS won't let you count that loss. So this project has to check for that
before recommending anything.

## What this program actually does

1. Reads your fake portfolio, current prices, and past buy/sell history from
   CSV files.
2. Goes through every stock you own and figures out which ones are currently
   worth less than what you paid for them.
3. Checks whether selling any of those losers right now would break the
   wash sale rule.
4. Ranks the remaining opportunities by how much tax money you'd actually
   save.
5. Suggests a similar replacement stock/ETF to buy instead, so you stay
   invested.
6. Prints a report showing everything it found.

## Project layout

```
dynamic-tax-loss-harvesting-engine/
│
├── main.py                     <- run this file to start the program
│
├── data/                        <- csv files with sample portfolio data
│   ├── portfolio.csv
│   ├── prices.csv
│   └── transactions.csv
│
├── models/                      <- basic data classes (no logic, just data)
│   ├── asset.py
│   ├── tax_lot.py
│   ├── portfolio.py
│   └── transaction.py
│
├── engine/                       <- the main logic lives here
│   ├── tax_loss_harvester.py    <- ties everything together
│   ├── wash_sale.py             <- checks the 30-day rule
│   ├── replacement_selector.py  <- picks a similar stock to buy back
│   └── portfolio_analyzer.py    <- finds your gains and losses
│
├── algorithms/                  <- smaller helper algorithms
│   ├── lot_selection.py         <- FIFO / LIFO / HIFO selling order
│   └── scoring.py                <- ranks opportunities by tax savings
│
├── utils/                        <- helper/support code
│   ├── csv_loader.py             <- reads the csv files
│   ├── report.py                 <- prints the final report
│   └── portfolio_generator.py    <- makes fake sample data if none exists
│
└── tests/
    └── test_engine.py            <- simple tests using plain assert statements
```

## How to run it

You just need Python 3 installed (no extra libraries required).

```bash
cd dynamic-tax-loss-harvesting-engine
python3 main.py
```

The first time you run it, it will notice there's no data yet and generate
some random sample data for you automatically. After that, it will use
whatever is already in the `data/` folder.

## How to run the tests

```bash
python3 tests/test_engine.py
```

If everything is working, you'll see a list of "passed" messages and a
final "All tests passed!" line.

## A few simplifications (so you know what's "fake" here)

- Tax rates are just made-up flat numbers (35% for short-term, 15% for
  long-term), not real tax brackets.
- The list of "similar" replacement stocks is a small hardcoded lookup
  table, not real financial data.
- Sample data is randomly generated, so numbers will look different every
  time you delete the `data/` folder and re-run the program.

This project is meant to show how the *pieces* of a tax loss harvesting
system fit together (loading data, analyzing gains/losses, checking rules,
scoring, and recommending), not to give real financial advice.
