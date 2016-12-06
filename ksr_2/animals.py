# -*- coding: utf-8 -*-

import os

from random import randint


class Animal(object):

    GROWTH_SCALE = {
        'born': lambda growth: growth == 0,
        'baby': lambda growth: 0 < growth <= 10,
        'child': lambda growth: 10 < growth <= 20,
        'young': lambda growth: 20 < growth <= 30,
        'mature': lambda growth: 30 < growth <= 40,
        'old': lambda growth: growth > 40
    }

    def __init__(self, growth_rate, food_need, water_need, name):
        self._weight = 1
        self._days_growing = 0
        self._type = 'generic'
        self._status = 'born'
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self.name = name

    @property
    def weght(self):
        return self._weight

    @property
    def days_growing(self):
        return self._days_growing

    @property
    def growth_rate(self):
        return self._growth_rate

    @property
    def food_need(self):
        return self._food_need

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
            'food_need': self._food_need,
            'water_need': self._water_need
        }

    def report(self):
        return {
            'name': self.name,
            'type': self._type,
            'status': self._status,
            'growth': self._weight,
            # 'growth_rate': self._growth,
            'days_growing': self._days_growing
        }

    def _update_status(self):
        # temp, _ = divmod(self.growth, 5)
        if self.GROWTH_SCALE['born'](self._weight):
            self._status = 'born'
        elif self.GROWTH_SCALE['baby'](self._weight):
            self._status = 'baby'
        elif self.GROWTH_SCALE['child'](self._weight):
            self._status = 'child'
        elif self.GROWTH_SCALE['young'](self._weight):
            self._status = 'young'
        elif self.GROWTH_SCALE['mature'](self._weight):
            self._status = 'mature'
        elif self.GROWTH_SCALE['old'](self._weight):
            self._status = 'old'

    def grow(self, current_food, current_water):
        if (current_food >= self._food_need) and (current_water >= self._water_need):
            self._weight += self._growth_rate
        self._update_status()
        self._days_growing += 1


class Cow(Animal):

    def __init__(self, name):
        super(Cow, self).__init__(3, 5, 4, name)
        self._type = 'Cow'

    def grow(self, current_food, current_water):
        if (current_food >= self._food_need) and (current_water >= self._water_need):
            if current_water >= self._water_need and current_food >= self._food_need:
                if self.GROWTH_SCALE['born'](self._weight):
                    self._weight += self._growth_rate * 1.4
                elif self.GROWTH_SCALE['baby'](self._weight):
                    self._weight += self._growth_rate * 1.3
                elif self.GROWTH_SCALE['child'](self._weight):
                    self._weight += self._growth_rate
                elif self.GROWTH_SCALE['young'](self._weight):
                    self._weight += self._growth_rate
                elif self.GROWTH_SCALE['mature'](self._weight):
                    self._weight += self._growth_rate
                elif self.GROWTH_SCALE['old'](self._weight):
                    self._weight += self._growth_rate * 0.5

        self._update_status()
        self._days_growing += 1


class Sheep(Animal):

    def __init__(self, name):
        super(Sheep, self).__init__(5, 3, 3, name)
        self._type = 'sheep'

    def grow(self, food, water):
        if water >= self._water_need and food >= self._food_need:
            if self.GROWTH_SCALE['born'](self._weight):
                self._weight += self._growth_rate * 1.4
            elif self.GROWTH_SCALE['baby'](self._weight):
                self._weight += self._growth_rate * 1.3
            elif self.GROWTH_SCALE['child'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['young'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['mature'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['old'](self._weight):
                self._weight += self._growth_rate * 0.5

        self._update_status()
        self._days_growing += 1
