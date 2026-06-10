# 第01集《白册进村》视频生产计划 / Video Production Plan

## 状态 / Status

中文：当前已补齐 `SC001` 后资产 ComfyUI 交付包，并按最新方案把 `SC001-SH001` 改为墙外正向偏斜前推到第一次撞门震钟，放弃升到墙头后转向的复杂运镜。`SC001-SH002` 废弃年轻军户扶钟构图，改为被撞门余震晃倒、半倒墙边、武器脱手、旁边骨钟横摆。`SC002-SH001` 到 `SC002-SH004` 已补齐分镜构图、运镜、光线策略和 ComfyUI 双语提示词，并接入 `r005e01.png` 到 `r009e01.png` 候选参考帧；状态仍为 `needs_config / pending_user_visual_qc`。`SC003-SH001` 到 `SC003-SH004` 已补齐分镜构图、运镜、光线策略、ComfyUI 双语提示词和 workflow 绑定；`r010e01.png` 到 `r014e01.png` 已取回并写入 canonical 3840x2160 候选图，但源图为 1672x941，`r012e01.png` 与 `r013e01.png` 需提示词微调，五张图在正式 I2V/FLF2V 前建议原生 4K 重生。其余场次仍保持 director-room 预资产分镜包状态。`SC001` 可在重生/确认 `r002e01.png`、`r003e01.png` 后试渲；`SC002` 可在用户视觉 QC 通过参考帧并补齐模型与 workflow 配置后小批量试渲；`SC003` 需先完成 R012/R013 微调和 R010-R014 原生 4K 确认。

