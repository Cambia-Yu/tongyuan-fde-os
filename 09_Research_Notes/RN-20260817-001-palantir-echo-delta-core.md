---
id: RN-20260817-001
type: research-note
topic: batch1-palantir-echo-delta-core
date: 2026-08-17
batch: Batch 1（协议 §八）
gaps: G-01, G-06（部分）
---

# RN-20260817-001｜Batch 1：Palantir Echo / Delta / Core

## Question
任务书 §5 提出的三问：Echo 承担什么？Delta 承担什么、可否改产品？Core 如何把碎石路修成高速公路（谁提交、谁判断泛化、如何防污染）？——对应 G-01，现状 EV-PAL-001~003 全部 🔴。

## Sources（三级证据链，全部本次核验）
1. **L1 官方**：Palantir 官方博客《Dev versus Delta: Demystifying engineering roles at Palantir》2019-04-08，作者 Bruno Pontes Soares Rocha（Palantir 招聘经理，访谈多位 Delta/Dev）。
2. **L2 一手从业者（口述）**：YC Lightcone 播客《The FDE Playbook for AI Startups with Bob McGrew》2025-09-08（McGrew：PayPal→Palantir 早期工程负责人→OpenAI Chief Research Officer→美陆军预备役 Lt Col, Detachment 2011）。本次经 PodCosmos AI 摘要页全文核验（摘要为 AI 生成，标注时间戳；YouTube 原片未逐帧复核——**残余风险登记**）。
3. **L2 一手从业者（文字）**：Nabeel Qureshi《Reflections on Palantir》2024-10-15（Palantir 8 年 FDE）。
4. **L3 中文转述**：小宇宙 68c6eb41《极客飞行日志》2025-09-14——页面自我声明「播客内容由 AI 结合公开资料生成」。**确认为 AI 生成节目，非人类访谈**；其内容与 Lightcone 一致，仅作结构线索，不得独立引用。

## Findings

### 1. Delta（前线部署软件工程师，FDSE）——L1 官方确认
- Palantir 四事业部：Product Development / **Business Development** / Internal Development / Sales；Delta 与 Dev 分属 BD 与 PD。
- 名称来源：早期 BD 各团队以 NATO 字母表命名，Delta 沿用为 FDSE 代称。
- Dev="one capability, many customers"；Delta="one customer, many capabilities"。
- 官方明确 Delta ≠ 咨询顾问：顾问做一次性分析，Palantir 部署既有产品、建长期方案。
- Dev↔Delta 转岗常见（作者本人即 FDSE 出身）。

### 2. Echo（嵌入式分析师）——L2 口述，未见官方文档
- McGrew：Echo 直接到客户现场、直接和最终用户交流、识别可用 demo 与可解问题、维护客户关系；画像=领域专家（前军官/医疗背景）+「异见者（heretics）」+ 能看到 3x-10x 改进空间。
- 官方招聘体系中的对应角色是 **Deployment Strategist**（官方博客《A Day in the Life of a Deployment Strategist》），官方自述两角色「界限经常模糊」。
- **裁决**：Echo 作 Palantir 实践事实记 L2（口述）；官方文档未用「Echo」一词——不写「Palantir 官方设有 Echo 岗」。

### 3. Core 泛化机制（碎石路→柏油高速）——L1+L2 双重确认，本次最高价值发现
- **L1（官方，2019）**：Delta 常把代码贡献回核心产品；大功能需求须与产品团队对照 roadmap 验证后并入，改动由产品团队 review。
- **L2（Nabeel，2024）**：「你的工作是解决问题、不用管过拟合；PD 的工作是把你做的泛化再卖给别人」；FDE 的手工苦活被 PD 逐个产品化——Magritte（数据接入）→Contour（可视化）→Workshop（应用搭建）——「现在驱动公司 50%+ 收入，它叫 Foundry」；2023 毛利 80% vs 埃森哲 32%。
- **L2（McGrew，2025）**：泛化六步——FDE 在单客户现场建方案→带回产品团队→FDE 参与泛化讨论→找出 3 个「微妙不同但同底层数学」的工作流→多客户 FDE 共同设计→跨客户验证；本体（Ontology）即防碎片化的平台答案（对象/属性/媒介/链接的通用 schema + 客户自定义类型）；传统 PM 常因不会「上跳一层抽象」而失败。
- **防污染机制**：不是所有客户定制都入 Core——产品团队掌握「对下 10 个客户成立」的抽象判断；原 FDE 全程参与防「正确方向但错误抽象」。

