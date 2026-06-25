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
- project review before handoff, merge, freeze, or release;
- project lifecycle hygiene and local `.alphaX/` compaction signals;
- source review for alphaX contract and mechanism drift;
- checkpoint-based memory evaluation and optional storage/recall through
  `agent-runtime-services` memory family capabilities;
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
ignored `.alphaX/`, an OS temporary directory, or the conversation response.
Source review may write ignored source-facing notes under this checkout's
`.alphaX/process/`; tracked source edits require `source work`.

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

## Memory Family Helper

`scripts/alphaX-memory-family-rpc.mjs` calls the resident
`agent-runtime-services` JSON-RPC surface for the memory family. It is available
in this source now; plugin skill packaging can reuse it later without copying
the adapter.
The why/how contract is in
[`docs/checkpoint-memory-evaluation-prd.md`](docs/checkpoint-memory-evaluation-prd.md).

```bash
node scripts/alphaX-memory-family-rpc.mjs describe
node scripts/alphaX-memory-family-rpc.mjs memory.event.append event.json
node scripts/alphaX-memory-family-rpc.mjs memory.claim.upsert claim.json
node scripts/alphaX-memory-family-rpc.mjs memory.relation.upsert relation.json
node scripts/alphaX-memory-family-rpc.mjs memory.context.retrieve retrieve.json
```

The helper defaults to the resident local endpoint
`http://127.0.0.1:8765/rpc`; set `RUNTIME_SERVICES_RPC_URL` to target another
compatible resident endpoint. Starting a scratch service is only for isolated
local validation.

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

For project review:

```text
alphaX run project review before handoff.
```

Triggers are semantic, not literal. User prompts in another language should map
to the same alphaX behaviors when the intent is the same.

## Repository Layout

- `alphaX/`: shared alphaX behavior plus scope-specific folders for `source work`, `source review`, `project work`, and `project review`.
- `assets/`: shareable visual assets, including the alphaX plugin icon.
- `templates/`: packets and project-local mapping templates.
- `skills/`: local reasoning skills.
- `docs/`: source-backed research, evidence, asset boundary, local `.alphaX/` schema, and the Chinese-language guide.
- `scripts/`: source verification, local `.alphaX/` bootstrap, context snapshot
  helpers, and the `agent-runtime-services` memory-family JSON-RPC helper.

## Source Review

`alphaX/source-review/README.md` defines a reusable governance mechanism for
reviewing alphaX itself. Source review checks contract drift, evidence
quality, stale state, false completion, and weak assumptions. It produces
`meta` work only and must not touch external projects.

Use `alphaX/source-review/bootstrap.md` as the cold-start procedure when running
that mechanism.

## Project Review

`alphaX/project-review/README.md` defines the scoped review mode for one
project. It checks claimed completion, changed files, validation
evidence, source drift, and project-local `.alphaX/` objective data before a
handoff, merge, release, or readiness claim, and reports implementation,
validation, integration, and completion-call state.

This scope is report-first by default. Durable review summaries belong in the
project's ignored `.alphaX/`, not
in this checkout's `.alphaX/process/`. A separate sanitized mechanism-feedback
note may be written to this checkout's ignored `.alphaX/process/review-feedback/`
when it helps alphaX evolve and does not copy project facts.

For PR/merge, handoff, freeze, release, publication, open-source readiness, or
stale/noisy project `.alphaX/` evidence, use
`templates/project-review/lifecycle-hygiene.md` to check remote state, public
metadata, commit shape, license posture, clean tracked source, ignored
`.alphaX/` boundaries, and whether project `.alphaX/` should be
compacted while preserving unfrozen evidence.

## Data Boundary

Ignored `.alphaX/` is generated locally and stores machine-local data and
process traces. It is not part of the open-source source tree.

- Project `.alphaX/`: objective project state, iteration events, evidence pointers, and local reports.
- This checkout's `.alphaX/local/`: machine-local paths, quasi-static project clues, and local config.
- This checkout's `.alphaX/process/`: alphaX self-governance, review feedback, source work candidates, and source work/review process data only.

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
