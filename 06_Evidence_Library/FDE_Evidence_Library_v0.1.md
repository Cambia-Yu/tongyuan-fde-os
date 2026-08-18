---
id: EV-LIB
type: evidence-library
version: 0.1
updated: 2026-08-16
rule: 每条证据必须说明「它证明了什么」；来源缺失的条目不得支撑任何 FACT
---

# FDE Evidence Library v0.1

字段：编号｜组织｜主题｜主张 Claim｜类型｜等级 L1-L5｜来源｜日期｜摘录/事实｜我们的解读｜支撑规则｜反例｜置信｜最近核验。

状态图例：✅ 已核验（本地实物或官方原文在手）｜🟡 转引待核（二手材料转引，原源未取得）｜🔴 来源缺失（仅有任务书/内部转述）。

---

## A 组｜公开实践锚点（多数已在闭环一台账登记为 PUB-01~04）

**EV-OAI-001** ✅｜OpenAI｜FDE 定义｜FDE 岗位连续承担发现、技术范围、系统设计、建设和生产发布，以生产采用与评测反馈衡量成功｜官方岗位说明｜L1｜ForFlow 台账 PUB-01（原文 URL 待补档）｜—｜「FDE 不是驻场程序员/售前/PM」的官方对照｜DOC-001｜未见｜High｜2026-07-23（台账登记日）

**EV-OAI-002** ✅（2026-08-18 核验；日期按复核方对当前页面的核正，**2026-05-11**——本方首抓时误读页面元数据为 2026-08-06，已更正）｜OpenAI｜部署公司官方发布｜① 部署公司成立，OpenAI 多数持股/控制；② **伙伴关系由 TPG 领衔；公司启动时有逾 40 亿美元初始投资**（原文 more than $4B initial investment，不压缩为「领投 N 家投资 X 亿」）；③ **已同意收购 Tomoro，受惯常交割条件与监管批准约束，预计未来数月完成——收购未交割**；④ Tomoro 约 150 名 FDE/部署专家**计划在交割/公司启动时带入**（未交割不写作已加入）；⑤ 角色列名=FDE+Deployment Specialist（**两者分工边界官方未披露，未知**）；⑥ 参与模式=聚焦诊断→少数优先工作流→FDE 进场设计-建设-测试-部署；⑦ Tomoro 此前工作=Tesco/Virgin Atlantic/Supercell（收购方转述）｜官方发布｜L1｜《OpenAI launches the OpenAI Deployment Company…》2026-05-11，openai.com/index/openai-launches-the-deployment-company/｜抓取 2026-08-18｜ORG/DOC 设计依据｜—｜High（原文在手）｜2026-08-18 更正登记

**EV-OAI-003** ✅（2026-08-18 本地核验）｜OpenAI 部署公司官网 deploy.co｜① 「Instead of starting with a general product, FDE teams work directly with customers to solve a specific problem」；② **「This cycle—build, prove, generalize—connects deployment to product development」（建设-证明-泛化周期，任务书 §12 三段表述的官方出处）**，连接 Agent SDK/AI 辅助创作/模型基准工具；③ 案例（官方自述，无第三方核验）：BBVA 12 万员工/25 国；John Deere 减药 70%、客户互动 6 倍、自建评测系统测准确率；④ 页面无日期（仅 ©2026）｜官方官网｜L1（事实）/自述案例=L2 营销自述｜deploy.co，抓取 2026-08-18｜**tomoro.ai 首页 301 重定向至 deploy.co**（交割进程迹象，非完成证据；部分旧文章经 deploy.co/news 保留原日期正文，见 EV-TOM-001）；「12 周生产」主张无页面可核、未采信｜ORG-003 接口参照；DOC/COM｜—｜High（原文在手）/Medium（案例）｜2026-08-18

**EV-ANT-001** ✅｜Anthropic｜工作流 vs Agent｜预先定义路径的工作流与模型动态决策的 Agent 应区分，按需逐步升复杂度｜官方工程博客｜L1｜台账 PUB-04｜—｜—｜DOC-007/DEL 复杂度阶梯｜—｜High｜2026-07-23

**EV-ANT-002** 🟡｜Anthropic｜工具工程｜用真实任务与真实数据来源评测工具、记录调用路径以发现流程与工具边界｜官方实践（规范 §9.4 转引）｜L1（待定位原文）｜手册规范 V0.2 §9.4｜—｜—｜DEL-工具评测｜—｜Medium｜未核验

**EV-NIST-001** ✅｜NIST｜AI 风险治理｜先建立情境（用途/价值/任务/范围/风险容忍/人类监督/数据代表性）再作初始决定；记录放行或停止决定｜官方框架｜L1｜台账 PUB-03｜—｜支撑准入证据包与放行记录制度｜DEL-002/D-5｜—｜High｜2026-07-23

