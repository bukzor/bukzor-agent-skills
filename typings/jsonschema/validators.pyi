from collections.abc import Callable, Iterable, Mapping

from jsonschema import FormatChecker, TypeChecker
from jsonschema.protocols import Validator

def extend(
    validator: type[Validator],
    validators: Mapping[str, object] | Iterable[tuple[str, object]] = ...,
    version: str | None = ...,
    type_checker: TypeChecker | None = ...,
    format_checker: FormatChecker | None = ...,
) -> type[Validator]: ...
def validates(version: str) -> Callable[[type[Validator]], type[Validator]]: ...
def validator_for(
    schema: Mapping[str, object] | bool,
    default: type[Validator] | None = ...,
) -> type[Validator] | None: ...
