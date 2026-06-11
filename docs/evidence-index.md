# Evidence Index

This index records why a source matters to Alpha Partner Source. Sources are not collected for completeness; each must support a collaboration rule, design choice, or research question.

## External Sources

### OpenAI Agents SDK Evolution

Source:

- https://openai.com/index/the-next-evolution-of-the-agents-sdk/

Why it matters:

- Shows frontier agent harness primitives: MCP, skills, `AGENTS.md`, shell, apply patch, sandbox execution, workspace manifest, and durable execution.

Source use:

- Supports the choice to make `AGENTS.md` the first local contract.
- Frames later migration from Markdown source to Skill or MCP only after the method stabilizes.

### OpenAI Codex Harness / App Server

Sources:

- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://openai.com/index/unlocking-the-codex-harness/

Why it matters:

- Treats Codex as a harness and agent loop across surfaces, not just a chat interface.

Source use:

- Supports the idea that the local source is a collaboration harness, not a single prompt.

### Claude Code Best Practices

Source:

- https://code.claude.com/docs/en/best-practices

Why it matters:

- Emphasizes exploration before planning and implementation, giving the agent ways to verify work, specific context, and aggressive context management.

Source use:

- Supports the operating loops and the requirement that partner work produces evidence, decision records, or verification.

### Human-AI Collaboration and the Transformation of Software Engineering Work

Source:

- https://arxiv.org/abs/2606.03394

Why it matters:

- Frames software engineering work as shifting from code authorship to directing, verifying, and governing autonomous or semi-autonomous systems.

Source use:

- Supports the alphaX partner model and the shift from throughput to judgment, oversight, and collaboration quality.

### Human-AI Synergy in Agentic Code Review

Source:

- https://arxiv.org/abs/2603.15911

Why it matters:

- Highlights that human reviewers contribute understanding, testing, and knowledge transfer beyond agent suggestions.

Source use:

- Supports keeping user judgment central and using Alpha Partner for critique, evidence gathering, and alternative generation rather than unchecked acceptance.

### CMU SEI AI Engineering Practices

Source:

- https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/

Why it matters:

- Promotes evaluation as a core engineering practice and revisits traceability, uncertainty, oversight, and modularity for foundation models and agentic systems.

Source use:

- Supports the validation and governance emphasis across project, research, and memory loops.

### GitHub Copilot Cloud Agent

Source:

- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

Why it matters:

- Provides a concrete execution-layer comparison for background task agents, branch work, logging, and review.

Source use:

- Serves as a contrast case: useful for execution mechanics, but not the main model for partner / co-founder collaboration.

### Claude Code Dynamic Workflows

Source:

- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code (official Anthropic announcement of Claude Code dynamic workflows).

Why it matters:

- Frames orchestration as a durable, auditable asset (orchestration-as-code) versus persistent goals, the same bet alphaX makes by carrying process and state in Markdown.
- Confirms that cross-checking only works when reviewers genuinely object instead of nodding; the frontier model's honesty / uncertainty-flagging is the load-bearing wall for fan-out + adversarial verification.

Source use:

- Supports the review-agent topology, `alphaX/review-agent-mechanism.md`, Agent Intake Rule, `confidence` / `unverified_claims` fields, and context economy (scaffolding-to-use discipline).
- Serves as a contrast case for product form: large unattended agent fleets are a low-level execution reference, not the high-checkpoint partner model.

## Internal Evidence Sources

### Agent-Native Organization

Source:

- Local project practice and future project notes.

Why it matters:

- Provides the product-form calibration surface for modeling people, roles, actions, context, and validation as software objects.

Source use:

- Prevents Alpha Partner Source from becoming only an engineering process.

### L0-L4 Requirements-To-Delivery Chain

Source:

- Existing memory and project practice around requirements-to-code ownership.

Why it matters:

- Encodes the boundary between human-owned problem and contract layers and agent-owned downstream implementation.

Source use:

- Protects against downstream patches that silently change business meaning.

### Agent Knowledge Governance Loop

Source:

- Existing project practice around candidate knowledge, owner confirmation, active retrieval, and source-backed answers.

Why it matters:

- Makes context quality a governed lifecycle rather than a retrieval trick.

Source use:

- Guides the memory loop and source-backed collaboration rule.

### Local-First Agent Permission Recovery

Source:

- Product direction about using alphaX to observe local work patterns and experiment with non-intrusive proactive pushes.

Why it matters:

- It extends Alpha Partner Source from reactive activation to controlled proactive assistance.
- It connects product thinking about local agent context to concrete workflow risks: missed decisions, stale branches, false completion, and focus loss.

Source use:

- Supports `alphaX/loop-registry.md` and the proactive nudge boundary in `alphaX/activation-guide.md`.
- Keeps the first implementation report-first and permission-bound instead of creating background watchers.
