from circle import Circle
import pytest
from math import pi

@pytest.mark.parametrize(
    ("sides", "expected_exception"),
    [
        pytest.param((1,), None, id="valid integer"),
        pytest.param((1.2,), None, id="invalid float"),
        pytest.param((pi,), None, id="approximate float"),
        pytest.param((), TypeError, id="empty parameters"),
        pytest.param((1, 2), TypeError, id="too many parameters"),
        pytest.param((0,), ValueError, id="zero"),
        pytest.param((-1,), ValueError, id="negative"),
        pytest.param(("1",), ValueError, id="str"),
        pytest.param((True,), ValueError, id="boolean"),
    ]
)
def test_circle_creation(sides, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            f = Circle(*sides)
    else:
        f = Circle(*sides)
        assert isinstance(f, Circle), f"Expected an instance of 'Circle', now is {type(f).__name__}"


@pytest.mark.parametrize(
    ("side", "perimeter"),
    [
        pytest.param(1, 1, id="valid integer"),
        pytest.param(1.2, 1.2, id="invalid float"),
        pytest.param(2 * pi, 2 * pi, id="approximate float"),
    ]
)
def test_circle_get_perimeter(side, perimeter):
    f = Circle(side)
    assert f.get_perimeter() == pytest.approx(perimeter), f"The perimeter should be {perimeter}, now is {f.get_perimeter()}"


@pytest.mark.parametrize(
    ("side", "area"),
    [
        pytest.param(1, 0.25 / pi, id="valid integer"),
        pytest.param(2.2, 1.21 / pi, id="invalid float"),
        pytest.param(2 * pi, pi, id="approximate float"),
    ]
)
def test_rectangle_get_area(side, area):
    f = Circle(side)
    assert f.get_area() == pytest.approx(area), f"The area should be {area}, now is {f.get_area()}"