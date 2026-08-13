---
label: STRATA
standing: agent
why:
  - ../genre.kb/confinement-is-the-syntactic-half.md
  - ../genre.kb/conservativity-is-the-semantic-half.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_tower.py::test_imports_respect_the_poset
---

# The Engine Tower Is a Theory Poset

The engine strata obey the genre laws themselves: each stratum's
definitions use only the vocabulary of strata at or below it
(confinement), and each added stratum changes nothing about lower
semantics -- typing adds no history, standing invalidates no typing,
genres rewrite no standing (conservativity). The tower is a poset of
conservative extensions, the very structure it hosts at the genre
stratum.
