---
id: FDE-OS-MIDX
type: master-index
version: 0.1
updated: 2026-08-16
status-codes: Draft / Researching / Evidence-backed / Designed / Field-tested / Validated / Deprecated
note: Field-tested 与 Validated 当前为零——未经过真实项目证据不得标注（任务书 §21）
---

# FDE OS Master Index v0.1

每条规则的唯一登记处。字段：Rule ID｜主题｜当前规则（一句话）｜状态｜知识状态｜证据｜置信｜Owner｜版本｜更新日。详细展开在各模块文件；本表只做总控。

## 01 Doctrine

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| DOC-001 | FDE 定义 | 面向真实业务结果的现场交付方式：从发现到生产发布的连续责任，非驻场开发/售前/PM 单一角色 | Evidence-backed | FACT（定义层面） | EV-OAI-001/002 | High |
| DOC-002 | FDE vs 咨询/外包/SaaS/SI | 边界未研究；仅有「Deployment Leverage 差异」假设 | Researching | — | 待 G-06/G-10 | Low |
| DOC-003 | Deployment Leverage | 假设：FDE 与咨询的核心差异是部署杠杆（同类新项目现场人力递减） | Researching | HYPOTHESIS | 待 G-06 | Low |
| DOC-004 | Value Depth | 假设：Trust→Access→Mission Criticality→Value Depth 是合同深化的真实结构；Land and Expand 是事实但「越签越贵」不是定义 | Researching | HYPOTHESIS | 待 G-07 | Low |
| DOC-005 | 复杂度阶梯 | 默认从单次辅助起步，七级递升，每级升档需上级运行证据 | Designed | DESIGN DECISION（采信 L1 实践） | EV-ANT-001 | High |
| DOC-006 | 卖结果≠outcome pricing | Value Unit 与 Pricing Mechanism 分离；禁止从「不卖人天」推出「必须结果付费」 | Researching | HYPOTHESIS | 待 G-08 | Medium |
| DOC-007 | Edge→Core 学习循环 | 假设：前线碎石路应被修成 Core 高速公路；机制未知 | Researching | HYPOTHESIS | 待 G-01/G-09 | Low |
| DOC-008 | 概念隔离 | 「Field Driven Engineering（湖南样本）」≠ 本系统 FDE | Designed | DESIGN DECISION | DEC-2026-004 | High |

## 02 Operating Model

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| ORG-001 | Echo-like 角色 | 假设：业务架构/问题发现/客户关系/业务结果归口 | Researching | HYPOTHESIS | 待 G-01 | Low |
| ORG-002 | Delta-like 角色 | 假设：系统转化/数据连接/Agent/Eval/Production | Researching | HYPOTHESIS | 待 G-01 | Low |
| ORG-003 | Core 公共能力层 | 假设：沉淀 Skill/Connector/Eval/Workflow/Runtime/模板；准入与泛化评审机制未设计 | Researching | HYPOTHESIS | 待 G-09 | Low |
| ORG-004 | Client Coach | 假设：从客户内部选优秀业务专家参与 Golden Case/调教/验收（本土雏形=协会「年轻骨干」机制） | Researching | HYPOTHESIS | EV-TY-009；EV-LY 待补 | Medium-Low |
| ORG-005 | 一人多角色边界 | Unknown：现阶段谁可兼任、何时必须分设 | Draft | Unknown | 待设计 | — |
| ORG-006 | Delta 外包风险 | Unknown：外包后如何不退化为「需求定义+软件外包」 | Draft | Unknown | 待设计 | — |
| ORG-007 | 手册编写角色制 | 主编/章节负责人/项目证据负责人/技术复核/业务复核/陌生测试者六角色 | Designed | DESIGN DECISION | EV-TY-006 §18 | High |

