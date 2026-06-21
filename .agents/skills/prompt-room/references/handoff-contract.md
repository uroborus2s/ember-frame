# 提示词交接合同

正式交接位置由项目根目录 `project-management.md` 决定。采用共享分镜文档时，
提示词部不另散输出可见的独立 prompts 目录，而是写入项目办公室指定
的对应分镜文档：

```text
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.md
  ## 图片提示词区
  ## 视频提示词区
```

提示词区至少包含：

```text
image_prompt
video_prompt
negative_prompt
asset_conditioning
control_refs
prompt_qc
handoff_to_video
```

草稿、失败尝试、候选版本、模型测试和 QC 明细进入项目办公室指定的提示词部
隐藏工作区，不得散落到项目根目录。
