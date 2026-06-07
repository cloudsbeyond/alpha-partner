# Pilot: agent-interaction-bridge Project-Local Pointer Adoption

Date: 2026-06-07

Surface:

- `/Users/lizhaohua/work/llm/agent-interaction-bridge`

## Why This Was Added

`agent-interaction-bridge` has already gone through two alphaX sessions:

- cold start against live project source of truth;
- focused `presentation.rendering` Spec Checkpoint.

That satisfies the partner workspace rule: add a project-local pointer only after repeated real-project use.

## Change Made

Added a short `Alpha Partner` section to project-local `AGENTS.md`.

The pointer:

- maps `alphaX 介入一下` and equivalent phrases to `/Users/lizhaohua/Desktop/codex/AGENTS.md`;
- states that project-local instructions, source-of-truth files, validation commands, permissions, and risk boundaries take precedence;
- requires autonomous context inspection before asking the user to restate the scene;
- preserves explicit approval for durable memory, external docs, publication targets, secrets, production state, and destructive state.

## Validation

Commands run:

```bash
bash /Users/lizhaohua/Desktop/codex/scripts/context-snapshot.sh /Users/lizhaohua/work/llm/agent-interaction-bridge
node ./bin/agent-interaction-bridge.mjs architecture check
git diff -- AGENTS.md
```

Observed results:

- `context-snapshot.sh` detected the project-local Alpha Partner pointer;
- architecture contract check passed;
- diff only changed the project-local `AGENTS.md` pointer section.

## Boundary

This adoption does not change project architecture, Product Runtime, Build-Time Governance, contracts, code, test expectations, or validation commands.

It only makes future alphaX activation local and cheaper.
