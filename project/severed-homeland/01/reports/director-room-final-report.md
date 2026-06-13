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
- `01/control/scene-packages/SC001/run_sc001_comfyui_keyframes.py`
- `01/control/scene-packages/SC001/blockout.blend`
- `01/control/scene-packages/SC001/blockout-export-manifest.json`
- `01/control/scene-packages/SC001/top-view.png`
- `01/control/scene-packages/SC001/camera-map.png`
- `01/control/scene-packages/SC001/shot-guides/r001_camera.png` 到 `r004_camera.png`
- `01/control/scene-packages/SC001/depth/r001_depth.png` 到 `r004_depth.png`
- `01/control/scene-packages/SC001/lineart/r001_lineart.png` 到 `r004_lineart.png`
- `01/control/scene-packages/SC001/space-audit.md`
- `01/control/scene-packages/SC001/masks/.gitkeep`

工作室执行与能力报告：

- `01/production/tool-capability-report.json`
- `01/production/studio-execution-manifest.json`
- `01/production/comfyui-sc001-keyframe-run.json`

美术规划交接包：

- `01/handoff/art-planning/scene-image-brief.md`
- `01/handoff/art-planning/scene-image-resource-index.json`
- `01/handoff/art-planning/scene-reference-prompts.json`
- `01/handoff/art-planning/shot-image-task-list.json`
- `01/prompts/sc001-r001-r004-keyframe-prompts.json`
- `01/assets/director-room/scenes/SC001/material-lock.json`
- `01/assets/director-room/scenes/SC001/master-reference-front.png`
- `01/assets/director-room/scenes/SC001/master-reference-reverse.png`
- `01/assets/director-room/scenes/SC001/key-prop-placement.png`
- `01/assets/director-room/scenes/SC001/blocking-overview.png`
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

`space-audit.md` 结论为 `ready_passed`。顶视图、机位图、四张导演视角图、四张深度图和四张线稿图均来自同一个 Blender 场景，支持四个参考帧属于同一空间。

2026-06-13 人工复核指出首次 `top-view.png` 无法看出场景内容。已返工：`top-view.png` 和 `camera-map.png` 增加只在总览图出现的高对比平面标注层，明确显示黑石墙、城门、门楼、骨钟、年轻军户、薛临墙、P017 旗位、兽族攻击轴线和 R001/R002/R003/R004 机位；正式镜头图、深度图和线稿图仍隐藏这些标注层，避免污染 ComfyUI 控制输入。

2026-06-13 追加升级：SC001 已建立“带统一材质/贴图的场景母版”。`material-lock.json` 固定黑石、石缝、缺口、积雪边、旧木、木纹、铁箍、铆钉、骨钟划痕、P017 旗帜和低细节城市背板的材质 ID。`master-reference-front.png`、`master-reference-reverse.png`、`key-prop-placement.png`、`blocking-overview.png` 与四个分镜控制图同源自升级后的 `blockout.blend`。城墙后方城市只作为低细节远景背板，不是完整城市场景，也不引入第二道墙或第二个门。

## 工具执行结果

Blender：完成。实际使用路径：

```bash
/opt/homebrew/Caskroom/blender/5.1.2/Blender.app/Contents/MacOS/Blender --background --python project/severed-homeland/01/control/scene-packages/SC001/build_sc001_blockout.py
```

已生成并返工确认 `blockout.blend`、`top-view.png`、`camera-map.png`、四张 `shot-guides/*_camera.png`、四张 `depth/*_depth.png`、四张 `lineart/*_lineart.png`、`material-lock.json`、`master-reference-front.png`、`master-reference-reverse.png`、`key-prop-placement.png` 和 `blocking-overview.png`。所有 PNG 为 1280x720。

ComfyUI：服务可用但模型缺失。`http://127.0.0.1:8188/system_stats` 返回 ComfyUI `0.24.0`，MPS 后端可见；但 `CheckpointLoaderSimple` 的 checkpoint 列表为空，`ControlNetLoader` 的 ControlNet 列表为空。本机发现的 `stable-diffusion-webui` SD2.1 权重文件是断链，临时接入 ComfyUI 后执行报错，随后已清理该失效符号链接。`run_sc001_comfyui_keyframes.py` 已写入并执行预检，结果记录在 `01/production/comfyui-sc001-keyframe-run.json`。2026-06-13 后续改用 Codex built-in image generation 对 R003/R004 先生成非 canonical candidate。

