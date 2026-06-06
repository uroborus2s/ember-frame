# Director Room 横屏设定审查

- 项目：`project/severed-homeland`
- 日期：2026-06-06
- 目标：将全剧视频交付从旧版移动端画幅合同修复为 `16:9` 横屏宽屏合同，适配宽屏电脑播放，同时保留手机横屏/自适应播放兼容性。

## 修复范围

本轮按 director-room 边界修复生产与镜头设定，不改剧情 canon：

- `production/series-video-rules.md`
- `project.json`
- `01` 至 `12` 集的 `script/` 格式标签、`director/camera-plan.md`、`shots/shot-list.json`
- `storyboard/storyboard-plan.md`
- `production/generation-plan.json`、`production/video-production-plan.md`
- `prompts/shot-prompts-draft.json`
- `prompts/comfyui-style-preset.json`
- `prompts/comfyui-shot-prompts.json`
- `prompts/comfyui-workflow-plan.json`
- `prompts/comfyui-prompt-brief.md`

## 横屏合同

- 交付画幅：`16:9`
- 默认主帧：横屏宽屏剧 / landscape widescreen drama
- 推荐最低视频参考帧与图像资产目标：`3840x2160`
- 运动规则、真实重心、角色连续性、道具首秒可读和对白交给字幕/音频的规则保持不变。

## 审查结果

- 所有 active 生产文件中的画幅字段已改为 `aspect_ratio: "16:9"`。
- 所有 active 分镜/镜头提示中的旧版移动端构图口径已改为横屏宽屏口径。
- `comfyui-style-preset` 的全局风格前缀已改为 `16:9 landscape widescreen drama`。
- 剧情 bible 没有被重写；`bible/scenes.md` 与 `bible/visual-style.md` 继续作为故事侧场景和视觉 canon。

## 验证

- active 文件关键词扫描已排除历史线程、history、runs、memory、migration、legacy 后执行。
- active 文件未发现会被生产流程解释为旧版移动端画幅的交付设定。
- 148 个 active JSON 文件解析通过。

## 注意

历史 `thread-results` 和 `runs/history` 记录没有改写；其中保留旧版生成事实，不作为当前横屏交付依据。
