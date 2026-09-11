# Devlog: 2026-09-11 — The session model lands as three theories, and adjudication is superseded by its own subject

## Focus

A sitting in `claude-code-holistics` (session `f9bdf6f0-d5fd-48a2-b065-da485f78241c`,
2026-09-09 through 09-11) read the corpus review, was corrected twice on
the owner's testimony, and ended with a claim ledger: a family of models
of a session in which an agent acts under rules, asks the owner for
decisions, and reads its rules through carriers that may or may not
arrive. Half of that ledger restated commitments this repo already held,
so it was split by subject rather than kept whole. This entry records
what landed here and why.

## Decisions

### The ledger splits by subject, and the split is decided by the ownership scan

`commitment` and `ask` land in `design.claims.kb/` beside `authorship`;
`carriage` and the proper-noun theory `claude-code` land in
`strata.claims.kb/` beside `protocol`; the simulation theories go to
`ideation.epistemics/session-model/` and import these by cross-repo
`why:` arrows.

**Rationale:** a fleet scan of every defining claim found `carriage`'s
words already stipulated in `protocol` (`directive`, `runtime`) and the
triggers design (`carrier`, `juncture`), and `commitment`'s subject
already held by `adjudication`. The claims-kb rule is derive before
extracting: file only what the instance adds, with `why:` naming the
prior. Two of the new claims turned out to restate protocol claims
outright -- hooks versus prose is `GRADE`, enforcement grade is who
computes the product -- and now cite them, adding only that a
juncture's kind bounds which grades are available.
**Alternatives considered:** one ledger in one place. Rejected because a
copy beside the original is exactly the double the ownership scan
exists to catch.

### `adjudication` is superseded by `commitment`

`adjudication.md` carries `verdict: superseded`; its seven staged files
are untouched. `commitment` covers the same subject -- what the owner
holds, and how a ruling becomes a record -- in four claims derived from
the owner's rulings at their transcript addresses.

**Rationale:** the owner's 2026-09-02 finding was that adjudication was
written upward from four anecdotes instead of downward from the priors.
The successor is written downward: each claim cites the ruling it
generalizes. **Alternatives considered:** reforming adjudication in
place. Its two words, `court` and `graduation`, name a rulemaking
apparatus the owner's rulings do not use; the owner's own vocabulary is
`universal`, `prior ruling`, `transcript address`.

### Ambient words are culled from ontologies before landing

The first draft stipulated `ask`, `reader`, `shape`, `veto`, `semantic`,
`observable`, `commitment`, `ruling`, `address`. The trespass scan
charged 43 findings fleet-wide, most of them siblings using those words
as ordinary English. Culling them and phrasing the genuine coinages
(`semantic juncture`, `observable juncture`, `transcript address`,
`prior ruling`) left 11.

**Rationale:** owning an ambient word polices noise; the ontology rule
says prefer the phrase the prose actually uses. **Alternatives
considered:** leaving the findings for siblings to import. Rejected
because the siblings were right and the stipulations were wrong.

## Conventions Established

- A theory arriving in a shared ledger runs the ownership scan from the
  repo root before landing; the scan's working directory is the ledger
  set, and from elsewhere it reports zero stipulations.
- Cross-repo `why:` arrows are legal and the tooling follows them; the
  import renders as the foreign claim's label.
- The owner's word `prior` (a recorded ruling) is `prior ruling` in
  ledgers, so that `Skill(llm-claims)`' `prior` (an imported theory)
  keeps its meaning.

## Open Questions

- `carrier` is now owned twice in `strata.claims.kb/`: by `carriage` in
  the owner's sense and by `data-structures` in the algebraic sense, the
  carrier set of a structure. The scan reports it as a contention and a
  person picks the loser. The agent's recommendation: `data-structures`
  says `carrier set`.
- Two force-1 trespasses remain: `extension.kb` says `gate` and
  `stratification.kb` says `universal`. Both are the speakers' to
  import or reword.

## References

- `claude-code-holistics/review.kb/2026-09-09-what-licenses-a-law.md`,
  the sitting's ledger, and its 2026-09-07 predecessor.
- `docs/dev/claims.kb/design.claims.kb/{commitment,ask}.md`,
  `strata.claims.kb/{carriage,claude-code}.md`,
  `ideation.epistemics/session-model/session-model.claims.md`.
- The prior this repo already held for token price:
  `design.claims.kb/authorship.kb/price-text-by-load-frequency.md`.
