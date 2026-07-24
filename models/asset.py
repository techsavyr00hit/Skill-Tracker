"""A simple Asset class. Represents one stock/ETF/fund that can be held."""


class Asset:
    def __init__(self, symbol, name="", asset_class="stock"):
        self.symbol = symbol
        self.name = name
        self.asset_class = asset_class

    def __repr__(self):
        return f"Asset({self.symbol}, {self.asset_class})"
