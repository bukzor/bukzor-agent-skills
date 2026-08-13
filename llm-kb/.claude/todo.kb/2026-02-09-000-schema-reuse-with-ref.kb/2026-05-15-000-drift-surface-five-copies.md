# Drift surface (2026-05-15)

The SKELETON-DEFAULT pattern (canonical schema in
`llm-subtask/skeleton/.claude/`, hand-copied to each consuming skill's
`.claude/`) now has three live copies of `ideas.jsonschema.yaml` and two
of `todo.jsonschema.yaml`. Drift risk is real until `$ref` lands.
Affected paths:

- `llm-subtask/skeleton/.claude/ideas.jsonschema.yaml` (canonical)
- `llm-subtask/skeleton/.claude/todo.jsonschema.yaml` (canonical)
- `llm-kb/.claude/ideas.jsonschema.yaml` (copy)
- `llm-subtask/.claude/ideas.jsonschema.yaml` (copy)
- `llm-collab/.claude/todo.jsonschema.yaml` (copy)

Resolution path: implement `$ref` resolution, then convert each copy to a
single-line `$ref` pointer.

(2026-05-21 correction: the actual count was six all along -- this list
omitted `llm-kb/.claude/todo.jsonschema.yaml`, in the repo since
`6a2c361`, the original centralization commit.)
