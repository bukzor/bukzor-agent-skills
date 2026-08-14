---
label: REWIRE
standing: agent
why:
  - evidence-induces-a-monotone-operator.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_an_unwarranted_reference_still_gates_ascent
---

# A Warrant Row Is Conjunctive

An ascent rule grants only when every premise clears the threshold,
so within a row support is conjunctive: one failed premise kills the
grant, and no strengthening of the others compensates. Across rows
support is disjunctive -- any satisfied row grants. Repair of lost
standing is therefore rewiring, not adding: replace the failed
premise or file a new row; piling further evidence into a dead row is
spend without effect, and piling it onto the entry itself does not
touch the row at all.
