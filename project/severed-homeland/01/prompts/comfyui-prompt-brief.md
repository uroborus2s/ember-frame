# 第01集 SC001 ComfyUI Prompt Brief

## Scope / 范围

中文：本交付包只覆盖第01集 `SC001-SH001` 到 `SC001-SH003`，即锁喉关外墙暴雪序幕。SC001 资产图已经进入可交付使用状态，四张 3840x2160 横屏参考帧可用于 ComfyUI 视频生成。

English: This delivery pack covers only episode 01 `SC001-SH001` through `SC001-SH003`, the Suohou Gate blizzard prologue. SC001 visual assets are usable for handoff, and four 3840x2160 landscape reference frames can be used for ComfyUI video generation.

## Creative Update / 创作更新

中文：SC001 开场改为斜侧攻城升镜。首帧应是攻城方斜后侧低机位，兽潮从左前向右后斜推城门，黑石墙不正面居中；尾帧应是同一面外墙的墙头外沿中景偏近，骨钟、黑石女墙、守军肩背和枪线可读，镜头仍面向同一个墙外攻城面，墙外兽潮仍在斜下方背景可见。禁止越过墙脊看向城内或另一侧，禁止把城墙读成两侧都被攻击的横墙。旁白在这条升镜中读：“北墙五百年，血从未干。”

English: SC001 now uses a diagonal siege-side lift. The first frame should be a low diagonal rear-side siege angle, with the beast tide pushing from front-left toward the gate at rear-right and the black wall not centered frontally; the last frame should be an exterior-edge wall-top medium-near composition on the same wall face, with bone bell, blackstone parapet, defender shoulders and spear line readable, while the camera still faces the same exterior siege side and the exterior beast tide remains visible below on a diagonal. Do not cross over the wall crown to the inner or opposite side, and do not read the wall as a horizontal barrier attacked from both sides. The voiceover reads during this lift: "For five hundred years, the northern wall's blood has never dried."

中文：`r001e01.png` 和 `r002e01.png` 已按新版构图更新并通过视觉检查，可作为 `SC001-SH001` 的 FLF2V 首尾帧交付位。该镜头时长改为 `3.5s / 84 frames @ 24fps`。

English: `r001e01.png` and `r002e01.png` have been updated to the revised composition and visually checked, and may be used as the FLF2V first/last-frame delivery slots for `SC001-SH001`. The shot duration is now `3.5s / 84 frames @ 24fps`.

中文：薛临墙台词已改为更像战场现场提醒的短句：“敌人上来了。”剧本明确语气为压低、急促但不慌，像把墙头所有人的视线从骨钟拉回门线。视频模型只表现短促开口和战场提醒状态，精确台词留给字幕和配音。

English: Xue Linqiang's line is changed into a battlefield warning: "The enemy is coming up." The script specifies a low, urgent but controlled tone, pulling every defender's attention from the bell back to the gate line. The video model should only show a brief speaking state and battlefield warning posture; exact words belong to subtitles and voice audio.

## Lighting Direction / 光影方向

中文：以下“统一摄影语法”是给提示词编写者和 QC 使用的，不直接写进最终 `positive_prompt`。实际喂给模型的 `风格` 段只保留少量风格锚点：低魔东方史诗、横屏宽银幕、冷白暴雪边境、低调高反差、材质与空间以参考帧为准、真实运动质感。逐镜头的冷天光、远火反打、黑墙负补光和体积雪雾强弱，统一放在各镜头 `光影` 段里。

English: The following unified cinematography grammar is for prompt authors and QC, not direct final `positive_prompt` text. The model-facing `Style` section should keep only a few style anchors: grounded low-magic Eastern epic, landscape widescreen, cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, and physical motion texture. Shot-specific cold sky light, distant fire counterlight, black-wall negative fill and volumetric haze strength belong in each shot's `Lighting` section.

