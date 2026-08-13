# Runtime Memory Audit

Design-next's memory policy mandates a recurring check: runtime
auto-memory (Claude Code's `MEMORY.md`) gets flagged when it grows
kb-shaped — dated entries, decision language, task lists — for
promotion into the real system or deletion. The check exists in
design; its cadence exists nowhere.

Today: unimplemented, and nothing would schedule it if it were.

Satisficed when: a recurring audit is recordable as a wake condition
like any other, cadence per instance — "check the shadow-kb
boundary" surfaces on schedule instead of on suspicion.
