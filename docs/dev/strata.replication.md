---
last-updated: "2026-08-09"
---

# Strata, replicated

A blind re-derivation of `strata.claims.kb/`, run as a conversation.
`strata.replication.kb/` holds the turns, numbered in send order, and
`strata.replication.kb/instructions.d/` holds what each one sends --
a whole file per paste, so sending it is select-all-and-send with no
operator note to strip. Open a fresh session at the repo root and
send them in order, waiting for a real answer each time; each turn
file says when to send it, what a miss looks like, and (where the
original run had a stubborn failure) points at a repair paste to send
only on that miss.

The point is an independent second draft, not a rubber stamp. Two
accounts that agree by different routes are evidence; one that
disagrees is worth more than another pass by the ledger's own author.

## The arc, and the keys it operationalizes

The original run succeeded because of six things, each of which it
found mid-course; the turns build them in from the start.

1. **The telos came last but organized everything.** The retention
   question -- what survives a "good idea" -- arrived mid-run, and the
   ledger reorganized around it. `010` states it up front as the
   fitness function: a structure earns its place by what it lets us
   keep.
2. **Intuition picked the target.** The generative step was someone
   pointing at one line of survey and saying *this feels like a
   structure*. `020` makes the agent nominate its own itches, fan out
   cheap conjectures past its first idea, then kill its own weak ones.
3. **Two failure modes ate turns.** Flattening (claims about only the
   most generic engine) and literature name-dropping (citation as a
   substitute for exhibition). `010`'s bar and `030`'s shape prevent
   them; `020` keeps a repair paste for the stubborn one.
4. **The account got honest when it had to run.** The executable-model
   comparison surfaced a missing premise and an import-graph hole.
   `040` demands the witness before the reveal instead of after, and
   adjudicates witness-vs-account mismatches in both directions --
   `/deformalize`'s review step, inlined to protect the blind.
5. **Commitment makes comparison meaningful.** `050` freezes the
   account as a chat ledger and `060` adds bets -- which claims will
   survive, where the held answer will win -- before `070` lifts the
   blind and demands rulings, and `080` demands defeats.
6. **The user-assessor layer is a scripted turn, not a residual.**
   Agent-signed claims stay `+` until the operator exercises the
   invited vetoes, and no agent can mint `standing: user` on its own.
   `090` stages the act-grain walkthrough -- each cluster of claims
   presented as the decision it amounts to, with alternatives and the
   fallout of rejecting -- whose original reply's amendments seeded
   the purpose root and the assessor law. Since distilled into
   `/review-open-questions`.

Numbers leave room between them; the operator improvises as needed and
files a turn (or a repair) only if the next run would need it too.

## The blind

`010` tells the agent not to open `strata.*`, `design.claims.*`,
`design-incubators/engine_tower/`, `devlog/`, `adr/`,
`.claude/todo*`, or `trash/`, and not to `git log` this repo's
commits from 2026-08-09 on -- every one of them leaks the answer.
The 2026-08-10 run taught the wide net: date-pinning the exclusions
failed, because the answer's vocabulary kept spreading into
later-dated files (a devlog *title* leaked "engine tower" and
"courts are sigils" to that run's subject via a bare `ls`), so
whole directories are out, listings included. It also asks
the agent to confess contamination rather than hide it: a labeled
contaminated run is still readable, an unlabeled one is not.

An agent that reads `070`'s file list early has broken the run. If you
hand over this whole directory instead of pasting turn by turn, expect
that. The pastes inline the procedures they need instead of invoking
skills -- nothing a blind agent loads may be able to name the answer.

## The environment

Run the subject in a dedicated worktree on a branch of its own, built
from `main` and holding the repo under study *and nothing about the
study*:

```sh
git worktree add -b <run-env> ../<repo>--<run> main
git -C ../<repo>--<run> rm -rq docs/dev/devlog docs/dev/adr \
    docs/dev/strata.replication.kb docs/dev/strata.replication.run.kb \
    docs/dev/strata.replication.md .claude/todo.md .claude/todo.kb
git -C ../<repo>--<run> commit-files . -- -m wip
```

Everything deleted there is something the subject would read about
itself: the turns it has not been sent yet and what the operator calls
a miss, its own earlier answers, the verdicts on them, the devlog
saying what the run is for. Keeping them merely forbidden worked once
and is one `ls` from not working.

The seal matters as much as the deletions: a bare `git status` in a
dirty checkout lists the answer's own paths, so an unsealed worktree
leaks through a command the subject has every reason to run. A bland
one-word message leaks nothing.

Then repair the ledger's mechanical rot before the run -- dangling
symlinks, a `verify:` that no longer selects, a schema that will not
resolve. A critique turn spends its depth on whatever is broken, so
leaving rot in place buys an audit of the rot; and the turn cannot be
re-asked of the same subject afterward (below). Mechanical breakage is
the operator's to fix, not a finding worth a turn.

Rebuild the branch, don't merge into it. An environment branch is a
checkpoint, not a line of work: when the repo moves under a run --
because the run's own findings were filed, which is the point -- the
next environment is a fresh branch off the new `main`, sealed the same
way. Merging `main` into a months-old seal fights conflicts for a tree
nobody wants to keep.

## Rewinding a run

Commit each stage as it lands -- the subject's reply into
`strata.replication.run.kb/` on `main`, one commit per turn, the
operator's verdict as its message. A run that commits only at the end
has no middle to point back at, which is how the first run lost its
critique turn.

The record stays out of the environment. Put the stage files in the
subject's own worktree and a re-asked turn is answered by a subject
that can read its own previous answer -- the rewind undone by a
`cat`. Two branches: the record on `main`, the environment sealed on
its own.

Rewinding the *conversations* is two cuts, because a run has two
participants and neither rewind reaches the other. Start with the
operator's: it holds every reply and every verdict, so an operator who
has read a spoiled answer will grade the replacement against it. Cut it
at the record that delivered the last good reply --
`claude-branch-extract <operator.jsonl> <uuid> --at`, per
`Skill(claude-code-archeology)`. Then the subject's, which the operator
cut does not touch: re-sending a turn is not a rewind either, since its
first answer stays in its context and what comes back is a revision.

Run the subject as its own session rather than a subagent and both cuts
are ordinary. A subagent costs an extra step and loses something in it:
its transcript lives under the operator's session, so it needs
`--as-session <worktree>` to become resumable, and it comes back without
its agent definition -- model and effort must be restored by hand.

## What to do with the result

Defeats land as edits to the claims they defeat -- the git diff is the
strikethrough (`Skill(llm-claims-kb)`). Agreements are worth
recording only where the two runs reached the same claim by different
routes; that is evidence about the claim, and belongs in its `why:`.
Graded bets say something about the *procedure* -- systematic misses
mean a turn needs sharpening, here. The run itself belongs in
`devlog/`.

## Provenance

The original: session `6b0cdfea-0afd-4539-8d78-4fffd9fd462c` under
`~/.claude/projects/-home-bukzor-repo-github-com-bukzor-bukzor-agent-skills/`
(`python3 -m bukzor.claude.branch_list` walks it). Each turn's
frontmatter lists the original lines it distills; `origin: []` marks a
turn the original never had. The collection's first commit is the
faithful reproduction -- nine turns mirroring the original's order,
corrections included as sent; the current form front-loads what those
corrections taught.
