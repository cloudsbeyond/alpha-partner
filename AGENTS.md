---
type: "Source Contract"
title: "Alpha Partner Source"
description: "Root machine-facing contract, scope guard, and source map."
tags: ["alphax", "contract", "source"]
---
# Alpha Partner Source

```yaml
repository: alpha-partner
source_contract: okf-markdown-profile
product:
  call_sign: alphaX
  shape: personified collaboration function
  not:
    - MCP server
    - application
    - knowledge base
    - runtime
    - centralized project context store
  product_goal: enable agents to autonomously solve more high-value research and development problems under explicit evidence, scope, data, and human authority boundaries
  p0: agent-native source for trigger recognition, scope guard, evidence-backed judgment, project re-entry, risk/progress reporting, project review, source review, and checkpoint memory evaluation
  source_evolution_goal: raise alphaX intelligence ceiling and extend Alpha Partner Source asset half-life

source_layers:
  core_principles: thin, hard, long-lived judgment and governance boundaries
  cognitive_frameworks: reusable thinking shapes for framing, evidence weighting, and review judgment
  operational_scaffolding: current carrier defaults that stay replaceable and pruneable
  implementation_carriers: current file formats, scripts, parsers, and generated-index mechanisms
  governance_contract: alphaX/source-work/intelligence-ceiling-half-life.md
  rule: the core must stay thinner and harder than the scaffolding; scaffolding can stabilize today's carriers but must not define the product core

organization_level_pipeline:
  role: product-level frame for source work and review, not a runtime or control plane
  flow:
    - organization behavior signals
    - context representation
    - agent collaboration and navigation
    - human confirmation and authority audit
    - memory and feedback optimization
  rule: optimize signal quality, representation fidelity, navigation judgment, authority clarity, and feedback learning without turning alphaX into an app or always-on service

project_local_data:
  default_install: ".git/info/exclude + ignored .alphaX/"
  minimum_files:
    ".alphaX/index.md": stable operation contract and file map for ignored project-local alphaX data
    ".alphaX/project-context.md": current reload baseline for objective project state
  optional_extensions:
    ".alphaX/evidence.md": evidence pointer registry when compact pointers outgrow project-context.md
    ".alphaX/decisions.md": durable project decision ledger when decisions need stable lookup
    ".alphaX/reviews/": explicit durable local review artifacts when requested or needed for handoff
  boundary: context not control; live project source wins
  forbidden:
    - target tracked AGENTS.md alphaX pointer
    - target versioned .gitignore edit
    - AGENTS.md inside project .alphaX
    - reports directory as default catch-all
    - copied Alpha Partner Source

scopes:
  source work:
    target: Alpha Partner Source
    writes: tracked source after owner acceptance; local candidates under source checkout .alphaX/process/
  source review:
    target: Alpha Partner Source and alphaX mechanisms
    writes: report-first; no tracked source edits unless switched to source work
  project work:
    target: one external project/problem
    writes: target project by request; target .alphaX/project-context.md or boundary-specific optional files; temp dir; conversation
    alpha_partner: read-only
  project review:
    target: one project's delivery evidence
    writes: target .alphaX/project-context.md or explicit local review artifact; temp dir; conversation
    no_fixing_without_scope_switch: true

review_contracts:
  source review:
    goal: improve alphaX source and mechanisms
    contract: alphaX/source-review/agent-workflow.md
  project review:
    goal: judge target project delivery evidence
    contract: alphaX/project-review/agent-workflow.md
  shared_output_fields:
    - observed_evidence
    - inference
    - missing_evidence
    - confidence
    - unverified_claims

checkpoint_memory_evaluation:
  p0_requires_runtime: false
  dimensions:
    - re-entry memory
    - update memory
    - evidence memory
    - action memory
  evidence_inputs:
    - live source
    - target .alphaX/project-context.md and boundary-specific optional files
    - explicit user decisions
    - command output
    - artifacts
    - already available memory notes

data_boundary:
  tracked_source_contains:
    - contracts
    - SOPs
    - templates
    - verifier rules
    - skills
    - generic evidence
  tracked_source_must_not_contain:
    - .alphaX/
    - local project paths
    - concrete project status
    - process ledgers
    - pilot evidence
    - transcripts
    - secrets
    - hidden model chain-of-thought

cold_start:
  - read: AGENTS.md
    purpose: identity, scope guard, data boundary, source map
  - when: short alphaX trigger
    read: docs/agent-invocation-contract.md
    before: scope_or_loop_classification
  - read: alphaX/session-runbook.md
    purpose: conditional SOP table
  - when: behavior_or_tone_needed
    read: alphaX/persona.md
  - when: selected_loop_or_evidence_rubric_needed
    read: alphaX/operating-system.md

source_map:
  root: [README.md, docs/README.zh-CN.md, index.md]
  trigger_contract: [docs/agent-invocation-contract.md, docs/agent-trigger-fixtures.json, docs/agent-trigger-fixtures.md, docs/agent-failure-modes.md]
  judgment_contract: [docs/agent-judgment-fixtures.json, docs/agent-judgment-fixtures.md]
  core_sops: [alphaX/session-runbook.md, alphaX/activation-guide.md, alphaX/operating-system.md, alphaX/persona.md]
  work_sops: [alphaX/source-work/agent-workflow.md, alphaX/source-work/intelligence-ceiling-half-life.md, alphaX/source-review/agent-workflow.md, alphaX/project-work/agent-workflow.md, alphaX/project-work/context-reloader.md, alphaX/project-review/agent-workflow.md]
  docs: [docs/evidence-index.md, docs/research-backlog.md, docs/okf-markdown-profile.md, docs/asset-boundary.yaml, docs/local-alphaX-schema.md, docs/checkpoint-memory-evaluation-prd.md]
  templates: [templates/]
  skills: [skills/problem-decomposer/SKILL.md, skills/double-diamond-research/SKILL.md, skills/insight-catcher/SKILL.md, skills/formal-development/SKILL.md]
  scripts: [scripts/init-local-alphaX.sh, scripts/verify-local-alphaX.sh, scripts/verify-alpha-source.sh, scripts/context-snapshot.sh, scripts/detect-applied-run-candidates.sh, scripts/generate-alphaX-indexes.mjs]
```

## Operating Rules

- Classify one scope before writes.
- After scope and loop selection, check matching source skills before final framing or action.
- Live source beats `.alphaX/`, memory, handoff, and summaries.
- Passing checks do not prove human/product acceptance.
- Keep core principles thin and hard; evolve cognitive frameworks from evidence; keep scaffolding depreciable and implementation carriers replaceable.
- Do not promote P1/P2 runtime, scheduler, connector, or adapter work into P0.
- Durable memory updates, external publication, risky operations, destructive commands, and secrets require explicit approval.

## Verification

```bash
bash scripts/verify-alpha-source.sh
bash scripts/verify-local-alphaX.sh
```
