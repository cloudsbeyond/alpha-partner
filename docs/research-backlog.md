---
type: "Research Backlog"
title: "Research Backlog"
description: "Research tracks and source anchors for Alpha Partner Source calibration."
tags: ["alphax", "research", "backlog"]
---
# Research Backlog

```yaml
purpose: improve alphaX collaboration quality and agent-native project work
not: generic Agent report

rules:
  - prefer primary sources: official docs, research papers, engineering blogs, product docs
  - extract mechanisms and failure modes
  - map each source back to Alpha Partner Source
  - treat Copilot/GitHub issue-to-PR agents as execution-layer references
  - record useful source conclusions in docs/evidence-index.md
  - keep project-coupled decisions in ignored local process data

tracks:
  human_agent_peer_collaboration:
    question: agent as partner in problem definition, research, design, validation, reflection
    anchors:
      - https://arxiv.org/abs/2606.03394
      - https://arxiv.org/abs/2603.15911
    use: [human judgment boundary, challenge/synthesize/execute split, review/reflection loops]

  agent_native_engineering_harness:
    question: infrastructure primitives for reliable long-running agent work
    anchors:
      - https://openai.com/index/the-next-evolution-of-the-agents-sdk/
      - https://openai.com/index/unrolling-the-codex-agent-loop/
      - https://openai.com/index/unlocking-the-codex-harness/
    use: [tools, skills, AGENTS.md, shell, patch, sandbox, manifest, durable execution]

  context_memory_tool_boundaries:
    question: useful context and memory without polluting source or global memory
    anchors:
      - https://code.claude.com/docs/en/best-practices
      - https://modelcontextprotocol.io/specification/
      - https://arxiv.org/abs/2606.22877
    use: [context loading, progressive disclosure, tool boundaries, source tracing, checkpoint memory evaluation]
    deferred: adapter/backend implementation until applied checkpoint evidence proves need

  evaluation_governance_oversight:
    question: trustworthy agent-native engineering/product decisions
    anchors:
      - https://www.sei.cmu.edu/library/ai-engineering-twelve-foundational-practices/
      - https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
    use: [evaluation, traceability, uncertainty, oversight, modularity, execution-layer comparison]

  agent_native_product_form:
    question: software objects for people, roles, projects, context, actions, validation
    anchors:
      - https://www.anthropic.com/news/introducing-claude-tag
      - https://claude.com/docs/claude-tag/overview
      - https://code.claude.com/docs/en/slack
    explicit_anchor_label: Claude Tag
    use: [workflow object model, collaboration surface, validation loop]
    p1_parking_lot: [channel identity, team marketplace, always-on runtime after function source proves useful]

  local_first_proactive_agents:
    question: useful interruption timing without opaque observation
    anchors:
      - concrete local-first product cases from project sessions
      - user-provided local-first product sources when inspected
      - official scheduled-agent docs only after permission model is clear
    use: [observation vs inference vs nudge vs push, privacy, cooldown, stop condition, action authority]

  source_portability_path_treaty:
    decision: open-source function source must not track local project paths
    local_aliases: ignored .alphaX/local/project-paths.md
    scripts: self-locate via BASH_SOURCE
    unverified_claim: runtime-carrier portability needs second-environment exercise
```
