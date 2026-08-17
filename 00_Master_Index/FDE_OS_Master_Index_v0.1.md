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
| DOC-003 | Deployment Leverage | 假设：FDE 与咨询的核心差异是部署杠杆（同类新项目现场人力递减）；首个单组织实证已取得（Palantir 毛利 80% vs 埃森哲 32%；新客户约 1 年毛利转正、现场团队缩小） | Researching | HYPOTHESIS（行业级）/ Palantir 事实（L2） | EV-PAL-002/003；G-06 剩余跨组织验证 | Low-Medium |
| DOC-004 | Value Depth | 假设：Trust→Access→Mission Criticality→Value Depth 是合同深化的真实结构；Land and Expand 是事实但「越签越贵」不是定义 | Researching | HYPOTHESIS | 待 G-07 | Low |
| DOC-005 | 复杂度阶梯 | 默认从单次辅助起步，七级递升，每级升档需上级运行证据 | Designed | DESIGN DECISION（采信 L1 实践） | EV-ANT-001 | High |
| DOC-006 | 卖结果≠outcome pricing | Value Unit 与 Pricing Mechanism 分离；禁止从「不卖人天」推出「必须结果付费」 | Researching | HYPOTHESIS | 待 G-08 | Medium |
| DOC-007 | Edge→Core 学习循环 | 假设：前线碎石路应被修成 Core 高速公路；机制在 Palantir 已充分实证（L1 官方回流流程 + L2 泛化分工与 Ontology），通元问科适用性待验 | Researching | Palantir 事实（L1+L2）/ HYPOTHESIS（通元问科适用） | EV-PAL-001/002/003 | Medium |
| DOC-008 | 概念隔离 | 「Field Driven Engineering（湖南样本）」≠ 本系统 FDE | Designed | DESIGN DECISION | DEC-2026-004 | High |

