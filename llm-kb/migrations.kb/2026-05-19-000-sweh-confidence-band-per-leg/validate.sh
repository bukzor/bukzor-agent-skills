#!/bin/bash
# validate.sh: find cost-benefit-sweh legs missing the `confidence:`
# field. Handles both flat (pre-001) and nested-2w (post-001) shapes.
#
# Read-only. Idempotent.
#
# Output format:
#   <path>:<leg-key>

set -uo pipefail

claude-open-tasks-list | grep '^## ' | sed 's/^## //' | \
  while IFS= read -r path; do
    [[ -f "$path" ]] || continue
    md-frontmatter "$path" 2>/dev/null | jq -r --arg p "$path" '
      .["@value"]["cost-benefit-sweh"] as $cbs |
      if $cbs == null then empty
      else (
        # Flat shape: legs as top-level keys of cost-benefit-sweh
        ($cbs | to_entries[] |
          select(.value | type == "object") |
          select(.value | has("@value")) |
          select(.value | has("confidence") | not) |
          "\($p):\(.key)"
        ),
        # Nested shape: under .2w
        (
          ($cbs["2w"] // {}) | to_entries[] |
          select(.value | type == "object") |
          select(.value | has("@value")) |
          select(.value | has("confidence") | not) |
          "\($p):2w.\(.key)"
        )
      )
      end' 2>/dev/null
  done
