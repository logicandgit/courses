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


class Circle(Shape):

    def __init__(self, radius):
        super(Circle, self).__init__(radius)

    def __str__(self):
        return '{} of type {} with radius {}'.format(
            super(Circle, self).__str__(),
            self.__class__.__name__,
            self.elem
        )

    def get_area(self):
        return math.pi * self.elem ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.elem

    def get_location(self):
        pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'I am point {}'.format(
            tuple(self.__dict__.values())
        )

    def get_distance_to(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Triangle(Shape):

    def __init__(self, point_one, point_two, point_three):
        super(Triangle, self).__init__(point_one)
        self.point_two = point_two
        self.point_three = point_three

    def __str__(self):
        return '{} of type {} with points {}, {}, {}'.format(
            super(Triangle, self).__str__(),
            self.__class__.__name__,
            *map(lambda x: tuple(x.__dict__.values()), self.__dict__.values())
        )

    def get_area(self):
        a, b, c = self._get_size(self.elem, self.point_two, self.point_three)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def get_perimeter(self):
        return sum(self._get_size(self.elem, self.point_two, self.point_three))

    def _get_size(self, point1, point2, point3):
        a = point1.get_distance_to(point2)
        b = point2.get_distance_to(point3)
        c = point3.get_distance_to(point1)
        return a, b, c


class Square(Shape):

    def __init__(self, side):
        super(Square, self).__init__(side)

    def __str__(self):
        return '{} of type {} with side {}'.format(
            super(Square, self).__str__(),
            self.__class__.__name__,
            self.elem
        )

    def get_area(self):
        return self.elem ** 2

    def get_perimeter(self):
        return self.elem * 4

    def get_location(self):
        pass

if __name__ == '__main__':
    rect = Rectangular(1, 2)
    print str(rect)
    point = Point(1, 2)
    print str(point)
    # print rect
    # print rect.get_area()
    # print rect.get_perimeter()
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(2, 2)
    triangele = Triangle(p1, p2, p3)
    print str(triangele)
    square = Square(4)
    print str(square)
    # print triangele.get_area()
    # print triangele.get_perimeter()
