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

Where the relation comes from is a separate question, ruled at
[EDGE]: each edge is a claim, so the graph well-foundedness is asked
of is the one a reader upholds, not the one on offer. Cycles are
therefore reader-relative too -- and a reader who has defeated an
edge has nothing left to reject.
