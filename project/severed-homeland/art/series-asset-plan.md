# 《断航故土》全剧 Bible 资产规划与提示词审批包

## 审批状态

- 项目根目录：`project/severed-homeland`
- 范围：全剧共享 bible 级主资产，不生成分集参考帧和镜头覆盖图。
- 当前状态：`pending_art_approval_after_output_format_repair`
- 图片生成：未开始。审批通过前不得创建 Codex 图片生成线程，也不得写入 canonical 图片文件。
- 产物日期：2026-06-05
- 合同修复：2026-06-05 已完成 code review 修复；当前 JSON 资产索引、系列提示词和线程计划已满足 `art-room` 系列资产合同，并已补齐全局提示词输出图片格式要求，仍等待人工美术审批。

## 输入来源

本轮主要读取重制后的 bible、全剧视频规则、12 集最终剧本、分集连续性和 scene breakdown。旧 `legacy/`、旧资产、旧提示词、旧 ComfyUI 参数和旧渲染结果不作为美术 canon；唯一例外是本次人工审核明确要求 C001 沈维桑脸型与发型沿用 legacy 沈维桑角色板，因此 legacy 图只作为 C001 face/hair reference，不恢复旧版故事或旧版资产路径。

核心来源：`bible/world.md`、`bible/geography.md`、`bible/factions.md`、`bible/characters.md`、`bible/scenes.md`、`bible/visual-style.md`、`bible/continuity.md`、`production/series-video-rules.md`、`01-12/script/final-script.md`、`01-12/continuity/visual-continuity-bible.json`。

## 全剧视觉锁定

《断航故土》第一季采用超写实电影级低魔东方史诗护送剧风格。视觉资产必须优先服务角色身份稳定、制度层级清晰、地理连续和真实身体代价。低魔元素只允许短促、局部、有限地贴近旧驿、日月残纹、灵翼经络和记忆残留，不能替代判断、行动和牺牲。

第一季不能被统一成单一灰冷逃亡色。残阳坳、金河、灰烬书院、清明院、边墙、北境和月下旧驿必须保持不同色彩与材质系统。人族群众不能乞丐化或同款化；肃明抓捕层级必须区分虫吏、奴兵、纯虫小兵、重甲虫士兵、白翳和厉螳；北境诸族必须体现族群、阶层、政治派别、迁徙压力和共生兽关系。

## 资产总览

| 类型 | 数量 | 输出目录 | 目的 |
| --- | ---: | --- | --- |
| 角色/族群模板 | 22 | `assets/characters/` | 主角、反派、盟友、肃明层级、北境族群、共生兽关系和沈家旧档身份锁定 |
| 地点主场景 | 16 | `assets/locations/` | 第一季核心地点和后续季伏笔地点空间锁定 |
| 道具/符号 | 15 | `assets/props/` | 旧驿、清明籍、盟书、粮牌、徽记等可读信息道具 |
| 服装系统 | 6 | `assets/costumes/` | 主角状态、肃明服制、北境服饰、人族地域群众差异 |
| 风格参考 | 6 | `assets/style/` | 全剧风格、地域色彩、材质、符号策略、竖屏构图、低魔规则 |

## 文件规则

所有 canonical 图片输出路径只保留最终确认版本。短文件码 basename 均不超过 20 个字符，例如 `c001m.png`、`l001m.png`、`p001m.png`、`k001m.png`、`f001m.png`。语义名称、来源、用途、审批状态和 QC 状态只写入 JSON 索引，不写入长文件名。

如果审批后生成多个候选图，只有最终确认图可留在 `output_path`。需要保留的中间版本必须移动到同级 `history/` 目录，并使用 `.v001`、`.v002` 后缀。不得创建 `v1/`、`v2/`、`versions/` 或 `drafts/`。

## 角色与族群模板

