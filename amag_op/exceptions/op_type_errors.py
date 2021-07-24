class CannotDivideByZeroError(ZeroDivisionError):
    def __init__(self):
        self.message = "Cannot divide by zero"

    def __str__(self):
        return self.message


class UndefinedExpoError(ValueError):
    def __init__(self):
        self.message = "0^0 undefined or something"

    def __str__(self):
        return self.message


class UnsupportedOpError(ValueError):
    def __init__(self, op):
        self.message = f"{op} -> Unsupported operation type"

    def __str__(self):
        return self.message
