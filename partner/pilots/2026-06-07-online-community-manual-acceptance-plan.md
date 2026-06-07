# Pilot Plan: online_community Manual Acceptance

Date: 2026-06-07

Surface:

- `/Users/lizhaohua/work/llm/clouds-beyond/online_community`

Purpose:

- Turn the current structural Session Runtime harness into a real-discussion manual acceptance review without committing transcript content or claiming product quality from tests alone.

## P0

Validate whether Session Runtime navigation signals are useful in a real internal discussion:

- evidence refs match local transcript lines;
- signals are actionable;
- interruption levels would not disrupt the discussion;
- draft confirmation boundaries are preserved;
- human reviewer signs off before acceptance is marked complete.

## Inputs Needed

Required outside git:

- one real internal discussion transcript or meeting record;
- a local source path not committed to the repo;
- a reviewer who can compare the generated report against the local transcript.

Optional:

- project context refs or source docs used in the discussion;
- reviewer notes about missed risks, false positives, interruption timing, and useful signals.

## Privacy Boundary

- Do not commit transcript content.
- Do not paste transcript content into partner workspace notes.
- Generate acceptance report under ignored storage or `/tmp`.
- Record only a non-sensitive summary after review.
- If the report includes raw transcript text, stop and treat it as a privacy failure.

## Runbook

From `/Users/lizhaohua/work/llm/clouds-beyond/online_community/backend`:

```bash
bash ../scripts/check_backend.sh
PYTHONPATH=src python3 -m unittest tests.test_session_runtime_acceptance tests.test_session_runtime tests.test_session_runtime_cli
PYTHONPATH=src python3 -m session_runtime.cli \
  --session-id "session:<local-id>" \
  --profile "work_buddy_internal_session" \
  --organization-id "organization:cloudsbeyond" \
  --participant-unit-id "unit:<reviewer-or-participant>" \
  --transcript-file "<absolute-local-transcript-path>" \
  --source-ref "transcript:<non-sensitive-local-label>" \
  --acceptance-report "acceptance-reports/<local-review-name>.md"
```

Then verify:

```bash
rg -n "<unique raw transcript sentence>" "acceptance-reports/<local-review-name>.md"
```

Expected result:

- no matches for raw transcript content;
- report includes evidence index, navigation signals, route review, manual checklist, and stop condition.

## Review Rubric

Accept only if all are true:

- every evidence ref can be traced to a local transcript line;
- each navigation signal is understandable and actionable;
- high-priority signals reflect real risk, missing context, conflict, or needed clarification;
- silent or after-turn interruption levels feel appropriate;
- SessionAgent and PersonalAgent views are not collapsed into one generic assistant voice;
- all AI-generated decisions, actions, signals, and verification events remain draft;
- human reviewer explicitly signs off.

Record as weak or failed if any are true:

- signals are mostly keyword artifacts rather than useful navigation;
- evidence refs point to the wrong line or are too coarse to review;
- report or logs expose raw transcript content where they should not;
- output implies decisions or actions are confirmed by AI;
- reviewer cannot tell what to do next from the report.

## Non-Sensitive Summary Shape

Record only this kind of summary in project or partner notes:

```text
review_date:
source_ref:
reviewer:
transcript_committed: no
report_path_local:
signals_reviewed:
accepted_signals:
rejected_signals:
main_failure_mode:
manual_acceptance_status: not_started | weak | passed
next_action:
```

## Stop Conditions

Stop before marking acceptance complete if:

- transcript source is unavailable to the reviewer;
- report embeds private transcript content;
- evidence refs drift;
- signals are not actionable;
- interruption levels would disrupt discussion;
- any AI-generated output is treated as confirmed without human review.
