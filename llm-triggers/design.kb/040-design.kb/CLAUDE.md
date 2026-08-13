# 040-design.kb — maintenance guide

One entry per subsystem design element: vocabulary, formats,
contracts, adapters.

## What Belongs Here

Decisions about how the trigger subsystem works, at
trigger-subsystem grain.

## What Does NOT Belong Here

- Ecosystem-level properties — design-next.kb's surface; it cites
  down here, never the reverse restated
- Consumer internals (task class, record class) — cite, don't absorb
- Implementation detail of a built shim — lives with the shim's code
  once it exists

Frontmatter conforms to `../040-design.jsonschema.yaml`.

## When to Add / Read

- **Add** when a design discussion settles (or usefully frames) a
  subsystem abstraction or boundary.
- **Read** before building a shim, a sweep, or a consumer of the
  wake-condition grammar.