### 4. 商业结构证据（供 COM/DOC 规则）
- FDE vs 咨询的可观测指标（McGrew）：新客户早期亏损→1 年后毛利转正；现场团队缩小；产品随部署变好；「挣得权利」进入更重要问题。
- 两大内部指标：①交付给客户的结果价值（及合同规模）②产品杠杆（FDE 不加人交付更多价值）——与任务书 §7.2 四变量假设高度吻合（单组织证据）。
- 定价：FDE 模式趋向 outcome-based + 大合同随价值增长（Kastle/HappyRobot 例）；「传统 PMF=压低单客户工作量，FDE=推高合同价值」。
- 筛选条件：必须进入 CEO 前五大问题；创业公司主动承担执行风险换信任。
- 规模信号：100+ YC 创业公司在招 FDE（三年前≈0）；「OpenAI 是总部产品团队，AI 创业公司是 FDE 团队」。

### 5. 反方/成本证据（任务书 §29 要求）
- Nabeel：FDE 代码技术债重（"gets the job done fast"）、每周 3-4 天驻场差旅失控、数据获取是政治问题、公司早期是「培养皿」。
- McGrew 自警：FDE 团队会漂移成咨询（客户要什么建什么≠客户需要什么），需领导层持续纪律；他自己最初的建议是「don't do this at home」；产品团队与 FDE 的张力「对所有人都痛苦」，FDE 常拒绝产品团队的「杰作」。
- 适用条件暗示：高客单价+大客户+平台化（Ontology）是这套机制的前提——与任务书 §15.3 警告一致。

## Contradictions
- 「Echo」官方性：口述有、官方文档无（Deployment Strategist 是官方名）。已按措辞规则处理。
- 中文圈流传「Bob McGrew 创办公司名叫 Echo Delta」——搜索引擎 AI 摘要噪声，无任何一手来源，**不采信**。
- 小宇宙任务书钦点播客实为 AI 生成节目：任务书 §11 要求「沿播客引用回溯原始分享」的怀疑态度被证明完全正确——回溯终点即 Lightcone（已核验）。

## Implications（写入系统的最小集）
- ORG-001/002/003：获得 Palantir 具体参照物与画像/分工/泛化流程；仍是通元问科 HYPOTHESIS，置信 Low→Medium。
- DOC-007（Edge→Core）：从纯假设升级为「Palantir 事实充分（L1+L2），通元问科适用性待验」。
- DOC-003/COM-004（部署杠杆/健康指标）：获得首个单组织实证（80% vs 32%、两大指标），行业级仍为 INFERENCE。
- G-01 基本关闭；G-06 获实质单组织证据。

## Rules affected
ORG-001~003、DOC-003、DOC-007、COM-004（均为 B 类局部修正：证据列+置信度，规则文本不动）。

## Remaining unknowns
1. Lightcone YouTube 原片逐段复核（本次依赖 AI 摘要页，带时间戳，风险低但未零）。
2. Echo 的官方文档确认（Palantir careers/blog 检索「Echo」零命中；可用 DS 官方 JD 替代参照）。
3. Palantir 第二位一手人对 Echo/Delta 配对的独立佐证（Nabeel 未用 Echo 一词）。
4. 商业层：Tomoro/OpenAI Deployment Company/瓴羊的平行证据（H-4/H-5 仍单组织）。

## Source 保存
四条 URL、发布时间、抓取日 2026-08-17 已入 Evidence Library EV-PAL-001~003、EV-POD-001。
