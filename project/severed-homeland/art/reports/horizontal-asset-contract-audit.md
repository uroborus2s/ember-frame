# Art Room 资产规格冲突审查

- 项目：`project/severed-homeland`
- 日期：2026-06-06
- 目标：修复“一刀切横屏”导致的资产规格冲突，明确哪些资产必须横屏，哪些设定图不应因横屏视频合同而重做。

## 修复范围

本轮按 art-room 边界修复资产规划、图像提示和线程派发合同：

- `art/series-asset-plan.md`
- `art/series-thread-plan.json`
- `assets/asset-index.json`
- `prompts/series-art-image-prompts.json`
- `01/art/*`、`02/art/*` 中已有分集资产合同
- 全局 art reports/reviews/audits 中仍作为当前 QC 口径使用的横屏合同描述

## 类型化输出合同

- 场景/地点主卡、shot override、F005 构图动作板：`16:9`，`3840x2160`。
- 分集 reference frame：`16:9`，`4096x2304`。
- 角色、服装、普通道具、徽章/旗帜、普通风格板：设定参考卡，`project_defined`，最低 `2048x2048`，允许竖幅、方图、多视图设定板或精确线控派生层。
- 角色、道具、服装、徽章和普通风格板不得被当作最终视频帧，也不得因视频横屏合同强制重做。
- 视频参考帧和 shot override 必须有前景、中景、背景分层，不能使用孤立透明卡片代替 I2V/FLF2V 场景帧。

## 实际 PNG 审查

当前 canonical PNG 按资产类型判定：

- master reference 现有且无需因横屏重做：38
- master reference 现有但低于最低分辨率，需普通 QC 决定是否重做：2
- 场景/F005 现有但非横屏，需横屏重新生成或 QC：12
- 尚未生成或无 PNG：20

因此，本轮不再把角色、服装、普通道具、徽章和普通风格板标记为“必须横屏重生”。这些图可继续作为身份、材质、比例、符号和线控参考；只有场景/视频画面类资产需要横屏重生。

## 批次状态

`art/series-thread-plan.json` 已按资产类型修复批次状态：

- B00：`reference_qc_passed_no_landscape_regeneration_required`
- B07：`mixed_style_reference_review_f005_landscape_composition_board_needed`
- B06/B01/B02：`needs_master_reference_qc_or_regeneration_not_landscape`
- B03：`needs_landscape_regeneration_qc`
- B04：`needs_landscape_generation`
- B05：`needs_master_reference_generation_not_landscape`

旧线程 ID、旧 final files 和旧 QC 结果保留在 `legacy_*` 字段中，只作历史参考。

## 验证

- active 文件关键词扫描未发现角色、服装、道具 master 设定图被强制横屏重生的合同冲突，也未发现镜头/参考帧仍使用旧画幅目标词。
- 148 个 active JSON 文件解析通过。
- 未修改 PNG 二进制文件；工作区中已有 PNG 改动保留为用户/既有改动。

## Handoff

建议下一步按 art-room 顺序处理资产：

1. 保留 B00 三势力徽章旗帜根资产作为精确符号参考。
2. 只对 B07 中 F005 横屏构图与动作因果板做横屏重生或 QC。
3. B06/B01/B02 走设定参考卡 QC，不因横屏强制重做。
4. B03/B04 地点主场景卡走 `16:9`、`3840x2160` 横屏生成或重生。
5. B05 道具与精确符号走设定参考卡生成，精确符号另建线控/透明派生层。

资产通过横屏 QC 后，再回到 director-room 刷新 post-asset ComfyUI prompt pack。
