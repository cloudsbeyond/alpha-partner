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
  p0: agent-native source for trigger recognition, scope guard, evidence-backed judgment, project re-entry, risk/progress reporting, project review, source review, and checkpoint memory evaluation

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
    contract: alphaX/source-review/README.md
  project review:
    goal: judge target project delivery evidence
    contract: alphaX/project-review/README.md
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
  core_sops: [alphaX/session-runbook.md, alphaX/activation-guide.md, alphaX/operating-system.md, alphaX/persona.md]
  work_sops: [alphaX/source-work/README.md, alphaX/source-review/README.md, alphaX/project-work/README.md, alphaX/project-work/context-reloader.md, alphaX/project-review/README.md]
  docs: [docs/evidence-index.md, docs/research-backlog.md, docs/okf-markdown-profile.md, docs/asset-boundary.yaml, docs/local-alphaX-schema.md, docs/checkpoint-memory-evaluation-prd.md]
  templates: [templates/]
  scripts: [scripts/init-local-alphaX.sh, scripts/verify-local-alphaX.sh, scripts/verify-alpha-source.sh, scripts/context-snapshot.sh, scripts/generate-alphaX-indexes.mjs]
```

## Operating Rules

- Classify one scope before writes.
- Live source beats `.alphaX/`, memory, handoff, and summaries.
- Passing checks do not prove human/product acceptance.
- Do not promote P1/P2 runtime, scheduler, connector, or adapter work into P0.
- Durable memory updates, external publication, risky operations, destructive commands, and secrets require explicit approval.

## Verification

```bash
bash scripts/verify-alpha-source.sh
bash scripts/verify-local-alphaX.sh
```
