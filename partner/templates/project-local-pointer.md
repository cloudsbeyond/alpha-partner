# Alpha Partner Project Pointer

Add this section to a project-local `AGENTS.md` only after the project repeatedly uses Alpha Partner.

## Alpha Partner

When the user says "alphaX 介入一下", "Alpha Partner 介入一下这个项目", "按 Alpha Partner 方式推进", or "用共同研究执行模式", activate alphaX mode for this project.

alphaX may inject and maintain an optional project-local `.alphaX/` directory, similar in role to project-local `.codex/` or `.trae/` conventions. This project `AGENTS.md` only defines how agents use that injected metadata.

If `.alphaX/` is present, read these files before summarizing project state, especially for re-entry context, handoff state, project progress, risk summaries, or decision-basis questions:

- `.alphaX/AGENTS.md`
- `.alphaX/project-context.md`

Treat `.alphaX/` as context, not control: it is not a project spec and never overrides live source of truth, project contracts, tests, git state, or human approval. If the directory or files are missing or stale, say so explicitly and continue from live project evidence.

Only alphaX should inject or update `.alphaX/` content. Keep `.alphaX/` thin: project key, relationship to alphaX, reload behavior, default output, and boundary. Do not store secrets, private workspace absolute paths, project specs, project contracts, changelog entries, or source-of-truth facts there.

Project-local instructions, source-of-truth files, validation commands, permissions, and risk boundaries in this repository take precedence.

After activation, do a first pass before asking the user to restate context:

- inspect cwd, git state, local `AGENTS.md`, `README`, specs, contracts, changelog, issues, attachments, links, and relevant memory;
- infer the P0 main line, primary loop, source of truth, missing evidence, and next concrete move;
- report the inference compactly, then proceed or ask only for ambiguity that cannot be resolved from available context.

Do not update durable memory, external docs, publication targets, secrets, production state, or destructive state without explicit approval.
