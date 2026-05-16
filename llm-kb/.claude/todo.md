<anthropic-skill-ownership llm-subtask />

- [x] Fix broken references to complete-example.md in SKILL.md (lines 84, 116)
- [x] Run movie-tracker test, evaluate against SKILL.md
- [ ] Configure permissions via .claude/settings.json instead of --allowedTools
- [x] Pivot to .kb naming (skill renamed llm.d → llm.kb)
- [ ] .claude/ideas.kb/2026-04-17-000-design-process-for-new-kb-structures.md
- [ ] .claude/ideas.kb/2026-04-17-001-codify-tables-lists-smell-as-kb-promotion-heuristic.md
- [x] SKILL.md: sharpen "Promotion Signals" -- added parallel-sections bullet, 50-token threshold for growth pressure
- [x] SKILL.md: make references prescriptive ("must read creating-a-new-kb.md on first kb creation")
- [x] SKILL.md: route "Creating a Collection" procedure through the new how-to doc
- [x] references/creating-a-new-kb.md: new doc with plan + four quality passes
- [x] SKILL.kb/ runtime infrastructure: triggers, 13 self-audits, shared procedures
- [x] docs/dev/ methodology kb: case-study, concepts, post-mortem split into capture + reconcile
- [ ] todo.kb/2026-05-15-000-reconcile-seed-case-study-may-13-har-browse-rust-port.md
- [x] Resolve `bin/llm.kb-validate` quirk: `SKILL.kb/SKILL.jsonschema.yaml` not auto-matched (moved schema to repo root)
- [ ] Route `must-read/after/distilling-from-a-raw-source.md` through `run-self-audits.md` for the generic audit portion
- [ ] Move `docs/dev/procedures.kb/reconcile-case-study.md` to `SKILL.kb/procedures.kb/` (consumer-facing parallel to post-mortem move)
- [ ] Re-read SKILL.md after the recent rewrite; confirm the "No schema found → copy from skeleton" line still reads coherent in context
- [ ] Verify `tests/` still pass after schema reshuffle, `.d → .kb` rename, and KbValidator extension
- [ ] Devlog entry for this session (skeleton-default schema centralization, sessions.jsonschema migration)
- [ ] Commit current working tree (CLEAN-KITCHEN)

## Later

- [ ] todo.kb/2026-01-02-000-complete-d-to-kb-rename.md (finish `.d → .kb` rename in `complete-example/`; promote ADR 2025-12-03-000 to Accepted) -- related to prototype.chatfs harmonization
- [ ] todo.kb/2025-12-04-000 (Claude enumerates contents despite explicit prohibition)
- [ ] todo.kb/2026-02-09-000 (Schema reuse with $ref)
- [ ] Decide `post-mortem.md` naming (capture-incident? learn-from-failure?) -- defer until a second case-study clarifies the modes
- [ ] Extract `SKILL.kb/self-audit.kb/bloat.md`'s "Frame" stance into `principles.kb/` once that collection is seeded
- [ ] Rename `SKILL.kb/must-read/` → `SKILL.kb/must-read.kb/` (user-handling) -- align with `Skill(llm-must-read-kb)` convention
