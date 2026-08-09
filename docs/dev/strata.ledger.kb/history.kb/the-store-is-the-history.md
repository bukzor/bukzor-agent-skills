---
label: WORD
standing: agent
---

# The Store Is the History

A store is a word in the free monoid of updates -- a DAG of
transactions where branching is allowed -- not a mutable current
state. "Prior states queryable" is not a feature bolted on: it is the
decision to keep the word rather than only its fold.

Everything downstream that speaks of recomputation assumes the word is
still there to recompute from.
