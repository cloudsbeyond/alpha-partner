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
  "alphaX/review-agent-mechanism.md"
  "alphaX/review-agent-bootstrap.md"
  "docs/asset-boundary.yaml"
  "docs/README.zh-CN.md"
  "docs/local-alphaX-schema.md"
  "docs/research-backlog.md"
  "docs/evidence-index.md"
  "functions/context-reloader/README.md"
  "templates/research-loop-packet.md"
  "templates/project-loop-packet.md"
  "templates/thinking-loop-packet.md"
  "templates/memory-candidate-packet.md"
  "templates/reentry-risk-packet.md"
  "templates/loop-report.md"
  "templates/project-local-pointer.md"
  "skills/problem-decomposer/SKILL.md"
  "scripts/init-local-alphaX.sh"
  "scripts/verify-local-alphaX.sh"
  "scripts/verify-alpha-source.sh"
  "scripts/context-snapshot.sh"
)

for file in "${required_files[@]}"; do
  check_file "$file"
done

check_pattern "^\\.alphaX/$" ".gitignore"
check_pattern "^\\.agents/$" ".gitignore"
check_pattern "MIT License" "LICENSE"
check_pattern "Alpha Partner Source" "AGENTS.md"
check_pattern "alphaX contract" "AGENTS.md"
check_pattern "alphaX contract: \\*\\*v0\\.1\\*\\*" "AGENTS.md"
check_pattern "personified collaboration function" "AGENTS.md"
check_pattern "Local Data Map" "AGENTS.md"
check_pattern "Runtime Modes And Write Boundary" "AGENTS.md"
check_pattern "External Assistance Mode" "AGENTS.md"
check_pattern "Interaction Language" "AGENTS.md"
check_pattern "GitHub" "AGENTS.md"
check_pattern "open-source function source only" "README.md"
check_pattern "LICENSE" "README.md"
check_pattern "docs/README.zh-CN.md" "README.md"
check_pattern "shareable_function_assets" "docs/asset-boundary.yaml"
check_pattern "open_source_repository_rule" "docs/asset-boundary.yaml"
check_pattern "tracked_tree_must_not_contain" "docs/asset-boundary.yaml"
check_pattern "Required Shape" "docs/local-alphaX-schema.md"
check_pattern "manifest.yaml" "docs/local-alphaX-schema.md"
check_pattern "scripts/init-local-alphaX.sh" "README.md"
check_pattern "scripts/verify-local-alphaX.sh" "README.md"
check_pattern "Context Reloader" "functions/context-reloader/README.md"
check_pattern "function/SOP" "functions/context-reloader/README.md"
check_pattern "project-local objective data" "templates/project-local-pointer.md"
check_pattern "Focus And Risk Loop" "alphaX/operating-system.md"
check_pattern "External Assistance Mode" "alphaX/session-runbook.md"
check_pattern "Loop Registry" "alphaX/loop-registry.md"
check_pattern "Agent-Native Activation" "alphaX/activation-guide.md"
check_pattern "Pilot Playbook" "alphaX/pilot-playbook.md"
check_pattern "Review Agent Mechanism" "alphaX/review-agent-mechanism.md"
check_pattern "Source Anchors" "alphaX/review-agent-mechanism.md"
check_pattern "Review Agent" "alphaX/review-agent-bootstrap.md"
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

check_absent_public "/Users/"
check_absent_public "partner/"
check_absent_public "agent-interaction-bridge"
check_absent_public "agent-runtime-services"
check_absent_public "online_community"
check_absent_public "clouds-beyond"
check_absent_public "PR #[0-9]+"
check_absent_public "v[0-9]+(\\.[0-9]+)* \\([0-9]{4}-[0-9]{2}-[0-9]{2}\\)"
check_absent_public "Codex is the current"
check_absent_public "current execution carrier"
check_absent_public "currently a Markdown-first"
check_absent_public "public initial release"
check_absent_public "首次公开发布"
check_absent_public "当前工作树"
check_absent_public "alphaX contract: \\*\\*v0\\.3\\*\\*"

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
