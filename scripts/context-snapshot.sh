#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-$PWD}"
if [ ! -d "$TARGET" ]; then
  printf 'FAIL: not a directory: %s\n' "$TARGET" >&2
  exit 1
fi

ROOT="$(cd "$TARGET" && pwd -P)"
ALPHA_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "$ROOT"

section() {
  printf '\n## %s\n' "$1"
}

section "Workspace"
printf 'path: %s\n' "$ROOT"
printf 'date: %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')"

section "Git"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'git_root: %s\n' "$(git rev-parse --show-toplevel)"
  printf 'branch: %s\n' "$(git branch --show-current 2>/dev/null || true)"
  printf 'status:\n'
  git status --short
  printf 'recent_commits:\n'
  git log --oneline -5 2>/dev/null || true
else
  printf 'not a git repository\n'
fi

section "Instruction Files"
find . -maxdepth 3 -type f \( \
  -name 'AGENTS.md' -o \
  -path '*/.alphaX/*' -o \
  -name 'README.md' -o \
  -name 'README' -o \
  -name 'CLAUDE.md' -o \
  -name 'GEMINI.md' -o \
  -name '*.code-workspace' \
\) -print | sort | sed -n '1,80p'

section "Partner Pointer"
if [ -d ".alphaX" ]; then
  printf 'present: .alphaX project metadata\n'
  find .alphaX -maxdepth 2 -type f -print | sort | sed -n '1,20p'
elif [ -f "AGENTS.md" ] && rg -n "Alpha Partner|alphaX|共同研究执行" "AGENTS.md" >/dev/null 2>&1; then
  printf 'present: root AGENTS.md references Alpha Partner\n'
  rg -n "Alpha Partner|alphaX|共同研究执行" "AGENTS.md" | sed -n '1,20p'
else
  printf 'not found in root AGENTS.md\n'
  printf 'pointer_template: %s/partner/templates/project-local-pointer.md\n' "$ALPHA_ROOT"
fi

section "Likely Source Of Truth"
find . -maxdepth 4 -type f \( \
  -iname '*prd*' -o \
  -iname '*spec*' -o \
  -iname '*contract*' -o \
  -iname '*architecture*' -o \
  -iname '*design*' -o \
  -iname '*roadmap*' -o \
  -iname '*changelog*' -o \
  -iname '*acceptance*' \
\) -not -path '*/node_modules/*' \
  -not -path '*/.git/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*' \
  -print | sort | sed -n '1,120p'

section "Top-Level Files"
find . -maxdepth 2 -type f \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*' \
  -not -name '.DS_Store' \
  -print | sort | sed -n '1,120p'
