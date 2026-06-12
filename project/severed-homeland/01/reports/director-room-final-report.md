# 第01集 SC001 导演部门最终报告

## 运行范围

- 项目根：`/Users/uroborus/AiProject/ember-frame/project/severed-homeland`
- 集 ID：`01`
- 场景：`SC001`
- 本轮只处理四个分镜参考帧：`r001e01.png`、`r002e01.png`、`r003e01.png`、`r004e01.png`。

固定输入均存在：`bible/characters.md`、`bible/scenes.md`、`01/script/final-script.md`、`01/reports/continuity-report.md`、`01/reports/script-score.md`、`production/series-video-rules.md`。

本轮使用的可选输入：`bible/continuity.md`、`bible/visual-style.md`、`assets/asset-index.json`。未发现并未使用：`01/assets/source-reference-index.json`、`01/production/render-feedback.json`、`production/tool-profiles.json`、`01/reviews/human-feedback.md`。

## 已创建产物

场景控制包：

- `01/control/scene-packages/SC001/scene-bible.md`
- `01/control/scene-packages/SC001/layout.yaml`
- `01/control/scene-packages/SC001/blockout-plan.md`
- `01/control/scene-packages/SC001/build_sc001_blockout.py`
- `01/control/scene-packages/SC001/blockout-export-manifest.json`
- `01/control/scene-packages/SC001/space-audit.md`
- `01/control/scene-packages/SC001/masks/.gitkeep`

工作室执行与能力报告：

- `01/production/tool-capability-report.json`
- `01/production/studio-execution-manifest.json`

美术规划交接包：

- `01/handoff/art-planning/scene-image-brief.md`
- `01/handoff/art-planning/scene-image-resource-index.json`
- `01/handoff/art-planning/scene-reference-prompts.json`
- `01/handoff/art-planning/shot-image-task-list.json`
- `01/prompts/sc001-r001-r004-keyframe-prompts.json`
- `01/assets/director-room/scenes/SC001/.gitkeep`
- `01/assets/director-room/shots/SC001-SH001/.gitkeep`
- `01/assets/director-room/shots/SC001-SH002/.gitkeep`
- `01/assets/director-room/shots/SC001-SH003/.gitkeep`

评审与日志：

- `01/logs/director-room-agent-calls.jsonl`
- `01/reviews/director-room-review-ledger.json`
- `01/reviews/director-room-scorecard.md`
- `01/reviews/human-feedback-log.jsonl`
- `01/reviews/feedback-revision-plan.json`

## 空间方案

`layout.yaml` 将 SC001 固定为同一个局部攻城空间：

- 场景尺寸：东西向 72 米，墙外北向纵深 90 米，门楼内侧南向纵深 18 米，高度 18 米。
- 坐标原点：城门外侧门槛中心，`x` 沿城墙，`y<0` 为墙外攻城方向，`y>0` 为门楼内侧，`z` 向上。
- 城墙、城门、门楼、骨钟、旗帜、兽族进攻方向、人物站位和四个摄像机均已固定。
- R001/R002 在墙外同轴推进；R003/R004 都在同一门楼/墙顶空间内，使用同一口骨钟和同一女墙关系。

## 工具执行结果

Blender：阻塞。当前环境没有 `blender` 命令，`/Applications/Blender.app/Contents/MacOS/Blender` 不存在，`python3 import bpy` 失败。因此未生成：

- `blockout.blend`
- `top-view.png`
- `camera-map.png`
- `shot-guides/r001_camera.png` 到 `r004_camera.png`
- `depth/r001_depth.png` 到 `r004_depth.png`
- `lineart/r001_lineart.png` 到 `r004_lineart.png`

ComfyUI：待配置。本机没有 `comfyui` 命令，`http://127.0.0.1:8188/system_stats` 无响应；项目也未提供 checkpoint、workflow template 或节点 ID。因此关键帧生成任务已写入任务单，但没有执行。

Krita/GIMP：可用但未调用。Krita 与 GIMP 已安装；由于没有生成关键帧候选图和 mask，本轮没有进行脸、道具或 mask 修正。

## 评分

| 员工/职责 | 分数 | 通过线 | 返工 | 状态 |
| --- | ---: | ---: | ---: | --- |
| scene-coordinate-agent / scene-bible | 93 | 90 | 0 | 通过 |
| scene-coordinate-agent / layout.yaml | 94 | 90 | 0 | 通过 |
| scene-coordinate-agent / blockout-plan | 90 | 85 | 0 | 通过 |
| studio-tool-execution-agent / Blender script | 88 | 85 | 0 | 脚本通过 |
| studio-tool-execution-agent / Blender execution | 45 | 85 | 0 | 阻塞 |
| main-coordinator / same-space audit | 70 | 85 | 0 | 坐标级通过，视觉证据阻塞 |
| scene-image-resource-agent / handoff and tasks | 86 | 90 | 0 | 待配置 |
| studio-tool-execution-agent / capability report | 91 | 85 | 0 | 通过 |

整体状态：`blocked`。阻塞原因不是文本规划缺失，而是本机缺少 Blender 与 ComfyUI 执行环境。

## 用户反馈处理

用户要求的步骤 1、2、3 已完成。步骤 4、5 因 Blender 不可用阻塞；步骤 6 只完成坐标级审核，等待 Blender 导出图后才能完成视觉证据审核；步骤 7 因缺少控制图和 ComfyUI 配置为 `needs_config`；步骤 8 等待生成候选图后再由 Krita/GIMP 执行。

本轮没有覆盖或修改现有 `01/assets/reference-frames/r001e01.png` 到 `r004e01.png`。其中 `r003e01.png`、`r004e01.png` 在工作区原本已有用户改动，本轮只读使用。

## 后续解除阻塞步骤

1. 安装 Blender 或提供 Blender 可执行路径。
2. 执行：

```bash
blender --background --python project/severed-homeland/01/control/scene-packages/SC001/build_sc001_blockout.py
```

3. 检查 `blockout-export-manifest.json` 是否变为 `ready`，并人工查看顶视图、机位图、导演视角图、深度图和线稿图。
4. 配置 ComfyUI checkpoint、workflow template、ControlNet/深度/线稿节点、参考图节点和输出路径。
5. 按 `shot-image-task-list.json` 生成候选关键帧，写入 candidate 目录，不直接覆盖 canonical 参考帧。
6. 若候选图有 mask、脸、道具或旗帜错误，再用 Krita/GIMP 做局部修正。
