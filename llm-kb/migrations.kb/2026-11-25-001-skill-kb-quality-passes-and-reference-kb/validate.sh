#!/bin/bash
# validate.sh: report drift from migration 2026-11-25-001. Read-only; exits 1
# on any finding. Checks, in order: old locations are gone; no live reader of
# an old path; no loose file in a `skill.kb/` (a collection's synthesis file
# and a schema sibling are not loose); each `reference.kb/` has a CLAUDE.md;
# `llm.kb-validate-links` is clean over the `skill.kb/` trees.
set -euo pipefail
shopt -s failglob
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

HERE="$(dirname "$(readlink -f "$0")")"
ROOT="$(readlink -f "$HERE/../../..")"
status=0

finding() {
  echo "FINDING: $*"
  status=1
}

if (( DEBUG > 0 )); then
  set -x
fi

# 1. old locations: a root references/, self-audit and principles paths
mapfile -t found < <(
  find "$ROOT" -mindepth 2 -maxdepth 3 \
    \( -path '*/.git' -o -path '*/node_modules' -o -path '*/.venv' -o -path '*/trash' \) -prune -o \
    \( \( -type d -name references -path "$ROOT/*/references" \) \
      -o -name 'self-audit.kb' -o -name 'self-audit.md' -o -name 'run-self-audits.md' \
      -o \( -type d -name principles.kb -path '*/llm-design-kb/skill.kb/*' \) \) \
    -print
)
for path in "${found[@]}"; do
  finding "old location still present: ${path#"$ROOT"/}"
done

# 2. live readers of an old path
"$HERE/old_paths.py" report || status=1

# 3. loose files in a skill.kb/
while IFS= read -r skill_kb; do
  while IFS= read -r file; do
    name="${file##*/}"
    [[ "$name" == CLAUDE.md ]] && continue
    [[ "$name" == *.jsonschema.yaml ]] && continue
    [[ "$name" == *.md && -d "${file%.md}.kb" ]] && continue  # synthesis file
    finding "loose file in skill.kb/: ${file#"$ROOT"/}"
  done < <(find "$skill_kb" -mindepth 1 -maxdepth 1 -type f)
done < <(find "$ROOT" -mindepth 2 -maxdepth 2 -type d -name skill.kb)

# 4. each reference.kb/ carries the collection guide llm-kb asks for
while IFS= read -r ref_kb; do
  [[ -f "$ref_kb/CLAUDE.md" ]] || finding "no CLAUDE.md: ${ref_kb#"$ROOT"/}"
done < <(find "$ROOT" -mindepth 3 -maxdepth 3 -type d -name reference.kb -path '*/skill.kb/*')

# 5. path references inside the moved trees resolve
find "$ROOT" -mindepth 2 -maxdepth 2 -type d -name skill.kb -print0 |
  xargs -0 -r "$ROOT/llm-kb/bin/llm.kb-validate-links" || status=1

exit "$status"
