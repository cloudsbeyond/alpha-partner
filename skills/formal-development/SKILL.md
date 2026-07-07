---
name: formal-development
description: "Use when alphaX is doing, re-entering, refactoring, or reviewing formal-development / 形式化研发 work as a project development OS / 项目研发 OS: project initialization / 项目初始化, later iteration / 后续迭代, existing-project formalization / 存量项目形式化重构, PRD.md creation or refresh, product narrative / 产品叙事 consolidation, architecture narrative / 架构叙事 boundary, formal contracts / 形式化契约, Project Traceability / 项目级追踪, coding or non-coding L0-L4 minimum shapes / 编码或非编码最小形态, project state routing / 项目状态路由, artifact placement / 产物落点, evidence feedback / 证据回灌, L4 validation alignment / 验证证据对齐, spec/SDD residue cleanup, or formal-development review / 形式化研发评审."
---

# Formal Development / 形式化研发

```yaml
skill: formal-development
purpose: operate alphaX formal-development / 形式化研发 as a project-level development OS / 研发 OS driven by consolidated product intent, fixed PRD.md projection / 形式化投影, architecture narrative / 架构叙事, formal contracts / 形式化契约, and validation evidence / 验证证据
not: PRD template generator, runtime, scheduler, connector, or generic spec-writing process
default_language: user's language
reentrant: true
stable_terms:
  product_narrative: product narrative / 产品叙事; project-declared human-facing L0 narrative path or paths
  formal_projection: formal projection / 形式化投影; fixed root PRD.md
  architecture_narrative: architecture narrative / 架构叙事; L1/L2 system organization narrative
  formal_contract: formal contract / 形式化契约; Concept Registry, YAML, schema, protocol, contract snapshot, or harness freeze signal
  execution_organization: execution or implementation organization / 执行或实现组织; L3 artifacts that realize L2 in code or non-code workflows
  validation_evidence: validation evidence / 验证证据; L4 proof or drift evidence for L3 conformance to L0-L2
  project_traceability: Project Traceability / 项目级追踪; L0-to-validation alignment surface
```

## Core Invariant / 核心不变量

Do not start formal development from scattered specs. Start by locating or
consolidating the project-specific product narrative, then keep `PRD.md` as
the fixed formal L0 projection of that same product intent.

```yaml
l0_assets:
  product_narrative:
    primary: <project-specific human narrative path, often README.md>
    localized: []
    supporting: []
    legacy_candidates: []
  formal_projection: PRD.md
```

`product_narrative` is a role, not a fixed filename. It may be `README.md`,
`README.zh-CN.md`, product docs, or a project-specific combination.
`formal_projection` is fixed as root `PRD.md`.

For layer terminology, goals, non-goals, carriers, anti-examples, and few-shot
classification, read `references/layer-glossary.md` only when needed.

Reference loading:

- Do not load all references by default. If the carrier is clear, read exactly
  one scenario file:
  - coding work: `references/coding-l0-l4.md`
  - non-coding work: `references/non-coding-l0-l4.md`
- Read `references/layer-glossary.md` only when layer terminology, goal,
  non-goal, anti-example, or few-shot classification is ambiguous.
- If the right reference is unclear, inspect `references/index.md` first, then
  load the smallest matching reference file.
- Keep `SKILL.md` as the operational route and layer scheme. Keep explanatory
  terminology, scenario examples, and few-shot material in reference files.

## Project Operating Loop / 项目研发闭环

Treat formal-development as a project-level development OS. It is not a
service or control plane; it is the repeatable loop that keeps project state,
layer decisions, durable assets, and evidence feedback aligned.

This loop is an index, not a second copy of the rules. When a rule changes,
edit the canonical section below and update this loop only if the route itself
changes.

```yaml
development_operating_loop:
  state_intake:
    purpose: establish current project state before edits
    canonical_rule: Re-entry Router / Re-entry inputs
  decision_route:
    purpose: choose the responsible layer before changing assets
    canonical_rule: Workflow / phase procedures and layer separation
  artifact_landing:
    purpose: land durable formal-development assets in tracked project source
    canonical_rule: Artifact Placement / 产物落点
  evidence_feedback:
    purpose: close each claim with proportionate proof and route drift upstream
    canonical_rule: Formal Development Review + Verify And Close
```

