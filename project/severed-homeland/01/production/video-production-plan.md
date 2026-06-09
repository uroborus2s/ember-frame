# 第01集《白册进村》视频生产计划 / Video Production Plan

## 状态 / Status

中文：当前已补齐 `SC001` 后资产 ComfyUI 交付包，并按最新方案把 `SC001-SH001` 改为墙外正向偏斜前推到第一次撞门震钟，放弃升到墙头后转向的复杂运镜。`SC001-SH002` 废弃年轻军户扶钟构图，改为被撞门余震晃倒、半倒墙边、武器脱手、旁边骨钟横摆。其余场次仍保持 director-room 预资产分镜包状态。`SC001-SH001` 到 `SC001-SH003` 可在重生/确认 `r002e01.png`、`r003e01.png` 并补齐模型与 workflow 配置后小批量试渲。

English: The post-asset ComfyUI delivery package is now complete for `SC001`, and `SC001-SH001` has been updated to the latest exterior front-biased push into the first gate-impact bell shock, dropping the complex wall-top turn. `SC001-SH002` abandons the young soldier bracing-the-bell composition and changes to aftershock collapse beside the wall, dropped weapon, and the same bell swinging beside him. The remaining scenes are still in director-room pre-asset shot-package state. `SC001-SH001` through `SC001-SH003` can enter a small test batch after `r002e01.png` and `r003e01.png` are regenerated/rechecked and model/workflow configuration is supplied.

## 生产规格 / Production Specs

- 画幅 / Aspect Ratio: `16:9`
- 帧率 / FPS: `24`
- 目标时长 / Target Duration: `270s`
- 规划时长 / Planned Duration: `271.2s`
- 风格 / Style: 超写实、电影级质感、真实触感古代材质、低魔东方史诗、真实重心和真实速度。

## 产物索引 / Artifact Index

- `01/director/director-brief.md`
- `01/director/camera-plan.md`
- `01/shots/scene-breakdown.json`
- `01/shots/shot-list.json`
- `01/storyboard/storyboard-plan.md`
- `01/continuity/visual-continuity-bible.json`
- `01/production/generation-plan.json`
- `01/prompts/shot-prompts-draft.json`
- `01/prompts/comfyui-prompt-brief.md`
- `01/prompts/comfyui-style-preset.json`
- `01/prompts/comfyui-asset-prompt-pack.json`
- `01/prompts/comfyui-shot-prompts.json`
- `01/prompts/comfyui-workflow-plan.json`
- `01/prompts/comfyui-tuning-log.json`
- `01/reports/comfyui-prompt-qc.md`
- `01/production/video-production-plan.md`

## 生产顺序 / Recommended Render Order

