import pytest

from amag_op.helpers.ops import add, subtract, expo, multiply, divide, perform_op


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1.0, 1.0, 2.0),
        (0, 0, 0.0),
        (1.0, -1.0, 0.0),
        (1, 1, 2),
    ],
)
def test_add_passes(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1.0, 1.0, 0.0),
        (0, 0, 0.0),
        (1.0, -1.0, 2.0),
        (-1, 1, -2),
    ],
)
def test_subtract_passes(x, y, result):
    assert subtract(x, y) == result


@pytest.mark.xfail
def test_subtract_fails():
    assert subtract(1.3, 1.0) == 0.3


@pytest.mark.parametrize(
    "x,y,result",
    [
        (2.0, 4.0, 16.0),
        (1.0, -1.0, 1.0),
        (3, 0, 1),
    ],
)
def test_expo_passes(x, y, result):
    assert expo(x, y) == result


@pytest.mark.parametrize(
    "x,y,result",
    [
        (2.0, 3.0, 6.0),
        (0, 0, 0.0),
        (1.0, -1.0, -1.0),
        (1, 1, 1),
    ],
)
def test_multiply_passes(x, y, result):
    assert multiply(x, y) == result


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1.0, 1.0, 1.0),
        (1.0, -1.0, -1.0),
        (3, 2, 1.5),
    ],
)
def test_divide_passes(x, y, result):
    assert divide(x, y) == result


@pytest.mark.parametrize(
    "x,y,op,result",
    [
        (1.0, 1.0, "addition", 2.0),
        (1.0, -1.0, "multiplication", -1.0),
        (1, 1, "division", 1),
        (0, 0, "subtraction", 0.0),
        (2, 0, "exponentiation", 1),
    ],
)
def test_perform_op_passes(x, y, op, result):
    assert perform_op(x, y, op) == result
