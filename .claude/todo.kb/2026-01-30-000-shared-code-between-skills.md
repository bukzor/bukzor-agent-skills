---
managed-by: Skill(llm-subtask)
cost-benefit-sweh:
  timebox:
    '@value': 2
    confidence: tentative
    rationale: |
      Investigate 2-3 alternatives (per-skill venv with project mode, --script + nearby pyproject.toml sources). Read uv docs, test cases per alternative, compare ergonomics. ~1.5-2.5 SWEh.
  benefit-2w:
    '@value': 0.5
    confidence: tentative
    rationale: |
      Current [tool.uv.sources] inline works with downsides (verbose boilerplate per script, path duplication). Better solution removes per-script tax across many skills. Frontmatter still status:in-progress.
  cost-of-delay-2w:
    '@value': 0.1
    confidence: tentative
    rationale: |
      Boilerplate cost is ongoing per new script. Small but real; no breakage if delayed.
---

# Shared Code Between Skills

## Problem

Multiple skills need to share Python code. No official convention exists.

## Current Solution (Accepted)

Inline `[tool.uv.sources]` in script metadata:

```python
#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["shared"]
#
# [tool.uv.sources]
# shared = { path = "../../lib/shared", editable = true }
# ///
```

Path is relative to script location, not CWD.

**Downsides:**
- Verbose boilerplate in every script
- Path must be repeated in each script
- No centralized dependency management

## Alternatives to Investigate

### Per-skill venvs

Each skill directory has its own `.venv` and `pyproject.toml`:

```
llm-collab/
├── pyproject.toml      # defines deps + sources
├── .venv/              # skill-specific venv
└── bin/
    └── llm-collab-adr  # uses project mode, not --script
```

Scripts use `uv run` (project mode) instead of `uv run --script`.

**Questions:**
- How do bin/ scripts invoke uv in project mode?
- Does the shebang work?
- How is the shared lib referenced?

### Per-skill pyproject.toml with sources redirect

Similar to above but scripts remain `--script` mode, with the pyproject.toml
only providing the sources redirect.

**Questions:**
- Does `uv run --script` respect a nearby pyproject.toml's `[tool.uv.sources]`?
- Or does --script mode ignore project context entirely?

## Investigation (2026-07-19)

Ran real, disposable experiments (`/tmp/uv-script-sources-test/`, not
committed) with `uv 0.11.29`.

**Question 2 answered — `--script` mode ignores nearby `pyproject.toml`
entirely.** A `dependencies = ["shared-lib"]` PEP 723 script next to a
`pyproject.toml` declaring `[tool.uv.sources] shared-lib = { path =
"../shared_lib" }` fails outright:
```
× No solution found when resolving script dependencies:
  ╰─▶ Because shared-lib was not found in the package registry and you
      require shared-lib, we can conclude that your requirements are
      unsatisfiable.
```
`--script` mode has its own isolated resolution; a nearby project file
is never consulted. Ruled out.

**Question 1 answered — per-skill project mode works end to end, and
is already proven in production.** `llm-kb` already *is* this
pattern: it's a `[tool.uv.workspace]` member (root `pyproject.toml`),
has its own `llm-kb/pyproject.toml`, and `llm-kb/bin/llm.kb-validate`
is a thin bash wrapper (`cd "$here/.." && uv run python -m
llmd.frontmatter_validate ...`) — no PEP 723 header, no per-script
`[tool.uv.sources]`. Reproduced the cross-skill case explicitly: a
`consumer-skill/pyproject.toml` with
`[tool.uv.sources] shared-lib = { path = "../shared_lib", editable = true }`
plus a `bin/consumer-tool` wrapper (`uv run python -c 'import
shared_lib; ...'`) resolved and ran cleanly — `hello from shared_lib`,
exit 0, one-time `uv sync`-style venv build, no boilerplate repeated
per script.

## Decision

Adopt **per-skill `pyproject.toml` + project mode** (alternative 1)
as the convention for skills that need another skill's `lib/python`
code, superseding inline per-script `[tool.uv.sources]` for that case:

- Skill becomes a `[tool.uv.workspace]` member of the root
  `pyproject.toml` (one-line registration, like `llm-kb` already is).
- The skill's own `pyproject.toml` declares `[tool.uv.sources]` once
  for any other skill it depends on.
- `bin/` scripts are thin bash wrappers (`cd` to skill root, `exec uv
  run python -m ...`/`-c ...`), matching `llm-kb/bin/llm.kb-validate`'s
  existing shape — not PEP 723 `--script` shebangs.

This doesn't touch ADR `2025-12-09-003-lib-python-pattern-for-testable-skill-scripts.md`:
that ADR's `#!/usr/bin/env -S uv run --script` shebang pattern is for
self-contained scripts using only their *own* skill's code, which has
no boilerplate problem and no reason to change. This item was
specifically about the cross-skill case, which `--script` mode cannot
serve (confirmed above) — the two patterns coexist, chosen per script
based on whether it needs another skill's code.

**Not rolled out to other skills this pass** — that's a separate
migration (audit which scripts currently use inline
`[tool.uv.sources]` for cross-skill sharing — none found repo-wide
today; the only `tool.uv.sources` in the tree is the root
`pyproject.toml`'s `basedpyright-as-pyright` entry — so this is a
forward-looking convention, not an active migration debt).
