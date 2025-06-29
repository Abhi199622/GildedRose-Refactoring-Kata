# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import create_item
from enums import ItemName


class GildedRoseTest(unittest.TestCase):
    def test_base_item_quality(self):
        item = create_item(name="foo", sell_in=4, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality decreases by 1 each day
        self.assertEqual(3, item.quality)

    def test_base_item_quality_sell_by_date_passed(self):
        item = create_item(name="foo", sell_in=0, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality decreases by 2 when sell date is passed
        self.assertEqual(2, item.quality)

    def test_item_quality_negative(self):
        item = create_item(name="foo", sell_in=0, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Ensure quality does not go negative
        self.assertEqual(0, item.quality)

    def test_aged_brie_item_quality(self):
        item = create_item(name=ItemName.AGED_BRIE, sell_in=2, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Aged Brie increases in quality as it gets older
        self.assertEqual(1, item.quality)

    def test_aged_brie_item_quality_sell_date_passed(self):
        item = create_item(name=ItemName.AGED_BRIE, sell_in=0, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Aged Brie twice increase in quality when sell date is passed
        self.assertEqual(2, item.quality)

    def test_aged_brie_item_quality_max(self):
        item = create_item(name=ItemName.AGED_BRIE, sell_in=2, quality=50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Ensure quality does not exceed 50
        self.assertEqual(50, item.quality)

    def test_sulfuras_item_sell_in_and_quality(self):
        item = create_item(name=ItemName.SULFURAS, sell_in=1, quality=80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Sulfuras is never sold nor any change in quality
        self.assertEqual(80, item.quality)
        self.assertEqual(1, item.sell_in)

    def test_backstage_quality_sell_in_less_than_equal_ten(self):
        item = create_item(name=ItemName.BACKSTAGE, sell_in=10, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality increases by 2 when sell_in is less than or equal to 10 days
        self.assertEqual(22, item.quality)

    def test_backstage_quality_sell_in_less_than_equal_five(self):
        item = create_item(name=ItemName.BACKSTAGE, sell_in=5, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality increases by 3 when sell_in is less than or equal to 5 days
        self.assertEqual(23, item.quality)

    def test_backstage_when_concert_over(self):
        item = create_item(name=ItemName.BACKSTAGE, sell_in=0, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality drops to 0 after the concert
        self.assertEqual(0, item.quality)

    def test_backstage_quality_sell_in_greater_than_10(self):
        item = create_item(name=ItemName.BACKSTAGE, sell_in=11, quality=20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality increases normally
        self.assertEqual(21, item.quality)

    def test_conjured_item_quality_and_sell_in(self):
        item = create_item(name=ItemName.CONJURED, sell_in=3, quality=6)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        # item sell date decreases by 1
        self.assertEqual(2, item.sell_in)

        # item decrease in quality twice as fast
        self.assertEqual(4, item.quality)

    def test_conjured_item_quality_sell_in_passed(self):
        item = create_item(name=ItemName.CONJURED, sell_in=0, quality=6)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        # Quality decreases by 4 when sell date is passed
        self.assertEqual(2, item.quality)
        self.assertEqual(-1, item.sell_in)

    def test_item_string_format(self):
        item = create_item(name="foo", sell_in=4, quality=4)
        self.assertEqual("foo, 4, 4", str(item))


if __name__ == '__main__':
    unittest.main()
