#!/bin/bash
# migrate.sh: cp missing schema files from skeleton into each skill's
# .claude/. Does NOT auto-resolve DIFFER cases (those need user
# judgment about direction).
#
# Idempotent: cp of byte-identical content is a no-op modulo mtime.
#
# Usage:
#   ./migrate.sh             # process all MISSING per validate.sh
#   ./migrate.sh PATH ...    # `cp` skeleton schema to each PATH

set -uo pipefail

SKILLS_ROOT="$HOME/repo/github.com/bukzor/bukzor-agent-skills"
SKEL="$SKILLS_ROOT/llm-subtask/skeleton/.claude"

resolve_src() {
  local dst=$1
  local schema; schema=$(basename "$dst")
  printf '%s/%s' "$SKEL" "$schema"
}

migrate_one() {
  local dst=$1
  local src; src=$(resolve_src "$dst")
  if [[ ! -f "$src" ]]; then
    echo "skip (no source): $dst (looked at $src)" >&2
    return 0
  fi
  if [[ -f "$dst" ]] && diff -q "$src" "$dst" >/dev/null 2>&1; then
    echo "skip (identical): $dst" >&2
    return 0
  fi
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
  echo "copied: $src -> $dst" >&2
}

if (( $# > 0 )); then
  for dst in "$@"; do migrate_one "$dst"; done
else
  HERE="$(cd "$(dirname "$0")" && pwd)"
  "$HERE/validate.sh" | awk '$1 == "MISSING" { print $2 }' | \
    while IFS= read -r dst; do
      migrate_one "$dst"
    done
fi
