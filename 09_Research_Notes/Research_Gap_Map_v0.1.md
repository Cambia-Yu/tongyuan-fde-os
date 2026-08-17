---
id: RN-GAP
type: gap-map
version: 0.1
updated: 2026-08-17
legend: 现有证据强度（High/Med/Low/None）× 对 FDE OS 的重要性（High/Med/Low）；每条 gap 指定后续检索/验证问题
---

# Research Gap Map v0.1

## 优先级矩阵

| Gap | 主题 | 现有证据 | 重要性 | 优先级 | 影响的规则 |
|---|---|---|---|---|---|
| G-01 | Palantir Echo/Delta/Core 一手机制 | **高（2026-08-17 批次完成）**：Delta=官方术语（L1）；泛化机制 L1+L2 双证；Echo 仅 L2 口述 | High | ✅ 基本关闭 | ORG-001~003、H-1、Edge→Core｜残余：Lightcone YouTube 原片复核、Echo 官方文档确认（见 RN-20260817-001 Remaining unknowns） |
| G-02 | 瓴羊一手材料（E248） | **高（2026-08-17 转写到手并全读核验，DEC-2026-012）**：六项主张全部验证+时间戳，另收获三支柱/商业模式/中国差异/成本自曝等 15 组；余项=原始音频比对 | High | ✅ 基本关闭 | ORG-004、H-2/H-7/H-8/H-9 |
| G-03 | Baseline & Benchmark 阶段方法 | **中（2026-08-17）**：TOOL-004/005 草案+跨组织方法证据+瓴羊样本；独立审核发现 Human Benchmark 与 Golden Set 仍需拆分、部分硬规则需降级 | High | Batch 2 返工后转现场验证 | DEL-008、GATE-2 |
| G-04 | Work Trace / 行为取证方法论 | **中（2026-08-17）**：TOOL-006 草案+任务挖掘侧证+瓴羊投手 90 天真实行为样本；独立审核要求补状态变化/耗时字段并放松样本硬阈值 | High | Batch 2 返工后转现场采集试点 | DEL-009、H-7 |
| G-05 | 客户采用/业务结果阶段的链路位置 | Med（手册 Ch7 与十阶段链错位） | Med | P1 | DEL 链路重检 |
| G-06 | Deployment Leverage 与四健康指标 | **中（2026-08-17）**：Palantir 单组织实证（毛利 80% vs 32%、两指标）已取得，跨组织仍缺 | High | P1（跨组织验证） | COM-004、H-4 |
| G-07 | Land & Expand vs Value Depth（事实/假设分界） | Low | Med-High | P1 | COM-002、H-5 |
| G-08 | Value Unit vs Pricing Mechanism 各公司实证 | **中低（2026-08-17）**：瓴羊 E248 已取得坐席/成本替代与效果分成两类样本；Palantir/其他组织与行业级归纳仍缺 | High | P1（跨组织验证） | COM-003、H-6 |
| G-09 | Edge→Core 泛化与防污染机制 | None | High | P1 | ORG-003、C 系统 |
| G-10 | FDE 反方观点系统收集 | None | High | P1 | 全模块（§29 十问） |
| G-11 | 受控上岗/灰度方法（Shadow→Assisted→Guarded→Full + Rollback） | **低-中（2026-08-17）**：手册有影子运行框架；瓴羊 E248 的低风险→高压力→逐步扩容样本已核，但通用方法与 Rollback 仍未系统化 | Med | P2 | DEL 阶段 07、H-9 |
| G-12 | Eval 方法（Golden Dataset 大小/构建/回归） | Low | Med | P2 | DEL 阶段 06 |
| G-13 | 内部项目 P0 材料补齐（四项目 26 项清单） | 部分 | High | P1（内部动作，非检索） | EV-TY-001~004 升级 |
| G-14 | 工具品类中立研究（按阶段能力需求→再选厂商） | None | Med | P2 | TOOL 体系、§35/36 |
| G-15 | Deployment Unit Economics（deploy 成本结构/人效曲线） | None | Med | P2 | COM-004 |

## 当前重点问题定义

### G-01 Palantir（残余项）
- Echo 是正式组织单元还是角色族？是否有官方材料进一步确认？
- Lightcone / Bob McGrew 原片对商业与组织主张逐段复核。
- Core 接受前线反馈的提交物、评审、泛化与客户定制隔离机制仍需更细证据。

### G-02 瓴羊（残余项）
- E248 转写已取得，不再做“重新获取转写”任务。
- 重要主张如进入高等级 FACT，尽量与原始音频/官方文字交叉核对。
- 继续研究 4+X 的产品化边界：标准化的是 Agent 产品、骨架、Skill、Connector、Eval 还是组合。

### G-03 Baseline / Human Benchmark
- 先完成 Issue #1 指定的最小返工：Human Benchmark 与 Golden Set 拆分；固定四维/固定统计阈值降为候选框架。
- 补 OpenAI / METR 等 primary anchors，避免二级方法文章承担过强结论。
- 后续内部动作：在真实项目取得代表性历史数据后做现场/盲测验证；没有数据继续标“未测”。

### G-04 Work Trace
- 先完成 Issue #1 指定的最小返工：补耗时、动作结果/状态变化；把 3-5 Case 定义为 initial discovery 起点而非充分样本。
- 补 Anthropic / Microsoft 等 primary anchors。
- 下一阶段必须观察真人处理真实 Case；方案流程图、SOP 或纸面推演不得升级为 Work Trace 证据。

## 内部待办（非检索，按 Gap 登记防丢失）

1. G-13：四项目 P0 清单逐项发起到客户/内部的材料请求（台账 L185-224 已列全）。
2. G-05：Batch 2 通过后做链路重检——把手册 8 章、十阶段链、L0-L5、官网五阶段、Gate 映射到一张表，裁决各阶段真实 Entry / Action / Artifact / Exit / Hold。
3. X-2：修正官网 methodology「最终」措辞（输出层，经用户确认后执行）。
4. X-7：ForFlow README 的规范路径更新为 V0.2（待用户确认后执行，本轮不动原文件）。
5. 合同 .doc 与测算 PDF 的条款提取（EV-TY-001 待办）。
