# 第01集《白册进村》资产拆解计划

## 状态

- 审批状态：`pending_user_art_approval`
- 图片生成：`not_started_pending_user_approval`
- 当前只预留 canonical output path，不创建图片文件。
- 合同修复：已补齐 `creation_order`、`creation_phase`、`depends_on_assets`、`blocks_assets`、`dependency_reason` 和 `priority`。

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

| 批次 | 类型 | 创建顺序 | 依赖批次 | 状态 |
| --- | --- | ---: | --- | --- |
| B04_E01_STYLE | style | 1 | - | blocked_pending_user_approval |
| B01_E01_CHARACTERS | characters | 2 | B04_E01_STYLE | blocked_pending_user_approval |
| B02_E01_LOCATIONS | locations | 3 | B04_E01_STYLE | blocked_pending_user_approval |
| B03_E01_PROPS_COSTUMES | props-costumes | 4 | B04_E01_STYLE | blocked_pending_user_approval |
| B05_E01_REFERENCE_FRAMES | reference-frames | 5 | B01_E01_CHARACTERS, B02_E01_LOCATIONS, B03_E01_PROPS_COSTUMES, B04_E01_STYLE | blocked_pending_user_approval |
| B06_E01_SHOT_OVERRIDES | reference-frames | 6 | B03_E01_PROPS_COSTUMES, B04_E01_STYLE, B05_E01_REFERENCE_FRAMES | blocked_pending_user_approval |

## 资产创建顺序与依赖

