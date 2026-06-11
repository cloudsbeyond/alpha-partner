# Research Backlog

This backlog organizes deep research for Alpha Partner Source. The goal is not a generic Agent report; the goal is to improve alphaX collaboration quality and agent-native project work.

## Research Rules

- Prefer primary sources: official docs, research papers, engineering blogs, product docs.
- Extract mechanisms and failure modes.
- Map each source back to this source.
- Do not treat Copilot/GitHub issue-to-PR agents as the main model; they are execution-layer references.
- Record useful source conclusions in `docs/evidence-index.md`; keep project-coupled decisions in ignored local process data.

## Track 1: Human-Agent Peer Collaboration

Question:

- What changes when the agent is a partner in problem definition, research, design, validation, and reflection, not only a coding executor?

Primary anchors:

- Human-AI Collaboration and the Transformation of Software Engineering Work: https://arxiv.org/abs/2606.03394
- Human-AI Synergy in Agentic Code Review: https://arxiv.org/abs/2603.15911

Use:

- Define where human judgment remains primary.
- Define where Alpha Partner should challenge, synthesize, or execute.
- Improve review and reflection loops.

## Track 2: Agent-Native Engineering Harness

Question:

- What infrastructure primitives make agents reliable enough for long-running work?

Primary anchors:

- OpenAI Agents SDK evolution: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- OpenAI Codex harness and App Server material: https://openai.com/index/unrolling-the-codex-agent-loop/ and https://openai.com/index/unlocking-the-codex-harness/

Use:

- Compare local source primitives against frontier harness primitives: tools, skills, `AGENTS.md`, shell, patch, sandbox, manifest, durable execution.
- Decide which mechanisms belong in local Markdown now and which belong in later engineering.

## Track 3: Context, Memory, and Tool Boundaries

Question:

- How should context and memory be shaped so the agent remains useful without polluting Alpha Partner Source or global memory?

Primary anchors:

- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/

Use:

- Improve context loading, progressive disclosure, tool boundaries, and source tracing.
- Decide when a local note becomes a durable memory candidate.

## Track 4: Evaluation, Governance, and Oversight

Question:

- What checks make agent-native work trustworthy in production-grade engineering and product decisions?

Primary anchors:

- CMU SEI AI Engineering: Twelve Foundational Practices: https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/
- GitHub Copilot cloud agent docs as an execution-layer comparison: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

Use:

- Keep evaluation, traceability, uncertainty, oversight, and modularity visible.
- Use Copilot-style agents only as a contrast for task execution, logging, and review flow.

## Track 5: Agent-Native Product Form

Question:

- What product surfaces become possible when software expresses people, roles, projects, context, actions, and validation as active collaboration objects?

Primary anchors:

- Local projects or product surfaces provided during concrete sessions.
- External product and engineering sources gathered during concrete project work.

Use:

- Avoid closed-door theorizing.
- Tie every product claim to a real workflow, object model, or validation loop.

## Track 6: Local-First Proactive Agents

Question:

- How should a local-first agent learn usage patterns, infer useful interruption timing, and recover user data permission from centralized super apps without becoming another opaque observer?

Primary anchors:

- Concrete local-first product cases provided during project sessions.
- User-provided local-first product thinking when a concrete source is provided or inspected in a project session.
- Official docs for scheduled agent work, only as execution references after the permission model is clear.

Use:

- Define the difference between observation, inference, candidate nudge, and external push.
- Keep privacy, cooldown, stop conditions, and user-held action authority visible.
- Map proactive behavior back to focus recovery, risk review, and project re-entry instead of generic notification automation.

## Track 7: Source Portability And Path Treaty

Decision: open-source function source must not track local project paths. Machine-local path aliases, if needed, live under ignored `.alphaX/local/project-paths.md`. Scripts self-locate via `BASH_SOURCE`. No resolver script or env var is required for the open-source source itself.

The runtime-carrier portability claim remains unverified until a second environment exercises this mechanism.
