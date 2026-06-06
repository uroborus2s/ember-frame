# C023 人族逃难流民群像模板索引与提示词评审

## 评审结论

- 评审状态：`pass_for_planning_prompt_addition`
- 资产 ID：`C023`
- 提示词 ID：`PROMPT_C023`
- 输出路径：`assets/characters/c023m.png`
- 生成状态：未启动图片生成，仅完成索引、提示词和线程计划登记。

## 使用范围

`C023` 是人族群众在征粮、战乱、白册复核和逃荒压力下的极端状态模板，不是普通人族群众默认形象。主使用场景为第 03 集 `山道难民沟` 逃荒队，辅助参考第 06 集清明院队列中“逃荒妇人”的收肩、低头和排队姿态。

## 已评审项目

| 项目 | 结果 | 说明 |
| --- | --- | --- |
| 短文件名 | pass | `c023m.png` basename 小于 20 字符。 |
| 资产索引 | pass | `assets/asset-index.json` 已新增 `C023`，含 `identity_lock`、`body_metrics`、依赖、用途和 `output_format`。 |
| 提示词结构 | pass | `prompts/series-art-image-prompts.json` 已新增 `PROMPT_C023`，保留 `production_metadata` 与 `model_visible_prompt` 分离。 |
| copy-ready | pass | 已补齐 `positive_prompt`、`negative_prompt`、`chatgpt_image_prompt`、`gemini_image_prompt` 和参考图执行说明。 |
| 输出格式合同 | pass | 已声明 9:16、2160x3840、PNG、neutral plain、alpha forbidden、多人群像视图和 QC 项。 |
| 线程计划 | pass | 已加入 `B01_CORE_CHARACTERS`，但保持未派发状态。 |
| 剧情边界 | pass | 不改剧本，不新增剧情信息；只把已有逃荒队和逃荒妇人姿态转为可复用资产。 |

## 关键视觉锁

- 群像必须像逃荒者、流民和乞讨边缘人群，但贫困来源要明确来自征粮、战乱、白册复核和迁徙压力。
- 同一画面至少包含三类年龄、性别、职业、地域或贫困程度差异，不能生成同款破布背景人。
- 衣物可以脏旧、洗褪、补丁多、肩背有压痕，但必须保留中式实用缝制和完整收边。
- 白册复核条、祖牌小盒、旧包袱和空粮袋只做可控视觉形状，不生成可读文字、随机徽记或现代标识。
- `C023` 补充 `K006` 的极端逃难状态；不得覆盖 `K006` 中“人族群众不能乞丐化或同款化”的全局规则。

## 阻塞与后续

当前不启动图片生成。后续在 B06 服装提示词再生成完成并审批后，可随 `B01_CORE_CHARACTERS` 一起派发 `C023` 图片任务。生成完成后需要在资产 QC 中再次检查多人差异、衣物构造、短文件名、无 alpha、无可读文字和非视频帧属性。
