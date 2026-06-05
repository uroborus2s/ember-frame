# 第01集《白册进村》资产拆解计划

## 状态

- 审批状态：`pending_user_art_approval`
- 图片生成：`not_started_pending_user_approval`
- 当前只预留 canonical output path，不创建图片文件。
- 合同修复：已补齐 `creation_order`、`creation_phase`、`depends_on_assets`、`blocks_assets`、`dependency_reason`、`priority` 和 `output_format`。

## 图片资产格式合同

- 角色、道具、服装和风格/地点资产卡不是最终视频帧：使用中性纯背景或资产板布局，不允许透明背景替代 cutout。
- 可复用角色卡必须明确多视图、细节裁切和尺度参考；道具/服装卡必须明确多角度、材质厚度、损伤/标记细节和手持/身体尺度。
- 精确白册、血牒、旧驿暗号、旗帜、印记和文字类痕迹必须保留线控/遮罩/后合成策略，不让模型随机造字或造徽记。
- 视频参考帧和 shot override 必须是 16:9、`background_policy=video_frame`、`alpha_policy=forbidden`，且明确前景、中景、背景、机位、光照、天气/时间和动作状态。

## 资产分层

1. 风格参考先行：`E01_F001`、`E01_F005`、`E01_F006` 锁定第01集材质、竖屏构图、低魔和精确符号边界。
2. 分集状态卡：角色、地点、道具和服装状态卡依赖全剧 master asset ID 与第01集风格板。
3. 精确资产：白册、血牒、旧驿暗号、虫蜡针、白蜡旗、药柜暗格和 shot override 先标记线控/遮罩/后合成策略。
4. 镜头参考帧：每个参考帧按同一 shot 的角色、地点、道具、服装与风格依赖生成。

## 统计

| creation_phase | 数量 |
| --- | ---: |
| style_reference | 3 |
| episode_state_cards | 30 |
| precision_assets | 6 |
| reference_frames | 40 |
| shot_overrides | 4 |

## 批次

| 批次                       | 类型               | 创建顺序 | 依赖批次                                                                         | 状态                            |
| ------------------------ | ---------------- | ---: | ---------------------------------------------------------------------------- | ----------------------------- |
| B04_E01_STYLE            | style            |    1 | -                                                                            | blocked_pending_user_approval |
| B01_E01_CHARACTERS       | characters       |    2 | B04_E01_STYLE                                                                | blocked_pending_user_approval |
| B02_E01_LOCATIONS        | locations        |    3 | B04_E01_STYLE                                                                | blocked_pending_user_approval |
| B03_E01_PROPS_COSTUMES   | props-costumes   |    4 | B04_E01_STYLE                                                                | blocked_pending_user_approval |
| B05_E01_REFERENCE_FRAMES | reference-frames |    5 | B01_E01_CHARACTERS, B02_E01_LOCATIONS, B03_E01_PROPS_COSTUMES, B04_E01_STYLE | blocked_pending_user_approval |
| B06_E01_SHOT_OVERRIDES   | reference-frames |    6 | B03_E01_PROPS_COSTUMES, B04_E01_STYLE, B05_E01_REFERENCE_FRAMES              | blocked_pending_user_approval |

## 资产创建顺序、依赖与输出格式

