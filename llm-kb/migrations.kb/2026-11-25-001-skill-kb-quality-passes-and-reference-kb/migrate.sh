#!/bin/bash
# migrate.sh: apply migration 2026-11-25-001 -- move quality passes and
# reference docs into each skill's `skill.kb/`, then rewrite live readers of
# the old paths. Idempotent: a move whose source is gone is skipped, and a
# rewritten reader no longer matches. Stages nothing; the caller commits.
set -euo pipefail
shopt -s failglob
export DEBUG="${DEBUG:-0}"

onerror() {
  error="$?"
  echo >&2 "ERROR($error)"
  exit "$error"
}
trap onerror ERR

HERE="$(dirname "$(readlink -f "$0")")"
ROOT="$(readlink -f "$HERE/../../..")"

# move SRC DST -- relative to ROOT; no-op once SRC is gone
move() {
  if [[ -e "$ROOT/$1" && ! -e "$ROOT/$2" ]]; then
    mkdir -p "$(dirname "$ROOT/$2")"
    git -C "$ROOT" mv -- "$1" "$2"
  fi
}

if (( DEBUG > 0 )); then
  set -x
fi

move llm-kb/skill.kb/self-audit.kb llm-kb/skill.kb/quality-passes.kb
move llm-kb/skill.kb/self-audit.md llm-kb/skill.kb/quality-passes.md
move llm-kb/skill.kb/procedures.kb/run-self-audits.md \
  llm-kb/skill.kb/procedures.kb/run-quality-passes.md
move llm-claims-kb/skill.kb/self-audit.kb llm-claims-kb/skill.kb/quality-passes.kb
move llm-design-kb/skill.kb/principles.kb llm-design-kb/skill.kb/quality-passes.kb

for skill in llm-kb llm-subtask llm-must-read-kb; do
  mapfile -t files < <(git -C "$ROOT" ls-files -- "$skill/references")
  for file in "${files[@]}"; do
    move "$file" "$skill/skill.kb/reference.kb/${file##*/}"
  done
done

move align/skill.kb/sort-goals-into-four-bins.md \
  align/skill.kb/reference.kb/sort-goals-into-four-bins.md
move llm-claims/skill.kb/theories.md llm-claims/skill.kb/reference.kb/theories.md
move persist-clarity/skill.kb/persistence.md \
  persist-clarity/skill.kb/reference.kb/persistence.md

"$HERE/old_paths.py" rewrite