English: The post-asset ComfyUI delivery package is now complete for `SC001`, and `SC001-SH001` has been updated to the latest exterior front-biased push into the first gate-impact bell shock, dropping the complex wall-top turn. `SC001-SH002` abandons the young soldier bracing-the-bell composition and changes to aftershock collapse beside the wall, dropped weapon, and the same bell swinging beside him. `SC002-SH001` through `SC002-SH004` now have completed composition, camera movement, lighting strategy and bilingual ComfyUI prompts, using candidate reference frames `r005e01.png` through `r009e01.png`; their status remains `needs_config / pending_user_visual_qc`. `SC003-SH001` through `SC003-SH004` now have completed storyboard composition, camera movement, lighting strategy, bilingual ComfyUI prompts and workflow bindings; `r010e01.png` through `r014e01.png` have been retrieved and saved as canonical 3840x2160 candidate frames, but their source images are 1672x941, `r012e01.png` and `r013e01.png` need prompt tuning, and all five should be native-4K regenerated before final I2V/FLF2V use. The remaining scenes are still in director-room pre-asset shot-package state. `SC001` can enter test rendering after `r002e01.png` and `r003e01.png` are regenerated/rechecked; `SC002` can enter a small test batch after user visual QC approves the reference frames and model/workflow configuration is supplied; `SC003` must first finish R012/R013 tuning and native-4K confirmation for R010-R014.

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
2. SC002 征粮制度段参考帧 QC 后试渲：`SC002-SH001`, `SC002-SH002`, `SC002-SH003`, `SC002-SH004`
3. SC003 南方红线密室参考帧生成与 QC：`SC003-SH001`, `SC003-SH002`, `SC003-SH003`, `SC003-SH004`
4. 残阳坳主空间锁定：`SC004-SH001`, `SC006-SH001`, `SC006-SH008`
5. 核心角色参考：`SC004-SH003`, `SC004-SH005`, `SC004-SH006`, `SC006-SH005`
6. 关键道具插入：`SC004-SH007`, `SC004-SH008`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`, `SC006-SH010`
7. 药屋暗格段：`SC005-SH001` 到 `SC005-SH005`
8. 残阳坳对白压力段：`SC004-SH002` 到 `SC004-SH009`, `SC006-SH002` 到 `SC006-SH009`

## SC001 ComfyUI Handoff / SC001 ComfyUI 交付

| Shot | Method | Reference Inputs | Output |
| --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（墙外正向偏斜攻城首帧）, `01/assets/reference-frames/r002e01.png`（同一墙外方向第一次撞门震钟尾帧）, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png`, `01/assets/characters/c024ae01.png`（低权重墙头守军剪影连续性） | `01/renders/raw/sc001-sh001.mp4` |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png`（旧扶钟构图已废弃，必须重生为半倒墙边、武器脱手、骨钟横摆）, `01/assets/characters/c024ae01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh002.mp4` |
| `SC001-SH003` | `I2V` | `01/assets/reference-frames/r004e01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh003.mp4` |

中文：`SC001-SH001` 改为墙外正向偏斜攻城前推：首帧从墙外攻城方向低机位看兽潮、攻城车或破门猛犸压向同一面黑石城门，尾帧保持同一墙外方向，第一次重撞城门，雪雾冲画面，墙头同一钟架和同一口骨钟横摆。R001-R004 硬锁为同一面城墙、同一个城门、同一个钟架、同一口钟；城外只允许由已加载 `C020/C021/E01_C020` 参考图节点约束的兽族士兵和伴生兽朝墙攻来。禁止越过墙脊看城内或另一侧，禁止读成城墙两边同时被攻击。前推期间读精炼旁白“肃明一千两百二十六年，北方大雪。”。`SC001-SH002` 新版首帧必须是年轻军户被震倒半倒墙边、武器脱手、骨钟横摆，并在镜头末尾落旁白“敌已叩关。”；`SC001-SH003` 台词统一为“敌人上来了。”，语气为压低、急促但不慌。视频 prompt 不要求生成精确文字，字幕和配音在后期音频阶段处理。

English: `SC001-SH001` now uses an exterior front-biased siege push: the first frame starts from a low exterior siege angle with the beast tide, siege cart or gate-breaking mammoth pressing toward the same blackstone gate, and the last frame keeps the same exterior direction for the first heavy gate impact, snow haze blasting into frame and the same wall-top bell frame plus same bone bell swinging. R001-R004 are locked to one wall, one gate, one bell frame and one bell; outside the wall, only beast troops and companion beasts constrained by loaded `C020/C021/E01_C020` reference image nodes press toward the wall. Do not cross over the wall crown to the inner or opposite side, and do not read the wall as being attacked from both sides. The refined voiceover "In Suming year one thousand two hundred twenty-six, heavy snow falls in the north." reads during the push. `SC001-SH002` must use the new first frame of the young soldier half-collapsed by the wall, weapon dropped and bell swinging, with the voiceover line "The enemy has reached the pass." landing at the shot end; `SC001-SH003` uses the updated line "The enemy is coming up," delivered low, urgent but controlled. Video prompts do not ask the model to generate exact text; subtitles and voice are handled in post/audio.

### SC001 Cinematic Lighting Fix / SC001 电影光影修正

中文：当前画面“脏、暗、灰”的解决方式不是全局调亮，而是建立亮部层级。`SC001-SH001` 最亮点是撞门瞬间的冷白雪雾，其次是城墙、攻城器械、巨兽和骨钟的冷白/淡金轮廓，再其次是暗红火点边缘；黑石墙继续作为负补光压住大暗面。`SC001-SH002` 最亮点是撞门方向反射到墙头的冷白雪雾，轮廓光落在钟架、锁链、头盔、肩甲和脱手武器上，暗红火只勾手指、武器边缘、钟缘和冻血。禁止全画面平均灰、禁止没有主光方向、禁止把雪雾做成糊掉细节的白灰罩。

English: The fix for the current muddy, dark, grey image is not global brightening, but a clear highlight hierarchy. In `SC001-SH001`, the brightest point is the cold-white snow haze at the gate impact, followed by cold-white/pale-gold rims on the wall, siege engine, beast silhouettes and bone bell, then dark-red fire edges; the blackstone wall remains the negative-fill mass. In `SC001-SH002`, the brightest point is cold-white snow-haze bounce from the gate-impact direction, with rim light on bell frame, chains, helmet, shoulder armor and dropped weapon, while dark-red fire only edges fingers, weapon, bell rim and frozen blood. Reject flat grey across the whole frame, missing key-light direction, and snow haze that turns details into a white-grey smear.

### ComfyUI Reference Binding / 参考图节点接入

中文：`C020/C021/E01_C020` 不能只写在提示词里。生产侧必须把 `assets/characters/c020m.png`、`assets/characters/c021m.png`、`01/assets/characters/c020e01.png` 分别接入图片节点，并连接到兽族参考或 IPAdapter 分支。SH001 建议权重约为 `0.50 / 0.40 / 0.55`；SH002/SH003 只作为背景连续性，建议降到 `0.35 / 0.30 / 0.40`，低于人物身份参考和 I2V 首帧。

English: `C020/C021/E01_C020` must not live only in prompt text. Production must load `assets/characters/c020m.png`, `assets/characters/c021m.png`, and `01/assets/characters/c020e01.png` as image nodes and connect them to the beast reference or IPAdapter branch. Suggested SH001 weights are about `0.50 / 0.40 / 0.55`; for SH002/SH003 they are background continuity only and should drop to `0.35 / 0.30 / 0.40`, below human identity reference and I2V first-frame strength.

中文：`SC001-SH001` 的人物建模参考只服务尾帧守军连续性，不接到解码或视频节点。建议 `01/assets/characters/c024ae01.png -> 角色 IPAdapter/reference 分支 -> K采样器 model`，权重 `0.25-0.30`，start `0.55`，end `1.00`；`01/assets/characters/c004e01.png` 只有在薛临墙确实出现在 SH001 尾帧时启用，权重 `0.20-0.25`，start `0.65`，end `1.00`。

English: SH001 character modeling references are only for tail-frame defender continuity and must not connect to decode or video nodes. Suggested path: `01/assets/characters/c024ae01.png -> character IPAdapter/reference branch -> KSampler model`, weight `0.25-0.30`, start `0.55`, end `1.00`; enable `01/assets/characters/c004e01.png` only if Xue Linqiang is actually visible in the SH001 tail frame, weight `0.20-0.25`, start `0.65`, end `1.00`.

## SC002 ComfyUI Handoff / SC002 ComfyUI 交付

| Shot | Method | Reference Inputs | Lighting Intent | Output |
| --- | --- | --- | --- | --- |
| `SC002-SH001` | `I2V, 6s / 144f` | `01/assets/reference-frames/r005e01.png`, `01/assets/characters/c016be01.png`, `01/assets/locations/l003e01.png`, `01/assets/props/p003e01.png`, `01/assets/props/p008e01.png` | 柔和清晨冷雾 + 低角逆光 + 窄侧光；粮尘丁达尔只做纵深。 | `01/renders/raw/sc002-sh001.mp4` |
| `SC002-SH002` | `I2V, 7s / 168f` | `01/assets/reference-frames/r006e01.png`, `01/assets/characters/c017e01.png`, `01/assets/props/p008e01.png` | 门槛侧光强化泥、木缸、粗布、祖牌盒和腕绑；虫蜡小顶光只落封条。 | `01/renders/raw/sc002-sh002.mp4` |
| `SC002-SH003` | `I2V, 7s / 168f` | `01/assets/reference-frames/r007e01.png`, `01/assets/characters/c016be01.png`, `01/assets/characters/c017e01.png`, `01/assets/props/p003e01.png`, `01/assets/props/p008e01.png` | 虫蜡白顶光压白册和小吏脸壳，侧光读手指、皮肤、旧木、麻布和皮甲；硬光只给封牌落点。 | `01/renders/raw/sc002-sh003.mp4` |
| `SC002-SH004` | `FLF2V, 8s / 192f` | `01/assets/reference-frames/r008e01.png` first, `01/assets/reference-frames/r009e01.png` last, `01/assets/characters/c017e01.png`, `01/assets/props/p008e01.png` | 清晨低角逆光切押车轮廓和冷雾，侧光擦车辙、泥水、祖牌盒和麻袋；家人只吃柔光。 | `01/renders/raw/sc002-sh004.mp4` |

中文：SC002 的核心不是把粮仓拍暗，而是让光线解释制度如何压人。逆光用于 SH001/SH004 的空气感和轮廓，侧光用于麻袋、湿木、泥水、祖牌盒、皮甲和手腕纹理，顶光只在 SH002/SH003 小面积压虫蜡封条和白册。底光不得大面积使用；丁达尔光只服务纵深，不得变成特效味。

English: SC002 should not simply darken the grain depot; lighting must explain how the system presses people down. Backlight gives SH001/SH004 air and silhouette, side light reveals burlap, wet wood, mud water, tablet box, leather armor and wrist textures, and top light is used only in small areas on SH002/SH003 insect-wax seal and register. Bottom light must not be broad; Tyndall light only supports depth, never VFX spectacle.

## SC003 ComfyUI Handoff / SC003 ComfyUI 交付

| Shot | Method | Reference Inputs | Lighting Intent | Output |
| --- | --- | --- | --- | --- |
| `SC003-SH001` | `I2V, 7s / 168f` | `01/assets/reference-frames/r010e01.png`（视觉方向通过，建议原生 4K 重生）, `01/assets/locations/l014e01.png`, `01/assets/props/p009e01.png` | 低位油灯暖侧光擦纸纤维、红线绒毛、铜钉和湿木；右上月白雨夜冷反光只点水滴和油布折痕。 | `01/renders/raw/sc003-sh001.mp4` |
| `SC003-SH002` | `I2V, 8s / 192f` | `01/assets/reference-frames/r011e01.png`（视觉方向通过，建议原生 4K 重生）, `01/assets/characters/c011e01.png`, `01/assets/characters/c002e01.png`, `01/assets/props/p002e01.png` | 顾怀章吃暖灯侧光，晏南枝只吃玉片窄冷光；红线保持人物之间的政治边界，不揭全脸。 | `01/renders/raw/sc003-sh002.mp4` |
| `SC003-SH003` | `I2V, 9s / 216f` | `01/assets/reference-frames/r012e01.png`（需提示词微调并原生 4K 重生）, `01/assets/props/p002e01.png`, `01/assets/props/p009e01.png`, `01/assets/characters/c002e01.png`, `01/assets/characters/c011e01.png` | 油灯掠血牒纸纤维、潮痕、旧蜡封；月白玉片只给未接指尖冷边，重点是一指宽空隙。 | `01/renders/raw/sc003-sh003.mp4` |
| `SC003-SH004` | `FLF2V, 9s / 216f` | `01/assets/reference-frames/r013e01.png` first（需提示词微调并强化匹配切）, `01/assets/reference-frames/r014e01.png` last（视觉方向通过，需轻微光影层级强化）, `01/assets/locations/l014e01.png`, `01/assets/props/p009e01.png` | 压暗油灯，红线水滴暖边转向残阳坳土褐与虫蜡冷白；冷白只作封锁线信息，不做圣光。 | `01/renders/raw/sc003-sh004.mp4` |

中文：SC003 的主视频参考帧已经落地为重采样候选。生产侧可用 R010/R011/R014 判断构图方向，但不应把当前候选直接当作最终 I2V/FLF2V 主参考帧。下一轮应优先微调 R012/R013，并把 R010-R014 全部原生 4K 重生或由用户明确批准当前重采样候选。`c002e01/c011e01/l014e01/p002e01/p009e01` 只能作为身份、地点、道具和材质参考，不能替代主视频帧。负面提示必须拒绝现代地图字、红线魔法导航、血牒圣旨化发光、玉片法器化、晏南枝全脸华丽揭示、皇座幻象、梦幻溶解、全局灰黑欠曝和视频花屏。

English: SC003 primary video reference frames are now present as resampled candidates. Production may use R010/R011/R014 to judge layout direction, but should not treat the current candidates as final I2V/FLF2V primary frames. The next pass should tune R012/R013 first, then regenerate R010-R014 as native 4K or obtain explicit user approval for the current resampled candidates. `c002e01/c011e01/l014e01/p002e01/p009e01` are only identity, location, prop and material references and must not replace the primary video frames. Negative prompts must reject modern map text, red-cord magic navigation, sacred glowing genealogy, jade-as-weapon treatment, glamorous full Yan face reveal, throne vision, dreamy dissolve, flat grey underexposure and video glitches.

## Art Room 资产需求 / Art Room Asset Needs

- 角色：沈维桑、沈照眠、罗青禾、晏南枝遮面流亡状态、白翳、白册官吏、粮税小吏、混血奴兵、纯虫族小兵、薛临墙、顾怀章。
- 地点：锁喉关外墙局部、金河粮仓带门槛、南方红线密室、残阳坳村口、罗青禾药屋内、残阳坳旧井检查桌。
- 道具：白册、清明香、白蜡旗、药柜暗格、旧驿暗号底板、月白玉片、半卷血牒、沈维桑猎弓、沈照眠草药袋、虫蜡针、骨钟、祖牌小盒。
- 参考帧优先级：`SC004-SH001`, `SC005-SH001`, `SC006-SH005`, `SC006-SH010`, `SC002-SH002`, `SC003-SH001`。

## 配置待决 / Unresolved Config

- `needs_config`: 未提供视频模型 checkpoint、图像模型 checkpoint、LoRA ID、ControlNet 模型、IPAdapter preset、ComfyUI workflow template 或 node ID。
- `reference_frame_status`: `E01_R003` 旧扶钟构图已废弃，必须重生为“半倒墙边、武器脱手、骨钟横摆”；`E01_R001/E01_R002` 若仍是上一版升镜/城头转向构图，也需按“墙外前推 + 撞门震钟”重新确认或重生；`E01_R010` 到 `E01_R014` 已取回为 3840x2160 重采样候选，`E01_R012/E01_R013` 需提示词微调，五张图在最终视频生产前建议原生 4K 重生；最终仍以用户画面 QC 为准。
- 精确文字和符号镜头必须使用静帧、后期文字或 `REDRAW`：`SC004-SH007`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`。
- 直接视频模型不负责精确对白。对白来自 `01/script/final-script.md`，后续进入 audio/post 阶段时再拆成字幕和配音行。

