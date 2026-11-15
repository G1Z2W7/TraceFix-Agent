# TraceFix Agent

TraceFix Agent 用可验证的回放和回归评测帮助开发者定位 Agent 故障，并安全审核修复候选。

## 项目解决什么问题

工具调用型 Agent 的一次失败通常跨越模型、检索、状态和外部 API。Trace 可以展示调用过程，但开发者仍需手动复现故障、判断原因和检查回归。

本项目把一次失败转换成可重复执行的测试用例。系统生成修复候选后，会在目标失败集和历史成功集上运行评测。人工审核者决定是否接受候选。

## 系统组成

- **Order Sandbox API** 提供订单状态流转、并发控制、异步事件和故障注入。
- **FlowPilot** 读取 OpenAPI，并根据自然语言目标执行多步接口调用。它会验证业务结果并生成 pytest 测试。
- **TraceFix** 导入 Agent Trace，创建安全回放，分析故障，并评估受限的配置变更。

## 安全边界

- TraceFix 不自动修改或发布生产代码。
- 回放默认禁止访问外部网络，并使用固定工具响应。
- 修复候选只能修改登记过的 Prompt、Tool Schema、检索配置或路由配置。
- 人工审核者批准后，候选才能晋升。

## 当前状态

项目处于工程规则建设阶段。产品代码尚未开始。

查看以下文档了解范围和开发计划：

- [项目章程](docs/PROJECT_CHARTER.md)
- [交付路线图](docs/ROADMAP.md)
- [贡献指南](CONTRIBUTING.md)
- [中文学习指南](docs/zh-CN/LEARNING_GUIDE.md)
- [架构决策记录](docs/adr/README.md)

## 开发流程

除仓库初始化提交外，所有变更都遵循以下流程：

```text
GitHub Issue -> 独立分支 -> Pull Request -> CI 验证 -> 人工审核 -> 合并
```

`main` 必须保持可运行。Pull Request 必须包含验收证据、失败用例、风险和回滚说明。

## 文档语言

README 和学习文档使用中文。公共接口、架构规范和代码标识符使用英文。英文技术规范是发生歧义时的依据。

## 安全问题

不要在公开 Issue 中提交令牌、凭据、个人数据或未脱敏 Trace。按照[安全策略](SECURITY.md)私下报告漏洞。

## 许可证

本项目使用 [Apache License 2.0](LICENSE)。

