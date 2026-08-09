# When the User Issues a `claim` Command

Marker commands (see `Skill(llm-subtask)` references/marker-commands.md);
also act on your own initiative — the core's "when claims churn" is the
trigger, not a user request:

- `claim list` — render the surviving ledger
- `claim: TEXT` or `claim XY: TEXT` — add a claim
- `claim accept: XY` — the user's ruling; re-sign `XY!`, with a clause
  of grounds (`../before/changing-a-claim.md`) — also how a `+` graduates
- `claim contest: XY` — reopen; mark `XY?`
- `claim retract: XY` — retract and propagate (`../after/retracting-a-claim.md`)
- `claim certify: XY` — name an executable check, run it; on success
  the claim goes bare, suffixed `-- certified(CHECK)`
- `claim flush` — end-of-context extraction (`the-context-or-session-is-ending.md`)
