# Alpha Partner Project Pointer

Add this section to a project-local `AGENTS.md` only after the project repeatedly uses Alpha Partner.

## Alpha Partner

When the user says "alphaX 介入一下", "Alpha Partner 介入一下这个项目", "按 Alpha Partner 方式推进", or "用共同研究执行模式", follow `/Users/lizhaohua/Desktop/codex/AGENTS.md`.

Project-local instructions, source-of-truth files, validation commands, permissions, and risk boundaries in this repository take precedence.

After activation, do a first pass before asking the user to restate context:

- inspect cwd, git state, local `AGENTS.md`, `README`, specs, contracts, changelog, issues, attachments, links, and relevant memory;
- infer the P0 main line, primary loop, source of truth, missing evidence, and next concrete move;
- report the inference compactly, then proceed or ask only for ambiguity that cannot be resolved from available context.

Do not update durable memory, external docs, publication targets, secrets, production state, or destructive state without explicit approval.
