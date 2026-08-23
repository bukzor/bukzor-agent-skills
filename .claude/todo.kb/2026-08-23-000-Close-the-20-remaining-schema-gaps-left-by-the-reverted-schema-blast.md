---
managed-by: Skill(llm-subtask)
status: open
---

# Close the 20 remaining schema gaps left by the reverted schema blast

**Priority:** Medium — real gaps, but every one of them has been a gap for
months; nothing regressed.
**Complexity:** Medium. Mechanical for the `$ref`-stub cases, genuine
design work for `private.bukzor-llc` and the `.prms` corpus.
**Context:** 2026-08-22/23 schema survey. A sub-agent was asked to add
schemas where collections lacked them and instead regenerated ~278 files
across 18 repos, overwriting 254 hand-written canonicals. All of it is
reverted and the damage+revert pairs are erased from history in 15 repos.
The *finding* was real; only the execution was not.

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
| `private.bukzor-llc` | 8 | constitution / playbook / strategy — needs real design |
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
   write the two-line `$ref` stub — `skill://llm-claims-kb/...`,
   `skill://llm-subtask/...`. This closed all of keepawake.
2. Otherwise hand-write a canonical beside the collection, reading every
   member's frontmatter first.

Enums only where the vocabulary is genuinely closed, and say why in the
`description:`. The anti-pattern to avoid is exactly what the sub-agent
did: `enum:` pinned to whatever values happened to be present.

## Implementation Steps

- [ ] `~/.claude` (2) — nearest to hand, and `~` should validate clean
- [ ] `2026-05-19--task-archeology` (1), `git-partial.prototyping` (1),
      `prototype.chatfs` (1) — one-offs
- [ ] `prototype.hearts-2025` (2)
- [ ] `private.evan-family` (1)
- [ ] `prototype.personal-reasoning-management` (2) — check whether the
      `.prms` dialect wants its own canonical in that repo
- [ ] `private.bukzor-llc` (8) — largest, and the only one where the
      frontmatter is business data rather than kb metadata

## Open Questions

- Does `docs/dev/` want a house rule that a claims ledger always roots at
  `claims.kb/`? keepawake had rooted its ledger directly at `docs/dev/`,
  which puts the defining claim outside every collection where no schema
  can reach it. That is a shape error a linter could catch.

## Success Criteria

- [ ] `llm.kb-validate` reports zero "No schema found" across the 18 repos
- [ ] No `enum:` in any new schema that is merely the observed value set

## Notes

Related: `2026-08-23-001-*` (the modeline sweep) shares the survey that
found these.