## 03 Delivery Playbook

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| DEL-001 | 链路形态 | 候选十阶段+Gate+反馈环（非线性、可跳 Gate 须书面解释）；链路本身仍是假设 | Researching | HYPOTHESIS | DEC-2026-009 | Medium |
| DEL-002 | 准入层级 | L0-L5 六级：按当前证据决定最高允许阶段，不做一次性总放行 | Designed | DESIGN DECISION | EV-TY-002（1 次回放） | High |
| DEL-003 | 直接否决/退回/缩小 | 否决 6 条、退回 8 条、缩小 5 条（评分不得覆盖否决） | Designed | DESIGN DECISION | 闭环一设计稿 | Medium-High |
| DEL-004 | 三层记录分离 | 团队建议/业务事实确认/正式批准三记录不得合并 | Designed | DESIGN DECISION | EV-TY-002 修订动作 | Medium-High |
| DEL-005 | 指标表述纪律 | 基线确认前，准确率/覆盖率/工时/ROI 只能作评估指标不得作效果承诺 | Evidence-backed | OBSERVATION | O-5/R-C04 | High |
| DEL-006 | 高风险人工放行 | 高风险经营动作首期由 AI 组织证据与建议，放行权留原责任角色 | Designed | DESIGN DECISION（强制规则候选） | O-2 四例 | High |
| DEL-007 | 原系统默认保留 | 已有 ERP/WMS/CRM 首期不重建；接入优先级：接口→只读→文件→桌面自动化→局部工作台→局部重构 | Designed | DESIGN DECISION | O-3 三例；EV-TY-006 §3.2 | High |
| DEL-008 | Baseline 阶段方法 | 缺位：仅有 L2 准入检查项，无阶段级方法 | Draft | — | G-03 | — |
| DEL-009 | Work Trace 方法 | 缺位：方向已立（H-7），无作业设计 | Draft | — | G-04 | — |
| DEL-010 | 客户采用/ROI 阶段 | 手册第 7 章有、十阶段链缺位——链路重检时裁决 | Draft | — | G-05 | — |

## 04 Commercial Engine

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| COM-001 | 信用阶梯 | 陌生→入口→关系→判断→交易→交付→Reference→机构（八级）；用可逆承诺改造一次性信任 | Researching | INFERENCE | EV-TY-008 | Medium-High |
| COM-002 | 首单机制 | 低风险≠免费、付费≠commitment；真正变量是客户承诺向量（预算/sponsor/负责人/数据/用户/节奏/上线资源） | Researching | INFERENCE | EV-EXT-002 | Medium |
| COM-003 | Value Unit / Pricing | Unknown：各公司实证未取得 | Researching | — | G-08 | — |
| COM-004 | 四健康指标 | 假设：客户结果↑/ACV↑/单位人力↓/复用比例↑ 可作 FDE 健康度核心指标 | Researching | HYPOTHESIS | G-06 | Low |
| COM-005 | 不卖 ROI 保证 | 过程/里程碑保证（gate 未过则停），不承担不可控结果风险 | Designed | DESIGN DECISION | EV-TY-008 L120 | Medium-High |
| COM-006 | 信用归因权 | 五个必须占住的可见位置（问题定义/指标共定/评审主持/复盘作者/高层关系） | Designed | DESIGN DECISION | EV-TY-008 | Medium |
| COM-007 | 输出层信用纪律 | 官网三层信用划分；未证实宣称一律下线 | Designed | DESIGN DECISION | EV-TY-007 | High |

## 05 Field Toolkit

| Rule/Tool | 名称 | 状态 | 位置 |
|---|---|---|---|
| TOOL-001 =〔作业-准入-01〕 | 客户初步调查表（9+14+12+8+12+字段组，五选一结论） | Draft V0.1（含完整示例） | ForFlow 作业包 |
| TOOL-002 =〔作业-场景-01〕 | 候选场景比较与直接否决表（两关+场景卡+12 维比较+AI 必要性检查） | Draft V0.1（含示例） | ForFlow 作业包 |
| TOOL-003 =〔作业-准入-02〕 | 项目准入审查表（L0-L5 逐级审查+三层记录） | Draft V0.1（含示例） | ForFlow 作业包 |
| TOOL-004~020 | Qualification Sheet 之外的 17 项（任务书 §20 清单：Stakeholder Map、Work Trace、Baseline Sheet、Golden Case、Shadow Run、Go/Hold/No-Go、Bad Case Review、Edge→Core Submission 等） | 未建 | — |

## 附：编号映射表（手册体系 ↔ OS 体系）

| 手册编号 | OS 编号 | 备注 |
|---|---|---|
| 〔作业-准入-01〕 | TOOL-001 | 原编号继续使用 |
| 〔作业-场景-01〕 | TOOL-002 | 同上 |
| 〔作业-准入-02〕 | TOOL-003 | 同上 |
| 手册规范 §5.2 成熟七态 | IA §4.3 | 直接继承 |
| 手册规范 §8.10 放行六态 | GATE 放行结果 | 直接继承 |
| L0-L5 准入层级 | GATE-0 区间实现件 | 层级≠Gate，映射关系待链路重检（G-05）确认 |

## 阅读与维护

- 本表每次规则增改必须同步：模块文件、Evidence Library 对应条目、（涉及时）Decision Log。
- Owner 列暂空——待用户指派后回填（首任默认为主 Agent 建设期代管）。
