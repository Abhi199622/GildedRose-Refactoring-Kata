# -*- coding: utf-8 -*-
from __future__ import print_function
from item import create_item
from gilded_rose import *



def main():
    print("OMGHAI!")
    items = [
        create_item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        create_item(name="Aged Brie", sell_in=2, quality=0),
        create_item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        create_item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        create_item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        create_item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        create_item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        create_item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        create_item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()
