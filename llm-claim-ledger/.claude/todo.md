# TODO

- [ ] .claude/todo.kb/2026-08-06-000-Rebase-llm-design-kb-on-the-claim-ledger.md
      — the plan: llm-design-kb becomes a discipline over the ledger;
      ledger gains lint, footnote provenance, file-per-claim + self-audit
      conventions; all legs (including other-scope ones) tracked there
- [ ] .claude/todo.kb/2026-08-08-000-Helper-command-family-bin-llm-claim-ledger.md
      — requirements for `bin/llm-claim-ledger-*` (shared parser, lint,
      attention, poset, replay + provenance-map convention), distilled
      from the prototype.llm-stet serialization audit; details the
      rebase plan's "ledger gains lint" leg
- [ ] USER: re-paste the SKILL.md Core block into claude.ai preferences
      (verbatim-shared; pending since 2026-07-24 — the `+` sigil, the
      governance line, the open-claims policy, and a worked example in
      place of the self-describing one; 2026-07-28 — `<-` no longer
      claims "entailment", per `SKILL.kb/arrows-are-motivation.md`)
- [ ] Give `good-smells.kb/` something it can fail. All 11 entries were
      read off the finished notation in one conversation, so the notation
      satisfies every one by construction and 8 stand at `open`. A
      criterion nothing can fail is a description, not a criterion. Two
      tests, cheapest first:
  - [ ] Score the criteria against the alternatives this design already
        rejected — `superseded` as a status, `obligated` as a status, the
        `'` sigil, node types beyond claims, formal entailment arrows.
        Several are recorded as foils in `design.ledger.kb/notation.kb/`
        bodies. Build the matrix: a criterion that rejects nothing in the
        set is a retraction candidate; a rejected alternative no criterion
        rejects means the criteria are incomplete and we made a call we
        cannot explain. Needs no external research
  - [ ] Then score against a published notation (Toulmin layout, IBIS,
        argument-mapping, ADR). Different question — whether these
        criteria are about claim notations in general or only about this
        one — and only worth the reading after the cheap test runs
  - [ ] Prediction to check the result against, recorded 2026-07-28:
        `DEMO`, `WRITING` and `IMAGE` will not survive as *criteria* —
        each judges our method rather than the notation, and any notation
        with a good example passes `DEMO`. They relocate to `purpose.kb/`
        or `SKILL.kb/` rather than being deleted. `NAME_LOCUS` degenerates
        to "we have persistent labels and they don't". The other seven
        discriminate. Being wrong here is the informative outcome
- [ ] Re-test the labels against `NAME_LOCUS` once the scoring item above
      closes. `NAME_LOCUS` says a label names the locus of contention,
      not the conclusion — by that standard `LEAST_FIX` and `CLAIMS_ONLY`
      both encode answers (`CYCLES` and `NODE_TYPES` are the loci). Not
      acted on: `NAME_LOCUS` is `standing: open`, and both labels are
      shared verbatim with prototype.personal-reasoning-management, where
      `CLAIMS_ONLY` is `certified(review 089)` — renaming a certified
      claim on an untested criterion is the tail wagging the dog
- [ ] Verify the sigil set (`?`/`!`/`+`) against the derivation chat once
      captured/exported — DUMB_MEDIA's rejected `'` sigil suggests there
      may have been a fuller set (e.g. superseded/retracted)
