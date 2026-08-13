# strata.replication.run.kb -- one run's record

One file per stage of one run of `../strata.replication.kb`, named for
the turn that asked for it, holding the subject's reply verbatim. The
operator's verdict on a stage is its **commit message**: the file says
what came back, the commit says whether it landed.

`../strata.replication.md` is the procedure's entry point; this is the
evidence a run happened and what it produced.

## The record is not the environment

This directory lives on `main`, never in the subject's worktree. It
holds the subject's own answers and, in the commit messages, the
operator's verdicts on them -- both of which a subject that re-reads
its repo would find. The first run kept the record inside the
environment; when a turn had to be re-asked, the previous answer was
sitting in the tree the re-asked subject was reading.

The environment is a separate branch, checked out in the subject's
worktree, carrying the repo under study and nothing about the study
(`../strata.replication.md`, "The environment").

Commit each stage as it lands, not in a batch at the end -- one
commit per turn, the verdict in the message. A run recorded only at
the end has no middle to point back at, which is how the first run
lost its critique turn.

## Rebuilding it from the transcript

`extract-stages.py` reads the subject's session JSONL and writes the
stage files: the deliverable is the subject's last message before the
next turn arrived. `--limit N` stops early, which is how a spoiled
stage stays out of the record.

The transcript is perishable and lives outside version control, so
extract early; the file under `~/.claude/projects/` is the primary
source and every stage file's frontmatter cites its line.

## Before a critique turn, repair the environment

Mechanical rot in the ledger under audit -- a dangling symlink, a
`verify:` that no longer selects, a schema that will not resolve -- is
the operator's to fix before the turn is sent, not a finding worth an
audit. A critique turn spends its depth on whatever is broken; leave
rot in place and that is what you buy, and the turn cannot be re-asked
of the same subject without the first answer in view.

## What does NOT belong here

Analysis of a run -- verdicts beyond the one-line commit message,
comparisons, adjudications -> `../devlog/`. Changes to the procedure
that a *next* run would need -> `../strata.replication.kb/`.