| ID | 资产 | 文件 | 输出路径 | 用途 |
| --- | --- | --- | --- | --- |
| C001 | 沈维桑全剧主角身份卡 | c001m.png | assets/characters/c001m.png | 主角身份锁定；脸型发型沿用 legacy 角色板，增加少年剑目星眉 |
| C002 | 晏南枝全剧主角身份卡 | c002m.png | assets/characters/c002m.png | 护送目标身份锁定 |
| C003 | 陆青砾墙下混裔身份卡 | c003m.png | assets/characters/c003m.png | 墙下无姓混裔身份锁定 |
| C004 | 薛临墙边墙老墙师身份卡 | c004m.png | assets/characters/c004m.png | 边墙军户导师身份锁定 |
| C005 | 沈照眠儿童识别者双状态卡 | c005m.png | assets/characters/c005m.png | 妹妹亲情锚点 |
| C006 | 罗青禾医者母亲身份卡 | c006m.png | assets/characters/c006m.png | 残阳坳情感起点 |
| C007 | 白翳清明院监察官身份卡 | c007m.png | assets/characters/c007m.png | 核心追捕者身份锁定 |
| C008 | 厉螳甲军府战斗虫族身份卡 | c008m.png | assets/characters/c008m.png | 甲军府军事压力 |
| C009 | 孟归藏旧书会亡书人身份卡 | c009m.png | assets/characters/c009m.png | 灰烬书院证人 |
| C010 | 鹿弥霜蹄鹿族萨满身份卡 | c010m.png | assets/characters/c010m.png | 北境寻灾源派证人 |
| C011 | 顾怀章复翼者旧臣身份卡 | c011m.png | assets/characters/c011m.png | 晏南枝价值来源 |
| C012 | 赫连雪岱白熊族护卫身份卡 | c012m.png | assets/characters/c012m.png | 鹿弥重装近卫 |
| C013 | 乌岚黑狼族斥候身份卡 | c013m.png | assets/characters/c013m.png | 北境寻灾源派外围联络人 |
| C014 | 拓跋砚熊白熊族盾卫工匠身份卡 | c014m.png | assets/characters/c014m.png | 北境军用工匠 |
| C015 | 青翎鸦见雪羽鸦族斥候身份卡 | c015m.png | assets/characters/c015m.png | 寒鸦堡外线传讯者 |
| C016 | 肃明基层虫吏层级模板 | c016m.png | assets/characters/c016m.png | 白册官吏 |
| C017 | 混血奴兵清污军户模板 | c017m.png | assets/characters/c017m.png | 扣腕押车封门层级 |
| C018 | 普通纯虫族小兵模板 | c018m.png | assets/characters/c018m.png | 封锁退路 |
| C019 | 中阶重甲虫士兵模板 | c019m.png | assets/characters/c019m.png | 守门压阵层级 |
| C020 | 北境攻城兵种群像模板 | c020m.png | assets/characters/c020m.png | 锁喉关与北境战场兵种区分 |
| C021 | 北境共生兽关系模板 | c021m.png | assets/characters/c021m.png | 北境共生兽与驭兽者关系参考 |
| C022 | 沈季衡旧驿测绘者档案影像身份卡 | c022m.png | assets/characters/c022m.png | 沈家旧驿血线与第 10 集虫蜡档案影像参考 |

## 地点主场景

| ID | 资产 | 文件 | 输出路径 | 用途 |
| --- | --- | --- | --- | --- |
| L001 | 残阳坳村落与药屋主场景卡 | l001m.png | assets/locations/l001m.png | 第一季起点 |
| L002 | 旧驿暗道白石残段主场景卡 | l002m.png | assets/locations/l002m.png | 旧驿系统视觉母版 |
| L003 | 金河粮磨区与渡船主场景卡 | l003m.png | assets/locations/l003m.png | 灭械令生产技术场景母版 |
| L004 | 灰烬书院文明断代主场景卡 | l004m.png | assets/locations/l004m.png | 灭史空间母版 |
| L005 | 清明院外署白墙主场景卡 | l005m.png | assets/locations/l005m.png | 清明籍制度空间母版 |
| L006 | 墙下集市无籍者空间主场景卡 | l006m.png | assets/locations/l006m.png | 无籍者与混裔世界母版 |
| L007 | 锁喉关边墙主门场景卡 | l007m.png | assets/locations/l007m.png | 边墙战争与控粮冲突母版 |
| L008 | 鸣骨岭北境过渡场景卡 | l008m.png | assets/locations/l008m.png | 北境寻灾源视觉入口 |
| L009 | 寒鸦堡军府档案主场景卡 | l009m.png | assets/locations/l009m.png | 肃明军事占领与旧档线索母版 |
| L010 | 月下盟书旧驿主场景卡 | l010m.png | assets/locations/l010m.png | 第一季主题反转核心空间 |
| L011 | 坍塌烽燧季终逃亡场景卡 | l011m.png | assets/locations/l011m.png | 季终动作与价值选择场景母版 |
| L012 | 白曜城与清明中枢伏笔场景卡 | l012m.png | assets/locations/l012m.png | 后续季首都/白册总源视觉伏笔 |
| L013 | 东海断航伏笔场景卡 | l013m.png | assets/locations/l013m.png | 第二季航权线伏笔视觉母版 |
| L014 | 南林南缘红线伏笔场景卡 | l014m.png | assets/locations/l014m.png | 晏南枝来处与南方旧礼法视觉母版 |
| L015 | 西部高原矮人旧盟伏笔场景卡 | l015m.png | assets/locations/l015m.png | 金河源头与灭械令后续线视觉母版 |
| L016 | 东北沼泽虫族起源伏笔场景卡 | l016m.png | assets/locations/l016m.png | 肃明伪史与虫族起源后续线视觉母版 |

