# Devlog: 2026-08-18 — Review-in-place: the census retired as a concept, not just an instance

## Focus

Yesterday's fold retired the census *instance*; today's session asked
whether the census *concept* should exist, walked a greenfield layout
of the epistemic skill cluster, and mapped it back onto the incumbents.
The planned deliverable (a census skeleton + fold procedure + two
trigger/doc pairs in /align) collapsed to two short edits and two
ledger claims.

## Decisions

### Review-in-place replaces the staging register (IN_PLACE)

**Rationale:** The user's retrospective doubt — "not sure the
review-ledger was useful enough to exist" — sent us back to
review-open-questions' Registers section, which already commands
writing survivors into the register the work keeps. The census had
*violated* its own cited basis by minting a register beside the homes.
The replacement is three existing mechanisms: `standing: agent` *is*
review state; git is the staging layer (diff = scope, revert =
wholesale rejection, merge = reconciliation complete); the standing
scan is the backstop when a review outlives its diff. Empirical
warrant: every census part that wasn't a durable claim proved
redundant at fold time, and the fold session itself was the staging
toll. Recorded as `design.claims.kb/a-claim-is-born-in-its-durable-ledger.md`;
enacted as a paragraph in review-open-questions' Registers section.
**Alternatives considered:** the full census machinery (skeleton,
fold procedure, staging lifecycle in review-open-questions) — designed
in this session, then defeated by the above before any of it was
built.

### Greenfield topology: skills are domains, occasions are triggers (DOMAINS)

**Rationale:** The skill/trigger boundary question dissolved once two
fused variables were separated: domain of law vs. unit of retrieval.
Six domains cover the cluster — claims (record), review-open-questions
(court), the lens skills (distill), llm-kb (collections),
must-read/llm-triggers (routing), llm-collab (chronicle). New
capability = new trigger in the owning domain, not a new skill.
Recorded as `authorship.kb/skills-are-domains-occasions-are-triggers.md`.
**Alternatives considered:** reifying "distill" as a real skill
merging align/formalize/deformalize — declined: the user's
session-persistence seam argument, plus formalize/deformalize were
reworked days ago and merging fresh work is manufactured churn.

### Rulings taken this session (user)

- distill and adjudicate stay separate skills: each is involved enough
  to want a session/persistence seam, and adjudication occurs without
  distillation.
- devlog survives as its own axis: the narrative third place for what
  fits neither code comments nor commit messages. ADR is probably
  subsumed by `design.claims.kb` (`verdict:` + `authority:` now carry
  the ruling; ADR's residue is narrative, i.e. devlog-shaped) —
  **punted**, on the record.
- `must-read.kb` is llm-triggers' running mechanism; the layout builds
  on it as-is.

## Conventions Established

- The bins of `align/SKILL.kb/sort-goals-into-four-bins.md` are also
  destinations: rules/heuristics → a `force:`-graded principles
  collection; short-term plan → descriptive claims in their theories;
  long-term plan → `open` questions beside theirs.
- /align's Ask step delegates any nontrivial batch to
  `Skill(review-open-questions)`.
- Decision-space for mapping greenfield onto incumbents: where a
  capability lives / what it is called / how old readers are routed /
  now-or-later; "adjust vs reform vs replace" is derived from those
  four, and a punt is a ruling that wants the record.

## Open Questions

- Fold llm-claims-kb into llm-claims (punted; cheap once llm-triggers
  matures).
- formalize/deformalize merge — on strain only.
- ADR → ledger + devlog fold (punted, above).

## References

- b7b89c0, ae1dee3 — the census's creation and fold (the evidence)
- 2026-08-17-001 devlog — the fold session
- `~/.claude/must-read.kb/when/redesigning-something-that-already-exists.md`
  — supplied the variable-separation move and the preservation audit
