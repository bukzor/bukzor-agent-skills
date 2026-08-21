---
label: RETENTION
standing: agent
why:
  - ../protocol.kb/enforcement-grade-is-who-computes-the-product.md
  - ../protocol.kb/the-floor-is-the-semantics.md
  - ../protocol.kb/a-trigger-bank-is-a-monitor.md
  - ../tower.kb/what-remains-to-prove.md
---

# How Does a Property Survive a Redesign?

As wrestled (the Lean-vs-Agda question, and behind it every "good
idea" that quietly cost something): by what mechanism does a property
I care about survive a restructuring I will not re-verify by hand?

Settled: it survives iff it is a law with a computer -- attention,
tooling, or kernel -- and a change's blast radius is the set of
`verify:` commands it breaks. The floor is the semantics: an unbound
law is at base strength, not broken, so partial formalization is the
steady state rather than a lapse. Demonstrated on this ledger itself:
escalating from attention to tooling grade found COMPLETION and the
missing premise in FREE_CONSERVE. Residue: the kernel rung,
OBLIGATION.
