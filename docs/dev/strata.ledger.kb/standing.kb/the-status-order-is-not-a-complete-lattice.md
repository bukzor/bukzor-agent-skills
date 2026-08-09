---
label: COMPLETION
standing: user
why:
  - status-is-a-poset-with-a-fibered-top.md
  - evidence-induces-a-monotone-operator.md
  - verdicts-are-assessor-indexed.md
  - ../fixpoint.kb/monotone-operators-have-least-fixpoints.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_two_checkers_certifying_one_entry_crash_the_operator
---

# The Status Order Is Not a Complete Lattice

The fibered top costs KNASTER its license: with no join over
distinct certificates, the status order is not a lattice, and the
evidence operator is not even total -- two checkers certifying one
entry ask for the missing join (the mechanized operator raises
exactly there). The repair is to value entries in the antichain
(downset) completion, which is a complete lattice, restores the
least-fixpoint definition wholesale, and matches reality: an entry
certified by two checkers holds both certificates. The repair is the
assessor law made structural -- the completed value is a map of
verdicts indexed by who issued them. Grade escalation
found it: the prose slid over the gap; the tooling-grade operator
could not.
