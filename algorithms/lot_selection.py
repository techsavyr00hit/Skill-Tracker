"""
Algorithms for choosing WHICH tax lots to sell when harvesting losses.
Different methods give different tax results.
"""


def select_fifo(lots):
    """First In, First Out: sell the oldest lots first."""
    return sorted(lots, key=lambda lot: lot.purchase_date)


def select_lifo(lots):
    """Last In, First Out: sell the newest lots first."""
    return sorted(lots, key=lambda lot: lot.purchase_date, reverse=True)


def select_hifo(lots):
    """Highest In, First Out: sell the most expensive lots first.
    This usually creates the biggest loss (or smallest gain)."""
    return sorted(lots, key=lambda lot: lot.purchase_price, reverse=True)


def select_lots_for_target_loss(lots, current_price, target_loss_amount):
    """
    Pick lots (highest cost basis first) until we reach the target loss
    amount, or until we run out of lots that are actually losing money.
    """
    ordered_lots = select_hifo(lots)
    selected = []
    accumulated_loss = 0.0

    for lot in ordered_lots:
        gain_loss = lot.unrealized_gain_loss(current_price)
        if gain_loss >= 0:
            continue  # skip lots that are not losing money

        selected.append(lot)
        accumulated_loss += abs(gain_loss)

        if accumulated_loss >= target_loss_amount:
            break

    return selected, accumulated_loss
