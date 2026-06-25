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

check_pattern() {
  local pattern="$1"
  local path="$2"
  rg -n "$pattern" "$ROOT/$path" >/dev/null || fail "missing pattern in $path: $pattern"
}

check_absent_public() {
  local pattern="$1"
  if rg -n "$pattern" "$ROOT" \
    -g '*.md' -g '*.yaml' -g '*.sh' \
    --glob '!.git/**' \
    --glob '!.alphaX/**' \
    --glob '!scripts/verify-alpha-source.sh' >/dev/null; then
    rg -n "$pattern" "$ROOT" \
      -g '*.md' -g '*.yaml' -g '*.sh' \
      --glob '!.git/**' \
      --glob '!.alphaX/**' \
      --glob '!scripts/verify-alpha-source.sh' >&2
    fail "public source contains forbidden pattern: $pattern"
  fi
}

required_files=(
  ".gitignore"
  "LICENSE"
  "README.md"
  "AGENTS.md"
  "alphaX/persona.md"
  "alphaX/operating-system.md"
  "alphaX/loop-registry.md"
  "alphaX/session-runbook.md"
  "alphaX/activation-guide.md"
  "alphaX/pilot-playbook.md"
  "alphaX/source-work/README.md"
  "alphaX/source-review/README.md"
  "alphaX/source-review/bootstrap.md"
  "alphaX/project-work/README.md"
  "alphaX/project-work/context-reloader.md"
  "alphaX/project-review/README.md"
  "assets/icon.png"
  "docs/asset-boundary.yaml"
  "docs/README.zh-CN.md"
  "docs/local-alphaX-schema.md"
  "docs/checkpoint-memory-evaluation-prd.md"
  "docs/research-backlog.md"
  "docs/evidence-index.md"
  "templates/research-loop-packet.md"
  "templates/project-work/loop-packet.md"
  "templates/thinking-loop-packet.md"
  "templates/memory-candidate-packet.md"
  "templates/checkpoint-memory-evaluation.md"
  "templates/reentry-risk-packet.md"
  "templates/loop-report.md"
  "templates/project-review/report.md"
  "templates/project-review/lifecycle-hygiene.md"
  "templates/source-review/feedback-report.md"
  "templates/project-work/local-pointer.md"
  "skills/problem-decomposer/SKILL.md"
  "scripts/init-local-alphaX.sh"
  "scripts/verify-local-alphaX.sh"
  "scripts/verify-alpha-source.sh"
  "scripts/context-snapshot.sh"
  "scripts/alphaX-memory-family-rpc.mjs"
)

for file in "${required_files[@]}"; do
  check_file "$file"
done

check_pattern "^\\.alphaX/$" ".gitignore"
check_pattern "^\\.agents/$" ".gitignore"
check_pattern "MIT License" "LICENSE"
check_pattern "Alpha Partner Source" "AGENTS.md"
check_pattern "Source contract" "AGENTS.md"
contract_line="$(rg -n '^Source contract: \*\*initial\*\*\.$' "$ROOT/AGENTS.md" || true)"
[ -n "$contract_line" ] || fail "AGENTS.md must contain one initial source contract line"
[ "$(printf '%s\n' "$contract_line" | wc -l | tr -d ' ')" = "1" ] || fail "AGENTS.md must contain exactly one initial source contract line"
check_pattern "personified collaboration function" "AGENTS.md"
check_pattern "Local Data Map" "AGENTS.md"
check_pattern "Scopes And Scope Guard" "AGENTS.md"
check_pattern "source work" "AGENTS.md"
check_pattern "source review" "AGENTS.md"
check_pattern "project work" "AGENTS.md"
check_pattern "project review" "AGENTS.md"
check_pattern "Interaction Language" "AGENTS.md"
check_pattern "GitHub" "AGENTS.md"
check_pattern "open-source function source only" "README.md"
check_pattern "LICENSE" "README.md"
check_pattern "docs/README.zh-CN.md" "README.md"
check_pattern "shareable_function_assets" "docs/asset-boundary.yaml"
check_pattern "project_review_artifacts" "docs/asset-boundary.yaml"
check_pattern "alpha_partner_feedback_exception" "docs/asset-boundary.yaml"
check_pattern "open_source_repository_rule" "docs/asset-boundary.yaml"
check_pattern "tracked_tree_must_not_contain" "docs/asset-boundary.yaml"
check_pattern "Required Shape" "docs/local-alphaX-schema.md"
check_pattern "manifest.yaml" "docs/local-alphaX-schema.md"
check_pattern "scripts/init-local-alphaX.sh" "README.md"
check_pattern "scripts/verify-local-alphaX.sh" "README.md"
check_pattern "assets/" "docs/README.zh-CN.md"
check_pattern "Claude Tag" "docs/evidence-index.md"
check_pattern "Claude Tag" "docs/research-backlog.md"
check_pattern "project-local objective data" "templates/project-work/local-pointer.md"
check_pattern "Focus And Risk Loop" "alphaX/operating-system.md"
check_pattern "source review" "alphaX/session-runbook.md"
check_pattern "Loop Registry" "alphaX/loop-registry.md"
check_pattern "Agent-Native Activation" "alphaX/activation-guide.md"
check_pattern "Pilot Playbook" "alphaX/pilot-playbook.md"
check_pattern "Source Work" "alphaX/source-work/README.md"
check_pattern "Source Review" "alphaX/source-review/README.md"
check_pattern "Source Anchors" "alphaX/source-review/README.md"
check_pattern "Source Review Bootstrap" "alphaX/source-review/bootstrap.md"
check_pattern "Project Work" "alphaX/project-work/README.md"
check_pattern "Context Reloader" "alphaX/project-work/context-reloader.md"
check_pattern "function/SOP" "alphaX/project-work/context-reloader.md"
check_pattern "Project Review" "alphaX/project-review/README.md"
check_pattern "assets/" "README.md"
check_pattern "assets/icon.png" "AGENTS.md"
check_pattern "assets/icon.png" "docs/asset-boundary.yaml"
check_pattern "Trigger Contract" "alphaX/project-review/README.md"
check_pattern "Asset And Data Boundary" "alphaX/project-review/README.md"
check_pattern "Project Review Report" "templates/project-review/report.md"
check_pattern "Project Lifecycle Hygiene" "templates/project-review/lifecycle-hygiene.md"
check_pattern "Review Feedback Report" "templates/source-review/feedback-report.md"
check_pattern "Lifecycle Hygiene Checks" "alphaX/project-review/README.md"
check_pattern "Project Compaction Pattern" "docs/local-alphaX-schema.md"
check_pattern "Lack of use is a weak negative signal" "alphaX/operating-system.md"
check_pattern "Checkpoint Memory Evaluation" "AGENTS.md"
check_pattern "Checkpoint Memory Evaluation PRD" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "DynamicMem Reference And Borrowed Ideas" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "Rubric" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "Call rubric" "templates/checkpoint-memory-evaluation.md"
check_pattern "agent-runtime-services" "AGENTS.md"
check_pattern "agent-runtime-services" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "alphaX-memory-family-rpc.mjs" "AGENTS.md"
check_pattern "alphaX-memory-family-rpc.mjs" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "ALPHAX_MEMORY_CONFIG" "scripts/alphaX-memory-family-rpc.mjs"
check_pattern "agentRuntimeServices" "docs/checkpoint-memory-evaluation-prd.md"
check_pattern "memory.context.retrieve" "templates/checkpoint-memory-evaluation.md"
check_pattern "memory.context.retrieve" "scripts/alphaX-memory-family-rpc.mjs"
check_pattern "owner-accepted.*source work" "AGENTS.md"
check_pattern "review-feedback" "alphaX/session-runbook.md"
check_pattern "source-work-candidates" "scripts/init-local-alphaX.sh"
check_pattern "agent-runtime-services.json" "scripts/init-local-alphaX.sh"
check_pattern "review-feedback" "templates/project-work/local-pointer.md"
check_pattern "Completion State Vocabulary" "alphaX/project-review/README.md"
check_pattern "Completion State" "templates/project-review/report.md"
check_pattern "completion_call" "templates/project-review/report.md"
check_pattern "lifecycle_hygiene_trigger" "templates/project-review/report.md"
check_pattern "Trigger Signals" "templates/project-review/lifecycle-hygiene.md"
check_pattern "unfrozen evidence" "templates/project-review/lifecycle-hygiene.md"
check_pattern "problem-decomposer" "skills/problem-decomposer/SKILL.md"
check_pattern "Interaction Language" "skills/problem-decomposer/SKILL.md"