**EV-GART-001** ✅（2026-08-18 升级：页面级一手核验，Batch 8 红队）｜Gartner｜原型存活率｜① 官方文档页《Proportion of AI and GenAI Prototypes Making It Into Production》（gartner.com/en/documents/6587902）：**平均仅 41% 生成式 AI 原型、42% 非生成式 AI 原型进入生产**（研究正文需订阅，页面摘要含确切数字）；② 官方新闻稿 2024-07-29（gartner.com/newsroom/press-releases/2024-07-29-…）：**预测 30% 生成式 AI 项目将于 2025 底前在 PoC 后放弃**，原因=数据质量差/风险控制不足/业务价值不清（完整 L1）｜官方｜L1（页面级）｜核验 2026-08-18｜支撑 DEL-005 指标纪律（异常1 拦截）；红队攻击背景｜不回答通元客户的具体组织机制（边界保留）｜High（①）/High（②）｜2026-08-18 升级

## B 组｜通元问科项目证据（EV-TY）

**EV-TY-001** ✅｜协会知识库 PoC（客户名内部掌握）｜范围收缩/合同结构｜① 客户初始诉求含内部研究/政策核验/报告生成/会员服务；② 首期收缩为代表性场景 PoC；③ 合同明确「初稿不构成正式报告，交付前需人工审核」；④ 签约前测算（50 份资料/5 万字）自我标注「不构成验收标准」｜项目材料｜L2（公司一手）｜LOC-A01 会议转录(5-26)、A02 启动草案(5-27)、A03 测算报告、合同 .doc(6-11)、官网案例页｜2026-05~06｜「三分类事项法」（可直接明确/需客户确认/必须测试后定）与「五级敏感口径」出自 5-27 草案｜O-1/O-2；R-C02｜验收结果未披露｜High（材料在）｜2026-08-16
→ 待办：解析合同 .doc 提取条款结构；确认 PoC 三条「能否」式验收的执行结果。

**EV-TY-002** ✅｜网络货运支付前智能审核（白银集团相关）｜准入回放｜① 需求两方向→首期收缩为支付前预审；② 15 条审核规则、200-500 笔样本均**建议值未取得**；③ 2026-07-23 历史回放结论 L1（送审方案的 L2 建议因证据不足被降级）｜项目材料+回放记录｜L2｜LOC-N01 总体方案(7-13)、N02 摸排清单、N03 送审方案(7-19)、02-历史回放(7-23)｜2026-07｜回放证明「按证据定层级」可执行，且暴露 6 个手册缺口（真实事项最低定义、负责人具名规则等）｜D-1；H-3 部分｜—｜High｜2026-08-16
→ 待办：P0 材料清单 8 项（台账 L199-206）全部未取得。

**EV-TY-003** ✅｜白银集团智能仓储｜范围收缩｜「智能仓储」收缩为库存/价值/库龄/库容/作业/运输风险监测；不替换原系统、不做硬件改造；建议历史事件验证先行｜项目材料｜L2｜LOC-W01 建设方案(7-19)｜2026-07｜O-1/O-3 第 3 例｜R-C06｜客户原始需求未取得｜Medium-High｜2026-08-16

**EV-TY-004** ✅（材料=官网+工程）｜供应链结算异常协同｜架构/职责边界｜① 三层架构（原系统不动+异常协同层+工作界面）；② 模型负责解释、规则/SQL 负责计算、放行留人——「算错了会直接改变业务金额的任务不允许模型自由推导」；③ 一次税率精度测试模型出现数千元级偏差，推翻了初期设计；④ 官网信用清单判定其为「唯一可追溯的真实项目材料」但量化结果仍需客户确认｜项目材料+官网审计｜L2｜settlement-coordination.md、docs/02 L7-10、notes/contract-doc-engine（后端工程实物）｜2026-05~08｜台账判定「材料缺失」（LOC-S01/S02 为购产运销协同方案，不得替代）；**项目实际运行状态未知**｜O-2/O-3/I-2｜X-2 口径张力｜High（架构）/Low（成效）｜2026-08-16
→ 待办：确认与「购产运销协同试点」是否同一项目（台账 P0 第 6 项）；取得异常事项样本与运行记录。

**EV-TY-005** ✅（占位）｜中物联采嫁销｜数据处理管线｜仅一行八步管线（文件→类型判断→结构化解析→业务分块→字段抽取→标准化→候选匹配→链路确认）+四个待答问题+一个空文件｜占位笔记｜L2（但内容极薄）｜vault 工作/中物联/采嫁销/ 三文件（293 字节）｜2026-05-31｜不得作为设计文档引用（X-6）｜无｜—｜Low｜2026-08-16

**EV-TY-006** ✅｜通元问科｜制度资产｜手册规范 V0.2：证据四级依据+成熟七态+验证四层+四张控制台账+四闭环+资产六类（失败模式独立）+放行六态｜内部规范｜L4（设计文件）｜`Downloads/FDE手册编写与现场验证规范_V0.2.md`｜2026-07-24｜FDE OS 03/05 模块的宪法（DEC-2026-003）｜全部 DEL/TOOL 规则｜—｜High｜2026-08-16

