---
label: FOLD
standing: agent
why:
  - the-store-is-the-history.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_history.py::test_state_is_a_monoid_action
---

# State Is a Fold

Current state is the image of the history under the unique
structure-preserving map from histories to key-to-payload maps under
override -- last writer wins per key. State is therefore *derived*,
never authoritative: two stores holding the same word agree on the
state for free, and any disagreement about state is a disagreement
about the word.
