class BaseError(Exception):
    _message = "An error occurred"

    def __init__(self, message: str | None = None):
        self.message = message or self._message
        super().__init__(self.message)
