---
why:
  - enable-accountable-deep-work
status: proposal
blocked-on: discussion
trigger: When ≥3 active items clearly share a root cause and the picker would benefit from knowing the coupling.
---

# Themes as First-Class Objects

A **theme** is a coherent problem domain that multiple items address
(e.g., "har-browse," "llm-kb"). Themes have:

- Membership: items tagged with the theme
- Their own state (active/fallow)
- Their own wake conditions and review cadence
- Their own debt computation, independent of member items

Cross-cutting items (touching ≥3 themes) get a **leverage multiplier**
in the picker — productive rabbit holes often improve multiple
themes simultaneously, and this signal is otherwise invisible.

Deferred because: themes are useful when item count grows large
enough that root-cause coupling is real. Premature themes are
overhead. Graduates when the operator notices three items sharing a
common substrate.

## Open questions

The relationship between themes and vitals isn't designed:

- A vital categorizes items by domain (revenue, body, ops). A theme
  groups items by *substrate* (har-browse, llm-kb). Items can belong
  to both — same item is both `vital: tech` and `theme: har-browse`.
  Is this OK or does it produce conflicting signals?
- Does the picker rank by vital-debt or theme-debt first? Both?
  Combined into one number?
- The "cross-cutting leverage multiplier" applies in the picker —
  does it also apply to the rabbit-hole calibration (multi-theme
  postmortems weighted differently)?
- Are themes journal-kind or task-kind? Neither maps cleanly — a
  theme might want its own review cadence independent of either
  vital kind.
- Membership is currently described as "tagged" — single membership
  per item, or multiple (a single item can belong to N themes)?
