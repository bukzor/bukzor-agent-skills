---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    "@value": 4.5
    rationale: |
      Three inline improvement items: bin/ script CWD-vs-path bug
      (~1h, same root cause as llm-collab bug), todo.kb/ideas.kb
      template boilerplate trim (~0.5h, both skills affected), tier
      selection guidance push toward lightest tier (~1h, requires
      SKILL.md update with heuristic). Plus the schedule dimension
      (~2h: placement ruling, duration shape, consumer updates in
      wsjf-rank and claude-open-tasks-list), which is blocked on
      lead-times promoting to a .kb/ and so may not start in window.
    confidence: tentative
  benefit-2w:
    "@value": 0.5
    rationale: |
      Per-session UX improvements affecting every llm-subtask
      invocation. Modest individual, flowing across all sessions
      that use the skill.
    confidence: tentative
  cost-of-delay-2w:
    "@value": 0.2
    rationale: |
      Each item is a per-session tax: bin/ scripts mangle filenames
      silently, templates waste agent attention, heavyweight tier
      defaults waste effort. Flowing taxes across all skill uses.
    confidence: tentative
---

- [ ] Two one-sentence rules, both agent-proposed 2026-08-31 and both
      awaiting the owner's word before they land as normative text:
  - [ ] Before minting a frontmatter field, grep for what already
        reads one. A repo minted `user-minutes:` for a cost axis
        `cost-benefit-sweh.timebox` already carried, and its whole
        backlog rated `unrated` in `wsjf-rank` while looking priced
        locally — green in the repo, absent from the list the owner
        chooses from. Worked instance:
        `private.meta-reasoning-corpus` devlog `2026-08-28-003`
  - [ ] `todo clear` greps a closed item's key phrase before deleting
        it; extend that to the item's declined alternatives and
        revisit conditions, which carry different phrases. A discharged
        todo took `Revisit once a remote exists — pushed is a fine
        check` with it, and the condition survived only because an
        unrelated session had quoted the doctrine into a devlog
- [ ] Schedule dimension: the schema rates effort, never wall-clock.
      `cost-benefit-sweh` carries `timebox`, `benefit-2w` and
      `cost-of-delay-2w` — all effort or value, none calendar — so a
      task with 1h of effort sitting behind a six-week government
      process prices as cheap and reads as cheap. Three candidate
      fields: a duration (`lead-time`) and two instants (`anchor`, when
      the blocking process actually started, and `needed-by`, the
      commitment). Projections stay derived rather than stored:
      `needed-by − lead-time` is the latest start, `anchor + lead-time`
      the finish. Raised 2026-09-02 against
      `private.bukzor-llc/lead-times.md`, which holds the shared vendor
      and government durations such a field would cite.
  - [ ] Rule the placement: inside `cost-benefit-sweh` or beside it?
        Beside, on the argument that lead time doesn't change priority
        — a cheap task blocked on the world already ranks high under
        WSJF, correctly. What's missing is the scheduling question
        ("when must I start"), which is not the ranking question
        ("what next")
  - [ ] Shape the duration to accept either a reference into a shared
        duration ledger, where a repo happens to keep one, or an
        irreducibly local value ("how long until the owner decides"),
        recording which — a derived number should recompute when its
        ledger moves, a declared one shouldn't. Most repos will have no
        ledger at all, so the reference form must be optional and the
        declared form must lose nothing
  - [ ] Make absent mean zero, and find another way to say "not
        assessed". Most tasks have no lead time; the schema shouldn't
        tax them for it
  - [ ] Grep the consumers before minting anything — `wsjf-rank`,
        `claude-open-tasks-list`, `task-list.md` — per the
        field-minting rule already in this file
- [x] Batch the three SKILL.md/skeleton UX-flow items below into one pass
  (same class of fix, each a small per-session tax; do together rather
  than as three separate touches — 2026-07-09 forward-looking review).
  Done 2026-07-19, all three below:
  - [x] todo.kb AND ideas.kb templates too boilerplate-heavy — trimmed
        both skeleton examples to title + frontmatter + blank sections,
        no bracketed placeholder prose; also fixed ideas.kb example
        missing `status: template` (todo.kb example already had it)
  - [x] Tier selection guidance too weak — added a "default to lightest
        tier" paragraph right after the four-tier list in SKILL.md, with
        the proposed heuristic and sub-bullet policy note
  - [x] Guidance on which repo owns a todo in multi-repo setups — new
        "Cross-Repo Ownership" section in SKILL.md, citing the
        breadcrumb-checkbox pattern

## Later

- [ ] todo.kb/2026-02-10-000 (Milestone/phase planning pattern gap) — discussion invited
