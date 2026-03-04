# Parentage as Why/How

## Decision

The filesystem tree expresses the primary why/how relationship.
Parent = why (motivation/abstraction). Child = how (realization/concreteness).
Nesting depth = abstraction level.

`why[]` in frontmatter expresses supplementary upward links for claims
with multiple independent justifications.

## Discussion

### Unifying two mechanisms

The design tower used numbered directories (010-mission, 020-goals, etc.)
to make abstraction visible. The discourse graph used `$ITEM.kb/` nesting.

Key insight from the prior session: both express the same relationship.
Walking up = "why does this exist?" Walking down = "how is this realized?"
The design tower made abstraction visible through directory names; nesting
depth achieves the same thing without fixed vocabulary.

Demonstrated working: `config-debug-hell.kb/test-maintenance` — parent
is the "why" (how to manage config debug hell), child is the "how"
(test maintenance strategy).

### One parent limitation

Filesystem nesting allows only one parent. A claim supported by two
independent lines of reasoning can only live under one. `why[]` in
frontmatter handles the supplementary links.

Convention: parentage captures the PRIMARY justification. `why[]` captures
additional support. The tree shows the main line of reasoning; cross-
references show the rest.

### `why[]` is conjunctive by default

`why: [A, B, C]` means "this claim holds because of A AND B AND C
together." Independent support lines are expressed as separate claims
or in body text. Open question: whether this needs revisiting.

### Path resolution

Cross-references use upward/lexical scoping — walk up ancestor scopes
until a match is found.

- Hoisting (moving a node to a broader scope) is non-breaking
- Local files shadow ancestors with the same name
- "Move nodes down, don't reach in" — inner scopes reference outer
  nodes without explicit paths

This convention proved robust during the vim config decomposition.
Reparenting sources to broader/deeper scopes doesn't break references.