## 道具与精确符号

| ID | 资产 | 文件 | 输出路径 | 用途 |
| --- | --- | --- | --- | --- |
| P001 | 半枚日月驿令道具卡 | p001m.png | assets/props/p001m.png | 旧驿入口反应 |
| P002 | 日月血牒与月白玉片道具卡 | p002m.png | assets/props/p002m.png | 晏南枝身份压力 |
| P003 | 清明白册制度道具卡 | p003m.png | assets/props/p003m.png | 验名/划册/定罪工具 |
| P004 | 虫蜡针与清明香追踪道具卡 | p004m.png | assets/props/p004m.png | 血纹筛查 |
| P005 | 沈照眠草药袋与烧焦发绳道具卡 | p005m.png | assets/props/p005m.png | 妹妹亲情锚点 |
| P006 | 鹿弥骨笛与血盐袋道具卡 | p006m.png | assets/props/p006m.png | 共生兽安抚 |
| P007 | 月下盟书残页与多族印记道具卡 | p007m.png | assets/props/p007m.png | 第一季主题反转核心道具 |
| P008 | 粮牌封蜡与押车绳道具卡 | p008m.png | assets/props/p008m.png | 征粮压迫 |
| P009 | 旧驿残图与测绘符号道具卡 | p009m.png | assets/props/p009m.png | 沈家测绘官旧物 |
| P010 | 朱赤旗布与日月纹道具卡 | p010m.png | assets/props/p010m.png | 季终价值冲突道具 |
| P011 | 北境骨铁攻城器具道具卡 | p011m.png | assets/props/p011m.png | 北境攻城职能参考 |
| P012 | 墙下黑市通行牌与碎陶护符道具卡 | p012m.png | assets/props/p012m.png | 陆青砾身份锚点 |
| P013 | 肃明黑日白翅徽记系统卡 | p013m.png | assets/props/p013m.png | 肃明层级识别 |
| P014 | 昭明日月双印系统卡 | p014m.png | assets/props/p014m.png | 旧帝国遗迹/驿令/血牒/盟书统一符号参考 |
| P015 | 灰墙军旧甲片与骨哨道具卡 | p015m.png | assets/props/p015m.png | 边墙军户生活与守墙动作参考 |

精确旗帜、徽记、印记、白册、血牒和盟书类资产需要先做 master prop card，再使用线稿控制或透明 PNG/SVG 后合成策略。不要让图像模型自行发明可读文字、徽章、印章、现代 logo 或北境新动物 crest。

## 服装与风格参考

| ID | 资产 | 文件 | 输出路径 | 用途 |
| --- | --- | --- | --- | --- |
| K001 | 沈维桑分季服装状态板 | k001m.png | assets/costumes/k001m.png | 主角分集状态卡服装母版 |
| K002 | 晏南枝流亡与身份揭示服装板 | k002m.png | assets/costumes/k002m.png | 护送目标分集状态卡服装母版 |
| K003 | 沈照眠村中与清明院服装板 | k003m.png | assets/costumes/k003m.png | 儿童识别者状态连续 |
| K004 | 肃明清明院服制层级板 | k004m.png | assets/costumes/k004m.png | 虫族官吏/奴兵/士兵层级区分 |
| K005 | 北境诸族服装材质层级板 | k005m.png | assets/costumes/k005m.png | 鹿族/狼族/熊族/牛族/鸦族差异参考 |
| K006 | 人族地域群众服装差异板 | k006m.png | assets/costumes/k006m.png | 群像服装与阶层差异参考 |
| F001 | 全剧低魔东方史诗风格板 | f001m.png | assets/style/f001m.png | 全剧视觉风格总板 |
| F002 | 第一季地域色彩路线板 | f002m.png | assets/style/f002m.png | 分场景调色与材质连续性 |
| F003 | 核心材质触感板 | f003m.png | assets/style/f003m.png | 资产生成材质基准 |
| F004 | 势力符号与禁用标志板 | f004m.png | assets/style/f004m.png | 徽记和符号后合成策略 |
| F005 | 9比16竖屏构图与动作因果板 | f005m.png | assets/style/f005m.png | 短剧镜头资产构图参考 |
| F006 | 低魔显化与旧驿金赤光规则板 | f006m.png | assets/style/f006m.png | 低魔效果边界参考 |

