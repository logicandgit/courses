# -*- coding: utf-8 -*-
import math


class Shape(object):

    def __init__(self, elem):
        self.elem = elem

    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0

    def __cmp__(self, fig2):
        if self.get_area() == fig2.get_area():
            return 0
        elif self.get_area() < fig2.get_area():
            return -1
        else:
            return 1
        # return cmp(self.get_area(), fig2.get_area())

    @staticmethod
    def get_max_shape(figures):
        max_fig = figures[0]
        for fig in figures[1:]:
            max_fig = fig if fig.get_area() > max_fig.get_area() else max_fig
        return max_fig

    def __str__(self):
        return 'I am shape'


class Rectangular(Shape):

    def __init__(self, length, width):
        super(Rectangular, self).__init__(length)
        self.width = width

    def __str__(self):
        return '{} of type {} with length {} and width {}, area: {}'.format(
            super(Rectangular, self).__str__(),
            self.__class__.__name__,
            self.elem, self.width,
            self.get_area
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
        return '{} of type {} with radius {}, area: {}'.format(
            super(Circle, self).__str__(),
            self.__class__.__name__,
            self.elem,
            self.get_area()
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
        return '{} of type {} with area: {} and point {}, {}, {}'.format(
            super(Triangle, self).__str__(),
            self.__class__.__name__,
            self.get_area(),
            *map(lambda x: tuple(x.__dict__.values()), self.__dict__.values())
        )

    def get_area(self):
        # a, b, c = self._get_size(self.elem, self.point_two, self.point_three)
        p = (self.ab + self.bc + self.ac) / 2
        return math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ac))

    def get_perimeter(self):
        # return sum(self._get_size(self.elem, self.point_two, self.point_three))
        return self.ab + self.bc + self.ac

    @property
    def ab(self):
        return self.elem.get_distance_to(self.point_two)

    @property
    def bc(self):
        return self.point_two.get_distance_to(self.point_three)

    @property
    def ac(self):
        return self.point_three.get_distance_to(self.elem)

    # def _get_size(self, point1, point2, point3):
    #     a = point1.get_distance_to(point2)
    #     b = point2.get_distance_to(point3)
    #     c = point3.get_distance_to(point1)
    #     return a, b, c


class Square(Shape):

    def __init__(self, side):
        super(Square, self).__init__(side)

    def __str__(self):
        return '{} of type {} with side {} and area: {}'.format(
            super(Square, self).__str__(),
            self.__class__.__name__,
            self.elem,
            self.get_area()
        )

    def get_area(self):
        return self.elem ** 2

    def get_perimeter(self):
        return self.elem * 4

    def get_location(self):
        pass

if __name__ == '__main__':
    # rect = Rectangular(1, 2)
    # print str(rect)
    # point = Point(1, 2)
    # print str(point)
    # print rect
    # print rect.get_area()
    # print rect.get_perimeter()
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 4)
    triangele = Triangle(p1, p2, p3)
    # print type(triangele.ab)
    # print
    # print triangele.get_perimeter()
    # triangele.elem = Point(1, 1)
    # print triangele.get_perimeter()
    # triangele.ab = 1
    # print int(2).__cmp__(1)
    # print str(triangele)
    square = Square(2)
    cirle = Circle(2)
    print str(triangele)
    print str(square)
    print str(cirle)
    print square > triangele
    print square < triangele
    print cmp(square, triangele)
    print cmp(triangele, square)
    print square > cirle

    print str(Shape.get_max_shape([square, cirle, triangele]))
    # print cmp(square, triangele)
    # print str(square)
    # print triangele.get_area()
    # print triangele.get_perimeter()
