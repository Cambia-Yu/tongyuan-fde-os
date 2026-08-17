---
id: RN-20260818-004
type: research-note
topic: batch5-eval-and-controlled-deployment
date: 2026-08-18
batch: Batch 5（Issue #5，G-11+G-12 合批）
---

# RN-20260818-004｜Batch 5：评测方法与受控部署

## Question
阶段 06/07 的方法空白如何以两个独立交付包填补（DEL-012 评测/GATE-5；DEL-013 受控部署/GATE-6）？

## Sources
范围审查八条边界（Issue #5 评论 1）；补证两锚点均本地全文核验：Anthropic《Demystifying evals for AI agents》（EV-ANT-003 ✅）、NIST AI RMF Manage 4.1-4.3（EV-NIST-002 ✅）。**更正**：本方 Issue 起草时误把「影子实践」归于 EV-PAL-002——该条目无此主张（边界 6 指出），已撤；Palantir 影子部署证据待原始材料再登记。

## Findings
1. 评测四对象分立（参照系/黄金集为输入，能力集/回归集为产出+毕业机制）；评分器三型与人工校准；瑞士奶酪（离线分数不替代真实使用）——全部有 L1 锚点原文支撑。
2. 四种运行方式重定义为**可选控制模式非升级阶梯**（按风险选式、允许停级/跳过/降级）；回滚十要素以 NIST Manage 4.1-4.3 为控制类别清单；瓴羊渐进节奏降为单组织样本参照。
3. TOOL-005B「只增例不改旧答案」按边界 3 校准为「版本化纠错机制」。

## Implications
DEL-012/013、TOOL-008/009、链路表 06/07 卡片更新；G-11/G-12 状态待 Reviewer 验收后同步 Gap Map。

## Remaining unknowns
回滚机制的跨组织实证（现仅 NIST 控制类别+设计推导）；四模式在通元真实项目的适配（零样本）；U4→U5 判据。

## Rules affected
DEL-012、DEL-013（新）；TOOL-008/009（新）；TOOL-005B（校准）。
