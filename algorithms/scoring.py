"""
Scoring functions used to rank tax loss harvesting opportunities.
A higher score means "harvest this one first".
"""

SHORT_TERM_TAX_RATE = 0.35  # simplified assumption
LONG_TERM_TAX_RATE = 0.15   # simplified assumption


def estimate_tax_savings(lot, gain_loss, as_of_date):
    """
    Estimate how much tax the investor saves by harvesting this loss.
    Short term losses are taxed (and saved) at a higher rate.
    """
    loss_amount = abs(gain_loss)
    if lot.is_long_term(as_of_date):
        rate = LONG_TERM_TAX_RATE
    else:
        rate = SHORT_TERM_TAX_RATE
    return loss_amount * rate


def score_opportunity(lot, gain_loss, as_of_date):
    """The score is simply the estimated tax savings in dollars."""
    return estimate_tax_savings(lot, gain_loss, as_of_date)


def rank_opportunities(losing_lots, as_of_date):
    """
    losing_lots: list of (lot, gain_loss)
    Returns a new list sorted from best opportunity to worst.
    Each item becomes (lot, gain_loss, score).
    """
    scored = []
    for lot, gain_loss in losing_lots:
        score = score_opportunity(lot, gain_loss, as_of_date)
        scored.append((lot, gain_loss, score))

    scored.sort(key=lambda item: item[2], reverse=True)
    return scored