## Artifact Placement / 产物落点

Land formal-development artifacts in the target project's tracked source by
default. Use target `.alphaX/` only for local context, review aids, or temporary
process evidence; do not put formal project assets there. Do not write target
project facts into Alpha Partner Source.

```yaml
artifact_placement:
  product_narrative:
    default: README.md or project-declared docs path
  formal_projection:
    fixed: PRD.md
  architecture_narrative:
    default: architecture/README.md or existing architecture entrypoint
  l2_contracts:
    default: architecture/, schemas/, contracts/, or existing contract directory
  project_traceability:
    machine: architecture/project-traceability.yaml
    human: architecture/project-traceability.md
  l3_execution:
    default: implementation, workflow, template, or operation directories
  l4_validation:
    default: tests, test-results, reviews, changelog, or validation evidence paths
  local_alphaX:
    allowed: context, review aids, temporary process evidence
    forbidden: formal L0-L4 project assets
```

## Re-entry Router / 可重入路由

Classify the project phase before writing. If the phase is ambiguous, inspect
live files and git state first, then declare the best-supported phase and
uncertainty.

```yaml
formal_development_phase:
  initialize:
    label_zh: 项目初始化
    use_when: new project, new repo, new product slice, or no declared L0 assets
    goal: establish first usable formal-development spine without overdesign
  iterate:
    label_zh: 后续迭代
    use_when: project already has L0-L4 assets and a new feature/change/bugfix arrives
    goal: route the change through the existing formal chain without drifting L0
  formalize_existing:
    label_zh: 存量项目形式化重构
    use_when: existing project has README/docs/spec/SDD/changelog/code but no stable formal-development spine
    goal: migrate valid intent and architecture into the L0-L4 chain without erasing history
  review:
    label_zh: 形式化研发评审
    use_when: user asks whether a project follows formal-development rules, before merge/release/handoff, or after a claimed completion
    goal: judge conformance from evidence, not improve the project unless scope switches to project work
```

Re-entry inputs, in order:

- current `pwd`, git branch, status, recent diff and changed files
- project `AGENTS.md`, README files, `PRD.md`, architecture docs, contracts,
  tests, changelog
- project-local `.alphaX/project-context.md` only as staleable context
- exact user decisions in the current thread
- validation commands and artifacts

Live tracked source wins over `.alphaX/`, memory, summaries, and prior handoff
notes.

## Workflow / 工作流

### 1. Classify Scope / 判定作用域

Use alphaX scope rules before edits: `source work`, `project work`,
`project review`, or `source review`. Do not write project facts into Alpha
Partner Source, and do not put alphaX process data into target tracked source.

### 2. Select Phase Procedure / 选择阶段流程

#### Initialize / 项目初始化

For a new project or product slice:

1. Identify the first product narrative entrypoint; if absent, draft it before
   writing `PRD.md`.
2. Create root `PRD.md` only after the product narrative is coherent enough to
   project.
3. Add the minimum architecture narrative or architecture README needed to
   explain system organization and boundary.
4. Add L2 contracts only for P0 surfaces that need durable implementation.
5. Add the smallest verification path that can catch L0/L1/L2/L4 drift.
6. Record P1/P2 in parking or open questions, not P0.

Default minimum:

```yaml
minimum_initialize_assets:
  - product_narrative primary path
  - PRD.md
  - architecture entrypoint or concept registry when structure matters
  - L3 execution artifact when execution is in scope
  - validation command or manual review gate
  - changelog/current baseline when the project will continue
```

#### Iterate / 后续迭代

For a later change in an already formalized project:

1. Reload declared L0 assets and the active downstream contract path.
2. Decide whether the change affects L0, L1, L2, L3 execution, or only L4
   validation evidence.
3. If L0 changes, update product narrative and `PRD.md` together before
   downstream assets.
