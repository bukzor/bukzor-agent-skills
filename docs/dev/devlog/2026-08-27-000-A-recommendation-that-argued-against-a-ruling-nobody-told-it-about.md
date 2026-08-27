# Devlog: 2026-08-27 — A recommendation that argued against a ruling nobody told it about

## Focus

Lane `-005` of the ref rollout: five fleet rulings, each researched and
written up as a recommendation with the case for and against, then
handed to the owner. All five were ruled the same day. **Nothing was
applied** — that is `todo.kb/2026-08-27-000`, deliberately a different
entry, because a lane whose charter is "recommend and record" does not
get to also execute.

## Decisions

### The briefs omitted the claim ledger, so one recommendation argued against a standing ruling

I wrote five sub-agent briefs and none of them named
`llm-kb/claims.kb/`. Ruling 2's agent concluded, on the merits, that
`research.home-office/use-cases.kb` wants no schema at all: three files,
two of them sharing exactly one key, the third carrying no frontmatter,
untouched since January. Good reasoning, and already foreclosed —
`CANONICAL_PER_COLLECTION` (`standing: user`) holds that a collection
whose files carry frontmatter and has no sibling schema gets one
written, and that "the ruling is to write the schema, not to strip the
frontmatter."

The fix was not to delete the merits argument. It stays in the file,
reframed: *an appeal to reopen the ruling, not a competing
recommendation*, with the actual output being a permissive local schema —
every property optional, nothing required.

**Rationale:** the ledger is the index of what is already settled. A
brief that omits it invites an agent to re-derive a decided question and
win the argument locally, in a file the owner then reads as advice.

The same ruling had a gap that had already been executed at fleet scale.
`CANONICAL_PER_COLLECTION` says a collection with *no schema* gets one;
on 2026-08-22 an agent read that as "make every collection have a
schema" and overwrote 254 hand-written stubs with full copies. New claim
`STUB_IS_SCHEMA`: a sibling schema file that exists **is** the schema,
however short — absent, write it; present at any length, leave it, and
report only if it fails to resolve. The parent ruling now carries a
pointer to it.

### The damage was never committed, so there was nothing to un-commit

The owner authorized un-committing bad commits and suggested `--fixup`
plus `rebase --autosquash`. I checked before rewriting anything:
`git log -G'^-?\$ref: "skill://'` across three repos since 2026-08-15
returns only stub-*adding* commits. Zero removals, anywhere.

The 2026-08-22 blast survived in exactly one place — the working tree of
a second, stale `dotfiles` checkout at `~/repo/github.com/bukzor/dotfiles`,
nine modified files stamped 14:03, uncommitted for five days. The live
`$HOME` tree (which *is* the dotfiles working tree) was clean the whole
time. Repair: copy all eleven to `trash/`, then `git checkout --` the
nine. Guard findings went 17 → 10, and the diff was exactly the seven
dotfiles lines.

**Rationale:** the tool the owner reached for presumes the damage is in
history. Two minutes of `log -G` is the difference between a correct
no-op and a history rewrite that fixes nothing.

### Nine of the guard's ten findings are the guard

After the revert: 10 findings, of which 9 are
`NO-REF <tree>/claims.jsonschema.yaml`. Category `claims` has two rival
canonicals — `llm-discourse-graph/jsonschema/claims` (enrolled) and
`llm-claims-kb/jsonschema/claim`, singular, so the table derived by
globbing `<skill>/jsonschema/` never maps `claims` onto it. Every
*correct* stub is reported as drift. The tenth is a real gap.

The owner adopted the daily anacron schedule as a trial anyway. The
admission rule that came with it — a `kind: recurring` guard joins the
schedule only when its baseline is near-zero — means the schedule step
is gated on fixing this first, hence `todo.kb/2026-08-27-001`. A guard
whose day-one report is nine-tenths its own bug teaches the owner that
guard reports are noise, after which both guards are dead.

### Two instruments, blind in the same two ways

For "should the guard root at `~`?", four instruments measured:

| instrument | `.kb` dirs | wall | crash |
|---|---|---|---|
| guard `collections()`, three roots | 660 | 5.4 s | no |
| guard `collections()`, root `~` | 630 | 16.0 s | `ERROR(1)` |
| `survey.find`, dirnames | 733 | 3.0 s | no |
| `git -C ~ ls-files` | 20 | 18 ms | no |

`survey.find()` prunes every top-level dotdir except `.claude`, so
`~/.vim` — the dotfiles tree's only collections outside `~/.claude` — is
invisible to the shared engine too, not just to the guard. And both
file-based instruments enumerate *files* while the guard checks
*directories*: six collections today hold no regular file at their own
level and cannot appear in any file-derived list.

Root `~` also crashes: 42 permission-denied lines from container overlay
dirs make `find` exit 1, `pipefail` propagates, the `ERR` trap fires, and
the guard prints **nothing** while exiting 1 — indistinguishable from
"found findings", the worst failure shape a recurring guard has.

Verdict: `$HOME/.vim` joins `ROOTS`. Declared, not derived, with the
`categories.tsv` failure mode re-created knowingly and a revisit trigger
written down.

## Conventions Established

- A recommendation whose merits argument loses to a standing ruling
  **keeps the argument**, relabeled as an appeal to reopen. Deleting it
  loses the reason to revisit; leaving it as a recommendation launders a
  settled question past the owner.
- A verdict's riders are marked for what they are. Where I added a
  stopping condition or a deferral the owner did not state, the file
  says "agent's call, recorded here, veto by editing this file." The
  owner ruled the verdict, not everything I hung off it.
- Evidence in a brief gets **re-derived, not inherited**. The parent
  brief was wrong in both directions on ruling 1's census, read one
  un-fetched clone counted ten times as ten independent lapses on ruling
  3, and misattributed the dotfiles findings on 4 and 5. Every one of
  those survived into a brief because the previous writer believed it.
- Drift now has a rate, measured twice four days apart: **half a finding
  a day**, arriving in repos nobody was auditing. That is the number the
  daily timer is priced against, and it is the first thing this
  migration has measured more than once.

## Open Questions

- [ ] `claims` vs `claim`: one canonical, an alias in the derived table,
      or two genuinely different objects. Whatever the answer, the
      derivation must express it — a hand-maintained table is what the
      glob replaced.
- [ ] Two untracked schemas in the stale clone
      (`.claude/{reference,user-preferences}.jsonschema.yaml`) are the
      wanted half of the 2026-08-22 sitting and exist nowhere else. They
      belong in the live `$HOME` tree; awaiting the owner's word.
- [ ] The bullet guard's 1191-finding baseline needs a triage pass, or a
      narrower question. It is honest about refusing to mechanize the
      judgment, which is also why it cannot be scheduled as-is.

## References

- `llm-kb/.claude/todo.kb/2026-08-23-005-Fleet-rulings-that-gate-the-schema-lanes.kb/` —
  the five recommendations, each with its `## Verdict`
- `llm-kb/.claude/todo.kb/2026-08-27-000-*` — apply the five verdicts
- `llm-kb/.claude/todo.kb/2026-08-27-001-*` — guard admission blockers
- `llm-kb/claims.kb/design.claims.kb/a-ref-stub-is-a-schema.md` (`STUB_IS_SCHEMA`)
- `llm-kb/claims.kb/design.claims.kb/status-is-a-spelling-not-a-concept.md` (`STATUS_ENUM`)
- `llm-kb/claims.kb/design.claims.kb/a-guard-runs-on-a-timer-and-arrives-at-session-start.md` (`GUARD_SCHEDULE`)
