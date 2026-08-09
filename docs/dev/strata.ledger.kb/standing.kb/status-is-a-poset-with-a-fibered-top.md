---
label: STATUS
standing: agent
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py::test_the_fibered_top_has_no_join
---

# Status Is a Poset with a Fibered Top

The status order is described ⊑ stipulated ⊑ obligated ⊑
certified(checker) -- a chain whose top splits into one incomparable
point per checker. The order tracks verification commitment, not
resolvedness: certified under one checker is not above certified
under another, and there is no join pretending otherwise.
