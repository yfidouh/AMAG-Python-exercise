from amag_op.exceptions.type_errors import NotFloatError
from amag_op.exceptions.op_type_errors import (
    CannotDivideByZeroError,
    UndefinedExpoError,
    UnsupportedOpError,
)


def check_for_float(*args):
    for arg in args:
        if not isinstance(arg, float) and not isinstance(arg, int):
            raise NotFloatError(arg)


def check_for_divide_by_zero(x):
    if x == 0:
        raise CannotDivideByZeroError()


def add(x, y):
    check_for_float(x, y)
    return x + y


def subtract(x, y):
    check_for_float(x, y)
    return x - y


def expo(x, y):
    check_for_float(x, y)
    if x == y == 0:
        raise UndefinedExpoError()
    return x ** y


def multiply(x, y):
    check_for_float(x, y)
    return x * y


def divide(x, y):
    check_for_float(x, y)
    check_for_divide_by_zero(y)
    return x / y


def perform_op(x, y, op):
    ops = {
        "addition": add,
        "multiplication": multiply,
        "exponentiation": expo,
        "subtraction": subtract,
        "division": divide,
    }

    if op not in ops:
        raise UnsupportedOpError(op)

    return ops[op](x, y)
