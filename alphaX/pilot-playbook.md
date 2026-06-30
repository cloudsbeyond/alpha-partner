---
type: "SOP"
title: "Pilot Playbook"
description: "Machine-facing procedure for alphaX project pilots."
tags: ["alphax", "pilot", "sop"]
---
# Pilot Playbook

```yaml
purpose: test whether alphaX improves real project R&D and thinking exploration
not: demo

pilot_tests_any:
  - sharper P0 definition
  - better product or architecture judgment
  - clearer L0-L4 boundary
  - stronger verification path
  - better external calibration
  - reusable reflection or memory candidate

candidate_filter:
  prefer:
    - clear source of truth
    - active decision or artifact
    - validation surface
  local_queue: ignored .alphaX/local/pilot-candidates.md

start_prompt_fields:
  alpha_partner_source: "{alpha-partner}/AGENTS.md"
  project_path_or_link: required
  source_of_truth: required
  current_goal: one concrete outcome
  first_output: [P0 main line, loop classification, evidence to inspect, next execution path]

flow:
  - cold start from AGENTS.md, alphaX/session-runbook.md, target instructions
  - classify loop: research|project|thinking|memory|review
  - use one template only when durable trace helps
  - do real work against target source of truth
  - run project-level validation when files or completion claims change
  - run bash scripts/verify-alpha-source.sh only if Alpha Partner Source changed
  - if source-work pilot and local ledger exists, append compact .alphaX/process/session-ledger.md entry

success_evidence_any:
  - changed concrete project artifact
  - clarified decision with stronger evidence
  - prevented over-scope or wrong-layer implementation
  - produced reusable packet, decision, or memory candidate
  - improved verification or source traceability

failure_evidence_any:
  - generic advice only
  - source of truth not identified
  - ticket executor behavior
  - process added without better decision or artifact
  - memory/trend claim used without current evidence

review_cadence:
  after_local_pilot_entries: 3
  inspect: .alphaX/process/session-ledger.md
  decide: [keep Markdown, adjust persona/runbook, add project-local pointers, promote stable skill, defer engineering]
```
