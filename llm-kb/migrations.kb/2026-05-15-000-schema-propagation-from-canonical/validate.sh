#!/bin/bash
# validate.sh: every project that authors .claude/{todo,ideas}.kb/ must
# carry the canonical $ref in the adjacent <category>.jsonschema.yaml.
# Extension on top of the $ref is allowed; omission is drift.
#
#   MISSING <path> -- authors the category but has no schema file
#   NO-REF  <path> -- schema file exists but doesn't $ref the canonical
#
# Read-only. Idempotent. Exit 0 when clean.
set -euo pipefail
shopt -s failglob
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

ROOTS=("${@:-$HOME/repo}")

if (( DEBUG > 0 )); then
  set -x
fi

report="$(
  find "${ROOTS[@]}" \
    \( -name .git -o -name node_modules -o -name trash \) -prune -o \
    -type d \( -path '*/.claude/todo.kb' -o -path '*/.claude/ideas.kb' \) -print |
    sort |
    xargs -d'\n' -rL1 bash -ec '
      category="$(basename "$1" .kb)"
      schema="$(dirname "$1")/$category.jsonschema.yaml"
      if [[ ! -f "$schema" ]]; then
        echo "MISSING $schema"
      elif ! grep -qF "skill://llm-subtask/jsonschema/$category.jsonschema.yaml" "$schema"; then
        echo "NO-REF  $schema"
      fi
    ' -
)"
if [[ -n "$report" ]]; then
  printf '%s\n' "$report"
  exit 1
fi
