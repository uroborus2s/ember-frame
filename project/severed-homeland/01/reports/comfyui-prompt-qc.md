# 第01集 SC001 ComfyUI Prompt QC

## Scope / 范围

中文：本 QC 覆盖 `01/prompts/comfyui-prompt-brief.md`、`01/prompts/comfyui-style-preset.json`、`01/prompts/comfyui-asset-prompt-pack.json`、`01/prompts/comfyui-shot-prompts.json`、`01/prompts/comfyui-workflow-plan.json`、`01/prompts/comfyui-render-prompts.md`，仅限 `SC001-SH001` 到 `SC001-SH003`。

English: This QC covers `01/prompts/comfyui-prompt-brief.md`, `01/prompts/comfyui-style-preset.json`, `01/prompts/comfyui-asset-prompt-pack.json`, `01/prompts/comfyui-shot-prompts.json`, `01/prompts/comfyui-workflow-plan.json`, and `01/prompts/comfyui-render-prompts.md`, limited to `SC001-SH001` through `SC001-SH003`.

## Result / 结论

中文：SC001 后资产 ComfyUI 交付包结构完整，双语结构化 prompt 字段齐全，并已提供可直接复制到 ComfyUI 节点的 `comfyui-render-prompts.md`。最新 `SC001-SH001` 已从斜侧升到墙头转向，改为墙外正向偏斜前推到第一次撞门震钟；`SC001-SH002` 已废弃年轻军户扶钟构图，改为半倒墙边、武器脱手、旁边骨钟横摆。`r002e01.png` 和 `r003e01.png` 需要按最新构图重生或复核；镜头时长保持 `3.5s / 84 frames @ 24fps`。由于项目未提供具体 ComfyUI 模型和 workflow 配置，三条镜头状态均为 `needs_config`，不是 `ready`。

English: The SC001 post-asset ComfyUI delivery package is structurally complete, bilingual structured prompt fields are present, and `comfyui-render-prompts.md` now provides copy-ready prompt blocks for ComfyUI nodes. The latest `SC001-SH001` has changed from a diagonal lift with wall-top turn into an exterior front-biased push to the first gate-impact bell shock; `SC001-SH002` has dropped the young soldier bracing-the-bell composition and now uses half-collapse beside the wall, dropped weapon and the same bell swinging. `r002e01.png` and `r003e01.png` need regeneration or recheck against the latest compositions; the shot duration remains `3.5s / 84 frames @ 24fps`. Because concrete ComfyUI model and workflow configuration is not provided, all three shots remain `needs_config`, not `ready`.

## Shot QC / 镜头 QC

| Shot | Method | Asset Use | Status | Notes |
| --- | --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `r001e01.png` first frame slot, `r002e01.png` last frame slot, plus `c020m.png`, `c021m.png`, `c020e01.png` loaded into beast reference nodes | `needs_config / needs_frame_recheck` | 已改为墙外正向偏斜前推到第一次撞门震钟；`r001` 应为墙外低机位攻城首帧，`r002` 应为同一墙外方向撞门震钟尾帧。兽族参考图必须接入图片节点，不可只写在 prompt 里。光影修正为：撞门雪雾最亮，冷白/淡金裂云天光切墙体、攻城器械、巨兽和骨钟轮廓，暗红火点只做边缘反打，黑墙负补光保留大暗面，禁止全画面灰黑。 |
| `SC001-SH002` | `I2V` | `r003e01.png` first frame, `c024ae01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config / needs_r003_regeneration` | 旧扶钟构图已废弃。新版 `r003` 必须是年轻军户被撞门余震晃倒、半倒墙边、武器脱手滑进雪泥、旁边同一口骨钟横摆；人物脸半遮，不做正脸表情。光影修正为：撞门方向冷白雪雾反光为亮部中心，裂云冷白/淡金边缘光切钟架、锁链、头盔、肩甲和武器，低位暗红火只勾手指、武器边缘、钟缘和冻血，黑墙负补光压脸和暗面。 |
| `SC001-SH003` | `I2V` | `r004e01.png` first frame, `c004e01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config` | 薛临墙台词已改为“敌人上来了。”；兽族参考只作为墙外背景连续性，权重必须低于薛临墙身份参考和 I2V 首帧。光影为战场口令中近景方案：半脸入黑墙负补光，远火小面积切出脸、手、旧甲片，雪雾分离枪线和门线。 |

