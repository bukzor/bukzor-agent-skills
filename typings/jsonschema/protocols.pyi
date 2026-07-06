from collections.abc import Iterable, Mapping
from typing import ClassVar, Protocol

from jsonschema import FormatChecker, TypeChecker
from jsonschema.exceptions import ValidationError
from referencing.jsonschema import SchemaRegistry

class Validator(Protocol):
    TYPE_CHECKER: ClassVar[TypeChecker]
    FORMAT_CHECKER: ClassVar[FormatChecker]

    def __init__(
        self,
        schema: Mapping[str, object] | bool,
        format_checker: FormatChecker | None = ...,
        *,
        registry: SchemaRegistry = ...,
    ) -> None: ...
    def iter_errors(self, instance: object) -> Iterable[ValidationError]: ...
    def evolve(self, **kwargs: object) -> Validator: ...
