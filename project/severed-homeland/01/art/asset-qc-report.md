# 第01集《白册进村》资产 QC 报告

## 结论

规划 QC 通过，等待用户审核后才能生成图片。

## 已检查

- 所有资产 basename 均不超过 20 字符。
- 所有 canonical output path 不在 `history/`、`v1/`、`versions/` 或 `drafts/` 下。
- 图像提示词均分离 `production_metadata` 和六段 `model_visible_prompt`。
- 白册、旧驿暗号、血牒、日月纹等精确道具均标记精确控制或后合成策略。
- `thread-plan.json` 全批次为 `blocked_pending_user_approval`。
- 未创建任何图片文件，未创建 Codex 背景线程。

## 风险

1. 第01集旧文件存在大量历史删除状态，本轮只重建 art-room 标准规划文件，不恢复旧图片和旧 ComfyUI 文件。
2. 白册/暗号类 REDRAW 资产审批通过后仍需要线稿、遮罩或透明图层控制。
3. 全 35 镜头参考帧全部预留会带来生成量，建议审批后先生成高优先级帧与可复用状态卡。
