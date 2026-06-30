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
check_dir ".alphaX/process/applied-runs"
check_dir ".alphaX/process/judgment-replays"
check_dir ".alphaX/process/loop-reports"
check_dir ".alphaX/process/pilots"
check_dir ".alphaX/process/review-feedback"
check_dir ".alphaX/process/source-evolution-candidates"
check_dir ".alphaX/process/source-work-candidates"
check_dir ".alphaX/process/thinking-notes"

check_file ".alphaX/manifest.yaml"
check_file ".alphaX/local/README.md"
check_file ".alphaX/process/README.md"

check_pattern "^schema_version: 1$" ".alphaX/manifest.yaml"
check_pattern "^kind: alphaX_local_data$" ".alphaX/manifest.yaml"
check_pattern "directory: \\.alphaX/local" ".alphaX/manifest.yaml"
check_pattern "directory: \\.alphaX/process" ".alphaX/manifest.yaml"
check_pattern "Applied Runs" ".alphaX/process/index.md"
check_pattern "Judgment Replays" ".alphaX/process/index.md"
check_pattern "Source Evolution Candidates" ".alphaX/process/index.md"
check_pattern "Thinking Notes" ".alphaX/process/index.md"

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

while IFS= read -r replay_file; do
  rel="${replay_file#$ROOT/}"
  if rg -n '^[[:space:]]+case_id:' "$replay_file" >/dev/null; then
    rg -n '^[[:space:]]+case_id:' "$replay_file" >&2
    fail "$rel uses legacy replay field case_id; use case_ids"
  fi
  if rg -n '^[[:space:]]+fixture_expected_judgment:' "$replay_file" >/dev/null; then
    rg -n '^[[:space:]]+fixture_expected_judgment:' "$replay_file" >&2
    fail "$rel uses legacy replay field fixture_expected_judgment; use expected_judgment"
  fi
  if rg -n '^judgment_replay_packet:' "$replay_file" >/dev/null; then
    awk -v rel="$rel" '
      BEGIN {
        required_count = split("case_ids source_claim observed_evidence expected_judgment actual_judgment changed_call remaining_unverified_claims", required, " ")
      }
      function reset_seen() {
        for (idx = 1; idx <= required_count; idx++) {
          seen[required[idx]] = 0
        }
      }
      function check_packet() {
        if (!in_packet) return
        for (idx = 1; idx <= required_count; idx++) {
          if (!seen[required[idx]]) {
            printf "%s packet %d missing %s\n", rel, packet, required[idx] > "/dev/stderr"
            exit 1
          }
        }
      }
      /^judgment_replay_packet:/ {
        check_packet()
        in_packet = 1
        packet += 1
        delete seen
        reset_seen()
        next
      }
      in_packet && /^[[:space:]]+[A-Za-z_][A-Za-z0-9_]*:/ {
        field = $0
        sub(/^[[:space:]]+/, "", field)
        sub(/:.*/, "", field)
        if (field in seen) {
          seen[field] = 1
        }
      }
      END {
        check_packet()
      }
    ' "$replay_file" || fail "$rel has incomplete judgment_replay_packet"
  fi
done < <(find "$ROOT/.alphaX/process/judgment-replays" -type f -name '*.md' -print)

printf 'Local alphaX data verification passed: %s\n' "$ROOT/.alphaX"
