# 第01集《白册进村》资产 QC 报告

## 结论

规划 QC 通过，等待用户审核后才能生成图片。本轮已完成 art-room 合同修复：资产规划、设计卡、提示词、索引和线程计划均包含必需字段。

## 已检查

- 必需 director-room 输入、必需 art-room 输出和图片输出目录均存在。
- 所有资产 basename 均不超过 20 字符。
- 所有 canonical output path 不在 `history/`、`v1/`、`versions/` 或 `drafts/` 下。
- `asset-manifest.json` 与 `thread-plan.json` 已补齐创建顺序、阶段、依赖、反向阻塞、依赖理由和优先级。
- `character-designs.json` 全部角色卡已包含 literal `body_metrics`，覆盖身高、体量、比例、剪影和尺度参考。
- `prop-costume-designs.json` 全部道具/服装卡已包含 literal `physical_dimensions`，覆盖长宽高、尺度参考、重量感和材料厚度。
- `art-image-prompts.json` 与 `prompts/series-art-image-prompts.json` 均补齐 `copy_ready`，且由六段 `model_visible_prompt` 派生。
- 图像提示词均分离 `production_metadata` 和六段 `model_visible_prompt`；可见提示词不含 asset_id、output path、source refs 或 usage 字段。
- 白册、旧驿暗号、血牒、日月纹等精确道具均标记精确控制或后合成策略。
- `thread-plan.json` 全批次为 `blocked_pending_user_approval`；未创建任何图片文件，未创建 Codex 背景线程。

## 风险

1. 第01集旧文件存在大量历史删除状态，本轮只修复 art-room 标准规划文件，不恢复旧图片和旧 ComfyUI 文件。
2. 白册/暗号类 REDRAW 资产审批通过后仍需要线稿、遮罩或透明图层控制。
3. 全 40 个参考帧和 4 个 shot override 均已预留；建议审批后先生成高优先级帧与可复用状态卡。

## 后续门禁

- 用户批准资产 manifest、设计卡、提示词和线程计划后，才能创建图像生成线程。
- 生成线程必须只写 canonical final files；任何保留的候选图只能进入同级 `history/` 并使用 `.v001`、`.v002` 后缀。