## R001 Replacement / R001 替换记录

- 中文：`r001e01.png` 已替换为 `019eac75-d625-7291-bfd7-273ec630f1c3` 最新 fortress_battle_far_view_war_aged_clean_4k 首帧，当前 canonical 分辨率为 4096x1840；被替换的临时 4096x1700 候选版本已归档到 `01/assets/reference-frames/history/r001e01.before-fortress-battle-4k-replace-20260609.png`，源图已保存在 `01/assets/reference-frames/history/r001e01.019eac75-source-fortress-battle-far-view-war-aged-clean-4k-20260609.png`。
- English: `r001e01.png` has been replaced with the latest fortress_battle_far_view_war_aged_clean_4k first frame from `019eac75-d625-7291-bfd7-273ec630f1c3`; the canonical file is now 4096x1840, and the replaced temporary 4096x1700 candidate is archived at `01/assets/reference-frames/history/r001e01.before-fortress-battle-4k-replace-20260609.png`, and the source image is preserved at `01/assets/reference-frames/history/r001e01.019eac75-source-fortress-battle-far-view-war-aged-clean-4k-20260609.png`.

## Asset Format Checks / 资产格式检查

- 中文：`E01_R001`、`E01_R002`、`E01_R003` 和 `E01_R004` 均为视频参考帧槽位；但 `E01_R002` 需复核是否已是撞门震钟尾帧，`E01_R003` 旧扶钟构图已废弃，必须重生后再作为 `SC001-SH002` 首帧。
- English: `E01_R001`, `E01_R002`, `E01_R003`, and `E01_R004` are video reference frame slots; however `E01_R002` must be rechecked as the gate-impact bell-shock tail frame, and the old bracing-the-bell `E01_R003` is superseded and must be regenerated before use as the `SC001-SH002` first frame.
- 中文：`C020/c020m.png`、`C021/c021m.png`、`E01_C020/c020e01.png` 必须作为图片节点接入 beast reference/IPAdapter 分支。ComfyUI 不会从 prompt 文件名自动读取这些图。
- English: `C020/c020m.png`, `C021/c021m.png`, and `E01_C020/c020e01.png` must be connected as image nodes to the beast reference/IPAdapter branch. ComfyUI will not load these images automatically from prompt file names.
- 中文：角色状态卡 `E01_C004`、`E01_C020`、`E01_C024A` 没有被用作 I2V/FLF2V 首帧，只作为身份、材质或 IPAdapter 候选参考。
- English: Character state cards `E01_C004`, `E01_C020`, and `E01_C024A` are not used as I2V/FLF2V first frames; they are only identity, material or IPAdapter candidate references.
- 中文：`E01_P021` 没有被用作视频帧，只作为骨钟、断矛、冻血和旧痕道具参考。
- English: `E01_P021` is not used as a video frame; it is only a prop reference for the bone bell, broken spear, frozen blood and old mark.

## Prompt Copy Checks / 提示词复制检查

- 中文：`comfyui-render-prompts.md` 已为 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 分别提供分段标题版 `positive_prompt_zh`、`negative_prompt_zh`、`positive_prompt_en`、`negative_prompt_en`。
- English: `comfyui-render-prompts.md` provides sectioned `positive_prompt_zh`, `negative_prompt_zh`, `positive_prompt_en`, and `negative_prompt_en` for `SC001-SH001`, `SC001-SH002`, and `SC001-SH003`.
- 中文：正向提示词均包含 `风格 / 目标 / 光影 / 画面内容 / 运镜 / 约束`；负向提示词均包含 `通用负面 / 镜头负面`。
- English: Positive prompts include `Style / Goal / Lighting / Visual Content / Camera / Motion / Constraints`; negative prompts include `Global Negative / Shot Negative`.
- 中文：`comfyui-shot-prompts.json` 仍是结构化源文件；生产侧复制提示词时应使用 Markdown，不要求操作员手动拼 JSON 字段。
- English: `comfyui-shot-prompts.json` remains the structured source file; production should copy prompts from the Markdown file and should not manually concatenate JSON fields.

