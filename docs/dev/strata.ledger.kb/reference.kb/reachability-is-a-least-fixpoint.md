---
label: REACH
standing: bare
why:
  - key-valued-fields-present-a-quiver.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
---

# Reachability Is a Least Fixpoint

The reachability preorder over the quiver is the least fixpoint of
X -> id ∪ E ∪ X;X. Dependency cones are up-sets in this preorder;
"what rests on this" and "what this rests on" are the two directions
of one relation.

Every dependency question downstream -- taint, trust bases,
motivation chains reaching a root -- is order theory over this
preorder, not a new mechanism.
