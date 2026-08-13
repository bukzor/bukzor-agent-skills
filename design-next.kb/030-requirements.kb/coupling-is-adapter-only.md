---
why:
  - ../020-goals.kb/runtime-portability.md
---

# Coupling Is Adapter-Only

Runtime-specific nouns — hook event names, SKILL.md frontmatter
fields the base Agent Skills standard doesn't define, `.claude/rules/`
glob semantics, plugin manifest shape — appear only inside a class
package's own delivery-facing content, or inside a clearly demarcated
mechanism subsection of a core/class entry (headed, e.g., **Claude
Code mechanism.**, with the runtime-neutral property it implements
stated first — see `memory-policy.md`), and only paired with a named
non-Claude-Code fallback. Outside those two shapes, the spec, the
engine, and a class's schema/templates/conventions page name only
properties and effects, never the mechanism that happens to deliver
them under the operator's current tool.

The rule binds titles as much as bodies: a requirement or class entry
whose own *name* encodes a mechanism ("...compiles to hooks") has
already coupled core or class-definition content to a runtime, even
if every sentence below the heading is mechanism-neutral. Name the
effect; let the adapter-facing content, wherever it lives, name the
mechanism.

Checkable: grep every mission-through-design entry's *normative*
claims — a property the system must have, a rule an implementation
must follow — for Claude-Code-specific terms; any hit outside
`delivery-boundary.md`, a class package's own delivery-facing files,
or a demarcated mechanism subsection is a defect. Naming today's
runtime primitives as motivation, or as an illustrative aside that
isn't itself the requirement, doesn't count — the defect is a
property or design claim that only holds under one runtime.
