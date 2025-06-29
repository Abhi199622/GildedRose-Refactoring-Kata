
def decrease_quality(quality: int, sell_in: int, decrease_by: int | None=None) -> int:
    """Decrease the quality of an item based on its sell_in value"""
    if not decrease_by:
        if sell_in <= 0:
            decrease_by = 2
        else:
            decrease_by = 1
    return max(0, quality - decrease_by)


def increase_quality(quality: int, increase_by: int = 1) -> int:
    """Increase the quality of an item"""
    return min(50, quality + increase_by)