from utils import decrease_quality, increase_quality
from enums import ItemName


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    """Normal item class for all items."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_sell_in(self):
        """Update sell by date of item."""
        self.sell_in -= 1

    def update_quality(self):
        """Update quality of item."""
        self.quality = decrease_quality(self.quality, self.sell_in)
        self.update_sell_in()


class AgedBrie(NormalItem):
    """This item increases in quality as it gets older."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Update quality of item."""
        if self.sell_in <= 0:
            self.quality = increase_quality(self.quality, increase_by=2)
        else:
            self.quality = increase_quality(self.quality, increase_by=1)
        self.update_sell_in()


class Sulfuras(NormalItem):
    """This item does not change in quality or sell_in."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Sulfuras does not change quality or sell_in."""
        pass  # No changes to quality or sell_in


class Backstage(NormalItem):
    """Item quality increases based on sell by date."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Update quality of item based on sell by date."""
        if self.sell_in > 10:
            self.quality = increase_quality(self.quality)
        elif self.sell_in > 5:
            self.quality = increase_quality(self.quality, increase_by=2)
        elif self.sell_in > 0:
            self.quality = increase_quality(self.quality, increase_by=3)
        else:
            self.quality = 0

        self.update_sell_in()


class Conjured(NormalItem):
    """item decreases in quality twice as fast."""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """Update quality of item."""
        if self.sell_in <= 0:
            self.quality = decrease_quality(self.quality, self.sell_in, decrease_by=4)
        else:
            self.quality = decrease_quality(self.quality, self.sell_in, decrease_by=2)
        self.update_sell_in()


def create_item(name, sell_in, quality):
    """Factory function to create items based on their type."""
    item_to_class_map = {
        ItemName.AGED_BRIE: AgedBrie,
        ItemName.SULFURAS: Sulfuras,
        ItemName.BACKSTAGE: Backstage,
        ItemName.CONJURED: Conjured
    }
    return item_to_class_map.get(name, NormalItem)(name, sell_in, quality)
