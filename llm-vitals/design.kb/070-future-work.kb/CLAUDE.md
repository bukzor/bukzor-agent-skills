--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Future Work Layer

Ideas worth remembering but not yet ready to act on. Each entry has
an explicit **trigger** — the condition under which it graduates
back into the active design.

## What Belongs Here

- Deferred design ideas with a stated trigger condition
- Promising but un-validated mechanisms
- Features that require accumulated data the system doesn't yet have

## What Does NOT Belong Here

- Currently-active design (those live in `040-design.kb/`)
- Speculation without an articulated trigger (write the trigger or
  don't record it)
- Implementation TODOs (those live with the code, not the design)

## Frontmatter

Each entry carries:

- `why:` — slugs from earlier layers explaining motivation
- `trigger:` — a one-line condition for promoting this idea

When an idea's trigger fires, promote the entry to its appropriate
layer (usually `040-design.kb/`) and delete it from here.

## When to Add / Read

- **Add** when an idea is worth recording but premature, with a
  stated trigger condition for revisiting.
- **Read** when reviewing whether any deferred ideas have become
  ready (trigger fired) and when checking that a proposed feature
  isn't already deferred here.
