---
label: LAZY_MARKER
standing: agent
verdict: dissolved
why:
  - while-exists-to-make-set-vs-namespace-path-decidable.md
---

# A Lazy/Eager Marker on Directories

Two drafts marked which directories the listing should stop at: a
stem-sibling trigger file beside the directory, and a `.kb` suffix.
Dissolved: the juncture is the marker. A directory under `while/` is
lazy because it is a set; every other directory is eager because it is
a prefix. Nothing further needs spelling.
