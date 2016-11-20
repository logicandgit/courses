# -*- coding: utf-8 -*-
import math


class Shape(object):

    def __init__(self, elem):
        self.elem = elem

    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0

    def __str__(self):
        return 'I am shape'


class Rectangular(Shape):

    def __init__(self, length, width):
        super(Rectangular, self).__init__(length)
        self.width = width

    def __str__(self):
        return '{} of type {} with length {} and width {}'.format(
            super(Rectangular, self).__str__(),
            self.__class__.__name__,
            self.elem, self.width
        )

    def get_area(self):
        return self.elem * self.width

    def get_perimeter(self):
        return 2 * (self.elem + self.width)

    def get_location(self):
        pass


class Square(Rectangular):

    def __init__(self, side):
        super(Square, self).__init__(side, side)


if __name__ == '__main__':
    rect = Rectangular(1, 2)
    # print str(rect)
    square = Square(4)
    # print str(square)
    print square.get_area()
    print square.get_perimeter()
