---
why:
  - ../010-mission.md
---

# Single-Source Improvement

Every shared behavior and every shared definition has exactly one
home; improvements land there and propagate everywhere for free.

V1's counter-examples show the cost: one definition duplicated
verbatim across three files, a promotion procedure restated in two,
the dated-record convention reinvented six times, eight `bin/`
scripts sharing bugs. Behavior expressed as prose must be re-taught
per document; behavior expressed as code or schema improves in one
place. The corollary goal: minimize the *named surface area* —
every name is an API, and renames half-land.
