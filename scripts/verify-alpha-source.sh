#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

fail() { printf 'FAIL: %s\n' "$1" >&2; exit 1; }
has() { rg -n "$1" "$ROOT/$2" >/dev/null || fail "missing pattern in $2: $1"; }
exists() { [ -e "$ROOT/$1" ] || fail "missing path: $1"; }

source_rg() {
  rg "$@" "$ROOT" \
    -g '*.md' -g '*.yaml' -g '*.yml' -g '*.json' -g '*.js' -g '*.mjs' -g '*.sh' -g '*.txt' \
    --glob '!.git/**' --glob '!.alphaX/**' --glob '!scripts/verify-alpha-source.sh'
}

absent_public() {
  local pattern="$1"
  if source_rg -n "$pattern" >/dev/null; then
    source_rg -n "$pattern" >&2
    fail "public source contains forbidden pattern: $pattern"
  fi
}

required_paths=(
  .gitignore LICENSE README.md AGENTS.md index.md assets/icon.png
  alphaX/index.md alphaX/persona.md alphaX/operating-system.md alphaX/loop-registry.md
  alphaX/session-runbook.md alphaX/activation-guide.md alphaX/pilot-playbook.md
  alphaX/source-work/README.md alphaX/source-review/README.md
  alphaX/project-work/index.md alphaX/project-work/README.md alphaX/project-work/context-reloader.md
  alphaX/project-review/README.md
  docs/index.md docs/asset-boundary.yaml docs/README.zh-CN.md docs/local-alphaX-schema.md
  docs/okf-markdown-profile.md docs/agent-invocation-contract.md docs/agent-trigger-fixtures.md
  docs/agent-trigger-fixtures.json docs/agent-failure-modes.md docs/checkpoint-memory-evaluation-prd.md
  docs/research-backlog.md docs/evidence-index.md
  templates/index.md templates/research-loop-packet.md templates/project-work/index.md
  templates/project-work/loop-packet.md templates/thinking-loop-packet.md
  templates/memory-candidate-packet.md templates/checkpoint-memory-evaluation.md
  templates/reentry-risk-packet.md templates/loop-report.md templates/project-review/report.md
  templates/source-review/feedback-report.md templates/project-work/local-pointer.md
  skills/problem-decomposer/SKILL.md
  scripts/init-local-alphaX.sh scripts/verify-local-alphaX.sh scripts/verify-alpha-source.sh
  scripts/context-snapshot.sh scripts/generate-alphaX-indexes.mjs
)
for path in "${required_paths[@]}"; do exists "$path"; done

has "^\\.alphaX/$" .gitignore
has "^\\.agents/$" .gitignore
has "MIT License" LICENSE

contract_count="$(rg -n '^source_contract: okf-markdown-profile$' "$ROOT/AGENTS.md" | wc -l | tr -d ' ')"
[ "$contract_count" = "1" ] || fail "AGENTS.md must contain exactly one okf-markdown-profile source_contract field"

while IFS=$'\t' read -r file pattern; do
  [ -z "${file:-}" ] && continue
  has "$pattern" "$file"
