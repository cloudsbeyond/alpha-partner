# Source Work

`source work` is the scope for changing Alpha Partner Source or the alphaX
function itself.

Use this scope when the user is changing:

- the alphaX contract in `AGENTS.md`;
- scope definitions, SOPs, templates, skills, docs, scripts, or verifiers;
- plugin packaging when the plugin carries alphaX invocation behavior;
- open-source boundaries and local `.alphaX/` source-governance rules.

Tracked source edits are allowed only when they directly serve the accepted
source work scope. Keep project facts out of the GitHub-tracked source. Local
process notes may go under this checkout's ignored `.alphaX/process/`.

When source work changes tracked files, run:

```bash
bash scripts/verify-alpha-source.sh
git diff --check
```

If local `.alphaX/` data is initialized or relied on, also run:

```bash
bash scripts/verify-local-alphaX.sh
```

Do not use `source work` for source review. Use `source review` first when the
task is to audit, critique, or find drift without applying changes.
