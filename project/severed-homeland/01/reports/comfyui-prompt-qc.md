# 第01集 SC001-SC003 ComfyUI Prompt QC

## Scope / 范围

中文：本 QC 覆盖 `01/prompts/comfyui-prompt-brief.md`、`01/prompts/comfyui-style-preset.json`、`01/prompts/comfyui-asset-prompt-pack.json`、`01/prompts/comfyui-shot-prompts.json`、`01/prompts/comfyui-workflow-plan.json`、`01/prompts/comfyui-render-prompts.md`，范围为 `SC001-SH001` 到 `SC001-SH003`、`SC002-SH001` 到 `SC002-SH004` 以及 `SC003-SH001` 到 `SC003-SH004`。

English: This QC covers `01/prompts/comfyui-prompt-brief.md`, `01/prompts/comfyui-style-preset.json`, `01/prompts/comfyui-asset-prompt-pack.json`, `01/prompts/comfyui-shot-prompts.json`, `01/prompts/comfyui-workflow-plan.json`, and `01/prompts/comfyui-render-prompts.md`, covering `SC001-SH001` through `SC001-SH003`, `SC002-SH001` through `SC002-SH004`, and `SC003-SH001` through `SC003-SH004`.

## Result / 结论

中文：SC001-SC003 后资产 ComfyUI 交付包结构完整，双语结构化 prompt 字段齐全，并已提供可直接复制到 ComfyUI 节点的 `comfyui-render-prompts.md`。最新 `SC001-SH001` 已从斜侧升到墙头转向，改为墙外正中对称史诗前推到第一次撞门；骨钟在门楼内，只作为钟声存在，第一镜不要求画面露出骨钟或同一钟架。`SC001-SH002` 已废弃年轻军户扶钟构图，改为半倒墙边、武器脱手、旁边骨钟横摆。`SC002-SH001` 到 `SC002-SH004` 已补齐构图、运镜和逐镜头光线。`SC003-SH001` 到 `SC003-SH004` 已按本轮要求优化视频/I2V 提示词、逐秒动作说明、运镜约束和负面运动/光线约束；R010-R013 已通过高分视觉 QC，可进入 I2V motion test 准备。由于项目未提供具体 ComfyUI 模型和 workflow 配置，所有已覆盖镜头仍不是 `ready`；SC002 的 R005-R009 仍需用户视觉 QC，SC003 下一步是配置补齐和 motion QC。

English: The SC001-SC003 post-asset ComfyUI delivery package is structurally complete, bilingual structured prompt fields are present, and `comfyui-render-prompts.md` provides copy-ready prompt blocks for ComfyUI nodes. The latest `SC001-SH001` has changed from a diagonal lift with wall-top turn into a centered exterior epic push to the first gate impact; the bone bell is inside the gatehouse and exists as sound only, with no on-screen bell or same bell frame required in the first shot. `SC001-SH002` has dropped the young soldier bracing-the-bell composition and now uses half-collapse beside the wall, dropped weapon and the same bell swinging. `SC002-SH001` through `SC002-SH004` now include completed composition, camera movement and shot-specific lighting. `SC003-SH001` through `SC003-SH004` have now been optimized for video/I2V prompts, beat-by-beat action instructions, camera constraints and negative motion/lighting constraints; R010-R013 have passed high-score visual QC and can enter I2V motion-test setup. Because concrete ComfyUI model and workflow configuration is not provided, covered shots are not `ready`; SC002 R005-R009 still require user visual QC, and SC003 next needs configuration plus motion QC.

## Shot QC / 镜头 QC

