---
name: delivery-room
description: 成片交付部。用于汇总剪辑预览、导演终审、交付规格、最终导出、成片 QC、版本归档和用户验收。用户提到成片、最终视频、交付、导演终审、导出规格、最终 QC、01.mp4、02.mp4 时使用。
---

# 成片交付部

成片交付部负责最终交付，不负责补故事、重写剧本、重做资产或生成镜头。未通过上游 QC 的内容不得进入最终成片。

## 输入

实际输入路径由项目根目录 `project-management.md`、`project-spec.md` 和项目办公室交接契约决定。逻辑输入必须覆盖：导演认可的剪辑预览、剪辑 QC、导演终审意见、项目总规格、交付规格和最终批准门。

## 输出

实际输出路径、版本归档和最终交付归口由项目根目录 `project-management.md` 指定；最终图片、视频、音频、字幕和格式要求由 `project-spec.md` 指定。成片交付部不在 skill 中定义项目目录。

成片交付部可以产出以下类型的专业内容：

```text
交付规格
最终 QC
发布 manifest
交付版本历史
用户验收记录
```

最终成片文件名、位置、归档方式和用户验收入口，由项目办公室在交付契约中指定。

## 运行方式

可创建：

```text
delivery-producer-agent
technical-qc-agent
director-approval-agent
archive-agent
```

循环：检查上游状态 -> 技术 QC -> 导演终审 -> 用户验收 -> 归档。

不得自动修改 `.agents/skills/delivery-room/`。

参考：`references/workflow.md`、`references/quality-gate.md`、`references/handoff-contract.md`。