done <<'EOF'
AGENTS.md	^repository: alpha-partner$
AGENTS.md	shape: personified collaboration function
AGENTS.md	project_local_data:
AGENTS.md	minimum_files:
AGENTS.md	optional_extensions:
AGENTS.md	scopes:
AGENTS.md	review_contracts:
AGENTS.md	checkpoint_memory_evaluation:
AGENTS.md	p0_requires_runtime: false
AGENTS.md	data_boundary:
AGENTS.md	cold_start:
AGENTS.md	source_map:
docs/agent-invocation-contract.md	p0_flow:
docs/agent-invocation-contract.md	intents:
docs/agent-invocation-contract.md	scope_rules:
docs/agent-invocation-contract.md	required_first_pass:
docs/agent-invocation-contract.md	output_self_check:
docs/agent-invocation-contract.md	forbidden_shortcuts:
templates/project-work/local-pointer.md	default: target .git/info/exclude
templates/project-work/local-pointer.md	target_tracked_tree:
templates/project-work/local-pointer.md	edit_versioned_AGENTS_md: false
templates/project-work/local-pointer.md	edit_versioned_gitignore: false
templates/project-work/local-pointer.md	project_alphaX_shape:
templates/project-work/local-pointer.md	optional_extensions:
templates/project-work/local-pointer.md	reports directory as default catch-all
docs/local-alphaX-schema.md	source_checkout_shape:
docs/local-alphaX-schema.md	target_project_shape:
docs/local-alphaX-schema.md	minimum_files:
docs/local-alphaX-schema.md	optional_extensions:
docs/local-alphaX-schema.md	current reload baseline
docs/local-alphaX-schema.md	git ls-files '.alphaX/\*' returns no paths
alphaX/project-review/README.md	^scope: project review$
alphaX/project-review/README.md	not: alphaX source governance review
alphaX/project-review/README.md	completion_fields:
alphaX/project-review/README.md	Escalation Gate:
templates/project-review/report.md	review_mode:
templates/project-review/report.md	completion_state:
templates/project-review/report.md	completion_call:
templates/project-review/report.md	Project Lifecycle Hygiene:
templates/project-review/report.md	lifecycle_hygiene_trigger:
templates/project-review/report.md	unfrozen evidence
docs/checkpoint-memory-evaluation-prd.md	p0_dependency: no runtime
docs/checkpoint-memory-evaluation-prd.md	evidence_inputs:
docs/checkpoint-memory-evaluation-prd.md	dimensions:
docs/checkpoint-memory-evaluation-prd.md	Rubric
templates/checkpoint-memory-evaluation.md	Call rubric:
templates/checkpoint-memory-evaluation.md	runtime_backend_used: no
templates/checkpoint-memory-evaluation.md	unverified_claims:
docs/asset-boundary.yaml	shareable_function_assets:
docs/asset-boundary.yaml	external_project_local_objective_data:
docs/asset-boundary.yaml	canonical_paths:
docs/asset-boundary.yaml	optional_paths:
docs/asset-boundary.yaml	project_review_artifacts:
docs/asset-boundary.yaml	tracked_tree_must_not_contain:
README.md	open-source function source only
README.md	without a runtime or RPC dependency
README.md	generate-alphaX-indexes.mjs
docs/okf-markdown-profile.md	YAML frontmatter
docs/okf-markdown-profile.md	generated index.md
skills/problem-decomposer/SKILL.md	problem-decomposer
skills/problem-decomposer/SKILL.md	Interaction Language
skills/problem-decomposer/SKILL.md	D0-D3
scripts/init-local-alphaX.sh	source-work-candidates
scripts/init-local-alphaX.sh	private-patterns.txt
scripts/init-local-alphaX.sh	source checkout
EOF

[ ! -e "$ROOT/partner" ] || fail "public source contains legacy local-asset directory: partner"
[ ! -e "$ROOT/context-reloader" ] || fail "public source contains legacy local-asset directory: context-reloader"

if git -C "$ROOT" ls-files '.alphaX/*' | rg . >/dev/null; then
  git -C "$ROOT" ls-files '.alphaX/*' >&2
  fail ".alphaX local data is tracked by git"
fi

snapshot_output="$(bash "$ROOT/scripts/context-snapshot.sh" "$ROOT")"
if printf '%s\n' "$snapshot_output" | rg -n '\.alphaX/(process/|\.DS_Store)' >/dev/null; then
  printf '%s\n' "$snapshot_output" | rg -n '\.alphaX/(process/|\.DS_Store)' >&2
  fail "context snapshot includes noisy local alphaX process or system files"
fi

node "$ROOT/scripts/generate-alphaX-indexes.mjs" --check >/dev/null || fail "generated Markdown indexes are stale or frontmatter is invalid"

ROOT_FOR_NODE_CHECK="$ROOT" node <<'NODE' || fail "structured source check failed"
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const root = process.env.ROOT_FOR_NODE_CHECK;
const read = (file) => fs.readFileSync(path.join(root, file), 'utf8');
const fail = [];
const files = cp.execFileSync('git', ['-C', root, 'ls-files', '--cached', '--others', '--exclude-standard', '--', '*.md'], { encoding: 'utf8' })
  .split('\n').map((line) => line.trim()).filter(Boolean).filter((file) => fs.existsSync(path.join(root, file)));

