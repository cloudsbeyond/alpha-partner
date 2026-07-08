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
  alphaX/source-work/agent-workflow.md alphaX/source-work/intelligence-ceiling-half-life.md
  alphaX/source-review/agent-workflow.md
  alphaX/project-work/index.md alphaX/project-work/agent-workflow.md alphaX/project-work/context-reloader.md
  alphaX/project-review/agent-workflow.md
  docs/index.md docs/asset-boundary.yaml docs/README.zh-CN.md docs/local-alphaX-schema.md
  docs/okf-markdown-profile.md docs/agent-invocation-contract.md docs/agent-trigger-fixtures.md
  docs/agent-trigger-fixtures.json docs/agent-judgment-fixtures.md
  docs/agent-judgment-fixtures.json docs/agent-failure-modes.md docs/checkpoint-memory-evaluation-prd.md
  docs/research-backlog.md docs/evidence-index.md
  templates/index.md templates/research-loop-packet.md templates/project-work/index.md
  templates/project-work/loop-packet.md templates/thinking-loop-packet.md
  templates/memory-candidate-packet.md templates/checkpoint-memory-evaluation.md
  templates/reentry-risk-packet.md templates/loop-report.md templates/project-review/report.md
  templates/source-review/feedback-report.md templates/source-work/index.md
  templates/source-work/judgment-replay.md templates/source-work/insight-catcher.md
  templates/project-work/local-pointer.md
  skills/double-diamond-research/SKILL.md
  skills/problem-decomposer/SKILL.md
  skills/insight-catcher/SKILL.md
  skills/formal-development/SKILL.md
  skills/formal-development/references/layer-glossary.md
  skills/formal-development/references/coding-l0-l4.md
  skills/formal-development/references/non-coding-l0-l4.md
  scripts/init-local-alphaX.sh scripts/verify-local-alphaX.sh scripts/verify-alpha-source.sh
  scripts/context-snapshot.sh scripts/detect-applied-run-candidates.sh scripts/generate-alphaX-indexes.mjs
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
AGENTS.md	product_goal:
AGENTS.md	source_evolution_goal:
AGENTS.md	check matching source skills
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
AGENTS.md	judgment_contract:
AGENTS.md	governance_contract:
AGENTS.md	skills:
AGENTS.md	skills/problem-decomposer/SKILL.md
AGENTS.md	skills/double-diamond-research/SKILL.md
AGENTS.md	skills/insight-catcher/SKILL.md
AGENTS.md	skills/formal-development/SKILL.md
alphaX/source-work/agent-workflow.md	intelligence-ceiling-half-life.md
alphaX/source-work/agent-workflow.md	product_goal:
alphaX/source-work/agent-workflow.md	source_evolution_goal:
alphaX/source-work/agent-workflow.md	templates/source-work/judgment-replay.md
alphaX/source-work/agent-workflow.md	templates/source-work/insight-catcher.md
alphaX/source-work/intelligence-ceiling-half-life.md	product_goal:
alphaX/source-work/intelligence-ceiling-half-life.md	source_evolution_goal:
alphaX/source-work/intelligence-ceiling-half-life.md	root_contract_rule:
alphaX/source-work/intelligence-ceiling-half-life.md	proof_boundary:
alphaX/source-work/intelligence-ceiling-half-life.md	judgment_replay:
alphaX/source-work/intelligence-ceiling-half-life.md	insight_catcher:
alphaX/source-work/intelligence-ceiling-half-life.md	diminishing_return_stop:
alphaX/source-work/intelligence-ceiling-half-life.md	intelligence_ceiling_signals:
alphaX/source-work/intelligence-ceiling-half-life.md	half_life_signals:
alphaX/source-work/intelligence-ceiling-half-life.md	docs/agent-judgment-fixtures.json
alphaX/source-work/intelligence-ceiling-half-life.md	offline_semantic_verifier_boundary:
alphaX/source-review/agent-workflow.md	intelligence-ceiling-half-life.md
alphaX/session-runbook.md	skill_router:
alphaX/session-runbook.md	double_diamond_research
alphaX/session-runbook.md	formal_development
alphaX/operating-system.md	source_skills:
alphaX/operating-system.md	problem_decomposer:
alphaX/operating-system.md	formal_development:
alphaX/operating-system.md	loop_verification_gate:
alphaX/operating-system.md	independent_sensor
alphaX/loop-registry.md	loop_quality_gate:
alphaX/loop-registry.md	independent verification sensor
docs/agent-invocation-contract.md	p0_flow:
docs/agent-invocation-contract.md	intents:
docs/agent-invocation-contract.md	skill_trigger_layer:
docs/agent-invocation-contract.md	insight_catcher
docs/agent-invocation-contract.md	formal_development
docs/agent-invocation-contract.md	scope_rules:
docs/agent-invocation-contract.md	required_first_pass:
docs/agent-invocation-contract.md	output_self_check:
docs/agent-invocation-contract.md	forbidden_shortcuts:
docs/agent-trigger-fixtures.md	F10-loop-verification-gate
docs/agent-trigger-fixtures.json	F10-loop-verification-gate
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
docs/local-alphaX-schema.md	callable_truth_source_contract:
alphaX/project-work/context-reloader.md	callable_truth_source_rule:
alphaX/project-review/agent-workflow.md	^scope: project review$
alphaX/project-review/agent-workflow.md	not: alphaX source governance review
alphaX/project-review/agent-workflow.md	completion_fields:
alphaX/project-review/agent-workflow.md	acceptance_state:
alphaX/project-review/agent-workflow.md	delivery_flow_boundary:
alphaX/project-review/agent-workflow.md	Escalation Gate:
templates/project-review/report.md	review_mode:
templates/project-review/report.md	completion_state:
templates/project-review/report.md	acceptance_state:
templates/project-review/report.md	delivery_flow_state:
templates/project-review/report.md	completion_call:
templates/project-review/report.md	Project Lifecycle Hygiene:
templates/project-review/report.md	lifecycle_hygiene_trigger:
templates/project-review/report.md	unfrozen evidence
docs/checkpoint-memory-evaluation-prd.md	evidence_inputs:
docs/checkpoint-memory-evaluation-prd.md	dimensions:
docs/checkpoint-memory-evaluation-prd.md	memory_lifecycle:
docs/checkpoint-memory-evaluation-prd.md	Rubric
templates/checkpoint-memory-evaluation.md	Call rubric:
templates/checkpoint-memory-evaluation.md	memory_lifecycle:
templates/checkpoint-memory-evaluation.md	unverified_claims:
templates/loop-report.md	verification_loop:
templates/project-work/loop-packet.md	loop_verification:
docs/asset-boundary.yaml	shareable_function_assets:
docs/asset-boundary.yaml	external_project_local_objective_data:
docs/asset-boundary.yaml	canonical_paths:
docs/asset-boundary.yaml	optional_paths:
docs/asset-boundary.yaml	project_review_artifacts:
docs/asset-boundary.yaml	tracked_tree_must_not_contain:
docs/agent-judgment-fixtures.md	source_of_truth: agent-judgment-fixtures.json
docs/agent-judgment-fixtures.md	replay_contract:
docs/agent-judgment-fixtures.md	G06-scaffold-half-life-drag
docs/agent-judgment-fixtures.md	G08-loop-without-independent-sensor
docs/agent-failure-modes.md	FD-001:
docs/agent-failure-modes.md	formal-development terminology overfit
docs/agent-failure-modes.md	FD-002:
docs/agent-failure-modes.md	execution-context leakage
templates/source-work/judgment-replay.md	judgment_replay_packet:
templates/source-work/insight-catcher.md	disposition_status_values: \[covered, partial, absent, parked-with-reason\]
templates/source-work/insight-catcher.md	do_not_convert_boundary:
templates/source-work/insight-catcher.md	trace_is_asset_check:
templates/source-work/insight-catcher.md	diminishing_return_stop:
README.md	generate-alphaX-indexes.mjs
docs/okf-markdown-profile.md	YAML frontmatter
docs/okf-markdown-profile.md	generated index.md
skills/double-diamond-research/SKILL.md	double-diamond-research
skills/double-diamond-research/SKILL.md	双菱形思考法
skills/double-diamond-research/SKILL.md	Double Diamond Research
skills/double-diamond-research/SKILL.md	Deliver
skills/problem-decomposer/SKILL.md	problem-decomposer
skills/problem-decomposer/SKILL.md	Interaction Language
skills/problem-decomposer/SKILL.md	D0-D3
skills/insight-catcher/SKILL.md	insight-catcher
skills/insight-catcher/SKILL.md	创意捕手
skills/insight-catcher/SKILL.md	templates/source-work/insight-catcher.md
skills/insight-catcher/SKILL.md	self_iteration_exit_gates:
skills/insight-catcher/SKILL.md	diminishing_return_stop:
skills/formal-development/SKILL.md	formal-development
skills/formal-development/SKILL.md	Project Operating Loop
skills/formal-development/SKILL.md	Semantic Preservation
skills/formal-development/SKILL.md	L0-L4 is a judgment lens, not a mandatory target-project field schema
skills/formal-development/SKILL.md	prd_refs
skills/formal-development/SKILL.md	yaml_refs
skills/formal-development/SKILL.md	code_refs
skills/formal-development/SKILL.md	source_context_boundary:
skills/formal-development/SKILL.md	scan_literals:
skills/formal-development/SKILL.md	Negative scans must also stay semantic
skills/formal-development/SKILL.md	development_operating_loop:
skills/formal-development/SKILL.md	state_intake:
skills/formal-development/SKILL.md	decision_route:
skills/formal-development/SKILL.md	artifact_landing:
skills/formal-development/SKILL.md	evidence_feedback:
skills/formal-development/SKILL.md	Artifact Placement
skills/formal-development/SKILL.md	artifact_placement:
skills/formal-development/SKILL.md	Re-entry Router
skills/formal-development/SKILL.md	formal_development_phase
skills/formal-development/SKILL.md	formalize_existing
skills/formal-development/SKILL.md	Formal Development Review
skills/formal-development/SKILL.md	formal_projection: PRD.md
skills/formal-development/SKILL.md	architecture/project-traceability.yaml
skills/formal-development/SKILL.md	formal L0-L4 project assets
skills/formal-development/SKILL.md	L3 execution artifact when execution is in scope
skills/formal-development/SKILL.md	L3 execution refs -> L4 validation evidence
skills/formal-development/SKILL.md	l2_contract_artifacts_and_validators
skills/formal-development/SKILL.md	changelog_and_residual_risk
skills/formal-development/SKILL.md	passing checks.*acceptance
skills/formal-development/SKILL.md	references/layer-glossary.md
skills/formal-development/SKILL.md	references/coding-l0-l4.md
skills/formal-development/SKILL.md	references/non-coding-l0-l4.md
skills/formal-development/SKILL.md	l4_validation:
skills/formal-development/references/layer-glossary.md	Layer Glossary
skills/formal-development/references/layer-glossary.md	Few-shot classification
skills/formal-development/references/coding-l0-l4.md	coding_minimum_shape:
skills/formal-development/references/coding-l0-l4.md	coding_l4_carriers:
skills/formal-development/references/coding-l0-l4.md	Coding traceability field names
skills/formal-development/references/coding-l0-l4.md	prd_refs/yaml_refs/code_refs/validation
skills/formal-development/references/non-coding-l0-l4.md	non_coding_minimum_shape:
skills/formal-development/references/non-coding-l0-l4.md	non_coding_l4_carriers:
scripts/init-local-alphaX.sh	source-work-candidates
scripts/init-local-alphaX.sh	applied-runs
scripts/init-local-alphaX.sh	judgment-replays
scripts/init-local-alphaX.sh	source-evolution-candidates
scripts/init-local-alphaX.sh	thinking-notes
scripts/detect-applied-run-candidates.sh	Applied Run Candidate Scan
scripts/detect-applied-run-candidates.sh	read-only candidate detection
scripts/detect-applied-run-candidates.sh	loop-reports
scripts/detect-applied-run-candidates.sh	review-feedback
scripts/detect-applied-run-candidates.sh	source-evolution-candidates
scripts/detect-applied-run-candidates.sh	does not create, modify, or delete applied-run files
scripts/verify-local-alphaX.sh	Applied Runs
scripts/verify-local-alphaX.sh	Judgment Replays
scripts/verify-local-alphaX.sh	Source Evolution Candidates
scripts/verify-local-alphaX.sh	Thinking Notes
scripts/verify-local-alphaX.sh	legacy replay field case_id
scripts/verify-local-alphaX.sh	fixture_expected_judgment
scripts/verify-local-alphaX.sh	remaining_unverified_claims
scripts/verify-local-alphaX.sh	check_packet
scripts/verify-local-alphaX.sh	packet %d missing
scripts/verify-local-alphaX.sh	expected_judgment
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
  const codexSkill = file.startsWith('skills/') && file.endsWith('/SKILL.md');
  if (file !== 'README.md' && file !== 'docs/README.zh-CN.md' && !generatedIndex) {
    if (!text.startsWith('---\n')) fail.push(`${file}: missing YAML frontmatter`);
  }
  if (file !== 'README.md' && file !== 'docs/README.zh-CN.md' && !generatedIndex && !codexSkill) {
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

const rootContract = read('AGENTS.md');
for (const needle of [
  'product_goal:',
  'source_evolution_goal:',
  'enable agents to autonomously solve more high-value research and development problems',
  'raise alphaX intelligence ceiling and extend Alpha Partner Source asset half-life',
]) {
  if (!rootContract.includes(needle)) fail.push(`AGENTS.md: missing canonical product/source evolution contract: ${needle}`);
}

function requireTokenGroup(label, text, tokens) {
  const lower = text.toLowerCase();
  for (const token of tokens) {
    if (!lower.includes(token.toLowerCase())) fail.push(`${label}: missing concept token ${token}`);
  }
}

for (const [label, tokens] of [
  ['AGENTS.md source layer contract', ['source_layers:', 'core_principles', 'cognitive_frameworks', 'operational_scaffolding', 'implementation_carriers']],
  ['AGENTS.md source governance pointer', ['governance_contract', 'alphaX/source-work/intelligence-ceiling-half-life.md']],
  ['AGENTS.md organization pipeline frame', ['organization_level_pipeline:', 'behavior', 'context representation', 'agent collaboration', 'human', 'authority', 'memory', 'feedback', 'not a runtime']],
]) {
  requireTokenGroup(label, rootContract, tokens);
}

const formalDevelopmentSkill = read('skills/formal-development/SKILL.md');
const residualScanLines = formalDevelopmentSkill
  .split('\n')
  .map((line, index) => ({ line: line.trim(), lineNumber: index + 1 }))
  .filter(({ line }) => line.startsWith('rg -n '));
const allowedResidualScanTerms = new Set([
  'acceptance', 'architecture', 'asset', 'changing', 'checks', 'context', 'detail', 'depend',
  'devops', 'driven', 'execution', 'function', 'host', 'is', 'l0_refs', 'l1_l2_refs',
  'l3_refs', 'l4_validation', 'md', 'merge', 'method', 'n', 'notes', 'owns', 'passing',
  'product', 'product_narrative', 'project', 'publication', 'readiness', 'review', 'rg',
  'runtime', 'selected', 'single', 'source', 'source_order', 'spec', 'target', 'tests',
  'the', 'traceability', 'validation', 'workflow', 'yaml',
  'AI', 'CI', 'L0', 'L1', 'L2', 'L3', 'L4', 'P0', 'P1', 'P2', 'PRD', 'SDD', 'YAML',
]);
for (const { line, lineNumber } of residualScanLines) {
  for (const match of line.matchAll(/\b[A-Za-z][A-Za-z0-9_]*\b/g)) {
    const token = match[0].replace(/\\\./g, '.');
    if (!allowedResidualScanTerms.has(token)) {
      fail.push(`skills/formal-development/SKILL.md:${lineNumber}: residual scan contains non-semantic or concrete-looking token ${token}; use role-level semantics`);
    }
  }
}

const sourceGovernance = read('alphaX/source-work/intelligence-ceiling-half-life.md');
requireTokenGroup(
  'source governance goal boundary',
  sourceGovernance,
  ['goal_boundary:', 'product_goal_role', 'external outcome', 'source_evolution_goal_role', 'self-iteration', 'product goal', 'applied research or development problem evidence', 'source mechanism'],
);
if (!sourceGovernance.includes('proof_boundary:')) {
  fail.push('source governance: missing proof_boundary marker');
}
for (const [label, tokens] of [
  ['source governance proof boundary: verifier integrity is not intelligence proof', ['verifiers', 'source integrity', 'not', 'intelligence-ceiling']],
  ['source governance proof boundary: docs are intent not behavior', ['docs', 'intent', 'not', 'behavior change']],
  ['source governance proof boundary: product goal needs applied evidence', ['product-goal', 'applied research or development problem evidence']],
  ['source governance proof boundary: intelligence improvement needs replay or applied run', ['intelligence-ceiling', 'judgment-case-set', 'replay', 'applied run', 'problem reframing', 'upstream redefinition', 'alternative-path comparison', 'evidence weighting', 'boundary call', 'default override', 'strongest counterargument', 'keep/narrow/park']],
  ['source governance proof boundary: half-life needs principle/scaffold separation', ['asset half-life', 'durable principle', 'short-lived scaffolding']],
]) {
  requireTokenGroup(label, sourceGovernance, tokens);
}

requireTokenGroup(
  'source governance applied evidence accumulation policy',
  sourceGovernance,
  ['count-based samples', 'uncovered judgment case', 'materially different', 'high-value research', 'development problem', 'source mechanism gap', 'owner review', 'weak negative evidence', 'pruning candidate'],
);
requireTokenGroup(
  'source governance PDCA convergence gate',
  sourceGovernance,
  ['convergence_gate:', 'three consecutive cycles', 'no tracked source change', 'new materially different', 'external or project-bound evidence', 'owner review', 'source-mechanism blocker', 'active goal'],
);
requireTokenGroup(
  'source governance alternative-path signal',
  sourceGovernance,
  ['alternative solution paths', 'generated and compared before recommendation'],
);

const sourceReview = read('alphaX/source-review/agent-workflow.md');
requireTokenGroup(
  'source review proof-boundary check',
  sourceReview,
  ['source-integrity', 'intelligence-ceiling', 'product-goal proof'],
);

const checkpointPrd = read('docs/checkpoint-memory-evaluation-prd.md');
requireTokenGroup(
  'checkpoint memory PRD no-runtime boundary',
  checkpointPrd,
  ['no runtime', 'RPC', 'backend', 'scheduler', 'persistent memory service'],
);

const checkpointTemplate = read('templates/checkpoint-memory-evaluation.md');
requireTokenGroup(
  'checkpoint memory template runtime boundary',
  checkpointTemplate,
  ['boundary:', 'runtime', 'backend', 'no', 'interpretation_owner', 'approvals_needed', 'do_not_do_now'],
);

const fixtures = JSON.parse(read('docs/agent-trigger-fixtures.json'));
if (fixtures.schema_version !== 1) fail.push('fixtures: schema_version must be 1');
if ('judgment_checks' in fixtures || 'judgment_coverage' in fixtures) fail.push('fixtures: judgment checks belong in docs/agent-judgment-fixtures.json');
if (!Array.isArray(fixtures.fixtures)) fail.push('fixtures: fixtures must be an array');
const entries = Array.isArray(fixtures.fixtures) ? fixtures.fixtures : [];
const entryIds = new Set(entries.map((entry) => entry?.id).filter(Boolean));
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

const judgmentFixtures = JSON.parse(read('docs/agent-judgment-fixtures.json'));
const judgmentFixtureGuide = read('docs/agent-judgment-fixtures.md');
if (judgmentFixtures.schema_version !== 1) fail.push('judgment fixtures: schema_version must be 1');
const replayContract = judgmentFixtures.replay_contract;
if (!replayContract || typeof replayContract !== 'object' || Array.isArray(replayContract)) fail.push('judgment fixtures: replay_contract is required');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('problem reframing')) fail.push('judgment fixtures: replay_contract purpose must include problem reframing');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('upstream redefinition')) fail.push('judgment fixtures: replay_contract purpose must include upstream redefinition');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('alternative-path comparison')) fail.push('judgment fixtures: replay_contract purpose must include alternative-path comparison');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('evidence weighting')) fail.push('judgment fixtures: replay_contract purpose must include evidence weighting');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('boundary call')) fail.push('judgment fixtures: replay_contract purpose must include boundary call');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('default override')) fail.push('judgment fixtures: replay_contract purpose must include default override');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('strongest counterargument')) fail.push('judgment fixtures: replay_contract purpose must include strongest counterargument');
if (typeof replayContract?.purpose !== 'string' || !replayContract.purpose.includes('scaffold treatment')) fail.push('judgment fixtures: replay_contract purpose must include scaffold treatment');
if (!judgmentFixtureGuide.includes('problem reframing')) fail.push('judgment fixture guide: replay_contract purpose must include problem reframing');
if (!judgmentFixtureGuide.includes('upstream redefinition')) fail.push('judgment fixture guide: replay_contract purpose must include upstream redefinition');
if (!judgmentFixtureGuide.includes('alternative-path comparison')) fail.push('judgment fixture guide: replay_contract purpose must include alternative-path comparison');
if (!judgmentFixtureGuide.includes('evidence weighting')) fail.push('judgment fixture guide: replay_contract purpose must include evidence weighting');
if (!judgmentFixtureGuide.includes('boundary call')) fail.push('judgment fixture guide: replay_contract purpose must include boundary call');
if (!judgmentFixtureGuide.includes('default override')) fail.push('judgment fixture guide: replay_contract purpose must include default override');
if (!judgmentFixtureGuide.includes('strongest counterargument keep/narrow/park call')) fail.push('judgment fixture guide: replay_contract purpose must include strongest counterargument keep/narrow/park call');
if (!judgmentFixtureGuide.includes('scaffold treatment')) fail.push('judgment fixture guide: replay_contract purpose must include scaffold treatment');
if (!Array.isArray(replayContract?.minimum_packet_fields) || replayContract.minimum_packet_fields.length < 7) fail.push('judgment fixtures: replay_contract.minimum_packet_fields must declare replay evidence fields');
if (!Array.isArray(replayContract?.evidence_boundary) || replayContract.evidence_boundary.length < 3) fail.push('judgment fixtures: replay_contract.evidence_boundary must separate replay from product proof');
for (const field of ['case_ids', 'source_claim', 'observed_evidence', 'expected_judgment', 'actual_judgment', 'changed_call', 'remaining_unverified_claims']) {
  if (Array.isArray(replayContract?.minimum_packet_fields) && !replayContract.minimum_packet_fields.includes(field)) fail.push(`judgment fixtures: replay_contract missing packet field ${field}`);
}
const replayTemplate = read('templates/source-work/judgment-replay.md');
for (const field of Array.isArray(replayContract?.minimum_packet_fields) ? replayContract.minimum_packet_fields : []) {
  if (!replayTemplate.includes(`${field}:`)) fail.push(`judgment replay template: missing packet field ${field}`);
}
if (!Array.isArray(judgmentFixtures.cases) || judgmentFixtures.cases.length < 7) fail.push('judgment fixtures: at least seven cases are required');
const judgmentCases = Array.isArray(judgmentFixtures.cases) ? judgmentFixtures.cases : [];
if (!Array.isArray(judgmentFixtures.required_coverage) || judgmentFixtures.required_coverage.length < 6) fail.push('judgment fixtures: required_coverage must declare at least six signals');
if (Array.isArray(judgmentFixtures.required_coverage) && !judgmentFixtures.required_coverage.includes('alternative solution paths')) fail.push('judgment fixtures: required_coverage must include alternative solution paths');
for (const coverage of Array.isArray(judgmentFixtures.required_coverage) ? judgmentFixtures.required_coverage : []) {
  if (!judgmentFixtureGuide.includes(coverage)) fail.push(`judgment fixture guide: missing required coverage ${coverage}`);
}
const requiredCaseTests = new Set(Array.isArray(judgmentFixtures.required_coverage) ? judgmentFixtures.required_coverage : []);
for (const item of judgmentCases) {
  const id = item?.id || '<unknown>';
  for (const field of ['id', 'primary_fixture_id', 'source_layer', 'scenario', 'weak_default']) {
    if (typeof item?.[field] !== 'string' || item[field].trim() === '') fail.push(`${id}: missing ${field}`);
  }
  if (item?.primary_fixture_id && !entryIds.has(item.primary_fixture_id)) fail.push(`${id}: unknown primary_fixture_id ${item.primary_fixture_id}`);
  if (!judgmentFixtureGuide.includes(id)) fail.push(`judgment fixture guide: missing case ${id}`);
  for (const field of ['tests', 'evidence_inputs', 'expected_judgment', 'required_output', 'pass_condition', 'completion_boundary', 'forbidden']) {
    if (!Array.isArray(item?.[field]) || item[field].length === 0) fail.push(`${id}: ${field} must be non-empty`);
  }
  if (Array.isArray(item?.tests)) {
    for (const test of item.tests) requiredCaseTests.delete(test);
  }
}
for (const missing of requiredCaseTests) fail.push(`judgment fixtures: missing case for ${missing}`);
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
