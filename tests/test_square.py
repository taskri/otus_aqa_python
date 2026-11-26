from square import Square
import pytest

@pytest.mark.parametrize(
    ("sides", "expected_exception"),
    [
        pytest.param((1,), None, id="valid integer"),
        pytest.param((1.2,), None, id="invalid float"),
        pytest.param((0,), ValueError, id="zero"),
        pytest.param((-2,), ValueError, id="negative integer"),
        pytest.param(("3",), ValueError, id="str"),
        pytest.param((True,), ValueError, id="boolean"),
        pytest.param((), TypeError, id="no parameters"),
        pytest.param((2, 4), TypeError, id="too many parameters"),
    ]
)
def test_square_creation(sides, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            f = Square(*sides)
    else:
        f = Square(*sides)
        assert isinstance(f, Square), f"Expected an instance of 'Square', now is {type(f).__name__}"


@pytest.mark.parametrize(
    ("side", "perimeter"),
    [
        (3, 12),
        (5.5, 22),
    ],
    ids= ["integer", "float"]
)
def test_square_get_perimeter(side, perimeter):
    f = Square(side)
    assert f.get_perimeter() == perimeter, f"The perimeter should be {perimeter}, now is {f.get_perimeter()}"


@pytest.mark.parametrize(
    ("side","area"),
    [
        (3, 9),
        (5.5, 30.25),
    ],
    ids= ["integer", "float"]
)
def test_square_get_area(side, area):
    f = Square(side)
    assert f.get_area() == area, f"The area should be {area}, now is {f.get_area()}"