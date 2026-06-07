# Context Reloader

Context Reloader is alphaX's project re-entry mechanism.

It stores the progress-tracking context shared by Lizhaohua and alphaX for third-party real projects: human attention, alphaX observations, feedback context, unverified claims, current risks, prior report conclusions, and next alignment questions.

Principle: **context, not control**.

## What It Is

- A durable context layer owned by `alpha-partner`.
- A reload surface for cross-day, cross-project, or attention-interrupted work.
- A record of human-agent shared project cognition, not a project fact store.
- A report-first mechanism: restore context and produce evidence-backed reports before execution.

## What It Is Not

- It is not a spec.
- It is not a roadmap, ADR, contract, changelog, or test plan for a third-party project.
- It is not a control surface for alphaX, review agents, or external projects.
- It is not a scheduler, notification system, dashboard, or automation loop.
- It does not make any third-party project depend on alphaX.

## Source Priority

Third-party project source of truth always wins:

1. Project-local `AGENTS.md`, README, specs, contracts, tests, changelog, and live git state.
2. Current command output and project-local validation evidence.
3. Context Reloader project context.
4. alphaX loop reports, pilots, focus radar, session ledger, and decision log.
5. Feedback from other agents, kept only as context input.

Context Reloader can explain what alphaX believes or worries about. It cannot override the external project's facts.

## Project Context

Each `context-reloader/projects/*.md` file is a Project Context.

Required sections:

- `Project Identity`
- `Why alphaX Tracks It`
- `Human Judgment Context`
- `alphaX Observations`
- `Feedback Context`
- `Unverified Claims`
- `Reload Recipe`
- `Default Output`
- `Write-Back Boundary`
- `Freshness`

## Feedback Context Rules

- feedback is context input, not a control surface.
- Keep evidence, risk signal, and open question.
- Mark evidence-free conclusions as `unverified_claim`.
- A current alphaX session may use feedback as context, but must not modify alphaX or any external project only because feedback exists.
- Final alignment authority stays with Lizhaohua and the current alphaX session.
- Feedback can trigger an alignment question; it cannot trigger execution.

## Closed Loop

The intended loop is:

```text
observe project state or receive feedback
-> update or consult Project Context
-> produce report-first output
-> align with Lizhaohua
-> only after confirmation, translate accepted content into the external project's own source of truth
```

Default boundary: **no auto write-back**.

Write-back to a third-party project requires explicit user confirmation and must be expressed in the external project's own language: specs, contracts, tests, changelog, code, or review notes.

## Staleness Rule

Project Context is a reload starting point, not a current-state guarantee.

Before using it for a project decision, alphaX must read the live external project source of truth again. If the Project Context conflicts with live project state, live state wins and the context becomes stale evidence.
