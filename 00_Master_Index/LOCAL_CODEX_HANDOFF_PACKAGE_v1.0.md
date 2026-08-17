---
id: LOCAL-CODEX-HANDOFF-v1.0
type: project-handoff
project: Tongyuan FDE Operating System
created: 2026-08-17
language: zh-CN
status: active-handoff
scope: 两个本地 Agent 接管 FDE OS 后续研究、建设、复核与 GitHub 协作
---

# 通元问科 FDE OS｜本地 Codex 双 Agent 全量交接包 v1.0

## 0. 先读这段

你正在接管的不是一篇文章、一个 PPT，也不是一个“FDE 方法论概念研究”。

你正在继续建设：

**通元问科 FDE 交付操作系统（Tongyuan FDE Operating System / FDE OS）**。

目标是让一名新的 FDE 在进入真实企业项目后，能够判断：

- 当前项目处于什么状态；
- 还缺什么证据；
- 下一步应该收集什么、问什么、做什么；
- 谁负责；
- 做到什么算完成；
- 哪些条件必须 Hold；
- 哪些经验应沉淀为可复用能力；
- 下一次部署是否因为本次积累而更轻、更快、更可靠。

**仓库 `main` 是 canonical baseline。不要从零重做。**

本交接包的目的，是让两个本地 Agent 可以在 GitHub 中自行协作，用户只看阶段报告和验收结果，不承担传话职责。

---

# 1. 用户真正要什么

用户要的是一套能进入真实企业现场的 FDE Operating System，而不是“看起来系统化”的知识库。

判断一项产出有没有价值，优先问：

> **它有没有改变现场判断、现场动作、验证方式或下一次复用？**

如果只是增加术语、框架、目录、文章，但不能让执行者更清楚下一步做什么，就不要优先写入核心 OS。

用户会严格审核以下问题：

1. 结论是否有证据，还是 Agent 想当然；
2. 事实、观察、推断、设计决定、假设有没有混写；
3. 有没有把某一家公司的做法泛化成行业规律；
4. Toolkit 是否真的能指导现场，而非只是漂亮模板；
5. 有没有把 PoC、纸面推演、Demo 写成生产结果；
6. 有没有为了“更完整”大范围重构既有体系；
7. 中文是否足够清楚，用户能否直接阅读。

用户不希望看到冗长的过程汇报。阶段报告要短、可验收、结论明确。

---

# 2. 语言与变更原则

## 2.1 中文优先

面向人阅读和执行的新内容默认中文为主体，英文只作为术语别名：

- 现状基线（Baseline）
- 人工参照系（Human Benchmark）
- 黄金集（Golden Set / Golden Dataset）
- 工作行为轨迹（Work Trace）
- 受控部署（Controlled Deployment）
- 部署杠杆（Deployment Leverage）

稳定 ID、机器字段、已有目录不要为了中文化而改名，例如：

`DOC-001`、`ORG-003`、`EV-LY-001`、`00_Master_Index`。

不要制造中英文两套平行 canonical 文档。

## 2.2 最小侵入

默认顺序：

**理解现状 → 找缺口 → 补证据 → 局部修正 → 留痕。**

不要：

- 批量重命名；
- 重写旧 Decision；
- 改稳定 ID；
- 为统一格式重构全库；
- 因为一个新框架就重写 Doctrine；
- 删除历史错误来“让仓库看起来干净”。

历史 Decision 记录“当时知道什么”，后续事实变化用新 Decision / 更正说明更新，不回写历史。

---

# 3. 遇到仓库内部冲突时，相信谁

当前仓库已有少量状态不同步，不允许只读一张表就下结论。

例如：后续 commit 已取得 E248、补充瓴羊定价与 Work Trace 证据，但某些较早的 Gap Map 行仍保留旧表述。

因此读取优先级固定为：

1. **最新 commit 与当前 open Issue 的最新评论**；
2. **Evidence Library + Decision Log + 最新 Research Notes / Audit Notes**；
3. **Master Index**；
4. **Open Questions**；
5. **Research Gap Map**；
6. 较早任务书、旧报告、旧快照。

发现冲突时：

- 不自行删旧记录；
- 先确认是不是“历史状态后来被更新”；
- 用更正、Decision 或局部状态同步解决；
- 结构性冲突才提交 Change Proposal。

---

# 4. 当前 FDE OS 的母架构

