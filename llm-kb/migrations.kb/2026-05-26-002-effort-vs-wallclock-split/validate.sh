#!/bin/bash
# validate.sh: report files whose cost-benefit-sweh.2w still uses
# `timebox` rather than the post-migration `effort`.
#
# Read-only. Idempotent. Assumes migration 001 has already run on
# the file (i.e., the nested `2w:` shape exists). If a file is still
# in flat shape, this script ignores it — 001 must come first.

set -uo pipefail

claude-open-tasks-list | grep '^## ' | sed 's/^## //' | \
  while IFS= read -r path; do
    [[ -f "$path" ]] || continue
    shape=$(md-frontmatter "$path" 2>/dev/null | \
      jq -r '
        .["@value"]["cost-benefit-sweh"]["2w"] as $w |
        if $w == null then "not-nested"
        elif ($w | has("effort")) then "renamed"
        elif ($w | has("timebox")) then "still-timebox"
        else "no-timebox"
        end' 2>/dev/null)
    case "$shape" in
      still-timebox) echo "still-timebox: $path" ;;
      not-nested)    echo "needs-001-first: $path" ;;
    esac
  done
