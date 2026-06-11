# alpha-partner 中文说明

`alpha-partner` 是 `alphaX` 的本地 source/meta base。`alphaX` 是一个带有人格化协作风格的项目协作函数，不是常驻运行实体本身。

英文公开源码是 canonical source；本文件是中文使用入口。正式合约、运行边界和 SOP 以根目录 `AGENTS.md` 为准。

## 它是什么

alphaX 是一个可复用的协作函数，用来辅助 AI 产品和软件工程工作。它可以被交付成 Skill、MCP surface、subagent 或 supervisor-agent action；这个仓库是 Markdown-first source。

它关注：

- 降低项目重新进入成本；
- 识别并复查项目风险；
- 形成有来源支撑的判断；
- 维护 contract-first 的工程链路；
- 保持实现、验证和证据可追踪；
- 沉淀紧凑的决策和证据记录。

## 运行模式

每次 alphaX 运行，在写文件前必须先判定模式。

- **Source Evolution Mode**：用户正在修改 alphaX 本身。只有直接服务于这次 alphaX source 变更时，才允许写本仓库。
- **External Assistance Mode**：用户只是用 alphaX 辅助外部项目、文档、产品问题、研究任务或工程问题。这个模式下，`alpha-partner` 是只读 source。

External Assistance Mode 下，输出只能写到目标项目、目标项目 ignored `.alphaX/`、系统临时目录，或直接在对话里报告。外部项目过程数据不得写入本 checkout 的 `.alphaX/process/`。

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

## 常用触发

中文触发是语义触发，不依赖英文源码里的字面示例。

```text
alphaX 介入一下
帮我恢复一下这个项目现场
review 一下我现在几个项目的风险
这件事真正要解决的问题是什么？
```

默认交互语言跟随用户：用户用中文，alphaX 应使用中文反馈；`D0-D3`、`P0/P1/P2`、`confidence`、`unverified_claims` 这类稳定结构字段保持不翻译。

## 目录结构

- `alphaX/`：行为、运行循环、激活、会话、pilot 和 review-agent 机制/runbook。
- `functions/`：可复用 function/SOP，目前包括 Context Reloader。
- `templates/`：研究、项目、思考、记忆和项目本地映射模板。
- `skills/`：本地 reasoning skill。
- `docs/`：研究、证据、资产边界、本地 `.alphaX/` schema 和中文入口。
- `scripts/`：源码验证、本地 `.alphaX/` 初始化和上下文快照工具。

## Review-Agent 机制

`alphaX/review-agent-mechanism.md` 定义了一个可复用的 alphaX 治理复查机制。review agent 用来检查 alphaX 自身的 contract drift、证据质量、过期状态、false completion 和弱假设。

review agent 只产出 `meta`，不得触达外部目标项目。真正运行这个机制时，使用 `alphaX/review-agent-bootstrap.md` 作为 cold-start 程序。

## 数据边界

`.alphaX/` 是 ignored 的本地数据面，不进入 GitHub-tracked tree。

- 目标项目的 `.alphaX/`：该项目的客观状态、迭代事件、证据指针和本地报告。
- 本 checkout 的 `.alphaX/local/`：本机路径、准静态项目线索和本地配置。
- 本 checkout 的 `.alphaX/process/`：只放 alphaX 自身治理和 source evolution 的过程数据。

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
