# Pilot: presentation.rendering Focused Spec Checkpoint

Date: 2026-06-07 | Surface: `/Users/lizhaohua/work/llm/agent-interaction-bridge`

Scope: `presentation.rendering` contract and Dynamic UI responsibility placement.

Source of truth inspected: `architecture/contracts/presentation-rendering.yaml`, `architecture/ai-contract-index.md`, `architecture/sops/agentic-interaction-change.md`, `architecture/system-design.md`, `architecture/agentic-ontology.md`, plus 9 source/test files in `src/`.

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

- `presentation.rendering` L2 invariant: Dynamic UI belongs to `ExpressionProfile`/`PresentationPlan`; `InteractionIntent` must not own visual routing.
- `ai-contract-index.md` marks `presentation.rendering` as `partial` with named gap: Dynamic UI still needs migration.
- Current `src/interaction/intent.ts` still owns Dynamic UI through `shouldUseDynamicUi`, `dynamicUiTaskIntent`, `presentation.source = dynamic_ui_heuristic`.
- `src/bot/reply-mode-policy.ts` routes Dynamic UI from `InteractionIntent`.
- `src/signal/reply-presentation.ts` already has reusable layout generation.

Validation: test suite passed: 72 files, 250 tests; architecture check passed; working tree clean.

## Recommendation

Smallest useful slice (user-confirmed only):
1. Add expression/presentation planning carrier separate from `InteractionIntent`.
2. Move Dynamic UI heuristic ownership out of `src/interaction/intent.ts`.
3. Keep presentation feedback as feedback in `InteractionIntent`, lower card/visual choice through new carrier.
4. Keep `presentAnswerCard` and card renderer mostly unchanged.
5. Update tests to prove routing no longer lives in intent.
6. Keep AI Contract Index `partial` until migration has implementation + harness evidence.
