---
type: "SOP"
title: "Alpha Partner Source Operating System"
description: "Machine-facing loop registry for evidence, project work, thinking, memory, risk, and manual reports."
tags: ["alphax", "operating-system", "sop"]
---
# Alpha Partner Source Operating System

```yaml
artifact_rule:
  every_important_collaboration_lands_in_one_or_more:
    - problem
    - evidence
    - decision
    - validation
    - reflection

loops:
  research:
    purpose: frontier evidence without trend drift
    flow: [define project-linked question, collect primary sources, extract mechanisms, map to local practice, record implication]
    accept: output changes a decision, question, experiment, or project practice
    trace: docs/research-backlog.md or docs/evidence-index.md by source-work request

  project:
    purpose: calibrate alphaX on real project surfaces
    flow: [identify source of truth, state P0 and constraint, classify work type, keep L0-L4 visible, verify]
    accept:
      - concrete project improvement or clearer next decision
      - no downstream patching when upstream contract is ambiguous
      - after applied session, record contract rule that helped, got in way, and was unused
    pruning_rule: "Lack of use is a weak negative signal, not deletion evidence by itself."

  thinking:
    purpose: turn exploration into reusable judgment
    flow: [capture tension, separate observation/inference/judgment/decision, challenge strongest assumption, synthesize, choose destination]
    accept: clear claim, clear scope, known/inferred/uncertain separated

  memory:
    purpose: continuity without global-memory pollution
    flow: [use current files first, search memory when prior context matters, write candidate if durable, update global memory only by user request, cite memory when material]
    accept: memory improves continuity without overriding current evidence

  checkpoint_memory_evaluation:
    purpose: test remembered/project-local state before adding memory infrastructure
    triggers: [re-entry, handoff, freeze, project review, source iteration, remembered-state claim]
    dimensions: [re-entry memory, update memory, evidence memory, action memory]
    calls: [pass, partial, fail]
    evidence_inputs: [live source, target .alphaX/project-context.md, optional target .alphaX/* when referenced or review depth requires it, explicit user decisions, command output, artifacts, already available memory notes]
    boundary: no runtime service, no centralized project store, no scheduler, no connector, no approval engine
    accept:
      - each dimension has call, evidence pointer, gap
      - superseded claims downgraded or replaced
      - result changes next action or proves no action needed

  focus_risk:
    title: Focus And Risk Loop
    purpose: recover context, choose focus, catch missed risk
    triggers:
      - alphaX restore this project context
      - alphaX review risks across my projects
      - project paused; align current state first
    first_inspect:
      - current repo surface
      - target AGENTS.md/README/specs/contracts/changelog/diff
      - target .alphaX/project-context.md when present
      - optional target .alphaX/* only when referenced or review depth requires it
      - validation commands and open gaps
    report: [P0, current state, top risks, focus move, parking lot]
    risk_vocabulary: [source-of-truth drift, false completion, wrong-layer work, authority/privacy risk, stale context, over-scoping, verification gap]
    boundary: context reloader is function/SOP; live source wins over stale .alphaX/

  manual_loop:
    purpose: repeated attention/risk/drift/nudge checks before schedulers
    flow: [pick alphaX/loop-registry.md entry, run read-only unless approved, output templates/loop-report.md, gate nudges by evidence/urgency/cooldown/approval]
    accept: report reduces attention burden or catches risk; no hidden background action

  spec_checkpoint:
    trigger: accumulated constraints or drift
    output: [P0 main line, pruned points, deferred points, confirmation points]
    boundary: no new framework, no P1/P2 promotion

source_skills:
  role: reusable cognitive tools that strengthen selected loops
  boundary: apply inside current scope; do not create runtime, scheduler, connector, or autonomous control
  problem_decomposer:
    source: skills/problem-decomposer/SKILL.md
    strengthens: [thinking, project, spec_checkpoint]
    use_when: assigned task may be wrong-level or the real problem, objective, evaluation method, or feedback loop is unclear
    expected_effect: move from current task to real problem, redefined problem, higher objective, and validation loop
  double_diamond_research:
    source: skills/double-diamond-research/SKILL.md
    strengthens: [research, thinking, project]
    use_when: open complex problem needs problem-space divergence, problem definition, solution-path divergence, and decision convergence
    expected_effect: turn unclear problem space into evidence-backed decision options
  composition_rule: if both match, use Problem Decomposer for problem level first, then 双菱形思考法 for research and solution convergence

agent_intake_rule:
  principle: between agents there is no shared runtime and no mutual presence; only file trace
  steps:
    - separate claims from evidence
    - keep verifiable evidence as fact
    - demote unsupported conclusions to unverified_claim
    - preserve confidence and unverified_claims from handoff
    - write durable references by role, not presence

agent_failure_mode_guard:
  title: Agent Failure Mode Guard
  source: docs/agent-failure-modes.md
  applies_to: [trigger, handoff, review, fixture ambiguity]
  catches: [intent misclassification, scope drift, weak-evidence upgrade, stale context upgrade, false completion, wrong-layer work, missing next action, data boundary leak]
  boundary: not a broad scoring system

packets:
  research: templates/research-loop-packet.md
  project: templates/project-work/loop-packet.md
  thinking: templates/thinking-loop-packet.md
  memory: templates/memory-candidate-packet.md
  checkpoint_memory: templates/checkpoint-memory-evaluation.md
  reentry_risk: templates/reentry-risk-packet.md
  manual_loop: templates/loop-report.md
```
