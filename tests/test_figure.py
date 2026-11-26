from figure import Figure
from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle
import pytest
from math import pi


@pytest.mark.parametrize(
    ("sides", "expected_exception"),
    [
        pytest.param((0,), ValueError, id="zero"),
        pytest.param((-2,), ValueError, id="negative integer"),
        pytest.param(("3",), ValueError, id="str"),
        pytest.param((True,), ValueError, id="boolean"),
        pytest.param((None,), ValueError, id="None"),
        pytest.param((), ValueError, id="no parameters"),
        pytest.param((2, 4), None, id="valid integers"),
        pytest.param((2.4, 4.5, 6.1, 3.7), None, id="valid floats"),
    ]
)
def test_figure_validation_by_sides(sides, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            Figure.validate_sides(*sides)
    else:
        f = Figure.validate_sides(*sides)
        assert f is None, f"Sides are not valid:{sides}"


@pytest.mark.parametrize(
    ("figure", "expected_str"),
    [
        pytest.param(Circle(2), "Object of class Circle", id="circle object"),
        pytest.param(Rectangle(2, 3), "Object of class Rectangle", id="rectangle object"),
        pytest.param(Square(2), "Object of class Square", id="square object"),
        pytest.param(Triangle(2, 3, 3), "Object of class Triangle",),
    ]
)
def test_figure_str(figure, expected_str):
    assert str(figure) == expected_str


@pytest.mark.parametrize(
    ("figure_a", "figure_b", "expected_area"),
    [
    pytest.param(Rectangle(2,3), Square(2), 10, id="Rectangle + Square integers"),
    pytest.param(Triangle(3, 4, 5), Circle(2 * pi), 6 + pi, id="Triangle + Circle approx"),
    pytest.param(Square(2.5), Square(2.5), 12.5, id="Square + Square floats"),
    ]
)
def test_figure_add_area(figure_a, figure_b, expected_area):
    assert figure_a.add_area(figure_b) == pytest.approx(expected_area), (f"Sum of 2 areas is expected to be {expected_area}, /"
                                                                         f"now is {figure_a.add_area(figure_b)}")


def test_figure_add_area_rejects_non_figure():
    figure = Rectangle(2, 3)
    with pytest.raises(ValueError):
        figure.add_area(None)