| Shot | 光影策略 / Lighting Strategy |
| --- | --- |
| `SC001-SH001` | 中文：斜侧攻城建立镜头需要最大环境纵深。冷白暴雪天光压出黑墙巨型剪影，黑墙负补光吞掉墙面和兽潮大暗面，远处暗红火线低位反打雪雾、烟尘、攻城队列、破旗、巨角、骨钟边缘和守军肩线。<br>English: The diagonal siege-establishing shot needs maximum environmental depth. Cold blizzard sky light silhouettes the black wall, black-wall negative fill swallows the wall face and beast tide's large shadow masses, and distant dark-red firelines low-counterlight snow haze, smoke, siege ranks, torn banners, horn edges, bone-bell edge and defender shoulder lines. |
| `SC001-SH002` | 中文：身体代价近景收窄光源。冷雪反光进钟裂，黑墙负补光压低人物，远火只在冻血、手指和骨钟裂边留下弱暖边，不做大场面火光。<br>English: The bodily-cost close shot narrows the light sources. Cold snow bounce enters bell cracks, black-wall negative fill presses the figure down, and distant fire leaves only a weak warm edge on frozen blood, fingers and bell cracks, not broad battlefield glow. |
| `SC001-SH003` | 中文：战场口令中近景强调人物可读性。半张脸被黑墙吞没，远火低位暖边只切出侧脸、手和旧甲片，雪雾分离枪线和门线，不形成英雄逆光。<br>English: The command close-medium shot prioritizes character readability. Half the face is swallowed by the black wall, low distant fire cuts only the side profile, hand and old armor plates, and snow haze separates spear line and gate line without heroic backlight. |

## Shot Method / 镜头方法

