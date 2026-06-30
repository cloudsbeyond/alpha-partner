---
type: "Guide"
title: "alpha-partner 中文指南"
description: "Chinese-language guide to Alpha Partner Source and alphaX usage."
tags: ["alphax", "guide", "zh-cn"]
---
# alpha-partner 中文说明

`alpha-partner` 是 `alphaX` 的本地 source/meta base。`alphaX` 是一个带有人格化协作风格的项目协作函数，不是常驻运行实体本身。

英文公开源码是 canonical source；本文件是中文使用入口。正式合约、运行边界和 SOP 以根目录 `AGENTS.md` 为准。

## 它是什么

alphaX 是一个可复用的协作函数，用来辅助 AI 产品和软件工程工作。它可以被交付成 Skill、MCP surface、subagent 或 supervisor-agent action；这个仓库是 Markdown-first source。

它关注：

- 降低项目重新进入成本；
- 识别并复查项目风险；
- 在 handoff、合入、freeze 或发布前做项目复查；
- 维护项目 lifecycle hygiene 和本地 `.alphaX/` 压缩信号；
- 复查 alphaX source 的 contract drift 和机制漂移；
- 用 checkpoint 方式评估 re-entry、update、evidence、action 四类记忆质量，且 P0 不依赖 runtime 或 RPC；
- 形成有来源支撑的判断；
- 维护 contract-first 的工程链路；
- 保持实现、验证和证据可追踪；
- 定期做外部校准；
- 沉淀紧凑的决策和证据记录。

## 四类 scope

每次 alphaX 运行，在写文件前必须先判定 scope：

- **`source work`**：修改 Alpha Partner Source 或 alphaX function 本身。
- **`source review`**：复查 Alpha Partner Source、alphaX 机制或 source checkout ignored `.alphaX/process/` 治理数据；默认 report-first，不改 tracked source。
- **`project work`**：辅助某个具体项目、文档、产品问题、研究任务或工程问题；`alpha-partner` 是只读 source。
- **`project review`**：在 handoff、合入、release、freeze 或声称完成前，对一个具体项目做 report-first 证据复查。

Scope guard 是每个 scope 对应的写入边界。`project work` 和 `project review` 只能写到被辅助项目、该项目 ignored `.alphaX/` schema 允许的文件、系统临时目录，或直接在对话里报告。`source review` 可在有用且允许时写入 source checkout ignored `.alphaX/process/` 的 source-facing note；tracked source 修改必须切到 `source work`。

## 快速开始

新会话先读：

```text
AGENTS.md
alphaX/session-runbook.md
```

本地初始化和验证：

```bash
bash scripts/init-local-alphaX.sh
bash scripts/verify-local-alphaX.sh
bash scripts/verify-alpha-source.sh
```

可以把私有字面量加入 `.alphaX/local/private-patterns.txt`；如果这些内容出现在 GitHub-tracked tree，source verifier 会失败。

## Checkpoint Memory Evaluation

`docs/checkpoint-memory-evaluation-prd.md` 定义 alphaX 如何判断 remembered state 或项目本地状态是否当前、证据充分、能指导下一步。P0 只依赖 live source、本地 `.alphaX/`、用户明确决策、命令输出、artifact 和已有 memory note；不要求 runtime service、RPC helper、scheduler 或后端。

## 常用触发

中文触发是语义触发，不依赖英文源码里的字面示例。Agent 侧触发合约和回归样例见
`docs/agent-invocation-contract.md` 与 `docs/agent-trigger-fixtures.md`。

```text
alphaX 介入一下
帮我恢复一下这个项目现场
review 一下我现在几个项目的风险
合入前审一下这个项目声称的功能是否真的实现
这件事真正要解决的问题是什么？
```

默认交互语言跟随用户：用户用中文，alphaX 应使用中文反馈；`D0-D3`、`P0/P1/P2`、`confidence`、`unverified_claims` 这类稳定结构字段保持不翻译。

## 目录结构

- `alphaX/`：行为和 scope SOP。
- `templates/`：报告 packet 和项目本地映射模板。
- `docs/`：证据、schema、资产边界、OKF profile 和中文入口。
- `scripts/`：初始化、验证、上下文快照和索引生成。
- `assets/`：可共享视觉资产，包括 `assets/icon.png`。

详细导航由生成的 `index.md` 文件承担。

## Review

Review 有两个 contract，目标不同：

- `alphaX/source-review/README.md`：改进 alphaX source 和机制，发现 contract drift、过期过程状态、未证实机制声明和 scaffolding-to-use imbalance。
- `alphaX/project-review/README.md`：判断一个目标项目的交付证据是否支持 handoff、合入、freeze、release、publication 或 claimed completion。

Project review 默认 report-first；如果需要落本地证据，只写入被复查项目 ignored `.alphaX/` schema 允许的文件。如果本次 review 对 alphaX 机制本身有学习价值，可以另写一份脱敏机制反馈到 source checkout ignored `.alphaX/process/review-feedback/`，但不能复制项目事实。

当项目进入 PR/合入、handoff、freeze、发布、公开阶段，或项目本地 `.alphaX/`
显得过期/噪声过高时，在 `templates/project-review/report.md` 的 lifecycle hygiene
字段中复查远端状态、公开元数据、提交形态、license 姿态、tracked source 是否干净、`.alphaX/`
是否仍被 ignored，以及项目本地 `.alphaX/` 是否需要在保留未冻结证据的前提下压缩成当前状态和证据指针。

## 数据边界

`.alphaX/` 是 ignored 的本地数据面，不进入 GitHub-tracked tree。

- 项目的 `.alphaX/`：ignored 的目标项目 objective data；按 `docs/local-alphaX-schema.md` 执行，context not control。
- Source checkout `.alphaX/local/`：本机路径、准静态项目线索和本地配置。
- Source checkout `.alphaX/process/`：只放 alphaX 自身治理、source work 和 source review 的过程数据。

开源仓库只承载可复用的函数资产：合约、SOP、模板、验证规则和通用 reasoning loop。数据资产分类见 `docs/asset-boundary.yaml`。

## 发布前检查

```bash
bash scripts/verify-alpha-source.sh
bash scripts/verify-local-alphaX.sh
git diff --check
git ls-files '.alphaX/*'
```

如果 `.alphaX/` 被 Git 跟踪，说明本地数据边界被破坏，需要先修正。

公开发布基线应来自已清理的公开源码树。旧本地历史和被忽略的 `.alphaX/`
数据不得进入公开历史。

## License

MIT。见根目录 `LICENSE`。
