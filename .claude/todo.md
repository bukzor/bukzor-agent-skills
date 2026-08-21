---
managed-by: Skill(llm-subtask)
---

Repo-level list. Skill-scoped work lives in each skill's own
`.claude/todo.md`; the breadcrumbs below point at every open list.

- [x] Witness the act algebra (contravention fold, moot color, real-ledger
      run) — brief: .claude/todo.kb/2026-08-17-000-Witness-the-act-algebra--contravention-fold-and-moot-color-in-engine-tower.md
      Done 2026-08-17; residue (uncited moot tests, fleet citation
      cycle) recorded in the brief
- [ ] `llm-claims-kb`'s `why:` resolution has no cross-ledger case:
      `claim_id()` computes every id relative to the citing ledger's own
      parent directory, so a `why:` path that climbs out to a sibling
      skill's `.claims.kb/` (e.g. `formalize/` citing `deformalize/`)
      reports as dangling even though the file exists and the path
      resolves on disk. Found 2026-08-15 wiring the `/formalize` ↔
      `/deformalize` seam — worked around by dropping those four `why:`
      entries to prose-only backtick paths (non-normative per
      `Skill(llm-claims-kb)`'s own rule), so nothing is broken, but the
      structural graph has no edge for a real cross-skill dependency.
      Needs a design decision before fixing: what a cross-ledger claim id
      looks like (ledger-qualified?), and whether `llm-claims-kb-graph`
      draws one drawing across ledgers or leaves the seam undrawn by
      design
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
- [ ] REOPENED 2026-08-18: devlog's v2 fate — the residue test's "cut"
      (above, 2026-07-18) has a counter-argument: the user's third-place
      definition (llm-collab/references.kb/file-types.kb/devlog.md)
      names a read-back moment ("what were the concerns surrounding
      this change?"). Marked as [!QUESTION] in
      design-next.kb/040-design.kb/class-record.md; ADR_FATE
      (design.claims.kb/does-the-ledger-subsume-the-adr.md) leans on it
- [ ] llm-design-kb/principles.kb charter: contents outgrew "design.kb
      authoring" scope (evaluate-uses-independently, test-the-residue) —
      widen CLAUDE.md charter or rehome (user rated rehoming tier-4)
- [ ] .claude/todo.kb/2026-01-02-000-skill-evolution-for-chatfs-harmonization.md
- [ ] .claude/todo.kb/2026-01-30-000-shared-code-between-skills.md
- [ ] .claude/todo.kb/2026-08-09-000-engine-tower-incubator-follow-ups.md
- [ ] Standing-theory residue left by the 2026-08-20 rename sweep (devlog
      007). Each is a recommendation the sweep declined to fold in, not an
      open question:
  - [ ] Widen `Mapping[str, Edge]` to allow several edges per edge-claim.
        The single-edge shape is an artifact of the first witness; no claim
        rules it
  - [ ] Lift the *into* half of the edge stratification — one assertion.
        The *out of* half stays declined: it wants an approximation
        fixpoint first
  - [ ] Lift `stale-when:` to non-defining claims, so a stipulation
        tripwire has a structural home instead of living in prose
- [ ] Build the antichain completion the standing theory already claims:
      COMPUTED (`standing.kb/standing-is-computed-not-stored.md`) and
      COMPLETION (`standing.kb/the-status-order-is-not-a-complete-lattice.md`)
      say standing's values live in the completion of the status order,
      and the engine raises at the missing join instead. The claims are
      honest about it — COMPLETION says the mechanized operator raises
      exactly there — but the repair they name is unbuilt, so no
      `verify:` can cover that sentence. Found 2026-08-20 by the
      `verify:` under-selection sweep; the two other under-selections
      that sweep found were fixed by writing the missing witness, this
      one cannot be. Either build the completion (values become
      antichains, joins total) or shrink both bodies to what the engine
      does
- [ ] `verify:` flattens to `certified(CHECK)` identically whether the
      check passes today or names a test nobody has written
      (`data-representation.kb/every-structure-lands-in-every-target.md`
      is the live instance, sanctioned by the claim schema as acceptance
      debt). A reader of the flattened ledger cannot tell a witnessed
      claim from an owed one. Notation defect in `Skill(llm-claims)`,
      surfaced 2026-08-20
- [ ] Judge the own side of `llm-claims-kb-ownership --candidates`:
      21 unowned words that concentrate in one theory and are said
      nowhere a finding could fire. Most are `ownership.kb`'s own
      coinages, which it does not yet own (`import`, `taker`,
      `unowned`, `double`, `idle`, `queue`, `cull`, `menu`,
      `position`, `ownership`); the rest are `below`, `type`, `axis`,
      `projection`, `defeated`, `guide`, `adr`, `phi`, `wrestled`,
      `attack`, `collapsed`. The scan proposes, `SHOULD_OWN` decides
      -- the count is evidence for the counterfactual, never the
      ruling on it. Deferred 2026-08-20 (the cull was the ask); the
      cull side of the same scan is settled, all 7 survivors kept
- [ ] `llm.kb-validate .` at the repo root descends into
      `.claude/worktrees/` even though `.gitignore:7` names it and the
      2026-08-12 fix filters discovery through `git check-ignore`:
      24 of the 25 errors it reports are duplicate copies from the two
      live worktrees. Likely cause -- a worktree carries its own `.git`,
      so `check-ignore` run inside it answers relative to that root.
      The live tree is clean (verified 2026-08-20, after fixing the two
      real errors it was hiding), so this is pure noise, and noise that
      trains the eye to ignore a red count
- [ ] `llm-discourse-graph` has no migration guide and no
      `must-read.kb/when/` trigger, unlike its sibling skills. Raised
      2026-08-20; the specifics were not recorded, so scope it from
      what `llm-kb` and `llm-claims` carry before spending
- [ ] 13 collection roll-ups now report `No schema found`, which is
      true and is where the three resolutions run out: a synthesis file
      cannot move into the `.kb/` it summarizes, its parent is not the
      thing to rename, and its `last-updated` is load-bearing (the claim
      schema says a cache is lawful iff it names the revision it derives
      from). The missing fourth resolution is that a collection's schema
      covers its roll-up, which
      `llm-kb/complete-example/food.jsonschema.yaml` already does and
      documents -- `last-updated`, "Required for summary files (e.g.,
      cake.md summarizing cake.kb/)" -- while `decorations.jsonschema.yaml`
      beside it says "items" and forbids the field. Settle the example
      against itself before generalizing from either half
- [ ] The walk still reaches no `README.md` and no `devlog/`/`adr/`
      entry, and `llm-discourse-graph` is the only skill whose dated
      docs carry frontmatter -- 9 ADRs with `date`/`status`/`supersedes`,
      1 devlog of 4 with a bare `date`. That is a collection wearing a
      plain directory: `adr.kb/` plus a schema, not a wider walk. The
      21 `SKILL.md` are the population a widened walk must not reach
      rather than resolve: a skill manifest is not kb data, and llm-kb
      defines no schema for Claude Code's keys
- [ ] Three `.claude/todo.jsonschema.yaml` outside this repo are not the
      canonical stub, though `llm-kb/migrations.kb/2026-07-07-000-schema-copies-to-ref-stubs.md`
      reads `status: complete` over a scope naming the whole tree:
      `dotfiles/` (89 lines), `prototype.chatfs/` (10),
      `ideation.physical-musings/` (12). The first two never mention
      `Skill(llm-subtask)`, so they look like the migration's own
      "diverged on purpose" exclusion rather than stale copies -- but
      the record does not say which, and a completeness claim nobody
      can re-derive is the thing the migration was written to prevent.
      Confirm each, then either stub it or name it in the exclusion
- [ ] Lean port of the engine tower — gated, not next: fires on the
      triggers in the brief (algebra bug escapes / real ledger goes
      non-degenerate after KEY+CUT close / incubator graduates);
      brief: .claude/todo.kb/2026-08-18-000-Lean-port-of-the-engine-tower.md
- [ ] Operator decision pending (2026-08-13): keep or revert the four
      commits of the audit-repair session -- 52e6c55 (engine), befce32
      (ledger), a9bf61a (paste split), e6e87f6 (record move). Offered as
      `git revert` of any subset; no answer given. The two edits most
      wanting a ruling either way touch `user`-signed claims: WORD (the
      "a DAG of transactions where branching is allowed" gloss struck,
      since a word is linear) and REGROUND ("theory" -> "view", a
      confinement fix). Neither ruling was changed, but neither edit was
      the agent's to make unilaterally
- [~] Finish the strata replication run -- PARKED 2026-08-13 at the
      operator's word; nothing expires, restart when they say. 080 was
      answered once (`docs/dev/strata.replication.run.kb/080-defeats.md`)
      and its findings are filed (52e6c55, befce32); what is parked is
      the *re-run* of 080 against the repaired ledger. Restart point:
      session `d7f2e549-1e8e-4981-99aa-780f9868341b` -- cut at the 070
      reply, verified by probe ("the graded blind-lift comparison ...
      sent to the coordinator") -- in worktree
      `bukzor-agent-skills--replication-run`, branch `env-2026-08-13`.
      Resume it, confirm Fable 5 at xhigh (the first 080 ran xhigh; hold
      it so the two are comparable), send
      `strata.replication.kb/instructions.d/080-defeats.md` unaltered,
      extract with `strata.replication.run.kb/extract-stages.py` and
      commit the stage on main. Then 090 (owner's rulings) and
      adjudication of 070's six filable claims
  - [ ] `env-2026-08-13` is not a private sandbox: peer sessions commit
        onto it (186e256, 31f0b70 landed the stale-when rename there).
        Re-check what the worktree holds before sending any turn -- the
        seal is a root commit precisely so `git log` stays uninformative,
        and each peer commit erodes that
  - [ ] Superseded pointers still exist and still resolve: branch
        `strata-replication-run`, tag `run/pre-080`, session
        `0476a1a8-b186-4988-8deb-83853c353acb`. The 2026-08-10 and
        2026-08-11 devlogs name them, correctly for their dates. This
        item is the current one; follow it, not them. Delete the branch
        and tag once the re-run has happened (they are shared refs, so
        that wants the operator's word)
- [ ] Decide the single-sigil seam (strata.claims): STANCE (user, 32b1a76)
      rules that a one-place "the standing" is a category error the schema
      must not encode, yet claim frontmatter holds exactly one `standing:`
      sigil. Lawful today because the sigil names its judge (a one-entry
      verdict map) and CONTINUUM names the un-quotiented escape valve
      (llm-discourse-graph). Goes live the first time two assessors
      disagree about one claim -- then: multi-assessor frontmatter, or
      port that claim to the discourse-graph presentation. Cited from
      `.claude/todo.kb/2026-08-16-000-Reconcile-llm-claims-kb-s-standing-scheme-with-PRMS-s-stmt-proof-and-STANCE-s-assessor-relativity.md`
      as a constraint on that redesign, not folded in -- this seam is
      about validity being assessor-relative, a different question from
      what verdicts a single assessor's judgment can carry
- [ ] Decide whether strata.claims.kb's transitively-implied `prior:`
      entries are meant: `tred` drops five of eighteen (purpose->genre,
      purpose->standing, purpose->protocol, history->protocol,
      fixpoint->standing), each reachable through `view` or `reference`.
      Either the header cites vocabulary it uses directly -- legitimate,
      and the drawing is just a Hasse view -- or it inherited an edge it
      never needed. Surfaced 2026-08-09 by bin/llm-claims-kb-graph
  - [x] Then: strata.claims.md's hand-drawn ASCII spine is derivable from
        the same `prior:` headers, so it is now a view with no stamp and
        no computer -- regenerate it, stamp it, or say why it stays
        hand-cut. Resolved 2026-08-13 (52e6c55, befce32): the third. The
        picture says it is hand-cut and names the computed copy;
        `test_tower.py` now reads the poset out of the twelve
        `<theory>.md` `why:` lines instead of mirroring it by hand
- [x] Witness test for RESTRICT
      (strata.claims.kb/fixpoint.kb/triangular-operators-restrict.md):
      a triangular operator on a two-lattice product whose first
      coordinate's lfp equals the lfp computed on the first lattice
      alone; wire `verify:` once it exists (bare standing needs no
      test, but the incubator witnesses every other fixpoint claim).
      Done 2026-08-13 (52e6c55):
      `test_fixpoint.py::test_a_triangular_operator_restricts_to_its_first_coordinate`,
      `verify:` wired, plus the `authority:` line (Bekic) it also lacked
- [ ] Enforce claim-label prefix-freedom by tooling: the rule lives only
      in claim.jsonschema.yaml description text (attention-grade); the
      2026-08-09 enforcement was a hand-check of 53 labels. Cross-file
      rule, so per-file schema can't hold it -- candidate homes:
      llm-claims-kb/bin/ (now exists, holds llm-claims-kb-dot and the
      dangling/ccomps/acyclic lints) or llm-kb/bin/llm.kb-validate
  - [ ] Partly done 2026-08-11: llm-claims-kb-flatten checks it (theory
        labels included, since flattening gives every theory one) and
        found FLEET prefixing FLEET_MAP in strata.claims.kb. It runs
        only when you flatten, so the check still wants a home that a
        pre-commit pass would reach
- [x] Land the strata.claims.kb migration on main: `defeated-by:` ->
      `stale-when:` on all thirteen lines, plus FLEET_MAP -> ATLAS, which
      breaks the prefix collision `grep FLEET` could not see through.
      Landed on main 2026-08-13 (03911d9, 891fd7e); verified here --
      thirteen `stale-when:` lines, ATLAS in `where-the-v1-skills-sit.md`
      and in question.md's table, flatten reports zero lints,
      `llm.kb-validate docs/dev/strata.claims.kb` reads 68 files 0 errors.
      (Attribution fix: the env-worktree commits 186e256/31f0b70 were
      that same session reaching into `env-2026-08-13`, not the
      replication session's doing.)
- [ ] Review the standing of the 21 theory-defining claims: the
      2026-08-11 migration gave every theory header `standing: agent`
      uniformly, because headers carried no standing before it. That is a
      signature nobody made claim-by-claim. Most are plausibly right (`+`
      is the resting state), but `strata.claims.kb/purpose.md` is the
      operating regime the user ruled on 2026-08-09 and reads as `user`;
      scan the rest for the same mismatch
- [x] llm.kb-validate walks gitignored directories: `llm.kb-validate .`
      at the repo root reports 12 errors, all inside `trash/`
      (`aborted-git-mv/` keeps a half-renamed ledger whose per-collection
      schemas are gone). Noise that trains the eye to ignore a red count
      -- skip what `git check-ignore` claims, or take an exclude flag.
      Fixed 2026-08-12: discovery filters through `git check-ignore`, a
      path named on the command line is validated regardless. The repo
      root now reads 0 errors; 17 files under `trash/` stopped counting
- [ ] The only dotted command names left in the repo are
      llm-kb/bin/llm.kb-validate{,-links}; the 2026-08-08 exact-prefix
      ruling makes them llm-kb-validate{,-links}. ~27 live references
      here plus 11 files under ~/.claude outside skills/ -- a sweep to
      do deliberately, not in passing
- [ ] llm-claims-kb has no story for non-claim (evidence) collections
      inside a ledger: PRMS `design.claims.kb/world.kb/` (substrate
      assessments, frontmatter-free by design) crashes
      `llm-claims-kb-dot`'s `split_frontmatter`, and the manual is silent
      on whether such collections are legal. Candidates: an exemption
      marker in the collection's CLAUDE.md, a collection `kind:`, or
      claims-only discipline stated in the manual. Counterpart item in
      `prototype.personal-reasoning-management/.claude/todo.md`
- [ ] Task 5 of the 2026-08-09/10 review arc (user-deferred, twice):
      future planning for the claims/strata corpus — next steps, potential
      endpoints, brief monetization discussion. Pure conversation; pick up
      when the user says go
- [ ] Evaluate absorbing the PRMS corpus dialect into llm-claims-kb (the
      `.claims.kb` ↔ `.prms.kb` seam): computed standing (the engine
      derives status; corpus records only bare and `!`) as a legitimate
      specialization vs a fork; label-form `why:` entries; `stmt:`/`proof:`
      as the strong form of `verify:`. Counterpart item (field-name
      convergence sketch) in
      `prototype.personal-reasoning-management/.claude/todo.md`.
      Superseded as the tracking item by
      `.claude/todo.kb/2026-08-16-000-Reconcile-llm-claims-kb-s-standing-scheme-with-PRMS-s-stmt-proof-and-STANCE-s-assessor-relativity.md`,
      which also folds in the `retracted`/`rejected`/`dissolved`
      verdict gap and `STANCE`'s assessor-relativity -- this line stays
      as the PRMS-side pointer
- [x] Make `glob_prune` earn its name (a real `os.walk` prune instead of a
      full glob plus two filters) -- measured 2026-08-13 and dropped.
      Discovery is 7% of runtime: the glob costs 144ms of a ~2000ms run,
      the rest is YAML + jsonschema over 366 files, and pruning saves
      ~70ms. Deciding descent means asking git per directory visited,
      hundreds of execs against today's 97. It subtracts nothing either:
      `corpus` must stay for the nested branch and "asking is asking"
      becomes a flag threaded through the walk. Revisit only if a corpus
      grows large enough for the walk to show up in a profile
- [ ] Fold llm-claims-kb into llm-claims — per DOMAINS
      (design.claims.kb/authorship.kb/skills-are-domains-occasions-are-triggers.md):
      the notation/file-form split priced load cost, now priced at the
      trigger-gated file. Punted 2026-08-18 pending llm-triggers
      maturing; on merge the old skill name keeps a routing stub
      (ROUTING)
- [ ] Merge formalize + deformalize — tripwire, not scheduled: fires
      when either skill's next rework strains against the other (they
      are one translation's two directions). Punted 2026-08-18
- [ ] USER: hand-copy llm-claims/SKILL.md's Core block into claude.ai
      preferences — the two are kept verbatim-identical and the block's
      wording changed during the 2026-08-09/10 polish (the .claims.kb
      rename itself left it byte-identical)
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
