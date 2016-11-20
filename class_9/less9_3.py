# -*- coding: utf-8 -*-

import time
import turtle


class Shape(object):

    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        return 'I am shape'

    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0

    def draw(self):
        print self.__class__.__name__


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

    def draw(self):
        super(Rectangular, self).draw()

        for _ in range(2):
            self._draw(self.elem)
            self._draw(self.width)

        turtle.reset()

    def _draw(self, size):
        # timeout = 3
        turtle.forward(size)
        # time.sleep(timeout)
        turtle.right(90)
        # time.sleep(timeout)


class Square(Rectangular):

    def __init__(self, side):
        super(Square, self).__init__(side, side)

if __name__ == '__main__':
    rect = Rectangular(100, 200)
    print str(rect)
    square = Square(400)
    print str(square)

    rect.draw()
    square.draw()
