---
label: DESCEND
standing: agent
why:
  - ../reference.kb/key-valued-fields-present-a-quiver.md
  - ../reference.kb/reachability-is-a-least-fixpoint.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "presupposition_cycle"
---

# Presupposition Is a Well-Founded Edge Relation

Presupposition is a second edge relation over the same claims -- a
quiver, not a status, not a verdict, and not something an act
asserts. It is well-founded: no claim is reachable from itself along
it, however far around.

A cycle is rejected rather than resolved. Admit one and defeating
either end moots both, so the acts that seeded the collapse land on a
claim that absorbs them -- a defeat that erases its own evidence, and
an answer with no reading. There is no repair at the fixpoint either:
the collapse is monotone in its seed, so any cycle it touches it
takes whole. What a cycle really reports is a modelling error at the
site, and the cheapest place to say so is the entry.

The declined alternative is to let the collapse close over cycles
quietly, as any reachability computation would. That answers, but the
answer is unreadable in exactly the case the reader most needs it,
and it converts a locatable error into a silently wrong standing.

Where the relation comes from is a separate question, and open: the
engine takes it alongside the record rather than out of it, so no
reader's stance bears on it and no act can raise or strike one. That
sits badly with acts being the only way anything enters the base, and
is the next thing to rule here.
