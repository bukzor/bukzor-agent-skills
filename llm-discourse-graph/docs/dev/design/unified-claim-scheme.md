# Unified Claim Scheme

Living specification for a unified knowledge representation scheme that
merges the discourse graph and design tower into a single structure.

## Data Model

### One node type: Claim

Everything is a claim — a propositional unit with varying attributes.
Former node types collapse into claims with different attribute profiles:

| Former type | As a claim |
|---|---|
| Definition | High normativity (validity.utility relevant, validity.truth = 1 by construction) |
| Question | Incomplete — has unknown referents (per erotetic logic: Hamblin, Hintikka, Groenendijk & Stokhof) |
| Deduction | Has `why[]` with certainty = 1.0 on the inferential link |
| Inference | Has `why[]` with certainty < 1.0 |
| Observation | Has source attribution, no `why[]` |

Node type is emergent from the claim's attributes and graph position, never
stored explicitly.

### One structural relation: Parentage = Question/Answer

Within this framework, parent/child relationships SHALL be considered
question/answer relationships. The filesystem tree IS the primary
inferential structure:

- Parent = a question (claim with unresolved referent)
- Children = candidate answers

The question type varies by use case:

| Use case | Parent question type | Children are... |
|---|---|---|
| Design knowledge | "How do we achieve X?" | Implementation approaches |
| Forensic analysis | "Why did X happen?" | Hypotheses/causes |
| Disagreement | "What should we do about X?" | Competing proposals |
| Definition | "What is X?" | Competing/complementary definitions |
| Categorization | "What Xs exist?" | Members |
| Fact-finding | "What is true about X?" | Findings/observations |

Directory names SHOULD spell out the question for disambiguation
(e.g. `what-is-consciousness.kb/`, `why-did-server-crash.kb/`).
Self-documenting names repay their verbosity in LLM-collaborative
workflows where only names are visible (e.g. `ls -RF`, cross-session
handoff, smaller models).

`$NOUN.kb/` MAY be used as shorthand when the question type is
obvious from context (implies "What $NOUNs exist?").

The design tower is a restriction of this general scheme where all
questions are required to be "how?"

Parent-child nesting via `$ITEM.kb/` expresses the primary question/answer
link. `why[]` in frontmatter expresses supplementary (non-primary) support.

### Validity: Three Axes

A claim's epistemic/pragmatic evaluation. Term borrowed from Habermas's
"validity claims" (Geltungsansprüche) — truth, rightness, sincerity,
comprehensibility as independently challengeable dimensions.

Our three axes:

| Axis | Range | Default | Domain |
|---|---|---|---|
| truth | 0–1 | 1 | Ontological — assessor's best estimate of correspondence to reality |
| certainty | 0–1 | 1 | Epistemic — how confident? |
| utility | -1–1 | 1 | Pragmatic — how valuable? Negative = harmful |

Defaults mean zero bits of denotation when a claim is fully accepted.
Defaults specified via JSON Schema `default` keyword.

### Validity: Per-Party Override

When multiple parties evaluate a claim differently, validity becomes a map
keyed by party identifier, with `$all` as the distinguished key for
consensus/default values.

Per-party entries relate to `$all` via JSON Merge Patch (RFC 7396)
semantics: missing keys inherit, present keys override.

The `$` prefix borrows the reserved-key convention from JSON Schema
(`$ref`, `$defs`). `$all` means "applies to all parties."

Party keys are strings, optionally `$ref` values pointing to source
documents for DRY.

### Challenge Modes Are Emergent

A claim's position on the validity axes + its graph structure determine
which challenges are valid:

| Region | Valid challenge | Derives from |
|---|---|---|
| Low normativity, empirical basis | Correctness (accuracy ↔ validity blend) | Has source, low utility relevance |
| High normativity | Utility ("not useful/desirable") | High utility relevance |
| High analytic | Definitional ("not a useful concept") | truth = 1 by construction |
| Any | Scope ("overstated reach") | Cross-cutting |

Correctness unifies Pollock's rebutting and undercutting defeaters into a
single challenge whose character varies with the claim's empirical ↔
logical basis. Basis is emergent from graph structure (has source → empirical
end; has `why[]` → logical end).

### Source Attribution

Sources are provenance metadata on claims, not a separate node type.
Inline by default, `$ref` for DRY when multiple claims share a source.

