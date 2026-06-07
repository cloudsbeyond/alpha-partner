# Pilot: agent-interaction-bridge Cold Start

Date: 2026-06-07

Surface:

- `/Users/lizhaohua/work/llm/agent-interaction-bridge`

Trigger tested:

```text
alphaX 介入一下 /Users/lizhaohua/work/llm/agent-interaction-bridge。
先只做 cold start，不改文件。
```

## Cold-Start Result

Inferred P0 main line:

- Agent-Interaction-Bridge is a local-first bounded interaction agent that separates human surfaces, bridge-domain mediation, execution agents, presentation/delivery, resources, state, and authority.

Primary loop:

- Project loop with thinking-loop support.

Current branch:

- `codex/product-runtime-build-governance`

Project-local partner pointer:

- Not present in root `AGENTS.md`; this is useful for testing whether alphaX can reconstruct context without a local pointer.

## Source Of Truth Inspected

- `AGENTS.md`
- `README.md`
- `architecture/README.md`
- `architecture/requirements-to-code-chain.md`
- `architecture/ai-contract-index.md`
- `architecture/sops/agentic-interaction-change.md`
- `architecture/contracts/*.yaml`
- `package.json`
- `src/architecture/contract-check.test.ts`
- `src/architecture/contract-registry.test.ts`
- `src/cli/commands/architecture.test.ts`

## Inferred Boundaries

- Product Runtime: Bridge Domain Agent mediates `HumanTurn`, `SurfaceContext`, `InteractionIntent`, `ExpressionProfile`, `PresentationPlan`, `DeliveryPlan`, `Carrier`, `AgentTask`, and `AgentSignal`.
- Build-Time Governance: Build Agent owns L3-L4 implementation, contracts, SOPs, tests, and evidence under human-owned frozen L0-L2.
- Runtime helper models may support perception, expression, retrieval, artifact generation, and quality evaluation, but must not approve risk, choose tools, mutate cwd/session/profile, or override endpoint configuration.
- Durable implementation must pass the gate: frozen L0-L2, durable L3-L4, freeze signal, AI Contract Index, and harness evidence.

## Current Risks

- All eight architecture contracts are `partial` at the contract-summary level, even though their L0-L2 records are frozen and L3-L4 mode is durable. AlphaX must not treat passing tests as full completion.
- `presentation.rendering` still has a named gap: Dynamic UI and explicit visual-structure feedback should move from intent/reply policy into `ExpressionProfile` and `PresentationPlan`.
- `resources.architecture` still has a named gap: `CapabilityCatalog` should sit above `ResourceCatalog` and keep resource/state gates explicit.
- `interaction.hitl`, `operator.commands`, and `runtime.data` are critical or authority-sensitive surfaces; durable changes there need explicit review discipline.

## Verification Evidence

Commands run from `/Users/lizhaohua/work/llm/agent-interaction-bridge`:

```bash
pnpm exec vitest run src/architecture/contract-check.test.ts src/architecture/contract-registry.test.ts src/cli/commands/architecture.test.ts
pnpm typecheck
node ./bin/agent-interaction-bridge.mjs architecture contracts
git status --short
```

Observed results:

- architecture contract tests passed: 3 files, 17 tests;
- typecheck passed;
- architecture contracts CLI listed all eight contracts as `partial`, with frozen/frozen/frozen L0-L2 and durable L3/L4;
- working tree remained clean.

## Partner Value Observed

- alphaX reconstructed the project P0 and current contract state without asking the user to restate context.
- The pilot identified source-of-truth files, current gaps, authority-sensitive surfaces, and verification commands from live project files.
- The result stayed in cold-start and verification mode instead of prematurely proposing implementation.

## Recommended Next Move

Run a focused Spec Checkpoint on `presentation.rendering`:

- decide whether the next real change should target the Dynamic UI migration into `ExpressionProfile` and `PresentationPlan`;
- if yes, inspect `architecture/contracts/presentation-rendering.yaml`, `src/runtime/interaction-runtime.ts`, `src/interaction/intent.ts`, `src/bot/reply-mode-policy.ts`, and `src/signal/reply-presentation.ts`;
- only preserve implementation after the contract gap, harness target, and AI Contract Index row are aligned.
