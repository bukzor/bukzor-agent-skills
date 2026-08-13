#!/bin/bash
# validate.sh: report files whose cost-benefit-sweh frontmatter is
# still in the flat (benefit-2w / cost-of-delay-2w / timebox at top level)
# shape and has not yet been nested under `2w:`.
#
# Read-only. Idempotent.

set -uo pipefail

claude-open-tasks-list | grep '^## ' | sed 's/^## //' | \
  while IFS= read -r path; do
    [[ -f "$path" ]] || continue
    shape=$(md-frontmatter "$path" 2>/dev/null | \
      jq -r '
        .["@value"]["cost-benefit-sweh"] as $cbs |
        if $cbs == null then "no-rating"
        elif ($cbs | has("2w")) then "nested"
        elif ($cbs | (has("benefit-2w") or has("cost-of-delay-2w") or has("timebox"))) then "flat"
        else "other"
        end' 2>/dev/null)
    case "$shape" in
      flat) echo "flat-shape: $path" ;;
    esac
  done
