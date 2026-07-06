"""Typed boundary around `jsonschema`, which ships no `py.typed` marker.

Without one, pyright falls back to a bundled (and, for this API, stale)
community stub, surfacing Unknown/Any almost everywhere `jsonschema` is
touched. The fix lives at `typings/jsonschema/` (repo root): a small local
stub package -- covering only the handful of names this module uses --
that takes precedence over the bundled one. This module is the only place
that imports `jsonschema` directly; everything it exports is fully typed
as a result, so nothing outside it ever sees an Unknown propagate in.
"""

import datetime

from jsonschema import Draft202012Validator, TypeChecker
from jsonschema.validators import extend
from referencing.jsonschema import SchemaRegistry

from .types import JsonObj, JsonValue


def _is_date(_checker: TypeChecker, instance: object) -> bool:
    return isinstance(instance, datetime.date) and not isinstance(instance, datetime.datetime)


def _is_instant(_checker: TypeChecker, instance: object) -> bool:
    return isinstance(instance, datetime.datetime) and instance.tzinfo is not None


# YAML emits datetime.date and datetime.datetime natively; JSON Schema has no
# matching types. `date` accepts a calendar day; `instant` accepts a tz-aware
# point in time. Naive datetime is intentionally unaccepted -- pick one.
_TYPE_CHECKER = Draft202012Validator.TYPE_CHECKER.redefine_many({
    "date": _is_date,
    "instant": _is_instant,
})

_KbValidator = extend(Draft202012Validator, type_checker=_TYPE_CHECKER)


def iter_schema_errors(schema: JsonObj, instance: JsonValue, registry: SchemaRegistry) -> list[str]:
    """Validate `instance` against `schema`, one formatted string per violation."""
    validator = _KbValidator(schema, registry=registry)
    errors: list[str] = []
    for error in validator.iter_errors(instance):
        path_parts: list[str] = []
        for p in error.absolute_path:
            if isinstance(p, int):
                path_parts.append(f"[{p}]")
            else:
                path_parts.append(f".{p}" if path_parts else str(p))
        path = "".join(path_parts)
        prefix = f"{path}: " if path else ""
        errors.append(f"{prefix}{error.message}")
    return errors
