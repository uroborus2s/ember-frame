# 第01集 SC001 ComfyUI Prompt Brief

## Scope / 范围

中文：本交付包只覆盖第01集 `SC001-SH001` 到 `SC001-SH003`，即锁喉关外墙暴雪序幕。SC001 资产图已经进入可交付使用状态，四张 4K 横屏参考图可用于 ComfyUI 视频生成。

English: This delivery pack covers only episode 01 `SC001-SH001` through `SC001-SH003`, the Suohou Gate blizzard prologue. SC001 visual assets are usable for handoff, and four 4K landscape reference images can be used for ComfyUI video generation.

## Texture Standard / 质感标准

中文：`r001e01.png` 已替换为 `019eac75-d625-7291-bfd7-273ec630f1c3` 最新 fortress_battle_far_view_war_aged_clean_4k 首帧，canonical 文件为 4096x1840 4K 宽银幕参考图。后续 `SC001` 尾帧以及 `SC002`、`SC003` 资产图必须以这张图的去粒子化真实质感为标准：黑石、旧木、骨钟/旧金属、兽皮毛、泥雪和布旗分材质处理，不允许黄色闪粉、数字噪点、全局假锐化或同质灰色颗粒材质。

English: `r001e01.png` has been replaced with the latest fortress_battle_far_view_war_aged_clean_4k first frame from `019eac75-d625-7291-bfd7-273ec630f1c3`; the canonical file is a 4096x1840 4K widescreen reference image. Later `SC001` tail-frame work and `SC002` / `SC003` asset images must match this de-particleized photoreal texture standard: separated blackstone, old timber, bone or aged metal, fur, mud-snow and cloth flag materials, with no yellow glitter, digital speckle, global fake sharpening or uniform grey grain texture.

## Creative Update / 创作更新

中文：SC001 开场改为墙外正向偏斜攻城前推，不再要求模型完成升到墙头后的转向。首帧应是墙外攻城方向低机位，约七成正向读城门压力、三成斜向给纵深；兽潮、攻城车或破门猛犸压向同一面黑石城门。尾帧仍保持同一墙外方向，攻城车木梁或铁包巨角第一次重撞城门，雪雾冲画面，墙头同一钟架和同一口骨钟在上方或侧上方横摆。禁止越过墙脊看向城内或另一侧，禁止把城墙读成两侧都被攻击的横墙。旁白在这条前推中只读精炼时代事件：“肃明一千两百二十六年，北方大雪。”；“敌已叩关。”改放 `SC001-SH002` 末尾。

English: SC001 now uses an exterior front-biased siege push, and no longer asks the model to complete a turn after climbing to the wall top. The first frame should be a low exterior siege angle, about seventy percent frontal gate pressure and thirty percent oblique depth, with the beast tide, siege cart or gate-breaking mammoth pressing toward the same blackstone gate. The last frame keeps the same exterior direction as a siege-cart beam or iron-wrapped horn hits the gate for the first time, snow haze blasts into frame, and the same wall-top bell frame and same bone bell swing above or upper-side. Do not cross over the wall crown to the inner or opposite side, and do not read the wall as a horizontal barrier attacked from both sides. This push only reads the refined era-event voiceover: "In Suming year one thousand two hundred twenty-six, heavy snow falls in the north."; "The enemy has reached the pass." lands at the end of `SC001-SH002`.

中文：`r001e01.png` 和 `r002e01.png` 若仍是上一版墙头转向构图，需要按本版“墙外前推 + 撞门震钟”重新确认或重生。该镜头时长保持 `3.5s / 84 frames @ 24fps`。

English: If `r001e01.png` and `r002e01.png` still reflect the previous wall-top turning composition, they must be rechecked or regenerated for this exterior push plus gate-impact bell-shock plan. The shot duration remains `3.5s / 84 frames @ 24fps`.

中文：`SC001-SH002` 废弃“年轻军户扶钟”构图。新版 `r003e01.png` 必须重生为：年轻军户被撞门余震晃倒，半倒在同一黑石女墙边，武器脱手滑进雪泥，旁边同一口骨钟横摆。人物脸被头盔、围巾、阴影和风雪半遮，不做正脸表情，重点是身体失衡、武器脱手和钟仍在响。

