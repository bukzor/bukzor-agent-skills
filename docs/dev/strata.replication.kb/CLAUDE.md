# strata.replication.kb -- maintenance guide

One pasteable conversation turn per file, numbered in send order.
`../strata.replication.md` is the operator's entry point: what the run
is for, and the key each turn operationalizes.

This is the best-known procedure, not a transcript. The faithful
reproduction of the original run is in git history (the collection's
first commit); improvements land as edits here, and the diff against
that commit is the record of what we learned about prompting.

## File shape

Frontmatter per `../strata.replication.jsonschema.yaml`. Then, in
order: a one-line title; an operator note saying when to send it and
what a miss looks like; **one fenced block -- the paste**; optionally
a `## Repair` section with one more fenced block, sent only when the
noted miss actually shows. Nothing outside a fence is sent, so nothing
inside a fence may address the operator. `<angle brackets>` inside a
paste mark an operator fill-in.

## What belongs here

A turn the run needs: data, elicitation, commitment, reveal, or
critique. A repair belongs with the turn it repairs, not as its own
file.

## What does NOT belong here

Findings from a run -- those argue with `../strata.ledger.kb/` by
editing claims, or land in `../devlog/`. Instructions for reading
ledgers -> the skills' `SKILL.kb/`.

## Adding or changing a turn

Insert at the free number between neighbors; the tens leave room. A
turn improvised mid-run earns a file (or a `## Repair`) only if the
next run would need it too. Where a paste quotes the original user's
words, keep the quote verbatim and let the surrounding prompt do the
sharpening -- the voice is part of what is being replicated.
