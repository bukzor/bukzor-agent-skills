---
label: STATUS
standing: user
why:
  - verdicts-are-assessor-indexed.md
verify: uv --directory docs/dev/design-incubators/engine_tower run pytest tests/test_standing.py -k "status_chain or fibered_top"
---

# Status Is a Poset with a Fibered Top

The status order is described ⊑ stipulated ⊑ obligated ⊑
certified(checker) -- a chain whose top splits into one incomparable
point per checker. The order tracks verification commitment, not
resolvedness: certified under one checker is not above certified
under another, and there is no join pretending otherwise.

The rungs are a contingent quotient: the underlying commitment space
is continuous, and this four-point cut is chosen for legibility at
attention grade -- greppable, small enough to hold in mind. What is
not contingent is the shape the assessor law forces: statuses
ordered by commitment force, the top fibered per assessor. Re-cut
the quotient when usage demands; un-fibering the top is not on
offer.
