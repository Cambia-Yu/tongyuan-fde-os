---
id: RN-20260818-002
type: research-note
topic: batch4-operating-model
date: 2026-08-18
revision: v2（二次返工：全文统一为已核版本，消除同文件新旧结论并存）
batch: Batch 4（Issue #3）
---

# RN-20260818-002｜Batch 4：组织模型（Operating Model，候选设计）

## Question
在四组织证据基础上，对 ORG-001~006 形成通元问科自己的候选组织设计；含 OpenAI 部署公司与 Tomoro 官方补证。

## Sources（本批新增核验）
1. **OpenAI 官方发布《OpenAI launches the OpenAI Deployment Company…》**（openai.com/index/openai-launches-the-deployment-company/，**发布日期 2026-05-11**——本方首抓时误读页面元数据为 2026-08-06，按复核方对当前页面的核正统一更正）。
2. **deploy.co**（OpenAI 部署公司官网，无日期仅 ©2026，抓取 2026-08-18）。
3. **tomoro.ai → deploy.co 301 重定向**（2026-08-18 实测；**部分旧文经 deploy.co/news 保留原日期正文（例：2026-03-31 business-critical AI），其余路径 404**）。

## Findings

### 补证结果（含时间切片；2026-08-18 二次返工统一口径）
- **收购状态**：OpenAI 公告原文「OpenAI has agreed to acquire Tomoro…subject to customary closing conditions, including regulatory approvals…expected to close in the coming months」——**已宣布、未交割**；tomoro.ai 首页迁移是进程迹象但非完成证据。Tomoro 按收购前独立样本计票；**首页已迁移、部分旧文保留、部分失效；本批未找到可直接证明 Tomoro 组织分工的原始页面**；「12 周生产」等流传主张无页面可核，未采信。
- **部署公司结构（官方，按公告 2026-05-11）**：OpenAI 多数持股/控制；**伙伴关系由 TPG 领衔；公司启动时有逾 40 亿美元初始投资**（原文 more than $4B initial investment，不压缩为「领投 N 家投资 X 亿」）；**Tomoro 约 150 名 FDE/部署专家计划在交割/公司启动时带入**（未交割状态下不写作已加入）；**官方仅列双称谓（FDE 与 Deployment Specialist），两者职责分工边界未披露=未知**。
- **参与模式（官方）**：聚焦诊断→少数优先工作流→FDE 进场设计-建设-测试-部署生产系统。
- **build-prove-generalize（官方，出自 deploy.co）**：「This cycle—build, prove, generalize—connects deployment to product development」——三段周期官方存在，且明确连接部署与产品开发；启动公告页无此词——任务书 §12 三段表述的证据源定位为 deploy.co。
- **案例（官方自述，无第三方核验）**：BBVA（12 万员工/25 国）；John Deere（减药 70%、客户互动 6 倍、自建评测系统测准确率）。

### 四组织角色交集（用户指定四列表格；计票口径=二次返工统一版）
| 外部原名 | 中文解释 | 可否进入通元设计 | 证据状态 |
|---|---|---|---|
| Delta（Palantir） | 前线部署软件工程师，官方内部代称 | ✅ 交集（驻场工程 4/4）→ 角色 B 素材 | L1 官方博客 |
| Echo（Palantir 口述） | 嵌入式分析师：现场找问题/维护关系 | ⚠️ 外部参照（业务侧角色 2/4 明确分轨）→ 角色 A 素材 | L2 口述，官方未确认 |
| Deployment Strategist（Palantir 官方岗） | 部署策略师：问题界定/干系人 | ⚠️ 同上（Palantir 分轨之一票） | L1 官方博客 |
| Dev/PD（Palantir） | 平台/产品开发，专职泛化 | ✅ 交集（回流 3/4）→ 角色 C 素材 | L1+L2 |
| BA（瓴羊） | 业务结果导向业务架构 | ⚠️ 外部参照（瓴羊分轨之一票，角色 A） | L3 转写 |
| AI 架构师（瓴羊） | 业务→模型尺寸/人机边界翻译 | ✅ 交集（驻场工程之一票，角色 B） | L3 转写 |
| 首席客服/首席销冠教练团（瓴羊） | 客户内部专家参与调教验收 | ⚠️ **1/4 明确机制**→角色 D 外部参照+内部设计 | L3 转写（嘉宾原话） |
| FDE / Deployment Specialist（OpenAI） | 前线部署工程师/部署专家（**双称谓，分工未知**） | ✅ 仅「驻场工程存在」计票（角色 B）；**双轨分工不计票** | L1 官方 |
| build-prove-generalize（OpenAI） | 建设-证明-泛化周期连接部署与产品 | ✅ 交集（回流 3/4 之一，角色 C 接口） | L1 deploy.co |
| 4+X（瓴羊） | 4 预设 Agent+企业数据资产/上下文 | ⚠️ 单组织产品结构，不直接入角色设计 | L3 |
| CSM（瓴羊前身） | 客户成功陪跑团队五年史 | ⚠️ 背景 | L3 |

### 交集结论（计票口径=统一版）
1. **驻场工程角色**（4/4）——唯一强交集；
2. **业务侧/技术侧双轨分离**（**2/4 明确**：Palantir、瓴羊；OpenAI 有双称谓但分工边界官方未披露=不计票；Tomoro 未知）→ 角色 A 依据=「外部参照（2/4）+内部三层分离设计」；
3. **部署→产品回流机制**（3/4：Palantir/OpenAI/瓴羊，形态各异）；
4. **客户业务教练**（**1/4 明确机制**：瓴羊；OpenAI「与领域专家工作」≠正式教练机制；通元协会「年轻骨干」属内部雏形不参与四组织计票）→ 角色 D=「外部参照+内部设计」，非跨组织共同事实。

## Contradictions
- deploy.co 案例（John Deere 70%/6x）与任务书 §12 提到的 Tomoro「12 周」主张无对应页面——后者维持不采信。
- Tomoro 旧文部分保留（deploy.co/news）与部分 404 并存——证据边界按逐主张核验表述。

## Implications
- ORG-001~004 各获得候选设计（见组织模型 v0.1.1）；ORG-005 定性条件版；ORG-006 防线清单版；量化阈值全部未知。
- 链路对齐总表三处责任缺位回填（中文候选名，标候选）。

## Rules affected
ORG-001~006 行更新（逐条，非机械升级）；DEC-2026-014。

## Remaining unknowns
1. 角色进入/退出量化条件；2. 泛化阈值（下一步）；3. 教练付费机制（商业批次）；4. 收购交割后的融合结构（待官方交割声明）；5. OpenAI 双称谓的职责分工边界（官方未披露）。
