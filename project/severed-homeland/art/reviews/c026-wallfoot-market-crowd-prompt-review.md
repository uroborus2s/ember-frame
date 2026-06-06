# C026 墙下集市无籍者与粮牌黑市群像模板提示词评审

- 资产 ID：`C026`
- 提示词 ID：`PROMPT_C026`
- 批次：`B01_CORE_CHARACTERS`
- 资产类型：`character_master_card`
- 输出路径：`assets/characters/c026m.png`
- 评审日期：2026-06-05
- 评审状态：`pass_for_planning_prompt_addition_100`
- 审核评分：100/100
- 图片生成：未启动；等待单独批准 B01 生成线程。

## 资产定位

C026 是墙下集市无籍者与粮牌黑市群像模板，覆盖无籍者、混裔跑腿、军户家眷、黑市商、灰墙军粮牌贩、债务追讨者、传话孩子、摊主和谨慎旧遗民。它承载“夹缝交易秩序、进墙名额压力、粮牌交换和无籍/混裔身份层级”的人群卡。

C026 不是 L006 墙下集市地点卡。L006 锁定空间、窄巷、灰布棚和粮牌交换点环境；C026 锁定其中的人群身份、体态、年龄、职业、交易姿态和层级差异。

## 使用范围

- 第 07 集墙下集市窄巷。
- 第 07 集粮牌交换点。
- 陆青砾所处无籍者、混裔跑腿、军户家眷和黑市商世界参考。
- 与 C003 陆青砾个人、C025 普通平民、C023 逃难流民、C024 边墙军户区分。

## 评审评分

| 项目 | 分数 |
| --- | ---: |
| 资产范围与不重叠边界 | 15/15 |
| 来源引用、使用范围与剧透边界 | 15/15 |
| production_metadata 与 model_visible_prompt 分离 | 15/15 |
| 六段式模型可见提示词与 copy_ready 完整度 | 20/20 |
| output_format 合同完整度 | 15/15 |
| negative prompt 与禁用项护栏 | 10/10 |
| B01 批次与依赖整合 | 10/10 |
| **总分** | **100/100** |

## 通过依据

- 已写入 `assets/asset-index.json`，短文件名 `c026m.png`，basename 小于 20 字符。
- 已写入 `prompts/series-art-image-prompts.json`，包含六段 `model_visible_prompt`、`copy_ready.positive_prompt`、`copy_ready.negative_prompt`、ChatGPT/Gemini 复制提示词。
- 已包含 `identity_lock` 和 literal `body_metrics`，可区分传话孩子、跑腿少年、成年交易者、军户家眷、黑市商和混裔体态。
- 已包含 literal `output_format`，交付类型为 `neutral_master_card`，PNG，3840x2160，16:9，neutral plain background，alpha forbidden。
- 可见提示词保持墙下集市的职业、交易和身份层级，不把它画成普通村落集市、逃荒流民营、正规边墙军户队列或陆青砾复制群。

## 结论

C026 达到 100/100，可进入 B01_CORE_CHARACTERS 后续生成排队；当前不生成图片，不创建 canonical PNG。
