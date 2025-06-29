# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                if item.sell_in <= 0:
                    increase_quality(item, increase_by=2)
                else:
                    increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in > 10:
                    increase_quality(item)
                elif item.sell_in > 5:
                    increase_quality(item, increase_by=2)
                elif item.sell_in > 0:
                    increase_quality(item, increase_by=3)
                else:
                    item.quality = 0
            else:
                decrease_quality(item, item.sell_in)
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def decrease_quality(item: Item, sell_in: int) -> None:
    """Decrease the quality of an item based on its sell_in value."""
    if sell_in <= 0:
        item.quality = max(0, item.quality - 2)
    else:
        item.quality = max(0, item.quality - 1)


def increase_quality(item, increase_by: int = 1) -> None:
    """Increase the quality of an item"""
    item.quality = min(50, item.quality + increase_by)