## 风险 / Risks

- 序幕战争与征粮群像容易失控，必须以局部因果和有限参考帧实现。
- 白翳、白册官吏、奴兵、纯虫族小兵的层级若混同，会破坏肃明制度视觉。
- 残阳坳旧井、药屋、检查桌、后山出口的地理若不稳定，SC004-SC006 会失去悬疑逻辑。
- 儿童威胁镜头必须克制，避免直观伤害奇观。

## ComfyUI Handoff Recommendation

中文：先重生/确认 `r002e01.png` 的撞门震钟尾帧和 `r003e01.png` 的半倒墙边首帧，再补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/兽族参考 IPAdapter node 和 output node 绑定，并按 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 顺序渲染。随后完成 SC002 用户视觉 QC；再按 `01/art/reports/sc003-storyboard-asset-qc-2026-06-11.md` 微调 SC003 的 `r012e01.png`、`r013e01.png`，并确认或原生 4K 重生 `r010e01.png` 到 `r014e01.png`，确认红线、血牒、玉片、遮面和封锁线方向都符合本计划后再小批量试渲。

English: First regenerate/recheck `r002e01.png` as the gate-impact bell-shock last frame and `r003e01.png` as the half-collapsed-by-the-wall first frame, then fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/beast reference IPAdapter nodes and output node bindings, and render `SC001-SH001`, `SC001-SH002`, and `SC001-SH003` in order. Then complete SC002 user visual QC; after that tune SC003 `r012e01.png` and `r013e01.png` according to `01/art/reports/sc003-storyboard-asset-qc-2026-06-11.md`, then approve or native-4K regenerate `r010e01.png` through `r014e01.png`, verifying red cord, genealogy, jade, veil and blockade-line direction before small-batch test rendering.
