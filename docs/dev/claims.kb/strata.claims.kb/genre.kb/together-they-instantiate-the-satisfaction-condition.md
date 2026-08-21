---
label: SATISFACTION
standing: agent
authority: "Goguen & Burstall, institutions -- the satisfaction condition"
why:
  - confinement-is-the-syntactic-half.md
  - conservativity-is-the-semantic-half.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_genre.py
---

# Together They Instantiate the Satisfaction Condition

Confinement and conservativity are the two halves of one discipline:
whether a claim holds does not depend on how much surrounding
vocabulary you can see. That is what an institution's defining axiom
asks -- satisfaction invariant under translation and reduct -- and
these two instantiate its preconditions here: confinement gives every
claim a home signature to be carried from, conservativity is that
invariance where this ledger can check it.

Calling them *the* satisfaction condition would overstate:
conservativity is a further property, and one that can fail in an
institution. What they buy is real anyway -- "the same theory,
carried across signatures" becomes a phrase with content, and
confinement stops being hygiene and starts being load-bearing.