FDE OS 不是一个文件，而是一套母系统。

核心模块：

1. `01_Doctrine`：FDE 是什么，和咨询、外包、SaaS、SI 的边界；
2. `02_Operating_Model`：前线角色如何协作，Edge 与 Core 如何联动；
3. `03_Delivery_Playbook`：项目从问题发现到生产与泛化的阶段、Gate 与动作；
4. `04_Commercial_Engine`：价值单位、定价、Land & Expand、部署杠杆与单位经济；
5. `05_Field_Toolkit`：现场直接使用的表单与工具；
6. `06_Evidence_Library`：所有 Rule 的证据底座；
7. `07_System_Map`：5 分钟能看懂系统如何运行；
8. `08_Outputs`：官网、CEO Blog、客户 PPT、培训等编译输出；
9. `09_Research_Notes`：研究过程、来源与反例；
10. `10_Decision_Log`：重要设计决定与历史状态。

输出层不能为了好看改变母系统事实。

---

# 5. 当前正在验证的核心闭环

以下是**系统级假设，不是已经被证明的行业事实**：

> 发现高价值问题 → 进入真实企业工作 → 建立现状基线 → 找到人工参照与优秀行为 → 观察 Work Trace → 构建最小价值证明 → Eval → 受控部署 → 生产运行 → Good/Bad Case 学习 → 抽象成 Skill / Connector / Eval / Workflow / Runtime / 模板 → 下一次部署更轻 → 获得更深业务访问 → 解决更高价值问题。

最终需要检验的是：

- 客户结果是否提升；
- 单位价值所需部署人力是否下降；
- 可复用产品/能力占比是否提高；
- 项目是不是越来越进入高价值、关键业务。

如果客户越来越多、现场人数也线性增长、每个项目都从零重做，那么不管名称叫什么，都更接近专业服务而非高杠杆 FDE 模型。

---

# 6. 交付链：当前只是假设，不得当最终 SOP

现有讨论形成的 0-9 链路：

0. 项目资格判断（Qualification）
1. 高价值问题发现（Problem Discovery）
2. 现状基线与人工参照（Baseline / Human Benchmark）
3. 工作行为轨迹（Work Trace）
4. 数据 / 系统 / 权限准备度（Agent Readiness）
5. 最小价值证明（MVP / Minimum Value Proof）
6. Eval
7. 受控部署（Shadow → Assisted → Guarded Automation → Autonomous / Full）
8. 生产运行与学习
9. 泛化 / 产品化（Generalization / Edge→Core）

这条链不是瀑布，应该最终表现为：

**阶段 + Gate + 反馈回路。**

现有手册 8 章、十阶段链、L0-L5、官网五阶段并未完全对齐。`G-05` 仍需正式裁决。

不要现在大改十阶段链；等 Batch 2 收尾后再做链路重检。

---

# 7. Baseline / Human Benchmark / Golden Set / Work Trace：必须分清

这是当前最重要的方法边界。

## 7.1 现状基线（Baseline）

回答：

> **AI 介入前，这项工作目前实际做到什么水平？**

它是后续效果、ROI、效率改善、质量改善的比较起点。

需要有：

- 明确业务 outcome；
- 指标公式与统计单元；
- 时间窗口；
- 样本来源；
- 纳入 / 排除条件；
- Case mix / 季节性 / 代表性说明；
- 可追溯数据来源。

成本、时长、质量、量可以作为**默认检查维度**，但不是所有场景都必须四项齐全的万能规则。

单次“这笔做了两天”不是 Baseline。

## 7.2 人工参照系（Human Benchmark）

回答：

> **在同样任务、同样 Case、尽可能可比的条件下，人实际能做到什么水平？**

应根据场景记录人类表现，例如：

- 结果质量 / 成功率；
- 完成时间；
- 人力 / 成本；
- 求助 / 升级；
- 合格水平、典型水平、优秀水平。

不要预设万能百分位，也不要把“最厉害员工的一次表现”直接当 Ground Truth。

## 7.3 黄金集（Golden Set）

回答：

> **什么答案、结果或行为在业务上被认为是正确 / 优秀的权威参照？**

它主要服务 Eval。

典型方法：真实 Case → 多人独立判定 → 分歧显性化 → 仲裁 → 版本冻结。

Human Benchmark 和 Golden Set 有关联，但不是一件事。