## 02 Operating Model

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| ORG-001 | 业务问题负责人（原 Echo-like 条目） | 候选设计：问题定义/**组织共定**核心指标与基线口径（建议方，正式业务事实确认仍归客户业务负责人）/客户关系/业务结果归口/放行建议方；进入退出量化条件未知 | Designed（候选，未现场验证） | DESIGN DECISION；依据=**外部参照（业务侧角色 2/4 组织明确分轨：Palantir、瓴羊；OpenAI 双称谓分工未知）**+内部三层分离 | EV-PAL-003（Echo 口述）；EV-LY-001 BA；组织模型 v0.1.1 角色 A | Medium-Low |
| ORG-002 | 技术交付负责人（原 Delta-like 条目） | 候选设计：系统转化/数据连接/评测/受控部署/生产接入/上浮提交发起方；进入退出量化条件未知 | Designed（候选，未现场验证） | DESIGN DECISION；依据=最强交集（驻场工程 4/4）+ 手册第 4-6 章 | EV-PAL-001/003；EV-OAI-002/003；EV-LY-001；组织模型 v0.1.1 角色 B | Medium-High |
| ORG-003 | 公共能力维护方（Core） | 候选设计：资产索引维护+上浮评审合并权；**最小接口**=提交（技术交付负责人）→评审（维护方+原项目技术交付负责人）→批准/拒绝（维护方单方，理由登记）；泛化阈值/防污染判据未知（G-09 不因本批关闭，完整机制未设计） | Designed（候选，仅最小接口） | DESIGN DECISION；依据=回流机制交集（3/4，形态各异） | EV-PAL-001/002（L1+L2）；EV-OAI-003（build-prove-generalize）；EV-LY-001④（4+X）；组织模型 v0.1.1 角色 C | Medium |
| ORG-004 | 客户业务教练（原 Client Coach 条目） | 候选设计：客户内部遴选（业务负责人提名）；**参与**黄金集判定/仲裁/调教，提供业务意见与停止信号；**正式验收权归属不在本批推出**；合同机制仅定参与义务+意见路径+停止信号三项，价格法律留商业批次 | Designed（候选，未现场验证） | DESIGN DECISION；**外部参照（1/4 组织明确机制：瓴羊）+内部雏形（协会年轻骨干）——非跨组织共同事实** | EV-LY-001⑤；EV-TY-009；组织模型 v0.1.1 角色 D | Medium-Low |
| ORG-005 | 一人多角色边界 | 候选（定性条件版）：A/B 可兼任当且仅当串行阶段+建议与批准分离+不同时为被验收方与验收方；分设信号（**登记为待验证设计假设**）=进入生产运营期/**多项目并行且至少一个进入生产期**/客户要求独立复核；量化门槛未知 | Designed（候选，仅定性条件） | DESIGN DECISION（三层分离制度的直接推论） | 三层分离（回放修订 4）；组织模型 v0.1.1 §4 | Medium |
| ORG-006 | 技术交付外包边界 | 候选（防线清单版）：外包可行性本体未知；若发生，信用归因权五位置不可外包（问题定义者/指标共定者/评审主持者/复盘作者/高层关系），违反任一项触发变更提案（Change Proposal）重审 | Designed（候选，仅防线） | DESIGN DECISION | EV-TY-008（L4 内部研究）；组织模型 v0.1.1 §5 | Medium-Low |
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
| DEL-008 | Baseline 阶段方法 | 方法草案已建（TOOL-004 v0.2）：先定**核心业务指标**（公式+统计单元），成本/时长/质量/量为**默认检查框架**按需取舍，先定口径后填数，单次记录不构成基线；服务 GATE-2 与 R-C04 | Designed（草案，未现场验证） | DESIGN DECISION（方法采信） | EV-EXT-004 + EV-EXT-007（L1 锚点）；内部反例=结算协同单样本 | Medium |
| DEL-009 | Work Trace 方法 | 方法草案已建（TOOL-006 v0.2.1）：真实人员处理真实 Case 的行为序列采集（八要素含耗时与动作结果/状态变化）；行为与事后自述分列；动作三分类（业务规则候选/系统摩擦/混合待核）；样本以**轨迹饱和+关键异常覆盖**为准（3-5 笔仅为初始 discovery 最低样本）；方案设计链路≠行为轨迹 | Designed（草案，未现场验证） | DESIGN DECISION（方法采信）；瓴羊投手案例佐证「优秀员工真实行为=训练对象」（EV-LY-001③，H-7 的组织级事实） | EV-EXT-006 + EV-EXT-007 + EV-EXT-001 + EV-LY-001 [13:24-15:40] | Medium-High |
| DEL-012 | 评测方法（G-12） | 设计决定（候选）：评测四对象分立（人工参照系/黄金集=输入，能力评测集/回归集=本规则产出，含毕业机制）；评分器三型选型与人工校准；多次试验；错误分类接反馈路由；生产案例四步防污染+归属三选一；项目阈值须批准记录（无通用样本量/通过线；Anthropic 20-50=早期实践参照）｜服务 GATE-5，只判达标不判生产风险 | Designed（候选，未现场验证） | DESIGN DECISION（方法锚点=EV-ANT-003 L1） | EV-ANT-003；EV-EXT-007；TOOL-008 | Medium-High |
| DEL-013 | 受控部署与回滚（G-11） | 设计决定（候选）：四种运行方式=**可选控制模式非升级阶梯**（影子/辅助/守卫/全自动；每模式四要素：权限边界/批准与暂停停止/进入证据与监测/退出降级触发；高风险放行权不因模式转移）；回滚十要素（触发/范围/停止授权/降级/接管/结果隔离/数据保全/通知/恢复验证/重新上线）｜服务 GATE-6，只判风险不构成部署认证，≠U4/U5 | Designed（候选，未现场验证） | DESIGN DECISION（控制类别锚点=NIST AI RMF Manage 4.1-4.3 L1；瓴羊灰度=单组织参照） | EV-NIST-002；EV-LY-001⑦；EV-EXT-008；TOOL-009 | Medium |
| DEL-011 | 使用轨迹与反馈路由 | 设计决定（候选）：五级使用状态 U1-U5（一次轨迹≠使用率、一次使用≠现场验证、GATE-6≠部署认证）；真实交付入口统一定义（不限 URL）；条件式反馈路由（使用证据四步入评测集、评测失败按根因分流、重复模式仅触发上浮候选评审、使用证据进六态产品决定）；观测物=TOOL-007 | Designed（候选，未现场验证） | DESIGN DECISION（GOV.UK beta/live 与 NIST AI 800-4 支撑总体模式，EV-EXT-008） | EV-EXT-008；EV-LY-001③；EV-PAL-002；TOOL-007 | Medium |
| DEL-010 | 客户采用/ROI 阶段 | 已裁决（2026-08-18，DEC-2026-013/R-3，候选落位）：并入阶段 08 的 Exit 必查维度（实际使用率/业务结果对照基线/ROI 口径）+ GATE-7 证据输入；不设独立阶段；C 类备选（07a 采用确认）触发条件已登记 | Designed（候选落位，未现场验证） | DESIGN DECISION | 官网5；EV-LY-001 [18:11]；手册第 7 章 | Medium |

## 04 Commercial Engine

