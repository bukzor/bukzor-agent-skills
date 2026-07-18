---
why:
  - ../020-goals.kb/runtime-portability.md
---

# Coupling Is Adapter-Only

Runtime-specific nouns — hook event names, SKILL.md frontmatter
fields the base Agent Skills standard doesn't define, `.claude/rules/`
glob semantics, plugin manifest shape — appear only inside a class
package's own delivery-facing content, and only paired with a named
non-Claude-Code fallback. The spec, the engine, and a class's
schema/templates/conventions page name only properties and effects,
never the mechanism that happens to deliver them under the operator's
current tool.

The rule binds titles as much as bodies: a requirement or class entry
whose own *name* encodes a mechanism ("...compiles to hooks") has
already coupled core or class-definition content to a runtime, even
if every sentence below the heading is mechanism-neutral. Name the
effect; let the adapter-facing content, wherever it lives, name the
mechanism.

Checkable: grep every mission-through-design entry's title and body,
outside `delivery-boundary.md` and a class package's own
delivery-facing files, for Claude-Code-specific terms; any hit is a
defect.
