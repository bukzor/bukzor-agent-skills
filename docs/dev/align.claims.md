---
label: ALIGN
standing: agent
ontology:
  - principle
  - plan
  - force
  - batch
stale-when: the 2026-08-16/17 batch commits -- the census's subject is frozen, rulings live in the real ledgers, and this ledger is disposable
---

# The principles the 2026-08-16/17 batch embodies -- an alignment census

Basal design rules first: `align.claims.kb/` holds the few timeless
principles the batch's decisions derive from, written as imperatives
-- a constitution for future work -- each graded `force:` (RFC 2119
per llm-design-kb's technical-policy: `must` non-negotiable,
`should` deviate only with recorded justification, `may` drop
without ceremony). What the principles do not themselves motivate
lands in two residue collections: `short-term-plan.kb/` -- the
specific yaml settled for now -- and `long-term-plan.kb/` --
deferred structures and open questions. Residue is descriptive and
carries no force.

Every claim is the agent's extraction of *your* intent --
`standing: agent`, veto invited -- with `why:` arrows to the batch
files that embody it. Rule by editing in place; the staged diff is
your reply:

- **adopt** -- re-sign `standing: user`
- **reject** (not your goal; the work invented it) -- add
  `defeated: true`
- **re-grade** -- edit `force:`
- **amend** -- edit the prose; marginalia welcome (`> [!@bukzor]`)
- **missing** -- add a file, or a note anywhere

Reconciliation refines, never accretes: a ruling is absorbed into
the claim's own text, and marginalia is removed once enacted.

Driver: `trash/vim-review.sh trash/review.files.list`

This census reviews the batch's *intent*, not its content: rulings
on the underlying claims themselves belong in their own files, in
their own ledgers.
