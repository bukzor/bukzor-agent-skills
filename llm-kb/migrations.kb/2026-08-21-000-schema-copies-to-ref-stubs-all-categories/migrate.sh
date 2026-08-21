#!/bin/bash
# migrate.sh: rewrite SNAPSHOT and STALE-REF files (per validate.sh's
# classification) to the canonical one-line $ref stub for their category.
# DIVERGED files carry local intent and are left for human judgment;
# CANON-CLOSED is a schema-design defect no script can fix.
#
# Idempotent: OK files never enter the input, and the rewrite is a
# byte-identical no-op for anything already conforming.
#
# Subsumes 2026-07-07-000-schema-copies-to-ref-stubs/migrate.sh, whose
# two hardcoded categories are two rows of categories.tsv.
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
export HERE
source "$HERE/lib.sh"

if (( DEBUG > 0 )); then
  set -x
fi

( "$HERE/validate.sh" "$@" ||
  : "non-OK entries are exactly what migrate is for: $?" ) |
  sed -n 's/^\(SNAPSHOT\|STALE-REF\) *//p' |
  xargs -d'\n' -rL1 bash -ec '
    canonical_stub "$(category_of "$1")" > "$1"
    echo "STUBBED   $1"
  ' - \
;
