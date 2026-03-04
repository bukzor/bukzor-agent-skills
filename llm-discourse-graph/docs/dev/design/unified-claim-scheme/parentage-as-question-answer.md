# Parentage as Question/Answer

## Decision

Within this framework, parent/child relationships SHALL be considered
question/answer relationships. The filesystem tree expresses the primary
question→answer structure. Parent = question (claim with unresolved
referent). Children = candidate answers. Nesting depth = abstraction level.

The question type varies by use case — "how?" for design knowledge,
"why?" for forensic analysis, "what should?" for disagreements, "what
Xs exist?" for categorization, etc.

Directory names SHOULD spell out the question for disambiguation
(e.g. `why-did-server-crash.kb/`). `$NOUN.kb/` MAY be used as
shorthand when the question type is obvious from context.

The design tower is a restriction where all questions are "how?"

`why[]` in frontmatter expresses supplementary upward links for claims
with multiple independent justifications.

## Discussion

### Generalization from why/how

The original insight (sv-bcb1) was that why/how is the shared organizing
principle. Walking up = "why does this exist?" Walking down = "how is
this realized?" But subsequent analysis (2026-03-04 lane-mixing session)
revealed that why/how is one instance of a more general pattern:
parent poses a question, children propose answers.

Evidence: the Alice/Bob disagreement example has a "what should we do?"
parent, not a "why/how" parent. Forensic analysis has "why did X happen?"
parents. The design tower has "how do we achieve X?" parents. All are
question→answer, but only the last is specifically why/how.

### Unifying two mechanisms

The design tower used numbered directories (010-mission, 020-goals, etc.)
to make abstraction visible. The discourse graph used `$ITEM.kb/` nesting.

Both express the same relationship: parent is a question, children are
candidate answers. The design tower made abstraction visible through
directory names; nesting depth achieves the same thing without fixed
vocabulary.

Demonstrated working: `config-debug-hell.kb/test-maintenance` — parent
is the question (how to manage config debug hell), child is one answer
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

## Q&A (2026-03-04 lane-mixing review)

### Q: How are contradictions expressed without a `contradicts[]` field?

Competing claims are siblings under a shared question-parent, with
per-party validity expressing who endorses which position. To contest
an existing claim: `mkdir $(basename $claim .md).kb/`, which promotes
the claim to a question with competing children. The original claim
becomes one child; the counter-claim becomes a sibling. This is
non-destructive — no rearrangement of the existing graph required.

### Q: Is categorization really question/answer?

`rules.kb/dealing.md` reads as "the rules include dealing." Reframed:
"What rules exist?" → "Dealing is one." This is the degenerate case —
the question is purely enumerative and the answers are trivially
accepted (validity defaults to 1). The framework treats this as
definitional: all parentage is question/answer, with categorization
as the weakest instance.
