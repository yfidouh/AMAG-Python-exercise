class FileTypeError(Exception):
    def __init__(
        self, ext, message="file type is not a csv or excel (.xlsx, .xls) type"
    ):
        self.ext = ext
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ext} -> {self.message}"


class FileDoesNotExistError(Exception):
    def __init__(self, fname, message="File does not exist"):
        self.fname = fname
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.fname} -> {self.message}"
