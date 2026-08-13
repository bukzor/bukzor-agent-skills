#!/bin/bash
# validate.sh: classify every .claude/{todo,ideas}.jsonschema.yaml under
# the search roots against the canonical schemas at
# llm-subtask/jsonschema/.
#
#   OK        -- already the canonical stub
#   SNAPSHOT  -- byte-identical to a historical canonical version; safe to stub
#   STALE-REF -- stub pointing at the pre-move skeleton path; safe to repoint
#   DIVERGED  -- matches no historical canonical blob; human judgment
#
# Read-only. Idempotent. Exit 0 when nothing but OK found.
set -euo pipefail
shopt -s failglob
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

SKILLS_REPO="$HOME/repo/github.com/bukzor/bukzor-agent-skills"
ROOTS=("${@:-$HOME/repo}")
MODELINE='# yaml-language-server: $schema=https://json-schema.org/draft-07/schema'

# Every blob hash the canonical schemas (and their pre-move skeleton
# paths) have ever had. A file matching one is an unmodified snapshot.
historical_hashes() {
  local path="$1"
  git -C "$SKILLS_REPO" rev-list --all -- "$path" |
    xargs -r -I{} git -C "$SKILLS_REPO" rev-parse --verify --quiet "{}:$path" ||
    : "path absent in some commits: $?"
}

canonical_blobs() {
  for category in todo ideas; do
    historical_hashes "llm-subtask/jsonschema/$category.jsonschema.yaml"
    historical_hashes "llm-subtask/skeleton/.claude/$category.jsonschema.yaml"
  done
}

classify() {
  local file="$1"
  local category stub
  category="$(basename "$file" .jsonschema.yaml)"
  stub="$MODELINE
\$ref: \"skill://llm-subtask/jsonschema/$category.jsonschema.yaml\""

  if [[ "$(cat "$file")" == "$stub" ]]; then
    echo "OK        $file"
  elif grep -q 'skill://llm-subtask/skeleton/.claude/' "$file"; then
    echo "STALE-REF $file"
  elif grep -qxF "$(git hash-object "$file")" <<< "$BLOBS"; then
    echo "SNAPSHOT  $file"
  else
    echo "DIVERGED  $file"
  fi
}

if (( DEBUG > 0 )); then
  set -x
fi

BLOBS="$(canonical_blobs | sort -u)"
export BLOBS MODELINE
export -f classify

report="$(
  find "${ROOTS[@]}" \
    \( -name .git -o -name node_modules -o -name trash \) -prune -o \
    -path '*/.claude/todo.jsonschema.yaml' -print -o \
    -path '*/.claude/ideas.jsonschema.yaml' -print |
    sort |
    xargs -d'\n' -rL1 bash -c 'classify "$1"' -
)"
if [[ -n "$report" ]]; then
  printf '%s\n' "$report"
fi
if grep -v '^OK ' <<< "$report" >/dev/null; then
  exit 1
fi
