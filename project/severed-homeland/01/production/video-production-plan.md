# 第01集《白册进村》视频生产计划 / Video Production Plan

## 状态 / Status

中文：当前为 director-room 预资产分镜包。尚未进入 Art Room 资产生产、ComfyUI 终版提示工程、渲染、剪辑、音频或交付 QC。

English: This is the director-room pre-asset shot package. It has not yet entered Art Room asset production, final ComfyUI prompt engineering, rendering, editing, audio or delivery QC.

## 生产规格 / Production Specs

- 画幅 / Aspect Ratio: `16:9`
- 帧率 / FPS: `24`
- 目标时长 / Target Duration: `270s`
- 规划时长 / Planned Duration: `269.5s`
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
- `01/production/video-production-plan.md`

## 生产顺序 / Recommended Render Order

1. 残阳坳主空间锁定：`SC004-SH001`, `SC006-SH001`, `SC006-SH008`
2. 核心角色参考：`SC004-SH003`, `SC004-SH005`, `SC004-SH006`, `SC006-SH005`
3. 关键道具插入：`SC004-SH007`, `SC004-SH008`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`, `SC006-SH010`
4. 药屋暗格段：`SC005-SH001` 到 `SC005-SH005`
5. 残阳坳对白压力段：`SC004-SH002` 到 `SC004-SH009`, `SC006-SH002` 到 `SC006-SH009`
6. 序幕世界压力段：`SC001-SH001` 到 `SC003-SH004`

## Art Room 资产需求 / Art Room Asset Needs

- 角色：沈维桑、沈照眠、罗青禾、晏南枝遮面流亡状态、白翳、白册官吏、粮税小吏、混血奴兵、纯虫族小兵、薛临墙、顾怀章。
- 地点：锁喉关外墙局部、金河粮仓带门槛、南方红线密室、残阳坳村口、罗青禾药屋内、残阳坳旧井检查桌。
- 道具：白册、清明香、白蜡旗、药柜暗格、旧驿暗号底板、月白玉片、半卷血牒、沈维桑猎弓、沈照眠草药袋、虫蜡针、骨钟、祖牌小盒。
- 参考帧优先级：`SC004-SH001`, `SC005-SH001`, `SC006-SH005`, `SC006-SH010`, `SC002-SH002`, `SC003-SH001`。

## 配置待决 / Unresolved Config

- `needs_config`: 未提供视频模型 checkpoint、图像模型 checkpoint、LoRA ID、ControlNet 模型、IPAdapter preset、ComfyUI workflow template 或 node ID。
- `needs_asset`: 新项目根目录尚无 `assets/asset-index.json`，也无 `01/art/asset-index.json`。
- 精确文字和符号镜头必须使用静帧、后期文字或 `REDRAW`：`SC004-SH007`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`。
- 直接视频模型不负责精确对白。对白来自 `01/script/final-script.md`，后续进入 audio/post 阶段时再拆成字幕和配音行。

## 风险 / Risks

- 序幕战争与征粮群像容易失控，必须以局部因果和有限参考帧实现。
- 白翳、白册官吏、奴兵、纯虫族小兵的层级若混同，会破坏肃明制度视觉。
- 残阳坳旧井、药屋、检查桌、后山出口的地理若不稳定，SC004-SC006 会失去悬疑逻辑。
- 儿童威胁镜头必须克制，避免直观伤害奇观。

## ComfyUI Handoff Recommendation

中文：先交 Art Room 生成角色、地点和关键道具资产，再回到 director-room 运行 post-asset prompt pass，生成 `comfyui-prompt-brief.md`、style preset、asset prompt pack、final shot prompts、workflow plan 和 prompt QC。当前 `generation-plan.json` 已给出每个镜头的方法、资产需求和风险。

English: First hand this package to Art Room for character, location and key prop assets. Then return to director-room for the post-asset prompt pass to create the ComfyUI prompt brief, style preset, asset prompt pack, final shot prompts, workflow plan and prompt QC. The current `generation-plan.json` already defines method, asset needs and risks for each shot.