## 7.4 工作行为轨迹（Work Trace）

回答：

> **真实人员处理真实 Case 时到底看了什么、做了什么、什么信息改变判断、何时求助、动作造成了什么结果？**

最小结构建议：

`Case → 信息/材料 → 动作 → 判断 → 动作结果/状态变化 → 下一步 → 分支 → 求助/升级 → 最终结果`

必须分开：

- 直接观察到的事实；
- 人员事后自述；
- Agent/研究者自己的推断。

Work Trace 不是复制人的所有动作。

观察到的动作要区分：

- 业务 / 决策逻辑候选；
- 系统摩擦；
- 混合待核。

影子 Excel、复制粘贴等动作有时是低效摩擦，有时却承载未成文业务规则，不能自动删除。

---

# 8. 当前组织模型：已知与假设必须分开

## 8.1 Palantir 已较强支持的部分

当前 Evidence 已支持：

- Delta 是 Palantir 官方使用的前线部署工程角色术语；
- Edge 工作会通过产品团队、产品开发 / review / 多客户场景抽象等机制回到 Core；
- FDE 与核心产品团队之间存在持续张力与泛化机制。

Echo 的细节主要来自前高管 / 从业者口述，证据弱于 Delta，不要写成同等级官方事实。

## 8.2 通元问科当前组织假设

当前候选是“2+1+1”项目单元：

- Echo-like：业务问题、价值定义、客户关系 / outcome owner；
- Delta-like：数据、系统、Agent、Eval、Production；
- Shared Core：沉淀 Skill / Connector / Eval / Workflow / Runtime / 模板；
- Client Coach：客户内部优秀业务人员 / 主管参与 Golden Case、调教和验收。

这仍是**通元问科的设计假设**，不是 Palantir 原样复制。

关键防线：Delta 不能退化成“Echo 写需求、Delta 接外包单”。Echo 和 Delta 应共同对业务结果负责。

---

# 9. 商业模型：目前最重要的判断

## 9.1 Deployment Leverage

FDE 与咨询的关键研究变量不是“是否驻场”，而是**部署杠杆是否形成**。

健康方向假设：

- 客户价值深度上升；
- 合同价值 / ACV 有机会提升；
- 单位价值对应的人力投入下降；
- 可复用产品能力占比提升。

这些指标目前仍需跨组织与本公司项目验证，不得当成熟 KPI 宣传。

## 9.2 Trust → Access → Mission Criticality → Value Depth

这是目前对 Land & Expand 的解释假设：

早期解决可验证问题 → 建立信任 → 获得更多系统 / 数据 / 业务访问 → 进入更关键工作 → 价值单位变大。

“早期便宜、后期一定更贵”不是定义，只是可能结果。

## 9.3 Value Unit ≠ Pricing Mechanism

必须分开：

- Value Unit：客户为什么付钱——解决的问题、持续业务结果、持续能力；
- Pricing Mechanism：怎么收费——license、项目费、usage、席位、效果分成、hybrid。

不要把“卖结果”自动写成“必须按 ROI 分成”。

瓴羊 E248 已提供两个具体收费样本：坐席 / 成本替代与超人工基线的效果分成；它证明瓴羊怎么做，不证明整个 FDE 行业都应如此。

---

# 10. 关键证据源地图

## A. 瓴羊 E248｜中国一手实践样本

文件：

`09_Research_Notes/Source_Materials/E248_硅谷101_对话瓴羊朋新宇_FDE落地实践_1小时03分钟.txt`

当前用途：

- 业务目标、业务数字、历史记录作为度量起点；
- 岗位标杆；
- 顶尖投手 90 天、一万多次真实行为；
- 数据采集 → 建模 → 执行 → 迭代；
- Client Coach / 首席教练；
- MVP / AB Test；
- 灰度上岗；
- 标准化 / 个性化边界；
- 两类收费方式；
- 拒绝“千人天”式低杠杆定制。

注意：

- 区分朋新宇原话与主持人总结；
- 转写可能有 ASR 错字；
- 如重要主张进入高等级 FACT，应尽量对原音频 / 官方访谈交叉核对。

## B. 32 分钟 FDE 二次解读

文件：

`09_Research_Notes/Source_Materials/FDE_Palantir_Bob_McGrew_二次解读_32分钟.md`

用途：

