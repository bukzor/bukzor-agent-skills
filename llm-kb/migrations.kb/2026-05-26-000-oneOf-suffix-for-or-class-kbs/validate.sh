#!/bin/bash
# validate.sh: scan .kb/ directories that look like OR-class
# (alternatives, one to be picked) but aren't yet named with .oneOf.
#
# Read-only. Idempotent. Output is one line per candidate:
#   <signal-sum>\t<path>\t<reason1,reason2,...>
# Sorted by signal sum descending.
#
# Usage:
#   ./validate.sh [ROOT ...]   # default: ~/repo ~/.claude

set -euo pipefail

if [[ $# -eq 0 ]]; then
  set -- "$HOME/repo" "$HOME/.claude"
fi

# Basenames that are always AND by convention; skip from OR candidacy.
is_skip_basename() {
  case "$1" in
    decision.kb|principle.kb|reference.kb|observation.kb|verified-claim.kb) return 0;;
    todo.kb|sessions.kb|ideas.kb|migrations.kb|todo.d) return 0;;
    *.oneOf.kb) return 0;;
  esac
  return 1
}

scan_one() {
  local kb=$1
  local base
  base=$(basename "$kb")
  is_skip_basename "$base" && return 0

  local signals=0
  local reasons=()

  # Signal 1 (+3): the kb's own CLAUDE.md uses chosen/alternative vocabulary
  if [[ -f "$kb/CLAUDE.md" ]] \
     && grep -qiE 'currently chosen|which (one|pattern|mechanism)|chosen.*see|considered and rejected' "$kb/CLAUDE.md"; then
    signals=$((signals + 3))
    reasons+=(kb-claude-chooses)
  fi

  # Signal 2 (+3): the parent same-stem .md has Answer./Why this one/Resolution
  local parent stem summary
  parent=$(dirname "$kb")
  stem=$(basename "$kb" .kb)
  summary="$parent/$stem.md"
  if [[ -f "$summary" ]] \
     && grep -qE '\*\*Answer\.\*\*|^## Why this one|^## Resolution|^## Decision|^## Outcome' "$summary"; then
    signals=$((signals + 3))
    reasons+=(parent-answers)
  fi

  # Signal 3 (+2): entries have status frontmatter chosen/rejected/selected/considered
  if grep -rqE '^status:\s*(chosen|rejected|selected|considered)$' "$kb" 2>/dev/null; then
    signals=$((signals + 2))
    reasons+=(entry-status-chosen-rejected)
  fi

  # Signal 4 (+1): small entry count (2-6) — alternative sets tend to be small
  local count
  count=$(find "$kb" -maxdepth 1 -name '*.md' -not -name 'CLAUDE.md' 2>/dev/null | wc -l)
  if (( count >= 2 && count <= 6 )); then
    signals=$((signals + 1))
    reasons+=("entry-count=$count")
  fi

  if (( signals >= 3 )); then
    local joined
    joined=$(IFS=,; echo "${reasons[*]}")
    printf '%d\t%s\t%s\n' "$signals" "$kb" "$joined"
  fi
}

while IFS= read -r -d '' kb; do
  scan_one "$kb" || true
done < <(find "$@" -type d -name '*.kb' -print0 2>/dev/null) | sort -rn
