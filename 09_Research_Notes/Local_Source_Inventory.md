---
id: RN-SRC-INV
type: source-inventory
version: 0.1
updated: 2026-08-16
scan-scope: /Users/cambia/Documents, /Users/cambia/Downloads, /Users/cambia/Desktop, /Users/cambia/ZCodeProject, /Users/cambia(home顶层), Obsidian vault
scan-mode: 只读扫描（未修改任何原文件）
---

# 本地资料源清单 Local Source Inventory v0.1

扫描日期：2026-08-16。方法：Spotlight（mdfind）+ find 文件名匹配 + 关键词内容 grep（FDE / Palantir / 瓴羊 / 朋新宇 / 催发货 / 蓝图 / 交付手册 / Forward Deployed / Echo / Delta / Tomoro / FDE OS）。

**总体结论**：FDE 相关本地资产远比任务书预设的丰富——交付规范的元系统（手册规范 V0.2）已存在且成熟，官网侧已完成一轮「信用证据」诚实化审计；但任务书点名的两份文件（E248 瓴羊转写、蓝图 V0.3）**在本地不存在**，且 Palantir Echo/Delta、瓴羊一手证据均无本地落盘。

---

## T1｜FDE 核心文档（体系直接输入）

| # | 文件 | 日期 | 规模 | 与 FDE OS 相关度 | 深读 | 冲突/重复 |
|---|---|---|---|---|---|---|
| 1 | `/Users/cambia/Downloads/FDE手册编写与现场验证规范_V0.2.md` | 2026-07-24 | 2223 行 / 65KB / sha d1d4ded2ff7f | **极高**——交付手册的编写与验证宪法：8章结构、证据等级、成熟七态、四层验证、四张控制台账、四个闭环、能力资产六类（含失败模式） | ✅ 已全文读 | 见 #2 版本关系 |
| 2 | `/Users/cambia/FDE手册编写与现场验证规范.md` | 2026-07-23 | 2717 行 / 57KB / sha 9e0864718568 | 高——同文档 **V0.1** 试行稿；ForFlow README 引用的是此路径（存在版本滞后：在建工作台指向旧版） | 抽查 | #1 的前一版，内容重叠 |
| 3 | `/Users/cambia/Documents/ForFlow/FDE手册第一版/`（README + 闭环一 7 文件） | 2026-07-23 | 17.8/8.3/6.7KB + 3 工具草案 ~10-13KB | **极高**——闭环一（项目准入）在建件：证据台账、章节决策设计稿、历史回放（网络货运支付前智能审核）、3 个工具草案；README 自认「尚未达到编写门槛」 | ✅ 已派 Agent 提取 | 无 |
| 4 | `/Users/cambia/Downloads/deep-research-report.md` | 2026-08-12 | 622 行 / 54KB / sha 1c51cb1d7231 | 高——商业引擎输入：信用冷启动研究（陌生→关系→行为→交付→Reference→机构信用阶梯），任务书 v0.2 约束下 | ✅ 已派 Agent 提取 | 无 |
| 5 | `/Users/cambia/ZCodeProject/FDE模式AI转型可行性分析.md`（+ _original.html） | 2026-07-22 | 326 行 | 中——**注意：这是第三方 Scribd 报告，其 FDE = Field Driven Engineering（湖南"智赋万企"共享驻场），与 Forward Deployed Engineer 不同概念**。仅作中国腰部企业落地的外部视角样本，禁止混入 FDE OS 主线 | 章节级已读 | 与主线概念冲突，须隔离 |

## T2｜公司真实项目材料（证据库 TY 条目来源）

