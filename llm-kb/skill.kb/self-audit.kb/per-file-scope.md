# Self-audit: per-file scope

A file in a `.kb/` should describe **one thing**. This audit catches
files that have grown to cover several -- the failure mode that turns a
kb into a few sprawling documents instead of many focused ones.

## Goal

Each file describes exactly one item of the collection's type. Files
covering multiple items get promoted to a sub-`.kb/` with one item per
file.

## Procedure

Open each touched file. Look for parallel `##` or `###` sections naming
items of the same kind -- multiple items inside one file is the trigger.

The 50-token tripwire: if any single sub-item exceeds ~50 tokens of
explanation, promote unconditionally. Below that, judgement applies (a
fixed 2-4-item list of one-line entries is fine as prose).

## Recovery

Promote per `../procedures.kb/promote-to-collection.md`.

## Related

- `promotion-signals.md` -- broader scan for the cross-file signals
  that trigger promotion.