1. SC001 后资产小批量试渲：`SC001-SH001`, `SC001-SH002`, `SC001-SH003`
2. 残阳坳主空间锁定：`SC004-SH001`, `SC006-SH001`, `SC006-SH008`
3. 核心角色参考：`SC004-SH003`, `SC004-SH005`, `SC004-SH006`, `SC006-SH005`
4. 关键道具插入：`SC004-SH007`, `SC004-SH008`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`, `SC006-SH010`
5. 药屋暗格段：`SC005-SH001` 到 `SC005-SH005`
6. 残阳坳对白压力段：`SC004-SH002` 到 `SC004-SH009`, `SC006-SH002` 到 `SC006-SH009`
7. 其余序幕世界压力段：`SC002-SH001` 到 `SC003-SH004`

## SC001 ComfyUI Handoff / SC001 ComfyUI 交付

| Shot | Method | Reference Inputs | Output |
| --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（墙外正向偏斜攻城首帧）, `01/assets/reference-frames/r002e01.png`（同一墙外方向第一次撞门震钟尾帧）, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png`, `01/assets/characters/c024ae01.png`（低权重墙头守军剪影连续性） | `01/renders/raw/sc001-sh001.mp4` |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png`（旧扶钟构图已废弃，必须重生为半倒墙边、武器脱手、骨钟横摆）, `01/assets/characters/c024ae01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh002.mp4` |
| `SC001-SH003` | `I2V` | `01/assets/reference-frames/r004e01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh003.mp4` |

中文：`SC001-SH001` 改为墙外正向偏斜攻城前推：首帧从墙外攻城方向低机位看兽潮、攻城车或破门猛犸压向同一面黑石城门，尾帧保持同一墙外方向，第一次重撞城门，雪雾冲画面，墙头同一钟架和同一口骨钟横摆。R001-R004 硬锁为同一面城墙、同一个城门、同一个钟架、同一口钟；城外只允许由已加载 `C020/C021/E01_C020` 参考图节点约束的兽族士兵和伴生兽朝墙攻来。禁止越过墙脊看城内或另一侧，禁止读成城墙两边同时被攻击。前推期间读时代事件旁白“肃明历1226年，北境十三部落联盟大举入寇。”。`SC001-SH002` 新版首帧必须是年轻军户被震倒半倒墙边、武器脱手、骨钟横摆，并在镜头末尾落旁白“北关五百载，白骨未成尘。”；`SC001-SH003` 台词统一为“敌人上来了。”，语气为压低、急促但不慌。视频 prompt 不要求生成精确文字，字幕和配音在后期音频阶段处理。

English: `SC001-SH001` now uses an exterior front-biased siege push: the first frame starts from a low exterior siege angle with the beast tide, siege cart or gate-breaking mammoth pressing toward the same blackstone gate, and the last frame keeps the same exterior direction for the first heavy gate impact, snow haze blasting into frame and the same wall-top bell frame plus same bone bell swinging. R001-R004 are locked to one wall, one gate, one bell frame and one bell; outside the wall, only beast troops and companion beasts constrained by loaded `C020/C021/E01_C020` reference image nodes press toward the wall. Do not cross over the wall crown to the inner or opposite side, and do not read the wall as being attacked from both sides. The voiceover "In Suming year 1226, the northern thirteen-tribe alliance invades in force." reads during the push. `SC001-SH002` must use the new first frame of the young soldier half-collapsed by the wall, weapon dropped and bell swinging, with the voiceover line "At the northern pass, five hundred years of bones have not turned to dust." landing at the shot end; `SC001-SH003` uses the updated line "The enemy is coming up," delivered low, urgent but controlled. Video prompts do not ask the model to generate exact text; subtitles and voice are handled in post/audio.

### SC001 Cinematic Lighting Fix / SC001 电影光影修正

中文：当前画面“脏、暗、灰”的解决方式不是全局调亮，而是建立亮部层级。`SC001-SH001` 最亮点是撞门瞬间的冷白雪雾，其次是城墙、攻城器械、巨兽和骨钟的冷白/淡金轮廓，再其次是暗红火点边缘；黑石墙继续作为负补光压住大暗面。`SC001-SH002` 最亮点是撞门方向反射到墙头的冷白雪雾，轮廓光落在钟架、锁链、头盔、肩甲和脱手武器上，暗红火只勾手指、武器边缘、钟缘和冻血。禁止全画面平均灰、禁止没有主光方向、禁止把雪雾做成糊掉细节的白灰罩。

English: The fix for the current muddy, dark, grey image is not global brightening, but a clear highlight hierarchy. In `SC001-SH001`, the brightest point is the cold-white snow haze at the gate impact, followed by cold-white/pale-gold rims on the wall, siege engine, beast silhouettes and bone bell, then dark-red fire edges; the blackstone wall remains the negative-fill mass. In `SC001-SH002`, the brightest point is cold-white snow-haze bounce from the gate-impact direction, with rim light on bell frame, chains, helmet, shoulder armor and dropped weapon, while dark-red fire only edges fingers, weapon, bell rim and frozen blood. Reject flat grey across the whole frame, missing key-light direction, and snow haze that turns details into a white-grey smear.

### ComfyUI Reference Binding / 参考图节点接入

中文：`C020/C021/E01_C020` 不能只写在提示词里。生产侧必须把 `assets/characters/c020m.png`、`assets/characters/c021m.png`、`01/assets/characters/c020e01.png` 分别接入图片节点，并连接到兽族参考或 IPAdapter 分支。SH001 建议权重约为 `0.50 / 0.40 / 0.55`；SH002/SH003 只作为背景连续性，建议降到 `0.35 / 0.30 / 0.40`，低于人物身份参考和 I2V 首帧。

English: `C020/C021/E01_C020` must not live only in prompt text. Production must load `assets/characters/c020m.png`, `assets/characters/c021m.png`, and `01/assets/characters/c020e01.png` as image nodes and connect them to the beast reference or IPAdapter branch. Suggested SH001 weights are about `0.50 / 0.40 / 0.55`; for SH002/SH003 they are background continuity only and should drop to `0.35 / 0.30 / 0.40`, below human identity reference and I2V first-frame strength.

中文：`SC001-SH001` 的人物建模参考只服务尾帧守军连续性，不接到解码或视频节点。建议 `01/assets/characters/c024ae01.png -> 角色 IPAdapter/reference 分支 -> K采样器 model`，权重 `0.25-0.30`，start `0.55`，end `1.00`；`01/assets/characters/c004e01.png` 只有在薛临墙确实出现在 SH001 尾帧时启用，权重 `0.20-0.25`，start `0.65`，end `1.00`。

English: SH001 character modeling references are only for tail-frame defender continuity and must not connect to decode or video nodes. Suggested path: `01/assets/characters/c024ae01.png -> character IPAdapter/reference branch -> KSampler model`, weight `0.25-0.30`, start `0.55`, end `1.00`; enable `01/assets/characters/c004e01.png` only if Xue Linqiang is actually visible in the SH001 tail frame, weight `0.20-0.25`, start `0.65`, end `1.00`.

## Art Room 资产需求 / Art Room Asset Needs

- 角色：沈维桑、沈照眠、罗青禾、晏南枝遮面流亡状态、白翳、白册官吏、粮税小吏、混血奴兵、纯虫族小兵、薛临墙、顾怀章。
- 地点：锁喉关外墙局部、金河粮仓带门槛、南方红线密室、残阳坳村口、罗青禾药屋内、残阳坳旧井检查桌。
- 道具：白册、清明香、白蜡旗、药柜暗格、旧驿暗号底板、月白玉片、半卷血牒、沈维桑猎弓、沈照眠草药袋、虫蜡针、骨钟、祖牌小盒。
- 参考帧优先级：`SC004-SH001`, `SC005-SH001`, `SC006-SH005`, `SC006-SH010`, `SC002-SH002`, `SC003-SH001`。

## 配置待决 / Unresolved Config

- `needs_config`: 未提供视频模型 checkpoint、图像模型 checkpoint、LoRA ID、ControlNet 模型、IPAdapter preset、ComfyUI workflow template 或 node ID。
- `reference_frame_status`: `E01_R003` 旧扶钟构图已废弃，必须重生为“半倒墙边、武器脱手、骨钟横摆”；`E01_R001/E01_R002` 若仍是上一版升镜/城头转向构图，也需按“墙外前推 + 撞门震钟”重新确认或重生；最终仍以用户画面 QC 为准。
- 精确文字和符号镜头必须使用静帧、后期文字或 `REDRAW`：`SC004-SH007`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`。
- 直接视频模型不负责精确对白。对白来自 `01/script/final-script.md`，后续进入 audio/post 阶段时再拆成字幕和配音行。

## 风险 / Risks

- 序幕战争与征粮群像容易失控，必须以局部因果和有限参考帧实现。
- 白翳、白册官吏、奴兵、纯虫族小兵的层级若混同，会破坏肃明制度视觉。
- 残阳坳旧井、药屋、检查桌、后山出口的地理若不稳定，SC004-SC006 会失去悬疑逻辑。
- 儿童威胁镜头必须克制，避免直观伤害奇观。

## ComfyUI Handoff Recommendation

中文：先重生/确认 `r002e01.png` 的撞门震钟尾帧和 `r003e01.png` 的半倒墙边首帧，再补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/兽族参考 IPAdapter node 和 output node 绑定，并按 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 顺序渲染。`SC001-SH001` 使用 `3.5s / 84f`；其余场次继续按预资产计划推进 Art Room 资产。

English: First regenerate/recheck `r002e01.png` as the gate-impact bell-shock last frame and `r003e01.png` as the half-collapsed-by-the-wall first frame, then fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/beast reference IPAdapter nodes and output node bindings, and render `SC001-SH001`, `SC001-SH002`, and `SC001-SH003` in order. `SC001-SH001` uses `3.5s / 84f`; the remaining scenes should continue through the pre-asset Art Room plan.
