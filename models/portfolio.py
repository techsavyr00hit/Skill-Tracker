"""Portfolio holds all the tax lots owned by the investor."""


class Portfolio:
    def __init__(self):
        # dictionary: symbol -> list of TaxLot objects
        self.lots_by_symbol = {}

    def add_lot(self, lot):
        if lot.symbol not in self.lots_by_symbol:
            self.lots_by_symbol[lot.symbol] = []
        self.lots_by_symbol[lot.symbol].append(lot)

    def remove_lot(self, lot):
        lots = self.lots_by_symbol.get(lot.symbol, [])
        if lot in lots:
            lots.remove(lot)

    def get_lots(self, symbol):
        return self.lots_by_symbol.get(symbol, [])

    def all_symbols(self):
        return list(self.lots_by_symbol.keys())

    def all_lots(self):
        """Return every tax lot in the whole portfolio as one flat list."""
        every_lot = []
        for symbol in self.lots_by_symbol:
            every_lot.extend(self.lots_by_symbol[symbol])
        return every_lot

    def total_cost_basis(self):
        total = 0.0
        for lot in self.all_lots():
            total += lot.cost_basis()
        return total

    def total_market_value(self, prices):
        total = 0.0
        for lot in self.all_lots():
            price = prices.get(lot.symbol, lot.purchase_price)
            total += lot.market_value(price)
        return total