| Shot | Method | Reference Inputs | Audio |
| --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（新版斜侧攻城首帧）, `01/assets/reference-frames/r002e01.png`（新版城头中景偏近尾帧） | 旁白 / voiceover |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png` | 断矛、冻血、远处战声 / broken spear, frozen blood, distant battle |
| `SC001-SH003` | `I2V` | `01/assets/reference-frames/r004e01.png` | 薛临墙台词 / Xue Linqiang line |

## ComfyUI Reference Binding / ComfyUI 参考图接入

中文：ComfyUI 不会因为 prompt 写了 `C020`、`C021` 或文件名就自动读取图片。生产 workflow 必须把下列图片接入 `Load Image` 或等价图片节点，再连接到 IPAdapter、Reference-only、Redux 或实际 workflow 使用的参考图分支。

English: ComfyUI will not load images automatically just because the prompt mentions `C020`, `C021`, or a file name. Production workflow must load the following files through `Load Image` or equivalent image nodes, then connect them to IPAdapter, Reference-only, Redux, or the actual reference branch used by the workflow.

| Image | Path | Node Role | Suggested Weight |
| --- | --- | --- | --- |
| FLF2V first frame | `01/assets/reference-frames/r001e01.png` | `PLACEHOLDER_FIRST_FRAME_IMAGE_NODE` | primary |
| FLF2V last frame | `01/assets/reference-frames/r002e01.png` | `PLACEHOLDER_LAST_FRAME_IMAGE_NODE` | primary |
| Beast troop master | `assets/characters/c020m.png` | `PLACEHOLDER_BEAST_TROOP_MASTER_IMAGE_NODE -> PLACEHOLDER_BEAST_IPADAPTER_NODE` | SH001 `0.50`; SH002/SH003 background `0.35` |
| Companion beast master | `assets/characters/c021m.png` | `PLACEHOLDER_COMPANION_BEAST_MASTER_IMAGE_NODE -> PLACEHOLDER_BEAST_IPADAPTER_NODE` | SH001 `0.40`; SH002/SH003 background `0.30` |
| Episode beast state | `01/assets/characters/c020e01.png` | `PLACEHOLDER_EPISODE_BEAST_STATE_IMAGE_NODE -> PLACEHOLDER_BEAST_IPADAPTER_NODE` | SH001 `0.55`; SH002/SH003 background `0.40` |
| Young soldier state | `01/assets/characters/c024ae01.png` | `PLACEHOLDER_YOUNG_SOLDIER_IMAGE_NODE -> PLACEHOLDER_CHARACTER_IPADAPTER_NODE` | SH002 `0.55` |
| Xue Linqiang state | `01/assets/characters/c004e01.png` | `PLACEHOLDER_XUE_LINQIANG_IMAGE_NODE -> PLACEHOLDER_CHARACTER_IPADAPTER_NODE` | SH003 `0.60` |

中文：SH001 的首尾帧是主约束；三张兽族参考图只锁多兵种、多伴生兽、毛皮骨饰旧铁材质，不替代首尾帧。SH002/SH003 中兽族只在背景，参考权重必须低于人物身份参考和 I2V 首帧。

English: SH001 first/last frames are the primary constraints; the three beast references only lock troop variety, companion-beast diversity, fur/bone/old-iron material language, and must not replace the first/last frames. In SH002/SH003, beast forces are background-only, so beast reference weights must stay lower than human identity reference and I2V first frame.

## Copy-Ready Prompts / 可复制提示词

中文：生产侧直接使用 `01/prompts/comfyui-render-prompts.md`，其中已经按镜头组装好分段标题版 `positive_prompt_zh/en` 和 `negative_prompt_zh/en`。正向提示词使用 `风格 / 目标 / 光影 / 画面内容 / 运镜 / 约束` 分段，负向提示词使用 `通用负面 / 镜头负面` 分段。`comfyui-shot-prompts.json` 继续作为结构化源文件和溯源文件，不建议操作员手动拼接。

English: Production should use `01/prompts/comfyui-render-prompts.md` directly. It contains sectioned assembled `positive_prompt_zh/en` and `negative_prompt_zh/en` per shot. Positive prompts use `Style / Goal / Lighting / Visual Content / Camera / Motion / Constraints`; negative prompts use `Global Negative / Shot Negative`. `comfyui-shot-prompts.json` remains the structured source and traceability file, not the operator copy surface.

## Asset Use Rules / 资产使用规则

- 中文：`E01_R001` 和 `E01_R002` 是已更新通过的 `SC001-SH001` 首尾帧交付位；`E01_R003` 和 `E01_R004` 可继续作为 `SC001-SH002`、`SC001-SH003` 的 I2V 首帧。
- English: `E01_R001` and `E01_R002` are the updated and accepted first/last-frame delivery slots for `SC001-SH001`; `E01_R003` and `E01_R004` may continue as the I2V first frames for `SC001-SH002` and `SC001-SH003`.
- 中文：`C020/c020m.png`、`C021/c021m.png`、`E01_C020/c020e01.png` 必须作为图片节点接入，分别锁兽族多兵种、伴生兽多样性和本集暴雪状态；只写在 prompt 里无效。
- English: `C020/c020m.png`, `C021/c021m.png`, and `E01_C020/c020e01.png` must be connected as image nodes, locking beast troop variety, companion-beast diversity and episode blizzard state respectively; prompt text alone is not sufficient.
- 中文：`E01_C004`、`E01_C020`、`E01_C024A` 是角色状态卡，只能作为身份、服装、材质参考，不作为视频首帧。
- English: `E01_C004`, `E01_C020`, and `E01_C024A` are character state cards for identity, wardrobe, and material reference only, not video first frames.
- 中文：`E01_L007` 可作为锁喉关外墙场景参考；`E01_P021` 只作为骨钟、断矛、冻血和旧痕道具参考。
- English: `E01_L007` can be used as the Suohou Gate location reference; `E01_P021` is only a prop reference for the bell, broken spear, frozen blood, and old mark.

## Unresolved Config / 待决配置

中文：项目尚未提供 ComfyUI checkpoint、LoRA、ControlNet、IPAdapter preset、workflow template 或 node ID；参考帧已通过。因此 `SC001-SH001` 到 `SC001-SH003` 均标为 `needs_config`。

English: The project does not provide ComfyUI checkpoint, LoRA, ControlNet, IPAdapter preset, workflow template, or node IDs; the reference frames have passed visual check. Therefore `SC001-SH001` through `SC001-SH003` are all marked `needs_config`.