| Shot | Method | Asset Use | Status | Notes |
| --- | --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `r001e01.png` first frame slot, `r002e01.png` last frame slot, plus `c020m.png`, `c021m.png`, `c020e01.png`, `p017m.png` loaded into beast / flag reference nodes | `needs_config / r002_static_frame_approved` | 已改为墙外正中对称史诗前推到第一次撞门；`r001` 当前风格通过，`r002` 已正式替换为更近城门、更强第一次撞门、P017 肃明虫族帝国旗正确的 4096x2304 尾帧。墙上守城旗帜必须继承 `P017` 肃明虫族帝国黑日白翅旗帜，禁止通用人族旗和随机徽章。骨钟在门楼内，只需要钟声，不要求画面露出骨钟或同一钟架。兽族参考图必须接入图片节点，不可只写在 prompt 里。光影修正为：撞门雪雾和碎屑最亮，冷白/淡金裂云天光切墙体、攻城器械、巨兽和城门轮廓，暗红火点只做边缘反打，黑墙负补光保留大暗面，禁止全画面灰黑。 |
| `SC001-SH002` | `I2V` | `r003e01.png` first frame, `c024ae01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config / needs_r003_regeneration` | 旧扶钟构图已废弃。新版 `r003` 必须是年轻军户被撞门余震晃倒、半倒墙边、武器脱手滑进雪泥、旁边同一口骨钟横摆；人物脸半遮，不做正脸表情。光影修正为：撞门方向冷白雪雾反光为亮部中心，裂云冷白/淡金边缘光切钟架、锁链、头盔、肩甲和武器，低位暗红火只勾手指、武器边缘、钟缘和冻血，黑墙负补光压脸和暗面。 |
| `SC001-SH003` | `I2V` | `r004e01.png` first frame, `c004e01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config` | 薛临墙台词已改为“敌人上来了。”；兽族参考只作为墙外背景连续性，权重必须低于薛临墙身份参考和 I2V 首帧。光影为战场口令中近景方案：半脸入黑墙负补光，远火小面积切出脸、手、旧甲片，雪雾分离枪线和门线。 |
| `SC002-SH001` | `I2V, 6s / 144f` | `r005e01.png` first frame, `c016be01.png`, `l003e01.png`, `p003e01.png`, `p008e01.png` as support references | `needs_config / pending_user_visual_qc` | 构图为粮袋墙上压、小吏高位、村民低位、押车通道退进；光线为柔和清晨冷雾、低角逆光、窄侧光和克制丁达尔纵深。 |
| `SC002-SH002` | `I2V, 7s / 168f` | `r006e01.png` first frame, `c017e01.png`, `p008e01.png` as support references | `needs_config / pending_user_visual_qc` | 门槛斜线构图已补齐，儿童威胁克制；光线为门槛侧光强化材质，小面积虫蜡顶光压封条，底光只允许泥水极弱反光。 |
| `SC002-SH003` | `I2V, 7s / 168f` | `r007e01.png` first frame, `c016be01.png`, `c017e01.png`, `p003e01.png`, `p008e01.png` as support references | `needs_config / pending_user_visual_qc` | 三层构图已锁定：白册证据前景、小吏/妇人/奴兵中景、粮袋墙背景；光线为虫蜡顶光压制度，侧光读手、皮肤、旧木、麻袋和皮甲，小硬光只给封牌落点。 |
| `SC002-SH004` | `FLF2V, 8s / 192f` | `r008e01.png` first frame, `r009e01.png` last frame, `c017e01.png`, `p008e01.png` as support references | `needs_config / pending_user_visual_qc` | 首尾帧同一门槛：粮袋拖上车到空门槛；光线为清晨逆光切押车空气感，侧光擦车辙、泥水、祖牌盒和麻袋，家人只吃柔光。 |
| `SC003-SH001` | `I2V, 7s / 168f` | `r010e01.png` approved primary I2V frame; `l014e01.png`, `p009e01.png` support references | `needs_config_motion_test` | 桌面红线构图已锁定：南缘下方、北境上方、朱赤红线斜穿三分线；光线为左下低位油灯擦纸/线/铜/湿木，右上雨夜月白冷反光点水滴和油布。 |
| `SC003-SH002` | `I2V, 8s / 192f` | `r011e01.png` approved primary I2V frame; `c011e01.png`, `c002e01.png`, `p002e01.png` support references | `needs_config_motion_test` | 红线分割顾怀章和晏南枝；暖灯只给顾怀章侧，月白玉片窄冷光只勾晏南枝指节、面纱边和下颌线，不揭全脸。 |
| `SC003-SH003` | `I2V, 9s / 216f` | `r012e01.png` approved primary I2V frame; `p002e01.png`, `p009e01.png`, `c002e01.png`, `c011e01.png` support references | `needs_config_motion_test` | 手部插入特写已锁定一指宽未接触空隙；血牒只做残缺旧证据，禁止圣旨光效和随机可读文字。 |
| `SC003-SH004` | `I2V, 9s / 216f` | `r013e01.png` approved primary transition-start I2V frame; `r014e01.png` optional later match target only | `needs_config_motion_test_optional_match_target` | 红线北端匹配残阳坳封锁线；暖暗转土褐与虫蜡冷白，冷白只作封锁信息，不做圣光或皇座幻象。 |

## R001 Replacement / R001 替换记录

