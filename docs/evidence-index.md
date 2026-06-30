---
type: "Evidence Index"
title: "Evidence Index"
description: "Source-backed evidence index for Alpha Partner Source design choices."
tags: ["alphax", "evidence", "research"]
---
# Evidence Index

```yaml
purpose: source-to-rule evidence index
not: bibliography

external_sources:
  - label: OpenAI Agents SDK evolution
    url: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
    supports: local AGENTS.md, skills, tools, durable execution as harness primitives
  - label: OpenAI Codex loop and harness
    urls:
      - https://openai.com/index/unrolling-the-codex-agent-loop/
      - https://openai.com/index/unlocking-the-codex-harness/
    supports: Alpha Partner Source as collaboration harness, not prompt
  - label: Claude Code best practices
    url: https://code.claude.com/docs/en/best-practices
    supports: exploration, context management, verification loops
  - label: Human-AI Collaboration and Software Engineering Work
    url: https://arxiv.org/abs/2606.03394
    supports: partner model, judgment, oversight
  - label: Human-AI Synergy in Agentic Code Review
    url: https://arxiv.org/abs/2603.15911
    supports: human judgment centrality and evidence critique
  - label: CMU SEI AI Engineering Practices
    url: https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/
    supports: evaluation, uncertainty, traceability, modularity
  - label: DynamicMem
    url: https://arxiv.org/abs/2606.22877
    supports: checkpoint memory evaluation dimensions
  - label: GitHub Copilot cloud agent
    url: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
    supports: execution-layer contrast for branch/log/review boundaries
  - label: Claude Code dynamic workflows
    url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
    supports: auditable orchestration, independent objection, unverified_claims
  - label: Claude Tag
    urls:
      - https://www.anthropic.com/news/introducing-claude-tag
      - https://claude.com/docs/claude-tag/overview
      - https://code.claude.com/docs/en/slack
    supports: channel-scoped agent identity as P1 product-form research

internal_sources:
  - label: Agent-native organization practice
    supports: people, roles, actions, context, validation as software objects
  - label: L0-L4 requirements-to-delivery chain
    supports: human-owned upstream boundary before downstream agent implementation
  - label: Agent knowledge governance loop
    supports: candidate knowledge, owner confirmation, retrieval, source-backed answers
  - label: Local-first permission recovery
    supports: focus recovery, risk review, nudge permission boundary
```

## Citations

- [OpenAI Agents SDK evolution](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI Codex loop](https://openai.com/index/unrolling-the-codex-agent-loop/)
- [OpenAI Codex harness](https://openai.com/index/unlocking-the-codex-harness/)
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [Human-AI Collaboration and the Transformation of Software Engineering Work](https://arxiv.org/abs/2606.03394)
- [Human-AI Synergy in Agentic Code Review](https://arxiv.org/abs/2603.15911)
- [CMU SEI AI Engineering Practices](https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/)
- [DynamicMem](https://arxiv.org/abs/2606.22877)
- [GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [Claude Code dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)
- [Claude Tag overview](https://claude.com/docs/claude-tag/overview)
- [Claude Code Slack docs](https://code.claude.com/docs/en/slack)
