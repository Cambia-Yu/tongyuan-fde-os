# 通元问科 FDE 交付操作系统（FDE OS）

**当前状态（2026-08-19）**：候选机制骨架已收口并通过双 Agent 红队审查——四模块、十阶段、十工具齐备；**未经真实项目现场验证（Field-tested=0）**。本仓库为团队可读候选版。

## 三步进入
1. **5 分钟**：先读 [系统总览图](07_System_Map/系统总览图_v0.1.md)
2. **30 分钟**：翻 [团队手册](08_Outputs/团队手册_候选版_v0.1.md) 你负责的那一章（按手册 8 章架构）
3. **现场干活**：直接开 [工具包](05_Field_Toolkit/)（TOOL-001~010，均可填写）

## 常见疑问
见 [FAQ](08_Outputs/FAQ_v0.1.md)（10 个高频问题：FDE 和驻场差在哪、为什么先测基线、哪些动作 AI 永不签、回滚怎么做事）。

## 模块地图
[核心原则](01_Doctrine/核心原则_v0.1.md)｜[组织模型](02_Operating_Model/组织模型_v0.1.md)｜[交付流程](03_Delivery_Playbook/链路对齐总表_v0.1.md)+[能力沉淀](03_Delivery_Playbook/能力沉淀_v0.1.md)｜[商业机制](04_Commercial_Engine/商业模型_v0.1.md)｜[证据库](06_Evidence_Library/FDE_Evidence_Library_v0.1.md)｜[决策记录](10_Decision_Log/Decision_Log.md)｜[研究记录](09_Research_Notes/)

## 治理
双 Agent 协作（Builder/Reviewer 闸门+Issue 驱动，见 [协作入口](00_Master_Index/AGENT_COORDINATION.md)）；[续建协议](00_Master_Index/续建工作协议_v1.0.md)约束一切变更（三轮验证/最小侵入/中文优先/稳定 ID）。

## 本地查看器
```bash
python3 server.py   # http://127.0.0.1:8795
```
