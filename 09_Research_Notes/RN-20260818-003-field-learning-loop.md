---
id: RN-20260818-003
type: research-note
topic: field-learning-loop-change-proposal-and-implementation
date: 2026-08-18
batch: Issue #4（现场学习闭环，C 类获批实施）
---

# RN-20260818-003｜现场学习闭环：提案、校准与获批实施

## Question
「从问题到真实使用并回收证据」如何以最小结构进入 FDE OS（不新增阶段/闸门）？

## Sources
提案 v1→Reviewer 七组校准→v2→用户批准推荐方案（2026-08-18，Issue #4 评论留痕）；锚点核验：GOV.UK 服务手册 ✅、NIST AI 800-4（2026-03-09）✅、OpenAI Cookbook ❌两次 403 待补验（EV-EXT-008）。

## Findings
1. v1 三处语义错误被纠正：GATE-6≠部署认证（改五级状态 U1-U5）；入口≠非 URL（改统一定义）；回流≠自动搬运（改条件路由，06 失败按根因分流 06/05/04/01-03）。
2. 补用户两条构造路线（评测驱动/能力驱动+七查）与第三类开放；TOOL-007 按独立语义设计（部署后人/系统/业务结果变化，非 TOOL-006 变体）。
3. 双读者手册规则固化为写作硬边界+四条失败判据的验收协议。

## Implications（实施产物）
链路对齐总表 §7（状态/入口/路由/构造路线）；TOOL-007 草案；DEL-011；EV-EXT-008；DEC-2026-015。G-11（受控部署方法）与 G-09（泛化阈值）均未关闭。

## Remaining unknowns
方法采用成本（双读者盲测未验）；OpenAI Cookbook 待补验；U4→U5 的量化判据（需真实项目数据）。

## Rules affected
DEL-011（新）；TOOL-007（新）；DEC-2026-015。