| Rule | 主题 | 当前规则 | 状态 | 知识状态 | 证据 | 置信 |
|---|---|---|---|---|---|---|
| COM-001 | 信用阶梯 | 陌生→入口→关系→判断→交易→交付→Reference→机构（八级）；用可逆承诺改造一次性信任 | Researching | INFERENCE | EV-TY-008 | Medium-High |
| COM-002 | 首单机制 | 低风险≠免费、付费≠commitment；真正变量是客户承诺向量（预算/sponsor/负责人/数据/用户/节奏/上线资源） | Researching | INFERENCE | EV-EXT-002 | Medium |
| COM-003 | Value Unit / Pricing | 瓴羊实证已取得：两类——按坐席收费（成本替代 8-9 折同效果）+按效果分成（超出人工基线的增长部分分成，MVP+AB test 结算，连续续费客户真实存在）；与「不卖人天」原则的关系：瓴羊明确拒绝千人天采购（EV-LY-001⑧/嘉宾 [26:40-27:39]） | Researching | 瓴羊事实（L3）；行业级仍 INFERENCE | EV-LY-001；Palantir 定价证据待 G-08 | Medium |
| COM-004 | 四健康指标 | 假设：客户结果↑/ACV↑/单位人力↓/复用比例↑ 可作 FDE 健康度核心指标；Palantir 版两大内部指标（结果价值/合同规模 + 产品杠杆）与之高度吻合（单组织） | Researching | HYPOTHESIS | EV-PAL-003（McGrew 两指标）；EV-PAL-002（毛利对比） | Low-Medium |
| COM-005 | 不卖 ROI 保证 | 过程/里程碑保证（gate 未过则停），不承担不可控结果风险 | Designed | DESIGN DECISION | EV-TY-008 L120 | Medium-High |
| COM-006 | 信用归因权 | 五个必须占住的可见位置（问题定义/指标共定/评审主持/复盘作者/高层关系） | Designed | DESIGN DECISION | EV-TY-008 | Medium |
| COM-007 | 输出层信用纪律 | 官网三层信用划分；未证实宣称一律下线 | Designed | DESIGN DECISION | EV-TY-007 | High |

## 05 Field Toolkit

| Rule/Tool | 名称 | 状态 | 位置 |
|---|---|---|---|
| TOOL-001 =〔作业-准入-01〕 | 客户初步调查表（9+14+12+8+12+字段组，五选一结论） | Draft V0.1（含完整示例） | ForFlow 作业包 |
| TOOL-002 =〔作业-场景-01〕 | 候选场景比较与直接否决表（两关+场景卡+12 维比较+AI 必要性检查） | Draft V0.1（含示例） | ForFlow 作业包 |
| TOOL-003 =〔作业-准入-02〕 | 项目准入审查表（L0-L5 逐级审查+三层记录） | Draft V0.1（含示例） | ForFlow 作业包 |
| TOOL-004 | 基线记录表（Baseline Sheet） | Draft V0.2（2026-08-17 返工后：核心业务指标优先、四维为默认框架；dry run=网络货运纸面推演通过） | `05_Field_Toolkit/TOOL-004_基线记录表_草案.md` |
| TOOL-005 | 人工参照系与黄金集记录表（Human Benchmark & Golden Set Sheet） | Draft V0.2（2026-08-17 返工后：A 人工参照系/B 黄金集两节拆分） | `05_Field_Toolkit/TOOL-005_人工参照系记录表_草案.md` |
| TOOL-006 | 工作行为轨迹表（Work Trace Sheet） | Draft V0.2.1（2026-08-17 返工后：八要素+饱和判据；Anthropic 引用归属已按原文收敛） | `05_Field_Toolkit/TOOL-006_工作行为轨迹表_草案.md` |
| TOOL-007 | 使用轨迹表（Usage Trace Sheet） | Draft V0.1（2026-08-18，Issue #4 获批设计；与 TOOL-006 语义独立；含数据边界与三铁律） | `05_Field_Toolkit/TOOL-007_使用轨迹表_草案.md` |
| TOOL-008 | 评测集构建与回归表（Eval Suite Sheet） | Draft V0.1（2026-08-18；四对象分立+防污染+阈值批准制） | `05_Field_Toolkit/TOOL-008_评测集构建与回归表_草案.md` |
| TOOL-009 | 受控部署记录表（Controlled Deployment Sheet） | Draft V0.1（2026-08-18；四模式四要素+回滚十要素） | `05_Field_Toolkit/TOOL-009_受控部署记录表_草案.md` |
| TOOL-010~020 | 其余待建项（Stakeholder Map、Shadow Run、Go/Hold/No-Go、Bad Case Review、Edge→Core Submission 等） | 未建 | — |

## 附：编号映射表（手册体系 ↔ OS 体系）

| 手册编号 | OS 编号 | 备注 |
|---|---|---|
| 〔作业-准入-01〕 | TOOL-001 | 原编号继续使用 |
| 〔作业-场景-01〕 | TOOL-002 | 同上 |
| 〔作业-准入-02〕 | TOOL-003 | 同上 |
| 手册规范 §5.2 成熟七态 | IA §4.3 | 直接继承 |
| 手册规范 §8.10 放行六态 | GATE 放行结果 | 直接继承 |
| L0-L5 准入层级 | GATE-0 区间实现件 | 层级≠Gate：正交多对多**候选映射**（DEC-2026-013，待真实 Gate 运行验证；见 `03_Delivery_Playbook/链路对齐总表_v0.1.md` §4 R-4） |

## 阅读与维护

- 本表每次规则增改必须同步：模块文件、Evidence Library 对应条目、（涉及时）Decision Log。
- Owner 列暂空——待用户指派后回填（首任默认为主 Agent 建设期代管）。
