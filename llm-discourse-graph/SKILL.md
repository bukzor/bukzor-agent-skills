---
name: llm-discourse-graph
description: "Epistemic knowledge graph for collaborative human-LLM inquiry. Five collections: questions, claims, deductions, sources, definitions."
---
--- # workaround: anthropics/claude-code#13005
setup: |
    All projects that depend on this skill should have as `CLAUDE.md` frontmatter:

    ```yaml
    --- # workaround: anthropics/claude-code#13003
    requires:
        - Skill(llm-discourse-graph)
    ```
---

# llm-discourse-graph

Epistemic knowledge graph for collaborative human-LLM knowledge management.
Built on the `llm.kb` pattern. Models what we believe, why, how confidently,
and where it comes from.

## The five collections

| Collection | What it holds |
|---|---|
| `questions.kb/` | Open inquiries that structure investigation |
| `claims.kb/` | Propositional assertions — observed or hypothesized |
| `deductions.kb/` | Structured inference — premises that entail or contradict a conclusion |
| `sources.kb/` | Provenance references (papers, reports, testimony) |
| `definitions.kb/` | What terms mean — scope, boundaries, usage |

### When to use each

- **Question**: someone asks something that needs investigation
- **Claim**: someone asserts something that may or may not be true
- **Deduction**: premises entail or contradict a conclusion (claim or deduction) — the body text explains *why*
- **Source**: citing where claims originate
- **Definition**: establishing what a term means, independent of claims about it

## Scoping and hierarchy

Elaboration uses the standard `llm.kb` nesting convention: `$ITEM.kb/`
as a sibling of `$ITEM.md`. Sub-scopes contain the same five collection
types (only those needed). The project root is itself an implicit scope.

### When to elaborate

- Multiple claims supporting/countering the same parent
- Sub-questions arising from a question or claim
- A deduction complex enough to need its own sub-claims

Most nodes should NOT have elaboration. A few sentences of body text with
frontmatter references to other nodes is the normal case.

### Roll-up

The parent node IS the summary. When a sub-scope resolves (e.g. a question
is answered), update the parent node's status and body accordingly.

## Path resolution

Cross-references use collection-relative paths: `claims.kb/conways-law.md`.
Resolution walks up ancestor scopes until a match is found, up to project root.

- Hoisting is non-breaking
- Local files shadow ancestors with the same name
- Content lives at the narrowest scope containing all its uses
- Prefer moving a node down over reaching in with explicit paths —
  upward resolution handles outer references naturally

## Schemas

Five `$COLLECTION.jsonschema.yaml` files, placed alongside the collections
they govern. See `schemas/` in this skill directory.

## Relations and metadata

Cross-references are paths in YAML frontmatter (`claims.kb/x.md`). Epistemic
metadata (status, likelihood, kind) tracks the standing of
each node. Questions derive their state from field presence: `resolved` means
answered, `candidate-resolutions` means under investigation, neither means
new/open. See the schemas for the complete field definitions.

### The core wiring pattern

Questions are answered by claims. Claims are supported by deductions.
Deductions draw on other claims as premises.

```
question
  candidate-resolutions: [claim]
                           ↑ conclusion
                         deduction
                           premises: [claim, claim, ...]
```

- `candidate-resolutions` points to **claims**, not deductions
- `conclusion` points to a **claim or deduction**, not a question
- `depends` expresses "needs context from" without implying support or refutation

## Creating a discourse graph

1. Create a scope directory with CLAUDE.md declaring this skill
2. Link or copy `$COLLECTION.jsonschema.yaml` schemas from `schemas/`
3. Create collections as needed — start with `sources.kb/` and `questions.kb/`
4. Populate nodes as markdown files with YAML frontmatter
5. Wire questions to claims via `candidate-resolutions`, claims to
   deductions via `conclusion`/`premises`
6. Elaborate nodes into sub-scopes when they outgrow a single file

### Decomposition workflow

When extracting a discourse graph from a source document:

1. **Source** — create the provenance node first
2. **Questions** — identify the inquiries the source addresses
3. **Claims + Deductions** — interleaved, not separate passes. Each claim
   is either justified by a deduction or fundamental.
4. **Wire** — link questions to their candidate-resolutions, add `depends`
5. **Scope** — identify strictly inner questions and nest them

## Reading a discourse graph

```bash
ls */                                        # What collections exist
grep -rL "resolved:" questions.kb/*.md        # Open questions
cat claims.kb/some-claim.md                  # Read a claim
ls claims.kb/some-claim.kb/                  # Has elaboration?
grep -l "status: contested" claims.kb/*.md   # Find contested knowledge
```

## Design rationale

See `docs/dev/adr/` for decision records covering collection types, lexical
scoping, elaboration conventions, terminology, similarity groups, and the
open world assumption.
