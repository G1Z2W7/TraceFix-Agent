# TraceFix Agent

面向工具调用型 AI Agent 的可验证回放、评测与安全演进系统。

## 项目目标

TraceFix Agent 计划由三个相互独立、可以单独运行的部分组成：

- **Order Sandbox API**：提供可控的订单业务、状态流转、并发场景和故障注入能力。
- **FlowPilot**：读取 OpenAPI，根据自然语言目标规划并执行多步接口调用，验证业务结果并生成测试。
- **TraceFix**：从真实 Agent Trace 中复现失败、分析原因、评估修复候选，并通过人工审核控制版本晋升。

## 当前状态

仓库处于初始化阶段。本次提交仅用于建立 `main` 默认分支。

后续开发遵循以下流程：

```text
GitHub Issue → 独立分支 → Pull Request → CI 验证 → 人工审核 → 合并
```

除本次初始化提交外，功能、架构和文档变更均通过 Pull Request 进入 `main`。