关键帧候选图：R003/R004 已生成 candidate，R001/R002 仍未生成。已写入：

- `01/assets/director-room/shots/SC001-SH002/candidates/r003e01.candidate.png`，1672x941，状态：`generated_candidate_pending_user_visual_qc`，版本：`v003_after_user_rejection`
- `01/assets/director-room/shots/SC001-SH003/candidates/r004e01.candidate.png`，1672x940，状态：`generated_candidate_pending_user_visual_qc`，版本：`v002_after_user_rejection`

未写入以下 candidate 输出：

- `01/assets/director-room/shots/SC001-SH001/candidates/r001e01.candidate.png`
- `01/assets/director-room/shots/SC001-SH001/candidates/r002e01.candidate.png`

R003/R004 candidate QC 记录见 `01/reviews/sc001-r003-r004-candidate-qc-2026-06-13.md`。Krita/GIMP：可用但未调用；应在用户/导演视觉 QC 明确指出 mask、脸、道具、旗帜或墙体边缘问题后再做局部修正。

## 评分

| 员工/职责 | 分数 | 通过线 | 返工 | 状态 |
| --- | ---: | ---: | ---: | --- |
| scene-coordinate-agent / scene-bible | 93 | 90 | 0 | 通过 |
| scene-coordinate-agent / layout.yaml | 95 | 90 | 1 | 通过 |
| scene-coordinate-agent / blockout-plan | 90 | 85 | 0 | 通过 |
| studio-tool-execution-agent / Blender script | 94 | 85 | 4 | 已执行通过 |
| studio-tool-execution-agent / Blender execution | 95 | 85 | 4 | 通过 |
| main-coordinator / same-space audit | 92 | 85 | 2 | 通过 |
| scene-image-resource-agent / scene master handoff | 91 | 90 | 2 | 场景母版通过，R003/R004 candidate 待用户 QC |
| studio-tool-execution-agent / ComfyUI run report | 82 | 85 | 1 | 服务可达，模型缺失 |
| imagegenpro / Codex image generation R003-R004 | 86 | 85 | 1 | candidate 已生成，待用户 QC |
| studio-tool-execution-agent / capability report | 94 | 85 | 1 | 通过 |

整体状态：`partial_candidates_ready_r003_r004_comfyui_model_missing_for_r001_r002`。阻塞原因不是 SC001 空间规划或 Blender 控制图缺失，而是 ComfyUI 当前没有可执行 checkpoint；若要把深度图和线稿图接成 ControlNet，还需要安装对应 ControlNet 模型。R003/R004 已有 Codex image generation candidate，可先做人工视觉 QC。

## 用户反馈处理

用户要求的步骤 1、2、3、4、5、6 已完成。用户对顶视图不可读的反馈已处理，已重新导出可读版 `top-view.png` 和 `camera-map.png`。用户要求升级“带统一材质/贴图的场景母版”已处理，已从同一 Blender 场景导出材质锁、正反母版、关键道具关系图和调度母版图。步骤 7 已把控制图交给本地 ComfyUI API 预检并尝试执行，但因模型缺失失败；随后按用户要求用 Codex built-in image generation 生成 R003/R004 candidate。步骤 8 等待用户/导演 QC 指出具体局部问题后再由 Krita/GIMP 执行。

本轮没有覆盖或修改现有 `01/assets/reference-frames/r001e01.png` 到 `r004e01.png`。其中 `r003e01.png`、`r004e01.png` 在工作区原本已有用户改动，本轮只读使用；新图只写入 director-room shot `candidates/`。

## 后续解除阻塞步骤

1. 将一个真实可读的 SD/SDXL checkpoint 放入 `/Users/uroborus/AiProject/ComfyUI/models/checkpoints/`，或配置 ComfyUI 的额外模型路径。
2. 如需使用本轮导出的 `depth/` 和 `lineart/` 作为 ControlNet 条件，将对应 depth/lineart ControlNet 模型放入 `/Users/uroborus/AiProject/ComfyUI/models/controlnet/`。
3. 重新运行：

```bash
python3 project/severed-homeland/01/control/scene-packages/SC001/run_sc001_comfyui_keyframes.py
```

4. 生成或确认剩余 R001/R002 candidate；R003/R004 candidate 先做用户/导演视觉 QC，不得直接覆盖 canonical 参考帧。
5. 若候选图有 mask、脸、道具、旗帜或墙体边缘错误，再用 Krita/GIMP 做局部修正。
