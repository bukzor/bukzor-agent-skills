---
managed-by: Skill(llm-subtask)
status: open
---

# Reconcile llm-claims-kb's Standing Scheme with PRMS's stmt/proof and STANCE's Assessor-Relativity

**Priority:** Not urgent -- both threads it merges are pre-existing and
deliberately deferred, not on fire. But block any further ad hoc patching
of `standing:`/`verify:` until this lands; today's session nearly did that
before catching itself.

**Complexity:** Large. Breaking schema change across every `.claims.kb/`
in the repo (`llm-claims`, `formalize`, `deformalize`,
`docs/dev/claims.kb/design.claims.kb`, `docs/dev/claims.kb/strata.claims.kb`), plus a
cross-repo question (whether/how to absorb `prototype.personal-reasoning-management`'s
dialect). Comparable in shape to the `defeated-by:` -> `stale-when:`
migration (`docs/dev/devlog/2026-08-13-000-...md`), likely bigger.

**Context:** Surfaced 2026-08-16, mid-conversation, trying to add
`retracted`/`rejected` as claim dispositions for `Skill(llm-claims-kb)`.
What started as "add a field" turned out to be the intersection of two
already-tracked, already-deferred design threads. Recommended shape for
doing this properly: a `/formalize` pass, now that it exists.

## Problem Statement

`Skill(llm-claims-kb)`'s claim schema (`claim.jsonschema.yaml`) treats
`standing:` as a single, hand-authored, four-value field (`bare | open |
agent | user`), with a separate `verify:` field for the re-runnable
check backing a certified claim. Three things this session found wrong
with that picture, all real, none new:

1. **No representation for a negative verdict.** A claim that was
   proposed and declined, or that stood and was later withdrawn, has to
   be deleted -- which breaks `grep`-ability and makes the deletion
   indistinguishable from a `why:` authoring bug (`dangling()` reports
   both identically). Chat notation's `~~XY~~` already covers this in
   chat form; file form has no equivalent.
2. **`open` isn't a judge, it's a verdict.** `bare`/`agent`/`user` name
   *who* judged; `open` names that *no one has yet*. Conflating "who"
   and "which way" into one four-value enum is why the schema had no
   room for a negative-verdict axis to begin with.
3. **`judge:` (the proposed replacement for who-judged) could
   generalize to a path** -- naming the runnable check that judges a
   claim, not just `agent`/`user` -- which turns out to already be
   `prototype.personal-reasoning-management`'s `stmt:`/`proof:` fields,
   a "strong form of `verify:`" per `.claude/todo.md:273`, already
   flagged for evaluation and never acted on. That todo item also names
   "computed standing (the engine derives status; corpus records only
   `bare` and `!`)" -- PRMS doesn't hand-author most of its standing at
   all.

