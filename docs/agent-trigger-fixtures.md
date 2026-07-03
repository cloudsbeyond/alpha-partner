---
type: "Verification Fixtures"
title: "Agent Trigger Fixtures"
description: "Regression fixtures for validating alphaX trigger-to-loop behavior."
tags: ["alphax", "fixtures", "agent"]
---
# Agent Trigger Fixtures

```yaml
source_of_truth: agent-trigger-fixtures.json
role: readable guide only
fixture_contract:
  proves:
    - trigger maps to one primary intent and loop
    - required source is read before decision
    - matching skills/*/SKILL.md is read when a source skill trigger is present
    - live target source wins over .alphaX/, memory, or handoff
    - output contains evidence, unverified_claims when needed, and one next action
    - forbidden writes or product expansions do not happen

judgment_fixtures:
  source: agent-judgment-fixtures.json
  boundary: trigger fixtures test routing; judgment fixtures test intelligence-ceiling behavior

fixtures:
  F01-risk-current-project:
    trigger: "@alphaX 帮我看看当前项目风险"
    expected_intent: risk_review
    scope: focus/risk
    loop: Focus/risk
    must_read: [target AGENTS.md, README/specs/contracts, git status/diff, target .alphaX/project-context.md when present, optional target .alphaX/* when referenced]
    must_output: [P0, current state, top risks with evidence, confidence, next focus move]
    forbidden: [code edits, source edits, scheduled nudge, completion call unless evidence review is explicitly requested]

  F02-progress-reentry:
    trigger: "alphaX 现在项目进展到哪儿了"
    expected_intent: context_progress
    scope: project work unless completion judgment requested
    loop: Focus/risk plus Context Reloader
    must_read: [alphaX/project-work/context-reloader.md, target instructions, target .alphaX/project-context.md when present, optional target .alphaX/* when referenced, live source/diff]
    forbidden: [treating stale .alphaX/ as truth]

  F03-before-merge-review:
    trigger: "合入前审一下"
    expected_intent: project_review
    scope: project review
    loop: Project review
    must_read: [alphaX/project-review/agent-workflow.md, target diff, tests, build output or missing validation evidence]
    forbidden: [implementing fixes without scope switch]

  F04-real-problem:
    expected_intent: problem_decompose
    must_read: [skills/problem-decomposer/SKILL.md, project source when project-bound]
    forbidden: [invented business goals]

  F09-double-diamond-research:
    trigger: "双菱形思考法"
    expected_intent: double_diamond_research
    must_read: [skills/double-diamond-research/SKILL.md, project source when project-bound]
    must_output: [P0 main line, Discover Define Develop Deliver map, evidence gaps, next decision]
    forbidden: [McKinsey-owned framework claim, one-solution recommendation before Define, P1/P2 promotion]

  F05-source-self-critique:
    expected_intent: source_review
    must_read: [alphaX/source-review/agent-workflow.md, alphaX/loop-registry.md, relevant source files, verifier output]
    forbidden: [tracked source edits]

  F06-source-drift:
    expected_intent: source_review or target project review
    forbidden: [mixing source-review and project-review outputs]

  F07-nudge-check:
    expected_intent: manual_loop
    must_read: [alphaX/loop-registry.md, active invocation evidence]
    forbidden: [external push, schedule, cross-app observation]

  F10-loop-verification-gate:
    trigger: "alphaX 设计一个自迭代 loop"
    expected_intent: manual_loop
    loop: Manual loop layer plus loop verification gate
    must_read: [alphaX/operating-system.md, alphaX/loop-registry.md, target source when target-bound, current loop gate evidence]
    must_output: [loop goal, authority boundary, independent sensor, feedback-to-next-action path, cost or stop boundary, manual-or-upgrade call]
    forbidden: [treating repeated activity as improvement, scheduling without approval, hidden authority upgrade]

  F08-engage:
    expected_intent: engage
    must_read: [AGENTS.md, alphaX/session-runbook.md, target instructions, skill router check]
    forbidden: [asking user to restate context before first source pass]

pass_criteria:
  - expected intent/scope named or implied
  - required source read or missing evidence stated
  - findings are evidence-backed
  - one concrete next action
  - forbidden action avoided without explicit approval

failure_recording:
  classify_with: Agent Failure Modes
  file: agent-failure-modes.md
  boundary: no project-specific facts in Alpha Partner Source
```
