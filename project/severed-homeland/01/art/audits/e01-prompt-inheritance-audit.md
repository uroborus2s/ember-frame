# 第一集资产提示词继承一致性审查与评分

审查对象：`project/severed-homeland/01/prompts/art-image-prompts.json`。本轮只审查评分，不改写提示词。评分按全剧提示词重写后的新规则：模型可见提示词保持六段、短且清楚；继承自全局资产的一致性必须能通过 `reference_inputs`、参考图/控制图/线控层说明或等价执行路径落到生成环节。只在 `asset-index.json` 中有 `parent_asset_id`/`depends_on_assets`，但提示词记录没有告诉生成者如何上传参考图时，不算完全锁住。

## 汇总

- 提示词数量：83
- 平均分：58.8
- 最低分：56
- 最高分：69
- 是否全部 100 分：否
- 有 parent_asset_id 的资产：32
- 有 depends_on_assets 的资产：83
- prompt metadata 含 reference_inputs：0/83
- copy_ready 含 reference_image_instructions：0/83
- 可见生产用途标签：83
- 可见镜头编号：44
- 病句/模板残留：40
- 16:9 与 1:1 格式冲突：33
- 元数据字段/路径泄漏：0

## 按类型评分

| 类型 | 数量 | 平均分 | 最低分 | 最高分 | 缺 reference_inputs | 缺 copy 参考说明 | 生产标签 | 病句 | 格式冲突 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| character | 15 | 61.5 | 56 | 65 | 15 | 15 | 15 | 0 | 15 |
| location | 6 | 65.7 | 65 | 69 | 6 | 6 | 6 | 0 | 0 |
| prop | 10 | 56 | 56 | 56 | 10 | 10 | 10 | 0 | 10 |
| costume | 5 | 56 | 56 | 56 | 5 | 5 | 5 | 0 | 5 |
| style | 3 | 56 | 56 | 56 | 3 | 3 | 3 | 0 | 3 |
| reference_frame | 44 | 58.2 | 56 | 61 | 44 | 44 | 44 | 40 | 0 |

## 问题计数

- missing_prompt_reference_inputs: 83
- missing_copy_ready_reference_image_instructions: 83
- visible_production_usage_label: 83
- copy_ready_missing_reference_or_fields: 83
- continuity_too_thin: 70
- visible_shot_code: 44
- visible_video_pipeline_term: 40
- bad_sentence_or_template_residue: 40
- resolved_legacy_format_conflict_for_landscape_contract: 33
- subject_too_thin: 27

## 明细评分

| Prompt | 类型 | 总分 | 继承分 | 卫生分 | Copy/参考分 | 主要问题 |
|---|---|---:|---:|---:|---:|---|
| PROMPT_E01_C001 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C002 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C004 | character | 61 | 12 | 12 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_C005 | character | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_C006 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C007 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C011 | character | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_C016A | character | 61 | 12 | 12 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_C016B | character | 60 | 12 | 12 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_C017 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C018 | character | 60 | 12 | 12 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_C020 | character | 61 | 12 | 12 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_C022 | character | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_C023 | character | 65 | 12 | 12 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, resolved_legacy_format_conflict_for_landscape_contract |
| PROMPT_E01_C024 | character | 61 | 12 | 12 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_F001 | style | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_F005 | style | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_F006 | style | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_K001 | costume | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_K002 | costume | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_K003 | costume | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_K004 | costume | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_K006 | costume | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_L001A | location | 65 | 12 | 16 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_L001B | location | 65 | 12 | 16 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_L001C | location | 65 | 12 | 16 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_L003 | location | 65 | 12 | 16 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_L007 | location | 69 | 12 | 16 | 6 | missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label, copy_ready_missing_reference_or_fields |
| PROMPT_E01_L014 | location | 65 | 12 | 16 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_O001 | reference_frame | 61 | 12 | 13 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_O002 | reference_frame | 61 | 12 | 13 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_O003 | reference_frame | 61 | 12 | 13 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_O004 | reference_frame | 61 | 12 | 13 | 6 | subject_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_P002 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P003 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P004 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P005 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P008 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P009 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P016 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P017 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P018 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_P020 | prop | 56 | 12 | 12 | 6 | subject_too_thin, continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions |
| PROMPT_E01_R001 | reference_frame | 56 | 12 | 7 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R002 | reference_frame | 56 | 12 | 7 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R003 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R004 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R005 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R006 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R007 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R008 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R009 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R010 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R011 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R012 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R013 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R014 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R015 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R016 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R017 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R018 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R019 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R020 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R021 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R022 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R023 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R024 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R025 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R026 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R027 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R028 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R029 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R030 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R031 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R032 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R033 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R034 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R035 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R036 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R037 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R038 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R039 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |
| PROMPT_E01_R040 | reference_frame | 58 | 12 | 9 | 6 | continuity_too_thin, missing_prompt_reference_inputs, missing_copy_ready_reference_image_instructions, visible_production_usage_label |

## 结论

第一集提示词内容本身多数能描述剧情资产，但还没有达到全剧提示词新模板的 100 分标准。主要缺口不是长度，而是继承执行层：83 条提示词全部缺少 `production_metadata.reference_inputs`，也全部缺少 `copy_ready.reference_image_instructions`，导致全局父资产和本集依赖只停留在 `asset-index.json`，生成时不一定会被模型实际使用。另有 83 条可见提示词带“第01集/审核用视觉资产参考”等生产用途文字，40 条参考帧存在 `。。` 或英文模板残句，33 条资产卡同时写 16:9 与 1:1，存在目标格式冲突。

## 修复优先级

1. 给 83 条 prompt 增加 `production_metadata.reference_inputs`，从 `asset-index.json` 的 `parent_asset_id` 和 `depends_on_assets` 映射到已批准全局/本集参考图。
2. 给 83 条 `copy_ready` 增加 `reference_image_instructions`，明确生成时上传/引用父资产、角色、场景、服装、道具和风格参考图。
3. 移除模型可见提示中的“第01集审核用视觉资产参考”、`SCxxx-SHxxx`、`I2V/FLF2V` 等生产标签，保留为 metadata。
4. 修复 40 条参考帧中的 `。。` 和英文模板残句，把英文机位残句改成自然中文镜头描述。
5. 统一资产卡输出格式：卡片不要同时写 `16:9横屏` 与 `1:1中性资产卡`；参考帧才保留视频帧比例和前中后景要求。
