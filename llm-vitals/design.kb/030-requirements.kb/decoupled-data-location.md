---
why:
  - unify-personal-and-enterprise
  - grow-incrementally
---

# Decoupled Data Location

The skill code must not assume any specific filesystem location for
vital data. The user provides one or more `vitals_root:` paths via
configuration; the skill operates over the union.

This requirement is what enables:

- Multiple data roots (e.g., personal in `private.evan-family`,
  business in `private.bukzor-llc`)
- The skill to be public/open-source while data remains in private
  repos
- Other users to adopt the skill without forking it

The skill is the durable artifact; the data is the user's. They must
be independently versioned, hosted, and shareable.
