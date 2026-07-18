# 《断航故土》美术部当前输出

owner: art-room
last_updated: 2026-06-21
status: g-p_hard_reference_frame_briefs_ready_image_generation_blocked

## 当前任务

### 第 01 集 G-P 分镜开拍前置美术命令

status: character_card_gate_pending_formal_reference_frames
source: `director-room/season-01/01/G-P/`

总导演已签署 G-P/P-01 至 P-05。美术部现在启动五个镜头的首轮视觉资产和参考帧准备，先做“可拍、可控、可交给提示词和视频”的资产，不追求孤立漂亮图。

| 分镜 | 美术任务 | 必须锁定 |
|---|---|---|
| P-01 | 黑石边墙、骨钟、紧闭粮门、床弩、少年军户流血手部参考 | 门外冲击、墙上军户、门内粮袋三层关系 |
| P-02 | 灶屋、冬粮急调木牌、虫蜡手印板、黑铁环、麦粒泥水特写 | 征粮不是普通抢劫，必须看见册、牌、虫蜡 |
| P-03 | 清明院白墙、儿童队列、虫蜡针、识字木牌、母亲贴墙侧近景 | 干净造成恐惧，血腥不能盖过验声流程 |
| P-04 | 红线密室、黑匣裂口、日月血牒残纹、旧驿残图、白翳半身参考 | 晏南枝动、白翳静，追杀冷净不怪物化 |
| P-05 | 残阳坳北坡、沈维桑下坡、两只灰兔、村口、绕沟小路、封路矛尖 | 冷开压力落到山坳日常，兔血、铜锣、封路矛尖都要在 |

输出要求：先回填每个分镜文档 `## 2. 美术资产区` 的资产清单、参考帧需求、控制图需求和 QC 标准；最终导演认可图片再回到对应 `{shot-id}.png`。

### 2026-06-21 G-P/P-01 至 P-05 美术参考帧需求回填

status: art_reference_plan_ready

已完成第一版文字回填：P-01 至 P-05 的 `## 2. 美术资产区` 均已补齐参考帧目标、必需资产/场景/道具清单、首帧/控制图/构图需求、不能漂移项和美术 QC 通过/失败标准。本轮未生成真实图片、未创建二进制资产；下一步可交提示词部按各分镜美术区刷新图片/视频提示词。

### 2026-06-21 G-P/P-01 至 P-05 候选参考帧与控制图

status: composition_candidates_only_formal_frames_withdrawn_pending_character_card_gate

总导演更正裁决：角色卡是 G-P 正式参考帧的第一闸门。此前五张画面没有把 `director-room/characters/` 的角色母图作为硬参考输入，只能保留为构图 / 气氛候选；正式 `P-01.png` 至 `P-05.png` 已从分镜目录撤回。五张 control-only SVG 可继续作为空间、身高、站位、运动线和背景锚点草图，但下一轮正式帧必须绑定角色卡视觉母图重新生成 / 合成并重新 QC。

| 分镜 | 候选图版本库 | 控制图 | 导演裁决 |
|---|---|---|---|
| P-01 | `art-room/.work/asset-versions/P-01-reference-frame/` | `director-room/season-01/01/G-P/P-01/assets/control/p01top.svg` | 候选图撤回正式资格；需用 C024/C021/NAR001 角色卡和声音闸门重做 |
| P-02 | `art-room/.work/asset-versions/P-02-reference-frame/` | `director-room/season-01/01/G-P/P-02/assets/control/p02top.svg` | 候选图撤回正式资格；需用 C016/C017/C025 角色卡和身高比例链重做 |
| P-03 | `art-room/.work/asset-versions/P-03-reference-frame/` | `director-room/season-01/01/G-P/P-03/assets/control/p03block.svg` | 候选图撤回正式资格；需先锁 C025 儿童旧歌和声音，再重做 |
| P-04 | `art-room/.work/asset-versions/P-04-reference-frame/` | `director-room/season-01/01/G-P/P-04/assets/control/p04top.svg` | 候选图撤回正式资格；需用 C002/C007 角色卡重做并补 C007 声音 |
| P-05 | `art-room/.work/asset-versions/P-05-reference-frame/` | `director-room/season-01/01/G-P/P-05/assets/control/p05top.svg` | 候选图撤回正式资格；需用 C001/C025 角色卡重做并补声效 |

隐藏版本库：`.work/asset-versions/P-01-reference-frame/` 至 `.work/asset-versions/P-05-reference-frame/`。正式帧不在对应分镜目录；Codex 默认生成原图保留在用户 `.codex/generated_images/` 下。

用户已明确：C001-C026 全角色 / 群像模板的角色母卡必须统一到与沈维桑、晏南枝同级的正式角色生产板标准，并且必须是真透明背景，方便切图和下游合成。

正式输出路径仍遵守导演部角色总卡合同：角色图与角色卡同目录，均在 `director-room/characters/`。本次 G-P 直接相关的 C001、C002、C007、C016、C017、C021、C024、C025 已复核为 3840x2160 RGBA alpha V2 角色生产板，可作为下一轮正式参考帧硬身份输入；C007/C016/C017/C024/C025 已补声音母卡 v001 并生成 24 kHz preview，但仍需人工听审和最终音频确认；C021 仍待分层兽类声效资产。

