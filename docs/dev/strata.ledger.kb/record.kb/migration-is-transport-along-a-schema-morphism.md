---
label: MIGRATE
standing: agent
why:
  - validation-is-a-typing-map.md
---

# Migration Is Transport Along a Schema Morphism

Schemas and their changes form a category: renames are isomorphisms,
splits and merges are morphisms with known shapes. A migration should
be *recorded* as the schema morphism and *executed* as the transport
of instances along it -- the universal lift, which is mechanical once
the morphism is stated. A migration log is then a diagram of schemas,
and the instance history is required to be a lift of that diagram.

Consequence: migration scripts that restate the transport by hand are
caches of a derivable value, with all the obligations that entails.
