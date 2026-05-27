#!/bin/bash
# migrate.sh: rename cost-benefit-sweh.2w.timebox → .effort.
# Does not auto-populate `wallclock`; that's a per-item judgment.
#
# Idempotent: files whose 2w.effort already exists are no-op'd.
# Also no-op on files still in flat shape (migration 001 must run first).
#
# Usage:
#   ./migrate.sh             # process all paths from claude-open-tasks-list
#   ./migrate.sh PATH ...    # process specific paths

set -uo pipefail

JQ_FILTER='
  if (.["@value"]["cost-benefit-sweh"]["2w"] == null) then .
  elif (.["@value"]["cost-benefit-sweh"]["2w"] | has("effort")) then .
  elif (.["@value"]["cost-benefit-sweh"]["2w"] | has("timebox")) then
    .["@value"]["cost-benefit-sweh"]["2w"] |= (
      .effort = .timebox | del(.timebox)
    )
  else .
  end
'

paths_from_stdin() {
  if (( $# > 0 )); then
    printf '%s\n' "$@"
  else
    claude-open-tasks-list | grep '^## ' | sed 's/^## //'
  fi
}

paths_from_stdin "$@" | while IFS= read -r path; do
  [[ -f "$path" ]] || { echo "skip (missing): $path" >&2; continue; }
  md-frontmatter "$path" 2>/dev/null | jq -c "$JQ_FILTER" | md-frontmatter-set 2>&1 \
    | sed "s|^|$path: |" >&2
done
