# Commands

Marker commands (see `Skill(llm-subtask)` references/marker-commands.md);
also act on your own initiative — the core's "when claims churn" is the
trigger, not a user request:

- `claim list` — render the surviving ledger
- `claim: TEXT` or `claim XY: TEXT` — add a claim
- `claim accept: XY` — adjudicate warranted, the operator's call; mark `XY!`,
  which is also how a `+` graduates
- `claim contest: XY` — reopen; mark `XY?`
- `claim retract: XY` — retract and propagate (`retraction-propagates.md`)
- `claim certify: XY` — name an executable check, run it; on success
  mark `certified(CHECK)`
- `claim flush` — end-of-context extraction (`flush.md`)
