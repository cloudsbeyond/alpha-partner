# alpha-partner

`alpha-partner` is the local source/meta base for `alphaX`, a personified
project-collaboration function.

The working call sign is `alphaX`.

Chinese guide: [`docs/README.zh-CN.md`](docs/README.zh-CN.md).

This is not a Codex application. Runtime carriers execute alphaX by reading this
source; they are not the product boundary. A dedicated always-on runtime could
make alphaX entity-like, but this repository's product boundary is the function
contract and project-local `.alphaX/` mappings.

## What It Is

alphaX is a reusable collaboration function for AI product and software
engineering work. It can be delivered as a Skill, MCP surface, subagent, or
supervisor-agent action, but this repository is the Markdown-first source.

It focuses on:

- project re-entry and risk review;
- source-backed judgment formation;
- contract-first engineering;
- verifiable implementation;
- external calibration;
- compact decision and evidence records.

## Runtime Modes

Every alphaX run must classify itself before writing files.

- **Source Evolution Mode**: the user is changing alphaX itself. Writes to this
  repository are allowed when they directly serve that requested source change.
- **External Assistance Mode**: the user is using alphaX to help an external
  project, document, product question, research task, or engineering problem.
  In this mode, `alpha-partner` is read-only source.

In External Assistance Mode, write outputs only to the target project, the
target project's ignored `.alphaX/`, an OS temporary directory, or the
conversation response. Do not write external project process data into this
checkout's `.alphaX/process/`.

## Start Here

Read `AGENTS.md` first, then follow `alphaX/session-runbook.md`.

For a new local checkout:

```bash
bash scripts/init-local-alphaX.sh
bash scripts/verify-local-alphaX.sh
bash scripts/verify-alpha-source.sh
```

Optionally add private literals to `.alphaX/local/private-patterns.txt`; the
source verifier will fail if they appear in the GitHub-tracked tree.

## Common Triggers

For repeated project work:

```text
alphaX engage.
```

For stepping back from a task to the real problem:

```text
What are we actually trying to solve?
```

For portfolio focus and risk:

```text
alphaX daily radar
```

Triggers are semantic, not literal. User prompts in another language should map
to the same alphaX behaviors when the intent is the same.

## Repository Layout

- `alphaX/`: alphaX behavior, operating loops, activation, session, pilot, and review-agent mechanism/runbooks.
- `functions/`: reusable function/SOP surfaces, starting with Context Reloader.
- `templates/`: packets and project-local mapping templates.
- `skills/`: local reasoning skills.
- `docs/`: source-backed research, evidence, asset boundary, local `.alphaX/` schema, and the Chinese-language guide.
- `scripts/`: source verification, local `.alphaX/` bootstrap, and context snapshot helpers.

## Review-Agent Mechanism

`alphaX/review-agent-mechanism.md` defines a reusable governance mechanism for
reviewing alphaX itself. The review agent checks contract drift, evidence
quality, stale state, false completion, and weak assumptions. It produces
`meta` work only and must not touch external target projects.

Use `alphaX/review-agent-bootstrap.md` as the cold-start procedure when running
that mechanism.

## Data Boundary

Ignored `.alphaX/` is generated locally and stores machine-local data and
process traces. It is not part of the open-source source tree.

- Target project `.alphaX/`: objective project state, iteration events, evidence pointers, and local reports.
- This checkout's `.alphaX/local/`: machine-local paths, quasi-static project clues, and local config.
- This checkout's `.alphaX/process/`: alphaX self-governance and source-evolution process data only.

The GitHub-tracked tree is intended to be open-source function source only.
Data assets are classified in `docs/asset-boundary.yaml`.

## Before Publishing

Run:

```bash
bash scripts/verify-alpha-source.sh
bash scripts/verify-local-alphaX.sh
git diff --check
git ls-files '.alphaX/*'
```

If `.alphaX/` is tracked by Git, the local data boundary is broken and must be
fixed before publishing.

Public release baselines should be built from sanitized tracked source. Old
local history and ignored `.alphaX/` data must not enter public history.

## License

MIT. See [`LICENSE`](LICENSE).
