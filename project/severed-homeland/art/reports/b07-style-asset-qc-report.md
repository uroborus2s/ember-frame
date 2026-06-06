# B07_STYLE 资产复核与 F005 更新报告

## 判断结论

- 项目根目录：`project/severed-homeland`
- 批次：`B07_STYLE`
- 结论：需要局部更新，不需要整批重做。
- 必须更新资产：`F005` / `assets/style/f005m.png`
- 保留资产：`F001`、`F002`、`F003`、`F004`、`F006`
- 完成日期：2026-06-06

## 更新原因

`F005` 的合同是 `landscape_composition_style_board`，要求 `3840x2160`、`16:9` 横屏，可作为镜头构图与动作因果参考。旧 canonical 文件为 `2160x3840` 竖版，且视觉上更接近抽象拼板，不能稳定指导横屏镜头的前景、中景、背景分层和动作接触点。

其余五张风格板属于普通 `style_reference` 设定参考板，合同允许 `project_defined` 版式，分辨率超过 `2048x2048`，因此不因横屏合同被强制重做。

## 新版 F005

| ID | 文件 | 路径 | QC |
| --- | --- | --- | --- |
| F005 | `f005m.png` | `assets/style/f005m.png` | passed |

## 合同验证

- 文件格式：PNG。
- 分辨率：`3840x2160`。
- 画幅：`16:9` landscape widescreen。
- 透明策略：RGB，不含 alpha。
- 文件名：`f005m` basename 为 5 字符，符合短文件码规则。
- 版本策略：旧 canonical 文件已归档为 `assets/style/history/f005m.v001.png`；canonical 路径只保留当前确认图。
- 资产类型：横屏构图与动作因果风格板，不是最终视频帧。

## 视觉 QC

- 新版包含门缝火光、手部道具、骨钟震动、巨兽角影、虫蜡针近景、断阶抓手、雪坡逃亡七个横屏缩略镜头。
- 每个缩略镜头都有明确前景、中景、背景，动作接触点和道具首秒可读。
- 底部材质/色彩样片带没有文字标签，保留黑石、雪白、麦金、深河青、虫蜡白、纸灰、干血暗红和旧金赤等可读锚点。
- 未观察到可读文字、UI、水印、HEX、网格编号、现代界面或 ComfyUI 参数。
- 灰褐、雪雾、纸灰和黑石作为材质/天气/条件色存在；暖金、麦色、干血红和深河青仍可读，未形成单一灰褐滤镜。

## 更新记录

- `assets/style/f005m.png`：替换为新版 16:9 横屏构图板。
- `assets/asset-index.json`：F005 状态改为 `landscape_16x9_regenerated_qc_passed`，记录新版 hash 和 history/source 信息。
- `prompts/series-art-image-prompts.json`：同步 F005 prompt metadata、合同状态和 QC 状态。
- `art/series-thread-plan.json`：B07 状态改为 `complete_qc_passed_f005_landscape_regenerated`。
- `art/series-thread-results.json`：记录 F005 history 文件、新版 hash、生成源和 QC 结果。

## 后续

B07_STYLE 当前可继续作为下游服装、角色、地点、道具与 director-room prompt refresh 的风格依赖。后续若重新生成地点主场景卡或镜头参考帧，应优先引用新版 F005 的横屏构图因果规则。