| # | 来源 | 日期 | 相关度 | 说明 |
|---|---|---|---|---|
| 6 | `kimi/workspace/tongyuan-wenke/`（官网重构工程） | 持续至 2026-08-16 | **极高** | `src/content/methodology.md`（对外方法论五阶段）；`settlement-coordination.md`（结算异常协同案例，无客户名、无效果数字、状态含糊）；`supply-chain-research-kb-poc.md`（知识库 PoC，合同已签、验收结果未披露）；`docs/02-credit-evidence-inventory.md`（13 条信用证据分级：旧官网 8 套系统/4 个已投产标签/+18%等指标被判定不可公开，正下线）；`audit/product-design-2026-08-16/report.md`（对标 Palantir AIP Bootcamp「5 天三个结果」与 OpenAI Deploy Co） |
| 7 | Obsidian vault：`/Users/cambia/Documents/Company/Company/` | 2026-04~06 | 高 | `商业判断/产品与交付/` 会议笔记（供应链AI知识库项目合作/启动评估、群核科技 AI 落地等）；`Maps/Topics/`（企业AI转型、AI Agent落地、AI商业化、供应链智能化）；`商业判断/组织与产业/`（OPC认证）；`工作/中物联/采嫁销/`（数据流转图/阶段视图/内容分块） |
| 8 | `/Users/cambia/Documents/202606-通元问科-技术服务合同（中物联现代供应链研究院）.doc` | 2026-06-11 | 高 | 知识库 PoC 的合同实物（.doc 未解析，需时再提取条款） |
| 9 | `/Users/cambia/Documents/Company/Company/供应链行业AI知识库与深度研究报告系统_签约前测算报告.pdf` | 2026-05-29 | 高 | 签约前测算（对应 kb-poc L25「50 份资料/5 万字」测算场景的原始出处，未解析） |
| 10 | `/Users/cambia/Documents/【260713】白银集团网络货运及供应链关联业务数字化与AI升级总体方案.pdf` | 2026-07-13 | 高 | 白银集团项目方案（手册规范点名的第 3 个贯穿案例「白银集团智能仓储」，未解析） |
| 11 | `notes/contract-doc-engine/` | 至 2026-08-15 | 高 | 供应链结算异常协同的后端 MVP（FastAPI+14表+37端点，合同审查引擎）——手册规范点名案例的工程实物 |
| 12 | `notes/freight-audit-prototype/` | 2026-07-28 | 高 | 网络货运支付前智能审核原型（闭环一历史回放对应的工程实物） |
| 13 | `Documents/供应链采购销售工作流/`（采嫁销工具） | 2026-06-04 | 中 | 中物联采嫁销协同工具（数据流转/阶段视图见 vault #7） |
| 14 | `notes/commerce-intelligence-workbench/` | 2026-08-15 | 中 | 跨境电商 AI 工作台（咨询级报告自动生成管线）——可作为 FDE OS 的第二个领域样本，与供应链主线弱相关 |
| 15 | `Downloads/于健镕_企业AI转型_FDE_简历_*.pdf/html`（5+ 份） | 2026-08 前后 | 低-中 | 个人 FDE 简历物料（对外输出层参考，非体系输入） |

## T3｜外部样本与待引来源（未落盘）

| # | 来源 | 状态 |
|---|---|---|
| 16 | 小宇宙 E248 对话阿里瓴羊朋新宇（中国式 FDE / 260 步催发货 / 顶尖投手 / 4+X / 灰度上岗） | **本地未找到**——全盘 grep「瓴羊/朋新宇/催发货/260步」零命中。任务书声称的内容（§10）暂只能以「用户转述」登记，证据等级 L3-待核 |
| 17 | 小宇宙 episode `68c6eb41a56ca3e0c4629d0f`（Palantir FDE / Echo / Delta / Bob McGrew 二次解释） | 本地无转写；URL 在任务书 §11 |
| 18 | OpenAI Deployment Company 官方页 `openai.com/index/openai-launches-the-deployment-company/` | 未抓取 |
| 19 | Tomoro `tomoro.ai` | 未抓取 |
| 20 | Palantir 官方文档/Blog/招聘页（Echo/Delta/Core、Foundry/AIP/Ontology） | 未抓取 |

## T4｜低相关（已排查排除）

- `notes/dashboard-chat/`、`notes/workbuddy-proxy/`、`Documents/wechatCrawl/`、`Documents/qianliu/`、`Documents/dsh/`（空）、`Desktop/商业洞察`（空）、`Codex/2026-07-23/fde-1-fde-ai/`（空壳 outputs/work，无内容）
- `Documents/AIPKM/.work/feishu-video-case/`（飞书 Agent 案例视频分析，泛企业 AI 样本，暂不纳入）
- `Documents/行业ai案例/customer-notes-to-action-list`（客户笔记→行动清单小工具，暂不纳入）

---

## 关键缺口与异常（供 Gap Map 引用）

1. **E248 瓴羊转写与《蓝图 V0.3》本地缺失**——前者是瓴羊证据的唯一来源但只剩任务书转述；后者可能从未保存（V0.1→V0.2 均在，V0.3 无踪）。
2. **五个真实项目均有「实物/文档」但证据形态不一**：知识库 PoC（合同+测算+案例页）、结算协同（后端工程+案例页）、网络货运审核（原型+历史回放）、白银（方案 PDF）、采嫁销（工具+流程图）——但**没有一个项目有基线（Baseline）数据落盘**。
3. **手册规范（V0.2）与 ForFlow 工作台（依据 V0.1 路径）存在版本漂移**。
4. **对外宣称与内部事实的差距已被官网审计系统暴露**（已投产标签/量化指标不可公开）——FDE OS 必须承接这套诚实化纪律，防止输出层反噬母体。
5. 本地无任何 Palantir/OpenAI Deploy/Tomoro 原始材料落盘，全部外部证据依赖后续网络研究。
