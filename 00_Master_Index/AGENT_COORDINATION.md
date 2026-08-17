# FDE OS｜跨 Agent 协作入口

本文件是 ChatGPT 与本地 Agent 的稳定协调入口，不替代现有 IA、Master Index、Decision Log 或 Research Notes。

## 当前工作批次

请先读取并执行 GitHub Issue：

- #1 `Batch 2｜Baseline / Human Benchmark / Work Trace：研究、定义与最小工具包`
- 链接：https://github.com/Cambia-Yu/tongyuan-fde-os/issues/1

## 本地 Agent 启动规则

每次继续 FDE OS 工作前：

1. 先同步 `main`；
2. 读取本文件；
3. 检查未关闭的 GitHub Issues；
4. 只执行当前批次，不自行扩张范围；
5. 完成后提交 commit，并在对应 Issue 或阶段报告中写明变更文件、证据变化、未解决问题。

## ChatGPT 复核规则

ChatGPT 负责读取本地 Agent 的提交与阶段报告，进行独立验收。若存在问题，优先在对应 Issue 中给出返工意见；不通过用户人工转述日常工作指令。

## 用户角色

用户只负责查看阶段报告和验收结果，不承担两个 Agent 之间的传话职责。

## 变更原则

继续遵守 `续建工作协议_v1.0.md`：中文优先、三轮验证、最小侵入、稳定 ID 不破坏、结构性修改先提 Change Proposal。
