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

### DynamicMem Long-Horizon Memory Benchmark

Source:

- https://arxiv.org/abs/2606.22877

Why it matters:

- Evaluates long-horizon personal-assistant memory over multi-month timelines and
  checkpointed user states, which maps directly to alphaX re-entry and stale
  context risks.
- Its failure pattern points to retrieval and delivered evidence quality as the
  load-bearing part of memory behavior, not only final answer generation.

Source use:

- Supports `Checkpoint Memory Evaluation` as P0: evaluate re-entry, update,
  evidence, and action memory before designing always-on memory infrastructure.
- Supports lifecycle checkpoints and evidence cutoffs instead of one final
  summary snapshot.

### agent-runtime-services Memory Substrate

Sources:

- https://github.com/cloudsbeyond/agent-runtime-services
- https://github.com/cloudsbeyond/agent-runtime-services/blob/main/architecture/memory-substrate-prd.md

Why it matters:

- Provides a project-neutral, open-source memory substrate with append-only
  events, extracted claims, relationship context, and evidence-backed retrieval
  bundles.
- Preserves namespace isolation, status, freshness, confidence, evidence refs,
  and policy metadata while keeping domain judgment and actions outside the
  substrate.

Source use:

- Supports `scripts/alphaX-memory-family-rpc.mjs` as the source-level adapter for
  `memory.event.*`, `memory.claim.*`, `memory.relation.*`, and
  `memory.context.retrieve`.
- Keeps alphaX responsible for interpretation, approval, and next action while
  letting reusable infrastructure own storage and recall.

### GitHub Copilot Cloud Agent

Source:

- https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

Why it matters:

- Provides a concrete execution-layer comparison for background task agents, branch work, logging, and review.

Source use:

- Serves as a contrast case: useful for execution mechanics, but not the main model for partner / co-founder collaboration.
- Informs project review boundaries only at the repo-scoped evidence and
  handoff-log level; it does not turn alphaX review into an issue-to-PR worker.

### Claude Code Dynamic Workflows

Source:

- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code (official Anthropic announcement of Claude Code dynamic workflows).

Why it matters:

- Frames orchestration as a durable, auditable asset (orchestration-as-code) versus persistent goals, the same bet alphaX makes by carrying process and state in Markdown.
- Confirms that cross-checking only works when reviewers genuinely object instead of nodding; the frontier model's honesty / uncertainty-flagging is the load-bearing wall for fan-out + adversarial verification.

Source use:

- Supports the source review topology, `alphaX/source-review/README.md`, Agent Intake Rule, `confidence` / `unverified_claims` fields, and context economy (scaffolding-to-use discipline).
- Supports `alphaX/project-review/README.md` by reinforcing independent
  verification, adversarial checking, and explicit convergence before claimed
  completion.
- Serves as a contrast case for product form: large unattended agent fleets are a low-level execution reference, not the high-checkpoint partner model.

### Claude Tag And Slack-Native Team Agents

Sources:

- https://www.anthropic.com/news/introducing-claude-tag
- https://claude.com/docs/claude-tag/overview
- https://code.claude.com/docs/en/slack

Why it matters:

- Confirms the product form of a channel-scoped agent identity with shared
  channel context, team-visible work threads, proactive follow-up, and
  administrator-controlled tools, repositories, memory, and spend.
- Shows the distinction between personal direct-message use and organization
  channel use: channel tagging acts under an organization identity and follows
  administrator-scoped access.

Source use:

- Supports the alphaX personal plugin as a stable local invocation surface while
  keeping P0 local, explicit, and permission-bound.
- Keeps `channel identity`, `team marketplace`, and `always-on runtime` as P1
  product-form research until alphaX has a dedicated runtime boundary.
- Treats exact Claude X posts as weak context signals only. Do not use an
  account-level X link as source evidence unless a stable, concrete post URL is
  available.

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
