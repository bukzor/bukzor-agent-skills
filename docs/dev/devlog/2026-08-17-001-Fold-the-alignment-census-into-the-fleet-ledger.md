# Devlog: 2026-08-17 — Fold the alignment census into the fleet ledger

## Focus

Settle the question: should `docs/dev/align.claims.kb/` (the
2026-08-16/17 alignment census, b7b89c0) be folded into prior kbs, or
stay a long-term resident? User closed the census's review — "finished,
for the time being" — which unblocked acting on the answer (ae1dee3).

## Decisions

### The constitution moves to the fleet ledger; the census retires

**Rationale:** The census's own charter declared its contents per-batch
and disposable once reconciled, but its nine basal principles were
"timeless design rules" — durable law in a disposable container.
`design.claims.kb`'s charter ("the rules its skills are written under")
is their exact description, so they became the new CONSTITUTION theory
at `design.claims.kb/principles.kb/`, standings preserved as ruled
(ORTHOGONAL user-signed; the rest `agent`, veto still open). EXECUTION,
the one open question, moved to `extension.kb/` beside the
migration-plan it cites — an open question outlives the review that
raised it.
**Alternatives considered:** Keeping `align.claims.kb/` as a durable
per-batch slot (its CLAUDE.md's own proposal) — rejected: nothing
routes there (zero external references; even `align/SKILL.md` doesn't
name it), and an empty `.kb/` reads as an open theory under
llm-claims-kb semantics. `llm-design-kb/principles.kb/` as the
principles' home — rejected: that bank ships with the skill to every
consumer; these principles bind this fleet's work.

### The plan residue dissolves without a move

**Rationale:** `short-term-plan.kb/` and `long-term-plan.kb/` were
views over commitments that already live in their own ledgers: the
chosen yaml is carried by the shared jsonschema and the notation
ledger's SUGAR wording ("one-entry sugar of the assessor-keyed map");
the assessor-collision tripwire is in llm-claims's helper-commands
todo. Verified each before deleting.

## Conventions Established

- A census's durable output is law and open questions; both get homes
  in the real ledgers before the census clears. If `/align` wants a
  standing census location, that convention belongs in `align/SKILL.md`
  (currently unwritten there), not in a resident directory.
- A collection needing an extended claim schema carries it as its own
  `$COLLECTION.jsonschema.yaml` (here: claim + `force:`, the census's
  fork, now `principles.jsonschema.yaml`).

## Open Questions

- EXECUTION (`extension.kb/when-does-the-reform-execute.md`) is still
  `standing: open`: does the batch carry the llm-discourse-graph reform
  itself, or is "decide and record" the whole deliverable?
- Eight of nine principles remain `standing: agent` — adopted into the
  ledger, not yet user-signed.

## References

- b7b89c0 — the census and the batch it reviewed
- ae1dee3 — the fold
- `llm-claims-kb-graph` reports cross-ledger `why:` arrows as dangling
  (tool limitation, targets verified on disk); a future lint could
  resolve across ledgers.