| Order | Asset ID | Subtype | Phase | Depends On | Blocks | Priority | Status |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | E01_F001 | style_reference | style_reference | F001 | E01_C001, E01_C002, E01_C004, E01_C005, E01_C006, E01_C007, E01_C011, E01_C016A, ... | high | not_started_pending_user_approval |
| 2 | E01_F005 | style_reference | style_reference | F005 | E01_L007, E01_L003, E01_L014, E01_L001A, E01_L001B, E01_L001C, E01_R001, E01_R002, ... | high | not_started_pending_user_approval |
| 3 | E01_F006 | style_reference | style_reference | F006 | E01_P009, E01_P002, E01_P003, E01_P004, E01_P017, E01_P018, E01_O001, E01_O002, ... | high | not_started_pending_user_approval |
| 4 | E01_C001 | character_episode_state_card | episode_state_cards | E01_F001, C001 | E01_R017, E01_R020, E01_R038, E01_R039, E01_R040 | high | not_started_pending_user_approval |
| 5 | E01_C002 | character_episode_state_card | episode_state_cards | E01_F001, C002 | E01_R011, E01_R012, E01_R025, E01_R027 | high | not_started_pending_user_approval |
| 6 | E01_C004 | character_episode_state_card | episode_state_cards | E01_F001, C004 | E01_R004 | medium | not_started_pending_user_approval |
| 7 | E01_C005 | character_episode_state_card | episode_state_cards | E01_F001, C005 | E01_R018, E01_R019, E01_R033, E01_R038, E01_O003 | high | not_started_pending_user_approval |
| 8 | E01_C006 | character_episode_state_card | episode_state_cards | E01_F001, C006 | E01_R019, E01_R026, E01_R029, E01_R039, E01_R040 | high | not_started_pending_user_approval |
| 9 | E01_C007 | character_episode_state_card | episode_state_cards | E01_F001, C007 | E01_R034, E01_R035, E01_R036, E01_R038, E01_O004 | high | not_started_pending_user_approval |
| 10 | E01_C011 | character_episode_state_card | episode_state_cards | E01_F001, C011 | E01_R011, E01_R012 | medium | not_started_pending_user_approval |
| 11 | E01_C016A | character_episode_state_card | episode_state_cards | E01_F001, C016 | E01_R016, E01_R019, E01_R021, E01_R031, E01_R032, E01_O001 | medium | not_started_pending_user_approval |
| 12 | E01_C016B | character_episode_state_card | episode_state_cards | E01_F001, C016 | E01_R005, E01_R007 | medium | not_started_pending_user_approval |
| 13 | E01_C017 | character_episode_state_card | episode_state_cards | E01_F001, C017 | E01_R006, E01_R008, E01_R009, E01_R015, E01_R032 | medium | not_started_pending_user_approval |
| 14 | E01_C018 | character_episode_state_card | episode_state_cards | E01_F001, C018 | E01_R015, E01_R032, E01_R037 | medium | not_started_pending_user_approval |
| 15 | E01_C020 | character_episode_state_card | episode_state_cards | E01_F001, C020 | E01_R001, E01_R002, E01_R003 | medium | not_started_pending_user_approval |
| 16 | E01_C022 | character_episode_state_card | episode_state_cards | E01_F001 | E01_R003 | medium | not_started_pending_user_approval |
| 17 | E01_C023 | character_episode_state_card | episode_state_cards | E01_F001 | E01_R015, E01_R032 | medium | not_started_pending_user_approval |
| 18 | E01_C024 | character_episode_state_card | episode_state_cards | E01_F001 | E01_R006, E01_R008, E01_R009 | medium | not_started_pending_user_approval |
| 19 | E01_L007 | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L007 | E01_R001, E01_R002, E01_R003, E01_R004 | medium | not_started_pending_user_approval |
| 20 | E01_L003 | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L003 | E01_R005, E01_R008, E01_R009 | medium | not_started_pending_user_approval |
| 21 | E01_L014 | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L014 | E01_R010, E01_R013, E01_R014 | medium | not_started_pending_user_approval |
| 22 | E01_L001A | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L001 | E01_R015, E01_R016, E01_R023, E01_R024 | high | not_started_pending_user_approval |
| 23 | E01_L001B | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L001 | E01_R025, E01_R026, E01_R028, E01_R029, E01_O002 | high | not_started_pending_user_approval |
| 24 | E01_L001C | location_episode_scene_card | episode_state_cards | E01_F001, E01_F005, L001 | E01_R030, E01_R031, E01_R032, E01_R037 | high | not_started_pending_user_approval |
| 25 | E01_P016 | prop_episode_state_card | episode_state_cards | E01_F001 | E01_R001, E01_R002, E01_R003 | medium | not_started_pending_user_approval |
| 26 | E01_P008 | prop_episode_state_card | episode_state_cards | E01_F001, P008 | E01_R006, E01_R008, E01_R009 | medium | not_started_pending_user_approval |
| 27 | E01_P005 | prop_episode_state_card | episode_state_cards | E01_F001, P005 | E01_R018, E01_R020, E01_R033, E01_O003 | medium | not_started_pending_user_approval |
| 28 | E01_P020 | prop_episode_state_card | episode_state_cards | E01_F001 | E01_R020, E01_R038, E01_R039, E01_R040 | medium | not_started_pending_user_approval |
| 29 | E01_K001 | prop_episode_state_card | episode_state_cards | E01_F001, K001 | E01_R017, E01_R039, E01_R040 | medium | not_started_pending_user_approval |
| 30 | E01_K002 | prop_episode_state_card | episode_state_cards | E01_F001, K002 | E01_R011, E01_R025 | medium | not_started_pending_user_approval |
| 31 | E01_K003 | prop_episode_state_card | episode_state_cards | E01_F001, K003 | E01_R018, E01_R038 | medium | not_started_pending_user_approval |
| 32 | E01_K004 | prop_episode_state_card | episode_state_cards | E01_F001, K004 | E01_R005, E01_R015, E01_R032 | medium | not_started_pending_user_approval |
| 33 | E01_K006 | prop_episode_state_card | episode_state_cards | E01_F001, K006 | E01_R006, E01_R015, E01_R032 | medium | not_started_pending_user_approval |
| 34 | E01_P009 | prop_episode_state_card | precision_assets | E01_F001, E01_F006, P009 | E01_R010, E01_R013, E01_R014 | high | not_started_pending_user_approval |
| 35 | E01_P002 | prop_episode_state_card | precision_assets | E01_F001, E01_F006, P002 | E01_R011, E01_R012, E01_R025 | high | not_started_pending_user_approval |
| 36 | E01_P003 | prop_episode_state_card | precision_assets | E01_F001, E01_F006, P003 | E01_R021, E01_R033, E01_R036, E01_O001, E01_O003, E01_O004 | high | not_started_pending_user_approval |
| 37 | E01_P004 | prop_episode_state_card | precision_assets | E01_F001, E01_F006, P004 | E01_R022, E01_R034, E01_R035 | high | not_started_pending_user_approval |
| 38 | E01_P017 | prop_episode_state_card | precision_assets | E01_F001, E01_F006 | E01_R015, E01_R023, E01_R024, E01_R030 | high | not_started_pending_user_approval |
| 39 | E01_P018 | prop_episode_state_card | precision_assets | E01_F001, E01_F006 | E01_R025, E01_R028, E01_R031, E01_O002 | high | not_started_pending_user_approval |
| 40 | E01_R001 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C020, E01_L007, E01_P016 | - | high | not_started_pending_user_approval |
| 41 | E01_R002 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C020, E01_L007, E01_P016 | - | high | not_started_pending_user_approval |
| 42 | E01_R003 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C020, E01_C022, E01_L007, E01_P016 | - | high | not_started_pending_user_approval |
| 43 | E01_R004 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C004, E01_L007 | - | medium | not_started_pending_user_approval |
| 44 | E01_R005 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016B, E01_L003, E01_K004 | - | medium | not_started_pending_user_approval |
| 45 | E01_R006 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C017, E01_C024, E01_P008, E01_K006 | - | medium | not_started_pending_user_approval |
| 46 | E01_R007 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016B | - | medium | not_started_pending_user_approval |
| 47 | E01_R008 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C017, E01_C024, E01_L003, E01_P008 | - | high | not_started_pending_user_approval |
| 48 | E01_R009 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C017, E01_C024, E01_L003, E01_P008 | - | high | not_started_pending_user_approval |
| 49 | E01_R010 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L014, E01_P009 | - | medium | not_started_pending_user_approval |
| 50 | E01_R011 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C002, E01_C011, E01_P002, E01_K002 | - | medium | not_started_pending_user_approval |
| 51 | E01_R012 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C002, E01_C011, E01_P002 | - | medium | not_started_pending_user_approval |
| 52 | E01_R013 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L014, E01_P009 | - | high | not_started_pending_user_approval |
| 53 | E01_R014 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L014, E01_P009 | - | high | not_started_pending_user_approval |
| 54 | E01_R015 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C017, E01_C018, E01_C023, E01_L001A, E01_P017, E01_K004, E01_K006 | - | high | not_started_pending_user_approval |
| 55 | E01_R016 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016A, E01_L001A | - | high | not_started_pending_user_approval |
| 56 | E01_R017 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C001, E01_K001 | - | high | not_started_pending_user_approval |
| 57 | E01_R018 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C005, E01_P005, E01_K003 | - | high | not_started_pending_user_approval |
| 58 | E01_R019 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C005, E01_C006, E01_C016A | - | high | not_started_pending_user_approval |
| 59 | E01_R020 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C001, E01_P005, E01_P020 | - | high | not_started_pending_user_approval |
| 60 | E01_R021 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016A, E01_P003 | E01_O001 | high | not_started_pending_user_approval |
| 61 | E01_R022 | reference_frame | reference_frames | E01_F001, E01_F005, E01_P004 | - | high | not_started_pending_user_approval |
| 62 | E01_R023 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L001A, E01_P017 | - | high | not_started_pending_user_approval |
| 63 | E01_R024 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L001A, E01_P017 | - | high | not_started_pending_user_approval |
| 64 | E01_R025 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C002, E01_L001B, E01_P002, E01_P018, E01_K002 | - | high | not_started_pending_user_approval |
| 65 | E01_R026 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C006, E01_L001B | - | medium | not_started_pending_user_approval |
| 66 | E01_R027 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C002 | - | medium | not_started_pending_user_approval |
| 67 | E01_R028 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L001B, E01_P018 | E01_O002 | high | not_started_pending_user_approval |
| 68 | E01_R029 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C006, E01_L001B | - | medium | not_started_pending_user_approval |
| 69 | E01_R030 | reference_frame | reference_frames | E01_F001, E01_F005, E01_L001C, E01_P017 | - | high | not_started_pending_user_approval |
| 70 | E01_R031 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016A, E01_L001C, E01_P018 | - | high | not_started_pending_user_approval |
| 71 | E01_R032 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C016A, E01_C017, E01_C018, E01_C023, E01_L001C, E01_K004, E01_K006 | - | high | not_started_pending_user_approval |
| 72 | E01_R033 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C005, E01_P003, E01_P005 | E01_O003 | high | not_started_pending_user_approval |
| 73 | E01_R034 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C007, E01_P004 | - | high | not_started_pending_user_approval |
| 74 | E01_R035 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C007, E01_P004 | - | high | not_started_pending_user_approval |
| 75 | E01_R036 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C007, E01_P003 | E01_O004 | high | not_started_pending_user_approval |
| 76 | E01_R037 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C018, E01_L001C | - | high | not_started_pending_user_approval |
| 77 | E01_R038 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C001, E01_C005, E01_C007, E01_P020, E01_K003 | - | high | not_started_pending_user_approval |
| 78 | E01_R039 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C001, E01_C006, E01_P020, E01_K001 | - | high | not_started_pending_user_approval |
| 79 | E01_R040 | reference_frame | reference_frames | E01_F001, E01_F005, E01_C001, E01_C006, E01_P020, E01_K001 | - | high | not_started_pending_user_approval |
| 80 | E01_O001 | shot_override | shot_overrides | E01_F001, E01_F005, E01_F006, E01_C016A, E01_P003, E01_R021, E01_O001, E01_O002, E01_O003, E01_O004 | E01_O001, E01_O002, E01_O003, E01_O004 | high | not_started_pending_user_approval |
| 81 | E01_O002 | shot_override | shot_overrides | E01_F001, E01_F005, E01_F006, E01_L001B, E01_P018, E01_R028, E01_O001, E01_O002, E01_O003, E01_O004 | E01_O001, E01_O002, E01_O003, E01_O004 | high | not_started_pending_user_approval |
| 82 | E01_O003 | shot_override | shot_overrides | E01_F001, E01_F005, E01_F006, E01_C005, E01_P003, E01_P005, E01_R033, E01_O001, E01_O002, E01_O003, E01_O004 | E01_O001, E01_O002, E01_O003, E01_O004 | high | not_started_pending_user_approval |
| 83 | E01_O004 | shot_override | shot_overrides | E01_F001, E01_F005, E01_F006, E01_C007, E01_P003, E01_R036, E01_O001, E01_O002, E01_O003, E01_O004 | E01_O001, E01_O002, E01_O003, E01_O004 | high | not_started_pending_user_approval |

## 审批重点

- 残阳坳村口/旧井/药屋/后山出口地理是否足够清楚。
- 白册官吏、粮税小吏、混血奴兵、纯虫族小兵、白翳是否层级分明。
- 晏南枝是否保持遮面与身份压力，未提前华丽揭示。
- 白册、旧驿暗号、血牒、日月纹是否采用后合成控制策略。
- 镜头参考帧是否覆盖 generation-plan 的首帧/终帧需求。
