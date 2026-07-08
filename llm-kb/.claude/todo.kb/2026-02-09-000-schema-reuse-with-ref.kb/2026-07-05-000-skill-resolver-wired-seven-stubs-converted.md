# Progress (2026-07-05): skill:// resolver wired; seven stubs converted

Wired the `skill://` resolver (`_retrieve_skill`/`_REGISTRY`, drafted in an
earlier uncommitted pass) into `KbValidator` by passing `registry=_REGISTRY`
in `validate_against_schema`. Proven red-green with a new pytest suite
(`frontmatter_validate_test.py`, `DescribeSkillRefResolution`) — first
observed `referencing.exceptions.Unresolvable` before the wiring, then green
after. `llm-kb/pyproject.toml` + `uv.lock` added so the skill has its own
pytest-capable venv (none existed before).

Converted all seven downstream stub copies to real one-line `$ref`s at the
skeleton (skeleton files themselves untouched, still canonical):

- `todo.jsonschema.yaml`: llm-kb, llm-collab, llm-subtask, llm-must-read-kb
- `ideas.jsonschema.yaml`: llm-kb, llm-collab, llm-subtask

Each conversion verified against real `.claude/{todo,ideas}.kb/` data
(0 errors) before moving to the next, and against a deliberately-broken
frontmatter file (confirmed the stub still rejects bad data, not just
passing everything silently).
