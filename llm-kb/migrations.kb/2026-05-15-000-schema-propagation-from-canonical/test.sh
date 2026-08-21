#!/bin/bash
# test.sh: classify_schema's six cases. Two of them are the reason this
# guard was rewritten -- `mentions-only` (prose naming the canonical,
# which the old grep passed) and `ruled` (a settled divergence, which the
# old grep flagged forever). The old mechanism is wrong on three of six.
set -uo pipefail
HERE="$(dirname "$(readlink -f "$0")")"
# shellcheck source=lib.sh
source "$HERE/lib.sh"

CANONICAL='skill://llm-subtask/jsonschema/todo.jsonschema.yaml'
fail=0

check() { # name expected
  local got
  got="$(classify_schema "$HERE/test-fixtures/$1.jsonschema.yaml" "$CANONICAL")"
  if [[ "$got" == "$2" ]]; then
    printf 'ok       %-16s %s\n' "$1" "$got"
  else
    printf 'MISMATCH %-16s got=%s want=%s\n' "$1" "$got" "$2"
    fail=1
  fi
}

check stub          OK        # the house two-line stub
check extender      OK        # $ref <canonical>#base from inside an allOf
check ruled         RULED     # $comment opens with RULING_TOKEN
check mentions-only NO-REF    # names the canonical in prose only
check lead-in       NO-REF    # token present but not at position 0
check bad           BAD-YAML  # unparseable, must not read as NO-REF

exit "$fail"