- 发现 Echo / Delta；
- 碎石路 → 高速公路；
- 产品杠杆；
- Land & Expand；
- FDE 退化成咨询的风险；
- 回溯 Bob McGrew / Palantir 原始资料。

它是二次解释，不作为 Palantir L1 事实来源。

## C. Palantir

优先顺序：

Palantir 官方 → 一手前员工 / 高管长访谈 → 高质量二次解读。

当前研究笔记：

`09_Research_Notes/RN-20260817-001-palantir-echo-delta-core.md`

## D. OpenAI / Tomoro

重点研究：

- FDE 从诊断 / workflow 选择到生产部署的连续责任；
- Eval / Golden Set；
- Deployment Company；
- build → prove → generalize 是否存在可验证机制。

涉及 2026 当前组织事实时必须回官方最新来源，不要依赖旧记忆。

---

# 11. 证据与知识状态纪律

每条重要判断要同时回答两个不同问题：

1. **来源有多可靠？**
2. **我们对这条主张知道到什么程度？**

知识状态继续使用：

- FACT
- OBSERVATION
- INFERENCE
- DESIGN DECISION
- HYPOTHESIS
- Unknown / Insufficient Evidence

现有 Evidence L1-L5 与知识状态存在语义重叠问题，已登记 `OQ-001`。

在 Change Proposal 触发条件满足前，不改 schema。

### 研究规则

- 单一公司的事实只能先写成该公司事实；
- 行业级 OBSERVATION 原则上需要多个独立组织；
- Secondary source 可以发现结构，不能自动升级为 Primary fact；
- Unknown 就写 Unknown；
- 没有 baseline 不写 ROI；
- Demo 成功不等于生产；
- PoC 不等于上线；
- 客户口头满意不等于业务结果。

---

# 12. 当前 Open Questions

至少保留：

## OQ-001
Evidence L4/L5 与知识状态 INFERENCE / HYPOTHESIS 的语义重叠。

当前不改架构，观察是否真的造成使用错误。

## OQ-002
DOC-001 不能只靠 OpenAI 定义整个 FDE 类型。

需要 Palantir + OpenAI + Tomoro / 瓴羊 / 其他组织形成交集分析。

累计到至少 3 个相对独立组织后再裁决通元问科 Doctrine。

## 新风险：公开仓库中的完整第三方转写

当前仓库是 public，且已存入完整第三方播客转写。

不要继续把更多完整第三方版权材料复制进公开 repo。

现有两份文件不要擅自删除，因为它们是用户明确要求写入；但后续应评估是否迁移为“私有原始资料 + GitHub 仅保留来源元数据 / 必要短摘录 / hash / Research Note”的结构。

这属于治理风险，不是本批返工任务，除非用户另行授权。

---

# 13. 当前最紧急任务：完成 Issue #1 Batch 2 返工

当前状态：

**部分通过，Issue #1 仍 open。**

独立验收记录：

`09_Research_Notes/RN-20260817-004-chatgpt-batch2-audit.md`

不要重做 Batch 2，只做 B 类最小返工。

## P0-1 TOOL-005

必须把 Human Benchmark 与 Golden Set 分开。

可以继续保留一个文件，但至少有两个独立 section / output：

### Human Benchmark

记录同条件下人的实际表现。

### Golden Set

记录什么答案 / 行为经过业务确认可作为 Eval 权威参照。

不要再把“多人标注+仲裁”当成 Human Benchmark 的全部。

## P0-2 TOOL-004

调整：

- 先写 Primary Business Outcome；
- 成本 / 时长 / 质量 / 量降为候选维度；
- 补 Case mix / 季节性 / 代表性；
- 删除“不报均值”等绝对规则；
- “完整业务周期”降为建议，不是通用硬阈值。

## P0-3 TOOL-006

调整：

- 增加耗时字段；
- 增加动作结果 / 状态变化字段；
- “首日数据废弃”降为观察反应性风险与 pilot 建议；
- 3-5 Case 只作为 initial discovery 起点；
- 是否够用看轨迹饱和度与关键异常覆盖。

## P1 Evidence

EV-EXT-004~006 目前证据等级表述偏强。

补 primary anchors：

- OpenAI：Evals / Golden Set / 真实工作流；
- METR：Human baseline（同任务、同条件的人类实际完成表现）；
- Anthropic：agent trajectory / transcript / state changes；
- Microsoft：Task Mining / actual desktop interactions。

