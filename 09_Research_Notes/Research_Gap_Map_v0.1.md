---
id: RN-GAP
type: gap-map
version: 0.1
updated: 2026-08-16
legend: 现有证据强度（High/Med/Low/None）× 对 FDE OS 的重要性（High/Med/Low）；每条 gap 指定 Phase 5 的检索问题
---

# Research Gap Map v0.1

## 优先级矩阵

| Gap | 主题 | 现有证据 | 重要性 | 优先级 | 影响的规则 |
|---|---|---|---|---|---|
| G-01 | Palantir Echo/Delta/Core 一手机制 | **高（2026-08-17 批次完成）**：Delta=官方术语（L1）；泛化机制 L1+L2 双证；Echo 仅 L2 口述 | High | ✅ 基本关闭 | ORG-001~003、H-1、Edge→Core｜残余：Lightcone YouTube 原片复核、Echo 官方文档确认（见 RN-20260817-001 Remaining unknowns） |
| G-02 | 瓴羊一手材料（E248 缺失） | None（任务书转述；2026-08-17 复查仍缺失） | High | **P0** | ORG-004、H-2/H-7/H-8/H-9 |
| G-03 | Baseline & Benchmark 阶段方法 | **中（2026-08-17）**：TOOL-004/005 草案+跨组织方法证据（EV-EXT-004/005）；缺现场验证与真实基线数据 | High | 方法草案完成，降为「现场验证+数据补齐」 | DEL-008、GATE-2 |
| G-04 | Work Trace / 行为取证方法论 | **中（2026-08-17）**：TOOL-006 草案+任务挖掘侧证（EV-EXT-006）；缺真实采集与瓴羊投手样本 | High | 方法草案完成，降为「现场采集试点」 | DEL-009、H-7 |
| G-05 | 客户采用/业务结果阶段的链路位置 | Med（手册 Ch7 与十阶段链错位） | Med | P1 | DEL 链路重检 |
| G-06 | Deployment Leverage 与四健康指标 | **中（2026-08-17）**：Palantir 单组织实证（毛利 80% vs 32%、两指标）已取得，跨组织仍缺 | High | P1（降为跨组织验证） | COM-004、H-4 |
| G-07 | Land & Expand vs Value Depth（事实/假设分界） | Low | Med-High | P1 | COM-002、H-5 |
| G-08 | Value Unit vs Pricing Mechanism 各公司实证 | Low（瓴羊/Palantir 均缺） | High | P1 | COM-003、H-6 |
| G-09 | Edge→Core 泛化与防污染机制 | None | High | P1 | ORG-003、C 系统 |
| G-10 | FDE 反方观点系统收集 | None | High | P1 | 全模块（§29 十问） |
| G-11 | 受控上岗/灰度方法（Shadow→Assisted→Guarded→Full + Rollback） | Low（手册影子运行章+瓴羊转述） | Med | P2 | DEL 阶段 07、H-9 |
| G-12 | Eval 方法（Golden Dataset 大小/构建/回归） | Low | Med | P2 | DEL 阶段 06 |
| G-13 | 内部项目 P0 材料补齐（四项目 26 项清单） | 部分 | High | P1（内部动作，非检索） | EV-TY-001~004 升级 |
| G-14 | 工具品类中立研究（按阶段能力需求→再选厂商） | None | Med | P2 | TOOL 体系、§35/36 |
| G-15 | Deployment Unit Economics（deploy 成本结构/人效曲线） | None | Med | P2 | COM-004 |

## P0 检索问题定义（Phase 5 第一批）

### G-01 Palantir
- Echo 是正式组织单元还是角色族？招聘页/前员工如何描述其 Problem Discovery 与价值定义职责？
- Delta 与 Echo 的协同界面是什么？Delta 有无产品修改权（本地 fork → 上浮）？
- Core 接受前线反馈的实际流程：提交物形态、评审机制、泛化判据、客户定制隔离方案。
- 人物线索：Bob McGrew、Nabeel Qureshi（后加入 OpenAI Deploy Co）、Barry McCardel（Sixteen？——注意人物-组织对应待核实）。
- 信源次序：Palantir 官方 Blog/招聘页 → 前员工长访谈（L2）→ 播客（L3，须回溯引用）。

### G-02 瓴羊
- 首选动作：重新获取 E248 转写（用户授权后从小宇宙抓取，或用户提供本地文件）；如不可得，检索朋新宇其他一手访谈交叉验证六项主张。
- 4+X 的产品化边界：瓴羊标准化的到底是 Agent 产品还是骨架/Skill/Connector/Eval（任务书 §10.5 之问）。

### G-03 Baseline
- 检索：企业 AI 项目 baseline 建立方法（人工参照系/human benchmark）、Palantir「先测量现状再部署」实践、瓴羊基线做法。
- 内部动作：为四个已发生项目回溯补建「最低基线」（审核量/单笔时间/异常比例/人工投入——回放文件 L87 已列出字段）。

### G-04 Work Trace
- 检索：process mining 在 Agent 训练中的应用、expert demonstration/golden case 构建、human feedback 采集设计。
- 与 G-02 投手案例、EV-EXT-001 网易方法合并分析，产出「Work Trace 采集作业草案」（TOOL）。

## 内部待办（非检索，按 Gap 登记防丢失）

1. G-13：四项目 P0 清单逐项发起到客户/内部的材料请求（台账 L185-224 已列全）。
2. G-05：链路重检工作坊——把手册 8 章、十阶段链、L0-L5、官网五阶段四方对齐成一张表，显式裁决 Baseline 与客户采用两个缺位。
3. X-2：修正官网 methodology「最终」措辞（输出层，经用户确认后执行）。
4. X-7：ForFlow README 的规范路径更新为 V0.2（待用户确认后执行，本轮不动原文件）。
5. 合同 .doc 与测算 PDF 的条款提取（EV-TY-001 待办）。
