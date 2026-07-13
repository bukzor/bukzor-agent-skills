---
why:
  - ../020-goals.kb/mechanism-over-exhortation.md
---

# Action Triggers Are Enforced Deterministically

Every trigger of the shape "before/after \<detectable action\>" is
enforced by whatever deterministic gating or context-injection
mechanism the active runtime provides — matched on the action itself,
delivered without depending on the model choosing to consult a file.
The requirement names the effect, not the mechanism: under Claude
Code that mechanism is hooks (see
`../040-design.kb/hook-wiring.md`, the Claude Code adapter of
`../040-design.kb/delivery-contract.md`); under a different runtime
it is that runtime's own interception point. See
`coupling-is-layer-3-only.md` for the general rule this entry's title
and body both hold to.

Checkable: enumerate the trigger genre; every action-shaped entry has
enforcement wiring in *some* adapter, and the prose copy exists only
as that wiring's payload — never as a freestanding exhortation the
model must remember unprompted.
