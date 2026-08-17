---
id: FDE-OS-IA
type: architecture
version: 0.1.1
updated: 2026-08-18
status: draft
---

# FDE OS 信息架构 v0.1

正式名称：**通元问科 FDE 交付操作系统**（Tongyuan FDE Operating System，简称 FDE OS）。

本文档定义 FDE OS 的模块划分、编号体系、状态词汇、层级关系和文件结构。它是所有后续模块建设的宪法性文件；修改本文档必须登记 Decision Log。

---

## 1. 一个先行判断：FDE OS 不是从零开始

本地审计（见 `Existing_FDE_Knowledge_Audit.md`）确认：交付维度的元系统已经存在——

- 《FDE手册编写与现场验证规范》V0.2（2026-07-24）已定义证据等级、成熟状态、四层验证、四张控制台账、四个建设闭环；
- ForFlow「FDE手册第一版」工作台已按该规范启动闭环一（项目准入），产出证据台账、历史回放与三个工具草案。

因此 FDE OS 的正确建设方式是：**以手册规范为 03/05 模块的编写宪法，向外扩展 Doctrine、Operating Model、Commercial Engine 三个缺失维度**，而不是另起炉灶重写交付流程。

| 已有资产 | 在 FDE OS 中的位置 | 处置方式 |
|---|---|---|
| 手册编写规范 V0.2 | 03/05 的编写与验证宪法 | 原位保留，引用不迁移 |
| ForFlow 手册第一版（闭环一） | 03 阶段 00-01 + 05 工具的在建件 | 原位保留，Master Index 挂链 |
| deep-research-report（信用阶梯） | 04 商业引擎的输入研究 | 引用 |
| tongyuan-wenke 官网内容 | 08 输出层产物 | 反向校验对象（输出不得修改事实） |
| Obsidian vault 商业判断笔记 | 06 证据库的公司事实来源 | 引用 |

---

## 2. 模块地图

```text
Tongyuan-FDE-OS/
├── 00_Master_Index/        系统总控：Master Index、信息架构、阅读指南
├── 01_Doctrine/            我们相信 FDE 是什么（定义、边界、杠杆原理）
├── 02_Operating_Model/     公司怎样组织才能做 FDE（角色、决策权、Edge→Core）
├── 03_Delivery_Playbook/   一个项目具体怎样跑（阶段 + Gate + 反馈环）
├── 04_Commercial_Engine/   怎样避免成为卖人天的咨询公司（定价、信用、杠杆）
├── 05_Field_Toolkit/       现场拿什么干活（可填写工具，非解释文章）
├── 06_Evidence_Library/    证据库（每条证据说明它证明了什么）
├── 07_System_Map/          总图（主体结构稳定后生成）
├── 08_Outputs/             从母体编译出的对外输出（官网/提案/JD/培训）
├── 09_Research_Notes/      研究笔记 RN-YYYYMMDD-XXX + 审计文档
├── 10_Decision_Log/        设计决定记录 DEC-YYYY-NNN
└── _archive/               已替代内容
```

四套子系统与模块的对应（任务书 §2）：

| 子系统 | 主模块 | 支撑模块 |
|---|---|---|
| A 问题解决系统 | 03（阶段 00-04） | 05、06 |
| B 交付运行系统 | 03（阶段 05-08） | 05、06 |
| C 产品学习系统 | 02（Edge→Core）+ 03（阶段 09） | 06 |
| D 商业系统 | 04 | 06 |

---

## 3. 编号体系（稳定 ID，不依赖标题）

| 前缀 | 对象 | 示例 | 规则 |
|---|---|---|---|
| DOC-NNN | Doctrine 规则 | DOC-001 | 语义变化时旧号废弃进 _archive，不回收复用 |
| ORG-NNN | Operating Model 规则 | ORG-003 | 同上 |
| DEL-NNN | Delivery Playbook 规则 | DEL-012 | 同上 |
| COM-NNN | Commercial Engine 规则 | COM-004 | 同上 |
| TOOL-NNN | Toolkit 工具 | TOOL-007 | 对接手册规范「作业-XX-NN」体系（见 §7） |
| GATE-N | 阶段闸门 | GATE-4 | 全局唯一，阶段可跳、闸门语义不变 |
| EV-XXX-NNN | 证据条目 | EV-PAL-001 | XXX=组织码（PAL/LY/OAI/TOM/TY/EXT） |
| DEC-YYYY-NNN | 设计决定 | DEC-2026-001 | 只增不改，修订走新 DEC |
| RN-YYYYMMDD-NNN | 研究笔记 | RN-20260816-001 | 每轮研究必留 |
| ASSET-XX-NNN | 能力资产 | 沿用手册规范附录二体系 | 登记在手册资产索引，OS 只挂链 |

组织码：PAL=Palantir，LY=瓴羊，OAI=OpenAI，TOM=Tomoro，TY=通元问科内部，EXT=其他外部组织。

---

## 4. 三层状态词汇（严格区分，不得混用）

### 4.1 知识状态（给「判断/主张」用，任务书 §14）

| 状态 | 含义 | 判定标准 |
|---|---|---|
| FACT | 公开证据明确支持 | 有 L1/L2 证据且无反例 |
| OBSERVATION | 多个案例重复出现 | ≥3 个独立案例呈现同一模式 |
| INFERENCE | 根据证据做出的合理推断 | 明确写出推理链 |
| DESIGN DECISION | 通元问科选择采用的方法 | 有 DEC 编号 |
| HYPOTHESIS | 尚未经真实项目验证 | 写明验证途径 |

