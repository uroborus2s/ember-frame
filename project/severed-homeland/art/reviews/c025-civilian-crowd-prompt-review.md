# C025 普通人族平民群像模板提示词评审

- 资产 ID：`C025`
- 提示词 ID：`PROMPT_C025`
- 批次：`B01_CORE_CHARACTERS`
- 资产类型：`character_master_card`
- 输出路径：`assets/characters/c025m.png`
- 评审日期：2026-06-05
- 评审状态：`pass_for_planning_prompt_addition_100`
- 审核评分：100/100
- 图片生成：未启动；等待单独批准 B01 生成线程。

## 资产定位

C025 是普通人族平民群像模板，覆盖残阳坳山民、金河粮仓带平民、麦田农户、粮磨工、船工家属、渡口小贩、低等账房、旧都渡口遗民、儿童、老人和家庭成年人。它承载“贫困但仍在生产、排队、交易和照看家人”的普通平民状态。

C025 不是 K006 服装板。K006 只规定人族地域群众服装、材质与阶层差异；C025 是可直接给角色群像、分集状态卡和后续镜头参考继承的身份群像卡。

## 使用范围

- 第 01 集征粮暴政中的老人、妇人、孩子和金河平民。
- 第 04 集金河粮磨区、渡口和粮牌检查口普通平民。
- 普通人族贫困但仍维持生活秩序的基础人群模板。
- 与 C023 逃难流民、C024 边墙军户、C026 墙下集市无籍者/黑市群像区分。

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

- 已写入 `assets/asset-index.json`，短文件名 `c025m.png`，basename 小于 20 字符。
- 已写入 `prompts/series-art-image-prompts.json`，包含六段 `model_visible_prompt`、`copy_ready.positive_prompt`、`copy_ready.negative_prompt`、ChatGPT/Gemini 复制提示词。
- 已包含 `identity_lock` 和 literal `body_metrics`，可区分儿童、少年、成年男女、老人、劳动者和低等账房体态。
- 已包含 literal `output_format`，交付类型为 `neutral_master_card`，PNG，2160x3840，9:16，neutral plain background，alpha forbidden。
- 可见提示词保持普通平民的生活秩序，不把他们画成现代灾民、乞讨队伍、C023 逃难流民、C024 边墙军户或 C026 墙下黑市人群。

## 结论

C025 达到 100/100，可进入 B01_CORE_CHARACTERS 后续生成排队；当前不生成图片，不创建 canonical PNG。
