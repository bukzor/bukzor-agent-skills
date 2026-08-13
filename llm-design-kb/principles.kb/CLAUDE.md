--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-kb)
---

# Principles Layer — Design Authorship

Reusable rules for *writing* design.kb content well, distilled from
practice across projects. Distinct from a project's own
`020-goals.kb/`/`030-requirements.kb/`: those state what a specific
system must do; these state how any design tower should be authored.

## What Belongs Here

- A rule about authoring design.kb entries that generalizes beyond
  any one project's tower
- One principle per file, kebab-case, descriptive of the rule itself

## What Does NOT Belong Here

- Project-specific goals/requirements/design — those live in that
  project's own design.kb layers
- Historical narrative of how a principle was discovered — an ADR
  or devlog's job, not this collection's

## When to Add / Read

- **Add** when a design-authoring lesson recurs across two or more
  projects, or is general enough to state once for all future ones.
- **Read** before or during any design.kb authoring session, and
  when reviewing an existing tower for authoring-quality issues (as
  opposed to content correctness).