**EV-TY-007** ✅｜通元问科｜输出层纪律｜官网信用证据清单 13 条分级 + 三层划分 + 未证实宣称下线决定；内部审计自判「声称的能力大于可追溯证据」｜内部审计｜L4｜docs/01（8-12）、docs/02、docs/03、audit/product-design（8-16）｜2026-08｜08_Outputs 的合规范本；对标 Palantir AIP Bootcamp「5 天三个结果」的表达结构（该对标本身未经 Palantir 原文核验）｜D-6｜—｜High｜2026-08-16

**EV-TY-008** ✅｜通元问科｜商业机制研究｜信用阶梯（八级：陌生→入口→关系→判断→交易→交付→Reference→机构）；first offer 七分类；不卖 ROI 保证卖里程碑；信用归因权五位置；90 天验证计划与证伪规则｜内部深度研究｜L4（研究综合，内含 A/B/C 分级外部案例）｜`Downloads/deep-research-report.md`（622 行）｜2026-08-12｜自声明局限：首单定价无结论、幸存者偏差、四类待取证证据｜COM-001~005｜X-3 粒度不一致｜Medium-High｜2026-08-16

**EV-TY-009** ✅｜通元问科｜客户关系实践｜5-26 两场协会会议：① 主动否定「向会员开放报告生成」（保协会利润池）；② 知识库=关系图而非文件夹（每条资料七元组：来源/时间/权限/适用场景/核心判断/核验状态/关联对象）；③ 「AI 入库、人来核验」；④ 客户提出互用身份/工信部背书/长期利益共享；⑤ 本地部署+资料不拷走作为安全牌｜会议笔记｜L2（一手）｜vault 商业判断/产品与交付 5-26 两篇 + 5-27 草案｜2026-05｜I-4 协会双刃剑的一手印证；H-2 Client Coach 的本土雏形（「年轻骨干」机制）｜ORG-004；COM 协会路径｜—｜High｜2026-08-16

## C 组｜外部样本（已核或半核）

**EV-EXT-001** ✅（笔记一手）｜网易智企｜组织 AI 落地方法｜① 全员两周产出 240+ skill 后发现「skill 堆积不等于能工作」，转向岗位工作流梳理；② 按时间占比找高频重复低价值任务，「员工的想象力不可靠，工作流才可靠」；③ AI 消化低价值工作后员工更忙（岗位价值须重设）；④ 杀手场景=跨系统上下文聚合；⑤ 企业级治理平台「帝王蟹」｜从业者分享（会议笔记）｜L2｜vault 2026-04-23 养虾笔记｜2026-04｜O-4 跨组织印证；H-7 Work Trace 的方法侧证（按岗位还原工作而非问需求）｜DEL-003 现场调查方法｜—｜Medium-High｜2026-08-16

**EV-EXT-002** 🟡｜（deep-research 转引案例群）｜冷启动机制｜Sierra 6 家付费 design partners / Gong 12 家免费中 11 家转付费 / Retool 150 万美元 pilot+响应密度 / OpenAI×Morgan Stanley 先建 eval 后扩展（采用率 98%）/ IBM Garage 三天 workshop / Thoughtworks Discovery vs Inception 分型 / 华为 115 个样板点=reference 工业化 / 北京揭榜 12 场景 1.1 亿元｜研究转引｜L2-L3（各案例等级见报告自评 A/B/C）｜deep-research L42-71｜2025-2026｜「低风险≠免费；付费≠commitment，真正变量是客户 commitment」｜COM-001/002｜华为案例反证「联合创新是信用结果而非原因」｜Medium（未回一手）｜2026-08-16
→ 待办：对进入 COM 模块的 3-4 个关键案例回溯一手来源。

**EV-EXT-003** ✅（隔离）｜湖南「智赋万企」报告｜同名异义样本｜Field Driven Engineering（共享驻场）≠ Forward Deployed Engineer；含 O-FDE 组织适配模型与 S.T.E.P. 四阶段｜第三方报告｜L3｜`ZCodeProject/FDE模式AI转型可行性分析.md`（Scribd 来源）｜2026-07-22｜仅作中国腰部企业落地约束的外部视角；DEC-2026-004 隔离｜无｜—｜Low-Medium｜2026-08-16

**EV-EXT-004** 🟡（2026-08-17 返工降措辞：四维为常见候选框架而非普遍规则）｜跨组织（企业 AI 实践）｜基线方法｜基线必须先于项目设立，「上线后发明指标」是常见失败模式；启动前指定具名业务指标、预设成功窗口；**成本/时长/质量/量是多源常见的候选维度框架，不是必测清单**（OpenAI 官方方法主张从业务目的与最重要 outcome 出发——见 EV-EXT-007）｜从业者方法文章（多源一致）+ 学术侧证 + L1 锚点｜L2/L3 + L1（EV-EXT-007）｜agility-at-scale.com、classicinformatics、arXiv 2512.04123；一手锚点见 EV-EXT-007｜抓取 2026-08-17｜支撑 TOOL-004 v0.2 与 DEL-008｜—｜Medium｜2026-08-17

