# 第01集 SC001 导演部门评分表

| 员工/职责 | 产物 | 分数 | 通过线 | 返工次数 | 状态 |
| --- | --- | ---: | ---: | ---: | --- |
| scene-coordinate-agent | `scene-bible.md` | 93 | 90 | 0 | 通过 |
| scene-coordinate-agent | `layout.yaml` | 95 | 90 | 1 | 通过 |
| scene-coordinate-agent | `blockout-plan.md` | 90 | 85 | 0 | 通过 |
| studio-tool-execution-agent | `build_sc001_blockout.py` | 92 | 85 | 3 | 已执行通过 |
| studio-tool-execution-agent | Blender `.blend` 与 PNG 导出 | 94 | 85 | 3 | 通过 |
| main-coordinator | `space-audit.md` | 90 | 85 | 1 | 同空间审核通过 |
| scene-image-resource-agent | 美术规划交接包与逐帧任务单 | 87 | 90 | 1 | ComfyUI 模型缺失 |
| studio-tool-execution-agent | `tool-capability-report.json` | 94 | 85 | 1 | 通过 |
| studio-tool-execution-agent | `comfyui-sc001-keyframe-run.json` | 82 | 85 | 1 | 服务可达，模型缺失 |
| main-coordinator | `director-room-final-report.md` | 90 | 85 | 1 | 部分完成报告通过 |

## 总结

整体状态：`blocked_comfyui_model_missing`

SC001 场景圣经、权威 layout、Blender 脚本、低模场景、顶视图、机位图、四张导演视角图、四张深度图、四张线稿图和同空间审核均已完成。ComfyUI Web/API 已启动并通过 `system_stats` 检查，但 checkpoint 与 ControlNet 列表为空，且本机找到的 Stable Diffusion v2.1 文件是断链，因此四张关键帧候选图未生成。Krita/GIMP 等待候选图或 mask 出现后再进入修正流程。
