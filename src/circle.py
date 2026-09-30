from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, circumference):
        self.validate_sides(circumference)
        self.circumference = circumference

    def get_perimeter(self):
        return self.circumference

    def get_area(self):
        return self.circumference ** 2 / (4 * pi)