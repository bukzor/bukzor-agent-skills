---
status: in-progress
scope: |
  Em-dash characters (`—`, U+2014) in prose across markdown files in
  inventory-visible task locations and skill markdown. Replace with
  ASCII `--` (double-hyphen). Does not touch code blocks or
  intentional quotation of source material.
originating-commits:
  - c32c963    # bukzor-agent-skills, 2026-05-21: ideas.kb: replace em-dashes with ASCII -- in 2026-04-17 entries
related-session: ~/.claude/sessions.kb/finish-debolding-cleanup.md
why: |
  Em-dashes (`—`) in LLM-generated prose are an "LLM tell" — a textual
  signature that signals the prose was machine-written rather than
  human-authored. The broader debolding/ASCII-dash sweep across the
  user's docs and skill markdown replaces em-dashes with ASCII `--` so
  artifacts read as the user's own voice and don't fingerprint as
  LLM-produced.

  Sweep started 2026-05-21 with a narrow scope (two ideas.kb entries
  from 2026-04-17); broader sweep tracked in the
  finish-debolding-cleanup session entry.
---

# Replace em-dash (—) with ASCII `--` in prose

## What gets replaced

Em-dash characters (`—`, U+2014) in markdown prose. Patterns this
covers:

- Mid-sentence asides: `foo — bar` → `foo -- bar`
- List-item parentheticals: `- foo — bar` → `- foo -- bar`
- Subordinate clauses: `because X — though Y` → `because X -- though Y`

## What should NOT be replaced

- Em-dashes inside fenced code blocks (unlikely; flag if found).
- Em-dashes inside block quotes (` > `) that quote source material
  where the original punctuation must be preserved.
- Filenames or URLs that happen to contain U+2014 (treat as
  intentional).
- Pre-rendered output, captured terminal sessions, or anything
  treated as immutable history.

## Algorithm

`validate.sh` greps for the em-dash character across inventory roots,
excluding `*/node_modules/`, `*/.git/`, `*/.claude/projects/`
(session logs), and `*/trash/`. Outputs one line per match with
`<path>:<line>:<content>`.

No automatic `migrate.sh`. The replacement is mechanically simple
(`sed -i 's/—/--/g' <file>`) but per-context judgment is needed (don't
nuke quoted source material). A semi-automated workflow: run
`validate.sh`, review the list, then `sed -i` files where every
occurrence is prose.

A guarded migrator could exist later: skip files containing certain
markers (e.g. files in `_quotes/`, `_captured/`, or carrying
`preserve-typography: true` frontmatter). Out of scope for this entry.

## Idempotency

`sed -i 's/—/--/g'` is idempotent — `--` doesn't match `—` so
re-running on already-converted text is a no-op.

## Sibling work

`~/.claude/sessions.kb/finish-debolding-cleanup.md` covers the broader
"strip LLM-tells" sweep including (probably) bold-as-emphasis removal,
voice tightening, etc. This migration captures only the em-dash slice.

## Why "applying" not "applied"

c32c963 swept two specific files. Em-dashes remain widespread across
the user's tree per the validator output.
