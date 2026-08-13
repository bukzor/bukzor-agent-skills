# Circular-ref finding (2026-07-05, experiment)

Scratch experiment at `trash/circular-ref-experiment/` (repo root, not
committed): two schemas, `a.jsonschema.yaml#/definitions/a_node` and
`b.jsonschema.yaml#/definitions/b_node`, each `$ref`ing the other --
a genuine mutual cycle in the schema graph. Validated a 3-level-deep
finite instance (`a -> b -> a`) through the real `load_schema` /
`validate_against_schema` path: resolved instantly, no hang, no
recursion error. A second instance with an error injected at the
deepest level correctly surfaced it at `next.next` (both the missing
`label` and the `additionalProperties` violation), proving the cycle
is actually traversed, not silently short-circuited.

**Conclusion: no implementation needed.** `referencing`/`jsonschema`
resolve `$ref` lazily, per validated node, rather than eagerly
flattening the schema graph into a tree. A cycle among *schema files*
is harmless as long as the *instance data* being validated is finite --
which YAML/JSON instance data always is (no aliases/anchors produce
graph cycles in the parsed value itself). The risk the checklist item
anticipated (infinite resolution loop) doesn't exist for this
validator's usage pattern. No code change, no test added to the
committed suite -- the experiment stands as the verification.
