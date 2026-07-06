from collections.abc import Iterable, Mapping

from jsonschema import FormatChecker, TypeChecker
from jsonschema.protocols import Validator

def extend(
    validator: type[Validator],
    validators: Mapping[str, object] | Iterable[tuple[str, object]] = ...,
    version: str | None = ...,
    type_checker: TypeChecker | None = ...,
    format_checker: FormatChecker | None = ...,
) -> type[Validator]: ...
