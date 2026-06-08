# 第01集 SC001 ComfyUI Prompt QC

## Scope / 范围

中文：本 QC 覆盖 `01/prompts/comfyui-prompt-brief.md`、`01/prompts/comfyui-style-preset.json`、`01/prompts/comfyui-asset-prompt-pack.json`、`01/prompts/comfyui-shot-prompts.json`、`01/prompts/comfyui-workflow-plan.json`、`01/prompts/comfyui-render-prompts.md`，仅限 `SC001-SH001` 到 `SC001-SH003`。

English: This QC covers `01/prompts/comfyui-prompt-brief.md`, `01/prompts/comfyui-style-preset.json`, `01/prompts/comfyui-asset-prompt-pack.json`, `01/prompts/comfyui-shot-prompts.json`, `01/prompts/comfyui-workflow-plan.json`, and `01/prompts/comfyui-render-prompts.md`, limited to `SC001-SH001` through `SC001-SH003`.

## Result / 结论

中文：SC001 后资产 ComfyUI 交付包结构完整，双语结构化 prompt 字段齐全，并已提供可直接复制到 ComfyUI 节点的 `comfyui-render-prompts.md`。新版 `SC001-SH001` 已改为斜侧攻城升镜，`r001e01.png` 和 `r002e01.png` 已按新版首尾帧构图更新并通过视觉检查；镜头时长已改为 `3.5s / 84 frames @ 24fps`。由于项目未提供具体 ComfyUI 模型和 workflow 配置，三条镜头状态均为 `needs_config`，不是 `ready`。

English: The SC001 post-asset ComfyUI delivery package is structurally complete, bilingual structured prompt fields are present, and `comfyui-render-prompts.md` now provides copy-ready prompt blocks for ComfyUI nodes. The updated `SC001-SH001` now uses a diagonal siege-side lift, and `r001e01.png` plus `r002e01.png` have been updated to the revised first/last-frame compositions and visually checked; the shot duration is now `3.5s / 84 frames @ 24fps`. Because concrete ComfyUI model and workflow configuration is not provided, all three shots remain `needs_config`, not `ready`.

## Shot QC / 镜头 QC

| Shot | Method | Asset Use | Status | Notes |
| --- | --- | --- | --- | --- |
| `SC001-SH001` | `FLF2V, 3.5s / 84f` | `r001e01.png` first frame slot, `r002e01.png` last frame slot, plus `c020m.png`, `c021m.png`, `c020e01.png` loaded into beast reference nodes | `needs_config` | 已改为斜侧攻城升镜；`r001` 为攻城方斜后侧低机位首帧，`r002` 为城头中景偏近尾帧，二者已更新并通过视觉检查。兽族参考图必须接入图片节点，不可只写在 prompt 里。光影为斜侧建立方案：冷白暴雪天光压黑墙剪影、黑墙负补光吞墙面和兽潮大暗面、暗红火线低位反打雪雾、破旗、巨角、骨钟边缘和守军肩线。 |
| `SC001-SH002` | `I2V` | `r003e01.png` first frame, `c024ae01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config` | 冻血、断矛、旧痕可读；兽族参考只作为墙外背景连续性，权重必须低于年轻军户身份参考和 I2V 首帧。光影为身体代价近景方案：冷雪反光进钟裂，黑墙负补光压低人物，远火只留弱暖边，不做大场面火光。 |
| `SC001-SH003` | `I2V` | `r004e01.png` first frame, `c004e01.png` character reference, plus low-weight background `c020m.png`, `c021m.png`, `c020e01.png` beast references | `needs_config` | 薛临墙台词已改为“敌人上来了。”；兽族参考只作为墙外背景连续性，权重必须低于薛临墙身份参考和 I2V 首帧。光影为战场口令中近景方案：半脸入黑墙负补光，远火小面积切出脸、手、旧甲片，雪雾分离枪线和门线。 |

## Asset Format Checks / 资产格式检查

- 中文：`E01_R001`、`E01_R002`、`E01_R003` 和 `E01_R004` 均可作为视频参考帧；`E01_R001` 和 `E01_R002` 已更新为 `SC001-SH001` 的 FLF2V 首尾帧。
- English: `E01_R001`, `E01_R002`, `E01_R003`, and `E01_R004` may be used as video reference frames; `E01_R001` and `E01_R002` have been updated for the `SC001-SH001` FLF2V first/last frames.
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
- 中文：`SC001-SH001` 的首尾帧已经从旧版正面攻城和城外仰拍骨钟修订为“斜侧攻城首帧”和“同侧外墙城头外沿尾帧”；后续 QC 重点转为 FLF2V 运动稳定性和方向连续性，必须拒绝越过墙脊看另一边、城墙两侧都被攻击、后墙厚度变主景或墙内侧出现兽潮。
- English: The `SC001-SH001` first/last frames have been revised from the old frontal siege and exterior upward bone-bell compositions into the diagonal siege first frame and same-side exterior-edge wall-top last frame; follow-up QC should focus on FLF2V motion stability and screen-direction continuity, rejecting any crossing over the wall crown to the opposite side, both-side attack reading, rear-wall thickness as the main subject, or beast attackers inside the wall.
- 中文：史诗光影必须保持真实摄影逻辑，但不能三镜同一种布光。QC 时必须确认“统一摄影语法”只作为编写和检查规则存在，不作为模型可见风格句进入 `positive_prompt`；每条镜头的主光比例、反打强度和暗面面积必须在各自 `光影` 段里体现，并拒绝圣光、魔法光柱、完整发光徽章和过曝 bloom。
- English: Epic lighting must stay grounded in cinematography, but the three shots must not share identical lighting. QC must confirm the unified cinematography grammar exists only as authoring and review guidance, not as a model-visible style sentence inside `positive_prompt`; each shot must express its own key-light balance, counterlight strength and shadow area in its `Lighting` section, while rejecting divine light, magic beams, complete glowing emblems and overexposed bloom.

## Handoff Recommendation / 交付建议

中文：`r001e01.png` 和 `r002e01.png` 已按新版构图更新并通过视觉检查。下一步补齐 `PLACEHOLDER_VIDEO_CHECKPOINT`、`PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`、`PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`、prompt node、image node、人物/兽族参考 IPAdapter node 和 output node 绑定，并按 `SC001-SH001`、`SC001-SH002`、`SC001-SH003` 顺序小批量试渲。第一轮还要看 `SC001-SH001` 在 `3.5s / 84f` 内的空间稳定、骨钟位置、旧痕不发光、尾帧守军连续性、斜侧升镜是否越过墙脊看向另一边、是否把城墙变成两侧被攻击的横墙、是否出现穿墙或 180 度调头、兽族是否保留多兵种多伴生兽，以及三镜光影是否有明确差异。

English: `r001e01.png` and `r002e01.png` have been updated to the revised composition and visually checked. Next, fill `PLACEHOLDER_VIDEO_CHECKPOINT`, `PLACEHOLDER_FLF2V_WORKFLOW_TEMPLATE`, `PLACEHOLDER_I2V_WORKFLOW_TEMPLATE`, prompt node, image node, character/beast reference IPAdapter nodes and output node bindings, and run a small render batch in the order `SC001-SH001`, `SC001-SH002`, `SC001-SH003`. The first render pass should check `SC001-SH001` spatial stability across `3.5s / 84f`, bone bell position, non-glowing old mark, tail-frame defender continuity, whether the diagonal lift crosses over the wall crown to the opposite side, whether the wall reads as attacked from both sides, whether it introduces wall pass-through or 180-degree turns, whether beast forces preserve multiple troop and companion-beast types, and whether the three shots have clear lighting differences.
