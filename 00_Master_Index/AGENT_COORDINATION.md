# FDE OS｜跨 Agent 协作入口

本文件是本地 Agent / 本地 Codex 的稳定协调入口，不替代现有 IA、Master Index、Decision Log 或 Research Notes。

## 启动入口

任何 Agent 继续 FDE OS 前，先读取：

- `00_Master_Index/LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md`

该文件包含项目目标、当前状态、证据纪律、两个 Agent 的分工、当前返工任务和 Batch 2 之后的推荐顺序。

## 当前工作批次

继续执行 GitHub Issue：

- #1 `Batch 2｜Baseline / Human Benchmark / Work Trace：研究、定义与最小工具包`
- 当前状态：部分通过，返工后复核
- 独立验收：`09_Research_Notes/RN-20260817-004-chatgpt-batch2-audit.md`

## 本地 Agent 启动规则

每次继续 FDE OS 工作前：

1. 先同步 `main`；
2. 读取 `LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md`；
3. 读取本文件；
4. 检查未关闭的 GitHub Issues 与最新评论；
5. 只执行当前批次，不自行扩张范围；
6. 完成后提交 commit，并在对应 Issue 或阶段报告中写明变更文件、证据变化、未解决问题。

## 双 Agent 协作

- Builder / Integrator：负责 canonical 文件修改与整合；
- Independent Reviewer / Research Auditor：负责独立取证、反例、证据等级与现场可执行性审核，优先通过 Issue / Audit Note 反馈，不与 Builder 并发修改同一批 canonical 文件。

详细角色、冲突处理和后续路线以 `LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md` 为准。

## 用户角色

用户只负责查看阶段报告和验收结果，不承担 Agent 之间的传话或日常仲裁职责。

## 变更原则

继续遵守 `续建工作协议_v1.0.md`：中文优先、三轮验证、最小侵入、稳定 ID 不破坏、结构性修改先提 Change Proposal。
