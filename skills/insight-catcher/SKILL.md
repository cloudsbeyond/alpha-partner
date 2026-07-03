---
name: "insight-catcher"
description: "创意捕手 / Insight Catcher. Use when external content, ideas, research signals, talks, notes, or creative inputs should be captured, graded, and turned into disposition-tracked alphaX mechanism candidates before any tracked source change. 当外部内容、想法、研究信号、分享、笔记或创意输入需要先捕获、分级并转成 alphaX 机制候选时使用。"
---

# 创意捕手

Insight Catcher captures creative inputs, grades their reusable mechanism value,
lands judgment evidence, and only then considers tracked source changes.

## 关键点（中文速览）

```text
一句话目标：外部内容、想法、研究信号或创意输入进来，第一产出是「带处置状态的候选 ledger + 判断 trace」，不是源码补丁。

三大支柱：
1. 核心目标（Core Objective）
   - 用「捕获 → 机制化 → 分级处置 → 证据落地」推进 alphaX，而不是逐条给源打补丁。
   - 每个识别出的机制候选必须落到唯一状态：covered 已覆盖 / partial 部分 / absent 缺席 / parked-with-reason 带理由搁置。
   - 源码补丁只是「source_decision=patch-candidate 且有回放证据」后的下游候选产物。

2. 六项验收标准（Acceptance Criteria）——检验判断过程是否诚实、可追溯、防漂移
   - 无静默丢失：每个机制候选都要在 ledger 里有显式状态，不能既不推进也不搁置。
   - 不以窄充全：部分覆盖必须标 partial 并写明缺口，禁止用单点补丁冒充多维候选处理。
   - 先证据后改源：任何 tracked 改动都需「处置状态 + source_decision 理由 + 至少一个 judgment-replay 案例」。
   - trace 即资产：本轮评估、承认的遗漏、分级变化原因，落在忽略层 .alphaX/process/。
   - 搁置要诚实：标 covered 必须指向真实已有源证据，否则只能标 partial 或 parked。
   - 数据边界：tracked 源不得含外部原文、私有事实、忽略层过程记录或本地插件资产路径。

3. 自迭代退出闸门（Self-Iteration Exit Gates）——命中任一即停，不得制造假进展
   - 硬闸门（owner）：要动 tracked 源 / 对外发布 / 风险操作 → 停在 owner review。
   - 收敛闸门：连续 N 轮（默认 3）无新外部证据、无新 tracked 变更、无新指令 → 停。换车道不算新进展。
   - 边际递减闸门：新一轮处置状态相比上一轮无跃迁（无 absent→partial、无 partial→covered）→ 停并标记 no_state_transition，交 owner 决定。
```