**EV-EXT-005** 🟡（2026-08-17 返工降措辞）｜跨组织（LLM 评测实践）｜人工参照系/黄金集方法｜试标注轮校准；机会校正指标（κ 类）**仅在输出可离散判定、样本与标注设计适用时使用**；IAA≥0.8 为部分来源的行业参考值，**非本 OS 硬规则**；分歧=判据含糊的诊断信号；第三人仲裁；数据集小而多样｜评测工程文章（多源一致）+ 学术 + L1 锚点（OpenAI golden set 定义 / METR human baseline，见 EV-EXT-007）｜L2/L3 + L1｜booking.ai、getmaxim.ai、arize.com、galtea.ai、arXiv 2506.13023｜抓取 2026-08-17｜支撑 TOOL-005 v0.2（A/B 两节）；「最厉害员工≠Ground Truth」的方法学支撑｜—｜Medium｜2026-08-17

**EV-EXT-006** 🟡｜跨组织（流程/任务挖掘）｜Work Trace 方法侧证｜流程挖掘=系统事件日志（端到端）；任务挖掘=用户级交互数据，暴露系统事件**之间**的变通动作/手工返工/影子表格——观察数据须区分业务规则与系统摩擦｜厂商方法文档（多源）+ **官方锚点：Microsoft Power Automate Process Advisor（Task Mining 目标=理解员工实际桌面操作、识别常见交互、错误与不必要动作；已由复核方独立核验）+ Anthropic《Demystifying evals for AI agents》（已由复核方按原文核验：transcript/trace/trajectory = trial 的**完整记录**，含 outputs、tool calls、reasoning、intermediate results 与 interactions；**outcome** = trial 结束时**环境的最终状态**——Anthropic 区分「轨迹记录」与「环境结果/最终状态」两类对象）**｜L2/L3 + L1（官方页，复核方核验）｜signavio.com、appian.com、uipath forum、paxray.com、abbyy.com；learn.microsoft.com/en-us/power-automate/process-advisor-overview；anthropic.com/engineering/demystifying-evals-for-ai-agents｜抓取 2026-08-17｜支撑 TOOL-006 与 DEL-009；**归属边界**：把「同时记录动作轨迹与动作后状态」迁移到人类 Work Trace，是本 OS 的 DESIGN INFERENCE（方法类比，受 Anthropic 轨迹/结果区分启发），**不是** Anthropic 给出的人类行为记录方法；反向发现：影子表格可能承载未成文业务规则｜—｜Medium｜2026-08-17 更新

**EV-EXT-007** ✅（2026-08-17 本地 Agent 亲自核验，RN-20260817-004 P1 指定的一手锚点包）｜OpenAI + METR｜评测方法 L1 锚点｜
① **OpenAI《How evals drive the next chapter in AI for businesses》2025-11-19**（openai.com/index/evals-drive-next-chapter-of-ai/；日期更正见 Issue #1 二次验收：本条曾误记为 2026-06-17，官方页面显示 2025-11-19）：golden set=「your most skilled experts' judgement and taste for what great looks like」的**活的、权威参照**（a living, authoritative reference）；从 purpose 与 most important outcomes 出发；沿真实工作流端到端构建任务、覆盖决策点；错误分析须带分类法；评测数据回流形成飞轮——**直接支撑 TOOL-005 B 节定义与 TOOL-004「核心指标优先」**；
② **METR Time Horizon 方法**（metr.org/time-horizons/）：human baseline=签约熟练专业人士（平均约 5 年经验）**在相同 instructions 与 affordances 下实际完成同批任务**，取成功完成时间的几何平均；Agent 评分另用自动成功标准，人类完成时间只用于度量任务难度——**直接支撑 TOOL-005 A 节（人工表现基准≠黄金答案集）**；自报局限：人类时长估计可能偏高。
｜官方一手｜L1｜抓取/核验 2026-08-17｜TOOL-004/005、DEL-008｜—｜High（原文在手）｜2026-08-17

## D 组｜待获取与已补证（Palantir 批次已核验，2026-08-17，见 RN-20260817-001）

**EV-PAL-001** ✅｜Palantir｜Delta 官方定义 / Edge→Core 机制｜① Delta=Forward Deployed Software Engineer 官方代称（源自 NATO 字母表），与 Dev 分属 Business Development / Product Development 事业部；② Dev=「one capability, many customers」，Delta=「one customer, many capabilities」；③ Delta 常向核心产品回交代码，大功能须对照产品 roadmap 验证并入、由产品团队 review；④ 官方明确 Delta≠咨询顾问（部署既有产品、建长期方案）｜官方博客｜L1｜《Dev versus Delta: Demystifying engineering roles at Palantir》2019-04-08，blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87｜抓取 2026-08-17｜官方机制证据：Delta 代码回流 Core 的协调与评审流程｜ORG-002/003、DOC-007｜—｜High｜2026-08-17
→ 注：该文未出现「Echo」一词；官方体系中与 Echo 职能对应的是 Deployment Strategist（官方博客《A Day in the Life of a Deployment Strategist》，两角色官方自述「界限经常模糊」）。

