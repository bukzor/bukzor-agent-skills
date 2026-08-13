#!/bin/bash
# migrate.sh: rewrite SNAPSHOT and STALE-REF files (per validate.sh's
# classification) to the canonical one-line $ref stub. DIVERGED files
# carry local intent and are left for human judgment.
#
# Idempotent: OK files are untouched; rewriting a rewritten file is a
# byte-identical no-op.
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
  : "non-OK entries are exactly what migrate is for: $?" ) |
  sed -n 's/^\(SNAPSHOT\|STALE-REF\) *//p' |
  xargs -d'\n' -rL1 bash -c '
    category="$(basename "$1" .jsonschema.yaml)"
    printf "%s\n%s\n" "$MODELINE" \
      "\$ref: \"skill://llm-subtask/jsonschema/$category.jsonschema.yaml\"" > "$1"
    echo "STUBBED   $1"
  ' - \
;
