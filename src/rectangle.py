from figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.validate_sides(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def get_area(self):
        return self.side_a * self.side_b