for (const file of files) {
  const text = read(file);
  const generatedIndex = file === 'index.md' || file.endsWith('/index.md');
  if (file !== 'README.md' && file !== 'docs/README.zh-CN.md' && !generatedIndex) {
    if (!text.startsWith('---\n')) fail.push(`${file}: missing YAML frontmatter`);
    if (!text.includes('```yaml\n')) fail.push(`${file}: missing fenced YAML body`);
  }

  const lines = text.split('\n');
  let fenced = false;
  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i];
    if (/^\s*(```|~~~)/.test(line)) { fenced = !fenced; continue; }
    if (fenced) continue;
    for (const match of line.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
      const raw = match[1].split('#')[0];
      if (!raw || /^[a-z]+:/i.test(raw) || raw.startsWith('mailto:')) continue;
      const target = path.normalize(path.join(root, path.dirname(file), decodeURIComponent(raw)));
      if (!fs.existsSync(target)) fail.push(`${file}:${i + 1}: broken link ${match[1]}`);
    }
  }
}

const contract = read('docs/agent-invocation-contract.md');
const intents = new Set();
let inIntents = false;
for (const line of contract.split('\n')) {
  if (line === 'intents:') { inIntents = true; continue; }
  if (inIntents && /^[a-z_]+:/.test(line)) inIntents = false;
  const match = inIntents && line.match(/^  ([a-z_]+):$/);
  if (match) intents.add(match[1]);
}

const fixtures = JSON.parse(read('docs/agent-trigger-fixtures.json'));
if (fixtures.schema_version !== 1) fail.push('fixtures: schema_version must be 1');
if (!Array.isArray(fixtures.fixtures)) fail.push('fixtures: fixtures must be an array');
const entries = Array.isArray(fixtures.fixtures) ? fixtures.fixtures : [];
for (const fixture of entries) {
  const id = fixture?.id || '<unknown>';
  for (const field of ['id', 'trigger', 'expected_intent', 'scope', 'loop']) {
    if (typeof fixture?.[field] !== 'string' || fixture[field].trim() === '') fail.push(`${id}: missing ${field}`);
  }
  for (const field of ['must_read', 'must_output', 'forbidden']) {
    if (!Array.isArray(fixture?.[field]) || fixture[field].length === 0) fail.push(`${id}: ${field} must be non-empty`);
  }
  if (fixture?.expected_intent && !intents.has(fixture.expected_intent)) fail.push(`${id}: unknown intent ${fixture.expected_intent}`);
}
for (const intent of intents) {
  if (!entries.some((fixture) => fixture.expected_intent === intent)) fail.push(`missing fixture for intent: ${intent}`);
}
for (const [id, needles] of Object.entries({
  'F01-risk-current-project': ['risk_review', 'completion call unless evidence review is explicitly requested'],
  'F02-progress-reentry': ['context_progress', 'target .alphaX/project-context.md when present'],
  'F03-before-merge-review': ['project_review', 'implementing fixes without scope switch'],
})) {
  const fixture = entries.find((entry) => entry.id === id);
  if (!fixture) { fail.push(`missing fixture: ${id}`); continue; }
  const text = JSON.stringify(fixture);
  for (const needle of needles) if (!text.includes(needle)) fail.push(`${id}: missing ${needle}`);
}

if (fail.length) {
  process.stderr.write(`${fail.join('\n')}\n`);
  process.exit(1);
}
NODE

forbidden_public_patterns=(
  "/Users/"
  "Source contract: initial"
  "first try loading rules"
  "agent-runtime-services"
  "alphaX-memory-family-rpc"
  "memory family"
  "memory-family"
  "JSON-RPC"
  "RUNTIME_SERVICES_RPC_URL"
  "ALPHAX_MEMORY_CONFIG"
  "runtime helper"
  "this checkout"
  "current session evidence"
  "current run"
  "allowed_current_session"
  "public initial release"
  "首次公开发布"
  "当前工作树"
)
for pattern in "${forbidden_public_patterns[@]}"; do absent_public "$pattern"; done

private_patterns="$ROOT/.alphaX/local/private-patterns.txt"
if [ -f "$private_patterns" ]; then
  while IFS= read -r pattern; do
    case "$pattern" in ""|\#*) continue ;; esac
    if source_rg -n -F "$pattern" >/dev/null; then
      source_rg -n -F "$pattern" >&2
      fail "public source contains a local private pattern"
    fi
  done <"$private_patterns"
fi

printf 'Alpha Partner open-source source verification passed: %s\n' "$ROOT"
