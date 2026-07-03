---
name: "insight-catcher"
description: "创意捕手 / Insight Catcher. Use when external content, ideas, research signals, talks, notes, or creative inputs should be captured, graded, and turned into disposition-tracked alphaX mechanism candidates before any tracked source change. 当外部内容、想法、研究信号、分享、笔记或创意输入需要先捕获、分级并转成 alphaX 机制候选时使用。"
---

# 创意捕手

Insight Catcher decomposes creative inputs into reusable mechanism candidates,
grades their disposition and vision value, then lands only vision-aligned keeps —
before any tracked source change.

创意捕手把创意输入**拆解**成可迁移机制候选，**处置分级**并做**价值对齐**，
最后只**落地**对齐 alphaX 愿景的保留项——且都在改源之前。

## 关键点（中文速览）

```text
一句话目标：外部内容、想法、研究信号或创意输入进来，第一产出是「带处置状态 + 价值对齐的候选 ledger + 判断 trace」，不是源码补丁。

四步主链路（拆解 → 处置分级 → 价值对齐 → 落地）：
1. 拆解：把一条输入切成原子的、可迁移的机制候选；切不动就先用 problem-decomposer，别拿原始输入直接打分。
2. 处置分级：逐候选落到唯一处置状态 covered/partial/absent/parked-with-reason，covered 引真实源证据；park/no-change 是一等结果，不是失败。
3. 价值对齐：想进 patch-candidate 的候选，必须对齐至少一条 alphaX 愿景信号（intelligence-ceiling 或 half-life），据此按 SOP 的 source_value_tiers 判据给 source_value；对不齐愿景的一律 park 或 no-change。
4. 落地：每个保留决定命名目标源层 + 最小源面，防落错层；再要 judgment-replay 案例才允许 tracked 补丁。

权威定义：验收标准、价值门、落地规则、退出闸门的权威定义在
alphaX/source-work/intelligence-ceiling-half-life.md 的 insight_catcher 块；
本 skill 只做「拆解方法 + 工作流 + 触发 + 引用」，不复制权威细节，避免半衰期双改。

三大质量目标：
- 价值判断可靠性：没有愿景信号对齐的候选不得冒充「值得进入 patch-candidate」。
- 开发质量可靠性：keep 必须落到正确源层的最小源面，且有回放背书。
- 防漂移：无静默丢失、不以窄充全、先证据后改源、搁置要诚实、trace 即资产、守数据边界。
```