Separately, and not to be conflated with the above but bearing on the
same field: `STANCE` (`docs/dev/claims.kb/strata.claims.kb/standing.kb/standing-is-standing-according-to.md`,
ratified `32b1a76`) already rules that a one-place "the standing" of an
entry is a category error -- standing is a two-place function of
evidence *and* stance/assessor, with no global arbiter even in
principle. `.claude/todo.md:189` names the same seam as still dormant:
"goes live the first time two assessors disagree about one claim,"
with `CONTINUUM` (`llm-discourse-graph`'s assessor-keyed presentation)
named as the escape valve. Any redesign of `standing:` that hardens a
single-assessor assumption further makes that seam harder to close
later.

## Current Situation

- `llm-claims-kb/jsonschema/claim.jsonschema.yaml`: `standing:` enum is
  `[bare, open, agent, user]`, required. `verify:` is a separate,
  optional string field.
- `Skill(llm-claims)`'s chat notation: `?`/`+`/`!`/bare sigil, plus
  `~~XY~~` for retraction (undifferentiated -- one marker for any
  "no longer holds," no distinction between a declined proposal and a
  withdrawn standing claim) and a `-- suffix` mechanism already used for
  `-- certified(CHECK)` and `-- authority: ...`.
- `prototype.personal-reasoning-management/corpus/demo.prms.kb/`: real,
  working example of `stmt:`/`proof:` (e.g. `proven.md`: `stmt: 2 + 2 =
  4`, `proof: decide`) and computed (not hand-authored) standing.
- `docs/dev/claims.kb/strata.claims.kb/standing.kb/` and `fleet.kb/`: `STANCE` and
  `CONTINUUM`, the formal statement of assessor-relative validity and
  its named escape valve.
- One claim in this repo has already been retracted in file form ahead
  of any of this landing (`formalize/design.claims.kb/run.kb/what-the-stopping-rule-is.md`,
  `STOP`) -- `standing: user` was kept as the closer fit for lack of
  anything better, explicitly flagged as provisional at the time.

## Proposed Solution (sketch only -- this is what the /formalize pass should test, not a pre-committed answer)

Split `standing:` into two fields:

- **`verdict:`** (always present): `open | accepted | rejected |
  retracted | dissolved` -- or possibly fewer, see Open Questions.
- **`judge:`** (present only when a real judge acted): `agent | user |
  <path>` -- the path case folding `verify:`'s job in, unifying with
  PRMS's `proof:`.

Chat-form mapping, reusing the existing suffix mechanism rather than
inventing new sigil characters:

| Chat | File |
|---|---|
| (bare) | `verdict: accepted`, no `judge:` |
| `?` | `verdict: open`, no `judge:` |
| `+` | `verdict: accepted`, `judge: agent` |
| `!` | `verdict: accepted`, `judge: user` |
| `~~XY~~: text` | `verdict: retracted` |
| `~~XY~~: text -- rejected` | `verdict: rejected` |
| `~~XY~~: text -- dissolved` | `verdict: dissolved` |

## Open Questions

- **Does the three-way negative split (`rejected`/`retracted`/
  `dissolved`) earn its keep in chat form**, or only in file form
  (accepting that `flatten` collapses all three to a bare `~~XY~~` on
  the way out)? `dissolved` in particular was derived from one instance
  (`STOP`), not requested.
- **Do `rejected`/`retracted`/`dissolved` unify further, differing only
  in the delta between authoring and judging** -- rejected/retracted as
  one axis (was there ever a prior accepting verdict: no vs. yes), with
  dissolved on a genuinely different axis (a well-formedness verdict,
  not a truth verdict, so it may not belong on the same axis at all).
  Raised 2026-08-16, not worked through.
- **Should `judge:` ever hold a value beyond `agent | user | <path>`**,
  given `STANCE` says the judge/assessor space isn't closed -- does a
  path-shaped judge (a check) need the same assessor-relativity a
  person-shaped judge does, or is a mechanical check exempt by
  construction (its verdict is the same for every stance)?
- **Fork vs. specialization**: is PRMS's dialect a distinct format that
  `llm-claims-kb` documents a mapping to/from (`Skill(llm-claims-kb)`'s
  own "What this is not" pattern, used today to distinguish it from
  `llm-discourse-graph`), or does `llm-claims-kb` grow the capacity to
  represent PRMS-shaped claims directly?
- Counterpart item noted in PRMS's own todo ("field-name convergence
  sketch," per `.claude/todo.md:273`) -- read it before designing, it
  may already have a proposal.

## Success Criteria

- [ ] A ruling (ADR-shaped, matching the `defeated-by:`->`stale-when:`
      precedent) on the schema change, before any migration starts.
- [ ] `STOP`'s `standing: user` corrected to whatever the new scheme
      says a dissolved-question verdict looks like.
- [ ] Migration plan for every existing `.claims.kb/` in this repo (see
      Current Situation for the list), sized and sequenced.
- [ ] An explicit ruling on the PRMS-dialect question (fork vs.
      specialization vs. absorption), not just a schema change that
      happens to make PRMS's fields expressible.
- [ ] `STANCE`/`CONTINUUM` checked against the final design: does the
      new `judge:`/`verdict:` shape make the single-assessor seam easier
      or harder to close later, when it does go live?

## Notes

Candidate first step: run `/formalize` on this problem itself --
`llm-claims-kb/jsonschema/claim.jsonschema.yaml`,
`prototype.personal-reasoning-management/corpus/demo.prms.kb/`, and
`docs/dev/claims.kb/strata.claims.kb/standing.kb/` + `fleet.kb/` as the paths.
Fittingly recursive: the tool built this session, pointed at the
question that stopped this session's own schema patch.
