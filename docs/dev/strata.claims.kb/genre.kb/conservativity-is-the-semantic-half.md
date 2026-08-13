---
label: CONSERVE
standing: user
why:
  - ../standing.kb/standing-is-computed-not-stored.md
  - ../purpose.kb/the-corpus-outgrows-any-reader.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_genre.py::test_a_confined_extension_conserves_core_standing
---

# Conservativity Is the Semantic Half

Conservativity is a statement about computed standing: standing
computed in an extension, restricted to a prior theory's entries,
equals standing computed in the prior alone. Extension adds claims;
it never changes what was already settled below. Where it appears to,
the prior was wrong and is fixed there -- the law localizes the
defect, which is its operational value. At unbounded scale the law
is not taste: localization is what keeps the unit of review bounded
while the corpus is not.
