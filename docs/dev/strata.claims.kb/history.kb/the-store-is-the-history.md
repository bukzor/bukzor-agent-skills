---
label: LOG
standing: user
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_history.py::test_any_prefix_is_queryable
---

# The Store Is the History

A store is an append-only log -- a word in the free monoid of
updates -- not a mutable current state. "Prior states queryable" is not a feature bolted on:
it is the decision to keep the word rather than only its fold.

A word is linear. Stores that branch hold several, and what their
merge is takes a law this theory does not yet have
(a-merge-needs-a-linearization-law.md).

Everything downstream that speaks of recomputation assumes the word is
still there to recompute from.
