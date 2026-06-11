#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

check_file() {
  local path="$1"
  [ -f "$ROOT/$path" ] || fail "missing file: $path"
}

check_dir() {
  local path="$1"
  [ -d "$ROOT/$path" ] || fail "missing directory: $path"
}

check_pattern() {
  local pattern="$1"
  local path="$2"
  rg -n "$pattern" "$ROOT/$path" >/dev/null || fail "missing pattern in $path: $pattern"
}

check_dir ".alphaX"
check_dir ".alphaX/local"
check_dir ".alphaX/process"
check_dir ".alphaX/process/loop-reports"
check_dir ".alphaX/process/pilots"

check_file ".alphaX/manifest.yaml"
check_file ".alphaX/local/README.md"
check_file ".alphaX/process/README.md"

check_pattern "^schema_version: 1$" ".alphaX/manifest.yaml"
check_pattern "^kind: alphaX_local_data$" ".alphaX/manifest.yaml"
check_pattern "directory: \\.alphaX/local" ".alphaX/manifest.yaml"
check_pattern "directory: \\.alphaX/process" ".alphaX/manifest.yaml"

if ! git -C "$ROOT" check-ignore -q ".alphaX/manifest.yaml"; then
  fail ".alphaX/ is not ignored by git"
fi

if git -C "$ROOT" ls-files '.alphaX/*' | rg . >/dev/null; then
  git -C "$ROOT" ls-files '.alphaX/*' >&2
  fail ".alphaX local data is tracked by git"
fi

if rg -n "BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY" "$ROOT/.alphaX" >/dev/null; then
  rg -n "BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY" "$ROOT/.alphaX" >&2
  fail ".alphaX contains a forbidden secret marker"
fi

printf 'Local alphaX data verification passed: %s\n' "$ROOT/.alphaX"