**EV-PAL-002** ✅｜Palantir（前员工）｜泛化分工 / Foundry 起源 / 反方证据｜① FDE（驻场，每周 3-4 天在客户处）与 PD（产品开发）二分：「你的工作是解决问题、不用管过拟合；PD 的工作是把你做的泛化再卖给别人」；② FDE 手工苦活被产品化：Magritte→Contour→Workshop，「现在驱动公司 50%+ 收入，它叫 Foundry」；③ 2023 毛利 80% vs 埃森哲 32%（**前员工原文四舍五入说法，官方一手校正=FY2023 81% vs 32.3%，见 EV-PAL-004**）；④ 客户团队 4-5 人、高速自治；⑤ 反方：技术债重、差旅失控、数据获取是政治问题、早期是「培养皿」；⑥ Airbus A350 制造提速 4x；⑦ 数据集成与 RBAC/审计是核心工作｜前员工回忆（8 年 FDE）｜L2｜Nabeel Qureshi《Reflections on Palantir》2024-10-15，nabeelqu.substack.com/p/reflections-on-palantir｜抓取 2026-08-17｜Edge→Core 的「泛化是 PD 的专职工作」与产品化的真实路径；同时是 FDE 模式成本侧的主要一手证据｜DOC-003/007、COM-004、ORG-003；反方→全模块｜—｜High｜2026-08-17

**EV-PAL-003** 🟡（与 EV-POD-001 为不同来源：本条 = YC Lightcone 原始访谈及其 AI 摘要页；EV-POD-001 = 中文二次解读节目，勿混用，DEC-2026-011）｜Palantir（前高管口述）｜Echo/Delta 配对 / 碎石路→柏油高速 / 商业指标 / 定价｜① Echo=嵌入式分析师（客户现场、和最终用户交流、识别可解问题与 demo、维护客户关系；画像=领域专家+「异见者」+能看到 3x-10x 改进空间）；② Delta=快速写码的部署工程师（错配画像=工匠型完美主义者）；③ 泛化六步：现场建方案→带回产品团队→FDE 参与泛化讨论→找 3 个「微妙不同但同底层数学」的工作流→多客户共同设计→跨客户验证；④ 本体（Ontology）=防碎片化的平台机制（通用 schema+客户自定义类型）；⑤ FDE vs 咨询可观测指标：新客户早期亏损→约 1 年后毛利转正、现场团队缩小、产品变好、「挣得权利」；⑥ 两大内部指标：客户结果价值/合同规模 + 产品杠杆；⑦ 定价趋向 outcome-based、合同随价值增大（Kastle/HappyRobot 例）；⑧ 准入：必须进入 CEO 前五大问题；⑨ 自警：FDE 会漂移成咨询、产品-FDE 张力「对所有人都痛苦」；⑩ 100+ YC 创业公司在招 FDE｜YC Lightcone 播客（口述一手，页面记录为 AI 摘要）｜L2（内容）/L3（记录）｜《The FDE Playbook for AI Startups with Bob McGrew》2025-09-08，podcosmos.com/ycombinator/lightcone-podcast/…（YouTube 原片待逐段复核）｜抓取 2026-08-17｜ORG-001/002/003 的直接参照；COM-002/004、DOC-003/004/006/007 的首个单组织实证｜McGrew 自述反方见 ⑨｜Medium-High（内容）/Medium（记录）｜2026-08-17

**EV-PAL-004** ✅（2026-08-18 登记官方一手校正，Reviewer 核验、URL 在案）｜Palantir + Accenture｜公司级毛利背景｜Palantir **FY2023 GAAP 总体毛利 81%**（SEC 10-K：sec.gov/Archives/edgar/data/0001321655/000132165524000022/pltr-20231231.htm）；Accenture **FY2023 gross margin 32.3%**（官方 FY23 Q4 财报稿：investor.accenture.com/~/media/Files/A/Accenture-IR-V3/quarterly-earnings/2023/q4fy23/final-q4-fy23-earnings-press-release.pdf）｜同期间、同为公司总体 gross margin 口径；**业务组合不同，不证明 FDE 团队、复用机制或部署杠杆的因果贡献**——仅作组织级财务背景；「FDE 实证」仍以口述/机制材料（EV-PAL-002/003，上限 L2/L3）为准｜—｜商业模型 §1/§4、DOC-003、COM-004、G-06｜—｜High（一手）｜2026-08-18

