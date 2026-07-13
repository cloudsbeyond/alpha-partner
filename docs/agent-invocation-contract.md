---
type: "Agent Contract"
title: "Agent Invocation Contract"
description: "Machine-facing contract for mapping short alphaX triggers to scope, loops, evidence, and output."
tags: ["alphax", "agent", "invocation"]
---
# Agent Invocation Contract

```yaml
p0_flow:
  - short_trigger
  - intent_and_scope_call
  - package_and_source_identity_resolution
  - required_source_read
  - skill_trigger_check
  - live_project_evidence_check
  - evidence_backed_state_or_risk_call
  - next_action

default_rule: do not ask the user to restate project context until first source pass fails to identify target, write boundary, or source of truth

source_identity_gate:
  project_work_and_review: resolve and hash-check the immutable accepted Source embedded in the installed package
  source_work_and_review: require an explicit live Source checkout and label candidate state
  behavior_identity: [package_version, package_source_commit, package_source_branch, package_source_authority]
  source_identity: [scope, source_commit, source_branch_or_ref, source_authority]
  forbidden: mutable checkout lookup as an implicit project-scope authority
  reporting_rule: copy scope and resolved source fields exactly from resolve-invocation; never substitute package-source or current-checkout identity
  scope_enum: [source-work, source-review, project-work, project-review]

intents:
  engage:
    triggers: ["alphaX engage", "@alphaX engage", "alphaX 介入一下"]
    default_scope: infer from target
    loop: Project loop
    first_read: [AGENTS.md, alphaX/session-runbook.md, target instructions]
    minimum_output: [P0, source of truth, loop, next action]

  context_progress:
    triggers: ["alphaX 现在项目进展到哪儿了", "restore this project context", "项目现在怎么样"]
    default_scope: project work unless reviewing completion
    loop: Focus/risk plus Context Reloader
    first_read: [alphaX/project-work/context-reloader.md, target .alphaX/project-context.md when present, optional target .alphaX/* when referenced or review depth requires it, live project source]
    minimum_output: [current state, changed evidence, risks, next action]

  risk_review:
    triggers: ["@alphaX 帮我看看当前项目风险", "alphaX daily radar", "review risks"]
    default_scope: focus/risk
    loop: Focus/risk
    first_read: [alphaX/operating-system.md Focus And Risk Loop, target instructions, live git/source state]
    minimum_output: [top risks with evidence, confidence, next focus move]

  project_review:
    triggers: ["合入前审一下", "run project review", "检查声称完成是否真的实现"]
    default_scope: project review
    loop: Project review
    first_read: [alphaX/project-review/agent-workflow.md, target source of truth, diff, validation surface]
    minimum_output: [findings first, completion state, missing evidence, next action]

  problem_decompose:
    triggers: ["这件事真正要解决什么", "what are we actually trying to solve"]
    default_scope: conversation or project work; live project evidence does not turn decomposition into project review
    loop: Thinking loop plus Problem Decomposer
    first_read: [skills/problem-decomposer/SKILL.md, project source when project-bound]
    minimum_output: [D0-D3 map, recommended focus, validation signal]

  double_diamond_research:
    triggers: ["双菱形思考法", "双菱形", "Double Diamond", "Double Diamond Research", "开放复杂问题研究结构"]
    default_scope: conversation or project work; incomplete implementation, failed validation, or missing acceptance evidence does not upgrade research to project review
    loop: Research loop plus 双菱形思考法 / Double Diamond Research
    first_read: [skills/double-diamond-research/SKILL.md, project source when project-bound]
    minimum_output: [P0 main line, Discover Define Develop Deliver map, evidence gaps, next decision]

  source_review:
    triggers: ["alphaX self-critique", "检查 alphaX 本身", "source drift check"]
    default_scope: source review
    loop: Source review or self-critique
    first_read: [alphaX/source-review/agent-workflow.md, alphaX/loop-registry.md Loop 7]
    minimum_output: [source risks, evidence, source-work candidates]

  manual_loop:
    triggers: ["alphaX nudge check", "alphaX PR CI watch", "alphaX research intake", "alphaX 设计一个自迭代 loop"]
    default_scope: project work; use source scope only for an explicit Alpha Partner Source review or change
    loop: Manual loop layer
    first_read: [alphaX/loop-registry.md, target source when applicable]
    minimum_output: [loop report, boundary, approval needs]

skill_trigger_layer:
  role: source skills are cognitive tools applied inside the chosen scope and loop
  timing: after intent_and_scope_call and required_source_read; before final framing, recommendation, or project action
  rule: read and apply the smallest matching skill; do not treat a skill as a new scope or runtime
  minimal_set:
    problem_decomposer:
      source: skills/problem-decomposer/SKILL.md
      use_when: the task may be solving the wrong problem, asks for real problem, essence, first-principles decomposition, or D0-D3 framing
      output: D0-D3 map, recommended focus, validation signal
    double_diamond_research:
      source: skills/double-diamond-research/SKILL.md
      use_when: the user says 双菱形思考法, 双菱形, Double Diamond, Double Diamond Research, or asks for open complex research to become decision options
      output: Stage 0, Discover, Define, Develop, Deliver, evidence gaps, next decision
    insight_catcher:
      source: skills/insight-catcher/SKILL.md
      use_when: creative inputs, readings, talks, notes, or research signals must be evaluated as alphaX mechanism candidates before tracked source changes
      output: disposition-tracked candidate ledger, judgment trace, exit-gate call, and next owner decision
    formal_development:
      source: skills/formal-development/SKILL.md
      use_when: formal-development work touches project initialization, later iteration, existing-project formalization, conformance review, PRD.md, product narrative, architecture narrative, L0-L4, formal contracts, Project Traceability, or spec/SDD residue cleanup
      output: phase call, L0 asset mapping, PRD projection boundary, downstream L1-L4 chain, conformance review findings when requested, validation and closeout state
  composition:
    - use problem_decomposer first when the P0 problem level is unclear
    - use formal_development before writing or reviewing PRD, architecture, contract, traceability, harness, or implementation assets in formal-development work
    - use double_diamond_research when the problem is open, multi-stakeholder, strategic, or research-heavy
    - use insight_catcher before source changes triggered by creative input batches
    - if both match, run problem_decomposer to locate the problem level, then double_diamond_research to structure research and solution convergence

scope_rules:
  - choose exactly one primary scope before writes
  - completion/merge/release/handoff/claimed implementation judgment => project review
  - current risk/progress/re-entry/focus without completion claim => Focus/risk or Context Reloader
  - problem decomposition, Double Diamond research, and manual-loop design stay project work unless the user explicitly asks for Source review or change
  - incomplete implementation or failed validation is project evidence; it does not by itself upgrade project work to project review
  - source review findings and calls concern Alpha Partner Source only; target-project facts may support routing or Source-mechanism evidence but must not become project implementation, validation, acceptance, completion, release, or mergeability findings
  - Alpha Partner Source change => source work only after owner acceptance
  - alpha-partner cwd plus external target => ask before writing here
  - ambiguous but read-only inspection can disambiguate => inspect first

required_first_pass:
  - identify target
  - read relevant alpha-partner contract/SOP
  - read target AGENTS.md/README/specs/contracts/tests/changelog/diff, target .alphaX/project-context.md when present, and optional target .alphaX/* only when referenced or review depth requires it
  - separate live facts, project-local objective data, memory/handoff claims, inference, missing evidence, user decisions
  - produce minimum output before optional durable trace

output_self_check:
  - intent and scope named or clearly implied
  - write boundary respected
  - source of truth read or missing evidence stated
  - material claims have evidence strength and freshness
  - cited target-file claims have an explicit successful content read; discovery or listing alone is missing evidence
  - weak/stale claims listed under unverified_claims
  - next action concrete and not P1/P2 expansion
  - project work may call hold/rework but does not declare completion or merge readiness
  - evidence-boundary overridden_default names the Source scaffold, while override_reason names the conflicting evidence
  - alternative-path research presents Define and comparable paths before any favored path, including in the opening
  - an explicit user or judgment-contract statement that Define and success criteria are sufficient for comparison is authoritative for that decision; sparse project evidence does not reopen Define
  - Double Diamond output always maps Discover, Define, Develop, and Deliver; stages beyond a blocked gate are marked blocked or deferred rather than omitted
  - comparable paths include a provisional reversible recommendation, reasons alternatives are deferred, and path-specific evidence gaps and validation approaches
  - project review starts with findings; completion and mergeability calls follow findings and missing evidence
  - nontrivial runs report package behavior identity and resolved Source identity
  - reported scope is one exact scope enum and resolved Source fields match resolve-invocation even when a candidate package embeds accepted project-scope Source
  - scaffold half-life review names durable_principle, short_lived_scaffold, and prune_or_replace_action while preserving the core boundary

forbidden_shortcuts:
  - treating .alphaX/project-context.md as current truth without rereading live source
  - treating optional target .alphaX/* as control or source of truth
  - treating passing checks as human/product acceptance
  - using design docs as proof of implementation
  - writing project facts into Alpha Partner Source
  - expanding to runtime/scheduler/notification/connector design unless P0 depends on it
```
