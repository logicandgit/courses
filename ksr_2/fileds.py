# -*- coding: utf-8 -*- 

import animals
import crops


class Field(object):

    def __init__(self, max_crops, max_animals):
        self._crops = []
        self._animals = []
        self._max_crops = max_crops
        self._max_animals = max_animals

    @property
    def crops(self):
        return self._crops

    @property
    def animals(self):
        return self._animals

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        return False

    def add_animal(self, crop):
        if len(self._animals) < self._max_animals:
            self._animals.append(crop)
            return True
        return False

    def harvest_crop(self, number_crop):
        return self._crops.pop(number_crop)

    def remove_animal(self, number_animal):
        return self._animals.pop(number_animal)

    def report_content(self):
        result = {}
        if self._crops:
            result['crops'] = self._crops
        if self._animals:
            result['animals'] = self._animals
        return result

    def report_needs(self):
        max_crops_need = {'light_need': 0, 'water_need': 0}
        result = {'water': 0, 'light': 0, 'food': 0}
        if self._crops:
            for crop in self._crops:
                if (crop.needs()['light_need'] > max_crops_need['light_need']) and \
                        (crop.needs()['water_need'] > max_crops_need['water_need']):
                    max_crops_need = crop.needs()
        if self._animals:
            for animal in self.animals:
                result['food'] += animal.needs()['food_need']
        result['water'] = max_crops_need['water_need']
        result['light'] = max_crops_need['light_need']
        return result

    def grow(self, food, light, water):
        pass


def display_crops(crops):
    # todo range(len)
    for crop in crops:
        print crops.index(crop)
        print crop.report()


def display_animals(animals):
    for animal in animals:
        print animals.index(animal)
        print animal.report()


def select_crop():
    index = raw_input('Select crop number: ')
    return index


def select_animal():
    index = raw_input('Select animal number: ')
    return index


def harvest_crop_from_field(field):
    list_crops = field.crops
    display_crops(list_crops)
    return field.harvest_crop(select_crop())


def remove_animal_from_field(field):
    list_animals = field.animals
    display_animals(list_animals)
    return field.harvest_crop(select_animal())

if __name__ == '__main__':
    field1 = Field(2, 3)
    wheat = crops.Wheat(1, 1, 1)
    wheat2 = crops.Wheat(2, 2, 2)
    cow = animals.Cow('Cow')
    cow2 = animals.Cow('Cow2')
    field1.plant_crop(wheat)
    field1.plant_crop(wheat2)
    field1.add_animal(cow)
    field1.add_animal(cow2)
    print field1.report_needs()
