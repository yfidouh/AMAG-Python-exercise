class NotFloatError(FloatingPointError):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"{self.arg} is not a float"
