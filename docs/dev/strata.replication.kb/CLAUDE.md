# strata.replication.kb -- maintenance guide

One pasteable conversation turn per file, numbered in send order.
`../strata.replication.md` is the operator's entry point and says what
the run is for.

## File shape

Frontmatter per `../strata.replication.jsonschema.yaml`, a one-line
title, a short operator note, then **exactly one fenced block: the
paste**. Nothing outside that block is meant to be sent, so nothing
inside it may address the operator. `<angle brackets>` inside a paste
mark the one thing the operator has to fill in before sending.

## What belongs here

A turn that has to be sent to reproduce or improve on the original
run: its data, its prods, or the review that follows. Improvements to
a turn are edits to its file -- the git diff is the record.

## What does NOT belong here

Findings from a run -- those argue with `../strata.ledger.kb/` by
editing claims, or land in `../devlog/`. Instructions for reading
ledgers -> the skills' `SKILL.kb/`.

## Adding a turn

Insert at the free number between its neighbors; the tens leave room.
A turn improvised mid-run earns a file only if the next run would need
it too -- otherwise the run's operator improvises again. Keep the
prods in the user's own voice: they are quoted evidence of what the
original had to be told, and rewriting them into agent-speak loses
the thing being replicated.
