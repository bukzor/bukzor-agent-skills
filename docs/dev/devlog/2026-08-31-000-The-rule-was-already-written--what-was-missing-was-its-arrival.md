# Devlog: 2026-08-31 — The rule was already written; what was missing was its arrival

## Focus

Tail of the llm-design-kb reform. Three asks from the owner: record the
LABEL_FORMATS ruling and scan for docs running counter to it, answer
whether the duplicate STANCE label is a problem, and update the
`llm-kb` docs on default values. Two of the three turned into
corrections of my own work rather than new work.

## Decisions

### A claim has two name renderings; only the definition site is qualified

`LABEL_FORMATS` (`standing: user`): a mention may drop the sigil and
the `(todo)`, and probably should; fully-qualified is required only
where the claim is stated. `llm-claims/SKILL.md` said the opposite —
"Sigils travel with the label" — which licenses a corpus of
standing-copies that no tool refreshes, disagreeing with itself on the
day a claim is re-signed.

**The file form had already ruled this way.** `why:` entries are bare
references "never carrying a copied sigil"; `flatten` computes the
sigils it prints in arrow clauses; `mentions.py` matches bare labels.
The chat notation was the straggler, and the scan for counter-running
text found exactly one passage.

**Rationale:** a sigil away from the definition site is a cache with no
invalidation. **Alternative declined:** require the qualified form
everywhere — reads as rigor, buys a corpus that cannot be swept.

### Naming conflicts resolve by the naming law, not by seniority

Two claims carried `STANCE`, and `principles.kb/fields-are-orthogonal-axes.md`
imports the strata one, so one flatten rendered both — `STANCE+` defined
at line 19, `STANCE!` cited at line 43, two different claims that a
reader resolves by scrolling to the wrong one.

I first recommended renaming the *strata* claim, tiebreaking on arrival
order and re-signing cost. The owner's correction: **"use rationality
not seniority to deciding naming conflicts."** Re-derived from
NAME_LOCUS, every criterion inverts the answer:

- a label names the locus of contention, not the conclusion. The
  design-side claim contests *what form a skill body takes*; stance was
  its answer and procedure the loser, so `STANCE` named its verdict —
  a defect present since it was minted, which the collision merely
  exposed;
- `strata.claims.kb/standing.md` stipulates `stance` in its ontology
  and its body defines it. `authorship.md` does not coin it and uses it
  as ordinary contrastive English;
- confinement is per-ledger, so the pair is formally out of
  jurisdiction — but the import is what puts both in one render, which
  is where that exemption stops protecting the reader.

Renamed to `BODY_FORM`, which names the question rather than either
answer. The sweep was one line; the cost argument I had leaned on was
never load-bearing.

### A schema must accept the materialized form of its own default

I shipped `todo: {const: true, default: false}` and the owner rejected
it: "Think of what *data* a schema-aware system should receive." A
consumer that fills defaults and round-trips would emit `todo: false`
and fail the schema that produced it.

`llm-design-kb/jsonschema/layer-entry.jsonschema.yaml` had written that
argument down already, for `why: []` — and **I had read that file in
this same session**. It was buried in one field's description in one
legacy schema. So the repair was `llm-kb/references/schema-design.md`,
which had no `default:` guidance at all: the coherence test stated
mechanically, both failing shapes, the legal look-alike (a default
naming one `oneOf` branch), and the zero-migration corollary. A scan of
all 15 `default:` occurrences in fleet schemas found no other violation.

## Conventions Established

- **Before writing a doc to close a gap, check whether the rule already
  exists and is merely arriving at the wrong time.** Twice this session
  the governing text was in my context and I erred anyway. Both repairs
  moved knowledge to the point of use — a lint string, an
  authoring reference — rather than restating it. Reaching for a new
  doc would have made the corpus longer without making either error
  less likely.
- **A lint states a test, not a verdict.** The duplicate-label lint now
  appends `TIP: both labels should name their own claim's locus of
  contention.` It took three drafts: my first said the label "stays
  with the claim whose contention it names", which presumes a squatter —
  and the function's own docstring already knew better, since two
  ledgers may each be named right and collide only on import. Owner
  trimmed the rest: a trailing clause about what to do when both pass
  was extraneous once the criterion was stated, and "not its
  conclusion" was anti-pattern enumeration the positive form already
  excludes.
- **Placement beats phrasing for anything meant to catch an agent
  mid-decision.** The lint fires exactly when the condition holds and
  costs nothing otherwise. Rejected: a `must-read.kb/when/` entry
  (bills every `llm-claims` load forever for a rare event), a corollary
  on NAME_LOCUS itself (its own home, and nobody reads it at collision
  time), a paragraph in the SKILL.md rename section (read after the
  decision is already made).

## Open Questions

- Three agent judgment calls shipped unruled, all listed in
  `.claude/todo.md`: the `BODY_FORM` coinage, LABEL_FORMATS's
  definition-site paragraph, and the proposed weld in
  `claim.jsonschema.yaml`'s `label:` description.
- A third `STANCE` exists (`llm-claims/claims.kb/design.claims.kb/stance.md`),
  legal under per-ledger namespaces and not colliding, since llm-claims
  never imports strata. Latent only. Likewise `grep STANCE` matches
  `NO_INSTANCES` — a substring collision the prefix rule does not
  forbid. Neither has a forcing function; recorded here rather than
  filed.

## References

- Commits: `fe3b475` (LABEL_FORMATS), `a0969a4` (schema defaults),
  `6dbdc4c` (BODY_FORM), `a9ba30d` → `3cd6a7f` → `648a14a` (the lint tip,
  three drafts)
- `docs/dev/adr/2026-08-28-000-A-skill-states-a-stance--not-a-procedure.md`
  — the ADR behind the renamed claim; keeps its name as provenance
- `llm-claims/claims.kb/design.claims.kb/notation.kb/how-decided-but-unbuilt-intent-is-marked.md`
  — where the `const: true` rejection is recorded
