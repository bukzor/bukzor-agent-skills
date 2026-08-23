---
managed-by: Skill(llm-subtask)
status: open
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
required-reading:
  - ~/.claude/skills/llm-kb/references/schema-reuse.md
cost-benefit-sweh:
  timebox:
    "@value": 6.0
    rationale: |
      13 of the 20 are mechanical: read the members' frontmatter, write a
      `$ref` stub or a small canonical. The `private.bukzor-llc` eight are
      business data rather than kb metadata and want real design; the
      `.prms` two want a dialect decision. Past 6h, what is left is the
      bukzor-llc design, which deserves its own entry.
    confidence: unsure
  benefit-2w:
    "@value": 1.5
    rationale: |
      20 collections currently catch no drift at all. Each stub also
      subjects its collection to validation for the first time -- the
      `scratch.vim-work` precedent is that this surfaces real conformance
      work behind it, which is benefit, not cost.
    confidence: confident
  cost-of-delay-2w:
    "@value": 0.25
    rationale: |
      Every one of these has been a gap for months; nothing regressed.
      Drift accrues only as fast as those collections are edited.
    confidence: confident
---

# Close the 20 remaining schema gaps

**Priority:** Medium -- real gaps, but every one of them has been a gap
for months; nothing regressed.
**Complexity:** Medium. Mechanical for the `$ref`-stub cases, genuine
design work for `private.bukzor-llc` and the `.prms` corpus.
**Context:** 2026-08-22/23 schema survey, itself the residual of the
2026-08-21 `$ref` rollout. A sub-agent asked to add schemas where
collections lacked them instead regenerated ~278 files across 18 repos,
overwriting 254 hand-written canonicals. All of it is reverted and the
history is erased. The *finding* was real; only the execution was not --
which is why the Delegation section below is written as prohibitions.

## Problem Statement

22 collections carry frontmatter under no schema, so `llm.kb-validate`
reports them and no drift is caught in any of them. Two are now closed
(`cros-claude-code-keepawake`, `~/.claude/claude-alignment-2026-04-29`);
20 remain.

## Current Situation

The live list is `trash/schema-gaps/missing-schemas.txt`, regenerable:

```sh
while read -r d; do (cd "$d" && llm.kb-validate . 2>&1) \
  | grep -oP 'No schema found: \K\S+' | sed "s|^|$d/|"; done \
  < /tmp/bukzor-repos.list | sort -u
```

| repo | n | shape |
| --- | --- | --- |
| `private.bukzor-llc` | 8 | constitution / playbook / strategy -- needs real design |
| `prototype.personal-reasoning-management` | 2 | `*.prms` corpus, its own dialect |
| `prototype.hearts-2025` | 2 | `docs/milestones`, `docs/rules` |
| `~/.claude` | 2 | `reference`, `user-preferences` |
| `prototype.chatfs` | 1 | `docs/dev/background` |
| `private.evan-family` | 1 | `financial` |
| `git-partial.prototyping` | 1 | `docs/dev/design.kb/integration-patterns` |
| `2026-05-19--task-archeology` | 1 | `.claude/decision` |

## Proposed Solution

Per collection, in this order of preference:

1. If the frontmatter matches a shape a skill already canonicalises,
   write the two-line `$ref` stub -- `skill://llm-claims-kb/...`,
   `skill://llm-subtask/...`. This closed all of keepawake.
2. Otherwise hand-write a canonical beside the collection, reading every
   member's frontmatter first.

Enums only where the vocabulary is genuinely closed, and say why in the
`description:`. The anti-pattern to avoid is exactly what the sub-agent
did: `enum:` pinned to whatever values happened to be present.

## Implementation Steps

- [ ] `~/.claude` (2) -- nearest to hand, and `~` should validate clean
- [ ] `2026-05-19--task-archeology` (1), `git-partial.prototyping` (1),
      `prototype.chatfs` (1) -- one-offs
- [ ] `prototype.hearts-2025` (2)
- [ ] `private.evan-family` (1)
- [ ] `prototype.personal-reasoning-management` (2) -- check whether the
      `.prms` dialect wants its own canonical in that repo
- [ ] `private.bukzor-llc` (8) -- largest, and the only one where the
      frontmatter is business data rather than kb metadata

## Delegation

- **Sole writer of:** one repo per agent. The eight rows of the table
  above are eight disjoint write-sets; fan out by repo, never by
  collection across repos.
- **Never write a file that already exists.** Not to improve it, not to
  normalize it, not to bring it in line with a canonical. If a
  `*.jsonschema.yaml` is already there, the collection is not a gap and
  is out of scope. This is the prohibition the original delegation
  lacked, and its absence cost 254 files.
- **Never touch `*/jsonschema/` in any skill.** Canonicals are read-only
  to this lane. A gap that seems to need a new canonical is a finding for
  lane -005.
- **Never write an `enum:` whose values are the observed set.** An enum
  asserts the vocabulary is closed. If you cannot say in the
  `description:` why nothing else is admissible, use a plain `type:
  string`.
- **New schema files carry a 2020-12 modeline**, matching the dialect
  they use -- do not copy a draft-07 first line from a neighbour. Lane
  -001 is sweeping exactly that mistake out of 229 files.
- **Verify with:** `llm.kb-validate <repo>` before and after, plus
  `git -C <repo> status -s .` showing only additions.

## Open Questions

- Does `docs/dev/` want a house rule that a claims ledger always roots at
  `claims.kb/`? keepawake had rooted its ledger directly at `docs/dev/`,
  which puts the defining claim outside every collection where no schema
  can reach it. That is a shape error a linter could catch.

## Success Criteria

- [ ] `llm.kb-validate` reports zero "No schema found" across the 18 repos
- [ ] No `enum:` in any new schema that is merely the observed value set
- [ ] Every repo's diff is additions only