## 提示词产物

全剧级图像提示词写入 `prompts/series-art-image-prompts.json`。每条记录都分离：

- 顶层字段：prompt_id、asset_id、asset_type、asset_subtype、output_path。
- `production_metadata`：asset_id、asset_subtype、短文件名 output_file、source_refs、continuity_refs、usage、审批状态、history 策略。
- `model_visible_prompt`：visible_goal、style_quality、subject_content、composition_motion、visible_continuity、negative_prompt。
- `output_format`：deliverable_kind、file_format、minimum_resolution、background_policy、alpha_policy、canvas_aspect_ratio、required_views、composition_layers、qc_checks。
- `copy_ready`：positive_prompt、negative_prompt、chatgpt_image_prompt、gemini_image_prompt，可直接复制给 ChatGPT 或 Gemini 图像生成。

可见提示词不包含 asset_id、episode_id、output_file、source refs 或使用说明；这些只留在生产元数据中，便于审批和后续线程派发。

## 输出格式合同

全局资产提示词不是最终视频帧提示词。每条全局 prompt 都已经写入 literal `output_format`，并把同一格式要求合并进 `copy_ready`：

| 资产类型 | 交付类型 | 图片格式 | 画幅与最低分辨率 | 背景/透明策略 |
| --- | --- | --- | --- | --- |
| 角色/族群模板 | neutral_master_character_card | PNG | 9:16 vertical，2160x3840 px | neutral_plain_background；此卡禁止 alpha，透明 cutout 必须另建 PNG/SVG |
| 地点主场景 | location_master_scene_card | PNG | 9:16 vertical，2160x3840 px | scene_card_with_spatial_environment；alpha forbidden |
| 道具/符号 | neutral_master_prop_card | PNG | 9:16 vertical，2160x3840 px | neutral_plain_background；此卡禁止 alpha，精确符号另建线稿/透明层 |
| 服装系统 | neutral_costume_system_card | PNG | 9:16 vertical，2160x3840 px | neutral_plain_background；此卡禁止 alpha，服装 cutout 另行规划 |
| 风格参考 | style_reference_board | PNG | 9:16 vertical，2160x3840 px | designed_style_board_canvas；alpha forbidden |

QC 必须检查 `required_views`、`composition_layers` 和 `qc_checks`，不得把角色、道具、服装和风格板误当作最终视频帧。

## 合同修复结果

本次审核发现旧版审批包仍处于“可读规划”状态，但未完全满足机器可审计合同。已修复：

1. `assets/asset-index.json` 已补齐每个资产的 `file_path`、`status`、`prompt_id`、`creation_order`、`creation_phase`、`depends_on_assets`、`blocks_assets`、`dependency_reason` 和 `priority`。
2. 22 个角色/族群模板均已有 literal `body_metrics` 与 `identity_lock`；15 个道具和 6 个服装/服制资产均已有 literal `physical_dimensions`；16 个地点均已有 `location_lock`。
3. 精确符号类资产 P002、P003、P007、P009、P010、P013、P014 已标记线稿控制或透明 PNG/SVG 后合成策略。
4. `prompts/series-art-image-prompts.json` 已从旧 `prompt_records` 改为合同要求的 `prompts` 数组，并为 65 条提示词补齐 `copy_ready`。
5. `art/series-thread-plan.json` 已拆分为风格、服装、角色、地点、道具/符号的 7 个依赖批次；所有批次仍为 `blocked_pending_art_approval`。
6. 65 个全局资产和 65 条提示词已补齐 `output_format`；线程计划也要求生成线程逐条遵守输出格式合同。
7. C001 沈维桑已锁定 legacy 同款窄长少年脸、黑色短碎乱发、额前碎刘海、贴脸鬓发、锋利剑眉、深黑星目和少年剑目星眉。

## 生成批次计划

预设批次写入 `art/series-thread-plan.json`，当前全部为 `blocked_pending_art_approval`：

