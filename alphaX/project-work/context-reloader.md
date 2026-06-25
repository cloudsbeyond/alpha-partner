# Context Reloader

Context Reloader is an alphaX function/SOP for project re-entry.

It does not store external project state in `alpha-partner`. It reads the
project's live source and ignored `.alphaX/` objective data, then
produces a report-first re-entry output. The resulting alphaX judgments belong
to alphaX process data assets, not to the project's objective data.

Principle: **function, not project store**.

## What It Is

- A reusable re-entry function for alphaX.
- A SOP that can later be delivered as a Skill, MCP tool, subagent, or supervisor-agent action.
- A report-first workflow for cross-day, cross-project, or attention-interrupted work.
- A reader of project-local `.alphaX/project-context.md`, not the owner of project facts.

## What It Is Not

- It is not a centralized Project Context directory.
- It is not a project spec, roadmap, ADR, contract, changelog, or test plan.
- It is not a scheduler, notification system, dashboard, or automation loop.
- It does not make any third-party project depend on `alpha-partner`.

## Source Priority

Project source of truth always wins:

1. Project-local `AGENTS.md`, README, specs, contracts, tests, changelog, and live git state.
2. Project-local ignored `.alphaX/` objective data, especially `.alphaX/project-context.md`.
3. Current command output and project-local validation evidence.
4. Optional local `.alphaX/local/project-meta-index.yaml` for quasi-static project clues only.
5. Optional local `.alphaX/process/` reports, pilots, focus radar, ledger, and decisions as historical evidence.
6. Feedback from other agents, kept only as context input.

## Project-Local Objective Data

Each concrete project may have:

- `.alphaX/AGENTS.md`: local instructions for alphaX-capable agents.
- `.alphaX/project-context.md`: project-local objective state data, iteration events, evidence pointers, and source anchors.
- `.alphaX/reports/`: optional ignored non-sensitive report artifacts generated for or by the project.

These files are data inputs for the alphaX function. They are context, not
control. They must not replace the project's versioned source of truth and
should avoid storing alphaX's broader risk judgment or goal-calibration assets.

## alphaX Process Data Assets

alpha-partner may keep alphaX's own process data assets:

- goal calibration summaries;
- risk judgments;
- decision rationale;
- review summaries;
- reusable lessons from applied work.

These are not raw hidden model chain-of-thought. They are reviewable reasoning
summaries and evidence-backed judgment records.

## Project Meta Index

Ignored `.alphaX/local/project-meta-index.yaml` may list projects alphaX can
re-enter on one machine. It is data, not a project record, and it must not be
committed to the open-source function source.

Allowed fields are quasi-static clues such as project key, path alias, local
`.alphaX` context path, relationship to alphaX, and source-of-truth anchors.

Disallowed fields include current branch, PR status, active P0, live risks,
private transcript content, current implementation status, and acceptance state.

## Function SOP

```text
receive alphaX trigger
-> identify project and project key
-> read project-local AGENTS.md and live git/source state
-> read .alphaX/AGENTS.md and .alphaX/project-context.md when present
-> consult .alphaX/local/project-meta-index.yaml only for quasi-static clues when present
-> separate live facts, project-local objective data, alphaX process judgments, historical evidence, and unverified claims
-> produce report-first output
-> write back only with explicit user approval, and only into the project's own language
```

Default boundary: **no auto write-back**.

Write-back to a project requires explicit user confirmation and must
be expressed in that project's own source-of-truth surface: specs, contracts,
tests, changelog, code, review notes, or ignored local `.alphaX/` objective
data. Risk judgments and goal calibration remain alphaX process data assets.

## Staleness Rule

`.alphaX/project-context.md` is a reload starting point, not a current-state guarantee.

Before using it for a project decision, alphaX must read the live
project source of truth again. If `.alphaX` conflicts with live project state,
live state wins and the `.alphaX` context becomes stale evidence.
