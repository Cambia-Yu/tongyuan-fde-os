---
id: RN-20260817-004
type: audit-note
topic: batch2-independent-audit
date: 2026-08-17
batch: Batch 2（Issue #1）
reviewer: ChatGPT
status: 返工后复核
---

# RN-20260817-004｜Batch 2 独立验收记录

## 结论

**部分通过，Issue #1 暂不关闭。**

已通过：
- 三个 Toolkit 均已形成 Purpose / Entry / Actions / Exit / Fields / Hold 的可执行骨架；
- dry run 明确标注为纸面推演，没有把未取得数据或未发生实施写成结果；
- Work Trace 已正确区分“观察行为 / 事后自述”以及“业务规则候选 / 系统摩擦 / 混合待核”；
- E248 已完成来源核验和最小范围回填。

需返工的核心问题如下。

## P0-1｜Human Benchmark 与 Golden Set 被混为同一对象

当前 TOOL-005 的主体实际上是“专家标注 + 分歧仲裁 + 黄金集冻结”方法。这能解决 **Golden Set / Eval Ground Truth**，但还没有充分解决 **Human Benchmark（人工参照系）**。

两者必须在概念上拆开：

- **Human Benchmark**：在同一任务/Case、可比条件下，人实际能做到什么水平。应记录结果质量/成功率、处理时长、必要成本或工作量、升级/求助等与该场景有关的表现，并区分典型水平、合格水平、优秀水平（具体分层按场景决定，不预设万能分位）。它回答“AI 应该和什么人类表现比较”。
- **Golden Set**：什么答案/行为被业务上认为是正确或优秀的权威参照。它回答“怎么判 AI 对不对”。

二者可以继续放在一个文件里以保持最小侵入，但必须分成两个明确 section / output，不能再写成一个同义对象。

一手方法锚点：
- OpenAI《How evals drive the next chapter in AI for businesses》：golden set 是领域专家对“great”判断的权威参考，并强调真实工作流、业务目标和决策点。
  https://openai.com/index/evals-drive-next-chapter-of-ai/
- METR Time Horizon：human baseline 是让真实人类在相同任务、说明和 affordance 下实际完成任务，记录成功与完成时间，再与 Agent 比较；这说明“人工表现基准”与“黄金答案集”不是一回事。
  https://metr.org/time-horizons/

## P0-2｜TOOL-004 把“四维基线”写得过于普遍

“成本/时长/质量/量”可以作为默认检查框架，但证据不足以把四项写成所有项目都必须测齐的普遍规则。

修改要求：
- 把四维改为“默认检查框架/候选维度”；
- 在最前面增加 **Primary Business Outcome / 核心业务指标**：先写清项目真正要改变的业务结果、指标公式、分母/分子、统计单元，再决定需要哪些辅助基线；
- 对季节性、Case mix、样本结构和统计窗口的代表性增加字段或说明；
- 删除“时长不报均值”这类绝对表述。应按分布和业务问题选择均值/中位数/P90等；例如成本核算时均值可能有意义；
- “≥1 个完整业务周期”改为设计建议，不作为跨场景硬阈值，重点是窗口具有代表性并明确局限。

OpenAI 官方 eval 方法强调从业务目的、最重要 outcome、真实工作条件出发，而不是固定四个万能指标：
https://openai.com/index/evals-drive-next-chapter-of-ai/

## P0-3｜TOOL-006 有字段缺口和两条过硬规则

整体方向通过，但需小修：

1. Actions 写了“耗时”，Artifacts/Fields 表里却没有“耗时”字段，需补齐。
2. 增加“动作结果 / 状态变化（state after）”字段，否则只能看到做了什么，看不到动作造成什么结果；这对还原分支逻辑和后续 Agent workflow 很重要。
3. “首日只熟悉不计数据”不能作为硬规则。观察反应性（Hawthorne/reactivity）应作为风险标记；可先做 pilot / familiarization，但是否废弃首日数据应根据观察条件决定。
4. “≥3 笔 Case”只能定义为 **初始 discovery 最低样本**，不能暗示三笔就足以完成稳定 Work Trace。样本是否够应由轨迹是否开始饱和、关键异常是否覆盖决定。

Microsoft 官方 Task Mining 明确将目标描述为理解员工实际桌面操作、识别常见用户交互、错误和不必要动作，可作为 Work Trace 的一手方法侧证：
https://learn.microsoft.com/en-us/power-automate/process-advisor-overview

Anthropic 的 agent eval 方法也把 transcript/trajectory 定义为任务全过程记录，包括工具调用、状态变化和中间结果；可用于补强“动作结果/状态变化”字段：
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

## P1｜Evidence Library 的方法证据需要升级

EV-EXT-004~006 当前主要由二级方法文章、厂商二次说明和若干论文拼接而成，作为草案设计输入可以，但当前“Medium-High / 方法学 FACT”的措辞偏强。

要求：
- 保留现有来源，不必删除；
- 新增上述 OpenAI / Anthropic / METR / Microsoft 一手来源作为 primary anchors；
- 在补齐前，不把“IAA≥0.8”“四维基线”“首日数据作废”等写成 FDE OS 通用规则；
- IAA / κ 只在输出可离散判定、样本和标注设计适用时使用，不能成为所有 Human Benchmark 的必选指标。

## 已通过部分，不要重做

- E248 对 Baseline / 岗位标杆 / Work Trace 的回填方向通过；
- Client Coach、MVP/AB Test、灰度上岗留待对应后续阶段处理是正确的范围控制；
- 网络货运 dry run 正确暴露“全部未测 / 规则原文未取得 / 方案链路不是行为轨迹”，这一点通过；
- DEL-008 / DEL-009 可以继续保持 `Designed（草案，未现场验证）`，不需要降回 Draft，但在返工完成前不升级置信度或成熟状态。

## 返工范围

只允许 B 类最小修改：
- TOOL-004 / TOOL-005 / TOOL-006；
- RN-20260817-002 增补更正说明（如需要）；
- EV-EXT-004~006 补 primary anchors / 调整措辞；
- Master Index 仅在 Rule 文案确实受影响时局部更新。

不要改目录、ID、十阶段链、GATE 编号，也不要新造一套 Toolkit。

返工提交后，在 Issue #1 报告：改了什么、哪些硬规则被降为建议、Human Benchmark 与 Golden Set 如何分开、Evidence 如何升级。随后交回 ChatGPT 二次验收。
