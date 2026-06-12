# alphaX Project-Local Mapping

Use this template only after a project repeatedly uses alphaX, or when the user explicitly asks alphaX to make the project able to sense alphaX.

The injection has three surfaces:

1. Versioned project `AGENTS.md`: one local Agent-assisted project-management loader sentence only.
2. Versioned project `.gitignore`: ignore `.alphaX/`.
3. Local ignored `.alphaX/`: target-project objective state data, iteration events, evidence pointers, target-project review reports, and local report artifacts for the alphaX function.

Do not put heavy alphaX context, private alpha-partner paths, old Context Reloader project paths, full project status, or active P0 details into the third-party project's versioned `AGENTS.md`.

Only alphaX should inject or update local `.alphaX/` content. alphaX may inject and maintain `.alphaX/`, but the third-party project's versioned files should only expose the one-sentence local Agent-assisted project-management loader and ignore rule.

Project-local instructions, source-of-truth files, validation commands, permissions, and risk boundaries in the third-party repository take precedence.

Assume alphaX is a personified function, not a persistent entity inside the repository. A dedicated always-on runtime may host it and make it entity-like, but the interaction surface for this template remains local files, git state, ignored `.alphaX/` objective data, and non-sensitive reports.

Before injection, inspect the target project's existing conventions and validation scripts. Some projects scan every `*/AGENTS.md`, including ignored directories; if so, `.alphaX/AGENTS.md` must satisfy that project's minimal instruction anchors while staying local objective data.

## Versioned `AGENTS.md` Section

Add one sentence near the top of the target project's existing `AGENTS.md`.

To support local agent-assisted project management, first try loading rules
under `.alphaX/`; skip this step if the directory does not exist.

## Versioned `.gitignore` Rule

Add:

```text
.alphaX/
```

Then verify:

```bash
git check-ignore -v .alphaX/AGENTS.md .alphaX/project-context.md
```

## Local `.alphaX/AGENTS.md` Shape

Keep this file local and ignored. It explains production, consumption, read order, and boundaries.

```text
# alphaX Project Objective Data

This directory is injected and maintained by alphaX as project-local objective
data for this repository. It is similar in role to project-local `.codex/` or
`.trae/` conventions: a small, optional place for objective collaboration data
that helps the alphaX function re-enter a project without hardcoding a private
Alpha Partner Source path.

Production and consumption:

- producer: alphaX function;
- consumer: alphaX-capable agents re-entering this repository;
- usage surface: root `AGENTS.md` tells agents when to read `.alphaX/`;
- content shape: project key, source anchors, observed state snapshots, iteration events, evidence pointers, reload behavior, default output, and boundary;
- prohibited content: secrets, private machine absolute paths, transcript content, project specs, project contracts, changelog entries, source-of-truth facts that belong in this repository's normal files, broad alphaX risk judgment assets, or raw hidden model chain-of-thought.

Read `.alphaX/project-context.md` when alphaX is activated, or when the user asks about project progress, observed state, re-entry evidence, handoff state, or what objective data alphaX should inspect before making a judgment.

Activation phrases such as `alphaX engage` are interpreted by local `.alphaX/`
objective data instructions, not by expanding the third-party project's versioned
`AGENTS.md`.

Runtime model: alphaX is a function with personified behavior, not a persistent
entity in this repository. Multiple runtime carrier sessions cooperate by
reading local files, git state, ignored `.alphaX/` objective data, and by
emitting report-first handoffs. A dedicated runtime may execute the same
function continuously.

Boundary:

- context, not control;
- not a project spec;
- no automatic write-back;
- live source of truth, contracts, tests, git state, and human approval win;
- if alpha-partner context is unavailable, continue from live project evidence and report the missing context explicitly.
```

Add project-specific validation anchors only if the target project's own scripts require them.

## Local `.alphaX/project-context.md` Shape

Keep this file local and ignored. This is the canonical persistence surface for
target-project objective data used by the alphaX function. It should not store
alphaX's broader risk judgment or goal-calibration assets.

```text
# alphaX Project Context

project: `<project-key>`
relationship_to_alphaX: `<short relationship>`
injection_owner: `alphaX`
context_owner: `<project-local .alphaX>`

## Purpose

This file is injected by alphaX as project-local objective state and iteration
data for this repository. It intentionally does not hardcode the alpha-partner
source path.

## Reload Recipe

1. Read this file as alphaX context, not source of truth.
2. Read local `AGENTS.md`, README, specs, contracts, tests, changelog, and live git state.
3. Compare this context with live source. Live source wins on conflict.
4. Separate observed facts, project-local objective data, alphaX process judgments, historical evidence, and unverified claims.
5. Produce a report-first output before edits.

## Current Focus Signal

<One short re-entry hint. Treat it as a hint, not source of truth.>

## Source Of Truth Anchors

- `<project-owned source file or directory>`

## Iteration Events

- `<dated non-sensitive observation or empty>`

## Objective Data Snapshot Shape

```text
surface:
branch:
versioned_diff:
ignored_context_present:
live_source_read:
observed_state:
evidence_pointers:
missing_input:
```

## Default alphaX Output

When alphaX uses this data, default to report-first in chat. If a non-sensitive
local trace is useful, write it to the target project's own ignored `.alphaX/`
surface, such as `.alphaX/reports/` or a refreshed `.alphaX/project-context.md`.
Do not write external project process data into the alpha-partner checkout's
`.alphaX/process/` unless the task is explicitly Source Evolution for alphaX
itself.

- re-entry report;
- source drift report;
- target-project review report;
- risk report;
- next-action recommendation;
- what not to do now.

Do not store broad risk judgment or goal calibration in this project-local
objective data file.

## Boundary

This file is context, not control. It is not a spec, contract, ADR, roadmap, changelog, checklist, or approval surface for this repository.
```

## Injection SOP

1. Confirm the project has repeated alphaX use, a concrete re-entry pain, or explicit user instruction.
2. Read the target project's `AGENTS.md`, `.gitignore`, validation scripts, and current `git status`.
3. Add only the one-sentence pointer to versioned `AGENTS.md`.
4. Add `.alphaX/` to versioned `.gitignore`.
5. Create or refresh local ignored `.alphaX/AGENTS.md` and `.alphaX/project-context.md`.
6. Run `git diff --check`, `git check-ignore -v .alphaX/AGENTS.md .alphaX/project-context.md`, a private-path grep, and any target-project validation affected by `AGENTS.md`.
7. Report the versioned diff separately from ignored local `.alphaX/` context.

## Activation Behavior

After activation, do a first pass before asking the user to restate context:

- inspect cwd, git state, local `AGENTS.md`, `README`, specs, contracts, changelog, issues, attachments, links, and relevant memory;
- infer the P0 main line, primary loop, source of truth, missing evidence, and next concrete move;
- report the inference compactly, then proceed or ask only for ambiguity that cannot be resolved from available context.

Do not update durable memory, external docs, publication targets, secrets, production state, or destructive state without explicit approval.