## Warnings / 警告

- 中文：`01/art/asset-index.json` 与 `01/art/asset-manifest.json` 中 `E01_R001` 到 `E01_R004` 仍保留 `ready_for_image_generation` 旧 metadata；但本地 PNG 文件已存在，本交付包按实际文件可用处理。
- English: `01/art/asset-index.json` and `01/art/asset-manifest.json` still keep old `ready_for_image_generation` metadata for `E01_R001` through `E01_R004`; the local PNG files exist, so this handoff treats the actual files as usable.
- 中文：缺少 ComfyUI checkpoint、LoRA、ControlNet、IPAdapter preset、workflow template 和 node ID，不能标记为生产 ready；其中必须包含兽族参考图分支或 IPAdapter 节点。
- English: ComfyUI checkpoint, LoRA, ControlNet, IPAdapter preset, workflow template and node IDs are missing, so the package cannot be marked production ready; this must include a beast reference or IPAdapter branch.
- 中文：`SC001-SH001` 现已放弃升到墙头转向，改为墙外同方向前推和第一次撞门震钟；后续 QC 必须拒绝 90 度转向、越过墙脊看另一边、城墙两侧都被攻击、后墙厚度变主景或墙内侧出现兽潮。
- English: `SC001-SH001` has dropped the wall-top turn and now uses a same-direction exterior push plus first gate-impact bell shock; follow-up QC must reject 90-degree turns, crossing over the wall crown to the opposite side, both-side attack reading, rear-wall thickness as the main subject, or beast attackers inside the wall.
- 中文：史诗光影必须保持真实摄影逻辑，但不能三镜同一种布光。QC 时必须确认“统一摄影语法”只作为编写和检查规则存在，不作为模型可见风格句进入 `positive_prompt`；每条镜头的主光比例、反打强度和暗面面积必须在各自 `光影` 段里体现，并拒绝圣光、魔法光柱、完整发光徽章和过曝 bloom。
- English: Epic lighting must stay grounded in cinematography, but the three shots must not share identical lighting. QC must confirm the unified cinematography grammar exists only as authoring and review guidance, not as a model-visible style sentence inside `positive_prompt`; each shot must express its own key-light balance, counterlight strength and shadow area in its `Lighting` section, while rejecting divine light, magic beams, complete glowing emblems and overexposed bloom.

## Handoff Recommendation / 交付建议

中文：下一步先按最新方案复核/重生 `r002e01.png` 和 `r003e01.png`，再补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/兽族参考 IPAdapter node 和 output node 绑定，并按 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 顺序小批量试渲。第一轮还要看 `SC001-SH001` 在 `3.5s / 84f` 内的空间稳定、骨钟位置、旧痕不发光、是否仍保持墙外同方向撞门震钟、是否出现 90 度转向或越墙、是否把城墙变成两侧被攻击的横墙、兽族是否保留多兵种多伴生兽，以及三镜是否都有明确亮部中心和主光方向。

English: Next, recheck/regenerate `r002e01.png` and `r003e01.png` according to the latest plan, then fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/beast reference IPAdapter nodes and output node bindings, and run a small render batch in the order `SC001-SH001`, `SC001-SH002`, `SC001-SH003`. The first render pass should check `SC001-SH001` spatial stability across `3.5s / 84f`, bone bell position, non-glowing old mark, whether it still stays in the same exterior gate-impact direction, whether it introduces a 90-degree turn or wall crossing, whether the wall reads as attacked from both sides, whether beast forces preserve multiple troop and companion-beast types, and whether all three shots have a clear highlight center and key-light direction.