English: `SC001-SH002` drops the young soldier bracing-the-bell composition. The new `r003e01.png` must be regenerated as the young soldier knocked down by the gate-impact aftershock, half-collapsed beside the same blackstone parapet, weapon slipping into snow mud, with the same bone bell swinging beside him. His face is half hidden by helmet, scarf, shadow and blizzard, with the focus on body imbalance, dropped weapon and the still-ringing bell.

中文：薛临墙台词已改为更像战场现场提醒的短句：“敌人上来了。”剧本明确语气为压低、急促但不慌，像把墙头所有人的视线从骨钟拉回门线。视频模型只表现短促开口和战场提醒状态，精确台词留给字幕和配音。

English: Xue Linqiang's line is changed into a battlefield warning: "The enemy is coming up." The script specifies a low, urgent but controlled tone, pulling every defender's attention from the bell back to the gate line. The video model should only show a brief speaking state and battlefield warning posture; exact words belong to subtitles and voice audio.

## Lighting Direction / 光影方向

中文：以下“统一摄影语法”是给提示词编写者和 QC 使用的，不直接写进最终 `positive_prompt`。实际喂给模型的 `风格` 段只保留少量风格锚点：低魔东方史诗、横屏宽银幕、冷白暴雪边境、低调高反差、材质与空间以参考帧为准、真实运动质感。逐镜头的冷天光、远火反打、黑墙负补光和体积雪雾强弱，统一放在各镜头 `光影` 段里。

English: The following unified cinematography grammar is for prompt authors and QC, not direct final `positive_prompt` text. The model-facing `Style` section should keep only a few style anchors: grounded low-magic Eastern epic, landscape widescreen, cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, and physical motion texture. Shot-specific cold sky light, distant fire counterlight, black-wall negative fill and volumetric haze strength belong in each shot's `Lighting` section.

| Shot | 光影策略 / Lighting Strategy |
| --- | --- |
| `SC001-SH001` | 中文：墙外攻城建立镜头需要明确亮部层级，而不是整体压灰。裂云低角度冷白带淡金天光切出城墙、攻城车、巨兽和骨钟轮廓；撞门雪雾是最亮区域；低位暗红火点只做边缘反打；黑石墙保留大面积负补光暗面。<br>English: The exterior siege-establishing shot needs a clear highlight hierarchy rather than global greyness. Low storm-break sky light, cold white with a faint pale-gold edge, cuts the wall, siege engine, beast and bone-bell silhouettes; the gate-impact snow haze is the brightest zone; low dark-red fire points only edge-counterlight forms; the blackstone wall keeps large negative-fill shadow masses. |
| `SC001-SH002` | 中文：身体代价近景用精致轮廓光解决“脏暗”。左上或侧后裂云冷白带淡金天光给钟架、锁链、头盔、肩甲和脱手武器轮廓；撞门方向冷白雪雾反光是亮部中心；低位暗红火只勾手指、武器边缘、钟缘和冻血；黑墙负补光压脸和暗面。<br>English: The bodily-cost close shot solves muddy darkness with refined rim light. Storm-break cold-white light with a faint pale-gold edge from upper-left or side-back rims the bell frame, chains, helmet, shoulder armor and dropped weapon; cold-white snow-haze bounce from the gate-impact direction is the highlight center; low dark-red fire only edges fingers, weapon, bell rim and frozen blood; black-wall negative fill presses face and dark side. |
| `SC001-SH003` | 中文：战场口令中近景强调人物可读性。半张脸被黑墙吞没，远火低位暖边只切出侧脸、手和旧甲片，雪雾分离枪线和门线，不形成英雄逆光。<br>English: The command close-medium shot prioritizes character readability. Half the face is swallowed by the black wall, low distant fire cuts only the side profile, hand and old armor plates, and snow haze separates spear line and gate line without heroic backlight. |

