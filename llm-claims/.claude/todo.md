# TODO

- [ ] Review how ontology cascades — ruled vs wanted. The owner,
      2026-09-01: "I don't think that's how ontology cascades, or not
      how it should, at least." The ruled form is CONTAINMENT_ADMITS
      (`design.claims.kb/ownership.kb/containment-admits-without-an-arrow.md`,
      standing bare): a descendant reads every word its container
      stipulates, no arrow needed; `ledger.py`'s `Theory.container`
      docstring restates it and the ownership law computes with it.
      Reconcile that against the owner's doubt. The outcome also sets
      the scope rule for `non-claim-tokens:` — NON_CLAIM_FIELD
      (`design.claims.kb/notation.kb/the-non-claim-list-rides-the-defining-claim.md`)
      holds the minimal reading (declaring theory's interior) until
      this rules
- [ ] Wire design.claims.kb's `why:` edges: 27 claims carry only 3
      `why:` edges -- ccomps reports 25 components (found 2026-08-09 by
      the new llm-claims-kb/bin/llm-claims-kb-graph; its SKILL.md
      names arrows-in-prose-not-frontmatter as the failure the file
      form exists to prevent). The support structure exists in the
      bodies; move it into frontmatter so the graph tools and the
      "ledger gains lint" leg below have something to check
- [ ] .claude/todo.kb/2026-08-06-000-Rebase-llm-design-kb-on-the-claim-ledger.md
      — the plan: llm-design-kb becomes a discipline over the ledger;
      ledger gains lint, footnote provenance, file-per-claim + self-audit
      conventions; all legs (including other-scope ones) tracked there
- [ ] .claude/todo.kb/2026-08-08-000-Helper-command-family-bin-llm-claims.md
      — requirements for `bin/llm-claims-*` (shared parser, lint,
      attention, poset, replay + provenance-map convention), distilled
      from the prototype.llm-stet serialization audit; details the
      rebase plan's "ledger gains lint" leg
- [ ] Settle `design.claims.kb/notation.kb/how-decided-but-unbuilt-intent-is-marked.md`
      (DECIDED_UNBUILT, `open`) -- TBD, current proposal there is a
      strawman, not a decision
- [ ] USER: re-paste the SKILL.md Core block into claude.ai preferences
      (verbatim-shared; pending since 2026-07-24 — the `+` sigil, the
      governance line, the open-claims policy, and a worked example in
      place of the self-describing one; 2026-07-28 — `<-` no longer
      claims "entailment", per `skill.kb/must-read.kb/when/writing-or-reading-an-arrow.md`;
      2026-08-15 — policy 4, every render is a patch)
- [ ] Give `good-smells.kb/` something it can fail. All 11 entries were
      read off the finished notation in one conversation, so the notation
      satisfies every one by construction and 8 stand at `open`. A
      criterion nothing can fail is a description, not a criterion. Two
      tests, cheapest first:
  - [ ] Score the criteria against the alternatives this design already
        rejected — `superseded` as a status, `obligated` as a status, the
        `'` sigil, node types beyond claims, formal entailment arrows.
        Several are recorded as foils in `design.claims.kb/notation.kb/`
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
        or `skill.kb/` rather than being deleted. `NAME_LOCUS` degenerates
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
- [ ] Admit unambiguous brace notation in an `ontology:` entry:
      `{pre,post}-fixed point` expands to two words, so one entry can
      carry a shared stem without the checker reading the whole string
      as a single term. Field case: `docs/dev/claims.kb/strata.claims.kb/fixpoint.md`
      wrote `pre-/post-fixed point`, which no claim can match verbatim
      and which the ownership scan therefore reported as never spoken,
      while `fixpoint.kb/` says "pre-fixed points" and "post-fixed
      point" in as many words. Slash-bundling should be rejected once
      braces are accepted
- [ ] Work the trespass docket: 252 findings over 121 stipulations
      (`llm-claims-kb-ownership --trespass`), 88 in
      `docs/dev/claims.kb/strata.claims.kb`. Take them in `--candidates` cull
      order — the heaviest stipulations are ambient words SHOULD_OWN
      says not to own, so culling clears findings in bulk before any
      per-finding repair is worth choosing
- [ ] Tighten `--candidates`' own side: `phi`, `defeated`, `collapsed`,
      `wrestled` are false positives at floor 8. Candidates are 2/3
      precise today; the cull side is clean
- [ ] USER (2026-08-30): reconsider `superseded-by[]` for out-of-force
      claims — "I suspect that ruling is flawed or outdated." The
      standing ruling is llm-claims-kb SKILL.md's "What this is not":
      the graph's `superseded-by:` does not translate to the ledger
      because "a ledger names [the successor] in the body, and the
      successor's label is what `grep` finds." What prompted the
      reconsideration: private.bukzor-llc's `strategy.jsonschema.yaml`
      adopted path-valued `superseded-by` the same day, because on
      unlabeled docs the field buys a machine check body prose cannot
      (validator insists a superseded doc names an existing successor)
      — the same argument may apply to `verdict: superseded` claims
      (and the graph's `live: false`), where nothing today checks that
      a replacement is actually named. The user's spelling
      `superseded-by[]` suggests array-valued (one claim replaced by
      several). Ruling lives in llm-claims-kb; filed here per the
      user's pointer
