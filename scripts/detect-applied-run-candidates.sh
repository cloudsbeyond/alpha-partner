#!/usr/bin/env bash
set -euo pipefail

SOURCE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
SCAN_ROOT="$SOURCE_ROOT"
MIN_SCORE=5
SHOW_ALL=0

usage() {
  cat <<'EOF'
Usage: bash scripts/detect-applied-run-candidates.sh [--root PATH] [--min-score N] [--all]

Read-only detector for local alphaX applied-run candidates.

By default it scans the source checkout's ignored process notes. With --root it
also supports target-project .alphaX surfaces such as reviews, reports, and
project-context notes. It prints candidate records when a loop, review, or
source-evolution note appears to contain mechanism learning.
It does not create, modify, or delete applied-run files.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --root)
      [ "$#" -ge 2 ] || { printf 'FAIL: --root requires a path\n' >&2; exit 2; }
      SCAN_ROOT="$(cd "$2" && pwd -P)"
      shift 2
      ;;
    --min-score)
      [ "$#" -ge 2 ] || { printf 'FAIL: --min-score requires a number\n' >&2; exit 2; }
      MIN_SCORE="$2"
      shift 2
      ;;
    --all)
      SHOW_ALL=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'FAIL: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$MIN_SCORE" in
  ''|*[!0-9]*)
    printf 'FAIL: --min-score must be a non-negative integer\n' >&2
    exit 2
    ;;
esac

SOURCE_PROCESS_ROOT="$SOURCE_ROOT/.alphaX/process"
SCAN_ALPHA_ROOT="$SCAN_ROOT/.alphaX"
SCAN_PROCESS_ROOT="$SCAN_ALPHA_ROOT/process"

printf '# Applied Run Candidate Scan\n\n'
printf 'source_root: %s\n' "$SOURCE_ROOT"
printf 'scan_root: %s\n' "$SCAN_ROOT"
printf 'source_process_root: %s\n' "$SOURCE_PROCESS_ROOT"
printf 'scan_process_root: %s\n' "$SCAN_PROCESS_ROOT"
printf 'mode: read-only candidate detection\n'
printf 'min_score: %s\n' "$MIN_SCORE"
printf 'writes: none\n\n'

if [ ! -d "$SCAN_ALPHA_ROOT" ]; then
  printf 'status: no_local_alphaX_data\n'
  printf 'candidate_count: 0\n'
  exit 0
fi

candidate_files="$(
  {
    for dir in loop-reports review-feedback source-evolution-candidates source-work-candidates thinking-notes; do
      [ -d "$SCAN_PROCESS_ROOT/$dir" ] || continue
      find "$SCAN_PROCESS_ROOT/$dir" -type f -name '*.md' -print
    done
    for file in project-context.md evidence.md decisions.md current-implementation-tracker.md iteration-events.md; do
      [ -f "$SCAN_ALPHA_ROOT/$file" ] || continue
      printf '%s\n' "$SCAN_ALPHA_ROOT/$file"
    done
    for dir in reviews review reports; do
      [ -d "$SCAN_ALPHA_ROOT/$dir" ] || continue
      find "$SCAN_ALPHA_ROOT/$dir" -type f -name '*.md' -print
    done
  } | sort -u
)"

if [ -z "$candidate_files" ]; then
  printf 'status: no_candidate_sources\n'
  printf 'candidate_count: 0\n'
  exit 0
fi

contains() {
  local pattern="$1"
  local file="$2"
  rg -i -n "$pattern" "$file" >/dev/null 2>&1
}

join_by_comma() {
  local IFS=", "
  printf '%s' "$*"
}

missing_fields_for() {
  local file="$1"
  local missing=()

  contains 'mechanism_tested|mechanism:|candidate_mechanisms:|convergence_gate|mechanism feedback|alphaX iteration signal|observed mechanism' "$file" || missing+=("mechanism_tested")
  contains 'before:|before_call|likely_call|Before/After Judgment|likely failure mode|before state' "$file" || missing+=("before_call")
  contains 'after:|after_call|revised_call|changed_call|actual_judgment|future .*closeout|gate_action' "$file" || missing+=("after_call")
  contains 'evidence:|observed_evidence|Evidence Read|evidence_read|source:|Reviewed Files|evidence summary|evidence file' "$file" || missing+=("evidence_pointer")
  contains 'changed_future_behavior|safe_next_action|next_action|should distinguish|should be refreshed|future alphaX source evolution' "$file" || missing+=("changed_future_behavior")
  contains 'proof_boundary|completion_boundary|does_not_prove|does_not_decide|not mergeable|not publishable|passing checks|owner review' "$file" || missing+=("proof_boundary")

  if [ "${#missing[@]}" -eq 0 ]; then
    printf '[]'
  else
    printf '['
    join_by_comma "${missing[@]}"
    printf ']'
  fi
}

