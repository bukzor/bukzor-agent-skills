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

Entries link via `why:` frontmatter to their motivation — a list of
file-relative path references, usually to a higher layer (e.g. a
requirement lists the goals it serves), or to a same-layer entry when
the motivating concept naturally lives at the same layer and promoting
it would introduce hierarchy with no other content.

```yaml
---
why:
  - ../020-goals.kb/site-agnostic-capture.md
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
  entry frontmatter or be called out in the sub-kb's CLAUDE.md / synthesis file.

Forward-facing: the design entry describes what the system *is*. Alternatives
are a footnote on the design space, not a historical log. If extensive
rationale or historicity matters, write an ADR instead
(see `Skill(llm-collab)`).

## Doc-Driven Development

Design docs lead implementation as often as they trail it -- writing the doc
first is cheaper, higher-level, and easier to review than tests are under TDD.
A behavior-describing doc therefore carries two kinds of prose, demarcated:

- **Undecorated prose is descriptive** -- shipped, verifiable behavior. A
  mismatch with ground truth is a doc bug: fix it.
- **`> [!TODO]` blocks are normative** -- decided behavior not yet
  implemented. A mismatch with ground truth is the point: implement toward it,
  never "correct" it to match the code.
- **`> [!QUESTION]` blocks are open** -- undecided behavior or design. Never
  implement one: an agent that builds an open question has shipped an
  unratified guess.

Both markers take a one-line title after the bracket -- a reminder at
checkbox-line grain, so a bare grep reads like a todo list:

```markdown
> [!TODO] island rule becomes `***`
> The island rule is `***`; lands with a `divider()` change plus
> regenerated goldens.

> [!QUESTION] is the island rule `***` or `---`?
> Pandoc accepts both; settles on checking what our other renderers
> accept.
```

Write a decided block as declarative future-state prose ("The rule is X"),
not an imperative task ("Switch to X"): landing it is then pure markup
removal — the prose is already the descriptive sentence. Write a question's
body to name what would settle it (operator ratification, prototype
evidence, prior art); it resolves by marker swap to a decided `[!TODO]`,
directly to descriptive prose, or by deletion.

The markers are Obsidian-callout-shaped (prior art: Obsidian's built-in
`[!todo]` and `[!question]` types); GitHub renders them as plain blockquotes
containing the literal bracket text -- acceptable, since browsers are a
tertiary consumer and the fallback is legible. Grep `[!TODO]` to enumerate a
doc's unimplemented surface, `[!QUESTION]` its undecided surface. The
terminal state of both is unmarked prose: when behavior lands or a question
settles, remove the callout markup (or the whole block, if surrounding prose
already says it). There is no `[!DONE]` or `[!ANSWER]` -- markers flag
deviation from ground truth, and a closed item's record is git.

Layers 010-030 are aspirational by nature and need no marker; the convention
applies where prose could be mistaken for a claim about current behavior
(040 and below, technical-policy, contract docs).

## Maintenance

After any session that changes code or design understanding in a project with
`design.kb/`:

1. **Find affected docs.** Which design.kb files relate to what changed this
   session? Read each one.
2. **Check claims against ground truth.** Look for stale assertions — things
   that were true when written but no longer are. `> [!TODO]` and
   `> [!QUESTION]` blocks are normative/open, never stale; instead, unwrap
   any TODO whose behavior landed this session, and resolve any QUESTION
   that settled.
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
- `principles.kb/` — reusable rules for authoring design.kb content
  well, distinct from any one project's own goals/requirements. Read
  before or during a design.kb authoring session.