保留已有来源，不必删除。

IAA / κ 只在输出可离散判定、标注设计适用时使用，不能成为所有 Human Benchmark 的统一硬指标。

返工完成后，由另一 Agent 独立复核；Issue #1 通过后关闭。

---

# 14. 两个本地 Agent 的固定分工

为了避免两个 Agent 同时改同一批文件造成冲突，从现在开始采用 Builder / Reviewer 双角色。

## Agent A｜Builder / Integrator

职责：

- 读取 Issue；
- 做系统内部核对；
- 必要时研究外部证据；
- 修改 canonical 文件；
- 维护 Rule / Toolkit / Evidence / Decision 的一致性；
- 提交小而清晰的 commit；
- 写阶段报告。

原则：

**一轮只解决一个明确问题，不自行扩大范围。**

## Agent B｜Independent Reviewer / Research Auditor（新 Codex）

职责：

- 在 Agent A 动手前，可针对高风险问题独立取证；
- Agent A 提交后独立审查证据、推理、字段和现场可执行性；
- 主动找反例与过度泛化；
- 对 Evidence Grade / Knowledge Status 有否决权；
- 优先用 Issue 评论或 Audit Note 给返工意见；
- 非必要不直接重写 Agent A 同一批 canonical 文件。

Reviewer 的目标不是找文字错误，而是问：

> **如果一个陌生 FDE 明天按这份东西执行，会不会被误导？**

## 分歧机制

两个 Agent 对重要规则意见不一致时：

1. 各自给出证据；
2. 标明 FACT / INFERENCE / DESIGN DECISION；
3. 如果证据不足，降级为 HYPOTHESIS / Open Question；
4. 不为“统一意见”强行达成结论；
5. 只有涉及公司战略选择、不可逆变更或用户偏好时才提交用户裁决。

不要把用户变成日常仲裁者。

---

# 15. GitHub 协作协议

GitHub 是两个 Agent 的唯一协作总线。

每次启动：

1. `git pull` / 同步 main；
2. 读 `00_Master_Index/LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md`；
3. 读 `00_Master_Index/AGENT_COORDINATION.md`；
4. 检查 open Issues；
5. 读当前 Issue 最新评论；
6. 再决定行动。

不要依赖聊天历史作为 canonical 状态。

## 写入原则

- 同一时间只有 Builder 修改同一组 canonical 文件；
- Reviewer 尽量用 Issue / Audit Note；
- commit 必须说明“为什么改、改了什么”；
- 不用 `final_v3_new_new` 式命名；
- 稳定 ID 不变；
- 结构变化先 Change Proposal。

---

# 16. Batch 2 之后的推荐顺序

Batch 2 通过以后，不要立刻继续造工具。

### 下一步 A｜Delivery Chain 重检（G-05）

把：

- 现有手册 8 章；
- 0-9 十阶段假设；
- L0-L5；
- 官网五阶段；
- Gate；

映射到一张表。

目标不是统一名字，而是确认：

- 每一阶段什么时候进入；
- 入口证据是什么；
- 必做动作；
- 输出 Artifact；
- Exit / Hold；
- 谁负责。

重点检查 Baseline、Human Benchmark、Work Trace、客户采用/ROI 在链路中的真实位置。

### 下一步 B｜Operating Model 决策

在 Palantir / 瓴羊 / OpenAI / Tomoro 跨组织证据基础上，对：

- Echo-like；
- Delta-like；
- Core；
- Client Coach；
- 一人多角色；
- 外包风险；

形成通元问科自己的设计决定。

不能直接复制 Palantir 部门名。

### 下一步 C｜Eval + Controlled Deployment

建立：

Golden Set → Eval → Shadow → Assisted → Guarded → Full / Autonomous → Rollback / Bad Case Review。

瓴羊 E248 中 MVP / AB Test / 灰度上岗可以作为中国样本，但需要与其他一手方法交叉验证。

### 下一步 D｜Commercial Engine

研究：

- Deployment Leverage；
- Unit Economics；
- Value Unit vs Pricing；
- Land & Expand / Value Depth；
- 什么时候低价试点有意义，什么时候只是低质量咨询；
- 如何避免人头增长驱动收入增长。

### 下一步 E｜Edge→Core

必须回答：

