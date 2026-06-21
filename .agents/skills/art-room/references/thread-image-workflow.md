# Codex 线程图片工作流

父级 Codex 实例负责后台线程调度。负责规划的子 agent 不直接调用线程工具。

## 必需工具

可用时使用 Codex app 线程工具：

- `codex_app.create_thread`
- `codex_app.read_thread`
- `codex_app.send_message_to_thread`

如果这些工具不可用，则写入当前有效的 `<project-office-designated art-thread-results path>`，设置 `status="blocked"`，并保留完整 `<project-office-designated art-thread-plan path>` 供后续运行。任何被替换、重试专属或诊断副本都必须进入 `<project-office-designated hidden art-run path>`。

## 调度规则

1. 读取 `<project-office-designated art-thread-plan path>`，按互不重叠的输出目录分组任务。
2. 条件允许时，每个批次创建一个后台线程，例如 `characters`、`locations`、`props-costumes`、`style`、`reference-frames`、`control-refs`、`blocking` 或 `storyboards`。
3. 如果生产项目位于当前 workspace 内，使用本地环境项目目标。除非用户明确要求，不要为图片文件单独开 worktree。
4. 除非用户明确要求，不要覆盖模型配置。
5. 每个线程提示词必须包含：
   - 项目根目录和 episode ID；
   - batch ID；
   - 精确的正式输出路径；
   - `<project-office-designated art-image-prompts path>` 中的提示词记录；
   - 对应 `production_metadata` 和六段式 `model_visible_prompt`；
   - 可直接提交给图像模型的 `copy_ready` 提示词文本；
   - `output_format` 契约，包括背景策略、alpha 策略、画幅比例、标注策略、控制图角色、必需视图、构图层、最低分辨率、`output_spec_id` 和 QC 检查；
   - 宽景、远景、群像、战场、城市、堡垒、山口或大量重复物体场景所需的 `scene_information_budget`；
   - 连续性引用；
   - 资产准备、清单和线程计划中的制作顺序与依赖；
   - 短文件名规则：basename 去掉扩展名后不超过 20 个字符；
   - 必须使用可用的图片生成能力；
   - 最终确认图只能写入正式输出路径；
   - 透明抠图和精确叠加层必须保留 alpha 意图；视频参考帧和镜头覆盖图必须是带前景、中景、背景层的场景帧；
   - 宽景和远景必须遵守信息预算：只有 3-5 个元素获得高细节，远处主体保持群组剪影或体块，小形体通过氛围和景深简化，避免颗粒化石块、颗粒化人群纹理、噪声微细节、AI 斑点、全画幅超细节和视觉信息过载；
   - 被废弃、拒绝、替换或未选中的图片必须移动到 `<project-office-designated hidden asset version repo for {asset-id}>`，命名为 `YYYYMMDDvNNNN.ext`，不得放进可见版本目录；
   - 返回一个紧凑 JSON manifest，记录最终文件、`version_repo` 和创建的 `discarded_files`。

## 轮询与重试

- 使用 `codex_app.read_thread` 轮询每个线程。
- 若线程报告缺少输入或输出路径不明确，使用 `codex_app.send_message_to_thread` 发送一次修正提示。
- 若线程依赖尚未完成的批次或资产，不要启动；将其标记为 blocked，或等待依赖输出确认。
- 未经用户批准，同一批次不要重试超过一次。
- 在 `<project-office-designated art-thread-results path>` 中保留所有阻塞项。
- 重试诊断、工作线程草稿、被替换的线程计划或结果，必须保存在 `<project-office-designated hidden art-run path>` 或 `<project-office-designated hidden art-run path>`，不要放在 art 根目录。

## 结果记录

写入 `<project-office-designated art-thread-results path>`：

```json
{
  "version": "1",
  "status": "completed",
  "threads": [
    {
      "batch_id": "characters",
      "thread_id": "thread-id",
      "status": "completed",
      "created_files": ["<project-office-designated character master asset path>", "<project-office-designated episode character asset path>"],
      "version_repo": "<project-office-designated hidden asset version repo for c001>",
      "discarded_files": ["<project-office-designated hidden asset version repo>/20260620v0001.png"],
      "warnings": []
    }
  ],
  "blocked_jobs": []
}
```

生成图片应留在以下项目相对目录中：

```text
<project-office-designated character master asset path>
<project-office-designated location master asset path>
<project-office-designated prop master asset path>
<project-office-designated costume master asset path>
<project-office-designated style master asset path>
<project-office-designated episode character asset path>
<project-office-designated episode location asset path>
<project-office-designated episode prop asset path>
<project-office-designated episode costume asset path>
<project-office-designated reference-frame asset path>
<project-office-designated shot-override asset path>
<project-office-designated control-reference asset path>
<project-office-designated blocking/control-asset path>
<project-office-designated storyboard asset path>
<project-office-designated hidden temporary asset path>
```

全剧母卡保留在项目办公室指定的全剧母资产归口。每集状态卡和场景方向资产，包括 `character_episode_state_card`、`prop_episode_state_card`、`location_episode_scene_card`、`location_scene_master_reference`、`location_art_top_view` 和 `location_orientation_grid_9`，保留在项目办公室指定的每集资产归口。

只有最终确认图可以留在正式路径。被废弃、拒绝、替换或未选中的图片必须进入隐藏资产版本库 `<project-office-designated hidden asset version repo for {asset-id}>`，文件名类似 `20260620v0001.png`。不要为生成美术资产创建可见 `history/`、`v1/`、`v2/`、`versions/` 或 `drafts/` 目录。

art 根目录只保存当前有效的线程计划和线程结果文件。不要把 `*-audit*`、`*-review*`、`*-score*`、`*-after-fix*` 或运行专属诊断文件写在 `thread-plan.json` 或 `thread-results.json` 旁边；根据用途放入 `<project-office-designated hidden audit path>`、`<project-office-designated hidden review path>`、`<project-office-designated hidden report path>` 或 `<project-office-designated hidden run path>`。
