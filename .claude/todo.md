---
managed-by: Skill(llm-subtask)
---

Repo-level list. Skill-scoped work lives in each skill's own
`.claude/todo.md`; the breadcrumbs below point at every open list.

- [ ] T2/v2.2: land the core-and-classes rework of design-next.kb — brief:
      .claude/todo.kb/2026-07-12-000-Land-v2-2-core-and-classes-rework--T2-.md
  - [x] HAIKU (mechanical, confirmed 2026-07-11): genre→class rename sweep
        in design-next.kb — genre-*.md → class-*.md; "genre"/"Genres"
        wording → "class"/"Classes" throughout (incl. five-layer-stack
        table); fix all cross-references to the renamed files
  - [ ] FABLE: draft the rework per the brief (030 additions + coupling
        rename; 040 reworks per the blast-radius classification; CLAUDE.md
        sweeps). Drafts only — no landing commit yet
  - [ ] ANY STRONG MODEL, FRESH CONTEXT (subagent or separate session;
        reviewer gets the tower + drafts, not the drafting session's
        narrative): adversarial review of the drafts, targeting the brief's
        Open Questions. Operator ratifies decision 3 (class-local
        code = consumer status)
  - [ ] Land: apply review verdicts, commit, update the brief
- [ ] Rewrite design-next.kb/040-design.kb/decisions-are-settled-questions.md
      to cite the spec's synthesis-file element instead of restating it: keep
      only the four decision-specific claims (no decision-record class;
      git-log + reviewed: provenance; merge-conflict-as-feature; replaces
      v1's dated decision logs), and fix the dangling "supersedes the
      decision sub-type" sentence. Survives T2 untouched — safe any time
- [ ] Align llm-design-kb's why: guidance (slug examples) with the
      2026-07-13 decision that why: values are file-relative path
      references — or explicitly scope that decision to design-next.kb;
      operator call
- [ ] .claude/todo.kb/2026-07-11-000-settle-task-grain-and-store-count-for-design-next.md
- [ ] T4: trigger-subsystem design session (llm-must-read-kb's successor):
      runtime-neutral condition vocabulary + compilation model for
      action-shaped triggers (risk: hooks-in-disguise), one-way
      triggers→kb-spec citation for bank format, packaging verdict (peer
      standard vs package in the suite — needs a real triggers-without-kb
      consumer to justify peer)
- [ ] Rename "summary" → "synthesis" everywhere: llm-kb SKILL.md summary-file
      sections, self-audit.kb/summary-file-value.md (file + wording), any
      remaining "summary file" refs in skills/tower (kb-spec.md already done)
- [ ] Discuss design-next.kb/040-design.kb/references-are-structured-data.md
      (status: proposal) — label grammar, hardened-label registry, depends:
      migration
- [ ] Run the session-log residue test (design-next): after design/tasks/
      incidents absorb their parts, can any session-narrative class name its
      read-back? Decides devlog's v2 fate (class-record session-log sub-type)
- [ ] llm-design-kb/principles.kb charter: contents outgrew "design.kb
      authoring" scope (evaluate-uses-independently, test-the-residue) —
      widen CLAUDE.md charter or rehome (user rated rehoming tier-4)
- [ ] .claude/todo.kb/2026-01-02-000-skill-evolution-for-chatfs-harmonization.md
- [ ] .claude/todo.kb/2026-01-30-000-shared-code-between-skills.md
- [ ] llm-kb/.claude/todo.md
- [ ] llm-collab/.claude/todo.md
- [ ] llm-subtask/.claude/todo.md
- [ ] llm-must-read-kb/.claude/todo.md
- [x] Create skill `llm-must-read-kb/` (was drafted as `must-read-d`) to
      document the trigger-dir convention (`before/`, `after/`, `when/`).
      Two homes still inconsistent: `~/.claude/must-read.d/` (personal —
      rename plan filed at `~/.claude/CLAUDE.rename-must-read-d-to-must-read-kb.Task.md`)
      and `llm-kb/SKILL.kb/must-read/` (skill-level — user handling).
- [x] Create ADR for skill design criteria (setup:, action-based triggers, depends:)
- [x] Refine load triggers for llm.kb and llm-subtask skills
- [x] ADR: skill and script naming conventions (consolidated bin/, subcommand form, skill naming)
- [x] ADR: lib/python/{libname}/ for testable Python with symlinks
- [x] Rename llm.d → llm.kb
- [x] Reconsider claude-style slug script behavior with `.` and `/` chars; fix preexisting filenames if changed
      -- real algorithm reverse-engineered from `~/.claude/projects/` naming
      (see `bin/claude-slug`); `~/bin/claude-path` and 4 title-slug scripts
      (llm-collab-adr/devlog, llm-subtask-idea/todo) now delegate to it
- [x] todo.kb/2025-12-11-000-complete-entangled-commit-separation-for-naming-refactor.md (deleted)
- [x] ADR: unify directory naming to .kb (docs/dev/adr/2025-12-11-001--unify-directory-naming-to-kb-suffix.md)
