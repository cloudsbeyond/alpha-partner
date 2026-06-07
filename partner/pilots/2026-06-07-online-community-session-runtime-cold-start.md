# Pilot: online_community Session Runtime Cold Start

Date: 2026-06-07

Surface:

- `/Users/lizhaohua/work/llm/clouds-beyond/online_community`

Trigger tested:

```text
alphaX 介入一下 /Users/lizhaohua/work/llm/clouds-beyond/online_community。
先自主对齐 session runtime 的 source of truth 和验收链路，不改文件，指出当前最值得验证的 P0 风险。
```

## Cold-Start Result

Inferred P0 main line:

- `online_community` is an AI-native real-time collaboration and decision-navigation product; the active P0 is turning the old Work Buddy text CLI prototype into a reusable `SessionRuntime` with evidence refs, draft confirmation boundaries, signal routing, and manual acceptance review.

Primary loop:

- Project loop with governance and acceptance-check support.

Current branch:

- `codex/session-runtime-acceptance-report`

Project-local partner pointer:

- Not present in root `AGENTS.md`; this remains useful for testing alphaX context reconstruction without a local pointer.

## Source Of Truth Inspected

- `AGENTS.md`
- `README.md`
- `backend/AGENTS.md`
- `backend/README.md`
- `specs/session-runtime-v1/spec.md`
- `specs/session-runtime-v1/tdd-assets.md`
- `backend/src/session_runtime/runtime.py`
- `backend/src/session_runtime/contracts.py`
- `backend/src/session_runtime/acceptance.py`
- `backend/tests/test_session_runtime_acceptance.py`
- `scripts/check_backend.sh`

## Inferred Boundaries

- Human/architect owns L0-L2: problem definition, structured expression, contract source, freeze signal, and stop condition.
- Agent owns L3-L4 only under frozen contract: `backend/src/session_runtime/`, schema snapshot, CLI output, acceptance report, and tests.
- Runtime output is draft by default; `NavigationSignal`, `Decision`, `ActionItem`, and `VerificationEvent` must not be AI-confirmed.
- Manual acceptance report is a review packet, not proof of real-scene quality.
- Report privacy boundary: acceptance report may include evidence refs and checklist, but must not embed raw transcript content.

## Current P0 Risk

The strongest current risk is not backend structure. It is false completion:

- automated tests, CLI smoke, schema snapshot, and guardrail checks can prove structure, traceability, draft status, and transcript privacy;
- they cannot prove that navigation signals are actionable in a real internal discussion or that interruption timing improves collaboration;
- real internal discussion manual review remains incomplete by project contract.

## Verification Evidence

Commands run:

From `/Users/lizhaohua/work/llm/clouds-beyond/online_community/backend`:

```bash
bash ../scripts/check_backend.sh
PYTHONPATH=src python3 -m unittest tests.test_session_runtime_acceptance tests.test_session_runtime tests.test_session_runtime_cli
python3 -m compileall src
PYTHONPATH=src python3 -m session_runtime.cli --session-id "session:demo" --profile "work_buddy_internal_session" --organization-id "organization:cloudsbeyond" --participant-unit-id "unit:liz" --transcript-file examples/sample_session.txt --source-ref "transcript:sample" --acceptance-report /tmp/alphax-online-community-acceptance-report.md
```

From `/Users/lizhaohua/work/llm/clouds-beyond`:

```bash
python3 scripts/concept_registry_check.py --scope online_community
python3 scripts/architecture_convergence_check.py --month 2026-05
python3 scripts/test_guardrail_cases.py --config online_community/architecture/guardrails/guardrail_cases.json
```

Observed results:

- backend baseline check passed: 18 tests;
- targeted session runtime tests passed: 11 tests;
- `compileall` passed;
- concept registry check passed;
- architecture convergence check passed;
- guardrail cases passed;
- CLI acceptance-report smoke passed;
- `/tmp/alphax-online-community-acceptance-report.md` did not contain sample transcript lines;
- target project working tree remained clean.

## Partner Value Observed

- alphaX reconstructed the active source chain without asking the user to restate project state.
- The pilot preserved the difference between structural verification and real discussion quality.
- The pilot identified the product-relevant risk: manual acceptance is still the real next gate, not more backend harness expansion.

## Recommended Next Move

Run a focused manual-acceptance planning checkpoint:

- choose one real internal discussion transcript or meeting record outside git;
- generate a local acceptance report under ignored storage;
- review evidence refs, signal actionability, interruption levels, and draft confirmation boundaries;
- record only a non-sensitive acceptance summary, not transcript content;
- do not mark manual acceptance complete until a human reviewer signs off.