| 顺序 | 批次 | 内容 | 依赖 | 状态 |
| ---: | --- | --- | --- | --- |
| 1 | B07_STYLE | 全剧风格板 | 无 | blocked_pending_art_approval |
| 2 | B06_COSTUMES | 服装系统 | B07_STYLE | blocked_pending_art_approval |
| 3 | B01_CORE_CHARACTERS | 核心、追捕线与沈家旧档角色 | B07_STYLE、B06_COSTUMES | blocked_pending_art_approval |
| 4 | B02_NORTHERN_AND_FACTION_TEMPLATES | 北境具名角色与族群/肃明层级模板 | B07_STYLE、B06_COSTUMES | blocked_pending_art_approval |
| 5 | B03_LOCATIONS_SEASON_ONE | 第一季核心地点 | B07_STYLE | blocked_pending_art_approval |
| 6 | B04_LOCATIONS_FUTURE_SEASONS | 后续季伏笔地点 | B07_STYLE | blocked_pending_art_approval |
| 7 | B05_PROPS_SYMBOLS | 核心道具与精确符号 | B07_STYLE、B01_CORE_CHARACTERS、B02_NORTHERN_AND_FACTION_TEMPLATES | blocked_pending_art_approval |

## 审批重点

1. 角色身份是否足够稳定，尤其沈维桑左肩旧伤、晏南枝古典美貌与皇室气度、陆青砾混裔细节、白翳制度性压迫、肃明层级和北境诸族差异。
2. 场景主卡是否覆盖第一季路线：残阳坳、旧驿暗道、金河、灰烬书院、清明院外署、墙下集市、锁喉关、鸣骨岭、寒鸦堡、月下旧驿、坍塌烽燧。
3. 道具和符号是否能在短剧首秒读懂，且不让模型发明精确文字或徽记。
4. 人族群众、虫族统治层级、北境族群与共生兽是否避免同质化。
5. 是否批准按 `art/series-thread-plan.json` 的七个批次和依赖顺序开始图片生成。

## 下一步

人工审批通过后，再按批次创建 Codex 背景图片生成线程，生成结果写入 `art/series-thread-results.json`，并在完成后进入资产 QC。QC 通过后再交回 director-room 做分集 prompt refresh 与镜头级参考帧规划。

## 合同审计补充

### 创建顺序与依赖

| Order | Batch | Phase | Depends On Batches | Depends On Assets | Blocks Batches | Priority |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | B07_STYLE | 01_style_references | - | - | B06_COSTUMES, B01_CORE_CHARACTERS, B02_NORTHERN_AND_FACTION_TEMPLATES, B03_LOCATIONS_SEASON_ONE, B04_LOCATIONS_FUTURE_SEASONS, B05_PROPS_SYMBOLS | critical |
| 2 | B06_COSTUMES | 02_costume_style_references | B07_STYLE | F001, F002, F003, F004, F005, F006 | B01_CORE_CHARACTERS, B02_NORTHERN_AND_FACTION_TEMPLATES | critical |
| 3 | B01_CORE_CHARACTERS | 03_character_master_cards | B07_STYLE, B06_COSTUMES | F001, F002, F003, F004, F005, F006, K001, K002, K003, K004, K005, K006 | B05_PROPS_SYMBOLS | high |
| 4 | B02_NORTHERN_AND_FACTION_TEMPLATES | 03_character_master_cards | B07_STYLE, B06_COSTUMES | F001, F002, F003, F004, F005, F006, K004, K005 | B05_PROPS_SYMBOLS | high |
| 5 | B03_LOCATIONS_SEASON_ONE | 04_location_master_scene_cards | B07_STYLE | F001, F002, F003, F005, F006 | - | high |
| 6 | B04_LOCATIONS_FUTURE_SEASONS | 04_location_master_scene_cards | B07_STYLE | F001, F002, F003, F005, F006 | - | high |
| 7 | B05_PROPS_SYMBOLS | 05_prop_and_precision_symbol_master_cards | B07_STYLE, B01_CORE_CHARACTERS, B02_NORTHERN_AND_FACTION_TEMPLATES | F001, F003, F004, F006, C001, C002, C003, C004, C005, C006, C007, C010, C011, C016, C017, C018, C019, C020, C021, C022 | - | high |

### 提示词审计

- `prompts/series-art-image-prompts.json` 已补齐 `output_format`、`copy_ready.positive_prompt`、`copy_ready.negative_prompt`、`copy_ready.chatgpt_image_prompt` 和 `copy_ready.gemini_image_prompt`。
- 全剧 bible 级 prompt record 的 `production_metadata.output_file` 已规范为短文件名，canonical 路径保留在 `output_path`。
- 可见提示词继续只保留六段模型可见内容，不混入 asset_id、source refs、usage 或输出路径。
