# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_base_item_quality(self):
        item = Item(name="foo", sell_in=4, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(3, item.quality)

    def test_base_item_quality_sell_by_date_passed(self):
        item = Item(name="foo", sell_in=0, quality=4)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(2, item.quality)

        
if __name__ == '__main__':
    unittest.main()
