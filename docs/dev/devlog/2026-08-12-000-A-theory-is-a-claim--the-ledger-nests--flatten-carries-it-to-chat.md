# Devlog: 2026-08-12 -- A theory is a claim; the ledger nests; flatten carries it to chat

## Focus

Started as one tool: hand a `*.claims.kb/` to a chat that has no files.
`bin/llm-claims-kb-flatten` renders the whole ledger as
`Skill(llm-claims)`'s one-line-per-claim form -- `standing:` back to the
trailing sigil, `why:` back to `<-` arrows wearing their targets'
sigils, `verify:` back to `-- certified(CHECK)`, prose cites of claim
files read back as the labels those files carry. Writing it exposed
the thing the file form had been getting wrong since its first draft,
and the rest of the session was that: a theory is a claim, indentation
is containment, and the shape nests without limit.

The decision, its alternatives, and what it cost:
`adr/2026-08-11-000-A-theory-is-a-claim--containment-is-indentation.md`.
This entry is the session's own record -- what the work turned out to
require, and what it left open.

## The tool wrote the spec

The flattener had to invent a header line for each theory, and could
not say who signed it, because on disk a theory had no `standing:`.
That is the tell: a renderer forced to make something up is reading a
model that is missing a field. The notation's own claim
(`THEORY_NODE+`, "a theory needs no node type of its own") had been
true in chat and false in files for as long as both existed.

Three corrections followed from the operator, each collapsing a
special case rather than adding one:

1. Theory-defining files are claims, same schema, one directory scope
   up -- so they carry `standing:` like everything else.
2. The structure is self-similar and nests without limit; the reader's
   hard-coded two levels (ledger -> theory -> claims) was an artifact.
3. The chat rendering is one nested list. Indentation carries
   containment, so membership needs no field, no header, and no fixed
   depth.

And a fourth, on the migration itself: **move the content, don't copy
it.** Each collection's `CLAUDE.md` gave up its lede and its ontology
bullets to the defining claim and kept only what a claim cannot say --
where a new file goes. A `CLAUDE.md` that restates the skill is
double-charged tokens with a drift schedule.

## Two rulings on absence

Both halves of `<name>.kb` + `<name>.md` are optional at `Skill(llm-kb)`
scope, so the question was whether a ledger differs. It does, in one
direction only.

- **`X.md` alone** is what it has always been: an ordinary claim.
- **`X.kb/` alone** is an *open theory* -- legal, cited `LABEL?`,
  stipulating nothing, its claims answering to the ontologies above
  it. Never a folder.

The asymmetry that decided it: at `llm-kb` scope a `<name>.md` is a
derived synthesis, deletable without loss, while here it is the
*definition* -- the ontology and the defeater exist nowhere else.
Requiring it up front would charge entry a signature nobody is ready
to make (against ENTRY_COST and DEFERRAL); forbidding the gap silently
would hide the debt. Leaving it open prices the debt where the ledger
already prices debt: the first claim inside that needs a word of its
own is the bill for the defining claim nobody wrote.

Suffixes settled the same way, by asking what the name has to do: only
the ledger root carries `.claims.kb` -- it types the entry point, and
distinguishes `strata.claims.kb/` from its plain-`.kb` sibling
`strata.replication.kb/`. Nested collections are plain `.kb`, and claim
ids strip only `.kb`, so `design.claims/notation` is a handle, not a
path. That last distinction became a bug fix of its own: the lints had
been printing ids where the reader needed a path to open
(`b835a17`).

## What the migration cost

52 files, three ledgers, one pass. Two costs were taken deliberately
rather than dodged:

- Theory labels now share one namespace with claim labels. `FLEET`
  (the throwaway theory) prefixes `FLEET_MAP` (a claim inside it), and
  `grep FLEET` cannot tell them apart. It is the one lint still firing
  repo-wide; which side renames is the operator's call (todo.md).
- The strata root needed a label and `STRATA_CLAIMS` collided with the
  established `STRATA`, so it is `ENGINE`.

And one newly visible debt: all 21 defining claims stand `agent`,
assigned uniformly by the migration because headers carried no
standing before it. That is a signature nobody made claim by claim --
`strata.claims.kb/purpose.md` in particular is the operating regime
the user ruled on, and reads as `user`. Filed.

## Also this session

- Repaired `docs/dev/strata.claims.md` twice: once from a subagent
  that reported "no stderr errors" while two lints were firing (verify
  the files, not the report), once from my own throwaway normalizer
  whose unfold branch collapsed a correct list into its key line.
  A one-shot script that edits frontmatter in place needs its diff
  read, not its exit status.
- Dropped a stray, empty `docs/dev/formalization.claims.kb/` -- schema
  stubs, an empty `instrument.kb/`, no claims, no references. It was
  scaffolding misfired into this repo on 2026-08-10; the real ledger
  landed nine minutes later in `bukzor-packaging` (`a4abc0e`), where
  it lives and is committed.

## Open Questions

- FLEET / FLEET_MAP: rename which side?
- The 21 `agent` signatures: which are actually the user's?
- The prefix-freedom check runs only when you flatten. It still wants
  a home a pre-commit pass reaches -- the long-standing item, now with
  a working implementation to move rather than write.
- `llm.kb-validate .` reports 12 errors from inside gitignored
  `trash/`. A red count that means nothing trains the eye to skip red
  counts.

## References

- `adr/2026-08-11-000-A-theory-is-a-claim--containment-is-indentation.md`
- `llm-claims-kb/SKILL.md` (Layout, Tools provided),
  `llm-claims-kb/SKILL.kb/self-audit.kb/confinement.md`
- Commits: `cd6cfbb` (flatten), `448e8a1` (the migration + ADR),
  `b835a17` (lints name files, not ids), `791441b` (an undefined
  theory is open, not absent)