4. If L1/L2 changes, update architecture narrative and formal contracts before
   implementation.
5. If L3 changes, verify the execution artifact remains linked to existing
   L1/L2 contracts and does not introduce new product promises.
6. If only L4 changes, update validation evidence without changing L0-L3; when
   L4 exposes drift, route the fix back to the responsible upstream layer.
7. Update traceability, validation indexes, changelog, and residual risk only
   when they are part of the project's existing spine.

#### Formalize Existing / 存量项目形式化重构

For a stock project with spec/SDD/process residue:

1. Inventory product narrative scattered across README, docs, old spec/SDD,
   architecture introductions, changelog, and code-facing docs.
2. Split findings into:
   - current product intent
   - current architecture judgment
   - historical process trace
3. Converge current product intent into declared product narrative paths and
   root `PRD.md`.
4. Converge architecture judgment into architecture narrative, Concept Registry,
   protocol, schema, or harness.
5. Preserve historical process trace as changelog, legacy, or review evidence.
6. Add residual scans so future work does not continue using old specs as the
   driver.

Do not delete old spec/SDD blindly. Downgrade it only after valid intent and
architecture judgment have a current home.

#### Review / 形式化研发评审

For conformance review, stay report-first unless the user switches to project
work. Review the project against the rubric below and cite evidence.

```yaml
formal_development_review:
  l0_assets:
    pass: actual product narrative path declared and PRD.md fixed as formal projection
    fail: PRD.md is the only L0 source, or product narrative is scattered and undeclared
  l0_equivalence:
    pass: PRD.md reflects product narrative without silent promises or deletions
    fail: PRD.md, README, docs, or changelog contradict P0 scope/value boundary
  layer_boundary:
    pass: architecture explains organization/flow/boundaries; contracts verify structure; L3 execution and L4 evidence stay downstream
    fail: architecture changes product promise, or L3/L4 artifacts redefine L0/L1/L2
  traceability:
    pass: nontrivial work maps L0 refs -> L1/L2 refs -> L3 execution refs -> L4 validation evidence -> residual risk
    fail: completion claim has checks or evidence but no upstream contract refs, or broad claim from narrow checks
  spec_residue:
    pass: old spec/SDD is legacy/source material, not current driver
    fail: scattered specs, SDD notes, or process docs still drive product or implementation
  validation:
    pass: commands or review gates correspond to claimed completion state
    fail: passing checks are presented as product acceptance, merge readiness, or publication readiness
```

Review output:

```text
Formal Development Review / 形式化研发评审:
- Call / 结论: pass | partial | fail
- Phase / 阶段: initialize | iterate | formalize-existing | review
- Evidence / 证据:
- Violations / 违规点:
- Missing Evidence / 缺失证据:
- Required Fix Before Durable Implementation / 持久实现前必须修复:
- Residual Risk / 剩余风险:
- Completion State / 完成状态:
```

### 3. Inventory Product Narrative / 盘点产品叙事

Inspect likely narrative surfaces before writing `PRD.md`:

- root `README*`
- product docs under `docs/`
- architecture introductions or blueprints
- changelog current baselines
- old spec/SDD files
- project-local `.alphaX/project-context.md` only as context, not truth

Classify each source:

```yaml
narrative_source_class:
  current_product_intent: converge into product_narrative and PRD.md
  current_architecture_judgment: converge into architecture narrative, SOP, Concept Registry, protocol, schema, or harness
  historical_process_trace: keep as changelog, legacy, or review evidence; do not drive current development
```

### 4. Establish L0 Asset Mapping / 建立 L0 资产映射

Declare actual paths before downstream edits. Prefer explicit paths over
abstract `product_narrative` placeholders in YAML or traceability assets.

### 5. Write Or Refresh PRD.md / 编写或刷新 PRD.md

Make `PRD.md` a compressed, citable, trackable, freezeable L0 projection of
confirmed product intent. It should include:

- L0 problem
- P0 scope
- non-goals
- downstream chain
- owner boundary
- return-to-L0 conditions

Do not let `PRD.md` invent promises that are absent from the product
narrative. Do not let it delete confirmed product intent silently.

