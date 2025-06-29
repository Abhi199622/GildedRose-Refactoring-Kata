# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_base_item_quality(self):
        item = Item(name="foo", sell_in=4, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality decreases by 1 each day
        self.assertEqual(3, item.quality)

    def test_base_item_quality_sell_by_date_passed(self):
        item = Item(name="foo", sell_in=0, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality decreases by 2 when sell date is passed
        self.assertEqual(2, item.quality)

    def test_item_quality_negative(self):
        item = Item(name="foo", sell_in=0, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Ensure quality does not go negative
        self.assertEqual(0, item.quality)

    def test_aged_brie_item_quality(self):
        item = Item(name="Aged Brie", sell_in=2, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Aged Brie increases in quality as it gets older
        self.assertEqual(1, item.quality)

    def test_aged_brie_item_quality_sell_date_passed(self):
        item = Item(name="Aged Brie", sell_in=0, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Aged Brie twice increase in quality when sell date is passed
        self.assertEqual(2, item.quality)

    def test_aged_brie_item_quality_max(self):
        item = Item(name="Aged Brie", sell_in=2, quality=50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Ensure quality does not exceed 50
        self.assertEqual(50, item.quality)

    def test_sulfuras_item_sell_in_and_quality(self):
        item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Sulfuras is never sold nor any change in quality
        self.assertEqual(80, item.quality)
        self.assertEqual(1, item.sell_in)

    def test_backstage_quality_sell_in_less_than_equal_ten(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality increases by 2 when sell_in is less than or equal to 10 days
        self.assertEqual(22, item.quality)

    def test_backstage_quality_sell_in_less_than_equal_five(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality increases by 3 when sell_in is less than or equal to 5 days
        self.assertEqual(23, item.quality)

    def test_backstage_when_concert_over(self):
        item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality drops to 0 after the concert
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
