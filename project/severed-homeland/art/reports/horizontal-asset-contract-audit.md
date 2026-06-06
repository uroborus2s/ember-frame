# Art Room 横屏资产合同审查

- 项目：`project/severed-homeland`
- 日期：2026-06-06
- 目标：将美术资产与图像提示从旧版移动端画幅合同修复为 `16:9` 横屏宽屏合同，并明确旧版 PNG 的处理方式。

## 修复范围

本轮按 art-room 边界修复资产规划、图像提示和线程派发合同：

- `art/series-asset-plan.md`
- `art/series-thread-plan.json`
- `assets/asset-index.json`
- `prompts/series-art-image-prompts.json`
- `01/art/*`、`02/art/*` 中已有分集资产合同
- 全局 art reports/reviews/audits 中仍作为当前 QC 口径使用的横屏合同描述

## 横屏输出合同

- `output_format.canvas_aspect_ratio`: `16:9`
- `output_format.minimum_resolution`: `3840x2160`
- `canvas_aspect_ratio_notes`: `16:9 landscape widescreen`
- 角色、道具、服装、风格板仍是 master card / board，不当作最终视频帧。
- 视频参考帧和 shot override 必须有前景、中景、背景分层，不能使用孤立透明卡片代替 I2V/FLF2V 场景帧。

## 实际 PNG 审查

当前 canonical PNG 文件仍是旧版移动端画幅或低于横屏目标：

- 旧版移动端画幅/低于横屏目标：52
- 已满足横屏目标并待 QC：0
- 尚未生成或无 PNG：20

因此，本轮没有把现有 PNG 判定为横屏通过。`assets/asset-index.json` 与 `prompts/series-art-image-prompts.json` 已加入 `landscape_contract_status`，将旧图标记为：

`legacy_portrait_or_subtarget_not_landscape_ready`

后续必须重新生成并通过横屏 QC 后，才能把 canonical 图作为横屏生产资产使用。

## 批次状态

`art/series-thread-plan.json` 已把旧完成批次改为横屏重生状态：

- B00/B07/B06/B01/B02：`needs_landscape_regeneration_qc`
- B03：`needs_landscape_regeneration_qc`
- B04/B05：`needs_landscape_generation`

旧线程 ID、旧 final files 和旧 QC 结果保留在 `legacy_*` 字段中，只作历史参考。

## 验证

- active 文件关键词扫描未发现旧版移动端画幅交付设定。
- 145 个 active JSON 文件解析通过。
- 未修改 PNG 二进制文件；工作区中已有 PNG 改动保留为用户/既有改动。

## Handoff

建议下一步按 art-room 顺序重新生成横屏资产：

1. B00 三势力徽章旗帜根资产
2. B07 风格板，尤其 F005 横屏构图与动作因果板
3. B06 服装系统
4. B01/B02 角色与族群模板
5. B03/B04 地点主场景卡
6. B05 道具与精确符号

资产通过横屏 QC 后，再回到 director-room 刷新 post-asset ComfyUI prompt pack。
