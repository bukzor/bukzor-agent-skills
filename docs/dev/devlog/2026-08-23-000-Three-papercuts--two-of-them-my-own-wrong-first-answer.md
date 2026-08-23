# Devlog: 2026-08-23 — Three papercuts, two of them my own wrong first answer

## Focus

Work in another repo (`~/claude/meta-reasoning`) kept scraping against
this one. Three friction points surfaced, all small, and the ask was to
file them as todos or just fix them if that cost the same. Two got
fixed, one got sharpened into a decision that isn't mine to make. What
makes the session worth an entry is that my first answer to two of the
three was wrong, and the wrongness is instructive.

## Decisions

### The link checker was documented, not written

I wanted to verify a batch of moved files' cross-references, saw nothing
in `llm-kb/SKILL.md` about link checking, and hand-rolled a regex
checker. It reported broken links that weren't — prose filenames
(`consolidation.md` mentioned in a sentence) and repo-root-relative
paths both looked like dangling refs to it.

`llm.kb-validate-links` already exists, at
`llm-kb/bin/llm.kb-validate-links`, and answered the same question with
`✅ 116 files, 0 with broken links`. It was invisible for a specific
reason: it's a PEP 723 `uv run --script` deliberately outside the
`llmd` wheel, so it is *not* an installed console script and does not
appear on `$PATH` beside `llm.kb-validate`. Nothing in SKILL.md said so.

**Rationale:** an undiscoverable tool gets reimplemented, badly, by the
next agent with the same question. SKILL.md now documents it under
Tools Provided, including why it's run by path and what `--strict` vs
`--lax` trade (strict = `./`/`../`-prefixed only, no false positives,
blind to bare-relative refs; lax = more recall, CLI examples in prose
surface as hits to triage).
**Alternatives considered:** promoting it to a console script so it
lives beside `llm.kb-validate`. Rejected for now — the inline-deps
form is why it can carry its own dependencies without widening the
wheel's, and the real endpoint is folding the check into
`llm.kb-validate` proper, already tracked at
`llm-kb/.claude/todo.kb/2026-06-03-000-validate-path-references.md`.

### `managed-by:` is strippable; `cost-benefit-sweh:` is not

`llm-kb/.claude/todo.kb/2026-08-23-003-*` had proposed, as its cheapest
option, stripping roll-up frontmatter wholesale on the grounds that the
keys are constants nobody reads — pending a reader sweep. I ran the
sweep and reported the cheap answer first. It was wrong in the part
that matters:

- `managed-by:` — no reader. Writers and a schema `const` pin, nothing
  consuming it. Strippable.
- `cost-benefit-sweh:` — **read**, by `claude-open-tasks-list` and
  `wsjf-rank`, and this repo's own `llm-subtask/.claude/todo.md`
  carries a populated one today. Stripping roll-ups wholesale deletes
  live prioritization data.
- `status:` — skeleton-set to `template`, hand-edited to `active` in at
  least one consumer; no reader found, sweep not exhaustive.

**Rationale:** the option that looked cheapest is unavailable as
stated, which means the item is really a decision between "strip the
constants, keep the data" (which still needs one of the other options
for what remains) and moving `cost-benefit-sweh` out of roll-ups
entirely so `### Synthesis Files`' "carries no frontmatter" can stand
unamended. Recorded in the item; left for the owner to rule.
**Alternatives considered:** ruling it myself. It changes what a
documented invariant means, and the data at risk is the user's backlog
prioritization.

### mtime is not a sequence number

`llm-subtask-todo` handed me `-002` in a directory already holding
`-000` through `-005`. All four dated-artifact creation scripts picked
"the previous entry" with `ls -1t | sed -n 1p` — newest by modification
time. Editing an old entry makes it mtime-newest, so the next create
restarts from its number and collides.

**Rationale:** `sort | sed -n $p` takes the lexical max of basenames
instead; NNN is zero-padded to fixed width, so lexical order *is*
numeric order, and timestamps stop participating. Verified per script
against the exact trap — a directory whose mtime-newest file is not its
number-highest — plus the empty-directory case (`000`).
**Alternatives considered:** `sort -t- -k4 -n`, which is what the
intent literally says. Rejected: zero-padding already guarantees the
lexical answer equals the numeric one, and the plain `sort` doesn't
break if a slug ever contains a dash in an unexpected place.

## Conventions Established

- Nest by what a file *elaborates*, not by what it resembles. Anything
  elaborating `X.md` goes under `X.kb/`, at whatever depth `X.md` sits.
  The trap is a directory already holding peer collections: two
  `$SIBLING.kb/` beside `X.md` make a third peer look like the
  precedent, when the only question is what the new collection is
  about. Now in `llm-kb/SKILL.md` under "Where an Elaboration Goes".
- A collection's roll-up takes the collection's own name
  (`X.kb/candidates.md` rolls up `X.kb/candidates.kb/`). `README.md`
  inside a collection is for the case that forces it — a collection
  elaborating a same-named item file cannot name its roll-up `X.md`,
  because `X.md` is the item. I wrote the flat version of this rule
  ("`README.md` is root scope only") into a devlog first, and it was
  contradicted twice inside the same repo I was writing about; the
  name-collision case is what decides it.
- A tool that isn't on `$PATH` must say so in SKILL.md, with the
  by-path invocation. Absence from the docs reads as absence from the
  repo, and the next agent writes a worse copy.
- `ls -1t` answers "recently touched", never "highest numbered". It
  remains correct in `llm-collab-session-start`, which genuinely wants
  recency; it was wrong in all four creation scripts.

## Open Questions

- [ ] Roll-up frontmatter: strip the constants and keep
      `cost-benefit-sweh`, or move that field out of roll-ups so
      "carries no frontmatter" stands? Tracked in
      `llm-kb/.claude/todo.kb/2026-08-23-003-*`. 24 files under `~`
      carry the skeleton frontmatter, across separate repos, so the
      sweep is one commit each.
- [ ] `status:` in roll-ups has no reader that the sweep found, but the
      sweep wasn't exhaustive. Worth confirming before it's stripped.

## References

- `llm-kb/SKILL.md` — Tools Provided, and "Where an Elaboration Goes"
- `llm-kb/.claude/todo.kb/2026-08-23-003-Schema-binding--roll-ups-scoping-rule-and-ruled-rivals.md`
- `llm-kb/.claude/todo.kb/2026-06-03-000-validate-path-references.md`
- `66334ef` — the sequence-numbering fix, with the per-script verification
- `~/claude/meta-reasoning/docs/dev/devlog/2026-08-23-001-*` — where the
  placement rule was first (mis)stated, then corrected
