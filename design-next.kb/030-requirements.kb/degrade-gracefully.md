---
why:
  - ../020-goals.kb/native-first.md
  - ../020-goals.kb/runtime-portability.md
---

# Degrade Gracefully

The system stays functional when a platform primitive churns,
regresses, or disappears. Native mechanisms carry the load
(paths-gated activation, hook injection), but each has a declared
fallback: description-based skill activation, prose trigger banks,
manually invoked validators.

The same requirement covers a larger event than in-place churn: the
operator adopting a different runtime entirely. A declared fallback
that survives a version bump should also be the first thing a new
runtime's adapter implements.

Checkable: for each native primitive the design depends on, the
design names its fallback and the fallback is exercised (not
bit-rotted). The platform's extension surface is churning quarterly;
depending on it without fallbacks trades one fragility (prose decay)
for another (feature churn).
