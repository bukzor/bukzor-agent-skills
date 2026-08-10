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
  - [x] Goals-level review: settle the ecosystem-goals framing (mission's
        three jobs: durable knowledge / attention / convention enforcement),
        then assess v2.2 against it — framing ratified 2026-07-19: three
        jobs stand; llm-vitals / llm-chat-librarian / claude-realignment
        are supported consumers of stable conventions (task-archeology
        precedent), not a fourth job; one-operator stipulated as a
        two-way door with a first-share tripwire
        (design-next.kb/070-future-work.kb/multi-operator.md).
        Assessment delivered 2026-07-20: durable-knowledge and
        enforcement jobs covered by committed design; attention's
        "gone stale" clause was the one gap — closed at
        goals/requirements grain this session: use-case inventory
        seeded (llm-triggers/design.kb/use-cases.kb/, 14 entries),
        wake-conditions-are-noticed requirement + sweep entry
        drafted status: proposal, trigger-desc amended (recurrence
        TBD, evaluation-state TBD, evaluability rule), class-trigger
        extended with the wake-shaped third kind (re-proposed). "Policy"
        dissolved into trigger instances (parameters as instance
        data + judgment body) — no policy concept in the design.
        Residue rides the proposal-ratification sweep below
    - [ ] write the two edits ratified in-conversation 2026-07-19:
          new goal 020-goals.kb/machine-legibility.md (stores legible
          to programs with no agent in the loop — stable frontmatter/
          naming/layout as the commitment; why:-link it from
          030-requirements.kb/filesystem-as-database.md) and sharpen
          mission job 1 (durable knowledge includes questions and
          claims still in flight, not only settled state)
    - [x] while there: decide whether class-task.md's elaboration step 2
          notes the option-pair asymmetry (an option's line retires on
          promotion — no pointer) or stays generic. Resolved 2026-07-19
          (operator corrections): pair-level symmetry, synthesis-level
          specialization — ideas.md is an unordered, non-exhaustive
          roll-up (no `- [ ]` list, no per-entry mandate; references
          welcome); step 2 stays generic ("pointer, in place");
          class-task.md, task-synthesis-drift-check.md, and the T3 ADR
          (addendum) updated
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
- [ ] .claude/todo.kb/2026-08-09-000-engine-tower-incubator-follow-ups.md
- [ ] Decide the single-sigil seam (strata.claims): STANCE (user, 32b1a76)
      rules that a one-place "the standing" is a category error the schema
      must not encode, yet claim frontmatter holds exactly one `standing:`
      sigil. Lawful today because the sigil names its judge (a one-entry
      verdict map) and CONTINUUM names the un-quotiented escape valve
      (llm-discourse-graph). Goes live the first time two assessors
      disagree about one claim -- then: multi-assessor frontmatter, or
      port that claim to the discourse-graph presentation
- [ ] Decide whether strata.claims.kb's transitively-implied `prior:`
      entries are meant: `tred` drops five of eighteen (purpose->genre,
      purpose->standing, purpose->protocol, history->protocol,
      fixpoint->standing), each reachable through `view` or `reference`.
      Either the header cites vocabulary it uses directly -- legitimate,
      and the drawing is just a Hasse view -- or it inherited an edge it
      never needed. Surfaced 2026-08-09 by bin/llm.claims-graph
  - [ ] Then: strata.claims.md's hand-drawn ASCII spine is derivable from
        the same `prior:` headers, so it is now a view with no stamp and
        no computer -- regenerate it, stamp it, or say why it stays hand-cut
- [ ] Witness test for RESTRICT
      (strata.claims.kb/fixpoint.kb/triangular-operators-restrict.md):
      a triangular operator on a two-lattice product whose first
      coordinate's lfp equals the lfp computed on the first lattice
      alone; wire `verify:` once it exists (bare standing needs no
      test, but the incubator witnesses every other fixpoint claim)
- [ ] Enforce claim-label prefix-freedom by tooling: the rule lives only
      in claim.jsonschema.yaml description text (attention-grade); the
      2026-08-09 enforcement was a hand-check of 53 labels. Cross-file
      rule, so per-file schema can't hold it -- candidate homes:
      llm-claims-kb/bin/ (now exists, holds llm.claims-dot and the
      dangling/ccomps/acyclic lints) or llm-kb/bin/llm.kb-validate
- [ ] llm-claims/.claude/todo.md
- [ ] llm-kb/.claude/todo.md
- [ ] llm-collab/.claude/todo.md (v2 dissolves llm-collab — weigh new
      investment against core-and-classes.md before spending)
- [ ] llm-subtask/.claude/todo.md
- [ ] llm-must-read-kb/.claude/todo.md
- [x] Create skill `llm-must-read-kb/` (was drafted as `must-read-d`) to
      document the trigger-dir convention (`before/`, `after/`, `when/`).
      All homes now consistent on `must-read.kb/`: personal
      (`~/.claude/must-read.kb/`) and skill-level (`llm-kb/`,
      `llm-claims/`), each SKILL.md carrying the skill-scope
      Required Reading stanza.
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
