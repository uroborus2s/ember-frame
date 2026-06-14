# 第01集《白册进村》视频生产计划 / Video Production Plan

## 状态 / Status

中文：当前已补齐 `SC001` 后资产 ComfyUI 交付包，并按最新方案把 `SC001-SH001` 改为墙外正中对称史诗前推到第一次撞门，门楼内钟声只作为音频桥，画面不强制露钟；`r002e01.png` 已正式替换为更近城门、更强撞击且墙旗为 P017 肃明虫族帝国旗的 4096x2304 尾帧。`r003e01.png` 与 `r004e01.png` 已在 2026-06-14 追加修复为 4096x2304：R003 锁定与 R004 女墙一致的门楼粗糙哑光黑石砌块、R001/R002/R004 同天气冷灰暴雪光、被余震震倒但活着且主角优先的年轻军户和横摆氧化旧金属警钟；R004 锁定薛临墙主角优先、墙顶粗糙黑石砌块材质分离、城外攻城雪泥战场虚化退后和同一氧化旧金属警钟。`SC002-SH001` 到 `SC002-SH004` 的 R005-R009 当前候选已被用户视觉 QC 退回，原因是角色一致性与身高差仍未满足；状态改为 `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`，不得进入 ComfyUI 绑定、小批量试渲或正式视频制作。下一轮必须先按 `C025 -> C017 -> C016 -> C018 -> C019` 同地平线比例链重生角色状态卡，再按 `4096x2304` 重生 R005-R009。`SC003-SH001` 到 `SC003-SH004` 已完成视频/I2V 提示词、逐秒动作说明、运镜约束和 workflow 绑定更新；`r010e01.png` 到 `r013e01.png` 为已通过高分复评的主 I2V 参考帧，`r014e01.png` 仅作为后续残阳坳封锁线匹配目标保留。其余场次仍保持 director-room 预资产分镜包状态。`SC001` 与 `SC003` 可在补齐模型与 workflow 配置后先做小批量 motion test。

