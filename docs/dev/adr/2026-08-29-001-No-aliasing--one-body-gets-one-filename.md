# No aliasing: one body gets one filename

**Date:** 2026-08-29
**Status:** Accepted — the prohibition is the owner's ruling, quoted
below. The four replacement rules began as agent-authored
generalization from a single anecdote; they were put to the owner as a
batch and ruled unamended on 2026-09-01.

## Context

`llm-must-read-kb`'s "Aliasing" section told authors to symlink when
one body serves several triggers: "Prefer symlinks over duplication;
duplication drifts." The reasoning is sound about maintenance and
silent about reading, which is the cost that actually recurs.

A bank's index is an `ls -RF` of filenames. Every alias is its own row.
The scanning agent has no way to know two rows share a body, so a
matched pair produces two reads and the body lands in context twice.
The owner, from practice:

> "What invariably happens is that claude reads all of them then
> realizes they're identical, after they're already duplicate in
> context."

The personal bank had four aliases, two of them pointing at one body:
`when/evaluating-a-contested-or-subjective-position.md`, aliased as
`before/contradicting-a-previous-response.md` and
`before/retracting-or-conceding-a-claim.md`.

Asked which of those three names actually worked, the owner reported:

> "anecdotally, 'retracting-or-conceding-a-claim' was the most
> effective of those"

That is the second finding, and the more surprising one. The concrete
action-verb slug fired; the abstract description of a situation got
scanned past. Aliasing had made this invisible and self-perpetuating —
symlinks let the *ineffective* name stay canonical while the effective
one looked like a mere alias, so nobody was ever forced to notice which
name was doing the work.

## Decision

One body, one filename. No symlinks, no copies.

When one body seems to serve several triggers:

- **Broaden the canonical slug** until it names the whole family — but
  only while it stays concrete. A slug of action verbs fires; an
  abstract description gets scanned past.
- **Keep the name that fires.** Where one variant's slug has proven to
  trigger reads and a broader description has not, effectiveness
  outranks incumbency; the proven name becomes canonical.
- **Name the remaining occasions in the body's opening prose**, where
  the H1 restates the trigger. The slug fires the read; prose carries
  the variants a slug cannot.
- **Two occasions with no honest broader name are two entries**,
  sharing a `procedures.kb/` method, each trigger file a thin pointer.

## Alternatives Considered

### Option A — keep symlink aliasing
- **Pros:** one body, no drift; every trigger phrasing stays
  individually scannable, which is the whole point of a filename index.
- **Cons:** pays the read cost once per alias, at scan frequency,
  forever. Drift costs an author one edit; duplication costs every
  matching session its context. Decisive.

### Option B — duplicate the body under each filename
- **Pros:** none over A.
- **Cons:** strictly worse — same double read, plus divergence. Already
  rejected by the superseded text.

### Option C — broaden every slug to the abstract superset
- **Pros:** mechanical rule, no judgment call, guaranteed one row.
- **Cons:** the anecdote is the counterexample.
  `evaluating-a-contested-or-subjective-position` *is* the honest
  superset of retracting/conceding/endorsing, and it is the name that
  failed to fire. Abstraction buys coverage and spends recognition.

### Option D — keep aliases, but mark each with a pointer to the canonical
- **Pros:** preserves multi-name retrieval; the agent could stop early.
- **Cons:** the agent must read the file to see the marker, and by then
  it has paid. This is the skill's own rule against gating recognition
  behind the thing being recognized ("a trigger cannot gate the
  knowledge that fires it").

## Consequences

**Positive:**
- Index rows and distinct bodies are one-to-one, so the bank's scan
  cost is honest and a matched trigger costs one read.
- Name effectiveness becomes observable: with one name per body, a
  trigger that never fires is a fact about that name.

**Negative:**
- Retrieval breadth now rests on a single slug plus opening prose. A
  body with two genuinely unrelated occasions costs a split and a
  `procedures.kb/` indirection where a symlink used to cost one line.
- The generalization rests on one reported anecdote about one file.
  It matches the pattern the skill already assumes (filenames are
  scanned, bodies are not), but it has not been measured.

**Neutral:**
- Applied to the personal bank the same day: four symlinks removed,
  and `when/evaluating-a-contested-or-subjective-position.md` renamed
  to `before/retracting-or-conceding-a-claim.md`, with the mirror
  motion (endorse, validate) carried in its opening prose. Two days
  later the owner renamed it again, to
  `before/asserting-or-conceding-a-claim-of-judgment.md`, promoting
  the mirror motion out of the prose and into the slug: prose is where
  a variant waits, not where it belongs once it turns out to be the
  primary occasion. Evidence that "one name" is a live constraint an
  owner keeps adjusting, not a one-time act — which is the cost this
  ADR accepts in exchange for one index row.
- One dangling reference to a removed alias survives in a 2026-08-21
  devlog. Left as-is: history records what was true then, and the
  rename made that path real again anyway.

## Related

- Supersedes the "Aliasing" section of `llm-must-read-kb/SKILL.md`;
  replaced by "No aliasing" in the same file.
- Design successor to this skill is `Skill(llm-triggers)`; the rule
  belongs to whichever governs the bank's shape.
- Narrative address: session `c78bbbb7` (2026-08-28/29), the
  `/review-open-questions` improvement pass; devlog
  `2026-08-29-000-The-sweep-sheds-the-asking-law.md`.
