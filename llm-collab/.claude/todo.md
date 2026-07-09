---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 3.0
    rationale: |
      Residual of inline items only (child todo.kb files rated
      separately). Two inline bugs/decisions: fix bin/ script arg-
      passing crash (~1.5h, sed-escape on slashes + slugify path
      collision), decide HACKING.md fate for kb-only repos (~0.5h
      decision + ~1h refactor if removed). ~3h.
    confidence: tentative
  benefit-2w:
    "@value": 0.5
    rationale: |
      Bug fix removes silent crash for any agent passing path as
      positional. HACKING.md decision unsticks llm-collab-init UX
      for kb repos. Modest QoL.
    confidence: tentative
  cost-of-delay-2w:
    "@value": 0.2
    rationale: |
      bin/ script crash is currently silent — agents may not even
      notice; same root cause flagged in llm-subtask, so it's a
      flowing per-session tax across both skills.
    confidence: tentative
---

- [x] todo.kb/2025-11-26-000 (destructure docs into references.kb/)
  - [x] Fix errors in must-read.d/before/creating-documentation.md
  - [x] Extract all content to references.kb/ (file-types, guidelines, workflows)
  - [x] Remaining: schemas, update references
- [x] todo.kb/2025-12-02-001 (create category overview files) — Low
- [x] todo.kb/2025-12-02-000 (factor SKILL.md above the fold) — Medium
- [x] Decide fate of creating-documentation.md (delete vs replace with index)
- [x] Consider must-read-before trigger for llm-collab-docs skill
- [~] todo.kb/2025-12-03-000 (pivot from .d to .kb naming) — references.kb/ done, triggers/validation remain
- [ ] todo.kb/2025-11-29-001 (document blocking pattern in subtask skill) — High/Low
- [x] todo.kb/2025-11-26-002 (devlog template redundancy fix) — Medium/Low
- [ ] todo.kb/2025-11-26-001 (ideas.kb/ pattern) — Medium/Low
- [x] Replace heredocs in bin/ scripts with skeleton/ copies
  - [x] llm-collab-init: all 6 heredocs → cp from skeleton/
  - [x] llm-collab-devlog: heredoc → sed from skeleton template
  - [x] llm-collab-adr: heredoc → sed from skeleton template
  - [x] llm-collab-idea: heredoc → sed from skeleton template
  - [x] Created missing skeleton/docs/adr/README.md
- [x] Check other scripts for docs/ → docs/dev/ migration needed (scan llm-collab and other skills)
  - [x] All bin/ scripts: rename -n|--name-only → -n|--dry-run (adr, devlog, idea, subtask-todo)
  - [x] skeleton/docs/dev/devlog/: old dir deleted, new dir exists with content
  - [x] Verify llm-collab-devlog script still works
  - [x] Run TESTING.md to verify bin/ scripts work with new paths
  - [x] Check other skill scripts for similar migration needs (none have docs/ refs)
- [x] Bug: bin/ scripts crash when agent passes path as positional arg
  - Fixed via strict `-C <dir>`/`--title <title>` grammar, no positionals
    accepted anywhere; see docs/dev/adr/2026-07-09-000-Strict--C---title-grammar-for-bin--script-args.md
    (commit 6b2b9aa)
- [ ] HACKING.md irrelevant for knowledge-base repos
  - llm-collab-init creates contributor onboarding template
  - For a .kb repo with no code, this is noise

## Later

- [x] todo.kb/2026-02-09-001 (cleanup stale path references) — skeleton, references.kb, TESTING.md
- [x] todo.kb/2026-02-09-000 (design.kb pattern for living design docs) — pattern designed, implemented
  - [x] Design structure and traceability model
  - [x] Document pattern (references/how-to-document-design-knowledge.md)
  - [x] Create skeleton/docs/dev/design/CLAUDE.md
  - [x] Update llm-collab-init script
  - [x] Add freshness hooks (session-end, ADR script)
  - [x] Remove stale file references from SKILL.md
  - [x] Update SKILL.md quick reference
- [ ] todo.kb/2025-12-11-000-Update-skeleton-to-match-docs-dev--pattern-from-git-partial.md (build `skeleton/docs/dev/milestones.kb/` template + `llm-collab-init` wiring — destination path already settled and documented) — High/Medium; blocks prototype.chatfs `docs/dev/milestones.kb/` creation
- [ ] todo.kb/2025-11-29-000 (devlog reevaluation - strategic) — Medium/High
- [ ] todo.kb/2025-11-26-003 (clarify todo.md/todo.kb relationship in subtask skill docs)