score_file() {
  local file="$1"
  local score=0
  local signals=()

  if contains 'owner correction|owner_correction|owner rejected|owner feedback|user feedback|accepted_judgment' "$file"; then
    score=$((score + 2))
    signals+=("owner_correction")
  fi
  if contains 'changed_call|Before/After Judgment|before:|after:|revised_call|actual_judgment' "$file"; then
    score=$((score + 1))
    signals+=("before_after_call")
  fi
  if contains 'mechanism gap|source mechanism|source-mechanism|mechanism candidate|mechanism_learning|residual risk|negative signal|gap_if_partial_or_absent' "$file"; then
    score=$((score + 2))
    signals+=("mechanism_gap")
  fi
  if contains 'convergence_gate|stop_at_owner_review|self_stopped|gate_action|stop_reason' "$file"; then
    score=$((score + 2))
    signals+=("self_stop_gate")
  fi
  if contains 'cycle_trailers|gate_counter: 3|executed_rounds:|max_rounds_remaining|recommended_next_action: stop' "$file"; then
    score=$((score + 1))
    signals+=("bounded_replay")
  fi
  if contains 'mechanism feedback|alphaX iteration signal|observed mechanism|Future .*closeout|should distinguish|project-context.md should be refreshed|not mergeable|not publishable|passing checks' "$file"; then
    score=$((score + 2))
    signals+=("mechanism_feedback")
  fi
  if contains 'default output|default scaffold|default .*override|override|wrong-layer|scaffolding|semantic preservation' "$file"; then
    score=$((score + 1))
    signals+=("default_or_boundary_override")
  fi
  if contains 'do_not_do|does_not_prove|proof_boundary|completion_boundary|do not ' "$file"; then
    score=$((score + 1))
    signals+=("proof_or_do_not_do")
  fi
  if contains 'changed_future_behavior|future default|safe_next_action|next_action' "$file"; then
    score=$((score + 1))
    signals+=("future_behavior_change")
  fi
  if contains 'applied run|applied evidence|judgment replay|source-evolution progress' "$file"; then
    score=$((score + 1))
    signals+=("applied_or_replay_language")
  fi

  printf '%s\t%s\n' "$score" "$(join_by_comma "${signals[@]:-}")"
}

candidate_count=0
tmp_output="$(mktemp)"
trap 'rm -f "$tmp_output"' EXIT

while IFS= read -r file; do
  [ -n "$file" ] || continue
  score_and_signals="$(score_file "$file")"
  score="${score_and_signals%%	*}"
  signals="${score_and_signals#*	}"

  if [ "$SHOW_ALL" -eq 0 ] && [ "$score" -lt "$MIN_SCORE" ]; then
    continue
  fi

  rel="$file"
  case "$file" in
    "$SCAN_ROOT"/*) rel="${file#$SCAN_ROOT/}" ;;
  esac

  applied_ref="absent"
  if [ -d "$SOURCE_PROCESS_ROOT/applied-runs" ]; then
    match="$(rg -l -F "$rel" "$SOURCE_PROCESS_ROOT/applied-runs" 2>/dev/null | head -n 1 || true)"
    if [ -z "$match" ]; then
      case "$(basename "$file")" in
        project-context.md|evidence.md|decisions.md|current-implementation-tracker.md|iteration-events.md)
          match=""
          ;;
        *)
          match="$(rg -l -F "$(basename "$file")" "$SOURCE_PROCESS_ROOT/applied-runs" 2>/dev/null | head -n 1 || true)"
          ;;
      esac
    fi
    if [ -n "$match" ]; then
      applied_ref="${match#$SOURCE_ROOT/}"
    fi
  fi

  candidate_count=$((candidate_count + 1))
  {
    printf '## Candidate %d\n\n' "$candidate_count"
    printf 'file: %s\n' "$rel"
    printf 'score: %s\n' "$score"
    printf 'signals: [%s]\n' "$signals"
    printf 'existing_applied_run_ref: %s\n' "$applied_ref"
    printf 'missing_fields: %s\n' "$(missing_fields_for "$file")"
    printf 'action: review before writing; create applied-run only if this changed a reusable mechanism judgment\n\n'
  } >>"$tmp_output"
done <<<"$candidate_files"

if [ "$candidate_count" -eq 0 ]; then
  printf 'status: no_candidates\n'
  printf 'candidate_count: 0\n'
  exit 0
fi

printf 'status: candidates_found\n'
printf 'candidate_count: %d\n\n' "$candidate_count"
cat "$tmp_output"
