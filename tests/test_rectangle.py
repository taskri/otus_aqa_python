from rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ("sides", "expected_exception"),
    [
        pytest.param((2, 4), None, id="valid integers"),
        pytest.param((3.5, 5.5), None, id="valid floats"),
        pytest.param((1,), TypeError, id="not enough sides"),
        pytest.param((2, 3, 4), TypeError, id="too many sides"),
        pytest.param((-2, 3), ValueError, id="negative integer"),
        pytest.param(("3", 3), ValueError, id="str"),
        pytest.param((True, 3), ValueError, id="boolean"),
    ]
)
def test_rectangle_creation(sides, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            f = Rectangle(*sides)
    else:
        f = Rectangle(*sides)
        assert isinstance(f, Rectangle), f"Expected an instance of 'Rectangle', now is {type(f).__name__}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [
        (3, 5, 16),
        (3.5, 5.5, 18),
        (2, 2, 8)
    ],
    ids= ["integer", "float", "same sides"]
)
def test_rectangle_get_perimeter(side_a, side_b, perimeter):
    f = Rectangle(side_a,side_b)
    assert f.get_perimeter() == perimeter, f"The perimeter should be {perimeter}, now is {f.get_perimeter()}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25),
        (2, 2, 4),
    ],
    ids= ["integer", "float", "same sides"]
)
def test_rectangle_get_area(side_a, side_b, area):
    f = Rectangle(side_a,side_b)
    assert f.get_area() == area, f"The area should be {area}, now is {f.get_area()}"