**EV-LY-001** ✅（转写已取得并全读核验，2026-08-17，DEC-2026-012）｜阿里瓴羊｜《硅谷101》E248 对话朋新宇（瓴羊 CEO，阿里数据中台方法论创立者；团队做企业数据/FDE 五年，前身 CSM 团队）｜时长 63 分钟（转写头部自证）｜来源：`09_Research_Notes/Source_Materials/E248_硅谷101_对话瓴羊朋新宇_FDE落地实践_1小时03分钟.txt`（ChatGPT 推送入仓）｜等级 L3（嘉宾访谈转写；**ASR 有错字**：红军=泓君/主播、彭鑫宇·小鹏=朋新宇、林扬=瓴羊、planter=Palantir、哈尼兹/哈尼斯工程=harness 工程；引用时区分嘉宾原话与主持人总结）｜抓取/全读 2026-08-17｜瓴羊事实核验结果（均为嘉宾原话除注明）：

① **FDE 三支柱** [05:04-06:07]：以业务结果为导向（问题必须有业务目标+业务数字+**业务过往历史记录**→构建测评级/指标体系）+以企业数据为基座+**以岗位标杆为预设**（客服/投手/销冠 Agent 起步=工作五到十年水平）——**Batch 2 三对象（Baseline/Human Benchmark/Work Trace）的瓴羊版定义**；
② **260 步催发货** [07:09-08:59]：3C 数码客户催发货环节 260 多步，三类（少发/配件/赠品），流程覆盖约 95%，横跨内部系统与多电商平台；已上线效果「逼近/超出人类最好状态的平均水平」（嘉宾转述复盘）；
③ **顶尖投手 90 天** [13:24-15:40]：多平台投流客户，最好投手三个月超 1 万次价格调整，一般投手约一百多次；「所有操作都是人在做的」（嘉宾明确回答主持人追问）；工作四要素=学习(数据采集)/建模/执行/迭代 [14:03]；
④ **4+X** [35:21-36:06]：4 个预设 Agent（营销/销售/客服/运营）+X（企业数据资产与上下文管理：数据、权限、审批、资金上限）；
⑤ **三角色** [42:54-44:47]：BA（业务结果导向，编排 260 步流程、设定评测标准，行业专家）+AI 架构师（业务问题→模型尺寸与人机干预边界）+首席客服/首席销冠（**从客户内部选最好角色组成 AI 教练团，「我们的角色会退后」**）；
⑥ **部署时间** [36:22-37:10]：典型项目一年多；熟悉工作岗位占 1/3 以上，教练团调教再占 1/3（学习+调教=2/3），「真正的实施执行和系统上线反而是快的」；
⑦ **灰度上岗** [40:55-42:11]：第一天 0-2 点低谷流量→评审调整；第二天 12-14 点高峰**全段流量**（「只有全量才知道异常的边界」）；第三天 8 小时渐扩，一周达到参照系（最好作息或内部最优员工标准）；
⑧ **商业模式** [22:29-23:52, 29:56-31:13]：两类——按坐席收费（如 500 客服 8-9 折成本替代同效果）+按效果分成（转化率超出人工部分分成）；效果付费「肯定是有的，而且是连续续费」；结算经 MVP+AB test；
⑨ **场景三问** [09:00-09:48]：哪里耗人最多/耗钱最多/耗时最多；
⑩ **定制/标准/个性化** [23:52-25:07]：「用定制化方式解决标准化问题；用标准化方式解决个性化问题」；
⑪ **对 Palantir 的界定** [28:35-29:35]：「Palantir 服务的企业原来都有基座，它是帮客户找出有价值的问题，而不是帮客户实现 to-do list 的 100 个功能需求」（46-47% 商业营收数字出自主持人）；
⑫ **中国市场差异** [53:38-54:45]：缺 Salesforce/SAP 式工作流与数据标准→「从打桩盖楼到装修都要干完」；大企业自有 IT 团队→纯交付无价值；
⑬ **反方/成本自曝** [47:27-47:59]：Q1 某 AI 项目收入约 300 万、投入约 1200 万，季度末才打平；[37:34] 执行层抵触「这是人性」；[19:56-21:11] 生产关系（IT 预算 vs 业务预算）是主要阻力，成功案例均为一号位自上而下；
⑭ **模型升级纪律** [52:34-53:28]：模型绑定不自动升级，升级须人工确认+测+对比效果；
⑮ 主持人总结（非嘉宾原话，引用须标注）[09:48-10:35]：260 步说明「客服最重要的是解决问题=对全公司业务流程每一环节的理解」——任务书 H-8「困难在完整上下文与 Action Chain」的近义表述来自此段主持综合。

｜支撑：H-2（✅瓴羊事实）、H-7（✅投手案例=优秀员工真实行为作训练对象）、H-8（▲ 260 步为事实，Action Chain 归因为主持综合）、H-9（✅「只有全量才知道异常边界」）、ORG-004、DEL-008/009 中国样本、COM-003/005｜反方：⑬｜Medium-High（转写一手、无原始音频比对）｜2026-08-17

**EV-LY-002**（防护性别名）｜Bob McGrew/Palantir 类二次解读节目**不得**登记为瓴羊来源；见 EV-POD-001。两份转写严禁混用（DEC-2026-011）。