- 什么前线能力应该上浮 Core；
- 什么只留客户层；
- 如何判断重复模式；
- 如何防止客户定制污染核心产品；
- 上浮提交物是什么；
- 谁审；
- 如何验证泛化后真的让下一次部署变轻。

---

# 17. 真实项目是试验场，不是宣传素材

优先用已有项目验证 FDE OS：

- 供应链研究知识库 PoC；
- 供应链结算异常协同；
- 网络货运支付前智能审核；
- 其他仓库 / 本地已有项目材料。

严格区分：

- 已发生；
- 已测试；
- 讨论过；
- 计划做；
- 未取得材料。

纸面 dry run 可以验证“工具是否告诉我们下一步缺什么”，不能验证“工具已现场有效”。

真正 Field-tested 至少需要陌生执行者或真实现场执行证据。

---

# 18. 每轮三轮验证

任何可能改变 Rule、阶段、组织模型、商业模型的重要动作：

## 第一轮｜系统内部

已有 OS 怎么说？是什么状态？有没有 Decision / Evidence / Gap？

## 第二轮｜外部证据

优先 Primary / First-hand；寻找反例；不要单组织泛化。

## 第三轮｜对抗审查

至少问：

- 是否把公司事实写成行业规律？
- 是否把喜欢的框架写成事实？
- 是否把设计决定写成 FACT？
- 是否存在更小改动？
- 是否真的让现场执行更清楚？
- 是否破坏旧 ID / 链接 / 历史？

低风险格式、错字、链接修复不必机械走完整三轮。

---

# 19. 用户阶段报告格式

用户不看 Agent 之间的日常对话。

只在一个批次真正结束时给用户报告，控制在短篇幅：

### 本轮结论
通过 / 部分通过 / 返工。

### 实际完成
最多 3-5 条。

### 关键判断变化
哪些假设被证实、降级或仍 Unknown。

### 尚未解决
只列真正阻塞下一步的事项。

### 下一动作
说明现在轮到哪个 Agent、做什么。

不要向用户输出几十条过程日志。

---

# 20. 红线

禁止：

- Palantir 崇拜式照搬；
- 把咨询顾问 / 外包工程师简单重命名 Echo / Delta；
- Agent for everything；
- Demo = proof；
- PoC = production；
- 客户赞美 = result；
- 单点案例 = baseline；
- 顶尖员工 = 自动 Ground Truth；
- Work Trace = SOP 抄写；
- 行为轨迹 = 所有人类动作都应该自动化；
- “卖结果” = 必须 outcome pricing；
- 合同金额增长 = FDE 成功；
- 人数增长驱动收入增长 = 产品杠杆；
- Secondary podcast = Primary fact；
- 为了完整而大规模重构；
- 为了看起来严谨而无限增加治理文件。

---

# 21. 两个 Agent 接管后的第一组动作

## Agent A / Builder

立即：

1. 同步 main；
2. 读取 Issue #1；
3. 读取 `RN-20260817-004-chatgpt-batch2-audit.md`；
4. 仅修改 TOOL-004 / 005 / 006、必要 Evidence / RN / Master Index；
5. 完成 P0 / P1 最小返工；
6. commit；
7. 在 Issue #1 提交短报告。

## Agent B / Reviewer

不要等待用户。

立即：

1. 同步 main；
2. 独立阅读三个 Toolkit 与 Audit Note；
3. 核对 OpenAI / METR / Anthropic / Microsoft primary anchors；
4. 等 Builder commit 后检查 patch；
5. 重点审：Human Benchmark vs Golden Set 是否真分开、硬规则是否降级、Work Trace 是否能还原状态变化；
6. 给出 PASS / REQUEST CHANGES；
7. 通过后关闭 Issue #1，并建立下一批 Issue（Delivery Chain 重检），不要让用户传话。

---

# 22. 最终目标提醒

不要试图证明“通元问科已经拥有成熟 FDE 方法论”。

FDE OS 的价值恰恰在于：

> **已知的写清楚，设计的标出来，不知道的明确保留；在不知道时，系统能告诉团队下一步应该拿什么证据。**

成熟度最终由真实部署证明，而不是由文档数量证明。

本文件自 2026-08-17 起作为两个本地 Agent 的项目级交接入口。后续如果本文件与更晚的正式 Decision / Issue 冲突，以更晚的仓库记录为准，并保留冲突历史。
