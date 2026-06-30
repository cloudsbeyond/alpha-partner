---
type: "Guide"
title: "alpha-partner"
description: "Public entrypoint for the alphaX Markdown-first source repository."
tags: ["alphax", "guide", "source"]
---
# alpha-partner

`alpha-partner` is the local source/meta base for `alphaX`, a personified
project-collaboration function.

The working call sign is `alphaX`.

Chinese guide: [`docs/README.zh-CN.md`](docs/README.zh-CN.md).

This is not an application or hosted service. Runtime carriers execute alphaX by
reading this source; they are not the product boundary. A dedicated always-on
runtime could make alphaX entity-like, but this repository's product boundary is
the function contract and project-local `.alphaX/` mappings.

## What It Is

alphaX is a reusable collaboration function for AI product and software
engineering work. It can be delivered as a Skill, MCP surface, subagent, or
supervisor-agent action, but this repository is the Markdown-first source.

It focuses on:

- project re-entry and risk review;
- project review before handoff, merge, freeze, or release;
- project lifecycle hygiene and local `.alphaX/` compaction signals;
- source review for alphaX contract and mechanism drift;
- checkpoint-based memory evaluation without a runtime or RPC dependency;
- source-backed judgment formation;
- contract-first engineering;
- verifiable implementation;
- external calibration;
- compact decision and evidence records.

## Scopes

Every alphaX run must classify its scope before writing files:

- **`source work`**: change Alpha Partner Source or the alphaX function itself.
- **`source review`**: review Alpha Partner Source, alphaX mechanisms, or local
  `.alphaX/process/` governance data. Report-first; no tracked source edits.
- **`project work`**: help a concrete project, document, product question,
  research task, or engineering problem. `alpha-partner` is read-only source.
- **`project review`**: report-first evidence review for one concrete project
  before handoff, merge, release, freeze, or claimed completion.

The scope guard is the write boundary attached to the chosen scope. Project
work and project review write only to the project being helped, that project's
ignored `.alphaX/` surfaces allowed by `docs/local-alphaX-schema.md`, an OS
temporary directory, or the conversation response.
Source review may write ignored source-facing notes under the source checkout's
`.alphaX/process/`; tracked source edits require `source work`.

## Start Here

Read `AGENTS.md` first, then follow `alphaX/session-runbook.md`.

For a new local checkout:

```bash
bash scripts/init-local-alphaX.sh
bash scripts/verify-local-alphaX.sh
node scripts/generate-alphaX-indexes.mjs --check
bash scripts/verify-alpha-source.sh
```

Optionally add private literals to `.alphaX/local/private-patterns.txt`; the
source verifier will fail if they appear in the GitHub-tracked tree.

## Checkpoint Memory Evaluation

[`docs/checkpoint-memory-evaluation-prd.md`](docs/checkpoint-memory-evaluation-prd.md)
defines how alphaX checks whether remembered or project-local state is current,
evidence-backed, and action-guiding. P0 must work from live source, local
`.alphaX/`, explicit user decisions, command output, artifacts, and available
memory notes; no runtime service, RPC helper, scheduler, or backend is required.

## Markdown Organization

Tracked Markdown and newly initialized ignored `.alphaX/` data use the
[`alphaX OKF Markdown Profile`](docs/okf-markdown-profile.md): small YAML
frontmatter, generated `index.md` navigation, relative internal links, and
explicit citations for external-source-backed claims.

Refresh source indexes with:

```bash
node scripts/generate-alphaX-indexes.mjs --write
node scripts/generate-alphaX-indexes.mjs --check
```

## Common Triggers

The Agent-facing trigger contract and regression fixtures live in
[`docs/agent-invocation-contract.md`](docs/agent-invocation-contract.md),
[`docs/agent-trigger-fixtures.json`](docs/agent-trigger-fixtures.json), and
[`docs/agent-trigger-fixtures.md`](docs/agent-trigger-fixtures.md).

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

For project review:

```text
alphaX run project review before handoff.
```

Triggers are semantic, not literal. User prompts in another language should map
to the same alphaX behaviors when the intent is the same.

## Repository Layout

- `alphaX/`: behavior and scope SOPs.
- `templates/`: report packets and project-local mapping templates.
- `docs/`: evidence, schema, asset boundary, OKF profile, and
  [`docs/README.zh-CN.md`](docs/README.zh-CN.md).
- `scripts/`: bootstrap, verification, context snapshot, and generated indexes.
- `assets/`: shareable visual assets, including `assets/icon.png`.

Generated `index.md` files provide the detailed navigation.

## Review

Review has two contracts with different goals:

- `alphaX/source-review/README.md`: improve alphaX source and mechanisms by
  finding contract drift, stale process state, unsupported claims, and
  scaffolding-to-use imbalance.
- `alphaX/project-review/README.md`: judge one target project's delivery
  evidence before handoff, merge, freeze, release, publication, or claimed
  completion.

Use `templates/project-review/report.md` for project claims, changed files,
validation evidence, source drift, lifecycle hygiene, and project-local
`.alphaX/` objective data.

Project review is report-first by default. Durable summaries belong in the
target project's ignored `.alphaX/` by `docs/local-alphaX-schema.md`, not in the
source checkout's `.alphaX/process/`. A sanitized mechanism-feedback note may go
to source `.alphaX/process/review-feedback/` only when it helps alphaX evolve
and contains no project facts.

## Data Boundary

Ignored `.alphaX/` is generated locally and stores machine-local data and
process traces. It is not part of the open-source source tree.

- Project `.alphaX/`: ignored target-project objective data following `docs/local-alphaX-schema.md`; context, not control.
- Source checkout `.alphaX/local/`: machine-local paths, quasi-static project clues, and local config.
- Source checkout `.alphaX/process/`: alphaX self-governance, review feedback, source work candidates, and source work/review process data only.

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

Public release baselines should be built from sanitized tracked source. Ignored
`.alphaX/` data must not enter public history.

## License

MIT. See [`LICENSE`](LICENSE).
