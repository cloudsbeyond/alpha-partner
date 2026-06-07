# Evidence Index

This index records why a source matters to the partner workspace. Sources are not collected for completeness; each must support a collaboration rule, design choice, or research question.

## External Sources

### OpenAI Agents SDK Evolution

Source:

- https://openai.com/index/the-next-evolution-of-the-agents-sdk/

Why it matters:

- Shows frontier agent harness primitives: MCP, skills, `AGENTS.md`, shell, apply patch, sandbox execution, workspace manifest, and durable execution.

Workspace use:

- Supports the choice to make `AGENTS.md` the first local contract.
- Frames later migration from Markdown workspace to Skill or MCP only after the method stabilizes.

### OpenAI Codex Harness / App Server

Sources:

- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://openai.com/index/unlocking-the-codex-harness/

Why it matters:

- Treats Codex as a harness and agent loop across surfaces, not just a chat interface.

Workspace use:

- Supports the idea that the local workspace is a collaboration harness, not a single prompt.

### Claude Code Best Practices

Source:

- https://code.claude.com/docs/en/best-practices

Why it matters:

- Emphasizes exploration before planning and implementation, giving the agent ways to verify work, specific context, and aggressive context management.

Workspace use:

- Supports the operating loops and the requirement that partner work produces evidence, decision records, or verification.

### Human-AI Collaboration and the Transformation of Software Engineering Work

Source:

- https://arxiv.org/abs/2606.03394

Why it matters:

- Frames software engineering work as shifting from code authorship to directing, verifying, and governing autonomous or semi-autonomous systems.

Workspace use:

- Supports the human-agent peer model and the shift from throughput to judgment, oversight, and collaboration quality.

### Human-AI Synergy in Agentic Code Review

Source:

- https://arxiv.org/abs/2603.15911

Why it matters:

- Highlights that human reviewers contribute understanding, testing, and knowledge transfer beyond agent suggestions.

Workspace use:

- Supports keeping Lizhaohua's judgment central and using Codex Partner for critique, evidence gathering, and alternative generation rather than unchecked acceptance.

### CMU SEI AI Engineering Practices

Source:

- https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/

Why it matters:

- Promotes evaluation as a core engineering practice and revisits traceability, uncertainty, oversight, and modularity for foundation models and agentic systems.

Workspace use:

- Supports the validation and governance emphasis across project, research, and memory loops.

### GitHub Copilot Cloud Agent

Source:

- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

Why it matters:

- Provides a concrete execution-layer comparison for background task agents, branch work, logging, and review.

Workspace use:

- Serves as a contrast case: useful for execution mechanics, but not the main model for partner / co-founder collaboration.

## Internal Evidence Sources

### Agent 化组织

Source:

- Local project practice and future project notes.

Why it matters:

- Provides the product-form calibration surface for modeling people, roles, actions, context, and validation as software objects.

Workspace use:

- Prevents the partner workspace from becoming only an engineering process.

### L0-L4 需求到交付链路

Source:

- Existing memory and project practice around requirements-to-code ownership.

Why it matters:

- Encodes the boundary between human-owned problem and contract layers and agent-owned downstream implementation.

Workspace use:

- Protects against downstream patches that silently change business meaning.

### Agent 知识治理闭环

Source:

- Existing project practice around candidate knowledge, owner confirmation, active retrieval, and source-backed answers.

Why it matters:

- Makes context quality a governed lifecycle rather than a retrieval trick.

Workspace use:

- Guides the memory loop and source-backed collaboration rule.

### 端侧 Agent 数据权限回收

Source:

- User-provided direction about using alphaX to observe work patterns and experiment with non-intrusive proactive pushes.

Why it matters:

- It extends the partner workspace from reactive activation to controlled proactive assistance.
- It connects product thinking about local agent context to concrete workflow risks: missed decisions, stale branches, false completion, and focus loss.

Workspace use:

- Supports `partner/loop-registry.md` and the proactive nudge boundary in `partner/activation-guide.md`.
- Keeps the first implementation report-first and permission-bound instead of creating background watchers.
