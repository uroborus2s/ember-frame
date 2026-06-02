# Short Drama Factory 工具设计包

本目录定义 `short-drama-factory` 的产品需求、系统架构、模块边界和 MVP 任务清单。它面向后续独立项目或 Shanforge 纳管开发，不是本教程已有 ComfyUI 课程章节的一部分。

`short-drama-factory` 的目标是把创意、剧本、分镜、提示词、角色/场景一致性资料、ComfyUI 生成、评分筛选和粗剪串成一个可审计、可返工、可进化的短剧生产流水线。

## 推荐阅读顺序

1. [产品需求文档](prd.md)
2. [系统架构](system-architecture.md)
3. [模块边界](module-boundaries.md)
4. [MVP 任务清单](mvp-task-list.md)

## 与现有仓库的关系

| 资产 | 角色 |
| --- | --- |
| `comfyui-ai-video-course` | 提供 Wan2.2 教程、工作流模板、项目记录模板和制作方法论。 |
| `short-drama-factory` | 计划开发的新工具，负责自动化编排短剧制作流程。 |
| `Shanforge` | 推荐作为工程治理底座，负责阶段化文档、skills、memory、workflow、任务闭环和演进机制。 |
| `ComfyUI` | 视频生成执行后端，MVP 阶段不替代它。 |

## 当前决策

- 第一版采用 CLI-first，不先做完整 Web 平台。
- 第一版先做半自动流程，关键阶段保留人工确认 Gate。
- 第一版只实现 ComfyUI/Wan2.2 后端适配，其他视频生成平台留作后续扩展。
- 业务代码不直接写入 Shanforge core。推荐新建独立 `short-drama-factory` 项目，再由 Shanforge 纳管。

