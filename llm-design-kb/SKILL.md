---
name: llm-design-kb
description: "Agent MUST load for design.kb/ directories and layered design documentation"
---
--- # workaround: anthropics/claude-code#13005
setup: |
    All projects that depend on this skill should have as `CLAUDE.md` frontmatter:

    ```yaml
    --- # workaround: anthropics/claude-code#13003
    depends:
        - Skill(llm-design-kb)
    ```
---

# Design Knowledge Bases

Layered design documentation using `.kb/` collections. Each layer justifies
the one below and realizes the one above, linked via `why:` frontmatter.

## Layers

Each layer answers a question that motivates the layer below:

| Layer | Answers | Motivates |
|---|---|---|
| `010-mission.kb/` | What problem are we solving? Who benefits? | goals |
| `020-goals.kb/` | How do we accomplish the mission? | requirements |
| `030-requirements.kb/` | How do we validate goals are achieved? | design |
| `040-design.kb/` | How do we satisfy requirements? | components |
| `050-components.kb/` | How do we implement the design? | deliverables |
| `060-deliverables.kb/` | How do we build the components? | — |
| `070-future-work.kb/` | What ideas are deferred? | — |

All layers are optional. Create as needed.

Auxiliary collections that don't occupy a why/how rung -- content
relevant to the design but not itself motivated-by/motivating a
numbered layer -- get an unnumbered `.kb/` (e.g. `use-cases.kb/`,
`background.kb/`). Only number a collection if it actually sits in the
why/how chain (something's `why:` points at it, and its own `why:`
points at the layer above).

`070-future-work.kb/` captures ideas worth remembering but not worth pursuing
now.

Entries link via `why:` frontmatter to their motivation — usually a
higher layer (e.g. a requirement lists the goals it serves), or a
same-layer entry when the motivating concept naturally lives at the
same layer and promoting it would introduce hierarchy with no other
content.

```yaml
---
why:
  - site-agnostic-capture
---
```

## Alternatives Considered

Design entries often surface the options weighed at decision time. Three
shapes, in order of growth:

- **Inline "Why not X".** Short bolded-phrase paragraphs under the chosen
  approach. Works for 1-3 alternatives with brief rationale.
- **Parallel list.** A numbered or tabled enumeration of alternatives, with
  selection stated outside the listing (or in a sibling entry). Works for
  design-space surveys where several options stay on the table.
- **Sub-kb.** When alternatives accrue per-item content, metadata, or
  lifecycle, promote the entry to a `.kb/` per `Skill(llm-kb)` promotion
  signals. Each alternative becomes its own file; selection can live in
  entry frontmatter or be called out in the sub-kb's CLAUDE.md / summary file.

Forward-facing: the design entry describes what the system *is*. Alternatives
are a footnote on the design space, not a historical log. If extensive
rationale or historicity matters, write an ADR instead
(see `Skill(llm-collab)`).

## Maintenance

After any session that changes code or design understanding in a project with
`design.kb/`:

1. **Find affected docs.** Which design.kb files relate to what changed this
   session? Read each one.
2. **Check claims against ground truth.** Look for stale assertions — things
   that were true when written but no longer are.
3. **Capture new concepts.** Did discussion surface goals, requirements, or
   components that aren't documented? Create entries in the appropriate
   collection.
4. **Trace `why:` chains.** New docs need `why:` frontmatter pointing to their
   motivation. Existing docs that gain new responsibilities need updated `why:`
   references. Follow chains to verify they connect back to goals/mission.
5. **Fix, don't flag.** Rectify stale docs directly. Only ask the user when
   the correction requires a design decision.
6. **Promote listing entries.** An entry with a plural filename or
   listing-heavy content (e.g. `patterns.md`, `alternatives.md`) wants to
   become a sub-`.kb/`. See `Skill(llm-kb)` promotion signals.

## References

- `references/how-to-document-design-knowledge.md` — Full creation guidance,
  relationship to ADRs/devlogs/CLAUDE.md, background.kb and technical-policy.kb
