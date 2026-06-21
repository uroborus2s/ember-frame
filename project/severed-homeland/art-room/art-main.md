# 《断航故土》美术部当前输出

owner: art-room
last_updated: 2026-06-21
status: blocked_missing_reference_image_alpha_generation_capability

## 当前任务

用户已明确：C001-C026 全角色 / 群像模板的角色母卡必须统一到与沈维桑、晏南枝同级的正式角色生产板标准，并且必须是真透明背景，方便切图和下游合成。

正式输出路径仍遵守导演部角色总卡合同：角色图与角色卡同目录，均在 `director-room/characters/`。当前同名 `c###m.png` 文件为旧包已批准 RGB 参考图，只能作为 Image 1 身份、服装、道具、材质和剪影硬参考；不能再标记为透明 alpha 最终资产。

| scope | status | formal_output_path | required_model_card_standard |
| --- | --- | --- | --- |
| C001-C026 | blocked_missing_generation_capability | `director-room/characters/c001m.png` ... `director-room/characters/c026m.png` | `PROJECT-CHAR-MODEL-SHEET-V2` + `OUT-CHAR-TRANSPARENT-THREEVIEW` |

## 统一角色母卡硬标准

- 画布：PNG，3840 x 2160，项目定义 16:9 角色生产板。
- 背景：`background_policy=transparent_alpha`，`alpha_policy=required`；禁止白底、灰底、中性底或场景底冒充透明。
- 上排：五个全身转面视图，front / three-quarter front / strict side / three-quarter back / back，同一脚底基线、同一身高比例、头手脚完整。
- 中排：六个同脸 / 同物种头部结构表情头像，表情变化不能换骨相、年龄、物种或阶层身份。
- 下排：色板、材质裁切、道具 / 饰物格；不得出现文字标签、箭头、UI、水印。
- 旧包 `c001m.png` 到 `c026m.png` 均只作为生成 Image 1 参考；透明 V2 通过 QC 后才能覆盖正式路径。
- 2026-06-21 已派发四个 V2 批次生成线程；当前本地 Codex worker 缺少合规的“本地参考图作为 Image 1 + 3840x2160 透明 alpha PNG + 本地写回 + 身份 QC”生图通道，因此四批全部记录为 `blocked`，没有覆盖旧图，也没有晋升角色卡状态。

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
