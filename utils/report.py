"""Prints a readable report of the harvesting recommendations."""


def print_report(recommendations, portfolio, prices):
    print("=" * 60)
    print("DYNAMIC TAX LOSS HARVESTING REPORT")
    print("=" * 60)

    print(f"\nTotal cost basis of portfolio: {portfolio.total_cost_basis():.2f}")
    print(f"Total market value of portfolio: {portfolio.total_market_value(prices):.2f}")

    if not recommendations:
        print("\nNo tax loss harvesting opportunities found today.")
        return

    print(f"\nFound {len(recommendations)} harvesting opportunity(ies):\n")

    total_tax_savings = 0.0
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. Symbol: {rec.lot.symbol}  (lot id {rec.lot.lot_id})")
        print(f"   Quantity: {rec.lot.quantity}")
        print(f"   Unrealized loss: {rec.gain_loss:.2f}")
        print(f"   Estimated tax savings: {rec.tax_savings:.2f}")
        if rec.replacement_symbol:
            print(f"   Suggested replacement buy: {rec.replacement_symbol}")
        else:
            print("   Suggested replacement buy: none found")
        print("-" * 40)
        total_tax_savings += rec.tax_savings

    print(f"\nTotal estimated tax savings if all are harvested: {total_tax_savings:.2f}")