**EV-POD-001** 🟡（转写已取得 2026-08-17，内容等级不变）｜小宇宙 episode `68c6eb41`《极客飞行日志》｜Bob McGrew/Palantir FDE 二次解读｜**Source metadata**：发布 2025-09-14｜时长 32 分钟（转写头部自证）｜来源：`09_Research_Notes/Source_Materials/FDE_Palantir_Bob_McGrew_二次解读_32分钟.md`（ChatGPT 推送入仓）｜双主持对谈体、AI 生成内容（页面声明）；头部与抽样核验：内容与 EV-PAL-003（Lightcone）一致（YC 招聘板 100+ FDE 职位、Bob McGrew 视角等）；ASR 错字（Baumgartner/Bom McRae=Bob McGrew）｜等级维持：L3（记录）、L4（内容），只作结构线索，不独立支撑主张｜—｜—｜Low｜2026-08-17 更新

**EV-TOM-001** 🟡（2026-08-18 按 Issue #3 复核 P0-4 精确化）｜Tomoro（收购前独立样本）｜① **首页已迁移**（tomoro.ai→deploy.co）；② **部分旧文章被迁移保留**：部分旧路径重定向至 deploy.co/news/… 且保留原日期与正文（例：2026-03-31 的 business-critical AI 文，复核方定位）；另一些路径 404；③ **本批未找到可直接证明 Tomoro FDE 组织分工的原始页面**——逐主张核验前不写「网站全不可得」；④ 可承载主张：约 150 名 FDE/部署专家（来源=收购方公告 EV-OAI-002④）；此前客户 Tesco/Virgin Atlantic/Supercell（同上⑦）；⑤ 「12 周生产」等流传主张无页面可核，未采信｜官方残迹（部分保留）+收购方转述｜L2（他方转述为主）｜2026-08-18｜仅作收购前独立样本计票；旧文快照可后续经 deploy.co/news 或存档服务补｜ORG 交集第 4 票（受限）｜—｜Low-Medium｜2026-08-18

---

## 引用规则

1. 任何规则升级为 FACT/OBSERVATION 前，其证据行必须全部 ≥ 🟡 且至少一条 ✅ 的 L1/L2；
2. 🔴 条目只能出现在 Hypothesis 的「验证途径」栏；
3. 每次定向研究（Phase 5）结束，新增/更新条目须更新 Last Verified 并在对应 RN 中登记。

**EV-EXT-008** ✅（2026-08-18 本地核验，Issue #4 指定锚点）｜GOV.UK + NIST｜部署后状态与监测的 L1 模式锚点｜
① **GOV.UK 服务手册**（L1 官方）：alpha=探索方案；beta=「take your best idea from alpha and start building it for real」——私测先邀**少量真实用户**→过评估→公测→live；beta 期即开始采集成功数据并迭代，live 延续——支撑「受控上线→真实使用→现场验证」状态分离（https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works；原型分册 https://www.gov.uk/service-manual/design/making-prototypes；live 分册 https://www.gov.uk/service-manual/phases/live/（核验 2026-08-18））；
② **NIST AI 800-4《Challenges to the Monitoring of Deployed AI Systems》2026-03-09**（L1 官方）：基于三场 2025 CAISI 从业者工作坊+文献综述；部署后监测横跨功能/运行/人因/安全/合规/大规模影响六类；「post-deployment monitoring – from incident monitoring to field studies – is a crucial practice for confident, wide-spread AI adoption」；明确缺口：「Insufficient research on human-AI feedback loops」「Immature information sharing ecosystem」——支撑使用轨迹采集与反馈路由必要性（https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems（核验 2026-08-18））；
③ **OpenAI Cookbook《Eval-driven system design: receipt inspection》**（官方托管实践案例）：本方本地抓取两次返回 403（访问记录保留）；**Reviewer 2026-08-18 从官方 developers.openai.com 成功打开全文核验**——状态=已核的官方托管实践案例（非行业标准、非 OpenAI 强制政策）；可承载主张仅限：从小规模标注数据开始；建立最小系统与初始评测；以业务 KPI/成本影响校准优化；评测驱动迭代与扩展数据。URL：https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection
｜支撑：DEL-011、TOOL-007、DEC-2026-015（仅总体模式；通元落位=DESIGN DECISION）｜—｜High（①②原文在手；③复核方核验）｜2026-08-18 更新

**EV-ANT-003** ✅（2026-08-18 本地全文核验，Batch 5 指定锚点）｜Anthropic｜评测方法 L1 锚点｜《Demystifying evals for AI agents》：① 定义五件套——task（单次测试，含输入与成功条件）/trial（一次尝试，输出不稳须多 trial）/grader（评分类逻辑，可多个）/trajectory（trial 完整记录：outputs、tool calls、reasoning、intermediate results）/outcome（trial 结束时环境最终状态，例：预订是否存在于 SQL 库）；② **能力集 vs 回归集分离**：能力集「选系统挣扎的任务，低通过率爬坡」，回归集「应接近全过、持续运行防漂移」；毕业机制=高通过率能力集可毕业为回归集；③ 评分器三型（代码：快/客观/可复现但脆；模型：灵活但须与人工专家校准、允许「无法判定」出口；人工：金标准但贵慢）——「deterministic where possible, LLM where necessary, human judiciously」；④ 自动评测与生产监测互补（瑞士奶酪模型：「automated evals for fast iteration, production monitoring for ground truth, periodic human review for calibration」）；⑤ 「20-50 条真实失败案例起步即可」（早期实践参照，非硬阈值；成熟系统需更大更难评测集）｜官方工程博客｜L1｜anthropic.com/engineering/demystifying-evals-for-ai-agents｜核验 2026-08-18｜支撑 DEL-012/TOOL-008（评测方法）；**不支撑受控部署方法**（边界 6）｜—｜High｜2026-08-18

