import pytest

from amag_op.helpers.ops import add, subtract, expo, multiply, divide, perform_op


@pytest.mark.parametrize(
    "x,y,expected_message",
    [
        ("arst", 1, "arst is not a float"),
        ("123", 1, "123 is not a float"),
    ],
)
def test_add_raises(x, y, expected_message):
    with pytest.raises(Exception) as e_info:
        add(x, y)
    assert str(e_info.value) == expected_message


@pytest.mark.parametrize(
    "x,y,expected_message",
    [
        ("arst", 1, "arst is not a float"),
        ("123", 1, "123 is not a float"),
    ],
)
def test_subtract_exceptions(x, y, expected_message):
    with pytest.raises(Exception) as e_info:
        subtract(x, y)
    assert str(e_info.value) == expected_message


@pytest.mark.parametrize(
    "x,y,expected_message",
    [
        ("arst", 1, "arst is not a float"),
        ("123", 1, "123 is not a float"),
        (0, 0, "0^0 undefined or something"),
    ],
)
def test_expo_exceptions(x, y, expected_message):
    with pytest.raises(Exception) as e_info:
        expo(x, y)
    assert str(e_info.value) == expected_message


@pytest.mark.parametrize(
    "x,y,expected_message",
    [
        ("arst", 1, "arst is not a float"),
        ("123", 1, "123 is not a float"),
    ],
)
def test_multiply_exceptions(x, y, expected_message):
    with pytest.raises(Exception) as e_info:
        multiply(x, y)
    assert str(e_info.value) == expected_message


@pytest.mark.parametrize(
    "x,y,expected_message",
    [
        ("arst", 1, "arst is not a float"),
        (1, 0, "Cannot divide by zero"),
    ],
)
def test_divide_exceptions(x, y, expected_message):
    with pytest.raises(Exception) as e_info:
        divide(x, y)
    assert str(e_info.value) == expected_message


@pytest.mark.parametrize(
    "x,y,op,expected_message",
    [
        (1, 0, "poop", "poop -> Unsupported operation type"),
    ],
)
def test_perform_op_exceptions(x, y, op, expected_message):
    with pytest.raises(Exception) as e_info:
        perform_op(x, y, op)
    assert str(e_info.value) == expected_message
