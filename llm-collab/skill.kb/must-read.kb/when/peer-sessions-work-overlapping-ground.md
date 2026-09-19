# When peer sessions work overlapping ground

Other sessions are live on related work -- named to you by the user,
seen in `ListAgents`, or evident from a `sessions.kb/` entry whose
scope touches yours -- and findings could usefully cross between them.

## Your session entry is your public face

The digest a peer reads is your `sessions.kb/` entry
(`Skill(llm-sessions)`); write nothing else for peers. Keep it current
at checkpoints -- a subtask finished, a decision about to be taken on
shared ground -- so that a peer arriving cold can read, in a minute:

- the task, one line;
- findings, as claims signed by their author (`+`, or `[!DRAFT]` on
  standing text) -- nothing becomes a ruling by crossing sessions;
- open questions, and which need the user;
- overlap suspects: what here touches which peer;
- wants: what you would take from a peer if they have it.

Edit only your own entry. Cross-references go in yours, pointing at
theirs.

## Pull at checkpoints; never poll

At each checkpoint, read the peers' entries and record in your own
what you adopt and what you contradict. Reading is free for the peer;
a message costs them a turn, and passes only as pointer, conflict, or
hand-off (`../../procedures.kb/send-a-peer-message.md`). Between checkpoints, do not watch for
changes -- if you genuinely depend on a peer finishing,
`notify_when_idle` is a one-shot subscription that costs them nothing.

## Contradictions go to the user, not to negotiation

When your finding and a peer's conflict, file both as claims under a
question in your entry and surface it to the user in one line. Two
agents arguing over a channel converge on whoever wrote last, not on
the truth.

## Fan-in when overlap is heavy

Three or more peers with dense overlap: one session (or a throwaway
one) reads every entry and writes each peer one delta -- "you should
know: ..." -- as a file. Then each peer gets a single pointer message.
This is 3 reads + 3 writes once, against a mesh that re-explains
context on every send.

## When NOT to trigger

- The peer is a sub-agent you spawned: it reports to you, and you own
  its context (`~/.claude/must-read.kb/when/spawning-a-sub-agent--delegating-a-task.md`).
- The overlap is in time, not concurrency: a prior session's baton is
  its devlog and ADRs (`../before/writing-an-ADR-or-devlog-entry.md`).
