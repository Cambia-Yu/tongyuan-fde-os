---
id: OPEN-QUESTIONS
type: open-questions-register
version: 0.1
updated: 2026-08-17
rule: 待裁决问题登记处——按续建工作协议 §五「先标记，再补证，再局部修正」，触发条件满足前不得提交 Change Proposal
---

# 待裁决问题登记（Open Questions）

## OQ-001｜证据等级 L4/L5 与知识状态的语义重叠

- **问题**（协议 §5.1 指定）：IA v0.1 中 L4=我们的推断/重构、L5=设计假设，与知识状态中的 INFERENCE / DESIGN DECISION / HYPOTHESIS 存在语义重叠。同一判断可能同时需要标两套状态，或使用者在「L4 还是 INFERENCE」之间无所适从。
- **当前处置**：不动三层状态制度（属 C 类）。日常实践中按 DEC-2026-007 的既有映射使用：知识状态给主张、L 等级给来源；内部设计文件作为来源时标 L4。
- **触发提交 Change Proposal 的条件**（出现任一即升级）：
  1. 同一判断在文档中同时出现两套状态且互相矛盾；
  2. 两轮以上研究在标注时实际发生困惑并写错（以 RN 记录为准）；
  3. Evidence 与 Claim 的分离在某个具体条目上无法表达。
- **登记日**：2026-08-17｜**来源**：续建工作协议 §5.1

## OQ-002｜DOC-001 的「行业通用定义」范围

- **问题**（协议 §5.2 指定）：DOC-001 目前用 OpenAI 的岗位说明支撑 FDE 定义，但「OpenAI 如何定义自己的 FDE」≠「FDE 类型的通用定义」。通用 Doctrine 只能取 Palantir / OpenAI / Tomoro / 瓴羊 / 其他可靠样本的**公共交集**。
- **当前处置**：不修改 DOC-001。Batch 1（Palantir）与后续批次研究中，每取得一个组织的 FDE 定义即记录其「与 OpenAI 定义的交集/差异」，累积到 ≥3 个组织后做交集分析，届时按 B 类（或如需改写 DOC-001 表述则附 Change Proposal）处理。
- **触发条件**：完成 Palantir + 至少另外两个组织的定义取证后。
- **取证累积**（随批次追加）：
  - 2026-08-17 Palantir（EV-PAL-001/002/003）：FDE=「携带既有产品驻场、现场快速定制解决客户问题」（McGrew）；官方 Delta=「one customer, many capabilities」的 FDSE；FDE 与 PD/产品团队是**双轨并存+回流**结构而非单一岗位定义。**与 OpenAI 定义（发现→生产连续责任，PUB-01）的交集**：驻场/现场、端到端到生产、以业务结果为成功度量；**差异**：Palantir 强调与核心产品团队的泛化回路，OpenAI JD 未强调产品回流。
- **登记日**：2026-08-17｜**来源**：续建工作协议 §5.2
