# Write for a Fresh Reader

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
