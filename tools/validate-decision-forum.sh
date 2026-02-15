#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

json_ok() {
  python3 -m json.tool "$1" >/dev/null
}

# Basic JSON validity
for f in "$ROOT_DIR"/schemas/*.json; do
  json_ok "$f"
done

for f in "$ROOT_DIR"/projects/decision.forum/examples/*.json; do
  json_ok "$f"
done

echo "OK: JSON files parse"

# Note: full JSON Schema validation would require an additional dependency.
# We keep this MVP validator dependency-free.