Fine-grained attribution via locator extensions:

```yaml
sources:
    - $ref: sources/the-book.md
      page: 3
      line: 10
    - $ref: sources/the-video.md
      timestamp: 33.3
    - $ref: sources/the-chat.md
      turn: 33
      line: 44
```

Locator fields (page, timestamp, turn, line) are domain-specific
extensions. The core schema validates `$ref`; locator fields are
advisory.

### Path Resolution

Cross-references use collection-relative paths. Resolution walks up
ancestor scopes until a match is found (upward/lexical scoping).

- Hoisting is non-breaking
- Local files shadow ancestors
- Content lives at the narrowest scope containing all its uses
- "Move nodes down, don't reach in" — upward resolution handles outer
  references naturally

## Schemas

### validity-axes

```yaml
$defs:
    validity-axes:
        type: object
        properties:
            truth:
                type: number
                minimum: 0
                maximum: 1
                default: 1
            certainty:
                type: number
                minimum: 0
                maximum: 1
                default: 1
            utility:
                type: number
                minimum: -1
                maximum: 1
                default: 1
        additionalProperties: false
```

### validity

```yaml
$defs:
    validity:
        type: object
        properties:
            $all:
                $ref: "#/$defs/validity-axes"
        additionalProperties:
            $ref: "#/$defs/validity-axes"
```

`$all` is optional. When absent, per-party entries merge-patch against
schema defaults. Three-tier cascade: schema → `$all` → per-party.

## Examples

### Simple claim (common case)

```yaml
---
validity:
    $all:
        truth: 0.8
why:
    - anti-sycophancy.md
sources:
    - $ref: sources/claude-ai-preferences.md
      section: "Position Defense"
---

Defend assistant's reasoning as long as you can find a legitimate way
to maintain it. Treat user disagreement as a request for deeper analysis,
not grounds for immediate reversal.
```

### Multi-party claim (debate)

```yaml
---
validity:
    $all:
        truth: 0.7
        certainty: 0.6
    sources/speaker-a.md:
        truth: 0.95
        certainty: 0.9
    sources/speaker-b.md:
        truth: 0.3
        utility: -0.2
sources:
    - $ref: sources/the-debate.md
      timestamp: 12.5
---

Modal editing is more efficient once the learning curve is overcome.
```

### Definition (high normativity)

```yaml
---
validity:
    $all:
        utility: 0.9
---

"Confident" means at least 80% estimated likelihood of user agreement,
if fully examined.
```

Truth defaults to 1 (true by stipulation). Certainty defaults to 1.
Only utility varies — how useful is this definition?

### Question (incomplete claim)

```yaml
---
resolved: anti-sycophancy.kb/position-defense.md
sources:
    - $ref: sources/claude-ai-preferences.md
---

How should an LLM handle user disagreement with its conclusions?
```

Questions are claims with unknown referents. `resolved` points to the
claim that fills the blank. `candidate-resolutions` (list) for unresolved
questions with multiple competing answers.

## Design Provenance

### Key Frameworks Cited

- **Habermas** — "validity claims" as the group name for multi-dimensional
  epistemic evaluation
- **Erotetic logic** (Hamblin, Hintikka, Groenendijk & Stokhof) — questions
  as propositions with unfilled variables
- **Pollock** — rebutting vs undercutting defeaters, unified into a single
  correctness challenge
- **RFC 7396** — JSON Merge Patch semantics for per-party override cascade
- **Searle** — direction of fit (word-to-world vs world-to-word) as the
  basis for the normativity axis

Full survey: `unified-claim-scheme/epistemic-dimensions-prior-art.md`

## Open Questions

- Should `why[]` semantics be conjunctive (all premises jointly) or
  disjunctive (each independently sufficient)? Current default: conjunctive.
- ~~How to express contradiction without negation claims?~~ **Resolved:**
  competing siblings under a shared question-parent, with per-party validity
  expressing who endorses which position. No `contradicts[]` field needed.
- How to contest reasoning specifically (not the conclusion)? Current
  approach: meta-claims about the justification, watch for friction.
- Should the design tower's fixed layer vocabulary (mission/goals/
  requirements/etc.) survive as a naming convention?
- Inline/short vs file-based/long claim format — do we want a lightweight
  tier analogous to llm-subtask's ephemeral/tactical split?
