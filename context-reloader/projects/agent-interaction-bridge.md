# Project Context: agent-interaction-bridge

## Project Identity

- project: `agent-interaction-bridge`
- local path: `{agent-interaction-bridge}`
- current branch observed: `codex/alphax-project-metadata`
- external source of truth:
  - `{agent-interaction-bridge}/AGENTS.md`
  - `{agent-interaction-bridge}/architecture/ai-contract-index.md`
  - `{agent-interaction-bridge}/architecture/contracts/*.yaml`
  - `{agent-interaction-bridge}/architecture/agentic-ontology.md`
  - `{agent-interaction-bridge}/architecture/sops/agentic-interaction-change.md`
  - live `git status`, project tests, and architecture checks

This Project Context belongs to `alpha-partner`. It is not a spec for `agent-interaction-bridge`.

## Why alphaX Tracks It

`agent-interaction-bridge` is the first report-first / interaction delivery engineering carrier for alphaX.

It is not just a sample repo. It tests whether alphaX can help a real external project while preserving source-of-truth boundaries, report-first behavior, L0-L2 versus L3-L4 ownership, and human-agent peer alignment.

The project is especially relevant because its product shape already includes human surfaces, bridge domain agent behavior, presentation planning, delivery quality, Feishu/Lark report surfaces, and `project_progress_report`-style output.

## Human Judgment Context

- Loop reports matter more than default execution.
- Boris-style background agents are useful because they report into a human attention surface; alphaX should borrow the report-first mechanism, not the agent-count or automation aesthetics.
- For this project, alphaX should first produce WIP closure, source drift, and next-action reports before modifying code.
- Any accepted insight must be translated into the external project's own contracts, architecture docs, tests, changelog, or implementation after user confirmation.

## alphaX Observations