**EV-NIST-002** ✅（2026-08-18 核验；**2026-08-18 返工更正来源**：原写「AI RMF 1.0 Playbook」不准确，Manage 4.1-4.3 条款原文出自 **AI RMF 1.0 Core, Table 4**；Playbook 为建议集合另行引用不混称）｜NIST｜部署后控制类别 L1 锚点｜AI RMF 1.0 **Core, Table 4, Manage 4.1-4.3**：**Manage 4.1** 部署后监测计划（含用户输入捕获与评估、申诉/覆盖、停用/退役、事件响应、恢复、变更管理）；**Manage 4.2** 持续改进（反馈整合、可信特征入改进指标、与法律框架对齐）；**Manage 4.3** 事件与错误沟通（向相关方与受影响社区通报、错误与未遂事件库、版本史）｜官方框架 Core｜L1｜https://airc.nist.gov/airmf-resources/airmf/5-sec-core/（Core Table 4）；Playbook 建议如引用另记页面｜核验 2026-08-18，返工更正 2026-08-18｜支撑 DEL-013/TOOL-009 的**控制类别清单**（监测/申诉/停用/响应/恢复/变更/沟通）；不替通元决定具体模式或阈值｜—｜High｜2026-08-18

**EV-OAI-004** 🟡（2026-08-18 检索留痕；同日按二次验收收敛为限定表述）｜OpenAI 部署公司 + Tomoro｜计费与结算条款｜**限定结论：截至 2026-08-18，在已检查的 OpenAI 启动公告（openai.com/index/openai-launches-the-deployment-company/）、deploy.co 首页及所列检索路径中，未发现 DeployCo/Tomoro engagement 的具体计费与结算条款**。① OpenAI 通用 Business/API 价格页**存在**（openai.com/business/pricing/）——不等于 DeployCo engagement 定价；② 19 家投资伙伴=启动公告官方事实（EV-OAI-002，L1）；③ 分析师「按结果/任务付费」预期=转述层观点（例：Coommit coommit.com/blog/forward-deployed-engineer-ai-2026；The AI Opportunities playbook theaiopportunities.com/p/the-openai-deployment-company-playbook），**不承担正文主张**；模糊估值口径（媒体 100-140 亿美元不一致）删除不用；④ 检索词（2026-08-18）：DeployCo pricing／OpenAI Deployment Company pricing model／Tomoro AI pricing——官方计费条款未命中｜官方页 L1（结构事实）/计费 Unknown（限定范围）｜抓取+复核 2026-08-18｜商业模型 §1/§8｜—｜Low（转述层）/High（负面检索范围如实）｜2026-08-18 更正


**EV-CN-001** 🟡（2026-08-18 检索登记，Batch 8）｜中国企业 AI 失败素材（单方叙述）｜《七个月驻场，六周失准：团队缺的不是 AI，是 FDE》（知乎专栏，zhuanlan.zhihu.com/p/2052808167919293158）：杭州某制造企业 AI 质检——乙方 3 名驻场工程师 7 个月，上线 6 周后模型失准；归因=数据漂移+业务闭环缺失｜自媒体单方叙述｜L4（未核当事人）｜抓取 2026-08-18｜仅作 DEL-007（数据质量攻击）/DEL-010（抵触与失用）的攻击素材，**不作为事实结论**｜—｜Low｜2026-08-18

**EV-CN-002** 🟡（2026-08-18 检索登记）｜中国 FDE 讨论与 toB 约束（媒体课程层）｜① InfoQ/极客时间《Demo 能跑，项目却落不了地：企业真正缺的是 FDE 能力》——6 类高频失败模式（需求失真/价值不清/验收困难等，infoq.cn/article/ZvwSZ2U61Q8uBMerbYD9）；② 至顶网 2026-07《为什么中国企业 AI 落地更需要 FDE？》——中国 toB 特殊约束：招投标、账期、信创合规（zhiding.cn/ai-applications/2026/0728/3194636.shtml）；③ 网易智企《复盘 100+ AI 项目》｜媒体/课程转述｜L3-L4｜抓取 2026-08-18｜DOC-001 攻击背景（低价驻场市场存在）；**未找到可核的中国 FDE 机制失败一手复盘——检索范围与缺口记录：两组检索词×2 变体（2026-08-18），命中均为媒体层**｜—｜Low-Medium｜2026-08-18