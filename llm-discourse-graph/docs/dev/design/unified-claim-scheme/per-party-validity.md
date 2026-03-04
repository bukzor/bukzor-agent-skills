# Per-Party Validity

## Decision

Validity is either a single axes object (everyone agrees) or a map keyed
by party identifier with `$all` as the consensus/default entry. Per-party
entries override `$all` via JSON Merge Patch (RFC 7396) semantics.

```yaml
# Everyone agrees
validity:
    $all:
        truth: 0.8

# Parties disagree
validity:
    $all:
        truth: 0.8
    sources/speaker-a.md:
        truth: 0.95
    sources/speaker-b.md:
        truth: 0.3
        utility: -0.2

# No consensus
validity:
    sources/speaker-a.md:
        truth: 0.9
    sources/speaker-b.md:
        truth: 0.3
```

## Discussion

### Why "party" entered the ontology

Prior use cases were all single-voice (one ChatGPT conversation) or
implicit two-party (user + assistant in a live chat). Multi-party sources
(debates, panel discussions) require tracking who holds what position.
Party was always needed; simple cases hid the gap.

### Why a map, not an array

One entry per party (enforced by map key uniqueness), direct lookup by
party name, no redundant `party:` field. Each value is a pure
validity-axes object — same shape as `$all`.

### Why `$all`, not `@all` or `@none` or `@default`

- `@` is reserved in YAML — requires quoting. `$` is not.
- `$` prefix has precedent from JSON Schema (`$ref`, `$defs`, `$schema`).
- `$all` means "applies to all parties" — clearer than `$none` ("no
  specific party") or `$default` ("the fallback").
- Unprecedented in the `$`-prefix ecosystem, but close enough to be
  unsurprising.

### Why `$all` is optional

Two cases where requiring it is awkward:
1. No consensus exists — forcing `$all` values would be artificial.
2. Everyone agrees — `$all` wrapper is noise around the common case.

Three-tier cascade: schema defaults → `$all` → per-party. Each tier
optional. When `$all` is absent, per-party entries merge-patch against
schema defaults.

### Why merge-patch (RFC 7396)

Battle-tested semantics for "missing = inherit, present = override."
Small spec, reference implementations in every language, trivial to
implement correctly.

### Party keys as source references

Party identifiers are strings that may be `$ref`-style paths to source
documents. This ties each party to a provenance document without adding
a separate linking mechanism. The validity schema doesn't need to know
about `$ref` — that's a cross-cutting concern.
