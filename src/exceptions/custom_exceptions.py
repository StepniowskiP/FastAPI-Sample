
class ValidationError(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return repr(self.message)