| Order | Asset ID | Subtype | Phase | Deliverable | Ratio | Background | Alpha | Depends On | Priority |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | E01_F001 | style_reference | style_reference | style_reference_board | 1:1 | style_board_layout | forbidden | F001 | high |
| 2 | E01_F005 | style_reference | style_reference | style_reference_board | 1:1 | style_board_layout | forbidden | F005 | high |
| 3 | E01_F006 | style_reference | style_reference | style_reference_board | 1:1 | style_board_layout | forbidden | F006 | high |
| 4 | E01_C001 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C001 | high |
| 5 | E01_C002 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C002 | high |
| 6 | E01_C004 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C004 | medium |
| 7 | E01_C005 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C005 | high |
| 8 | E01_C006 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C006 | high |
| 9 | E01_C007 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C007 | high |
| 10 | E01_C011 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C011 | medium |
| 11 | E01_C016A | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C016 | medium |
| 12 | E01_C016B | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C016 | medium |
| 13 | E01_C017 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C017 | medium |
| 14 | E01_C018 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C018 | medium |
| 15 | E01_C020 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, C020 | medium |
| 16 | E01_C022 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001 | medium |
| 17 | E01_C023 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001 | medium |
| 18 | E01_C024 | character_episode_state_card | episode_state_cards | character_episode_state_turnaround_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001 | medium |
| 19 | E01_L007 | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L007 | medium |
| 20 | E01_L003 | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L003 | medium |
| 21 | E01_L014 | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L014 | medium |
| 22 | E01_L001A | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L001 | high |
| 23 | E01_L001B | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L001 | high |
| 24 | E01_L001C | location_episode_scene_card | episode_state_cards | location_episode_scene_card_with_zone_diagram | 3:2 | scene_card_not_final_video_frame | forbidden | E01_F001, E01_F005, L001 | high |
| 25 | E01_P016 | prop_episode_state_card | episode_state_cards | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001 | medium |
| 26 | E01_P008 | prop_episode_state_card | episode_state_cards | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, P008 | medium |
| 27 | E01_P005 | prop_episode_state_card | episode_state_cards | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, P005 | medium |
| 28 | E01_P020 | prop_episode_state_card | episode_state_cards | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001 | medium |
| 29 | E01_K001 | prop_episode_state_card | episode_state_cards | costume_state_turnaround_and_detail_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, K001 | medium |
| 30 | E01_K002 | prop_episode_state_card | episode_state_cards | costume_state_turnaround_and_detail_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, K002 | medium |
| 31 | E01_K003 | prop_episode_state_card | episode_state_cards | costume_state_turnaround_and_detail_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, K003 | medium |
| 32 | E01_K004 | prop_episode_state_card | episode_state_cards | costume_state_turnaround_and_detail_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, K004 | medium |
| 33 | E01_K006 | prop_episode_state_card | episode_state_cards | costume_state_turnaround_and_detail_sheet | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, K006 | medium |
| 34 | E01_P009 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006, P009 | high |
| 35 | E01_P002 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006, P002 | high |
| 36 | E01_P003 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006, P003 | high |
| 37 | E01_P004 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006, P004 | high |
| 38 | E01_P017 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006 | high |
| 39 | E01_P018 | prop_episode_state_card | precision_assets | prop_item_state_sheet_with_scale_and_detail_crops | 1:1 | neutral_plain_background | forbidden_on_card; transparent_cutout_requires_separate_png_or_svg_asset | E01_F001, E01_F006 | high |
| 40 | E01_R001 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C020, E01_L007, E01_P016 | high |
| 41 | E01_R002 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C020, E01_L007, E01_P016 | high |
| 42 | E01_R003 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C020, E01_C022, E01_L007, E01_P016 | high |
| 43 | E01_R004 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C004, E01_L007 | medium |
| 44 | E01_R005 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016B, E01_L003, E01_K004 | medium |
| 45 | E01_R006 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C017, E01_C024, E01_P008, E01_K006 | medium |
| 46 | E01_R007 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016B | medium |
| 47 | E01_R008 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C017, E01_C024, E01_L003, E01_P008 | high |
| 48 | E01_R009 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C017, E01_C024, E01_L003, E01_P008 | high |
| 49 | E01_R010 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L014, E01_P009 | medium |
| 50 | E01_R011 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C002, E01_C011, E01_P002, E01_K002 | medium |
| 51 | E01_R012 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C002, E01_C011, E01_P002 | medium |
| 52 | E01_R013 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L014, E01_P009 | high |
| 53 | E01_R014 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L014, E01_P009 | high |
| 54 | E01_R015 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C017, E01_C018, E01_C023, E01_L001A, E01_P017, E01_K004, E01_K006 | high |
| 55 | E01_R016 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016A, E01_L001A | high |
| 56 | E01_R017 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C001, E01_K001 | high |
| 57 | E01_R018 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C005, E01_P005, E01_K003 | high |
| 58 | E01_R019 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C005, E01_C006, E01_C016A | high |
| 59 | E01_R020 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C001, E01_P005, E01_P020 | high |
| 60 | E01_R021 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016A, E01_P003 | high |
| 61 | E01_R022 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_P004 | high |
| 62 | E01_R023 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L001A, E01_P017 | high |
| 63 | E01_R024 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L001A, E01_P017 | high |
| 64 | E01_R025 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C002, E01_L001B, E01_P002, E01_P018, E01_K002 | high |
| 65 | E01_R026 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C006, E01_L001B | medium |
| 66 | E01_R027 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C002 | medium |
| 67 | E01_R028 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L001B, E01_P018 | high |
| 68 | E01_R029 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C006, E01_L001B | medium |
| 69 | E01_R030 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_L001C, E01_P017 | high |
| 70 | E01_R031 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016A, E01_L001C, E01_P018 | high |
| 71 | E01_R032 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C016A, E01_C017, E01_C018, E01_C023, E01_L001C, E01_K004, E01_K006 | high |
| 72 | E01_R033 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C005, E01_P003, E01_P005 | high |
| 73 | E01_R034 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C007, E01_P004 | high |
| 74 | E01_R035 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C007, E01_P004 | high |
| 75 | E01_R036 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C007, E01_P003 | high |
| 76 | E01_R037 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C018, E01_L001C | high |
| 77 | E01_R038 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C001, E01_C005, E01_C007, E01_P020, E01_K003 | high |
| 78 | E01_R039 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C001, E01_C006, E01_P020, E01_K001 | high |
| 79 | E01_R040 | reference_frame | reference_frames | video_generation_reference_frame | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_C001, E01_C006, E01_P020, E01_K001 | high |
| 80 | E01_O001 | shot_override | shot_overrides | shot_override_video_frame_control_plate | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_F006, E01_C016A, E01_P003, E01_R021, E01_O001, E01_O002, E01_O003, E01_O004 | high |
| 81 | E01_O002 | shot_override | shot_overrides | shot_override_video_frame_control_plate | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_F006, E01_L001B, E01_P018, E01_R028, E01_O001, E01_O002, E01_O003, E01_O004 | high |
| 82 | E01_O003 | shot_override | shot_overrides | shot_override_video_frame_control_plate | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_F006, E01_C005, E01_P003, E01_P005, E01_R033, E01_O001, E01_O002, E01_O003, E01_O004 | high |
| 83 | E01_O004 | shot_override | shot_overrides | shot_override_video_frame_control_plate | 16:9 | video_frame | forbidden | E01_F001, E01_F005, E01_F006, E01_C007, E01_P003, E01_R036, E01_O001, E01_O002, E01_O003, E01_O004 | high |

## 审批重点

- 残阳坳村口/旧井/药屋/后山出口地理是否足够清楚。
- 白册官吏、粮税小吏、混血奴兵、纯虫族小兵、白翳是否层级分明。
- 晏南枝是否保持遮面与身份压力，未提前华丽揭示。
- 白册、旧驿暗号、血牒、日月纹是否采用后合成控制策略。
- 镜头参考帧是否覆盖 generation-plan 的首帧/终帧需求，并清楚分离前景、中景和背景。
