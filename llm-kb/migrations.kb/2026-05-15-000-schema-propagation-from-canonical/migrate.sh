#!/bin/bash
# migrate.sh: write the canonical $ref stub for each MISSING schema file
# (per validate.sh). NO-REF files are NOT auto-resolved: a full copy is
# the 2026-07-07 conversion migration's job; anything else is genuine
# divergence for the user to judge.
#
# Idempotent: only creates files that don't exist.
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
export MODELINE='# yaml-language-server: $schema=https://json-schema.org/draft-07/schema'

if (( DEBUG > 0 )); then
  set -x
fi

( "$HERE/validate.sh" "$@" ||
  : "non-clean report is exactly what migrate is for: $?" ) |
  sed -n 's/^MISSING *//p' |
  xargs -d'\n' -rL1 bash -ec '
    category="$(basename "$1" .jsonschema.yaml)"
    printf "%s\n%s\n" "$MODELINE" \
      "\$ref: \"skill://llm-subtask/jsonschema/$category.jsonschema.yaml\"" > "$1"
    echo "STUBBED $1"
  ' - \
;