| scope | status | formal_output_path | required_model_card_standard |
| --- | --- | --- | --- |
| G-P direct characters | visual_ready_voice_gate_pending | `director-room/characters/c001m.png`, `c002m.png`, `c007m.png`, `c016m.png`, `c017m.png`, `c021m.png`, `c024m.png`, `c025m.png` | `PROJECT-CHAR-MODEL-SHEET-V2` + `OUT-CHAR-TRANSPARENT-THREEVIEW` |

### 2026-06-21 G-P/P-01 至 P-05 角色卡硬参考正式帧重制 brief

status: blocked_image_generation_unavailable_briefs_ready

本轮已读取导演签署区、角色卡限制、美术资产区、导演回看区、角色总卡索引和 C001/C002/C007/C016/C017/C021/C024/C025 角色卡；八张角色母图均复核为 3840x2160 RGBA alpha，可作为硬 identity / scale / costume reference。当前 worker 无法把这些本地角色母图作为硬参考输入图像生成链路并写回 4K 正式帧，因此未生成、未覆盖、未晋升任何 `P-01.png` 至 `P-05.png`。

| 分镜 | brief | manifest | image generation status | formal frame |
|---|---|---|---|---|
| P-01 | `art-room/.work/asset-versions/P-01-reference-frame/image-generation-brief.md` | `art-room/.work/asset-versions/P-01-reference-frame/manifest.jsonl` | `blocked_image_generation_unavailable` | not_generated |
| P-02 | `art-room/.work/asset-versions/P-02-reference-frame/image-generation-brief.md` | `art-room/.work/asset-versions/P-02-reference-frame/manifest.jsonl` | `blocked_image_generation_unavailable` | not_generated |
| P-03 | `art-room/.work/asset-versions/P-03-reference-frame/image-generation-brief.md` | `art-room/.work/asset-versions/P-03-reference-frame/manifest.jsonl` | `blocked_image_generation_unavailable` | not_generated |
| P-04 | `art-room/.work/asset-versions/P-04-reference-frame/image-generation-brief.md` | `art-room/.work/asset-versions/P-04-reference-frame/manifest.jsonl` | `blocked_image_generation_unavailable` | not_generated |
| P-05 | `art-room/.work/asset-versions/P-05-reference-frame/image-generation-brief.md` | `art-room/.work/asset-versions/P-05-reference-frame/manifest.jsonl` | `blocked_image_generation_unavailable` | not_generated |

总导演审核请求：请派发具备本地图片 reference 绑定、结构 SVG 控制和指定路径写回能力的图像线程，逐镜按 brief 生成候选图；通过美术自检后再晋升到 `director-room/season-01/01/G-P/P-XX/P-XX.png`。旧候选图只允许作为 composition mood，不得作为 identity 或正式首帧。

## 统一角色母卡硬标准

- 画布：PNG，3840 x 2160，项目定义 16:9 角色生产板。
- 背景：`background_policy=transparent_alpha`，`alpha_policy=required`；禁止白底、灰底、中性底或场景底冒充透明。
- 上排：五个全身转面视图，front / three-quarter front / strict side / three-quarter back / back，同一脚底基线、同一身高比例、头手脚完整。
- 中排：六个同脸 / 同物种头部结构表情头像，表情变化不能换骨相、年龄、物种或阶层身份。
- 下排：色板、材质裁切、道具 / 饰物格；不得出现文字标签、箭头、UI、水印。
- 旧包图片如需继续使用，只作为 identity / costume / prop / material / silhouette reference；透明 V2 通过 QC 后才能覆盖正式路径。
- 2026-06-21 复核：G-P 直接相关角色母图已具备透明 V2 视觉条件；正式分镜图仍必须在生成 / 合成时实际使用这些角色母图作为硬参考，不能用未绑定角色卡的候选图冒充。

## 阵营旗帜徽章锁定

- 2026-06-21 已从下载目录旧包导入三张已批准根资产，作为后续所有阵营徽章和旗帜的硬基础：昭明 `P016`、肃明/清明 `P017`、北境万兽/兽族联盟 `P018`。
- 三张根资产不得重画、重设计、替换图形结构或让模型自由发明变体；涉及这三个势力的旗帜、徽章、服饰纹样、封条、石刻、旗号和后合成叠加层，都必须从对应根资产派生。
- 当前旧包只提供中性背景 RGB 母版卡；后续新做的独立旗帜、徽章、线控层、抠图层或后合成 overlay 必须使用透明背景 PNG/SVG：`background_policy=transparent_alpha`，`alpha_policy=required`，`annotation_policy=forbidden`。
- 正式公共资产：
  - `art-room/shared-assets/props/p016m.png`
  - `art-room/shared-assets/props/p017m.png`
  - `art-room/shared-assets/props/p018m.png`

## 过程记录

- 资产准备计划：`.work/asset-prep-plan.md`
- 资产清单：`.work/asset-manifest.json`
- 图片提示词：角色卡 `Section 3` 为正式入口；`.work/art-image-prompts.json` 为机器可读追溯副本
- 线程计划：`.work/thread-plan.json`
- 线程结果索引：`.work/thread-results/thread-results-index.json`
- 隐藏版本库：`.work/asset-versions/`
- QC 报告：`.work/asset-qc-report.md`