English: The post-asset ComfyUI delivery package is now complete for `SC001`, and `SC001-SH001` has been updated to a centered exterior epic push into the first gate impact, with the gatehouse bell as an audio bridge only and no on-screen bell required; `r002e01.png` has been formally replaced with a 4096x2304 closer-gate, stronger-impact tail frame using P017 Suming insect empire wall flags. `r003e01.png` and `r004e01.png` were additionally corrected on 2026-06-14 at 4096x2304: R003 now locks R004-matched rough matte blackstone gatehouse blocks, R001/R002/R004-matched cold grey blizzard lighting, a living aftershock-fallen young soldier with stronger protagonist priority, and the swinging oxidized old metal bell; R004 now locks protagonist-priority Xue Linqiang, rough blackstone wall-top masonry with clearer material separation, softened exterior churned siege field and the same oxidized old metal bell. The current SC002 R005-R009 candidates have failed user visual QC because character identity and height hierarchy still do not hold; status is now `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11`, so SC002 must not enter ComfyUI binding, test rendering, or final video production. The next pass must rebuild the episode character cards against the `C025 -> C017 -> C016 -> C018 -> C019` same-ground scale ladder and regenerate R005-R009 at `4096x2304`. `SC003-SH001` through `SC003-SH004` have now been updated with video/I2V prompts, beat-by-beat action instructions, camera constraints and workflow binding updates; `r010e01.png` through `r013e01.png` are high-score approved primary I2V reference frames, while `r014e01.png` is retained only as a later Canyangao blockade match target. The remaining scenes are still in director-room pre-asset shot-package state. `SC001` and `SC003` can enter small motion-test batches after model and workflow configuration is supplied.

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
2. SC002 征粮制度段用户视觉 QC 通过后试渲：`SC002-SH001`, `SC002-SH002`, `SC002-SH003`, `SC002-SH004`
3. SC003 南方红线密室参考帧生成与 QC：`SC003-SH001`, `SC003-SH002`, `SC003-SH003`, `SC003-SH004`
4. 残阳坳主空间锁定：`SC004-SH001`, `SC006-SH001`, `SC006-SH008`
5. 核心角色参考：`SC004-SH003`, `SC004-SH005`, `SC004-SH006`, `SC006-SH005`
6. 关键道具插入：`SC004-SH007`, `SC004-SH008`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`, `SC006-SH010`
7. 药屋暗格段：`SC005-SH001` 到 `SC005-SH005`
8. 残阳坳对白压力段：`SC004-SH002` 到 `SC004-SH009`, `SC006-SH002` 到 `SC006-SH009`

## SC001 ComfyUI Handoff / SC001 ComfyUI 交付

| Shot | Method | Reference Inputs | Output |
| --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `01/assets/reference-frames/r001e01.png`（墙外正中对称史诗攻城首帧）, `01/assets/reference-frames/r002e01.png`（同一墙外方向、更近城门、更强第一次撞门尾帧；门楼内钟声，画面不强制露钟）, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png`, `01/assets/characters/c024ae01.png`（低权重墙头守军剪影连续性） | `01/renders/raw/sc001-sh001.mp4` |
| `SC001-SH002` | `I2V` | `01/assets/reference-frames/r003e01.png`（4096x2304，门楼粗糙哑光黑石砌块匹配 R004 女墙，天气光线匹配 R001/R002/R004，年轻军户被余震震倒但活着且主角优先、武器脱手、氧化旧金属警钟横摆）, `01/assets/characters/c024ae01.png`, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh002.mp4` |
| `SC001-SH003` | `I2V` | `01/assets/reference-frames/r004e01.png`（4096x2304，薛临墙主角优先、墙顶大块粗糙黑石砌块、城外攻城雪泥战场虚化退后、同一氧化旧金属警钟）, `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png` | `01/renders/raw/sc001-sh003.mp4` |

中文：`SC001-SH001` 改为墙外正中对称史诗攻城前推：首帧从墙外攻城方向低机位看兽潮、攻城车或破门猛犸压向同一面黑石城门，尾帧保持同一墙外方向和中轴压力，更近靠近城门，第一次重撞城门，雪雾、碎冰、旧木屑、门闩震动和黑石边缘反光更浓烈。旧金属警钟在门楼里，第一镜只需要钟声，不要求钟体或同一钟架出现在画面中。R001/R002 硬锁为同一面城墙、同一个城门、同一墙外攻城方向和门楼内钟声；R003/R004 可在后续墙头/门楼空间揭示同一口旧金属警钟。城外只允许由已加载 `C020/C021/E01_C020` 参考图节点约束的兽族士兵和伴生兽朝墙攻来。禁止越过墙脊看城内或另一侧，禁止读成城墙两边同时被攻击。前推期间读精炼旁白“肃明一千两百二十六年，北方大雪。”。`SC001-SH002` 新版首帧必须是年轻军户被震倒半倒墙边、武器脱手、旧金属警钟横摆，并在镜头末尾落旁白“敌已叩关。”；`SC001-SH003` 台词统一为“敌人上来了。”，语气为压低、急促但不慌。视频 prompt 不要求生成精确文字，字幕和配音在后期音频阶段处理。

English: `SC001-SH001` now uses a centered exterior epic siege push: the first frame starts from a low exterior siege angle with the beast tide, siege cart or gate-breaking mammoth pressing toward the same blackstone gate, and the last frame keeps the same exterior direction and central-axis pressure, moves closer to the gate, and shows the first heavy gate impact with stronger snow haze, ice splinters, old timber chips, gate-bar shock and blackstone edge reflection. The old metal alarm bell is inside the gatehouse; this first shot needs only the bell sound, with no visible bell body or same bell frame required. R001/R002 are locked to one wall, one gate, the same exterior attack direction and gatehouse bell sound; R003/R004 may reveal the same old metal alarm bell later in the wall-top/gatehouse space. Outside the wall, only beast troops and companion beasts constrained by loaded `C020/C021/E01_C020` reference image nodes press toward the wall. Do not cross over the wall crown to the inner or opposite side, and do not read the wall as being attacked from both sides. The refined voiceover "In Suming year one thousand two hundred twenty-six, heavy snow falls in the north." reads during the push. `SC001-SH002` must use the new first frame of the young soldier half-collapsed by the wall, weapon dropped and bell swinging, with the voiceover line "The enemy has reached the pass." landing at the shot end; `SC001-SH003` uses the updated line "The enemy is coming up," delivered low, urgent but controlled. Video prompts do not ask the model to generate exact text; subtitles and voice are handled in post/audio.

### SC001 Cinematic Lighting Fix / SC001 电影光影修正

中文：当前画面“脏、暗、灰”的解决方式不是全局调亮，而是建立亮部层级。`SC001-SH001` 最亮点是撞门瞬间的冷白雪雾、碎冰和旧木屑，其次是城墙、攻城器械、巨兽和城门的冷白/淡金轮廓，再其次是暗红火点边缘；黑石墙继续作为负补光压住大暗面，旧金属警钟只作为门楼内钟声存在。`SC001-SH002` 最亮点是撞门方向反射到墙头的冷白雪雾，轮廓光落在钟架、锁链、头盔、肩甲和脱手武器上，暗红火只勾手指、武器边缘、钟缘和冻血。禁止全画面平均灰、禁止没有主光方向、禁止把雪雾做成糊掉细节的白灰罩。

English: The fix for the current muddy, dark, grey image is not global brightening, but a clear highlight hierarchy. In `SC001-SH001`, the brightest point is the cold-white snow haze, ice splinters and old timber chips at the gate impact, followed by cold-white/pale-gold rims on the wall, siege engine, beast silhouettes and gate, then dark-red fire edges; the blackstone wall remains the negative-fill mass, and the old metal alarm bell exists only as gatehouse sound. In `SC001-SH002`, the brightest point is cold-white snow-haze bounce from the gate-impact direction, with rim light on bell frame, chains, helmet, shoulder armor and dropped weapon, while dark-red fire only edges fingers, weapon, bell rim and frozen blood. Reject flat grey across the whole frame, missing key-light direction, and snow haze that turns details into a white-grey smear.

### ComfyUI Reference Binding / 参考图节点接入

中文：`C020/C021/E01_C020` 不能只写在提示词里。生产侧必须把 `assets/characters/c020m.png`、`assets/characters/c021m.png`、`01/assets/characters/c020e01.png` 分别接入图片节点，并连接到兽族参考或 IPAdapter 分支。SH001 建议权重约为 `0.50 / 0.40 / 0.55`；SH002/SH003 只作为背景连续性，建议降到 `0.35 / 0.30 / 0.40`，低于人物身份参考和 I2V 首帧。

English: `C020/C021/E01_C020` must not live only in prompt text. Production must load `assets/characters/c020m.png`, `assets/characters/c021m.png`, and `01/assets/characters/c020e01.png` as image nodes and connect them to the beast reference or IPAdapter branch. Suggested SH001 weights are about `0.50 / 0.40 / 0.55`; for SH002/SH003 they are background continuity only and should drop to `0.35 / 0.30 / 0.40`, below human identity reference and I2V first-frame strength.

中文：`SC001-SH001` 的人物建模参考只服务尾帧守军连续性，不接到解码或视频节点。建议 `01/assets/characters/c024ae01.png -> 角色 IPAdapter/reference 分支 -> K采样器 model`，权重 `0.25-0.30`，start `0.55`，end `1.00`；`01/assets/characters/c004e01.png` 只有在薛临墙确实出现在 SH001 尾帧时启用，权重 `0.20-0.25`，start `0.65`，end `1.00`。

English: SH001 character modeling references are only for tail-frame defender continuity and must not connect to decode or video nodes. Suggested path: `01/assets/characters/c024ae01.png -> character IPAdapter/reference branch -> KSampler model`, weight `0.25-0.30`, start `0.55`, end `1.00`; enable `01/assets/characters/c004e01.png` only if Xue Linqiang is actually visible in the SH001 tail frame, weight `0.20-0.25`, start `0.65`, end `1.00`.

## SC002 ComfyUI Handoff / SC002 ComfyUI 交付

| Shot | Method | Reference Inputs | Lighting Intent | Output |
| --- | --- | --- | --- | --- |
| `SC002-SH001` | `I2V, 6s / 144f` | `01/assets/reference-frames/r005e01.png`, `01/assets/characters/c016be01.png`, `01/assets/characters/c018e01.png`, `01/assets/locations/l003e01.png`, `01/assets/props/p003e01.png`, `01/assets/props/p008e01.png` | 柔和清晨冷雾 + 低角逆光 + 窄侧光；C018 只作持械封路与身高体型参考，粮尘丁达尔只做纵深。 | `01/renders/raw/sc002-sh001.mp4` |
| `SC002-SH002` | `I2V, 7s / 168f` | `01/assets/reference-frames/r006e01.png`, `01/assets/characters/c017e01.png`, `01/assets/characters/c018e01.png`, `01/assets/props/p008e01.png` | 门槛侧光强化泥、木缸、粗布、祖牌盒和腕绑；C017 五指硬化手扣成人前臂/袖口，C018 只作背景持械封路剪影。 | `01/renders/raw/sc002-sh002.mp4` |
| `SC002-SH003` | `I2V, 7s / 168f` | `01/assets/reference-frames/r007e01.png`, `01/assets/characters/c016be01.png`, `01/assets/characters/c017e01.png`, `01/assets/characters/c018e01.png`, `01/assets/props/p003e01.png`, `01/assets/props/p008e01.png` | 虫蜡白顶光压白册和 C016B 小吏脸壳，侧光读 C017 手指、皮肤、旧木、麻布和皮甲；C018 只在背景守路持械。 | `01/renders/raw/sc002-sh003.mp4` |
| `SC002-SH004` | `FLF2V, 8s / 192f` | `01/assets/reference-frames/r008e01.png` first, `01/assets/reference-frames/r009e01.png` last, `01/assets/characters/c017e01.png`, `01/assets/characters/c018e01.png`, `01/assets/props/p008e01.png` | 清晨低角逆光切押车轮廓和冷雾，侧光擦车辙、泥水、祖牌盒和麻袋；C018 维持同一持械封路线，不搬粮、不扣腕。 | `01/renders/raw/sc002-sh004.mp4` |

中文：SC002 的核心不是把粮仓拍暗，而是让光线解释制度如何压人。逆光用于 SH001/SH004 的空气感和轮廓，侧光用于麻袋、湿木、泥水、祖牌盒、皮甲和手腕纹理，顶光只在 SH002/SH003 小面积压虫蜡封条和白册。底光不得大面积使用；丁达尔光只服务纵深，不得变成特效味。

English: SC002 should not simply darken the grain depot; lighting must explain how the system presses people down. Backlight gives SH001/SH004 air and silhouette, side light reveals burlap, wet wood, mud water, tablet box, leather armor and wrist textures, and top light is used only in small areas on SH002/SH003 insect-wax seal and register. Bottom light must not be broad; Tyndall light only supports depth, never VFX spectacle.

中文：SC002 当前是候选资产交付，不是开拍许可。正式视频前必须由用户确认 `r005e01.png` 到 `r009e01.png` 中 C016B 官吏脸型/白蜡高帽/190-210cm 身高继承、C017 奴兵五指硬化手与低后背细金钱尾辫、C018 纯虫族 200-230cm 持械封路和同地面体型压迫均满足导演要求。

English: SC002 is currently a candidate asset handoff, not production approval. Before final video work, the user must visually confirm that `r005e01.png` through `r009e01.png` satisfy the director requirements for C016B official face, wax-white tall hat and 190-210 cm height inheritance, C017 five-finger hardened hand plus one thin low money-tail braid, and C018 200-230 cm armed pure-insect route-blocking scale pressure on the same ground plane.

## SC003 ComfyUI Handoff / SC003 ComfyUI 交付

| Shot | Method | Reference Inputs | Motion / Lighting Intent | Output |
| --- | --- | --- | --- | --- |
| `SC003-SH001` | `I2V, 7s / 168f` | `01/assets/reference-frames/r010e01.png`（高分通过，主 I2V 帧）, `01/assets/locations/l014e01.png`, `01/assets/props/p009e01.png` | 0-2s 油灯雨滴微动，2-5s 沿红线北推，5-7s 停北端水滴；低位暖侧光与右上冷雨反光锁纸、线、铜、水材质。 | `01/renders/raw/sc003-sh001.mp4` |
| `SC003-SH002` | `I2V, 8s / 192f` | `01/assets/reference-frames/r011e01.png`（高分通过，主 I2V 帧）, `01/assets/characters/c011e01.png`, `01/assets/characters/c002e01.png`, `01/assets/props/p002e01.png` | 锁低桌沿双人构图；顾手压图、晏手收紧玉片、焦点回到红线；顾暖侧光、晏窄冷边，不揭全脸。 | `01/renders/raw/sc003-sh002.mp4` |
| `SC003-SH003` | `I2V, 9s / 216f` | `01/assets/reference-frames/r012e01.png`（高分通过，主 I2V 帧）, `01/assets/props/p002e01.png`, `01/assets/props/p009e01.png`, `01/assets/characters/c002e01.png`, `01/assets/characters/c011e01.png` | 血牒只滑 2-3cm 后停在指尖前；5-9s 持续守住一指宽空隙；暖冷交界压在红线与未接触空隙处。 | `01/renders/raw/sc003-sh003.mp4` |
| `SC003-SH004` | `I2V, 9s / 216f` | `01/assets/reference-frames/r013e01.png`（高分通过，转场首镜主 I2V 帧）, `01/assets/locations/l014e01.png`, `01/assets/props/p009e01.png`; `r014e01.png` 仅保留为后续可选匹配目标 | 本轮不强制 R013->R014 FLF2V；只做红线北端雨滴、短匹配移动和曝光下落，给后续剪辑匹配残阳坳封锁线。 | `01/renders/raw/sc003-sh004.mp4` |

中文：SC003 四张核心密室参考帧 `r010e01.png` 到 `r013e01.png` 已完成高分复评，达到导演分 `92+`、美术分 `95+`，本轮可作为主 I2V 图像输入进入小批量 motion test。`r014e01.png` 属于残阳坳封锁线目标画面，只能作为后续剪辑或经明确批准后的 FLF2V 终帧测试，不再作为 SC003 四张密室核心帧。`c002e01/c011e01/l014e01/p002e01/p009e01` 只能作为身份、地点、道具和材质参考，权重必须低于主视频帧。负面提示必须拒绝现代地图字、红线魔法导航、血牒圣旨化发光、玉片法器化、晏南枝全脸华丽揭示、皇座幻象、梦幻溶解、全局灰黑欠曝和视频花屏。

English: The four core SC003 room reference frames `r010e01.png` through `r013e01.png` have passed the high-score review, meeting director `92+` and art `95+`, and may now be used as primary I2V image inputs for small-batch motion tests. `r014e01.png` belongs to the Canyangao blockade target image and should only be used for a later edit match or explicitly approved FLF2V tail test, not as one of the four core SC003 room frames. `c002e01/c011e01/l014e01/p002e01/p009e01` are only identity, location, prop and material references and must stay below the primary video frame weight. Negative prompts must reject modern map text, red-cord magic navigation, sacred glowing genealogy, jade-as-weapon treatment, glamorous full Yan face reveal, throne vision, dreamy dissolve, flat grey underexposure and video glitches.

## Art Room 资产需求 / Art Room Asset Needs

- 角色：沈维桑、沈照眠、罗青禾、晏南枝遮面流亡状态、白翳、白册官吏、粮税小吏、混血奴兵、纯虫族小兵、薛临墙、顾怀章。
- 地点：锁喉关外墙局部、金河粮仓带门槛、南方红线密室、残阳坳村口、罗青禾药屋内、残阳坳旧井检查桌。
- 道具：白册、清明香、白蜡旗、药柜暗格、旧驿暗号底板、月白玉片、半卷血牒、沈维桑猎弓、沈照眠草药袋、虫蜡针、旧金属警钟、祖牌小盒。
- 参考帧优先级：`SC004-SH001`, `SC005-SH001`, `SC006-SH005`, `SC006-SH010`, `SC002-SH002`, `SC003-SH001`。

## 配置待决 / Unresolved Config

- `needs_config`: 未提供视频模型 checkpoint、图像模型 checkpoint、LoRA ID、ControlNet 模型、IPAdapter preset、ComfyUI workflow template 或 node ID。
- `reference_frame_status`: `E01_R003` 与 `E01_R004` 已于 2026-06-14 修复并替换为 4096x2304 正式视频参考帧，状态为 `ready_for_sc001_i2v_motion_test_pending_model_config`；`E01_R005` 到 `E01_R009` 已按同一泥地真实身高差、C016B 全局继承、C017 五指手/细尾辫、C018 持械封路方案重做并进入用户视觉 QC，不得在确认前标记为 final approved；`E01_R010` 到 `E01_R013` 已通过 SC003 高分复评，可作为主 I2V motion test 参考帧；`E01_R014` 只作为后续残阳坳封锁线匹配目标，不能混入 SC003 密室 I2V 首镜。最终正式渲染仍以模型配置和 motion QC 为准。
- 精确文字和符号镜头必须使用静帧、后期文字或 `REDRAW`：`SC004-SH007`, `SC005-SH004`, `SC006-SH004`, `SC006-SH007`。
- 直接视频模型不负责精确对白。对白来自 `01/script/final-script.md`，后续进入 audio/post 阶段时再拆成字幕和配音行。

## 风险 / Risks

- 序幕战争与征粮群像容易失控，必须以局部因果和有限参考帧实现。
- 白翳、白册官吏、奴兵、纯虫族小兵的层级若混同，会破坏肃明制度视觉。
- 残阳坳旧井、药屋、检查桌、后山出口的地理若不稳定，SC004-SC006 会失去悬疑逻辑。
- 儿童威胁镜头必须克制，避免直观伤害奇观。

## ComfyUI Handoff Recommendation

中文：先补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/道具/地点参考 IPAdapter node 和 output node 绑定，再按 `SC003-SH001`、`SC003-SH002`、`SC003-SH003`、`SC003-SH004` 做小批量 I2V motion test。`SC003-SH004` 本轮只使用 `r013e01.png` 做转场首镜；如要做 R013 到残阳坳封锁线的 FLF2V，必须先确认或重做正确尾帧，并避免把完整村口画面提前混进密室镜头。

English: First fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/prop/location reference IPAdapter nodes and output node bindings, then run a small I2V motion test batch in the order `SC003-SH001`, `SC003-SH002`, `SC003-SH003`, and `SC003-SH004`. For this pass `SC003-SH004` uses only `r013e01.png` as the transition-start shot; if an R013-to-Canyangao FLF2V pass is needed, approve or rebuild the correct tail frame first and prevent the full village-gate image from blending into the room shot.
