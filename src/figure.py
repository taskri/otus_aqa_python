from abc import ABC, abstractmethod


class Figure(ABC):
    def __str__(self):
        return f"Object of class {self.__class__.__name__}"

    @staticmethod
    def validate_sides(*sides):
        for side in sides:
            if not isinstance(side, (int, float)) or isinstance(side, bool) or side <= 0:
                raise ValueError(f"Side must be a positive number, now {side}")

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Can add only other figure")
        return self.get_area() + other_figure.get_area()