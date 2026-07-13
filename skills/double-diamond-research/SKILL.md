---
name: "double-diamond-research"
description: "Use when the user says 双菱形思考法, 双菱形, Double Diamond, or Double Diamond Research, or when an open complex research, strategy, product, organization, market, policy, AI adoption, industry, or cross-stakeholder problem must be framed from unclear problem space to evidence-backed decision options."
---
# 双菱形思考法

```yaml
skill: double-diamond-research
aliases:
  - 双菱形思考法
  - 双菱形
  - Double Diamond
  - Double Diamond Research

purpose: use two divergence-convergence cycles to turn an open, ambiguous, complex problem into a decision-grade recommendation
core_move: not answer first; first find the right problem, then compare solution paths, then converge by evidence, pilots, and constraints

concept_calibration:
  attribution: Double Diamond / 双菱形 is commonly attributed to the UK Design Council innovation framework, not to McKinsey.
  four_stages: [Discover, Define, Develop, Deliver]
  rhythm:
    first_diamond: "Discover diverges to open the problem space; Define converges to the real research problem."
    second_diamond: "Develop diverges to generate solution paths; Deliver converges to a validated recommendation."
  consulting_overlay:
    use: [hypothesis-driven thinking, issue tree, MECE decomposition, stakeholder analysis, evidence chain, option comparison, pilot design]
    rule: Double Diamond provides the research rhythm; consulting methods provide analysis discipline.
  avoid:
    - presenting Double Diamond as a McKinsey-owned framework
    - turning the skill into framework history or methodology explanation unless the user asks
    - recommending one path before the Define gate is explicit

best_for:
  - strategic transformation
  - organization change
  - product innovation
  - city governance
  - AI adoption and implementation strategy
  - industry research
  - public policy
  - business model design
  - complex system optimization
  - cross-department collaboration
  - open problems where stakeholders disagree on the problem definition

not_for:
  - already-clear implementation tasks
  - simple configuration questions
  - narrow factual lookup
  - normal project management execution
  - coding tasks where requirement, boundary, and acceptance criteria are already settled
```

## Operating Rule

Use the user's language by default. If the user says `双菱形思考法` or `双菱形`, make that the visible name. Keep `Double Diamond` and `Double Diamond Research` as aliases, not as the only user-facing label.

Start with the smallest useful structure. Do not force all sections if the user only needs a quick framing. For serious research, strategy, PRD, architecture, or decision work, run the full stage gate.

## Stage 0: 研究启动

Anchor the research to a decision before opening the problem.

```yaml
goal: clarify why this research exists and what decision it must support
questions:
  - 决策背景是什么？
  - 谁要用这个研究？
  - 最终要支持什么决策？
  - 时间、资源、数据、权限和边界是什么？
  - 什么变化可以证明这次研究有价值？
outputs:
  - decision_background
  - decision_user
  - target_decision
  - research_boundary
  - success_signal
```

If this stage is unclear, ask the smallest missing question instead of fabricating a decision owner or success standard.

## Discover: 打开问题

Do not rush to answer. Open the system behind the surface problem.

```yaml
goal: understand what is happening before accepting the apparent problem
key_questions:
  - 这个问题是谁的问题？
  - 问题的症状和根因分别是什么？
  - 不同利益相关方如何定义这个问题？
  - 哪些约束是真约束，哪些只是默认假设？
  - 有没有历史案例、外部标杆或相邻行业经验可以借鉴？
methods:
  - interviews
  - desk research
  - expert interviews
  - data inventory
  - process map
  - stakeholder map
  - system causality map
  - trend scan
  - policy and market environment scan
  - MECE research issue tree
outputs:
  - problem_map
  - stakeholder_map
  - initial_hypotheses
  - evidence_base
  - key_uncertainties
  - research_question_tree
```

In consulting mode, use a MECE issue tree to break an open problem into research modules. Keep the tree practical: it should improve evidence collection and decision quality, not become a decorative taxonomy.

## Define: 定义问题

Converge from many observations into one researchable, decision-relevant problem.

```yaml
goal: move from many possible problems to the highest-leverage problem worth solving now
key_questions:
  - 最核心的矛盾是什么？
  - 哪个问题一旦解决，会带来最大杠杆效应？
  - 现在真正需要回答的是事实问题、判断问题，还是决策问题？
  - 这个问题的成功标准是什么？
  - 哪些问题暂时不研究？
outputs:
  - core_problem_statement
  - research_boundary
  - judgment_criteria
  - priority_order
  - validation_hypotheses
  - next_stage_design_principles
```

Use this format when the problem definition is still unstable:

