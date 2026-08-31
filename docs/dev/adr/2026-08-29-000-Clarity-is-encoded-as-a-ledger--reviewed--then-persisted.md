# Clarity is encoded as a ledger, reviewed, then persisted

**Date:** 2026-08-29
**Status:** Accepted

## Context

`persist-clarity`'s founding run (the `metareasoning-pub` session)
worked, but exposed a gap: the skill went straight from private
judgment to disk. The agent inventoried the session, chose standings,
quoted rulings, and filed four artifacts — and the owner's first veto
surface was a committed diff across four genres. Standing was written
*by the filing agent*, reviewable only after the fact and only by
reading everything.

The owner's redesign sketch:

> ## Clarity
> Encourage agent to build a /llm-claims structure that encodes their "clarity".
> ## Review
> Present to user and integrate feedback, if any
> ## Persistence
> Several strategies for how to "persist clarity".

> In fact, perhaps the "persistence" bit should be tucked under
> skill.kb/, and only referenced from SKILL.md as an after-review
> activity.

The fit is exact: the `Skill(llm-claims)` notation already carries
everything the four residues demand — sigils are standing, strikes
are reversals, `?` claims are opens — and its bank already governs
the two integration points (`when/the-context-or-session-is-ending.md`
obliges serialization with standing; `before/presenting-claims-to-the-
user.md` makes `+` a veto offer, never a sign-off queue). The review
beat costs almost nothing because the render *is* the review artifact.

## Decision

The operation becomes three ordered beats:

1. **Encode** — the session's clarity rendered as a claim ledger
   (`Skill(llm-claims)` notation — a substrate dependency on the
   output format, not an orchestration of a peer). The four residues
   become the ledger's coverage test rather than filing instructions.
2. **Review** — the render presented for rulings. A veto point, not a
   gate — no claim queues for sign-off — ending at the user's
   satisfaction (owner, 2026-08-31).
3. **Persist** — user-elected: "a disk-ledger is optional,
   recommended, but user-decided" (owner, 2026-08-31), so the
   operation may end at the chat render. On go,
   `skill.kb/persistence.md` carries the filing: per-ecosystem homes,
   per-residue landing rules, the narrative address and re-entry
   path, verify-and-commit.

The residue list is re-cut: **opens** join it (they were a separate
"Open threads" section, but they are claim-shaped — `?` — and belong
in the reviewable ledger); the **narrative address** leaves it (it is
path-shaped, not claim-shaped, and lands at the persist beat).

## What moved where

Every part of the incumbent body, its fate — all scheduled now; grep
found no external readers of any section, so no routes needed:

| incumbent part | fate |
|---|---|
| framing (decisions vs. clarity, evaporation) | kept, SKILL.md opener |
| four residues | kept, reframed as encode-beat coverage test |
| residue table (design/debug columns) | obviated — one transfer sentence replaces it |
| re-entry path section | moved, `skill.kb/persistence.md` |
| open threads section | merged into residue 4 (encode) + landing rule (persist) |
| procedure steps 1–2 (inventory, cold-reader test) | kept, encode beat |
| procedure steps 3–5 (file, re-entry, verify+commit) | moved, `skill.kb/persistence.md` |
| homes by ecosystem | moved, `skill.kb/persistence.md` |
| lens-lands-as-normative rule | moved to the persist file; "phrased as a reusable rule" stays in the residue |
| anti-pattern: conclusions-summary | absorbed into residue 1 ("the ledger with the sigils stripped") |
| anti-pattern: parallel structure | absorbed into the persist file's filing stance |
| anti-patterns: dump, journey, polishing | moved, `skill.kb/persistence.md` (polishing's priority rule also stated at encode) |
| description frontmatter | unchanged — the occasions did not change |

## Alternatives considered

### Option A — keep the single-pass procedure (incumbent)
- **Pros:** fewer beats; no render before filing.
- **Cons:** standing is fixed silently by the filing agent, and the
  owner's veto surface is a multi-genre committed diff — the founding
  run's observed cost.

### Option B — make review blocking (require rulings before persist)
- **Pros:** nothing lands at agent standing.
- **Cons:** `Skill(llm-claims)`'s own presentation rule forbids
  rendering `+` as a sign-off queue — rulings cannot be required.
  Declined as stated. The 2026-08-31 ruling then moved the persist
  *trigger* to the user — "the operation can end at chat-ledger" —
  so an unelected persist ends at the render, not in auto-filing.

### Option C — keep persistence in SKILL.md (one file)
- **Pros:** one load; every full run reads the persist text anyway,
  so splitting saves few tokens.
- **Cons:** sequencing, not savings, is the point: the filing detail
  is dead weight during encode and review, and the cold file can
  grow rich landing rules without charging the first two beats.
  Review added the stronger ground — change-rate separation:
  strategy text churns per-ecosystem while the stance stays stable,
  and the split keeps that churn out of the hot body. The split is
  the owner's stated preference; the price argument alone is
  roughly neutral.

### Option D — encode directly into `llm-claims-kb` files, skipping the chat render
- **Pros:** no translation step in claims-ledger projects.
- **Cons:** writes standing to disk *before* the veto point, which is
  the founding gap restated; most projects have no file ledger; the
  chat render is the cheapest review surface there is. Declined.

## Consequences

**Positive:**
- Standing becomes explicit before disk, and the veto point moves
  from diff-review to ledger-review — structured, cheap, one screen.
- Sessions that never kept a ledger get one at the boundary, where
  it matters most.
- The review beat inherits `Skill(llm-claims)`'s bank instead of
  duplicating presentation rules that would drift.
- Rulings arrive in-band, attached to labels; the acceptance quote
  becomes `authority:` at serialization, retiring the founding run's
  after-the-fact transcript archeology for owner quotes.

**Negative:**
- A full run costs one render and one beat of latency before filing.
- Hot body plus cold file total slightly more text than the
  incumbent single file.

**Neutral:**
- The skill now depends on the `llm-claims` notation as its encoding
  substrate. Per `authorship.kb/skills-are-operator-composed.md`,
  naming an output convention is the permitted kind of dependency;
  porting persist-clarity somewhere without llm-claims means porting
  the notation's core block too.

## Related

- Depends on: `docs/dev/claims.kb/design.claims.kb/authorship.kb/skills-are-operator-composed.md`,
  `.../price-text-by-load-frequency.md`
- Related to: `2026-08-28-000-A-skill-states-a-stance--not-a-procedure.md`
  (each beat states what the agent is accountable for; the beats
  themselves are the operation, not a setting-bound checklist),
  `llm-claims/skill.kb/must-read.kb/when/the-context-or-session-is-ending.md`
  and `.../before/presenting-claims-to-the-user.md` (the two
  integration points this design leans on)
- Narrative address: session `b00bf5bc-214b-4952-9282-02677d77709f`
  (branch of `71a95d3e`, project `-home-bukzor-claude-meta-reasoning`) —
  the founding run and, post-compaction, this redesign.
