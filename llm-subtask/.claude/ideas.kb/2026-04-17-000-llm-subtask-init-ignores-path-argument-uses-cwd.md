---
managed-by: Skill(llm-subtask)
---

# Agent repeatedly passes path arguments to CWD-based scripts

All llm-subtask and llm-collab bin/ scripts use CWD, not a path
argument. But an LLM agent's natural instinct is to pass the target
directory as an argument — this happened repeatedly in a single session
(2026-04-17):

- `llm-subtask-init /path/to/repo` — silently used CWD, created
  todo.md in the wrong repo.
- `llm-subtask-idea "title" /path/` — produced a mangled filename
  with the path baked into the name (sed error).
- `llm-collab-devlog /path/` — crashed with sed error on slashes.
- `llm-collab-init /path/` — generated a devlog entry with the
  entire path slugified into the filename.

The agent had to be told to check `-h` before it understood the
CWD convention. Even then, using `cd` before each invocation felt
unergonomic compared to passing a path.