```yaml
skill: insight-catcher
canonical_names: [insight-catcher, 创意捕手]
purpose: turn creative inputs into disposition-tracked alphaX mechanism candidates before any tracked source change
purpose_zh: 把创意输入转成「带处置状态的 alphaX 机制候选」，再决定是否改源
first_deliverable: templates/source-work/insight-catcher.md
not:
  - a source patch generator / 不是补丁生成器
  - a summary of the input batch / 不是输入内容摘要
  - a durable memory updater / 不是持久记忆更新器
  - a way to justify a change already decided / 不是为已决定的改动补理由

scope: source work
boundary:
  - candidate and source decouple: record reusable mechanism candidates, never copy external article facts or private data into tracked source
  - 候选与来源解耦：只记录可迁移机制候选，绝不把外部原文或私有数据抄进 tracked 源
  - the ledger and its judgment trace are the asset; a tracked patch is only a downstream candidate after source_decision=patch-candidate and replay support
  - ledger 与判断 trace 才是资产；tracked 补丁只是 source_decision=patch-candidate 且有 replay 支撑后的下游候选产物
  - live source wins; existing coverage must be cited, not assumed
  - live source 优先；已覆盖必须引用真实证据，不能假设

when_to_use:
  - user brings external content, research, talks, notes, or ideas for alphaX evaluation / 用户带来外部内容、研究、分享、笔记或想法要评估
  - user asks whether an idea should become an alphaX mechanism candidate / 用户问某个想法是否应成为 alphaX 机制候选
  - user asks what to keep, narrow, or park from a batch of creative inputs / 用户问一批创意输入里哪些推进、收窄、搁置
  - a source-work round risks narrowing many candidates into one convenient patch / 一轮源工作有把多候选窄化成单补丁的风险
  - before opening a tracked source diff triggered by creative inputs / 在因创意输入动 tracked diff 之前

core_objective:
  statement: evolve alphaX by capture, mechanism framing, graded disposition, and evidence landing, not by per-item source patching
  statement_zh: 用「捕获 → 机制化 → 分级处置 → 证据落地」推进 alphaX，而不是逐条给源打补丁
  first_output_rule: the first deliverable is a disposition-tracked candidate ledger plus judgment trace, never a source patch
  first_output_rule_zh: 第一产出永远是「带处置状态的候选 ledger + 判断 trace」，绝不是源码补丁
  disposition_states: [covered, partial, absent, parked-with-reason]
  disposition_states_zh: [已覆盖, 部分, 缺席, 带理由搁置]
  invariant: every identified mechanism candidate resolves to exactly one disposition_status; a tracked patch is only a downstream candidate after source_decision=patch-candidate and replay support
  invariant_zh: 每个识别出的机制候选只落到唯一 disposition_status；tracked 补丁只是 source_decision=patch-candidate 且有 replay 支撑后的下游候选产物
  generalization: constrains the shape of judgment, independent of how many candidates or input items exist this round
  generalization_zh: 约束的是判断的形状，与本轮候选或输入条目多少无关

acceptance_criteria:
  no_silent_loss:
    must: every identified mechanism candidate appears in the ledger with an explicit disposition
    must_zh: 每个识别出的机制候选都要在 ledger 里有显式处置状态
    anti_pattern: a candidate is neither advanced nor parked / 某候选既不推进也不搁置
  no_narrowing_as_complete:
    must: partial coverage is marked partial with a named gap, never marked covered
    must_zh: 部分覆盖必须标 partial 并写明缺口，绝不标 covered
    anti_pattern: a single-point patch presented as full multi-dimensional handling / 用单点补丁冒充多维候选处理
  evidence_before_source:
    must: any tracked source change requires disposition_status, source_decision reason, and at least one judgment-replay case
    must_zh: 任何 tracked 改动都需处置状态、source_decision 理由和至少一个 judgment-replay 案例
    anti_pattern: change source first, backfill the reason; land a candidate with no replay / 先改源再补理由，或无回放就落源
  trace_is_asset:
    must: this round's evaluation, omissions acknowledged, and why the classification changed land as a trace in ignored .alphaX/process/
    must_zh: 本轮评估、承认的遗漏、分级变化原因，落在忽略层 .alphaX/process/
    anti_pattern: jump straight to output leaving no why / 直接跳到产物，不留为什么
  parking_honesty:
    must: covered points to real existing source evidence; otherwise mark partial or parked-with-reason
    must_zh: 标 covered 必须指向真实已有源证据，否则只能标 partial 或 parked
    anti_pattern: mark covered without a source pointer / 无源证据指针就标 covered
  data_boundary:
    must: tracked source carries no external article text, private facts, ignored process records, or local plugin/runtime asset paths
    must_zh: tracked 源不得含外部原文、私有事实、忽略层过程记录或本地插件/运行时资产路径
  reusable: these checks judge whether the judgment process is honest, traceable, and drift-resistant; any future catch round can apply them unchanged
  reusable_zh: 这些检查判断的是「判断过程是否诚实、可追溯、防漂移」，任何未来捕获轮都能原样套用

self_iteration_exit_gates:
  rule: stop on the first triggered gate; do not manufacture progress to keep the loop running
  rule_zh: 命中第一个触发的闸门就停；不得为维持循环而制造假进展
  hard_stop_owner_gate:
    when: change needs tracked source, external publication, or a risk operation
    when_zh: 要动 tracked 源、对外发布、或风险操作
    action: stop at owner review; report per candidate; do not self-advance
    action_zh: 停在 owner review，逐候选汇报，不自行推进
  convergence_stop:
    when: N consecutive rounds (default 3) with no new evidence, no new tracked change, and no new user instruction
    when_zh: 连续 N 轮（默认 3）无新证据、无新 tracked 变更、无新指令
    action: stop at owner review
    action_zh: 停在 owner review
    guard: lane switching (source-work / review / project) does not count as new progress
    guard_zh: 换车道（源工作 / 评审 / 项目）不算新进展
  diminishing_return_stop:
    when: a new round produces no disposition state transition versus the last round (no absent->partial, no partial->covered)
    when_zh: 新一轮处置状态相比上一轮无跃迁（无 absent→partial、无 partial→covered）
    action: stop and mark no_state_transition; hand the keep-or-stop decision to the owner
    action_zh: 停下并标记 no_state_transition，把继续或停止的决定交给 owner

workflow:
  - restate the input batch and its evidence boundary; exclude private or local data / 复述输入批次与证据边界，排除私有或本地数据
  - list every mechanism candidate identified from the batch / 列出批次里识别到的每个机制候选
  - for each candidate, assign disposition and status_reason, cite existing source evidence for covered, name the gap for partial/absent, and state the do_not_convert_boundary / 逐候选给出处置状态与理由，covered 引证据、partial/absent 写缺口、并写不应转成源机制的边界
  - run the six acceptance checks as the judgment trace; record omissions and narrowing corrections / 用六项验收检查作为判断 trace，记录遗漏与窄化纠正
  - evaluate the three exit gates before proposing any tracked change / 提任何 tracked 改动前先评三道退出闸门
  - for each source_decision=patch-candidate, require a judgment-replay case and owner gate before a tracked patch proceeds / 每个 source_decision=patch-candidate 都要有 judgment-replay 案例和 owner gate，tracked 补丁才可推进
  - land the ledger and trace via templates/source-work/insight-catcher.md; keep the trace in ignored .alphaX/process/ / 用模板落盘 ledger 与 trace，trace 放忽略层
  - state the completion boundary: what is proven versus what still needs an applied run / 写清完成边界：证明了什么、还需哪次实战

output_shape:
  use: templates/source-work/insight-catcher.md
  minimum:
    - input_batch with evidence boundary
    - candidate_mechanisms each with disposition_status, status_reason, and evidence_before_source
    - judgment_trace with the six checks and omissions
    - exit_gates evaluation
    - completion_boundary and one next action

alpha_partner_use:
  pairs_with: [source_work, source_review]
  compose:
    - if the real problem or objective is unclear, apply problem-decomposer first / 若真实问题或目标不清，先用 problem-decomposer
    - if the solution space is open, apply double-diamond-research to frame options / 若解空间开放，用 double-diamond-research 框定选项
    - use this skill to grade mechanism candidates before any source_decision=patch-candidate becomes a tracked source patch / 用本技能给机制候选分级，再让 source_decision=patch-candidate 转化为 tracked 源补丁前完成证据判断
  durable_memory_update: explicit user approval only / 仅在用户明确同意时更新持久记忆

proof_boundary:
  proves: creative inputs have explicit, traceable dispositions before source change
  proves_zh: 创意输入在改源前有显式、可追溯的处置状态
  does_not_prove: patch-candidate mechanisms improve real external project outcomes, or that each tracked patch is worth its maintenance cost
  does_not_prove_zh: 不证明 patch-candidate 机制改善真实外部项目结果，也不证明每个 tracked 补丁值得其维护成本
```