### 6. Separate Downstream Layers / 分离下游层级

Use this chain:

```text
product narrative / 产品叙事 + PRD.md / 形式化投影
  -> architecture narrative / 架构叙事 + concept registry / 概念注册表
  -> protocol / schema / contract snapshot / equivalent formal asset / 等价形式化资产
  -> execution / implementation organization / 执行或实现组织
  -> harness / drift check / AI Contract Index / 契约漂移检查
  -> changelog / validation evidence / 变更记录与验证证据
```

Rules:

- L0 product narrative and `PRD.md` own why, for whom, what problem, value
  boundary, P0 scope, and non-goals.
- L1 architecture narrative explains system organization, main flow, objects,
  states, authority, and boundaries.
- L2 formal contracts make L1 structure verifiable.
- L3 execution or implementation organization realizes L2 contracts in concrete
  code modules or non-code execution artifacts; it must not change product
  promise or architecture contract silently.
- L4 validation evidence proves whether L3 conforms to L0/L1/L2; it can expose
  drift, but it must not redefine the product, architecture, or contract.

Minimum layer shape:

```yaml
l0_product: [product_narrative, PRD.md]
l1_architecture: [architecture narrative, concept registry]
l2_formal_contract: [schema, protocol, rubric, checklist, contract snapshot]
l3_execution: [code modules or repeatable non-code workflow artifacts]
l4_validation:
  minimum_shape: [expectation, refs, evidence, result, residual_risk]
  rule: treat passing checks as validation evidence, not human acceptance
```

Read `references/layer-glossary.md` for full layer goals and non-goals. For
scenario-specific coverage, minimum shapes, and L4 examples, read only the
matching reference file under `references/`.

### 7. Decide Whether Project Traceability Is Needed / 判断是否需要项目级追踪

Add or update `architecture/project-traceability.md` and `.yaml` when work spans
multiple long-lived slices, modules, profiles, or future agent iterations.

Minimum machine-readable shape:

```yaml
l0_assets:
  product_narrative:
    primary: README.md
    localized: []
    supporting: []
  formal_projection: PRD.md
authority:
  source_order:
    - README.md
    - PRD.md
    - project_traceability_yaml
    - architecture_narrative_and_concept_registry
    - l2_contract_artifacts_and_validators
    - l3_execution_artifacts
    - l4_validation_evidence
    - changelog_and_residual_risk
```

Each verified expectation must include actual L0 refs, L1/L2 refs, L3 execution
refs, L4 validation evidence, and residual risk.

### 8. Verify And Close / 验证与收口

Run the project or source verification appropriate to the scope. Always add a
residual scan for wrong entrypoints:

```bash
rg -n '(single L0|单一 L0|唯一 L0|the L0 product asset|PRD\.md is the L0|owns L0|SDD ->|spec-driven|source_order: \[PRD.md|source_order: \[product_narrative)'
rg -n '(passing checks.*acceptance|validation.*product acceptance|L4.*(acceptance|merge readiness|publication readiness)|tests?.*product acceptance|review notes.*changing L0)'
git diff --check
```

Completion state vocabulary:

```yaml
completion_state:
  integration_state: draft|validated-local|committed-local|pushed|PR-ready|mergeable|publishable
  l0_mapping: <actual product_narrative path(s) + PRD.md>
  validation: <commands run>
  residual_risk: []
```

Passing checks prove validation, not product acceptance, merge readiness, or
publication readiness.

## Spec Checkpoint / 规格检查点

When the user asks to align, compress, prune, review, or refresh PRD/architecture
assets, output:

```text
P0 主链路：
<一句话>

本轮剪枝：
- <删除/合并/降级的点>

保留但后置：
- <移到 P1/P2/待决策/阶段性调研的点>

待确认：
- <需要用户确认的少数决策点>
```

Default P0 main line for this SOP:

```text
先按项目声明产品叙事入口，再把同一组产品意图固定投影为 PRD.md，随后由架构叙事、形式化契约和验证资产承接 L1-L4。
```
