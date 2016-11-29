# -*- coding: utf-8 -*-

import os

from random import randrange


class Crop(object):
    _growth = 0
    _days_growing = 0
    _growth_rate = None
    _light_need = None
    _water_need = None
    _type = 'generic'
    _status = 'seed'

    STATUS = ('seed', 'seeding', 'young', 'mature', 'old')

    def __init__(self, growth_rate, light_need, water_need):
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need

    @property
    def growth(self):
        return self._growth

    @property
    def days_growing(self):
        return self._days_growing

    @property
    def growth_rate(self):
        return self._growth_rate

    @property
    def light_need(self):
        return self._light_need

    @property
    def water_need(self):
        return self._water_need

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    def needs(self):
        return {
            'light_need': self._light_need,
            'water_need': self._water_need
        }

    def report(self):
        return {
            'type': self._type,
            'status': self._status,
            'growth': self._growth,
            # 'growth_rate': self._growth,
            'days_growing': self._days_growing
        }

    def _update_status(self):
        # temp, _ = divmod(self.growth, 5)
        if self._growth == 0:
            self._status = Crop.STATUS[0]
        elif 0 < self._growth < 5:
            self._status = Crop.STATUS[1]
        elif 5 <= self._growth < 10:
            self._status = Crop.STATUS[2]
        elif 10 <= self._growth < 15:
            self._status = Crop.STATUS[3]
        elif self._growth >= 15:
            self._status = Crop.STATUS[4]

    def grow(self, current_light, current_water):
        if (current_light >= self._light_need) and (current_water >= self._water_need):
            self._growth += self._growth_rate
            self._update_status()
        self._days_growing += 1


def auto_grow(crop, days):
    for _ in range(days):
        ligth = randrange(1, 10)
        water = randrange(1, 10)
        crop.grow(ligth, water)


def check(value):
    return value.isdigit() and 1 <= int(value) <= 10


def manual_grow(crop):
    exit = False
    while not exit:
        light = raw_input('Enter light: ')
        water = raw_input('Enter water: ')
        if check(light) and check(water):
            crop.grow(light, water)
            exit = True
        else:
            print 'You set bad value: {} or {}. Please choose from 1 to 10'.format(light, water)
        # if light.isdigit() and  or water


def manager():
    exit = False
    example = Crop(1, 1, 1)
    while not exit:
        print ("""
        Hello %UserName%! It is game.
        1 - Manual Grow Crop
        2 - Automatically Grow Crop
        3 - Display Crop Report
        4 - Exit
        """)
        choice = get_menu_choice()
        run_choice(example, choice)


def get_menu_choice():
    valid = False
    value = None
    while not valid:
        choice = raw_input('Set you choice: ')
        if choice.isdigit() and 1 <= int(choice) <= 4:
            valid = True
            value = int(choice)
        else:
            print 'You set bad value: {}. Please choose from 1 to 4'.format(choice)
    return value


def run_choice(corp, choice):
    if choice == 1:
        manual_grow(corp)
    elif choice == 2:
        auto_grow(corp, 30)
    elif choice == 3:
        print corp.report()
    else:
        exit(0)

if __name__ == '__main__':
    corp1 = Crop(1, 1, 1)
    corp2 = Crop(2, 2, 2)
    corp3 = Crop(3, 3, 3)

    print corp2.water_need
    print corp1.report()
    print corp3.needs()

    auto_grow(corp1, 5)
    print corp1.report()
    manager()
