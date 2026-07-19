---
why:
  - ../010-mission.md
  - ../../../design-next.kb/030-requirements.kb/degrade-gracefully.md
---

# The Floor

The floor is the subsystem's base delivery mechanism, present on
every consumer: a filename-indexed bank (`bank-format.md`) scanned
during planning — the listing is the index; bodies load only when a
trigger matches. It requires zero runtime support: no interception,
no interpreter, no install step beyond the host context naming the
bank.

The floor is not a fallback; it is the semantics. Every trigger means
what its floor reading says, on every consumer, always. Mechanical
enforcement (`interpretation-not-compilation.md`) strengthens
delivery of that same meaning where a runtime can detect the
condition — it never replaces or reinterprets it, and the scan
continues even on consumers whose every condition is also bound
(defense in depth).

**Why not "fallback":** a fallback engages on failure; the floor is
engaged continuously and carries the meaning that stronger delivery
merely enforces. The nearest prior term, degrade-gracefully's
"declared fallback", under-states that always-on role.
