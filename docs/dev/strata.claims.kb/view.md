---
label: VIEW
standing: agent
why:
  - history.md
  - purpose.md
ontology:
  - view
  - cache
  - derivative
  - refresh
  - recompute
  - staleness
  - debt
  - drift
  - stamp
  - reader
  - diff
stale-when: a reader that can afford to recompute every read -- then caches, and everything priced here, vanish
---

# View

Auxiliary theory: derived values over a store. Exists so `standing`
and `protocol` can lean on one account of caches, refresh, and
staleness instead of each carrying their own.
