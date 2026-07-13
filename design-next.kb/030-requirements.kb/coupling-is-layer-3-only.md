---
why:
  - ../020-goals.kb/runtime-portability.md
---

# Coupling Is Layer-3-Only

Runtime-specific nouns — hook event names, SKILL.md frontmatter
fields the base Agent Skills standard doesn't define, `.claude/rules/`
glob semantics, plugin manifest shape — appear only in layer-3
(delivery) entries, and only paired with a named non-Claude-Code
adapter or fallback. Layers 0–2 (spec, engine, genres) name properties
and effects, never the mechanism that happens to deliver them under
the operator's current tool.

The rule binds titles as much as bodies: a requirement or genre entry
whose own *name* encodes a mechanism ("...compiles to hooks") has
already coupled layer 0/2 to layer 3, even if every sentence below
the heading is mechanism-neutral. Name the effect; let the adapter
entry name the mechanism.

Checkable: grep every mission-through-design entry's title and body,
outside `delivery-contract.md`, `plugin-delivery.md`, `hook-wiring.md`,
and `thin-skills.md`, for Claude-Code-specific terms; any hit is a
defect.