if [ -e "$ROOT/partner" ]; then
  find "$ROOT/partner" -maxdepth 4 -type f >&2 || true
  fail "public source still contains legacy partner/ local-asset tree"
fi

if [ -e "$ROOT/context-reloader" ]; then
  find "$ROOT/context-reloader" -maxdepth 4 -type f >&2 || true
  fail "public source still contains legacy context-reloader/ tree"
fi

if git -C "$ROOT" ls-files '.alphaX/*' | rg . >/dev/null; then
  git -C "$ROOT" ls-files '.alphaX/*' >&2
  fail ".alphaX local data is tracked by git"
fi

snapshot_output="$(bash "$ROOT/scripts/context-snapshot.sh" "$ROOT")"
if printf '%s\n' "$snapshot_output" | rg -n '\.alphaX/(process/|\.DS_Store)' >/dev/null; then
  printf '%s\n' "$snapshot_output" | rg -n '\.alphaX/(process/|\.DS_Store)' >&2
  fail "context snapshot includes noisy local alphaX process or system files"
fi

check_absent_public "/Users/"
check_absent_public "partner/"
check_absent_public "agent-interaction-bridge"
check_absent_public "online_community"
check_absent_public "clouds-beyond"
check_absent_public "PR #[0-9]+"
check_absent_public "Baseline freeze"
check_absent_public "alphaX-contract-v[0-9]"
check_absent_public "\\bv[0-9]+\\.[0-9]+"
check_absent_public "v[0-9]+(\\.[0-9]+)* \\([0-9]{4}-[0-9]{2}-[0-9]{2}\\)"
check_absent_public "Codex is the current"
check_absent_public "current execution carrier"
check_absent_public "currently a Markdown-first"
check_absent_public "public initial release"
check_absent_public "首次公开发布"
check_absent_public "当前工作树"

private_patterns="$ROOT/.alphaX/local/private-patterns.txt"
if [ -f "$private_patterns" ]; then
  while IFS= read -r pattern; do
    case "$pattern" in
      ""|\#*) continue ;;
    esac
    if rg -n -F "$pattern" "$ROOT" \
      -g '*.md' -g '*.yaml' -g '*.sh' \
      --glob '!.git/**' \
      --glob '!.alphaX/**' >/dev/null; then
      rg -n -F "$pattern" "$ROOT" \
        -g '*.md' -g '*.yaml' -g '*.sh' \
        --glob '!.git/**' \
        --glob '!.alphaX/**' >&2
      fail "public source contains a local private pattern"
    fi
  done <"$private_patterns"
fi

printf 'Alpha Partner open-source source verification passed: %s\n' "$ROOT"
