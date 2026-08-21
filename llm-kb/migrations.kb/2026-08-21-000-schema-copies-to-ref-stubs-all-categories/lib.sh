# shellcheck shell=bash
# lib.sh: the category table (categories.tsv) read as data, plus the two
# shapes derived from it -- the canonical file and the stub that points at
# it. Sourced by validate.sh and migrate.sh so neither names a category.
#
# Callers must set HERE to this directory before sourcing.

export SKILLS_REPO="$HOME/repo/github.com/bukzor/bukzor-agent-skills"
# A plain stub uses only `$ref`, which means the same thing in every
# dialect, so it declares the better-tooled draft-07 meta-schema; see
# llm-kb/references/schema-reuse.md.
export MODELINE='# yaml-language-server: $schema=https://json-schema.org/draft-07/schema'

uncommented() {
  sed -e 's/[[:space:]]*#.*//' -e '/^[[:space:]]*$/d' "$1"
}

table() {
  uncommented "$HERE/categories.tsv"
}

categories() {
  table | cut -f1
}

skill_of() {
  table | awk -v category="$1" '$1 == category { print $2; found = 1 }
    END { if (!found) exit 1 }'
}

canonical_path() {
  echo "$SKILLS_REPO/$(skill_of "$1")/jsonschema/$1.jsonschema.yaml"
}

canonical_uri() {
  echo "skill://$(skill_of "$1")/jsonschema/$1.jsonschema.yaml"
}

canonical_stub() {
  printf '%s\n$ref: "%s"\n' "$MODELINE" "$(canonical_uri "$1")"
}

category_of() {
  basename "$1" .jsonschema.yaml
}

# The $ref target of a file that is *only* a $ref (comments and blank
# lines aside) -- the shape a stub has. Empty for anything richer: an
# extender ($ref plus local properties) is not a stub and must not be
# repointed as if it were.
pure_stub_ref() {
  local body
  body="$(sed -e '/^[[:space:]]*#/d' -e '/^[[:space:]]*$/d' "$1")"
  if [[ "$body" =~ ^\$ref:[[:space:]]*\"?([^\"]+)\"?$ ]]; then
    printf '%s\n' "${BASH_REMATCH[1]}"
  fi
}

# The document-root $ref of any schema file, stub or not -- an extender
# has one too, alongside its local properties.
document_ref() {
  sed -n 's/^\$ref:[[:space:]]*"\?\([^"]*\)"\?[[:space:]]*$/\1/p' "$1"
}

export -f uncommented table categories skill_of canonical_path \
  canonical_uri canonical_stub category_of pure_stub_ref document_ref
