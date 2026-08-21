# Before Writing a Claim

Write each claim for an agent with no memory of the conversation that
produced it. The line is done when that reader can act on it without
asking anyone — so put the justification *in* the claim text rather than
pointing at where it was said.

```
RT?: the retries are the problem
RT?: the 30s client timeout fires before the 45s upstream retry
     completes, so every slow request is issued twice
```

Both cost one line. Only the second survives the context that produced
it. Under-statement is the failure mode to watch for, not verbosity: a
thin line reads fine to you, who still remember.

## Prefer the positive statement

Treat any impulse to write "not", "rather than", or another negation as
a warning. It earns its place only where the contrast carries direct,
context-free utility -- naming a declined alternative the reader would
otherwise reach for. Everywhere else it is a revision scar: the line
records the argument that produced it in place of the state it reached,
and the next reader pays for a debate they were not in.

The same failure at claim scale is a claim about an absence.
`NO_STOP+: the procedure has no stopping rule` catalogues what is
missing, and there is no end to that catalogue. What was meant is a
question: `STOP?: what is the correct stopping rule?`

## An open question carries `?`

Undone work enters the ledger as a claim signed `?`, its text naming
what an answer would settle. It needs no mark of its own: `?` already
says no one has judged, and scheduling the work is
`Skill(llm-subtask)`'s job.