- 中文：`r001e01.png` 已替换为 `019eac75-d625-7291-bfd7-273ec630f1c3` 最新 fortress_battle_far_view_war_aged_clean_4k 首帧，当前 canonical 分辨率为 4096x1840；被替换的临时 4096x1700 候选版本已归档到 `01/assets/reference-frames/history/r001e01.before-fortress-battle-4k-replace-20260609.png`，源图已保存在 `01/assets/reference-frames/history/r001e01.019eac75-source-fortress-battle-far-view-war-aged-clean-4k-20260609.png`。
- English: `r001e01.png` has been replaced with the latest fortress_battle_far_view_war_aged_clean_4k first frame from `019eac75-d625-7291-bfd7-273ec630f1c3`; the canonical file is now 4096x1840, and the replaced temporary 4096x1700 candidate is archived at `01/assets/reference-frames/history/r001e01.before-fortress-battle-4k-replace-20260609.png`, and the source image is preserved at `01/assets/reference-frames/history/r001e01.019eac75-source-fortress-battle-far-view-war-aged-clean-4k-20260609.png`.

## Asset Format Checks / 资产格式检查

- 中文：`E01_R001`、`E01_R002`、`E01_R003` 和 `E01_R004` 均为视频参考帧槽位；`E01_R001` 当前墙外正中对称史诗风格通过，`E01_R002` 的 canonical `r002e01.png` 已正式替换为更近城门、更强第一次撞门且旗帜改为 P017 肃明虫族帝国旗的 4096x2304 尾帧；第一镜不因骨钟或钟架不可见判退。`E01_R003` 旧扶钟构图已废弃，必须重生后再作为 `SC001-SH002` 首帧。
- English: `E01_R001`, `E01_R002`, `E01_R003`, and `E01_R004` are video reference frame slots; `E01_R001` passes with the current centered exterior epic style, while canonical `r002e01.png` for `E01_R002` has been formally replaced with a 4096x2304 closer-gate, stronger first-impact tail frame with corrected P017 Suming insect empire flags. The first shot is not rejected for an invisible bell or bell frame. The old bracing-the-bell `E01_R003` is superseded and must be regenerated before use as the `SC001-SH002` first frame.
- 中文：`C020/c020m.png`、`C021/c021m.png`、`E01_C020/c020e01.png` 必须作为图片节点接入 beast reference/IPAdapter 分支。ComfyUI 不会从 prompt 文件名自动读取这些图。
- English: `C020/c020m.png`, `C021/c021m.png`, and `E01_C020/c020e01.png` must be connected as image nodes to the beast reference/IPAdapter branch. ComfyUI will not load these images automatically from prompt file names.
- 中文：角色状态卡 `E01_C004`、`E01_C020`、`E01_C024A` 没有被用作 I2V/FLF2V 首帧，只作为身份、材质或 IPAdapter 候选参考。
- English: Character state cards `E01_C004`, `E01_C020`, and `E01_C024A` are not used as I2V/FLF2V first frames; they are only identity, material or IPAdapter candidate references.
- 中文：`E01_P021` 没有被用作视频帧，只作为骨钟、断矛、冻血和旧痕道具参考。
- English: `E01_P021` is not used as a video frame; it is only a prop reference for the bone bell, broken spear, frozen blood and old mark.
- 中文：`E01_R010` 到 `E01_R013` 是已通过高分复评的 SC003 主 I2V 视频参考帧；`E01_R014` 只作为残阳坳封锁线匹配目标保留。`c002e01/c011e01/l014e01/p002e01/p009e01` 只能作支持参考，不能替代主视频帧。
- English: `E01_R010` through `E01_R013` are the high-score approved SC003 primary I2V video reference frames; `E01_R014` is retained only as the Canyangao blockade match target. `c002e01/c011e01/l014e01/p002e01/p009e01` are support references only and must not replace primary video frames.

## Prompt Copy Checks / 提示词复制检查

- 中文：`comfyui-render-prompts.md` 已为 `SC001-SH001` 到 `SC001-SH003`、`SC002-SH001` 到 `SC002-SH004` 以及 `SC003-SH001` 到 `SC003-SH004` 分别提供分段标题版 `positive_prompt_zh`、`negative_prompt_zh`、`positive_prompt_en`、`negative_prompt_en`。
- English: `comfyui-render-prompts.md` provides sectioned `positive_prompt_zh`, `negative_prompt_zh`, `positive_prompt_en`, and `negative_prompt_en` for `SC001-SH001` through `SC001-SH003`, `SC002-SH001` through `SC002-SH004`, and `SC003-SH001` through `SC003-SH004`.
- 中文：正向提示词均包含 `风格 / 目标 / 光影 / 画面内容 / 运镜 / 约束`；负向提示词均包含 `通用负面 / 镜头负面`。
- English: Positive prompts include `Style / Goal / Lighting / Visual Content / Camera / Motion / Constraints`; negative prompts include `Global Negative / Shot Negative`.
- 中文：`comfyui-shot-prompts.json` 仍是结构化源文件；生产侧复制提示词时应使用 Markdown，不要求操作员手动拼 JSON 字段。
- English: `comfyui-shot-prompts.json` remains the structured source file; production should copy prompts from the Markdown file and should not manually concatenate JSON fields.

