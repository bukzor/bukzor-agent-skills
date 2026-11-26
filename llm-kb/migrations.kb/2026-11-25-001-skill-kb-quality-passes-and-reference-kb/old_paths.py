#!/usr/bin/env python3
"""Find, or rewrite, live readers of the paths migration 2026-11-25-001 moved.

    old_paths.py report    # print path:line:text per live hit; exit 1 on any
    old_paths.py rewrite   # rewrite each hit's path literal in place; exit 0

Live means not a frozen record. Frozen: devlogs, ADRs, case studies, other
migrations' entries, the replication run, the parent plan and its handoff kb,
the fleet ledger's note on the declined name, a todo file marked
`status: done` (and the `.kb/` beside it), and checked-off todo items with
their continuation lines. Both modes act on the same set, so a clean report
is the postcondition of `rewrite`.
"""

import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

NAMES = (
    "splitting-large-docs|complete-example|pattern-guide|dated-slug-filename|"
    "schema-reuse|frontmatter-outside-a-collection|creating-a-new-kb|"
    "schema-design|create-new-trigger|todo\\.kb-pattern|four-tier-system|"
    "marker-commands"
)
LOOSE = "theories|persistence|sort-goals-into-four-bins"

# (pattern, replacement): each pattern is the old path literal; replacing it
# yields text the pattern no longer matches, so a rewrite is idempotent.
RULES = [
    (r"self-audit\.kb", "quality-passes.kb"),
    (r"self-audit\.md", "quality-passes.md"),
    (r"run-self-audits", "run-quality-passes"),
    (r"llm-design-kb/principles\.kb", "llm-design-kb/skill.kb/quality-passes.kb"),
    (r"skill\.kb/principles\.kb", "skill.kb/quality-passes.kb"),
    (r"(llm-kb|llm-subtask|llm-must-read-kb)/references/", r"\1/skill.kb/reference.kb/"),
    (r"(?<![\w./-])references/(" + NAMES + r")\.md", r"skill.kb/reference.kb/\1.md"),
    (r"skill\.kb/(" + LOOSE + r")\.md", r"skill.kb/reference.kb/\1.md"),
    (r"\.\./\.\./(theories|sort-goals-into-four-bins)\.md", r"../../reference.kb/\1.md"),
]
RULES = [(re.compile(p), r) for p, r in RULES]

FROZEN_GLOBS = [
    "docs/dev/devlog/*",
    "*/docs/dev/devlog/*",
    "docs/dev/adr/*",
    "*/docs/dev/adr/*",
    "*/docs/adr/*",
    "*/docs/dev/case-studies.kb/*",
    "llm-kb/migrations.kb/*",
    "docs/dev/strata.replication.run.kb/*",
    ".claude/todo.kb/2026-11-25-000-*",
    "docs/dev/claims.kb/design.claims.kb/authorship.kb/"
    "the-pass-collection-is-quality-passes.md",
]
DONE = re.compile(r"^status: (done|closed)\s*$", re.M)


def is_done(path: Path) -> bool:
    return bool(DONE.search(path.read_text()[:2000]))


def frozen(rel: str) -> bool:
    if any(fnmatch.fnmatch(rel, g) for g in FROZEN_GLOBS):
        return True
    path = ROOT / rel
    if "/todo.kb/" in rel or rel.startswith(".claude/todo.kb/"):
        if is_done(path):
            return True
        # a file inside `X.kb/` belongs to the record of `X.md`
        for parent in path.parents:
            if parent == ROOT:
                break
            if parent.suffix == ".kb":
                sibling = parent.with_suffix(".md")
                if sibling.exists() and is_done(sibling):
                    return True
    return False


def candidates() -> list[str]:
    pat = "|".join(p.pattern for p, _ in RULES)
    out = subprocess.run(
        ["git", "-C", str(ROOT), "grep", "-lIE", "-e", pat.replace("(?<![\\w./-])", "")],
        capture_output=True,
        text=True,
    ).stdout
    return [rel for rel in out.splitlines() if not frozen(rel)]


def live_lines(text: str):
    """Yield (number, line, live) with checked-off items marked not live."""
    in_checked = False
    for number, line in enumerate(text.split("\n"), 1):
        stripped = line.lstrip()
        if stripped.startswith("- [x]"):
            in_checked, indent = True, len(line) - len(stripped)
            yield number, line, False
        elif in_checked and line.strip() and len(line) - len(stripped) > indent:
            yield number, line, False
        else:
            in_checked = False
            yield number, line, True


def main(mode: str) -> int:
    hits = 0
    for rel in candidates():
        path = ROOT / rel
        out = []
        for number, line, live in live_lines(path.read_text()):
            new = line
            if live:
                for pat, repl in RULES:
                    new = pat.sub(repl, new)
            if new != line:
                hits += 1
                if mode == "report":
                    print(f"{rel}:{number}:{line.strip()[:140]}")
            out.append(new)
        if mode == "rewrite":
            path.write_text("\n".join(out))
    return 1 if mode == "report" and hits else 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("report", "rewrite"):
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
