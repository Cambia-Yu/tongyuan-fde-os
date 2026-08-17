---
id: RN-20260818-002
type: research-note
topic: batch4-operating-model
date: 2026-08-18
batch: Batch 4（Issue #3）
---

# RN-20260818-002｜Batch 4：组织协作与责任机制（候选设计）

## Question
在四组织证据基础上，对 ORG-001~006 形成通元问科自己的候选组织设计；含 OpenAI 部署公司与 Tomoro 官方补证。

## Sources（本批新增核验）
1. **OpenAI 官方发布《OpenAI launches the OpenAI Deployment Company…》**（openai.com/index/openai-launches-the-deployment-company/，页面自标发布时间 2026-08-06，抓取 2026-08-18）——注意：Issue #3 范围审查中复核方提到「2026-05-11 官方页」，与本页 2026-08-06 不一致，按证据纪律以页面自标时间为准并留此差异待复核方说明（可能存在另一更早公告页）。
2. **deploy.co**（OpenAI 部署公司官网，无日期仅 ©2026，抓取 2026-08-18）。
3. **tomoro.ai → deploy.co 301 重定向**（2026-08-18 实测）。

## Findings

### 补证结果（含时间切片）
- **收购状态**：OpenAI 页原文「OpenAI has agreed to acquire Tomoro…subject to customary closing conditions, including regulatory approvals…expected to close in the coming months」——**已宣布、未交割**；tomoro.ai 重定向是进程迹象但非完成证据。Tomoro 按收购前独立样本计票；其原官网内容已不可独立回溯，此前流传的「12 周生产」等主张无页面可核（**未采信，不登记为事实**）。
- **DeployCo 结构（官方）**：OpenAI 多数持股/控制；TPG 领投 19 家机构（含 Bain、Capgemini、麦肯锡）投资 40 亿美元以上；Tomoro 约 150 名 FDE/部署专家「自第一天起」加入；角色=FDE+Deployment Specialist 双轨。
- **参与模式（官方）**：聚焦诊断→少数优先工作流→FDE 进场设计-建设-测试-部署生产系统。
- **build-prove-generalize（官方，出自 deploy.co）**：「This cycle—build, prove, generalize—connects deployment to product development」——三段周期官方存在，**且明确连接部署与产品开发**。
- **案例（官方自述）**：BBVA（12 万员工/25 国）；John Deere（减药 70%、客户互动 6 倍、自建评测系统测准确率）——营销自述级，无第三方核验。
- **OpenAI 页未见**「build/prove/generalize」字样（该词只在 deploy.co）——任务书 §12 的三段表述证据源终于定位。

### 四组织角色交集（用户指定四列表格）
| 外部原名 | 中文解释 | 可否进入通元设计 | 证据状态 |
|---|---|---|---|
| Delta（Palantir） | 前线部署软件工程师，官方内部代称 | ✅ 交集（驻场工程 4/4）→ 角色 B 素材 | L1 官方博客 |
| Echo（Palantir 口述） | 嵌入式分析师：现场找问题/维护关系 | ✅ 交集（业务侧角色 3/4）→ 角色 A 素材 | L2 口述，官方未确认 |
| Deployment Strategist（Palantir 官方岗） | 部署策略师：问题界定/干系人 | ✅ 同上 | L1 官方博客（A Day in the Life） |
| Dev/PD（Palantir） | 平台/产品开发，专职泛化 | ✅ 交集（回流 3/4）→ 角色 C 素材 | L1+L2 |
| BA（瓴羊） | 业务结果导向业务架构 | ✅ 同上（角色 A） | L3 转写 |
| AI 架构师（瓴羊） | 业务→模型尺寸/人机边界翻译 | ✅ 同上（角色 B） | L3 转写 |
| 首席客服/首席销冠教练团（瓴羊） | 客户内部专家参与调教验收 | ⚠️ 2/4 不入交集→角色 D 参照 | L3 转写（嘉宾原话） |
| FDE / Deployment Specialist（OpenAI） | 前线部署工程师/部署专家双轨 | ✅ 交集（双轨 3/4） | L1 官方 |
| build-prove-generalize（OpenAI） | 建设-证明-泛化周期连接部署与产品 | ✅ 角色 C 接口参照 | L1 deploy.co |
| 4+X（瓴羊） | 4 预设 Agent+企业数据资产/上下文 | ⚠️ 单组织产品结构，不直接入角色设计 | L3 |
| CSM（瓴羊前身） | 客户成功陪跑团队五年史 | ⚠️ 背景 | L3 |

### 交集结论（三项入设计依据）
1. **驻场工程角色**（4/4）；2. **业务侧/技术侧双轨分离**（3/4：Palantir/瓴羊/OpenAI）；3. **部署→产品回流机制**（3/4，形态各异：代码回交/周期连接/平台预设）。反例与差异已保留（客单价/平台依赖/资本结构），未抹平。

## Contradictions
- 复核方引用的收购公告日期（2026-05-11）与我核验的启动页（2026-08-06）不一致——不裁决，登记差异（可能两份公告）。
- deploy.co 案例（John Deere 70%/6x）与任务书 §12 提到的 Tomoro「12 周」主张无对应页面——后者维持不采信。

## Implications
- ORG-001~004 各获得候选设计（见组织协作与责任机制 v0.1）；ORG-005 定性条件版；ORG-006 防线清单版；量化阈值全部 Unknown。
- 链路对齐总表三处责任缺位回填（中文候选名，标候选）。

## Rules affected
ORG-001~006 行更新（逐条，非机械升级）；DEC-2026-014。

## Remaining unknowns
1. 角色进入/退出量化条件；2. 泛化阈值（下一步 E）；3. 教练付费机制（商业批次）；4. 收购交割后的融合结构；5. 范围审查中日期差异待复核方说明。
