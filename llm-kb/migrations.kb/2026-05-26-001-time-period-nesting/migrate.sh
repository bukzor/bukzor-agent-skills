#!/bin/bash
# migrate.sh: restructure cost-benefit-sweh frontmatter from flat
# (benefit-2w / cost-of-delay-2w / timebox) to nested under `2w:`.
#
# Idempotent: files already in nested shape are no-op'd.
#
# Usage:
#   ./migrate.sh             # process all paths from claude-open-tasks-list
#   ./migrate.sh PATH ...    # process specific paths

set -uo pipefail

JQ_FILTER='
  if (.["@value"]["cost-benefit-sweh"] == null) then .
  elif (.["@value"]["cost-benefit-sweh"] | has("2w")) then .
  else
    .["@value"]["cost-benefit-sweh"] |= (
      {
        "2w": (
          {
            timebox: .timebox,
            benefit: .["benefit-2w"],
            "cost-of-delay": .["cost-of-delay-2w"]
          } | with_entries(select(.value != null))
        )
      }
    )
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
