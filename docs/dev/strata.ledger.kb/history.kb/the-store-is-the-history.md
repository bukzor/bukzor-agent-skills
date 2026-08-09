---
label: WORD
standing: agent
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_history.py::test_any_prefix_is_queryable
---

# The Store Is the History

A store is a word in the free monoid of updates -- a DAG of
transactions where branching is allowed -- not a mutable current
state. "Prior states queryable" is not a feature bolted on: it is the
decision to keep the word rather than only its fold.

Everything downstream that speaks of recomputation assumes the word is
still there to recompute from.
