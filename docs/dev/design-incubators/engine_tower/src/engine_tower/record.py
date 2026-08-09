"""record -- schemas, typing, migration as transport.

Schemas + migrations form a category; instances sit fibered over it.
Validation is a typing judgment I |= Sigma; a migration acts on
instances as the pushforward (opcartesian lift).  [TYPING, MIGRATE]
"""

from collections.abc import Callable
from dataclasses import dataclass

from engine_tower.history import Payload


@dataclass(frozen=True)
class Schema:
    name: str
    fields: frozenset[str]  # required field names
    ref_fields: frozenset[str] = frozenset()  # values are keys (reference reads these)


def validates(payload: Payload, schema: Schema) -> bool:
    """The typing judgment  payload |= schema.  [TYPING]"""
    return schema.fields <= payload.keys()


@dataclass(frozen=True)
class Migration:
    """An arrow Sigma -> Sigma' with its action on instances.

    The opcartesian-lift law, in checkable form: push must carry
    payloads validating against source to payloads validating against
    target.  A rename is an isomorphism (push has an inverse).
    [MIGRATE]"""

    source: Schema
    target: Schema
    push: Callable[[Payload], Payload]
