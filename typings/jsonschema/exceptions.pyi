from collections.abc import Iterable

class ValidationError(Exception):
    message: str
    absolute_path: Iterable[str | int]
