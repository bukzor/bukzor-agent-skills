#!/bin/bash
# migrate.sh: rename OR-class .kb/ to .oneOf.kb/ and update inbound links.
#
# Idempotent. Each path argument is processed independently; failures on
# one path do not abort the rest.
#
# Usage:
#   ./migrate.sh PATH [PATH ...]
#
# Each PATH should be a .kb/ directory (absolute or relative). The script
# skips:
#   - paths already named *.oneOf.kb (already migrated)
#   - paths that don't exist but whose .oneOf.kb sibling does (already migrated)
#   - paths that don't exist and whose .oneOf.kb sibling also doesn't (missing)

set -uo pipefail

if [[ $# -eq 0 ]]; then
  echo "usage: $0 PATH [PATH ...]" >&2
  exit 2
fi

migrate_one() {
  local src=$1
  src="${src%/}"

  case "$src" in
    *.oneOf.kb)
      echo "skip (already-oneOf): $src" >&2
      return 0
      ;;
  esac

  local dst="${src%.kb}.oneOf.kb"

  if [[ ! -d "$src" ]]; then
    if [[ -d "$dst" ]]; then
      echo "skip (done): $src -> $dst" >&2
    else
      echo "skip (missing): $src" >&2
    fi
    return 0
  fi

  # Find owning repo for git mv + scoped link search.
  local repo=""
  repo=$(git -C "$src" rev-parse --show-toplevel 2>/dev/null || true)

  if [[ -n "$repo" ]]; then
    (cd "$repo" && git mv "$src" "$dst")
  else
    mv "$src" "$dst"
    repo=$(dirname "$src")
  fi

  # Update inbound references within the owning repo (or fallback parent).
  local old_base new_base
  old_base=$(basename "$src")
  new_base=$(basename "$dst")

  local n=0
  while IFS= read -r ref; do
    sed -i "s|${old_base}|${new_base}|g" "$ref"
    echo "  updated link in: $ref" >&2
    n=$((n + 1))
  done < <(grep -rlF --include='*.md' "$old_base" "$repo" 2>/dev/null || true)

  echo "migrated: $src -> $dst  (updated $n inbound link file(s))" >&2
}

for src in "$@"; do
  migrate_one "$src"
done
