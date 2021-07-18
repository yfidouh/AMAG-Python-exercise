# TODO define custom exception types.


def add(x, y):
    if type(x) is not float or type(y) is not float:
        raise Exception("not float")
    return x + y


def subtract(x, y):
    if type(x) is not float or type(y) is not float:
        raise Exception("not float")
    return x - y


def expo(x, y):
    if type(x) is not float or type(y) is not float:
        raise Exception("not float")

    if x == y == 0:
        raise Exception("0^0 undefined or something")

    return x ** y


def multiply(x, y):
    if type(x) is not float or type(y) is not float:
        raise Exception("not float")
    return x * y


def divide(x, y):
    if type(x) is not float or type(y) is not float:
        raise Exception("not float")
    if y == 0:
        raise Exception("divide by zero error")
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
        raise Exception("unsupported operation type")

    return ops[op](x, y)
