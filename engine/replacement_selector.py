"""
When we harvest a loss, we usually want to buy a similar (but not
"substantially identical") asset so the portfolio stays balanced,
without breaking the wash sale rule.

This is a simplified version that uses a lookup table of similar assets.
"""

# A simple map of symbol -> list of similar replacement symbols.
# In a real system this would come from a database of asset correlations.
DEFAULT_REPLACEMENT_MAP = {
    "VTI": ["ITOT", "SCHB"],
    "ITOT": ["VTI", "SCHB"],
    "SCHB": ["VTI", "ITOT"],
    "VOO": ["IVV", "SPLG"],
    "IVV": ["VOO", "SPLG"],
    "SPLG": ["VOO", "IVV"],
    "VXUS": ["IXUS", "SCHF"],
    "IXUS": ["VXUS", "SCHF"],
    "SCHF": ["VXUS", "IXUS"],
    "BND": ["AGG", "SCHZ"],
    "AGG": ["BND", "SCHZ"],
    "SCHZ": ["BND", "AGG"],
}


class ReplacementSelector:
    def __init__(self, replacement_map=None):
        self.replacement_map = replacement_map or DEFAULT_REPLACEMENT_MAP

    def select_replacement(self, symbol):
        """Return the best replacement symbol, or None if we don't know one."""
        options = self.replacement_map.get(symbol, [])
        if not options:
            return None
        return options[0]

    def all_options(self, symbol):
        return self.replacement_map.get(symbol, [])
