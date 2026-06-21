# 视频到剪辑交接

视频生成部只把通过 QC 且符合项目办公室交接条件的素材交给剪辑部。过程、失败、备选和返工前版本只进入项目办公室指定的隐藏版本库；不得在明面目录创建 `raw/`、`rejected/` 或 `approved/` 作为正式结构。

## 交接位置

实际交接位置由项目根目录 `project-management.md` 和 `.project/` 契约决定。若项目采用导演部分镜目录：

```text
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.mp4
director-room/{season-id}/{episode-id}/{shot-group-id}/{shot-id}/{shot-id}.md
```

`{shot-id}.md` 的视频生成区记录最终视频路径、QC 状态、隐藏版本库追溯路径、已知风险和剪辑建议。隐藏版本库只用于追溯，不是剪辑部的正式素材入口。

## render manifest

每个镜头必须记录：

```text
shot_id
scene_id
storyboard_id
source_frame
last_frame
audio_ref
dialogue_id
video_path
version_repo_ref
generation_mode
technique_profile
tool_name
tool_version_or_model_ref
fps
duration
resolution
segment_index
handles
recommended_in
recommended_out
qc_status
known_risks
```

## shot QC

每个镜头必须记录：

```text
score
threshold
director_intent_status
character_identity_status
scene_space_status
prop_state_status
motion_status
camera_status
image_quality_status
lipsync_status
editability_status
manifest_status
failure_reason
approved_by_video_room
needs_director_review
needs_upstream_revision
```

## failure ledger

失败素材必须记录到隐藏版本库 manifest 或项目办公室指定返工记录：

```text
shot_id
attempt
version_path
failure_type
failure_description
root_cause
retry_strategy
upstream_department_if_any
keep_for_learning
```

常见 `failure_type`：

```text
character_drift
scene_drift
prop_state_error
motion_weight_error
camera_mismatch
lipsync_mismatch
random_text_or_ui
low_quality_source
temporal_flicker
not_editable
tool_limit
missing_input
```

## 剪辑交接说明

剪辑部需要能一眼读懂：

```text
1. 本批可剪素材概览
2. 镜头顺序和推荐剪辑用法
3. 每个镜头推荐入点/出点/头尾余量
4. 对白、口型和音频引用
5. 需要保留的导演节奏点
6. 可用 alternate take 的隐藏版本库引用
7. known risks
8. 禁止剪辑硬救的问题
9. 需要导演回看的镜头
10. 失败摘要和返工入口
```

## 交接硬规则

- 剪辑部正式读取的是导演部分镜目录中的最终视频或项目办公室指定交接入口，不读取视频部过程目录。
- 交给剪辑部的视频必须有稳定短文件名，语义说明写入 manifest 或 `{shot-id}.md`，不靠长文件名解释。
- 口型镜头必须带 `dialogue_id`、`audio_ref`、起止时间和 `lipsync_status`。
- 如果视频部知道某镜头有风险，必须写入 `known_risks`，不能让剪辑部在时间线上才发现。
- 剪辑部反馈“不可剪”时，优先回到隐藏版本库 manifest、镜头 QC 和项目办公室返工入口，不得只导出一个新格式文件糊弄。
