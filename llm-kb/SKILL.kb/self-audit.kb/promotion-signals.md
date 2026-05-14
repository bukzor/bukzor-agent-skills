# Self-audit: promotion signals

Flat `.md` files signal when they want to become `.kb/` directories.
This scan catches those signals while editing, before the promotion
gets costly.

## Goal

Any flat `.md` that should be a `.kb/` gets promoted before it
accumulates more content under the wrong shape.

## Procedure

For each flat `.md` you touched, scan for these signals:

- Plural filename -- `patterns.md`, `tools.md`, `alternatives.md`.
  The name signals a listing; the directory shape should follow.
- Parallel sections of the same type -- multiple `##` or `###`
  headings describing items of the same kind, even in prose form.
- Listing-heavy content -- most of the file is a numbered list,
  table, or parallel enumeration of homogeneous items.
- Per-item growth pressure -- items want their own frontmatter,
  lifecycle (status, last-updated), or paragraph. Any single item
  exceeding ~50 tokens triggers unconditionally.

## Recovery

When any signal fires, promote per
`../procedures.kb/promote-to-collection.md`.

## When to skip promotion

A fixed 2-4-item list of one-line entries stays as flat prose. The
signal is **growth pressure**, not the mere presence of a list.

## Related

- `per-file-scope.md` -- single-file scope audit; this scans
  across many.
