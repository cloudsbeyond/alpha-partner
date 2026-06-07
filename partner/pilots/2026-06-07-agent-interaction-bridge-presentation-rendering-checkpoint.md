# Pilot: presentation.rendering Focused Spec Checkpoint

Date: 2026-06-07

Surface:

- `/Users/lizhaohua/work/llm/agent-interaction-bridge`

Scope:

- `presentation.rendering` contract and Dynamic UI responsibility placement.

## Source Of Truth Inspected

- `architecture/contracts/presentation-rendering.yaml`
- `architecture/ai-contract-index.md`
- `architecture/sops/agentic-interaction-change.md`
- `architecture/system-design.md`
- `architecture/agentic-ontology.md`
- `src/runtime/interaction-runtime.ts`
- `src/interaction/intent.ts`
- `src/bot/reply-mode-policy.ts`
- `src/signal/reply-presentation.ts`
- `src/signal/presentation.ts`
- `src/presentation/document.ts`
- `src/interaction/intent.test.ts`
- `src/bot/reply-mode-policy.test.ts`
- `src/signal/reply-presentation.test.ts`

## Spec Checkpoint

```text
P0 主链路：
把 Dynamic UI 从 InteractionIntent 的视觉 routing 债务迁到 ExpressionProfile / PresentationPlan，同时保留当前可用的 Feishu/Lark 卡片化展示和安全降级。

本轮剪枝：
- 不重写 Feishu card renderer；renderer 当前只是 carrier lowering，已有测试覆盖。
- 不扩大到 CapabilityCatalog / ResourceCatalog；那是 resources.architecture 的独立 gap。
- 不把所有 presentation feedback 都强制成卡片；通用可读性批评仍保持 chat-native text。
- 不改变 AgentTask、endpoint profile、approval、cwd/session 或 helper-model authority。

保留但后置：
- ActionLog 对 presentation decision 的记录，等职责迁移完成后再接入。
- helper model typed proposal 的表达规划，等 deterministic ExpressionProfile / PresentationPlan carrier 稳定后再评估。
- 真实 Feishu smoke test，等代码改造后再做端到端验证。

待确认：
- 下一轮是否只做一个最小迁移：新增 ExpressionProfile / PresentationPlan carrier，先让 Dynamic UI selection 不再由 InteractionIntent 拥有。
- AI Contract Index 是否继续保持 presentation.rendering 为 partial，直到 Dynamic UI migration 有实现和 harness evidence。
```

## Evidence

Observed from source:

- `presentation.rendering` L2 invariant says Dynamic UI belongs to `ExpressionProfile` and `PresentationPlan`; `InteractionIntent` may record presentation feedback but must not own visual routing.
- `architecture/ai-contract-index.md` marks `presentation.rendering` as `partial` with the named gap: Dynamic UI still needs migration into `ExpressionProfile` and `PresentationPlan`.
- Current `src/interaction/intent.ts` still owns Dynamic UI classification through `shouldUseDynamicUi`, `dynamicUiTaskIntent`, and `presentation.source = dynamic_ui_heuristic`.
- Current `src/bot/reply-mode-policy.ts` routes Dynamic UI task requests to card reply mode from `InteractionIntent`.
- Current `src/signal/reply-presentation.ts` already has reusable layout generation for architecture, report, comparison, and visual cards.

## Validation Run

Commands run from `/Users/lizhaohua/work/llm/agent-interaction-bridge`:

```bash
pnpm test -- src/interaction/intent.test.ts src/interaction/model-judge.test.ts src/bot/prompt-plan.test.ts src/bot/reply-mode-policy.test.ts src/signal/reply-presentation.test.ts src/signal/delivery-support-executor.test.ts src/signal/feishu-delivery-support.test.ts src/bot/feishu-signal-delivery.test.ts src/card/presentation-card.test.ts src/card/chat-presentation-contract.test.ts src/card/text-renderer.test.ts src/card/interaction-card.test.ts src/presentation/document.test.ts src/presentation/capabilities.test.ts src/presentation/templates.test.ts src/presentation/renderers/feishu-card.test.ts src/presentation/renderers/html.test.ts src/presentation/renderers/markdown.test.ts src/signal/feishu-renderer.test.ts
node ./bin/agent-interaction-bridge.mjs architecture check
git status --short
```

Observed results:

- test suite passed: 72 files, 250 tests;
- architecture contract check passed;
- target project working tree remained clean.

## Recommendation

Proceed only if the user wants a real project change next.

The smallest useful implementation slice would be:

1. Add a small expression/presentation planning carrier that can represent Dynamic UI selection separately from `InteractionIntent`.
2. Move Dynamic UI heuristic ownership out of `src/interaction/intent.ts`.
3. Keep explicit presentation feedback as feedback meaning in `InteractionIntent`, but lower card/visual choice through the new planning carrier.
4. Keep `presentAnswerCard` and card renderer mostly unchanged.
5. Update tests so the contract proves routing no longer lives in intent while current card behavior remains stable.
6. Keep AI Contract Index status `partial` until the migration has implementation, harness evidence, and architecture check evidence.