```yaml
skill: insight-catcher
canonical_names: [insight-catcher, 创意捕手]
purpose: decompose creative inputs into mechanism candidates, grade disposition and vision value, and land only vision-aligned keeps before any tracked source change
purpose_zh: 把创意输入拆解为机制候选，做处置与价值分级，只把对齐愿景的保留项落到正确源层，再决定是否改源
first_deliverable: templates/source-work/insight-catcher.md
authority:
  canonical_contract: alphaX/source-work/intelligence-ceiling-half-life.md insight_catcher block
  rule: this skill carries the decompose method, workflow, triggers, and quick-view only; acceptance checks, vision_value_gate, landing_rule, and exit gates are defined authoritatively in the SOP and referenced here, not duplicated
  rule_zh: 本 skill 只承载拆解方法、工作流、触发与速览；验收检查、价值门、落地规则、退出闸门的权威定义在 SOP，本处只引用不复制
not:
  - a source patch generator / 不是补丁生成器
  - a summary of the input batch / 不是输入内容摘要
  - a durable memory updater / 不是持久记忆更新器
  - a way to justify a change already decided / 不是为已决定的改动补理由

scope: source work
boundary:
  - candidate and source decouple: record reusable mechanism candidates, never copy external article facts or private data into tracked source
  - 候选与来源解耦：只记录可迁移机制候选，绝不把外部原文或私有数据抄进 tracked 源
  - the ledger and its judgment trace are the asset; a tracked patch is only a downstream candidate after source_decision=patch-candidate, vision-value alignment, and replay support
  - ledger 与判断 trace 才是资产；tracked 补丁只是 source_decision=patch-candidate、对齐愿景且有 replay 支撑后的下游候选产物
  - live source wins; existing coverage must be cited, not assumed
  - live source 优先；已覆盖必须引用真实证据，不能假设

when_to_use:
  - user brings external content, research, talks, notes, or ideas for alphaX evaluation / 用户带来外部内容、研究、分享、笔记或想法要评估
  - user asks whether an idea should become an alphaX mechanism candidate / 用户问某个想法是否应成为 alphaX 机制候选
  - user asks what to keep, narrow, or park from a batch of creative inputs / 用户问一批创意输入里哪些推进、收窄、搁置
  - a source-work round risks narrowing many candidates into one convenient patch / 一轮源工作有把多候选窄化成单补丁的风险
  - before opening a tracked source diff triggered by creative inputs / 在因创意输入动 tracked diff 之前

core_objective:
  statement: evolve alphaX by decompose, disposition-grade, value-align, and land, not by per-item source patching
  statement_zh: 用「拆解 → 处置分级 → 价值对齐 → 落地」推进 alphaX，而不是逐条给源打补丁
  first_output_rule: the first deliverable is a disposition-tracked, vision-value-aligned candidate ledger plus judgment trace, never a source patch
  first_output_rule_zh: 第一产出永远是「带处置状态 + 价值对齐的候选 ledger + 判断 trace」，绝不是源码补丁
  disposition_states: [covered, partial, absent, parked-with-reason]
  disposition_states_zh: [已覆盖, 部分, 缺席, 带理由搁置]
  invariant: every mechanism candidate resolves to exactly one disposition_status; a tracked patch is only a downstream candidate after source_decision=patch-candidate, vision-value alignment, and replay support
  invariant_zh: 每个机制候选只落到唯一 disposition_status；tracked 补丁只是 patch-candidate、对齐愿景且有 replay 支撑后的下游候选产物
  generalization: constrains the shape of judgment, independent of how many candidates or input items exist this round
  generalization_zh: 约束的是判断的形状，与本轮候选或输入条目多少无关

decompose_method:
  goal: turn a raw external input into atomic, reusable mechanism candidates before any grading
  goal_zh: 打分前先把原始外部输入切成原子的、可迁移的机制候选
  steps:
    - restate the input and its evidence boundary; exclude private or local data / 复述输入与证据边界，排除私有或本地数据
    - separate the transferable mechanism from the source-specific story, product, or anecdote / 把可迁移机制与来源特定的故事、产品、轶事分开
    - split a bundled idea into one candidate per distinct mechanism; do not merge distinct mechanisms into one convenient candidate / 把捆绑的想法按不同机制拆成多个候选，不把多机制并成一个方便候选
    - if a candidate is not yet a transferable mechanism, apply problem-decomposer to reach the real mechanism instead of grading the raw input / 若某候选还不是可迁移机制，先用 problem-decomposer 找到真机制，别拿原始输入打分
  authority_note: the no_silent_loss and no_narrowing_as_complete checks that police this step are defined in the SOP insight_catcher block
  authority_note_zh: 约束本步的 no_silent_loss 与 no_narrowing_as_complete 检查，权威定义在 SOP insight_catcher 块

acceptance_criteria:
  canonical: alphaX/source-work/intelligence-ceiling-half-life.md insight_catcher block
  note: names only; each check's must/anti-pattern is defined authoritatively in the SOP and applied unchanged
  note_zh: 此处只列名称；每项的 must/反模式权威定义在 SOP，原样套用
  checks:
    - no_silent_loss / 无静默丢失：每个候选都要有显式处置状态
    - no_narrowing_as_complete / 不以窄充全：部分覆盖标 partial 写缺口，绝不标 covered
    - evidence_before_source / 先证据后改源：任何 tracked 改动需处置状态 + source_decision 理由 + 价值对齐 + 至少一个 replay 案例
    - trace_is_asset / trace 即资产：评估、遗漏、分级变化原因落在忽略层 .alphaX/process/
    - parking_honesty / 搁置要诚实：标 covered 必须指向真实源证据，否则 partial 或 parked
    - data_boundary / 数据边界：tracked 源不得含外部原文、私有事实、忽略层过程记录或本地插件/运行时资产路径
    - vision_value_alignment / 价值对齐：patch-candidate 必须对齐至少一条 intelligence_ceiling_signals 或 half_life_signals，据此给 source_value；对不齐愿景的候选不得进 patch-candidate
  reusable: these checks judge whether the judgment process is honest, traceable, drift-resistant, and vision-aligned; any future catch round applies them unchanged
  reusable_zh: 这些检查判断「判断过程是否诚实、可追溯、防漂移、对齐愿景」，任何未来捕获轮都能原样套用

vision_value_gate:
  canonical: alphaX/source-work/intelligence-ceiling-half-life.md insight_catcher.vision_value_gate
  rule: a candidate may become source_decision=patch-candidate only if it aligns to at least one intelligence_ceiling_signals or half_life_signals entry; record source_value high|medium|low from that alignment
  rule_zh: 候选只有对齐至少一条 intelligence-ceiling 或 half-life 愿景信号才可成为 patch-candidate；据此给 source_value 高|中|低
  source_value_tiers: grade source_value by the SOP insight_catcher.vision_value_gate.source_value_tiers rubric; do not re-expand the tier definitions here
  source_value_tiers_zh: 用 SOP insight_catcher.vision_value_gate.source_value_tiers 判据给 source_value；此处不复述分级细则
  signal_source: reuse the intelligence_ceiling_signals and half_life_signals lists in the SOP; do not create a parallel signal list
  signal_source_zh: 复用 SOP 里的 intelligence_ceiling_signals 与 half_life_signals 清单，不新造平行清单
  no_alignment_action: park or mark no-change; a candidate aligned to no vision signal must not be presented as worth becoming a patch-candidate
  no_alignment_action_zh: 不对齐则 park 或 no-change；对不齐愿景的候选不得冒充「值得进入 patch-candidate」

landing_rule:
  canonical: alphaX/source-work/intelligence-ceiling-half-life.md insight_catcher.landing_rule
  rule: every keep names the target source layer and the smallest source surface before a tracked patch
  rule_zh: 每个保留决定在动 tracked 补丁前，命名目标源层与最小源面
  source_layers:
    [
      core_principles,
      cognitive_frameworks,
      operational_scaffolding,
      implementation_carriers,
    ]
  guard: do not land a durable rule on the wrong layer; core stays thinner and harder than scaffolding
  guard_zh: 别把持久规则落在错误层；core 要比 scaffolding 更薄更硬

self_iteration_exit_gates:
  canonical: alphaX/source-work/intelligence-ceiling-half-life.md insight_catcher.exit_gates
  rule: stop on the first triggered gate; do not manufacture progress to keep the loop running; gate details are defined authoritatively in the SOP
  rule_zh: 命中第一个触发的闸门就停；不得为维持循环制造假进展；闸门细节权威定义在 SOP
  hard_stop_owner_gate:
    when: change needs tracked source, external publication, or a risk operation
    action: stop at owner review; report per candidate; do not self-advance
  convergence_stop:
    when: N consecutive rounds (default 3) with no new evidence, no new tracked change, and no new user instruction
    action: stop at owner review; lane switching does not count as new progress
  diminishing_return_stop:
    when: a new round produces no disposition state transition versus the last round
    action: stop and mark no_state_transition; hand the keep-or-stop decision to the owner

workflow:
  - decompose: restate the input batch and evidence boundary; split it into atomic mechanism candidates; apply problem-decomposer when a candidate is not yet a transferable mechanism / 拆解：复述输入与证据边界，切成原子机制候选，切不动时用 problem-decomposer
  - disposition-grade: for each candidate assign disposition and status_reason; cite existing source evidence for covered; name the gap for partial/absent; state the do_not_convert_boundary; park or no-change is a first-class result / 处置分级：逐候选给处置状态与理由，covered 引证据、partial/absent 写缺口、写不该转成源机制的边界，park/no-change 是一等结果
  - value-align: for each candidate proposed as patch-candidate, name the aligned intelligence_ceiling_signals or half_life_signals entry and set source_value; park or mark no-change when no vision signal aligns / 价值对齐：拟 patch-candidate 的候选命名对齐的愿景信号并设 source_value；对不齐则 park 或 no-change
  - land: for each keep, name the target source layer and smallest source surface before any tracked patch / 落地：每个保留决定命名目标源层与最小源面，再谈 tracked 补丁
  - run the acceptance checks (SOP-defined) as the judgment trace; record omissions and narrowing corrections / 用 SOP 定义的验收检查作为判断 trace，记录遗漏与窄化纠正
  - evaluate the three exit gates before proposing any tracked change / 提任何 tracked 改动前先评三道退出闸门
  - for each source_decision=patch-candidate, require a judgment-replay case and owner gate before a tracked patch proceeds / 每个 patch-candidate 都要有 judgment-replay 案例和 owner gate，tracked 补丁才可推进
  - land the ledger and trace via templates/source-work/insight-catcher.md; keep the trace in ignored .alphaX/process/; state the completion boundary: what is proven versus what still needs an applied run / 用模板落盘 ledger 与 trace，trace 放忽略层；写清完成边界：证明了什么、还需哪次实战

output_shape:
  use: templates/source-work/insight-catcher.md
  minimum:
    - input_batch with evidence boundary
    - candidate_mechanisms each with disposition_status, status_reason, vision_value_alignment, landing_layer, and evidence_before_source
    - judgment_trace with the acceptance checks and omissions
    - exit_gates evaluation
    - completion_boundary and one next action

alpha_partner_use:
  pairs_with: [source_work, source_review]
  compose:
    - if a candidate is not yet a transferable mechanism or the real problem is unclear, apply problem-decomposer first / 若候选还不是可迁移机制或真实问题不清，先用 problem-decomposer
    - if the solution space is open, apply double-diamond-research to frame options / 若解空间开放，用 double-diamond-research 框定选项
    - use this skill to decompose, grade, and value-align mechanism candidates before any patch-candidate becomes a tracked source patch / 用本技能拆解、分级并价值对齐机制候选，再让 patch-candidate 转成 tracked 源补丁前完成证据判断
  durable_memory_update: explicit user approval only / 仅在用户明确同意时更新持久记忆

proof_boundary:
  proves: creative inputs are decomposed into candidates with explicit, traceable dispositions and named vision-value alignment before source change
  proves_zh: 创意输入在改源前被拆解为候选，且有显式、可追溯的处置状态与命名的愿景价值对齐
  does_not_prove: a vision-aligned keep actually advances the intelligence ceiling or asset half-life, that patch-candidate mechanisms improve real external project outcomes, or that each tracked patch is worth its maintenance cost — those need an applied run
  does_not_prove_zh: 不证明对齐愿景的保留项真的抬升了智能上限或半衰期，也不证明 patch-candidate 机制改善真实外部项目结果或每个补丁值回维护成本——这些需要 applied run
```
