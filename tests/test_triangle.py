from triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("sides", "expected_exception"),
    [
        pytest.param((2, 2, 2), None, id="valid sides"),
        pytest.param((1.5, 2.3, 3.6), None, id="valid floats"),
        pytest.param((), TypeError, id="no parameters"),
        pytest.param((1.5, 3), TypeError, id="not enough parameters"),
        pytest.param((1.5, 2.3, 3.6, 3), TypeError, id="too many parameters"),
        pytest.param((None, 1, 1), ValueError, id="None"),
        pytest.param((0, 0, 0), ValueError, id="zeros"),
        pytest.param((-1, 1, 1), ValueError, id="negative"),
        pytest.param((True, 1, 1), ValueError, id="boolean"),
        pytest.param(("1", 1, 1), ValueError, id="str"),
        pytest.param((1, 2, 4), ValueError, id="triangle inequality conditions are not met"),
    ]
)
def test_triangle_creation(sides, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            f = Triangle(*sides)
    else:
        f = Triangle(*sides)
        assert isinstance(f, Triangle), f"Expected an instance of 'Triangle', now is {type(f).__name__}"



@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [
        (1, 1, 1, 3),
        (1.5, 1.2, 1, 3.7)
    ],
    ids=["integers", "floats"],
)
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    f = Triangle(side_a, side_b, side_c)
    assert f.get_perimeter() == perimeter, f"The perimeter should be {perimeter}, now is {f.get_perimeter()}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (3, 4, 5, 6),
        (1, 1.2, 1, 0.48),
    ],
    ids=["integers", "floats"],
)
def test_triangle_get_area(side_a, side_b, side_c, area):
    f = Triangle(side_a, side_b, side_c)
    assert f.get_area() == pytest.approx(area), f"The area should be {area}, now is {f.get_area()}"