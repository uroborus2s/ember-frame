# 第01集《白册进村》资产 QC 报告

## 结论

规划 QC 通过，等待用户审核后才能生成图片。本轮已补齐图片资产格式合同：每个计划图片资产都有 literal `output_format`，提示词可见文本和 copy-ready 字段已包含对应图片格式要求。

## 已检查

- 必需 director-room 输入、必需 art-room 输出和图片输出目录均存在。
- 所有资产 basename 均不超过 20 字符。
- 所有 canonical output path 不在 `history/`、`v1/`、`versions/` 或 `drafts/` 下。
- `asset-manifest.json`、`asset-index.json`、`art-image-prompts.json` 和 `thread-plan.json` 均包含 `output_format` 或线程级输出格式合同。
- `output_format` 全部包含 `deliverable_kind`、`file_format`、`minimum_resolution`、`background_policy`、`alpha_policy`、`canvas_aspect_ratio`、`required_views`、`composition_layers` 和 `qc_checks`。
- 角色、道具、服装、地点和风格资产卡均明确不是最终视频帧；使用中性背景或资产板布局，不用透明背景替代 cutout。
- 视频参考帧和 shot override 均为 16:9 video_frame，alpha forbidden，并要求前景、中景、背景、机位、光照、天气/时间和动作状态可读。
- 图像提示词继续分离 `production_metadata` 和六段 `model_visible_prompt`；可见提示词不含 asset_id、output path、source refs 或 usage 字段。
- `copy_ready` 已随格式要求重新派生，可直接复制给 ChatGPT 或 Gemini 图像生成。
- `thread-plan.json` 全批次为 `blocked_pending_user_approval`；未创建任何图片文件，未创建 Codex 背景线程。

## 风险

1. 第01集旧文件存在大量历史删除状态，本轮只修复 art-room 标准规划文件，不恢复旧图片和旧 ComfyUI 文件。
2. 白册/暗号类 REDRAW 资产审批通过后仍需要线稿、遮罩或透明图层控制。
3. 全 40 个参考帧和 4 个 shot override 均已预留；建议审批后先生成高优先级帧与可复用状态卡。

## 后续门禁

- 用户批准资产 manifest、设计卡、提示词和线程计划后，才能创建图像生成线程。
- 生成线程必须只写 canonical final files；任何保留的候选图只能进入同级 `history/` 并使用 `.v001`、`.v002` 后缀。
