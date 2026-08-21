#!/bin/bash
# migrate.sh: rewrite unambiguous slug `why:` items to file-relative paths.
# Idempotent -- a rewritten item ends in `.md` and is never a slug again.
# See why_paths.py.
set -euo pipefail
exec "$(dirname "$(readlink -f "$0")")/why_paths.py" migrate "$@"
