---
last-updated: "2026-08-09"
---

# Strata, replicated

A blind re-derivation of `strata.ledger.kb/`, run as a conversation.
`strata.replication.kb/` holds the turns: one pasteable prompt per
file, numbered in send order. Open a fresh session at the repo root and
send them in order, waiting for a real answer each time.

The point is an independent second draft, not a rubber stamp. Two
accounts that agree are evidence; one that disagrees is worth more than
another pass by the ledger's own author.

## The arc

`010` is the original ask, verbatim, plus the reading list and the
blind. `020`-`070` are the prods the original run needed, promoted to
opening conditions and given a bar to clear: every structure must name
its carrier, laws, smallest instance, and falsifier, and `060` freezes
the account as a claim ledger *before* the blind lifts. `080` reveals
the existing answer and asks for a ruling on every disagreement; `090`
asks for defeats against it.

Numbers leave room between them; the operator improvises as needed and
files a turn only if the next run would need it too.

## The blind

`010` tells the agent not to open `strata.*`,
`design-incubators/engine_tower/`, `devlog/2026-08-09-*`,
`.claude/todo*`, or `trash/`, and not to `git log` this repo's
2026-08-09 commits -- every one of them leaks the answer. It also asks
the agent to confess contamination rather than hide it: a labeled
contaminated run is still readable, an unlabeled one is not.

An agent that reads `080`'s file list early has broken the run. If you
hand over this whole directory instead of pasting turn by turn, expect
that.

## What to do with the result

Defeats land as edits to the claims they defeat -- the git diff is the
strikethrough (`Skill(llm-claim-ledger-kb)`). Agreements are worth
recording only where the two runs reached the same claim by different
routes; that is evidence about the claim, and belongs in its `why:`.
The run itself belongs in `devlog/`.

## Provenance

The original: session `6b0cdfea-0afd-4539-8d78-4fffd9fd462c` under
`~/.claude/projects/-home-bukzor-repo-github-com-bukzor-bukzor-agent-skills/`
(`python3 -m bukzor.claude.branch_list` walks it). Each turn's
frontmatter carries the line it reproduces, or `new`. It reached the
ledger in one long conversation, and every bar in `020`-`070` was a
mid-course correction there rather than an opening condition -- which
is the one thing this replication deliberately changes.
