# 通元问科 FDE 交付操作系统（Tongyuan FDE Operating System）

这是通元问科用于真实企业 AI 项目的内部交付操作系统母体。仓库 `main` 是当前 canonical baseline，但**任何单个文档都不能单独代表最新状态**。

## 从这里开始

如果你是新接管的 Agent / Codex，请按顺序读取：

1. `00_Master_Index/LOCAL_CODEX_HANDOFF_PACKAGE_v1.0.md` —— 项目目标、已知/未知、方法边界、长期路线；
2. `00_Master_Index/AGENT_COORDINATION.md` —— 当前批次、双 Agent 分工、冲突裁决和批次切换规则；
3. GitHub 当前 open Issue —— 当前真正要执行和验收的任务；
4. 本批涉及的 Decision / Evidence / Research Note / Toolkit；
5. `00_Master_Index/FDE_OS_Master_Index_v0.1.md` —— Rule / Toolkit 总索引。

**README 只做导航，不作为实时状态权威来源。**

## 当前状态（2026-08-17）

- 第一轮骨架、证据体系和治理规则已经建立；
- Palantir Echo / Delta / Core 第一批取证已完成，部分机制已有 L1/L2 支撑；
- 瓴羊 E248 转写已取得并核验，`EV-LY-001` 已回填；
- Batch 2 已产出 Baseline / Human Benchmark / Work Trace 三个 Toolkit 草案和纸面 dry run；
- Batch 2 当前为**部分通过、返工后复核**，详见 Issue #1 与 `RN-20260817-004-chatgpt-batch2-audit.md`；
- 目前仍没有任何核心规则或 Toolkit 可因为文档完成而自动视为 `Field-tested / Validated`，成熟度必须由真实现场证据升级。

## 当前最重要的方法边界

- Baseline：AI 介入前真实业务表现的比较起点；
- Human Benchmark：相同任务与条件下，人实际能做到什么水平；
- Golden Set：什么答案/行为可作为 Eval 的权威参照；
- Work Trace：真实人员处理真实 Case 时的行为、判断、状态变化与分支轨迹；
- Work Trace 不等于 SOP，也不等于把所有人类动作自动化。

## 系统模块

- `01_Doctrine`：FDE 定义与边界
- `02_Operating_Model`：Echo / Delta / Core / Client Coach 等组织设计
- `03_Delivery_Playbook`：阶段、Gate、Entry / Exit / Hold
- `04_Commercial_Engine`：Deployment Leverage、Value Unit、Pricing、Land & Expand
- `05_Field_Toolkit`：现场直接使用的作业工具
- `06_Evidence_Library`：Rule 的证据底座
- `07_System_Map`：系统总览
- `08_Outputs`：官网、PPT、培训等输出层
- `09_Research_Notes`：研究、反例、审核记录
- `10_Decision_Log`：正式设计决定与历史状态

## 证据纪律

1. 公司个案事实不能直接写成行业规律；
2. FACT / OBSERVATION / INFERENCE / DESIGN DECISION / HYPOTHESIS 必须区分；
3. 没有 baseline 不写 ROI；
4. Demo / PoC / 纸面推演不等于生产结果；
5. 结构性改动先走 Change Proposal；
6. 历史 Decision 只增不改，后续变化通过新 Decision / 更正记录处理。

## 双 Agent 协作

当前默认角色：

- Builder / Integrator：负责 canonical 文件修改与整合；
- Independent Reviewer / Research Auditor：负责独立取证、反例、证据等级和现场可执行性审核。

具体权限与批次切换以 `00_Master_Index/AGENT_COORDINATION.md` 为准。

## 公开仓库注意事项

本仓库当前为 public。不要继续提交客户敏感原始资料、企业内部数据或新的完整第三方版权材料。公开仓库优先保存 source metadata、必要短摘录、证据定位、Research Note 和可公开方法资产；需要完整原始材料时应优先放在受控的私有资料层。

## 本地查看器

```bash
python3 server.py
```

默认打开 `http://127.0.0.1:8795`，用于只读浏览 Markdown 文档树和全文搜索。