## Video Quality Lock / 视频画质锁

中文：SC001 的“脏暗、模糊、花屏”问题必须在构图和 prompt 两层处理。构图上要求前景、中景、背景明确分层，关键脸、手、武器、钟架、城门和兽潮轮廓可读；光影上用明确亮部中心和轮廓光解决灰暗，不靠全局提亮。雪雾只允许做体积层、撞击亮部和隐藏剪切点，不能糊成覆盖细节的灰白罩。ComfyUI 负面提示必须包含：粒子化噪点、黄色闪粉、数字颗粒、全局高频锐化、视频涂抹、花屏、压缩块、局部融化、糊脸、手指融化、甲片粘连、关键轮廓糊掉。

English: SC001 must solve muddy darkness, blur and video glitches at both composition and prompt levels. Composition requires clear foreground/midground/background separation and readable key faces, hands, weapons, bell frame, gate and beast silhouettes; lighting solves darkness with a clear highlight center and rim light, not global brightening. Snow haze is only volumetric depth, impact highlight and hidden cut point, never a grey-white veil over detail. ComfyUI negative prompts must include particle-like digital speckle, yellow glitter, global high-frequency sharpening, video smearing, glitching, compression blocks, local melting, blurred faces, melted fingers, fused armor plates and blurred key silhouettes.

## Shot Method / 镜头方法

| Shot | Method | Reference Inputs | Audio |
| --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（墙外正向偏斜攻城首帧）, `01/assets/reference-frames/r002e01.png`（同一墙外方向撞门震钟尾帧） | 旁白 / voiceover |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png`（必须重生为半倒墙边、武器脱手、骨钟横摆） | 断矛、冻血、远处战声 / broken spear, frozen blood, distant battle |
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

- 中文：`E01_R001` 和 `E01_R002` 需要按“墙外正向偏斜攻城 + 撞门震钟”重新确认；`E01_R003` 旧扶钟构图已废弃，必须重生后再作为 `SC001-SH002` 的 I2V 首帧；`E01_R004` 可继续作为 `SC001-SH003` 的 I2V 首帧。
- English: `E01_R001` and `E01_R002` must be rechecked against the exterior front-biased siege plus gate-impact bell-shock plan; the old bracing-the-bell `E01_R003` composition is superseded and must be regenerated before use as the `SC001-SH002` I2V first frame; `E01_R004` may continue as the `SC001-SH003` I2V first frame.
- 中文：`C020/c020m.png`、`C021/c021m.png`、`E01_C020/c020e01.png` 必须作为图片节点接入，分别锁兽族多兵种、伴生兽多样性和本集暴雪状态；只写在 prompt 里无效。
- English: `C020/c020m.png`, `C021/c021m.png`, and `E01_C020/c020e01.png` must be connected as image nodes, locking beast troop variety, companion-beast diversity and episode blizzard state respectively; prompt text alone is not sufficient.
- 中文：`E01_C004`、`E01_C020`、`E01_C024A` 是角色状态卡，只能作为身份、服装、材质参考，不作为视频首帧。
- English: `E01_C004`, `E01_C020`, and `E01_C024A` are character state cards for identity, wardrobe, and material reference only, not video first frames.
- 中文：`E01_L007` 可作为锁喉关外墙场景参考；`E01_P021` 只作为骨钟、断矛、冻血和旧痕道具参考。
- English: `E01_L007` can be used as the Suohou Gate location reference; `E01_P021` is only a prop reference for the bell, broken spear, frozen blood, and old mark.

## Unresolved Config / 待决配置

中文：项目尚未提供 ComfyUI checkpoint、LoRA、ControlNet、IPAdapter preset、workflow template 或 node ID；参考帧已通过。因此 `SC001-SH001` 到 `SC001-SH003` 均标为 `needs_config`。

English: The project does not provide ComfyUI checkpoint, LoRA, ControlNet, IPAdapter preset, workflow template, or node IDs; the reference frames have passed visual check. Therefore `SC001-SH001` through `SC001-SH003` are all marked `needs_config`.
