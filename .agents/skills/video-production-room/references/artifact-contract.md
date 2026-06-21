# 视频生成部 Artifact 契约

每个视频生产子任务返回一个结构化 envelope。父级 Codex 协调者负责检查、评分、返工、写入项目办公室指定位置和交接。员工产物默认是候选执行稿或执行记录，不得自行宣布最终完成。

## Envelope

```json
{
  "status": "success",
  "summary": "一句话说明本员工提交了哪个候选执行稿或执行结果。",
  "shot_refs": ["SC001-SH001"],
  "artifacts": [
    {
      "path": "<project-office-designated-render-manifest-or-shot-document>",
      "kind": "json-or-markdown",
      "content": "{ \"shots\": [] }"
    }
  ],
  "next_actions": ["video-qc-agent"],
  "warnings": [],
  "handoff": {
    "main_output": "<project-office-designated-output>",
    "assumptions": [],
    "quality_notes": [],
    "blocked_questions": []
  }
}
```

## 状态值

- `success`: 可进入下一步或父级 QC，但不代表最终通过。
- `warning`: 可评审，但存在必须保留的风险。
- `blocked`: 缺少导演签署、通过 QC 的首帧、控制证据、音频、工具能力、`project-spec.md` 或项目契约，无法继续。
- `needs_upstream_revision`: 问题属于导演、美术、提示词、配音或剪辑输入，视频部不能自行修复。

## Artifact 规则

- 使用项目相对路径，不在员工输出中写绝对路径。
- 实际输出路径、隐藏版本库和最终归口由项目根目录 `project-management.md` 与 `.project/` 契约决定。
- 视频规格、清晰度、帧率、格式和预览/最终版边界由 `project-spec.md` 决定。
- Markdown 用于生成计划、QC 报告、交接说明和失败复盘。
- JSON 用于工具能力报告、render manifest、shot QC、failure ledger 和可机读索引。
- 过程材料、试错参数、废弃素材和重跑记录进入项目办公室指定隐藏版本库，不得散落在项目根目录。
- 子任务不得修改导演签署区、美术资产区、提示词区、配音区、音乐区或剪辑区。
- 不得把临时 proxy、低模预演、带标注控制图或 blocking 视频伪装成最终分镜视频。

## 必需记录字段

每个镜头至少记录：

```text
shot_id
source_frame
last_frame
audio_ref
video_path
version_repo_ref
generation_mode
technique_profile
tool_name
tool_version_or_model_ref
input_refs
fps
duration
resolution
segment_index
qc_status
failure_reason
known_risks
next_action
```

## 评审记录

```json
{
  "shot_id": "SC001-SH001",
  "attempt": 3,
  "status": "needs_revision",
  "score": 82,
  "threshold": 90,
  "checks": [
    {"name": "director_intent", "status": "passed"},
    {"name": "character_identity", "status": "failed"},
    {"name": "editability", "status": "passed"}
  ],
  "failure_reason": [
    "第 2 秒后角色脸型变窄，发型轮廓偏离角色状态卡。"
  ],
  "revision_request": [
    "缩短为 3 秒 I2V，使用通过 QC 的首帧和角色状态卡，降低镜头运动强度。"
  ]
}
```

只有 `qc_status="passed_qc"` 且父级确认剪辑可用、导演或项目办公室质量门允许时，素材才允许进入导演部分镜目录成为 `{shot-id}.mp4`。否则只能留在隐藏版本库。
