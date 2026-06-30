---
type: "SOP"
title: "Alpha Partner Source Session Runbook"
description: "Machine-facing session start, route, evidence, and close contract."
tags: ["alphax", "session", "sop"]
---
# Alpha Partner Source Session Runbook

```yaml
cold_start:
  canonical:
    - read: AGENTS.md
      purpose: identity, scope guard, data boundary, source map
    - when: Short alphaX trigger
      read: docs/agent-invocation-contract.md
      before: scope_or_loop_call
    - read: smallest matching SOP
    - when: behavior calibration needed
      read: alphaX/persona.md
    - when: loop, evidence rubric, memory, focus/risk, manual loop, or intake rule needed
      read: alphaX/operating-system.md
  summarize:
    - alphaX is a personified collaboration function
    - default mode is Joint Research Execution
    - project .alphaX/ stores ignored objective project data, starting from index.md and project-context.md
    - source checkout .alphaX/ stores ignored local/process data

conditional_reads:
  activated_from_project: [alphaX/activation-guide.md]
  short_trigger: [docs/agent-invocation-contract.md, docs/agent-trigger-fixtures.json]
  project_reentry: [alphaX/project-work/context-reloader.md, target .alphaX/project-context.md when present]
  source_review: [alphaX/source-review/agent-workflow.md]
  project_review: [alphaX/project-review/agent-workflow.md]
  pilot: [alphaX/pilot-playbook.md]
  focus_or_risk: [alphaX/operating-system.md, optional .alphaX/process/focus-radar.md]
  recurring_loop: [alphaX/loop-registry.md]
  local_alphaX_needed:
    init: bash scripts/init-local-alphaX.sh
    verify: bash scripts/verify-local-alphaX.sh

scope_guard:
  source work:
    meaning: change Alpha Partner Source or alphaX function
    writes: tracked source only for accepted source change
  source review:
    meaning: review Alpha Partner Source and alphaX mechanisms
    writes: report-first; no tracked edits unless switched to source work
  project work:
    meaning: help one external project/problem
    writes: target project, target .alphaX/project-context.md, boundary-specific target .alphaX optional files, temp dir, or chat
    alpha_partner: read-only
  project review:
    meaning: report-first evidence review for one target project
    writes: target .alphaX/project-context.md, explicit target .alphaX/reviews/ artifact when useful and allowed, temp dir, or chat
    fixing_requires_scope_switch: true
  ambiguity:
    alpha_partner_cwd_external_target: ask before writing here

loop_router:
  research: templates/research-loop-packet.md
  project: templates/project-work/loop-packet.md
  project_review: templates/project-review/report.md
  source_review: templates/source-review/feedback-report.md or compact .alphaX/process note
  thinking: templates/thinking-loop-packet.md
  memory: templates/memory-candidate-packet.md
  focus_risk: templates/reentry-risk-packet.md
  manual_loop: templates/loop-report.md

skill_router:
  timing: after scope_guard and loop_router; before final framing, recommendation, or write action
  boundary: skills are cognitive tools inside the selected scope, not new scopes or runtimes
  rule: read the smallest matching skills/*/SKILL.md and apply it explicitly
  skills:
    problem_decomposer:
      file: skills/problem-decomposer/SKILL.md
      triggers: [real problem, essence, first-principles decomposition, D0-D3, wrong-level task]
      pairs_with: [thinking, project, spec_checkpoint]
    double_diamond_research:
      file: skills/double-diamond-research/SKILL.md
      triggers: [双菱形思考法, 双菱形, Double Diamond, open complex research, decision options]
      pairs_with: [research, thinking, project]
  composition:
    - if problem level is unclear, apply problem_decomposer before double_diamond_research
    - if the problem is already defined but solution space is open, apply double_diamond_research directly

project_local_setup:
  guide: templates/project-work/local-pointer.md
  default: target .git/info/exclude
  schema: docs/local-alphaX-schema.md
  expansion_rule: start with index.md and project-context.md; split optional files only for evidence, decision, or durable-review boundaries
  forbid:
    - target tracked AGENTS.md alphaX pointer
    - target versioned .gitignore edit
    - copying Alpha Partner Source into target repo
    - default reports directory
```

## Evidence Quality Rubric

```yaml
priority:
  - current local files and command output
  - exact user-provided sources
  - memory entries when prior context matters
  - external primary sources
  - secondary trend sources as weak signals only

strong_evidence:
  directness: code, diff, test, build, artifact, explicit acceptance tied to claim
  freshness: current branch/doc/command/user decision
  verifiability: rerunnable command, readable file, URL, artifact, line or commit pointer
  source_of_truth: contract, spec, test, release artifact, live git/source state

weak_evidence:
  - design intent as implementation proof
  - passing checks as human/product acceptance
  - chat or memory as current repo state
  - stale .alphaX/ as current truth

trace_shape:
  evidence:
    - source: file|command|url|artifact|user decision
      claim_supported: claim
      strength: strong|medium|weak|missing
      freshness: current|stale|unknown
      verified: yes|no
```

## Output Self-Check

```yaml
must_pass:
  - intent and scope match docs/agent-invocation-contract.md
  - write boundary respected
  - required source and live project evidence read, or missing evidence stated
  - material claims have evidence strength and freshness
  - unverified_claims includes unsupported, stale, or agent-supplied claims
  - next action is concrete and does not promote P1/P2 into P0
  - known failures in docs/agent-failure-modes.md avoided or called out
```

## Close

```yaml
verify:
  source_changed: bash scripts/verify-alpha-source.sh
  local_alphaX_used: bash scripts/verify-local-alphaX.sh
  always_report: [changed, verified, active_or_deferred]

ledger:
  source work: optional .alphaX/process/session-ledger.md
  source review: optional actor=source-review kind=meta entry
  project work: no alpha-partner ledger write
  project review: no alpha-partner ledger write
  exception: sanitized review-feedback only when mechanism feedback exists

handoff_state:
  p0: one-line current main line
  active_surface: project path, repo, or conversation
  branch: branch or n/a
  last_verified: YYYY-MM-DD
  next_block: one concrete next action
  open_risks:
    - id: short-id
      level: P0|P1|P2|P3
      evidence: file|command|note
  confidence: high|medium|low
  unverified_claims: []
```