## Warnings / 警告

- 中文：`01/art/asset-index.json` 与 `01/art/asset-manifest.json` 中 `E01_R001` 到 `E01_R004` 仍保留 `ready_for_image_generation` 旧 metadata；但本地 PNG 文件已存在，本交付包按实际文件可用处理。
- English: `01/art/asset-index.json` and `01/art/asset-manifest.json` still keep old `ready_for_image_generation` metadata for `E01_R001` through `E01_R004`; the local PNG files exist, so this handoff treats the actual files as usable.
- 中文：缺少 ComfyUI checkpoint、LoRA、ControlNet、IPAdapter preset、workflow template 和 node ID，不能标记为生产 ready；其中必须包含兽族参考图分支或 IPAdapter 节点。
- English: ComfyUI checkpoint, LoRA, ControlNet, IPAdapter preset, workflow template and node IDs are missing, so the package cannot be marked production ready; this must include a beast reference or IPAdapter branch.
- 中文：`SC002` 的 R005-R009 参考帧是 generated candidates，已可用于提示词绑定，但需要用户视觉 QC 后才能作为 final approved 帧进入正式渲染。
- English: SC002 R005-R009 reference frames are generated candidates and can be used for prompt binding, but require user visual QC before they become final approved frames for production rendering.
- 中文：`SC003` 的 R010-R013 已完成高分视觉 QC，但仍缺 ComfyUI 模型、workflow template 和节点绑定；正式渲染前必须先做小批量 I2V motion QC。
- English: SC003 R010-R013 have completed high-score visual QC, but ComfyUI model, workflow template and node bindings are still missing; before formal rendering, run a small I2V motion QC batch.
- 中文：`SC001-SH001` 现已放弃升到墙头转向，改为墙外同方向正中对称前推和第一次撞门；门楼内钟声保留，画面不强制露钟。后续 QC 必须拒绝 90 度转向、越过墙脊看另一边、城墙两侧都被攻击、后墙厚度变主景或墙内侧出现兽潮，但不得再因“正中对称”或“骨钟不可见”判退第一镜。
- English: `SC001-SH001` has dropped the wall-top turn and now uses a same-direction centered exterior push plus first gate impact; gatehouse bell sound remains, with no on-screen bell required. Follow-up QC must reject 90-degree turns, crossing over the wall crown to the opposite side, both-side attack reading, rear-wall thickness as the main subject, or beast attackers inside the wall, but must no longer reject the first shot for centered symmetry or an invisible bell.
- 中文：史诗光影必须保持真实摄影逻辑，但不能三镜同一种布光。QC 时必须确认“统一摄影语法”只作为编写和检查规则存在，不作为模型可见风格句进入 `positive_prompt`；每条镜头的主光比例、反打强度和暗面面积必须在各自 `光影` 段里体现，并拒绝圣光、魔法光柱、完整发光徽章和过曝 bloom。
- English: Epic lighting must stay grounded in cinematography, but the three shots must not share identical lighting. QC must confirm the unified cinematography grammar exists only as authoring and review guidance, not as a model-visible style sentence inside `positive_prompt`; each shot must express its own key-light balance, counterlight strength and shadow area in its `Lighting` section, while rejecting divine light, magic beams, complete glowing emblems and overexposed bloom.

## Handoff Recommendation / 交付建议

中文：下一步先补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/道具/地点参考 IPAdapter node 和 output node 绑定，然后按 `SC003-SH001` 到 `SC003-SH004` 做小批量 I2V motion test。重点 QC：红线方向不漂移、SH002 不揭全脸、SH003 一指宽空隙不消失、SH004 不提前混入完整村口画面。

English: Next, fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/prop/location reference IPAdapter nodes and output node bindings, then run a small I2V motion test from `SC003-SH001` through `SC003-SH004`. QC focus: red-cord direction does not drift, SH002 does not reveal the full face, SH003 one-finger gap does not disappear, and SH004 does not blend in a full village-gate image early.
