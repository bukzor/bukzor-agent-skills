--- # workaround: anthropics/claude-code#13003
depends:
    - Skill(llm-design-kb)
---

# Design Layer — Architectural Primitives

Entries describe *what the system is* — the core architectural
concepts that realize the requirements in `030-requirements.kb/`.

## What Belongs Here

- Core primitives (vital, two-tier SLO, debt, status)
- Cross-cutting design decisions (vital kinds, repo split, vocabulary)
- Architectural mechanisms (error budgets, burn rate, status coloring)

## What Does NOT Belong Here

- Component-level implementation (file formats, CLI signatures) — those
  live in `050-components.kb/`
- Phased build plans — those live in `060-deliverables.kb/`
- Deferred ideas — those live in `070-future-work.kb/`

## Frontmatter

Entries carry `why:` linking to motivating items in
`030-requirements.kb/` (most common), or higher layers when appropriate.

Optional `status:` field (default `accepted`) tracks decision lifecycle:

- **idea**: raw thought; possibly to be discarded
- **proposal**: worked out enough to engage with; under consideration
- **accepted** (default; omit field): decided; treat as ground truth
- **rejected**: considered and not adopted; kept for visible alternatives
- **superseded**: replaced by another entry; carries `superseded-by:` slug

Optional `blocked-on:` for `idea` / `proposal` entries:

- **discussion**: human deliberation hasn't resolved
- **information**: external facts missing (research, data, prior art)

Body length is governed by **information available**, not by status —
a `proposal` can be exhaustively researched (long body) while still
undecided. `bloat` audit handles length; status governs decision state
separately.

## When to Add / Read

- **Add** when an architectural primitive, mechanism, or boundary
  decision is established that's not already documented.
- **Read** before implementing components, extending the design, or
  triaging whether a new idea belongs here or in `070-future-work.kb/`.
