#!/bin/bash
# validate.sh: classify every schema file in the homedir whose category
# has a published canonical (see categories.tsv) against that canonical.
#
#   OK        -- already the canonical stub, byte for byte
#   EXTENDER  -- $ref's the canonical's `#base` and closes locally; the
#                prescribed shape for a consumer with local fields
#   ALIAS     -- a one-line $ref at something other than this category's
#                canonical, so not a copy of anything: this migration has
#                nothing to do with it. Chiefly `questions.jsonschema.yaml`
#                inside a *.claims.kb/, where `questions` is a claim-ledger
#                collection, not the discourse-graph category of that name.
#   SNAPSHOT  -- byte-identical to some historical canonical version; safe to stub
#   STALE-REF -- a stub for this category pointing at a superseded path; safe to repoint
#   DIVERGED  -- a full schema matching no historical canonical blob; human
#                judgment, never rewritten
#
# Also checks each canonical is extendable, i.e. publishes two entry
# points: a strict root built from an open `#base`. A consumer that needs
# one extra field can only avoid DIVERGED-forever if `#base` exists.
#
#   CANON-OK      -- canonical publishes `#base`, or is itself a stub
#   CANON-CLOSED  -- canonical has no `#base`; extenders have nowhere to go
#
# Read-only. Idempotent. Exit 0 when every line is a conforming class
# (OK, EXTENDER, ALIAS, CANON-OK).
#
# Subsumes 2026-07-07-000-schema-copies-to-ref-stubs/validate.sh, whose
# scope (todo + ideas, under ~/repo) is two rows of categories.tsv.
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
export HERE
source "$HERE/lib.sh"

# The one homedir-wide `find` engine, so the noise-prune list (trash/,
# node_modules/, venvs, caches) stays in exactly one place; see
# ~/.claude/must-read.kb/when/surveying-the-homedir-for-an-artifact-type.md
ARCHEOLOGY="$HOME/claude/homedir-archeology"

# Every blob the canonical has ever had, including under the paths it was
# renamed from (--follow discovers those, so a future move costs nothing
# here) and its current, possibly uncommitted, content.
canonical_blobs() {
  local canonical="$1" relative
  relative="${canonical#"$SKILLS_REPO"/}"
  git -C "$SKILLS_REPO" hash-object "$canonical"
  ( git -C "$SKILLS_REPO" log --all --follow --format= --name-only -- "$relative" |
      sort -u |
      xargs -d'\n' -rL1 bash -ec '
        git -C "$SKILLS_REPO" rev-list --all -- "$1" |
          xargs -r -I{} git -C "$SKILLS_REPO" rev-parse --verify --quiet "{}:$1"' - ||
    : "the path is absent in some reachable commits: $?" )
}

# Path prefixes to drop: the canonicals themselves (a canonical is not a
# copy of itself), every *other* worktree of the skills repo (editing one
# rewrites another branch's working tree), and the hand-kept list.
excluded_prefixes() {
  categories | xargs -d'\n' -rL1 bash -ec 'canonical_path "$1"' -
  ( git -C "$SKILLS_REPO" worktree list --porcelain |
      sed -n 's/^worktree //p' |
      grep -vxF "$SKILLS_REPO" ||
    : "there need not be another worktree: $?" )
  uncommented "$HERE/excluded-prefixes.txt" | sed -e "s|^~/|$HOME/|"
}

in_scope_files() {
  ( cd "$ARCHEOLOGY" &&
    categories |
      awk 'NR > 1 { print "-or" } { print "-name"; print $1 ".jsonschema.yaml" }' |
      xargs -d'\n' uv run --quiet bukzor-homedir-archeology find ) |
    sed "s|^\./|$HOME/|" |
    sort |
    awk 'NR == FNR { skip[FNR] = $0; n = FNR; next }
      { for (i = 1; i <= n; i++) if (index($0, skip[i]) == 1) next; print }' \
      <(excluded_prefixes) -
}

classify() {
  local file="$1" category canonical ref
  category="$(category_of "$file")"
  canonical="$(canonical_uri "$category")"
  ref="$(pure_stub_ref "$file")"

  if cmp -s <(canonical_stub "$category") "$file"; then
    echo "OK        $file"
  elif [[ "$(document_ref "$file")" == "$canonical#base" ||
    "$(document_ref "$file")" == "$canonical#/\$defs/base" ]]; then
    echo "EXTENDER  $file"
  elif [[ -n "$ref" ]]; then
    if [[ "$(basename "$ref")" == "$category.jsonschema.yaml" ]]; then
      echo "STALE-REF $file"
    else
      echo "ALIAS     $file"
    fi
  elif grep -qxF "$(git hash-object "$file")" "$BLOB_DIR/$category"; then
    echo "SNAPSHOT  $file"
  else
    echo "DIVERGED  $file"
  fi
}

# A canonical is extendable when it publishes the open `#base` anchor
# beside its strict root; see llm-kb/references/schema-reuse.md.
classify_canonical() {
  local canonical="$1"
  if [[ -n "$(pure_stub_ref "$canonical")" ]] ||
    grep -q '^[[:space:]]*\$anchor:[[:space:]]*base[[:space:]]*$' "$canonical"; then
    echo "CANON-OK      $canonical"
  else
    echo "CANON-CLOSED  $canonical"
  fi
}

if (( DEBUG > 0 )); then
  set -x
fi

export BLOB_DIR
BLOB_DIR="$(mktemp -d)"
trap 'rm -r "$BLOB_DIR"' EXIT
export -f canonical_blobs classify classify_canonical

categories |
  xargs -d'\n' -rL1 bash -ec \
    'canonical_blobs "$(canonical_path "$1")" | sort -u > "$BLOB_DIR/$1"' -

report="$(
  { categories | xargs -d'\n' -rL1 bash -ec 'classify_canonical "$(canonical_path "$1")"' -
    in_scope_files | xargs -d'\n' -rL1 bash -ec 'classify "$1"' -
  }
)"
printf '%s\n' "$report"

if grep -qv '^\(OK\|EXTENDER\|ALIAS\|CANON-OK\) ' <<< "$report"; then
  exit 1
fi
