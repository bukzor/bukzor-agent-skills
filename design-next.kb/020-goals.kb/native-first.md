---
why:
  - ../010-mission.md
---

# Native First

Prefer platform primitives and adopted open standards over bespoke
inventions. A hand-rolled mechanism is justified only where no native
primitive exists — and it should be shaped for later replacement by
one.

V1 evidence on both sides: the must-read bank was a hand-rolled soft
hook system built before hooks could inject context (now they can);
the `skill://` URI bet anchored to a standard that stalled unmerged.
Bespoke inventions carry permanent maintenance and teaching costs;
native primitives are maintained, documented, and enforced by the
platform.

This governs mechanism choice within a given runtime, not which
runtime to depend on — see `runtime-portability.md` for the companion
goal and `../030-requirements.kb/coupling-is-adapter-only.md` for how
the two compose without conflict.
