# -*- coding: utf-8 -*-
import math


class Rectangular:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * sum(self.length, self.width)

    def get_location(self):
        pass


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_location(self):
        pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Triangle:

    def __init__(self, point_one, point_two, point_three):
        self.point_one = point_one
        self.point_two = point_two
        self.point_three = point_three

    def get_area(self):
        a, b, c = self._get_size(self.point_one, self.point_two, self.point_three)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def get_perimeter(self):
        return sum(self._get_size(self.point_one, self.point_two, self.point_three))

    def _get_size(self, point1, point2, point3):
        a = point1.get_distance_to(point2)
        b = point2.get_distance_to(point3)
        c = point3.get_distance_to(point1)
        return a, b, c


class Square:

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

    def get_location(self):
        pass

if __name__ == '__main__':
    # rect = Rectangular(1, 2)
    # print rect
    # print rect.get_area()
    # print rect.get_perimeter()

    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(2, 2)
    triangele = Triangle(p1, p2, p3)
    print triangele.get_area()
    print triangele.get_perimeter()
