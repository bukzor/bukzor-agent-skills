---
managed-by: Skill(llm-subtask)
status: done
related-effort: ./2026-08-21-000-ref-rollout-beyond-todo-ideas.md
suggested-reading:
  - ./2026-08-21-000-ref-rollout-beyond-todo-ideas.kb/2026-08-21-001-layer-entry-canonical-recommendation.md
cost-benefit-sweh:
  timebox:
    "@value": 2.0
    rationale: |
      Five rulings, each an agent-written recommendation plus a user
      verdict. The agent time is the research; the decision is minutes.
      Past 2h the recommendations are being written too long -- the
      layer-entry precedent settled in one page.
    confidence: unsure
  benefit-2w:
    "@value": 1.0
    rationale: |
      Three of the five unblock mechanical work in other lanes. The
      other two decide whether recurring guards keep running at all,
      which is worth more than two weeks can show.
    confidence: unsure
  cost-of-delay-2w:
    "@value": 1.0
    rationale: |
      Highest of any lane: undecided rulings hold up the lanes that
      depend on them, and a fan-out that hits one mid-flight either
      stalls or guesses. Decide these first.
    confidence: confident
---

# Fleet rulings that gate the schema lanes

**Priority:** First. Three of the five gate mechanical work elsewhere.
**Context:** residual of the 2026-08-21 `$ref` rollout. These are the
items the rollout deliberately handed up rather than defaulting, because
each legislates for the whole fleet rather than for one tree.

Precedent for the shape: `claims` gained `live:`/`superseded-by:` in
2026-08-21 after an agent wrote the case and the user ruled -- and the
verdict was **not** the one the write-up proposed. Write the
recommendation; do not act on it.

## The five

### 1. Does the decision-lifecycle trio earn its own canonical?

`status` / `blocked-on` / `superseded-by` appear as three hand-synced
copies across cluster 1, and were deliberately left out of the
`layer-entry` canonical rather than folded in. Same question the trio's
exclusion deferred: shared shape, or coincidence of three authors
reaching for the same three words?

### 2. Do the four canonical-less collections want a canonical?

`research.home-office/use-cases.kb`,
`summer-programming-project/.../curriculum.kb`, and
`github-manager/{goals,maintenance-actions}.kb`. The recurring guard is
silent on them **by construction** -- it globs published canonicals, so a
collection with none is invisible to every sweep. That invisibility is
the finding; whether each wants a canonical is the ruling.

### 3. Do `deductions` and `questions` want the `live:` axis?

`claims` gained `live: bool` + `superseded-by: path[]` on 2026-08-21. A
claim's death often strands the deductions resting on it, and a question
can stop mattering without being answered. Deliberately not done at the
time: there was no observed instance, and legislating the shape of three
collections from evidence about one is how the original conflation got
in. Rule on whether that still holds.

### 4. Do the recurring guards get a schedule?

Ten of the 42 findings in the last residual sweep were already in the old
scope and the old root -- six weeks of ordinary drift on a guard that
only runs when someone happens to open a migration. A hook, a cron, a
`/session-end` step, or an explicit "on demand only". **A `kind:
recurring` migration nobody runs is a `complete` one that lies.**

### 5. Should the guard's roots include `~`?

Coverage of the dotfiles repo today is an accident: `~/repo/.../dotfiles`
happens to sit inside a scanned root, which is the only reason
`~/.vim/.claude/` was ever seen. Anything dotfiles tracks at top level
outside `~/repo`, `~/claude`, `~/.claude` is invisible by construction.
Weigh against what `~` drags in.

## Arriving from other lanes

- **`prototype.chatfs` enums** (lane -002): `status: exploring|active`
  and `kind: investigation` sit outside closed enums. If the ruling is
  "widen", the canonical edit lands here, not there.
- **The rival marker's shape** (lane -003): comment-with-prefix or a real
  schema key. Decide there if it stays a local convention; bring it here
  if it becomes fleet vocabulary.

## Delegation

- **This lane produces recommendations, not changes.** One file per
  ruling under a sibling `.kb/`, in the shape of
  `2026-08-21-001-layer-entry-canonical-recommendation.md`.
- **Never write to `*/jsonschema/`.** No canonical is created, edited, or
  deleted by this lane. The verdict authorizes the edit; the edit happens
  in the lane that needed it.
- **Never default a ruling because the recommendation seemed obvious.**
  The one precedent went the other way.
- **Parallel-safe with:** every lane, since it writes only prose here.
  But its *verdicts* gate -002 and -003, so run it first.

## Success Criteria

- [x] Five written recommendations, each naming its declined alternative
- [x] Five user verdicts recorded
- [x] Every lane that was waiting on one knows which way it went
