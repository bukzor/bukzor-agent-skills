#!/bin/bash
# validate.sh: every project that authors <category>.kb/ for a category
# with a published canonical must carry the canonical $ref in the
# adjacent <category>.jsonschema.yaml. Extension on top of the $ref is
# allowed; omission is drift.
#
#   MISSING <path> -- authors the category but has no schema file
#   NO-REF  <path> -- schema file exists but doesn't $ref the canonical
#
# "Adjacent" is strict: llm.kb-validate resolves a schema only as a
# sibling of the .kb/ it governs, with no inheritance from an ancestor
# scope (schema_for() in frontmatter_validate.py). A nested sub-scope
# therefore needs its own schema file, which is why this walks every
# *.kb/ and not just the top of each graph.
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

HERE="$(dirname "$(readlink -f "$0")")"
# shellcheck source=lib.sh
source "$HERE/lib.sh"

ROOTS=("$@")
(( ${#ROOTS[@]} )) || ROOTS=("$HOME/repo" "$HOME/claude" "$HOME/.claude")

if (( DEBUG > 0 )); then
  set -x
fi

report="$(
  collections "${ROOTS[@]}" |
    sort |
    xargs -d'\n' -rL1 bash -ec '
      category="$(basename "$1" .kb)"
      skill="$(skill_of "$category" 2>/dev/null)" || exit 0
      schema="$(dirname "$1")/$category.jsonschema.yaml"
      if [[ ! -f "$schema" ]]; then
        echo "MISSING $schema"
      elif ! grep -qF "skill://$skill/jsonschema/$category.jsonschema.yaml" "$schema"; then
        echo "NO-REF  $schema"
      fi
    ' -
)"
if [[ -n "$report" ]]; then
  printf '%s\n' "$report"
  exit 1
fi
