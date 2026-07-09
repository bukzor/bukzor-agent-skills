# Strict -C/--title grammar for bin/ script args

**Date:** 2026-07-09
**Status:** Accepted

## Context

`llm-collab-{adr,devlog,init,session-start}` and `llm-subtask-{idea,todo,init}`
were CWD-implicit: creators took the title as `"$*"`, init/session-start
took no arguments at all. Agents naturally pass a target directory as a
positional argument, and this failed silently rather than loudly:

- `llm-subtask-init /path/to/repo` — ignored the path, wrote `todo.md`
  into CWD instead (documented 2026-04-17 in
  `llm-subtask/.claude/ideas.kb/2026-04-17-000-llm-subtask-init-ignores-path-argument-uses-cwd.md`).
- `llm-subtask-idea "title" /path/` — the path was slugged into the
  filename.
- `llm-collab-devlog /path/` — crashed on `sed`'s `/` delimiter,
  leaving a 0-byte file.

Two llm-subtask/llm-idea creators also still built entries via
`sed -e "s/Example Title/$TITLE/g"`, which collides with `/` in a title
the same way.

## Decision

All seven scripts now require `-C <dir>` for the target directory
(default: `.`) and, on the four creators, `--title <title>` for the
entry title. **No positional arguments are accepted anywhere** — any
bare token is a loud, non-mutating error naming both flags as the
likely fix. `-C`'s absence defaults to CWD, preserving the pleasant
no-arg case; `--title` is always required on creators (there is no
sensible default). The two remaining `sed`-based substitutions were
replaced with the bash `${var//a/b}` pattern the llm-collab pair
already used, closing the slash-crash class independent of the grammar
change.

`HERE`/`SKELETON` self-location is now computed before the `-C` cd in
every script (a latent bug: `llm-collab-init` previously computed it
*after* cd'ing, which only worked because `$0` happened to be absolute
in practice).

## Alternatives Considered

### A: Loud rejection of path-like positionals only (keep title positional)
Reject any positional containing `/`, leave plain-word titles as
positional. **Cons:** titles in this corpus routinely *contain* path
fragments (e.g. "Fix docs/dev migration drift", "SKILL.md: sharpen
Promotion Signals") — the exact shape of real titles in this repo's own
devlog/todo history. A content-sniffing veto on `/` produces both false
positives (rejects legitimate slashy titles) and false negatives (a
slash-free positional path, e.g. `llm-subtask-init myrepo`, sails
through unguarded). Killed on this evidence before implementation.

### B: DWIM — first positional is dir if it names an existing path, else title
Matches the observed agent instinct on the first try. **Cons:** same
polarity-flipped content-sniffing problem as A. Worse: it's silent on
misfire — a title that happens to name an existing directory (e.g.
`llm-subtask-todo "docs"`) gets silently reclassified as a `-C` target,
reproducing exactly the wrong-location-write failure mode being
eliminated. Any classifier that inspects the *content* of an untyped
positional is guessing intent from an inherently ambiguous signal.

### C: Greedy `--title` (consume all remaining args as the title)
Syntax-directed rather than content-sniffed, so not DWIM in the same
sense — but it silently swallows a misplaced flag or a trailing target
path into the title (`--title Fix drift -C /path` → `-C /path` becomes
part of the title; `--title fix the thing /path/to/repo` → the path is
swallowed). The second case is unmitigable without resurrecting
content-sniffing. Evidence against: all four incident calls quoted
their titles, so the convenience greedy buys (unquoted multi-word
titles) is thin, while the failure it reopens is exactly the silent
wrong-artifact write this ADR exists to close.

### D: Layered grammar — strict `-C`/`--title` core plus a freehand
positional-title fallback, guarded by an existence/slash/dash veto that
only *blocks* (never reclassifies)
Structurally sound (veto-as-blocker can't misroute, only bounce to the
strict form) and was the frontrunner for a while. **Cons:** checked
against this repo's actual title corpus, the veto fires on a large
fraction of *legitimate* calls (titles routinely contain `SKILL.md`,
`docs`, `bin/`, `todo.md`) with an outcome that depends on what happens
to exist in the caller's CWD — the same invocation succeeds in one repo
and errors in another. That's the worst regime for teaching an agent a
convention: inconsistent behavior instead of one rule learned once.
The scripts' users are agents (cheap, reliable retriers that re-read
usage every session), not casual humans, so the ergonomic surface this
option buys has little payer to justify its cost.

### E: `-m`/`--title` synonym
Shipped briefly, then removed at the user's request — no analytical
objection, just a preference for one spelling per concept.

## Consequences

**Positive:**
- No silent wrong-location writes or mangled/crashed titles are
  possible; every malformed call fails loudly with a usage hint before
  any file is touched.
- The grammar is fully deterministic — outcome depends only on syntax,
  never on what exists in the caller's CWD.
- `-C` generalizes an established convention (`git -C`, `make -C`)
  agents already know.

**Negative:**
- Breaking interface change: every prior documented invocation
  (`llm-collab-adr "Decision title"`) now errors. Mitigated by the
  error message showing the correct form, and by sweeping all 26
  living-doc references (SKILL.md, TESTING.md, references/, skeleton
  templates, and the stamped `.claude/{todo,ideas}.kb/CLAUDE.md`
  copies across llm-collab/llm-subtask/llm-kb/llm-must-read-kb/
  llm-discourse-graph) to the new syntax in the same change.
- Residual gap shared by every option considered: an agent that passes
  neither `-C` nor `--title` and is simply in the wrong CWD gets no
  help distinguishing "wrong directory" from "missing title" beyond
  the two separate error branches already provide.

**Neutral:**
- `llm-subtask-init`/`llm-collab-init`/`llm-collab-session-start` take
  no title, only `-C`; the asymmetry with the four creators is
  intentional, not an oversight.

## Related

- Supersedes: the CWD-implicit interface documented across
  `llm-collab/SKILL.md`, `llm-subtask/SKILL.md`, and both skills'
  `references.kb/`/`references/` since inception.
- Related to:
  `llm-subtask/.claude/ideas.kb/2026-04-17-000-llm-subtask-init-ignores-path-argument-uses-cwd.md`
  (the incident report that started this), commit `6b2b9aa`.
