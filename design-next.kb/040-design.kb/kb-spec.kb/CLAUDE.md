--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# kb-spec.kb — maintenance guide

Long-form definitions of spec elements, elaborating `../kb-spec.md`
(this collection's synthesis).

## What belongs here

One spec element per file, named for the element, holding the
long-form definition its `kb-spec.md` bullet can't fit.

## What does NOT belong here

- Elements whose bullet still says everything — no file until the
  bullet overflows
- Procedures, behavior, teaching — the spec defines formats only

## When to add / read

- **Add** when an element's definition outgrows its bullet in
  `../kb-spec.md`.
- **Read** when implementing or auditing against an element whose
  bullet doesn't answer the question.
