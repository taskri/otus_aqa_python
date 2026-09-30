from figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.validate_sides(side_a, side_b, side_c)
        self.validate_triangle(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @staticmethod
    def validate_triangle(side_a, side_b, side_c):
        conditions = [side_a + side_b > side_c, side_b + side_c > side_a, side_c + side_a > side_b]
        if not all(conditions):
            raise ValueError(f"Invalid triangle sides: {side_a, side_b, side_c}")