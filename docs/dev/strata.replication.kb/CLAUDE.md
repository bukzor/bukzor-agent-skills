# strata.replication.kb -- maintenance guide

One conversation turn per file, numbered in send order; the text each
one sends lives beside it in `instructions.d/`, one file per paste.
`../strata.replication.md` is the operator's entry point: what the run
is for, and the key each turn operationalizes.

This is the best-known procedure, not a transcript. The faithful
reproduction of the original run is in git history (the collection's
first commit); improvements land as edits here, and the diff against
that commit is the record of what we learned about prompting.

## File shape

Frontmatter per `../strata.replication.jsonschema.yaml`. Then, in
order: a one-line title; an operator note saying when to send it and
what a miss looks like; a pointer to its paste in `instructions.d/`;
optionally a `## Repair` section pointing at a second paste, sent only
when the noted miss actually shows.

The paste is a whole file so that sending it is one copy: select all,
send. That only holds if it stays send-ready -- no frontmatter, no
title, nothing addressed to the operator, which is what the turn file
is for. `instructions.d/<turn>.md` is a turn's paste;
`instructions.d/<turn>--repair.md` is its repair. `<angle brackets>`
inside a paste mark an operator fill-in.

## What belongs here

A turn the run needs: data, elicitation, commitment, reveal, or
critique. A repair belongs with the turn it repairs, not as its own
file.

## What does NOT belong here

Findings from a run -- those argue with `../strata.claims.kb/` by
editing claims, or land in `../devlog/`. Instructions for reading
ledgers -> the skills' `skill.kb/`.

## Adding or changing a turn

Insert at the free number between neighbors; the tens leave room. A
turn improvised mid-run earns a file (or a `## Repair`) only if the
next run would need it too. Where a paste quotes the original user's
words, keep the quote verbatim and let the surrounding prompt do the
sharpening -- the voice is part of what is being replicated.
