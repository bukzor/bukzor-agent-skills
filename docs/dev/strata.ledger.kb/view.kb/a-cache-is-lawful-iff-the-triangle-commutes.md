---
label: TRIANGLE
standing: agent
why:
  - ../history.kb/state-is-a-fold.md
---

# A Cache Is Lawful iff the Triangle Commutes

A view is a function of state. A written-down copy of a view's value
is lawful exactly when it equals the view applied to the fold of the
current history -- the triangle (history, state, cached value)
commutes. Drift is the name of its failure, and is a property of the
cache, not of the underlying data.

Consequence: a stored summary is never a second source of truth; it
is a proposition about the store, currently true or currently false.
