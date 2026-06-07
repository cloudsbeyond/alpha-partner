# Pilot: online_community Session Runtime Cold Start

Date: 2026-06-07 | Surface: `/Users/lizhaohua/work/llm/clouds-beyond/online_community`

Trigger: `alphaX 介入一下 /Users/lizhaohua/work/llm/clouds-beyond/online_community。先自主对齐 session runtime 的 source of truth 和验收链路，不改文件，指出当前最值得验证的 P0 风险。`

## Result

P0: `online_community` is an AI-native real-time collaboration and decision-navigation product; active P0 is turning the old Work Buddy text CLI prototype into a reusable `SessionRuntime` with evidence refs, draft confirmation boundaries, signal routing, and manual acceptance review. Branch: `codex/session-runtime-acceptance-report`. No project-local pointer.

Source of truth inspected: `AGENTS.md`, `README.md`, `backend/AGENTS.md`, `backend/README.md`, `specs/session-runtime-v1/` (spec.md, tdd-assets.md), `backend/src/session_runtime/` (runtime.py, contracts.py, acceptance.py), `backend/tests/test_session_runtime_acceptance.py`, `scripts/check_backend.sh`.

## Boundaries

- Human/architect owns L0-L2: problem definition, structured expression, contract source, freeze signal, stop condition.
- Agent owns L3-L4 under frozen contract: `backend/src/session_runtime/`, schema snapshot, CLI output, acceptance report, tests.
- Runtime output is draft by default; `NavigationSignal`, `Decision`, `ActionItem`, `VerificationEvent` must not be AI-confirmed.
- Manual acceptance report is a review packet, not proof of real-scene quality.
- Report privacy: may include evidence refs and checklist, but must not embed raw transcript content.

## P0 Risk: False Completion

Automated tests, CLI smoke, schema snapshot, and guardrail checks prove structure, traceability, draft status, and transcript privacy. They cannot prove navigation signals are actionable in a real discussion or that interruption timing improves collaboration. Real internal discussion manual review remains incomplete by project contract.

## Evidence

Backend baseline check passed (18 tests); targeted session runtime tests passed (11 tests); `compileall` passed; concept registry check passed; architecture convergence check passed; guardrail cases passed; CLI acceptance-report smoke passed; report did not contain sample transcript lines; working tree clean.

## Value

alphaX reconstructed the active source chain without asking user to restate project state. Preserved the difference between structural verification and real discussion quality. Identified the product-relevant risk: manual acceptance is still the real next gate, not more backend harness expansion.

## Next

Manual-acceptance planning checkpoint: choose one real internal discussion transcript outside git, generate local acceptance report under ignored storage, review signals/actionability/interruption/draft boundaries, record only non-sensitive summary.
