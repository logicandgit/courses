# -*- coding: utf-8 -*- 
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

items = []

items += [Item('Aged Brie', 2, 0)]


def update_quality():
    for item in items:
        degradation = 2 if 'conjured' in item.name.lower() else 1
        increase = 1

        if 'sulfuras' in item.name.lower():
            continue

        if item.sell_in <= 0:
            degradation *= 2
        item.sell_in -= 1

        if 'aged brie' in item.name.lower() or 'backstage passes' in item.name.lower():
            if 'backstage passes' in item.name.lower():
                if item.sell_in < 11:
                    increase += 1
                if item.sell_in < 6:
                    increase += 1
                if item.sell_in <= 0:
                    item.quality = 0
                    continue
            if item.quality < 50:
                item.quality += 1 * increase

        else:
            item.quality -= 1 * degradation
            if item.quality < 0:
                item.quality = 0


if __name__ == '__main__':
    print("Basic tests")
    # Testing just one day lapse
    for _ in range(1):
        update_quality()
    print("Testing " + items[0].name)
    print(items[0].sell_in, 9, "Expected different value")
    print(items[0].quality, 19, "Expected different value")