# 通元问科 FDE 交付操作系统（Tongyuan FDE Operating System）

**版本**：v0.1（骨架轮）｜**建立日期**：2026-08-16｜**当前阶段**：Phase 1-4 + 6/7 完成，Phase 5（定向研究）未启动

## 本地查看器

```bash
cd Tongyuan-FDE-OS
python3 server.py            # 打开 http://127.0.0.1:8795
```

只读文档视图：左侧目录树（12 模块骨架，空目录显示「未建」）+ 正文按 .md 源文件实时渲染（每次打开都从磁盘重读，改完即见）+ 全文搜索（输入关键词列出命中文件与上下文片段，点击跳转高亮）+ 右侧本页目录。查看器不做任何内容修饰；frontmatter 中的 version/status/updated 显示在正文上方。除 `index.html`、`marked.min.js`、`server.py` 三个查看器文件外，目录内全部为 .md 内容文件。

---

## 这个系统现在是什么状态

FDE OS 是通元问科的内部交付操作系统母体。今天（2026-08-16）完成的是**第一轮：本地盘点 + 系统骨架**。8 份交付物已就位，但没有任何模块内容、没有任何规则达到现场验证状态。

一句话现状：

> 我们已经有一部相当成熟的「交付手册宪法」和一次真实的历史回放；完全没有的是组织模型、商业定价结论、瓴羊与 Palantir 的一手证据，以及所有项目的基线数据。

## 哪些东西已经相对可靠

- **交付流程的准入段**：L0-L5 六级准入层级、三个作业工具草案、直接否决/退回/缩小条件——经过一次真实项目回放检验（网络货运项目，回放把方案的 L2 建议诚实降级为 L1）。
- **证据纪律**：六级证据优先级、「方案文件不能证明效果」、三层记录分离（建议/业务确认/批准）——已在闭环一落地。
- **官网信用三层与未证实宣称下线**——已经执行过一轮审计。
- 外部锚点四个：OpenAI FDE 岗位说明、OpenAI Deployment Company、NIST AI RMF、Anthropic 复杂度阶梯（均为 L1，两条待抓原文）。

## 哪些还是假设（不许写成事实）

- Echo/Delta/Core 组织映射、Client Coach、十阶段链的线性顺序、Deployment Leverage 与四健康指标、Value Depth 深化路径、「不卖人天≠结果付费」的分离框架、Work Trace 作为 Agent 训练主来源、瓴羊全部六项主张（260 步/投手/4+X/灰度/部署时间/三角色）——全部标 HYPOTHESIS，证据库中为 🔴 来源缺失状态。
- 所有五个真实项目（协会知识库 PoC、网络货运审核、白银仓储、结算协同、采嫁销）都没有基线数据，除知识库 PoC 有合同实物外，验收/运行证据普遍缺失。

## 从哪里开始阅读

| 顺序 | 文件 | 用途 |
|---|---|---|
| 1 | `00_Master_Index/FDE_OS_Information_Architecture_v0.1.md` | 系统宪法：模块、编号、三层状态词汇 |
| 2 | `00_Master_Index/FDE_OS_Master_Index_v0.1.md` | 全部规则的总控表（当前 35 条骨架） |
| 3 | `09_Research_Notes/Existing_FDE_Knowledge_Audit.md` | 最重要的单一文档：已有知识按 FACT/OBSERVATION/INFERENCE/DESIGN/HYPOTHESIS 五分类，含 10 项矛盾清单 |
| 4 | `09_Research_Notes/Local_Source_Inventory.md` | 本地 20 组资产盘点（含两份点名文件缺失的结论） |
| 5 | `06_Evidence_Library/FDE_Evidence_Library_v0.1.md` | 证据库（✅已核 14 条 / 🟡转引待核 / 🔴来源缺失 4 组） |
| 6 | `09_Research_Notes/Research_Gap_Map_v0.1.md` | 15 个缺口 + P0 检索问题定义 |
| 7 | `10_Decision_Log/Decision_Log.md` | 九项已登记设计决定 |
| 8 | `09_Research_Notes/RN-20260816-001-local-discovery.md` | 本轮研究笔记 |

## 下一轮研究是什么（待确认后启动）

P0 四项（见 Gap Map）：Palantir Echo/Delta/Core 一手机制（G-01）→ 瓴羊 E248 补证（G-02）→ Baseline 阶段方法（G-03）→ Work Trace 方法论（G-04）。同时内部动作：四项目 P0 材料 26 项的补齐请求（G-13）、链路重检工作坊（G-05）。

## 与既有文件的关系（重要）

本系统**不替代、不移动、不覆盖**任何既有文件：
- 《FDE手册编写与现场验证规范》V0.2（Downloads）= 03/05 模块的编写宪法，原位有效；
- ForFlow「FDE手册第一版」= 闭环一在建件，原位继续；
- Obsidian vault = 公司知识库，以引用接入；
- tongyuan-wenke 官网工程 = 输出层（08）的反向校验对象。

## 维护规则速记

1. 每条重要判断标知识状态；来源标 L1-L5；规则/工具标成熟状态——三套词汇不得混用（IA §4）。
2. 没有真实项目证据不得标 Field-tested/Validated。
3. 结构性改动必须登记 Decision Log。
4. 每轮研究必须留 RN 笔记。
5. 输出层（官网/PPT/提案）只能从母体编译，不得反向修改事实。
