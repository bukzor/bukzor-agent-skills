# Shared Shape, Separate Semantics

Two collections that look alike (same node/edge/elaboration shape,
same lifecycle, same file conventions) are not thereby the same
thing. Before merging them, ask whether their *content* means the
same kind of thing, not just whether their *mechanics* match.

When the mechanics match but the semantics don't, extract the shared
mechanics as a primitive at the layer below (a spec-level shape, a
common schema fragment, a shared procedure) and keep the collections
themselves separate, each with its own vocabulary. Interop between
them comes from ordinary cross-references, not from forcing one
vocabulary to cover both. This is the same move as factoring a base
class out of two unrelated-but-similarly-shaped types: share the
shape, not the identity.
