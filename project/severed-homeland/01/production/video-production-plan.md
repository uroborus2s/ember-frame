# 第01集《白册进村》视频生产计划 / Video Production Plan

## 状态 / Status

中文：当前已补齐 `SC001` 后资产 ComfyUI 交付包，并已按新版斜侧攻城升镜更新 `SC001-SH001`。`r001e01.png` 和 `r002e01.png` 已通过新版首尾帧构图检查。其余场次仍保持 director-room 预资产分镜包状态。`SC001-SH001` 到 `SC001-SH003` 可在补齐模型与 workflow 配置后小批量试渲。

English: The post-asset ComfyUI delivery package is now complete for `SC001`, and `SC001-SH001` has been updated to the new diagonal siege-side lift. `r001e01.png` and `r002e01.png` have passed the updated first/last-frame composition check. The remaining scenes are still in director-room pre-asset shot-package state. `SC001-SH001` through `SC001-SH003` can enter a small test batch after model and workflow configuration is supplied.

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
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（新版斜侧攻城首帧）, `01/assets/reference-frames/r002e01.png`（单墙单钟城头尾帧）, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh001.mp4` |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh002.mp4` |
| `SC001-SH003` | `I2V` | `01/assets/reference-frames/r004e01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh003.mp4` |

中文：`SC001-SH001` 改为斜侧攻城升镜：首帧从攻城方斜后侧低机位看兽潮斜推城门，尾帧沿同一面墙斜爬上墙头并约 45 度转向人族女墙空间。R001-R004 硬锁为同一面城墙、同一个钟架、同一口钟；城外只允许继承 `C020/C021/E01_C020` 的兽族士兵和伴生兽朝墙攻来。升镜期间读旁白“北墙五百年，血从未干。”。`SC001-SH003` 台词统一为“敌人上来了。”，语气为压低、急促但不慌。视频 prompt 不要求生成精确文字，字幕和配音在后期音频阶段处理。

English: `SC001-SH001` now uses a diagonal siege-side lift: the first frame starts from a low diagonal rear-side siege angle with the beast tide pushing diagonally toward the gate, and the last frame climbs along the same wall to the wall top before turning about 45 degrees into the human parapet space. R001-R004 are locked to one wall, one bell frame and one bell; outside the wall only C020/C021/E01_C020 beast troops and companion beasts press toward the wall. The voiceover "For five hundred years, the northern wall's blood has never dried" reads during the lift. `SC001-SH003` uses the updated line "The enemy is coming up," delivered low, urgent but controlled. Video prompts do not ask the model to generate exact text; subtitles and voice are handled in post/audio.

## Art Room 资产需求 / Art Room Asset Needs

- 角色：沈维桑、沈照眠、罗青禾、晏南枝遮面流亡状态、白翳、白册官吏、粮税小吏、混血奴兵、纯虫族小兵、薛临墙、顾怀章。
- 地点：锁喉关外墙局部、金河粮仓带门槛、南方红线密室、残阳坳村口、罗青禾药屋内、残阳坳旧井检查桌。
- 道具：白册、清明香、白蜡旗、药柜暗格、旧驿暗号底板、月白玉片、半卷血牒、沈维桑猎弓、沈照眠草药袋、虫蜡针、骨钟、祖牌小盒。
- 参考帧优先级：`SC004-SH001`, `SC005-SH001`, `SC006-SH005`, `SC006-SH010`, `SC002-SH002`, `SC003-SH001`。

## 配置待决 / Unresolved Config

- `needs_config`: 未提供视频模型 checkpoint、图像模型 checkpoint、LoRA ID、ControlNet 模型、IPAdapter preset、ComfyUI workflow template 或 node ID。
- `reference_frame_status`: `01/art/asset-index.json` 与 `01/art/asset-manifest.json` 中 `E01_R001` 到 `E01_R004` 已更新为 `generated_candidate_pending_user_qc`；最终仍以用户画面 QC 为准。
- 精确文字和符号镜头必须使用静帧、后期文字或 `REDRAW`：`SC004-SH007`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`。
- 直接视频模型不负责精确对白。对白来自 `01/script/final-script.md`，后续进入 audio/post 阶段时再拆成字幕和配音行。

## 风险 / Risks

- 序幕战争与征粮群像容易失控，必须以局部因果和有限参考帧实现。
- 白翳、白册官吏、奴兵、纯虫族小兵的层级若混同，会破坏肃明制度视觉。
- 残阳坳旧井、药屋、检查桌、后山出口的地理若不稳定，SC004-SC006 会失去悬疑逻辑。
- 儿童威胁镜头必须克制，避免直观伤害奇观。

## ComfyUI Handoff Recommendation

中文：SC001 的参考帧已通过新版构图检查。生产侧补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node 和 output node 绑定后，按 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 顺序渲染。`SC001-SH001` 使用 `3.5s / 84f`，其余场次继续按预资产计划推进 Art Room 资产。

English: SC001 reference frames have passed the updated composition check. Production should fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node and output node bindings, then render `SC001-SH001`, `SC001-SH002`, and `SC001-SH003` in order. `SC001-SH001` uses `3.5s / 84f`; the remaining scenes should continue through the pre-asset Art Room plan.
