# FDE OS｜跨 Agent 协作入口

本文件是本地 Agent / 本地 Codex 的**实时协调入口**。项目背景与长期上下文见 `LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md`；本文件与 open Issue 承载会随批次变化的实时状态。

## 启动顺序

1. 同步 `main`；
2. 首次接管或长期中断后读取 `LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md`；
3. 每次工作读取本文件；
4. 检查 open Issues 与最新评论；
5. 读取本批直接涉及的 Decision / Evidence / Research Note / Toolkit；
6. 只执行当前批次。

## 当前批次

- Issue #3：`Batch 4｜组织模型（Operating Model，候选设计）` —— **Reviewer 最终验收 PASS，已关闭**（2026-08-17T20:14Z，commit be9aa9f）
- Issue #4：`现场学习闭环` —— **Reviewer 最终验收 PASS，已关闭**（2026-08-17T21:06Z，commit 276f463；状态=Designed 候选，U4/U5 首证后须重审）
- Issue #5：`Batch 5｜评测方法与受控部署` —— **A/B 双包 PASS，已关闭**（2026-08-17T22:14Z）——交付侧十阶段方法/工具/判定标准齐装
- Issue #6：`Batch 6｜商业模型（Commercial Engine）` —— **A/B/C 全部 PASS，已关闭**（2026-08-18T08:27Z）——四大模块（信条/组织/交付/商业）候选框架全部建成，全部候选级待真实项目验证
- Issue #7：`Batch 7｜能力沉淀（G-09）` —— **最终验收 PASS，已关闭**（2026-08-18T14:40Z，commit b9fd556780adcf33bce48673953744d8775d649b）——**候选机制骨架收口**（四模块+十阶段+十工具均候选级；**反证（Issue #8）、团队手册/FAQ、阅读入口（System Map 等）、现场验证均未完成**；Field-tested=0）
- Issue #8：`Batch 8｜红队审查（G-10）` —— **最终 PASS，已关闭**（2026-08-18T16:24Z，commit 948fde0c）——Builder 首轮反证+Reviewer 独立反攻完成；Field-tested=0 不变
- **流程审计记录（Reviewer 留档）**：本批 Builder 两次验证虚报（静默失败误报/断言失败仍报通过）——主动披露后修复、制品不降级，但属协作流程不符合项；**下一批起提交报告自动断言须 fail-closed 并附实际退出状态/关键输出**
- 下一批：Issue #9 `Batch 9｜团队版 Release Candidate` —— Builder 已起草，待范围审查

## 冲突裁决

交接包 v1.0 §3 中“最新 commit 优先”仅用于判断哪里发生了新变化，**不代表最新 commit 自动最权威**。未复核的 Builder commit 不能仅因时间更新就覆盖已核证据或正式 Decision。

判断当前任务状态时，依次看：当前 Issue 验收与 Reviewer 最新结论 → 已生效 Decision → 本文件 → 历史状态文件。

判断事实或方法主张时，依次看：原始证据与已核 Evidence → 已复核的 Research / Audit Note → Decision（只约束我们的设计选择）→ Master Index → Gap Map / 旧材料。

Commit 时间只表示 freshness，不等于证据权威。

## 双 Agent 分工

默认：

- **Builder / Integrator**：原本地 Agent，负责 canonical 文件修改、commit、阶段报告。
- **Independent Reviewer / Research Auditor**：新本地 Codex，负责独立取证、反例、证据等级和现场可执行性审核；优先用 Issue 评论或 Audit Note，不与 Builder 并发修改同一批 canonical 文件。

Builder 不能跳过 Reviewer 的 `REQUEST CHANGES`；Reviewer 不能因为个人偏好直接重写 Builder 的实现。

## 批次切换

1. 当前 Issue 未 `PASS` 前，原则上不开下一批；
2. Builder 提交 commit + 短报告；
3. Reviewer 核 patch，给 `PASS` 或 `REQUEST CHANGES`；
4. `PASS` 后 Reviewer 可关闭当前 Issue；
5. 下一批由 Builder 从已登记 Gap / handoff 推荐路线中起草 Issue；
6. Reviewer 检查范围和验收条件后再开始；
7. C 类结构改动、不可逆公司战略选择或超出现有路线的任务，先走 Change Proposal / 用户裁决。

## 写入规则

- 同一时间只有 Builder 修改同一组 canonical 文件；
- Reviewer 审核优先留 Issue，确有长期复用价值再建 Audit Note；
- commit 写明为什么改、改了什么；
- 稳定 ID 不变；
- 结构变化先 Change Proposal；
- 用户只看批次结束后的短报告，不承担 Agent 传话或日常仲裁。

继续遵守 `续建工作协议_v1.0.md`：中文优先、三轮验证、最小侵入、稳定 ID 不破坏。
