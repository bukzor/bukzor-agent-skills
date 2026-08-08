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
from jsonschema.exceptions import UnknownType
from jsonschema.validators import extend, validates, validator_for
from referencing.jsonschema import SchemaRegistry

from .types import JsonObj, JsonValue

# The llmd dialect's identity. The URI doubles as the fetchable home of the
# meta-schema (served by frontmatter_validate's skill:// retriever). Schemas
# using the extension types below declare it via `$schema:`; a schema with
# no `$schema` gets this dialect by default.
DIALECT_URI = 'skill://llm-kb/jsonschema/dialect.jsonschema.yaml'


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

# extend() rather than create(): create() derives the class's referencing
# specification from the meta-schema's $id, and an unknown $id falls back to
# OPAQUE -- which would break base-URI resolution for file-relative $refs.
# extend() inherits 2020-12's specification; the META_SCHEMA override plus
# validates() then registers the class under the dialect's own URI, so
# validator_for() -- and evolve(), on every $ref crossing -- selects it for
# schemas declaring DIALECT_URI, while schemas declaring a stock dialect get
# that stock validator, honestly: extension types are UnknownType there
# (rendered as a legible schema-bug error in iter_schema_errors).
_KbValidator = extend(Draft202012Validator, type_checker=_TYPE_CHECKER)
_KbValidator.META_SCHEMA = {'$id': DIALECT_URI}
_KbValidator = validates('llmd')(_KbValidator)


def iter_schema_errors(schema: JsonObj, instance: JsonValue, registry: SchemaRegistry) -> list[str]:
    """Validate `instance` against `schema`, one formatted string per violation.

    The schema's `$schema` selects the dialect it is interpreted under:
    DIALECT_URI, any stock JSON Schema dialect, or -- when absent -- the
    llmd dialect. An undeclarable situation (unknown dialect; extension
    types under a stock dialect) is reported as an error, never guessed
    around.
    """
    dialect = schema.get('$schema')
    if dialect is None:
        cls = _KbValidator
    else:
        found = validator_for(schema, default=None)
        if found is None:
            return [f"unknown $schema dialect {dialect!r}: expected {DIALECT_URI} or a standard JSON Schema dialect"]
        cls = found
    validator = cls(schema, registry=registry)
    errors: list[str] = []
    try:
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
    except UnknownType as e:
        errors.append(f"schema bug: type {e.type!r} is not defined in the schema's declared dialect; the llmd extension types (date, instant) require `$schema: {DIALECT_URI}` (or no $schema) in the schema that uses them")
    return errors
