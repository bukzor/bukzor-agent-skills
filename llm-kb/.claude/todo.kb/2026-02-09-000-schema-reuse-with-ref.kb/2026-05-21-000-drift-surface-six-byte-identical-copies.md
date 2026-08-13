# Drift-surface update (2026-05-21)

Six schema files are now **byte-identical** (md5 `91c4d226…`): skeleton's
`todo.jsonschema.yaml` and `ideas.jsonschema.yaml`, plus the four downstream
copies (`llm-subtask/.claude/ideas`, `llm-kb/.claude/{todo,ideas}`,
`llm-collab/.claude/todo`). Previously there were two hash families
(skeleton-with-`managed-by`-const vs skill-local-without); the
strict-`managed-by`-propagation session collapsed both into one. Each file is
now ~200 lines (added `status`, `required-reading`, `suggested-reading`,
`related-effort` and flipped `additionalProperties: false`).

Implication for `$ref` work: any further field addition now requires **six
hand-edits** instead of the prior two-shape surgery. Drift pressure is
strictly worse per change. The mitigation is unchanged — implement
stub-`$ref` resolution (decision B, 2026-05-18) and collapse the five
downstream copies into one-line pointers at `llm-subtask/skeleton/.claude/`.

Inventory diverges from the 2026-05-15 list: that entry enumerated five
paths, omitting `llm-kb/.claude/todo.jsonschema.yaml` (which has lived in
the repo since `6a2c361`, the original centralization commit). The actual
count was six all along; today's session updated all six in lockstep.
