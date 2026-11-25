---
status: planning
scope: |
  Every skill's `skill.kb/` in bukzor-agent-skills, and every reader of the
  paths below:
  - `skill.kb/self-audit.kb/` and `self-audit.md` become
    `skill.kb/quality-passes.kb/` and `quality-passes.md` (`llm-kb`,
    `llm-claims-kb`);
  - `llm-design-kb/skill.kb/principles.kb/` folds into
    `skill.kb/quality-passes.kb/`, as passes run while writing;
  - `references/` at a skill root (`llm-kb`, `llm-subtask`,
    `llm-must-read-kb`) and loose reference files in `skill.kb/`
    (`align/skill.kb/sort-goals-into-four-bins.md`,
    `llm-claims/skill.kb/theories.md`, `persist-clarity/skill.kb/persistence.md`)
    become `skill.kb/reference.kb/`.
  Not in scope: `docs/dev/` and design ledgers, which are maintainer material.
why: |
  Implements the fleet ledger's `LAYOUT`, `PASS_NAME`, `SKILL_KB` and
  `REFERENCE_KB` (`docs/dev/claims.kb/design.claims.kb/authorship.kb/`): one
  name and one place for quality passes and reference docs across skills, so
  every `skill.kb/` is a collection of kbs.
---

# `skill.kb/`: quality passes and reference docs

## Transformation

Per skill, `git mv` each path in scope, then sweep its readers: the `SKILL.md`
bootstrap and mentions, `must-read.kb/` entries, `procedures.kb/run-self-audits.md`
(renamed `run-quality-passes.md`), relative links inside the moved files, the
fleet ledger's citations, and `~/.claude/must-read.kb` entries.

`validate.sh`: no `self-audit` path, no root `references/`, and no loose file
other than `CLAUDE.md` or a collection's synthesis file in any `skill.kb/`;
`llm.kb-validate-links` clean.
