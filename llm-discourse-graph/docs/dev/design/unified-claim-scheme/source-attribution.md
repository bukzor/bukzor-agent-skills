# Source Attribution

## Decision

Sources are provenance metadata on claims, not a separate node type.
Inline by default, `$ref` for DRY. Fine-grained locators via extension
fields on source references.

## Discussion

### Sources resist collapsing into claims

Twice during design, sources pulled toward being a distinct type:
1. DRY — multiple claims sharing the same source metadata (title, URL,
   authors) need a shared reference to avoid drift.
2. Party — debate participants are sources that multiple claims attribute
   positions to.

Resolution: sources ARE claims when externalized (a `$ref` target is a
markdown file that can contain any content). The `$ref` mechanism provides
DRY without requiring a separate ontological type. The source file can
have its own validity, its own frontmatter — it's a claim about an
external document's existence and relevance.

### Fine-grained locators

Academic standards for citing within a document:
- W3C Web Annotation / Media Fragments — selectors for text and media
- CTS (Canonical Text Services) — hierarchical text addressing
- Citation styles (APA, Chicago) — page, paragraph, figure

Our approach: `$ref` + domain-specific extension fields.

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

The schema validates `$ref`; locator fields are domain-specific and
advisory. This keeps the core schema simple while allowing arbitrarily
precise attribution.

### Temporal ordering from source attribution

For real-time decomposition (e.g., YouTube debates), temporal sequence
is a property of the source, not the claim graph. Claims have their own
logical structure (parentage = why/how); temporal order is reconstructable
by sorting on source timestamps. Two independent orderings, cleanly
separated.

### Upward path resolution and sources

The "look in parent scope" convention means reparenting a source file
to a broader scope is non-breaking for all inner references. A source
shared across multiple sub-scopes naturally lives at their common
ancestor — upward resolution finds it from anywhere below.
