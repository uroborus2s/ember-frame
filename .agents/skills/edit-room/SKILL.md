---
name: edit-room
description: 剪辑部。用于根据通过 QC 的视频镜头、配音、音乐、字幕和导演节奏，规划或执行剪辑、转场、节奏、声画同步、字幕、EDL、预览片和剪辑 QC。用户提到剪辑、转场、节奏、字幕、声画同步、成片预览、EDL、画面转场不自然时使用。
---

# 剪辑部

剪辑部负责把已通过 QC 的镜头、配音、音乐和字幕组装成可审片的版本。它不能用剪辑掩盖故事、剧本、角色或视频源头错误。

## 输入

实际输入路径由项目根目录 `project-management.md` 和项目办公室交接契约决定。凡涉及预览、成片、字幕、清晰度或交付格式，必须同时读取根目录 `project-spec.md`。逻辑输入必须覆盖：通过 QC 的视频镜头、配音、音乐、字幕文本、剧本、导演节奏和导演部分镜目录中的已认可资产。

## 输出

实际输出路径、隐藏版本库和最终归口由项目根目录 `project-management.md` 指定。剪辑部不在 skill 中定义项目目录。

剪辑部可以产出以下类型的专业内容：

```text
剪辑计划
EDL
字幕稿
预览 manifest
剪辑 QC
分镜或成片剪辑版本历史
```

服务具体分镜的剪辑交接文件，最终被导演认可后只能回到项目办公室指定的导演部对应分镜目录，通常放入该分镜目录下的 `assets/edit/`，并由对应 `{shot-id}.md` 引用。整集或成片交付版本的最终归口由项目办公室在交付契约中另行指定。

## 运行方式

可创建：

```text
edit-director-agent
rhythm-agent
subtitle-agent
sound-sync-agent
edit-qc-agent
```

循环：剪辑计划 -> 粗剪 -> 声画同步 -> 字幕 -> QC -> 返工 -> 交付。

不得自动修改 `.agents/skills/edit-room/`。

参考：`references/workflow.md`、`references/quality-gate.md`、`references/handoff-contract.md`。
