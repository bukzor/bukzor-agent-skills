---
name: claude-code-archeology
description: "Agent MUST load on /claude-code-archeology, when a question is about what happened in a past Claude Code session (what was tried, decided, or lost), when recovering sessions after a crash or freeze, or before parsing anything under ~/.claude/projects."
---

# Claude Code archeology

`~/.claude/projects/*/*.jsonl` is the only durable record of most work
done here. It answers questions nothing else can -- what was tried and
abandoned, what a command printed before the machine froze, what was
decided in a conversation that ended without a commit. Treat it as a
primary source.

Never `grep` the raw JSONL. It matches JSON-escaped text, misses
anything split across content blocks, and prints a 4000-column line on a
hit. Use the tools below; they decode first.

## The tools

| command                                     | answers                                                     |
| ------------------------------------------- | ----------------------------------------------------------- |
| `claude-search PATTERN [--role talk] [--all]` | which session discussed this, with snippets                  |
| `claude-inventory [--days N] [--sh]`          | what was I working on; `--sh` emits resume commands          |
| `claude-branch-list FILE [--branches-only]`   | the file's tree, marking real rewind points                  |
| `claude-branch-extract [--at] [--as-session CWD]` | linearize one branch into a new resumable JSONL          |
| `claude-jsonl-cwd FILE`                       | the directory a session ran in (needed to resume it)         |
| `claude-jsonl-path DIR`                       | the projects/ dir holding a cwd's sessions                   |
| `claude-jsonl-display < FILE`                 | render a transcript readably -- **on stderr**; stdout carries only a machine-oriented `result.result` line, if any, so `\| tail`/`\| grep` on stdout alone will not see it |
| `claude-jsonl-to-log < FILE`                   | same rendering, captured to a `.log` file beside it           |

Library behind them: `claude_code_archeology.{session,search,inventory,
tree,format_short,branch_extract}` -- import it rather than re-parsing
when a question needs custom analysis:

```sh
uv run --project ~/repo/github.com/bukzor/bukzor-tools python - <<'PY'
from claude_code_archeology import session
PY
```

Every module is doctested; `uv run pytest` in that repo runs them.

## Format facts that bite

- **The file is a forest, not a log.** Records carry `uuid` and
  `parentUuid`; a rewind writes new records as *siblings* of the old
  continuation, and each compaction starts a new root (its
  `compact_boundary` record has no parent). `--resume` and the rewind
  picker walk back from the newest record only, so abandoned branches
  and every pre-compaction era are unreachable in the UI -- extraction
  is the only way back -- but fully present in the file. That's where
  "we tried that and it didn't work" lives.
- **The `projects/<slug>/` name is not invertible.** The slug maps both
  `/` and `.` to `-`, so `prototype.chatfs/docs` and
  `prototype-chatfs-docs` collide. Read `cwd` from the records
  (`claude-jsonl-cwd`); never decode the directory name. Last value
  wins, since resuming from elsewhere rewrites it.
- **`type: user` is not "the user typed this".** Tool results are stored
  as user records. Distinguishing them (`role_of`, `is_user_text`) is
  what makes "what did I actually ask for" answerable.
- **Subagent transcripts live under the parent session**, in
  `projects/<slug>/<session-id>/subagents/agent-<id>.jsonl`, with every
  record marked `isSidechain: true`. Nothing globbing `projects/*/*.jsonl`
  sees them -- not `--resume`, not the tools above unless pointed at the
  file. They are shaped like sessions otherwise, so
  `claude-branch-extract --as-session CWD` re-homes one as a session of
  its own: the marks come off, `cwd` moves to the directory the work
  belongs in, and it resumes like anything else. What does not come
  back is the agent definition it ran under -- the promoted session
  gets the plain system prompt and the session's own model.
- **User-role text is often harness-injected**: compaction summaries,
  skill preambles, command wrappers, `[Request interrupted...]`. Filter
  it before drawing conclusions about what a person said.
- Files are append-only, so a frozen or killed session loses nothing but
  the in-flight turn. A crashed write can leave one malformed line;
  parse defensively rather than failing the whole file.

## Rewinding to a state the picker will not offer

`/rewind` cuts only at *your own* prompts, on the one chain resume
loaded -- which, after a plain extraction, is most of what you want.
What it cannot reach is a state that must *keep* an assistant reply or
tool result and drop what followed, a point inside a turn, or a promoted
subagent's transcript, whose user-role records are tool results rather
than prompts. Answering a reply differently is not on that list: rewind
to the prompt that produced it and re-send. For the rest, cut the file:

1. `claude-branch-list FILE` (or a `claude-search` hit) names the record
   the state you want is built around.
2. `claude-branch-extract FILE <uuid> --at` writes a new session cutting
   just past it -- the ref plus the message after it, since a message cut
   away needs another extraction to get back while one kept too many is
   droppable in-session with `/rewind`; add `--as-session <cwd>` when the
   source is a subagent's. It prints the record it actually cut after.
3. `cd <cwd> && claude --resume <new-id>`, then send the turn again --
   `/rewind` first if the extra trailing message is in your way.

Two things do not come back with it: the repo state the dropped turn
worked against -- version control is the only rewind for that, so commit
each step of anything you may want to re-run -- and, for a promoted
subagent, its agent definition. Re-asking without rewinding is not the
same experiment: the first answer stays in context, and what comes back
is a revision of it.

**A subagent is not rewound by rewinding its caller.** Its transcript is
a separate append-only file, bound to the spawning tool-use by
`subagents/agent-<id>.meta.json` and resumed through its `agentId`, and
the file-history records backing `/rewind` cover the repo only, never
`~/.claude/projects`. So a caller cut plus a re-sent turn reaches a
subagent that remembers everything. Cut both files, or -- better for
anything you may want to replay -- run the other side as its own session
and drive it with `SendMessage`.

In-place surgery -- cutting a poisoned tail so the *same* agent id
resumes, clearing a `stoppedByUser` refusal in the meta.json -- is
`Skill(claude-code-surgery)`.

## Recovery after a crash or freeze

1. `claude-inventory --days 2 --sh` -- every resumable session, newest
   first, as paste-ready `(cd DIR && claude --resume ID)` commands.
2. Hand the list to the user, who resumes what still matters. Don't
   resume anything yourself.
3. When a session's useful work is on an abandoned branch,
   `claude-branch-list` it and extract the branch rather than hunting
   through the live chain.

## Mining a session for evidence

When the transcript is evidence about an incident rather than work to
resume, file it like any other perishable source -- capture the extract
into the investigation's `evidence.kb/`, don't re-read the JSONL at
every question. See `Skill(incident-forensics)`.

Two habits keep this honest:

- Quote what the record says, and cite `file:line` (the tools print line
  numbers for exactly this). A transcript is a record of what was
  *claimed* at the time, which is not the same as what was true.
- A session's own summary of itself -- compaction summaries, `ai-title`
  records -- is a lossy secondary source. Check it against the records
  it summarizes before repeating it.
