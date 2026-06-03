# 第01集《清明香入村》美术资源 QC 与评分报告

版本：v01  
日期：2026-06-03  
范围：第一集 art-room 标准包、项目级可复用资产、4 张新增服装板、6 张第一集参考帧、1 张 SC008-SH003 shot override。

## 总评

综合评分：**91 / 100，ready with warnings**。

第一集美术资源已经具备 Prompt Room 交接条件：核心角色、服装、残阳坳空间、清明制度道具、昭明旧物、区域色、六张关键参考帧和 SC008-SH003 井沿覆盖帧都有 canonical 文件。主要风险不是缺文件，而是使用边界：沈维桑/沈照眠角色板含后续状态，白册/药牌/木牌/旧驿图不可直接生成可读文字，文字必须后期叠加。

## 分项评分

| 分类 | 评分 | 状态 | 分析 |
| --- | ---: | --- | --- |
| 角色资产 | 90 | ready with warnings | 沈维桑、沈照眠、罗青禾、白翳身份锚点清楚；后续状态必须限制，不进入第一集常规镜头。 |
| 服装资产 | 86 | ready with warnings | 本轮补齐四张第一集服装板，均为 941x1672。部分后续状态只作边界参考。 |
| 场景资产 | 92 | ready | 残阳坳黄昏、村口验血、药屋内外、旧井、暗格均存在，能支撑村口到药屋再到旧井空间连续性。 |
| 道具资产 | 91 | ready | 清明白册、虫蜡针/清明香工具板、旧驿图、半枚日月驿令、沈照眠旧物均可用；文字位必须后期处理。 |
| 风格资产 | 93 | ready | 总风格、区域色、清明制度白、旧昭明材质统一；符号和材质板密度高，prompt 需只取局部。 |
| 参考帧 | 91 | ready | 六张第一集参考帧存在且规格统一；新增 SC002-SH001 首帧补齐沈维桑村口出场 I2V 锁定。 |
| Shot Override | 94 | ready | 新增 SC008-SH003 井沿月白反光可读性覆盖帧，941x1672；月白一线清楚，未展示人物、手或完整玉片。 |
| 路径与版本卫生 | 95 | ready | 未发现 v1/v2/versions/drafts 目录；history 文件位于 sibling history 目录，canonical 路径不带版本号。 |
| 追踪性 | 94 | ready | asset-manifest、art-image-prompts、thread-plan、thread-results、asset-index 已建立追踪链路。 |

## 本轮新增图片

- assets/costumes/costume_shen_weisang_states.png：941x1672，第一集使用猎户状态；火后/雪线状态仅作后续边界。
- assets/costumes/costume_shen_zhaomian_states.png：941x1672，第一集使用村童状态；清明白衣为后续威胁状态。
- assets/costumes/costume_luo_qinghe_states.png：941x1672，药屋医者服装、头巾、药篮、腰间工具清楚。
- assets/costumes/costume_bai_yi_states.png：941x1672，清明监察使白色官制、膜翼、虫蜡针和白册参考成立。
- 01/assets/reference-frames/sc002_sh001_shen_weisang_gate_observation.png：941x1672，SC002-SH001 首帧；沈维桑第一集猎户状态、人群遮挡和村口验血环境成立。
- 01/assets/shot-overrides/sc008_sh003_well_glint_readability_override.png：941x1672，SC008-SH003 优先覆盖帧；井沿、清明香、月白反光可读性明显提升。

## 关键问题

1. SC002-SH001 使用边界：首帧只锁定沈维桑第一集猎户状态，不得混入角色板中的发光裂纹、火后状态或雪线披风。
2. SC008 使用边界：原 reference frame 只作封锁线和空间气氛参考；SC008-SH003 必须优先使用新增 shot override。
3. 文字不可直接依赖生成：白册“旧污疑似”、药名牌、征粮木牌、旧驿图地名都应由后期文字层控制，图像资产只提供留白和材质承载面。
4. 后续状态混入风险：角色板和服装板是多状态板，第一集镜头必须明确只取沈维桑猎户状态、沈照眠村童状态、罗青禾药屋状态、白翳巡检状态。
5. 晏南枝/玉片揭示风险：第一集只允许井下声音和月白一线反光，不允许完整人物、手、玉片或身份物。

## 交接建议

Prompt Room 可以接手。建议优先使用 01/art/asset-manifest.json 与 01/prompts/art-image-prompts.json 作为第一集美术资产索引，再按 01/production/generation-plan.json 的五个 production group 生成 ComfyUI-ready 镜头提示词。
