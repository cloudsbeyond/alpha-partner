---
type: "SOP"
title: "Project Work"
description: "Project work trigger contract, scope guard, and assistance procedure."
tags: ["alphax", "project-work", "sop"]
---
# Project Work

```yaml
scope: project work
target: one concrete project, document, product question, research task, or engineering problem
alpha_partner_source: read-only

target_project_owns:
  - source of truth
  - ignored .alphaX/ data following docs/local-alphaX-schema.md

allowed_writes:
  - target project files when user asked to change that project
  - target .alphaX/ surfaces allowed by docs/local-alphaX-schema.md
  - OS temp dir
  - conversation

forbidden_writes:
  - source checkout .alphaX/process/ for project process data
  - alpha-partner tracked source unless user switches to source work
  - target tracked AGENTS.md alphaX pointer or versioned .gitignore edit
  - target .alphaX/AGENTS.md or catch-all reports directory

reentry:
  read: [alphaX/project-work/context-reloader.md, live target source, target .alphaX/ per schema when present]
  rule: live project source wins over stale .alphaX/ data

delivery_loop:
  purpose: keep project assistance tied to delivery state, artifact, gate, validation, and feedback instead of task-only execution
  states: [intake, clarify, design, implement, review, validate, handoff, reflect]
  required_before_execution:
    - current_state
    - target_artifact_or_decision
    - next_action
    - advance_hold_or_rework
    - gate
    - validation_method
    - validation_evidence
    - feedback_route
  advance_rule:
    advance_when: [target artifact exists or target decision is resolved, applicable human-owned gate is cleared, validation evidence supports the next action]
    otherwise: hold or rework at the responsible boundary
    output: advance_hold_or_rework with an evidence-bound reason
  authority_gates:
    human_owned:
      - strategic direction or business goal
      - L0-L2 product, architecture, data, permission, security, or contract decision
      - merge, release, publication, external document refresh, or durable memory update
    agent_owned:
      - L3-L4 implementation or validation work under a frozen upstream contract
      - evidence collection, comparison, and risk reporting
  feedback_to_rework:
    trigger: [user comment, review finding, failing test, missing evidence, acceptance gap]
    flow:
      - classify responsible boundary
      - list rework items
      - update or request the smallest affected artifact
      - name changed artifacts
      - state validation method and evidence
      - report closed items and open residue
  memory_filter:
    candidate_when:
      - reusable boundary judgment
      - verified project fact
      - evidence that changes future re-entry or action
    requires: [source pointer, verification path, update_or_expiry_rule]
    park_when: unverified, one-off, private, noisy, chat-only, or not actionable
  boundary: not a runtime, scheduler, connector, approval engine, or centralized project store

not_for:
  handoff_merge_release_freeze_or_claimed_completion: use project review first
```
