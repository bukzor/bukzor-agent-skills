---
managed-by: Skill(llm-subtask)
---

Repo-level list. Skill-scoped work lives in each skill's own
`.claude/todo.md`; the breadcrumbs below point at every open list.

- [x] T2/v2.2: land the core-and-classes rework of design-next.kb — brief:
      .claude/todo.kb/2026-07-12-000-Land-v2-2-core-and-classes-rework--T2-.md
  - [x] HAIKU (mechanical, confirmed 2026-07-11): genre→class rename sweep
        in design-next.kb — genre-*.md → class-*.md; "genre"/"Genres"
        wording → "class"/"Classes" throughout (incl. five-layer-stack
        table); fix all cross-references to the renamed files
  - [x] FABLE: draft the rework per the brief (030 additions + coupling
        rename; 040 reworks per the blast-radius classification; CLAUDE.md
        sweeps). Drafts only — no landing commit yet
  - [x] ANY STRONG MODEL, FRESH CONTEXT (subagent or separate session;
        reviewer gets the tower + drafts, not the drafting session's
        narrative): adversarial review of the drafts, targeting the brief's
        Open Questions. Verdict: land with fixes; all four open questions
        correctly stayed open. Decision 3 still awaits operator
        ratification (not asserted either way in the drafts, so not a
        landing blocker) — see brief's Open Questions
  - [x] Land: apply review verdicts (F1-F5, see commit 9d80ded), commit,
        update the brief
- [x] Rewrite design-next.kb/040-design.kb/decisions-are-settled-questions.md
      to cite the spec's synthesis-file element instead of restating it: keep
      only the four decision-specific claims (no decision-record class;
      git-log + reviewed: provenance; merge-conflict-as-feature; replaces
      v1's dated decision logs), and fix the dangling "supersedes the
      decision sub-type" sentence. Survives T2 untouched — safe any time
- [x] Align llm-design-kb's why: guidance (slug examples) with the
      2026-07-13 decision that why: values are file-relative path
      references — or explicitly scope that decision to design-next.kb;
      operator call. Resolved 2026-07-18: propagate to llm-design-kb —
      its own why.jsonschema.yaml analog (technical-policy.jsonschema.yaml)
      already treated why: as untyped path strings, so only the SKILL.md
      teaching example was stale
- [ ] Green-light the v2 build — the gate that fires the trigger in
      design-next.kb/070-future-work.kb/v1-migration-bridge.md; blocked on
      the children:
  - [x] (T3) .claude/todo.kb/2026-07-11-000-settle-task-grain-and-store-count-for-design-next.md
        — settled 2026-07-19: all three axes recorded in class-task.md
        (+ two 070 entries); sessions.kb dated-prefix sweep scheduled
        in that repo's reconcile-sessions-kb-schema-drift session
  - [x] T4: trigger-subsystem design session (llm-must-read-kb's successor)
        — settled 2026-07-19: packaging is in-suite (triggers depend on
        llm-kb, no triggers-without-kb consumer exists); condition
        vocabulary is three neutral kinds (command/path pattern,
        lifecycle point) plus a floor-noticeable admission test;
        compilation rejected in favor of interpretation (per-runtime
        shims read trigger files at fire time — staleness structurally
        impossible, coverage report replaces `kb doctor`); bank format
        stays one authoring format, enforcement varies by detectability;
        task↔trigger boundary resolved via a shared wake-condition
        grammar. Recorded in new skill `llm-triggers/design.kb/`
        (design-next.kb cites down rather than restating); journey ADR:
        docs/dev/adr/2026-07-19-001-Trigger-subsystem-condition-vocabulary-and-interpretation-model--T4-.md.
        Left open in llm-triggers/design.kb/: several status:proposal
        entries and [!QUESTION] blocks (elaboration-frontmatter field
        names, per-cell sweep semantics, exact hook-event bindings) —
        folded into the tower-wide proposal-ratification sweep below
    - [x] T4 input, inherited from the retired
          integrate-sessions-kb-into-llm-subtask taskfile: test
          whether skill-bundled commands
          (`~/.claude/skills/<skill>/commands/<name>.md`) resolve as
          top-level `/<name>` — bears on the adapter-side packaging
          of delivery machinery. Tested 2026-07-19 (scratch skill +
          `claude -p` probes): they do NOT resolve, neither as
          `/<name>` nor `/<skill>:<name>`; the skill itself IS a
          top-level `/<skill>` command (commands/skills merged per
          docs); only plugins bundle multiple commands (namespaced
          `/<plugin>:<name>`)
  - [ ] Goals-level review: settle the ecosystem-goals framing (mission's
        three jobs: durable knowledge / attention / convention enforcement),
        then assess v2.2 against it — session 2026-07-19 opened this;
        Claude's framing delivered, operator reaction pending. Open points:
        where llm-vitals / llm-chat-librarian / claude-realignment sit
        (fourth job: introspection/health?); is one-operator a permanent
        assumption?
    - [ ] while there: decide whether class-task.md's elaboration step 2
          notes the option-pair asymmetry (an option's line retires on
          promotion — no pointer) or stays generic; asymmetry is already
          specified in Horizon-and-priority + task-synthesis-drift-check
  - [ ] Ratify (or reject) the tower's `status: proposal` entries and
        `[!QUESTION]` blocks — enumerate (now spans two towers post-T4):
        grep -rn 'status: proposal\|!QUESTION' design-next.kb llm-triggers/design.kb
  - [ ] Extend ~/bin/claude-open-tasks-list to the decision grammars — brief:
        .claude/todo.kb/2026-07-19-000-Extend-claude-open-tasks-list-to-the-decision-grammars.md
- [x] Rename "summary" → "synthesis" everywhere: llm-kb SKILL.md summary-file
      sections, self-audit.kb/summary-file-value.md (file + wording), any
      remaining "summary file" refs in skills/tower (kb-spec.md already done)
- [x] Discuss design-next.kb/040-design.kb/references-are-structured-data.md
      (status: proposal) — label grammar, hardened-label registry, depends:
      migration. Resolved 2026-07-18: kebab-slug labels (not free strings);
      no separate hardened-label registry (the promoted key's schema entry
      is the record). `blocked-on: discussion` cleared; still
      `status: proposal` like the rest of the untouched tower — the
      `depends:` migration itself is unbuilt, deferred to when v2 lands
- [x] Run the session-log residue test (design-next): after design/tasks/
      incidents absorb their parts, can any session-narrative class name its
      read-back? Decides devlog's v2 fate (class-record session-log sub-type).
      Resolved 2026-07-18: cut. Skimmed 3 real devlog entries — every
      section (narrative-of-failure, decisions/alternatives, conventions
      established, open items) already better-homed in incident/design/
      principles-procedures/task; no residue, no nameable read-back moment.
      Updated class-record.md and core-and-classes.md accordingly
- [ ] llm-design-kb/principles.kb charter: contents outgrew "design.kb
      authoring" scope (evaluate-uses-independently, test-the-residue) —
      widen CLAUDE.md charter or rehome (user rated rehoming tier-4)
- [ ] .claude/todo.kb/2026-01-02-000-skill-evolution-for-chatfs-harmonization.md
- [ ] .claude/todo.kb/2026-01-30-000-shared-code-between-skills.md
- [ ] llm-kb/.claude/todo.md
- [ ] llm-collab/.claude/todo.md (v2 dissolves llm-collab — weigh new
      investment against core-and-classes.md before spending)
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