### 4.2 证据等级（给「来源」用，任务书 §13）

L1 官方/原始 → L2 一手从业者 → L3 高质量二次解释 → L4 我们的推断/重构 → L5 设计假设。

### 4.3 成熟状态（给「规则/工具/资产」用，继承手册规范 §5.2）

草拟 → 内部演练 → 单项验证 → 重复验证 → 稳定做法（另有：暂停使用 / 已替代）。

**三者的关系**：一条规则的「知识状态」回答它是不是真的；「成熟状态」回答它被验证到什么程度；规则引用的每条证据有自己的 L 等级。一条规则可以是 DESIGN DECISION（我们选择如此）同时是稳定做法（内部反复验证过），但绝不能把 DESIGN DECISION 写成 FACT。

### 4.4 与手册规范「依据类型」的对接

手册规范的四类依据（公开实践/项目验证/公司规则/待验证判断）在 FDE OS 中继续使用，映射：

- 公开实践 ≈ 支撑 FACT/OBSERVATION 的 L1/L2 来源；
- 项目验证 ≈ TY 内部证据（EV-TY-*）；
- 公司规则 ≈ DESIGN DECISION；
- 待验证判断 ≈ HYPOTHESIS 或 INFERENCE。

---

## 5. Delivery Playbook 阶段与 Gate 骨架（v0.1 候选，允许研究后修改）

十阶段候选链（任务书 §3，状态：HYPOTHESIS，待公开证据重检线性假设）：

```text
00 Qualification        项目资格判断          ←→ 手册规范第2章；闭环一在建
01 Problem Discovery    高价值问题发现        ←→ 手册规范第2章
02 Baseline & Benchmark 业务基线/人工参照系  ←→ 手册规范未显式覆盖【缺口G-03】
03 Work Trace           工作行为取证/流程建模 ←→ 手册规范第3章部分覆盖【缺口G-04】
04 Agent Readiness      数据/系统/权限验证    ←→ 手册规范第3-4章
05 MVP                  最小价值验证          ←→ 手册规范第5章
06 Eval                 评测                  ←→ 手册规范第5章
07 Controlled Deploy    受控上岗/边界测试     ←→ 手册规范第5-6章（影子运行）
08 Production           生产运营/持续学习     ←→ 手册规范第6章
09 Generalization       复制/产品化/入Core    ←→ 手册规范第8章
```

注意：手册规范第 7 章「客户采用、业务结果与 ROI」在十阶段链中没有对应位（并入 06/08 之间作为独立关注点），这是链路假设的一个已知待解问题（详见 Gap Map G-05）。

Gate 候选（任务书 §34）：GATE-0 值不值得做 / GATE-1 问题定义明确 / GATE-2 基线存在 / GATE-3 AI 就绪 / GATE-4 MVP 证明价值 / GATE-5 Eval 达标 / GATE-6 生产风险可接受 / GATE-7 值得 Scale。放行结果沿用手册规范六态：通过/有条件通过/退回补充/缩小范围/暂停/终止。跳 Gate 必须书面解释并留 DEC。

**L0-L5 与 GATE 的关系（2026-08-18，R-4 候选映射/设计决定，DEC-2026-013）**：两套体系正交——L0-L5 是证据准入层级（当前证据最多允许进入哪级工作），GATE 是阶段放行判断；多对多映射（L2↔GATE-1/2 区间、L3↔GATE-3/4、L4↔GATE-5/6、L5↔GATE-6/7；L1 与 GATE-7 无对应），禁止一一配对。**该映射为候选性质，待真实 Gate 运行验证**（GATE-0~7 全部未执行过）。详见 `03_Delivery_Playbook/链路对齐总表_v0.1.md` §4 R-4。

每个 Playbook 阶段必须五件套（硬要求，任务书 §33）：Purpose / Entry Criteria / Actions / Exit Criteria / Artifacts（对接手册规范 §8 的十四节单章结构——五件套是其最小公约数）。

---

## 6. 阅读层级

| 层级 | 时长 | 入口 | 回答 |
|---|---|---|---|
| L1 | 5 分钟 | 07_System_Map | FDE OS 是什么 |
| L2 | 30 分钟 | 03 各阶段卡 | 这一阶段该怎么做 |
| L3 | 现场 | 05 工具 | 我现在填什么、问什么、判断什么 |

---

## 7. 与既有编号体系的并存规则

手册规范已定义「〔作业-场景-01〕」「〔资产-评测-03〕」角标体系。为避免双轨，规则如下：

1. 手册作业包与资产索引**继续使用**其原编号体系，FDE OS 的 TOOL-NNN 仅作为 OS 内的二级索引指向它们；
2. FDE OS 新建工具（超出手册范围，如 Stakeholder Map、Edge→Core Submission）使用 TOOL-NNN；
3. 两套编号的映射表维护在 Master Index 附表。

---

## 8. 变更控制

- 本文档版本进入 frontmatter；重大结构调整须新开 DEC 并在 10_Decision_Log 登记；
- 模块内文件命名遵循「主题_vX.Y.md」，系统稳定后主文件改固定名、版本进 frontmatter（任务书 §41）；
- 任何文件被 _archive 替代时保留原文件与替代关系说明。