- 2026-06-07 cold start reconstructed Product Runtime and Build-Time Governance boundaries and identified Dynamic UI routing in `InteractionIntent` as wrong-layer work.
- 2026-06-07 `presentation.rendering` checkpoint compressed the Dynamic UI gap into a narrow responsibility migration toward `ExpressionProfile` and `PresentationPlan`.
- 2026-06-07 project-local pointer was adopted in the external project `AGENTS.md` after repeated alphaX use.
- 2026-06-07 daily radar observed alphaX-driven Runtime Services separation WIP on `codex/extract-runtime-services` and upgraded the risk from pointer-only drift to broader closure risk.
- 2026-06-08 Runtime Services separation closed and merged to `main` (bridge PR #8 `e64bba0`, runtime-services PR #1 `d20a334`); bridge no longer owns model/resource/storage, adapter consumes Runtime Services as status source.
- 2026-06-08 project-local re-entry converted to alphaX-injected `.alphaX/` metadata, merged to `main`; `.alphaX/` is ignored local injected metadata, not versioned project fact.
- 2026-06-08 closure pass verified the Runtime Services separation WIP as alphaX-driven work, not uncontrolled external WIP.
- 2026-06-08 boundary fixes made `delivery-support` default through `runtime-services-adapter`, made adapter resources come from `services.resources.status()`, made `resources` and `doctor` use Runtime Services live resource status, and downgraded `models smoke` to a resource-status proxy without model/vector/artifact side effects.
- 2026-06-08 evidence: `agent-interaction-bridge` passed `pnpm test` (65 files, 228 tests), `pnpm typecheck`, `pnpm build`, `architecture check`, `architecture contracts`, `resources`, `models smoke`, `doctor`, `npm pack --dry-run`, and `git diff --check`; `agent-runtime-services` passed `pnpm test` (2 files, 6 tests), `pnpm typecheck`, `pnpm build`, and `git diff --check`.
- 2026-06-08 human update: `agent-runtime-services` is being optimized and handled by other sessions. Current alphaX thread should not treat the sibling package as its main blocker; it should continue closing the bridge-side consumer boundary and record the dependency as parallel context.
- 2026-06-08 bridge-side closure commit: `ec8f643 Extract Runtime Services consumer boundary` on `codex/extract-runtime-services`.
- 2026-06-08 dependency stabilization: `agent-runtime-services` is committed at `f50fa16 Initialize runtime services package` on `codex/initial-runtime-services`; Runtime Services passed `pnpm test`, `pnpm typecheck`, `pnpm build`, and `npm pack --dry-run --json` with `dist/index.d.ts` included.
- 2026-06-08 bridge re-verification against `agent-runtime-services@f50fa16`: `agent-interaction-bridge` passed `pnpm test` (65 files, 228 tests), `pnpm typecheck`, `pnpm build`, `architecture check`, `architecture contracts`, and `npm pack --dry-run --json` with `dist/index.d.ts` included.
- 2026-06-08 remote closure: `agent-runtime-services` PR #1 merged to `main` as `d20a334`; `agent-interaction-bridge` PR #8 merged to `main` as `e64bba0`.
- 2026-06-08 project-local alphaX metadata injection: external project branch `codex/alphax-project-metadata` is clean and pushed. Commits: `781db8e Document optional alphaX project metadata` updates `AGENTS.md`; `55de257 Ignore alphaX local metadata` ignores `.alphaX/`. The actual `.alphaX/` files remain local injected metadata, not versioned project facts.

## Feedback Context

Feedback is context input, not a control surface.

Retained signals from review-agent feedback:

- same-day or same-period evidence is not enough to prove that alphaX lowers project re-entry cost;
- scaffolding-to-use ratio should stay visible;
- workspace staleness matters because old context can become a risk source;
- the next strong test is cross-day reuse against this project's Runtime Services separation WIP;
- report-first loops should prove value before scheduling, push, or automation.

Retained signals from 2026-06-08 Runtime Services closure review:

- adapter resource status must not create a false green light from bridge-local config when RPC is healthy;
- bridge `models smoke` should not own model-call, vector-upsert, or artifact-save orchestration;
- `resources` and `doctor` should report Runtime Services live status, not a bridge-local approximation;
- storage and resource wording should say Runtime Services home when that is the asset owner.
- bridge docs should refer to `../agent-runtime-services` or package boundaries, not a user-local absolute path.

These are risk signals and open questions. They do not authorize alphaX to change this external project or the alphaX contract by themselves.

## Unverified Claims

- `unverified_claim`: alphaX lowers human project re-entry cost on this project.
- `unverified_claim`: structured handoff plus Project Context reduces reload time better than reading the repo from scratch.
- `unverified_claim`: report-first output will produce better project decisions than direct code execution across repeated WIPs.
- `unverified_claim`: a real long-running Runtime Services RPC process and the bridge CLI are end-to-end consistent beyond the local RPC tests.

## Reload Recipe

When alphaX is asked to re-enter `agent-interaction-bridge`:

1. Read this Project Context.
2. Read the external project `AGENTS.md`.
3. Run read-only `git status --short --branch` in the external project.
4. Inspect `.alphaX/`, `architecture/ai-contract-index.md`, relevant YAML contracts, and current branch/diff.
5. Compare live source of truth against this Project Context.
6. Report stale context, unverified claims, WIP scope, source drift, closure risks, and one recommended next action.
7. Continue execution only after the report names the minimal safe closure path.

## Default Output

Default to report-first:

- WIP closure report;
- source drift report;
- contract boundary report;
- next-action recommendation;
- explicit list of what not to do now.

Do not default to code edits, refactors, test rewrites, PR repair, or automatic project write-back.

## Write-Back Boundary

No auto write-back.

Context from this file can influence the external project only after Lizhaohua confirms the judgment. Confirmed content must be rewritten into the external project's own language and location: specs, contracts, architecture docs, tests, changelog, code, or review notes.

This Project Context must not become a hidden source of truth for `agent-interaction-bridge`.

## Freshness

- last_reloaded: 2026-06-08
- last_aligned_with_user: 2026-06-08
- confidence: medium-high
- staleness risk: high if used without re-reading live `agent-interaction-bridge` status and checking whether `.alphaX/` has been reinjected locally
