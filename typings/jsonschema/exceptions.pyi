from collections.abc import Iterable

class ValidationError(Exception):
    message: str
    absolute_path: Iterable[str | int]

class UnknownType(Exception):
    type: object
    instance: object
    schema: object
