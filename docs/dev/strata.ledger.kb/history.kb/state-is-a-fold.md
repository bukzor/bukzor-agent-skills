---
label: FOLD
standing: agent
why:
  - the-store-is-the-history.md
---

# State Is a Fold

Current state is the image of the history under the unique
structure-preserving map from histories to key-to-payload maps under
override -- last writer wins per key. State is therefore *derived*,
never authoritative: two replicas agreeing on the word agree on the
state for free, and any disagreement about state is a disagreement
about the word.