```text
我们观察到：______
这影响了：______
根本原因可能是：______
因此本研究要回答：______
决策者需要据此决定：______
成功标准是：______
不在本轮研究范围内的是：______
```

Guardrail: open complex research usually fails because the problem is defined too early, too narrowly, or incorrectly. If Define is weak, do not proceed as if solution work is ready.

## Develop: 生成方案

After Define is clear, diverge again into multiple comparable solution paths.

```yaml
goal: generate multiple candidate paths around the defined core problem
key_questions:
  - 有哪些不同层级的解决路径？
  - 短期止血、中期优化、长期重构分别是什么？
  - 政策、组织、技术、商业模式、流程、文化层面分别能做什么？
  - 有没有低成本试点方案？
  - 哪些方案看起来好，但风险过高？
methods:
  - solution tree
  - scenario planning
  - benchmark cases
  - innovation matrix
  - cost-benefit analysis
  - risk matrix
  - impact-feasibility matrix
  - sensitivity analysis
outputs:
  - candidate_solution_pool
  - solution_combinations
  - priority_matrix
  - pilot_design
  - risk_hypotheses
  - resource_estimate
path_evidence_rule:
  - each candidate path names its strongest supporting evidence, evidence gap, and distinct validation path
  - comparison without path-specific evidence and validation is not decision-grade
```

Use one of these comparison structures when helpful:

```yaml
risk_appetite_options:
  A: 保守优化型
  B: 结构调整型
  C: 突破创新型

time_horizon_options:
  short_term: 0-3 个月可做什么
  mid_term: 3-12 个月改变什么
  long_term: 12 个月以上重构什么
```

Do not present a single favorite solution as the only path unless the user has already made a decision and only needs implementation planning.

When Define and the comparison criteria are sufficient but evidence is not
strong enough for an irreversible commitment, still make a provisional
recommendation: choose the smallest reversible pilot or research path, and
state why the other paths are deferred. Do not turn evidence uncertainty into
an unranked list. Ordering is part of the contract: the opening and P0 may name
the decision process, but must not name a favored candidate before the visible
Define gate, candidate paths, and comparison. If Define itself is unsupported,
stop at Define and ask for the smallest missing decision instead of fabricating
paths.

## Deliver: 验证交付

Converge from candidate paths into an executable, verifiable, communicable recommendation.

```yaml
goal: turn research into a decision recommendation, pilot, or implementation roadmap
key_questions:
  - 我们推荐哪个方案？为什么不是其他方案？
  - 证据强度够不够？
  - 最小可行试点是什么？
  - 失败信号是什么？
  - 谁负责、何时做、用什么资源、如何衡量？
outputs:
  - final_recommendation
  - evidence_chain
  - implementation_roadmap
  - pilot_plan
  - KPI
  - risk_plan
  - decision_memo
```

Use this final deliverable structure when the user needs a decision-ready answer:

```text
1. 结论先行：我们建议采取______
2. 问题定义：真正的问题是______
3. 证据基础：支持判断的关键证据有______
4. 方案比较：我们评估了 A/B/C 三类方案
5. 推荐路径：优先选择______
6. 实施节奏：短中长期路线图
7. 风险与前提：关键风险、触发条件、备选方案
8. 下一步行动：谁在何时完成什么
```

## Default Output

Use this compact output unless the user asks for a full report:

```text
P0 主链路：
<一句话说明：先找对问题，再找对解法，用证据和试点收敛到决策>

Stage 0 / 研究启动：
- 决策背景：
- 决策使用者：
- 边界：
- 成功信号：

Discover / 打开问题：
- 问题地图：
- 利益相关方：
- 初始假设：
- 关键不确定性：

Define / 定义问题：
- 核心问题：
- 判断标准：
- 本轮不研究：

Develop / 生成方案：
- 候选路径：
- 比较维度：
- 可试点假设：

Deliver / 验证交付：
- 推荐路径：
- 证据链：
- 路线图：
- 风险和失败信号：
- 下一步：

P1/P2 停车场：
- <未来可能有用，但不影响本轮 P0 的内容>
```

## Pruning Rules

- Keep P0 to the problem-definition and decision path; move future-useful ideas to P1/P2.
- Do not expand vendor, component, or technology research unless it changes the P0 decision.
- Do not design a full system for edge cases before the core problem and success criteria are clear.
- Merge duplicate stakeholder, evidence, and solution categories.
- Mark observation, inference, assumption, decision, missing evidence, and out-of-scope items separately when stakes are high.
- If evidence is weak, recommend a pilot or next research step instead of pretending the recommendation is settled.
