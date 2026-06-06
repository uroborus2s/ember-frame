# 全剧资产提示词一致性审计

- 项目：`project/severed-homeland`
- 范围：全剧级 master asset prompts，不含第 01 集分集 prompts
- 提示词文件：`project/severed-homeland/prompts/series-art-image-prompts.json`
- 资产索引：`project/severed-homeland/assets/asset-index.json`
- 资产/提示词数量：68
- 审计时间：2026-06-05T09:13:16.561Z

## 评分口径

满分 100 需要同时满足：结构合同完整、资产自身锁进入 `model_visible_prompt/copy_ready`、类型专属锁进入可见提示、依赖资产锁或参考输入可用于模型、精确徽章/符号/文字有线控或后合成策略、剧情/用途/连续性锚点进入可见提示。该分数是提示词与资产索引的文本/结构审计，不能替代最终出图 QC。

## 总结

- 平均分：75.4
- 最高分：87
- 最低分：47
- 达到 100 分且无问题：0/68
- 分级：needs_revision=36，high_risk=32

## 类型统计

| 类型 | 数量 | 平均分 | 最低分 | 最高分 | 100分数量 |
| --- | ---: | ---: | ---: | ---: | ---: |
| character | 22 | 74.2 | 47 | 86 | 0 |
| location | 16 | 85.4 | 78 | 87 | 0 |
| prop | 18 | 70.1 | 58 | 82 | 0 |
| costume | 6 | 67 | 58 | 74 | 0 |
| style | 6 | 77.2 | 66 | 85 | 0 |

## 问题类型统计

| 问题代码 | 数量 |
| --- | ---: |
| REFERENCE_INPUTS_MISSING | 65 |
| DEPENDENCY_LOCK_NOT_VISIBLE | 64 |
| TYPE_LOCK_WEAK | 60 |
| OWN_LOCK_WEAK | 48 |
| STORY_CONTINUITY_WEAK | 33 |
| PHYSICAL_DIMENSIONS_WEAK | 24 |
| BODY_METRICS_WEAK | 22 |

## 高风险/低于85分资产

| Prompt | Asset | 名称 | 总分 | 主要问题 |
| --- | --- | --- | ---: | --- |
| PROMPT_C002 | C002 | 晏南枝全剧主角身份卡 | 80 | OWN_LOCK_WEAK: visible/copy prompt covers 20/39 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 13/29 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/13 |
| PROMPT_C003 | C003 | 陆青砾墙下混裔身份卡 | 81 | TYPE_LOCK_WEAK: visible/copy prompt covers 11/29 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/14<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 1/8 dependency locks |
| PROMPT_C004 | C004 | 薛临墙边墙老墙师身份卡 | 78 | OWN_LOCK_WEAK: visible/copy prompt covers 19/38 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 11/29 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 3/14 |
| PROMPT_C006 | C006 | 罗青禾医者母亲身份卡 | 77 | OWN_LOCK_WEAK: visible/copy prompt covers 21/42 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 11/32 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 3/14 |
| PROMPT_C007 | C007 | 白翳清明院监察官身份卡 | 78 | OWN_LOCK_WEAK: visible/copy prompt covers 24/46 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 11/31 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 3/14 |
| PROMPT_C008 | C008 | 厉螳甲军府战斗虫族身份卡 | 72 | OWN_LOCK_WEAK: visible/copy prompt covers 18/39 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 8/29 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/13 |
| PROMPT_C009 | C009 | 孟归藏旧书会亡书人身份卡 | 74 | OWN_LOCK_WEAK: visible/copy prompt covers 15/32 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 7/23 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/11 |
| PROMPT_C010 | C010 | 鹿弥霜蹄鹿族萨满身份卡 | 77 | OWN_LOCK_WEAK: visible/copy prompt covers 20/39 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 12/29 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 2/13 |
| PROMPT_C011 | C011 | 顾怀章复翼者旧臣身份卡 | 66 | OWN_LOCK_WEAK: visible/copy prompt covers 21/49 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 6/34 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/14 |
| PROMPT_C012 | C012 | 赫连雪岱白熊族护卫身份卡 | 77 | OWN_LOCK_WEAK: visible/copy prompt covers 21/41 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 9/27 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/12 |
| PROMPT_C013 | C013 | 乌岚黑狼族斥候身份卡 | 81 | OWN_LOCK_WEAK: visible/copy prompt covers 17/31 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 8/21 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/9 |
| PROMPT_C014 | C014 | 拓跋砚熊白熊族盾卫工匠身份卡 | 75 | OWN_LOCK_WEAK: visible/copy prompt covers 20/40 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 9/26 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/10 |
| PROMPT_C015 | C015 | 青翎鸦见雪羽鸦族斥候身份卡 | 76 | OWN_LOCK_WEAK: visible/copy prompt covers 22/41 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 7/26 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/10 |
| PROMPT_C016 | C016 | 肃明基层虫吏层级模板 | 74 | OWN_LOCK_WEAK: visible/copy prompt covers 25/49 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 8/32 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/13 |
| PROMPT_C017 | C017 | 混血奴兵清污军户模板 | 71 | OWN_LOCK_WEAK: visible/copy prompt covers 25/49 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 5/28 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/11 |
| PROMPT_C018 | C018 | 普通纯虫族小兵模板 | 65 | OWN_LOCK_WEAK: visible/copy prompt covers 20/48 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 4/31 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 0/13 |
| PROMPT_C019 | C019 | 中阶重甲虫士兵模板 | 73 | OWN_LOCK_WEAK: visible/copy prompt covers 24/47 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 6/28 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/11 |
| PROMPT_C020 | C020 | 北境攻城兵种群像模板 | 71 | OWN_LOCK_WEAK: visible/copy prompt covers 21/47 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 10/35 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 4/19 |
| PROMPT_C021 | C021 | 北境共生兽关系模板 | 69 | OWN_LOCK_WEAK: visible/copy prompt covers 21/48 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 8/35 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 1/16 |
| PROMPT_C022 | C022 | 沈季衡旧驿测绘者档案影像身份卡 | 47 | OWN_LOCK_WEAK: visible/copy prompt covers 8/51 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 4/34 type-specific anchors<br>BODY_METRICS_WEAK: body_metrics coverage 2/14 |
| PROMPT_L001 | L001 | 残阳坳村落与药屋主场景卡 | 83 | TYPE_LOCK_WEAK: visible/copy prompt covers 15/31 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 1/7 dependency locks<br>REFERENCE_INPUTS_MISSING: prompt record has depends_on_assets in asset index but no explicit reference image/control inputs for model dispatch |
| PROMPT_L012 | L012 | 白曜城与清明中枢伏笔场景卡 | 82 | TYPE_LOCK_WEAK: visible/copy prompt covers 15/32 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 1/9 dependency locks<br>REFERENCE_INPUTS_MISSING: prompt record has depends_on_assets in asset index but no explicit reference image/control inputs for model dispatch |
| PROMPT_L013 | L013 | 东海断航伏笔场景卡 | 78 | TYPE_LOCK_WEAK: visible/copy prompt covers 12/29 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 1/7 dependency locks<br>REFERENCE_INPUTS_MISSING: prompt record has depends_on_assets in asset index but no explicit reference image/control inputs for model dispatch |
| PROMPT_P001 | P001 | 半枚日月驿令道具卡 | 72 | OWN_LOCK_WEAK: visible/copy prompt covers 15/37 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 15/37 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/11 |
| PROMPT_P002 | P002 | 日月血牒与月白玉片道具卡 | 67 | OWN_LOCK_WEAK: visible/copy prompt covers 32/77 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 13/42 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/14 |
| PROMPT_P003 | P003 | 清明白册制度道具卡 | 76 | OWN_LOCK_WEAK: visible/copy prompt covers 34/73 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 15/38 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/8 |
| PROMPT_P004 | P004 | 虫蜡针与清明香追踪道具卡 | 73 | OWN_LOCK_WEAK: visible/copy prompt covers 16/40 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 16/40 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/11 |
| PROMPT_P005 | P005 | 沈照眠草药袋与烧焦发绳道具卡 | 77 | OWN_LOCK_WEAK: visible/copy prompt covers 15/34 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 15/34 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/7 |
| PROMPT_P006 | P006 | 鹿弥骨笛与血盐袋道具卡 | 77 | OWN_LOCK_WEAK: visible/copy prompt covers 16/37 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 16/37 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/11 |
| PROMPT_P007 | P007 | 月下盟书残页与多族印记道具卡 | 74 | OWN_LOCK_WEAK: visible/copy prompt covers 39/84 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 20/49 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/14 |
| PROMPT_P008 | P008 | 粮牌封蜡与押车绳道具卡 | 68 | OWN_LOCK_WEAK: visible/copy prompt covers 13/37 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 13/37 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/13 |
| PROMPT_P009 | P009 | 旧驿残图与测绘符号道具卡 | 69 | OWN_LOCK_WEAK: visible/copy prompt covers 34/79 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 15/44 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/14 |
| PROMPT_P010 | P010 | 朱赤旗布与日月纹道具卡 | 73 | OWN_LOCK_WEAK: visible/copy prompt covers 34/74 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 15/39 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/11 |
| PROMPT_P011 | P011 | 北境骨铁攻城器具道具卡 | 82 | OWN_LOCK_WEAK: visible/copy prompt covers 20/41 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 20/41 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/11 |
| PROMPT_P012 | P012 | 墙下黑市通行牌与碎陶护符道具卡 | 65 | OWN_LOCK_WEAK: visible/copy prompt covers 12/37 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 12/37 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/13 |
| PROMPT_P013 | P013 | 肃明黑日白翅派生徽记系统卡 | 64 | OWN_LOCK_WEAK: visible/copy prompt covers 32/91 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 14/55 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/13 |
| PROMPT_P014 | P014 | 昭明日月星盘派生符号系统卡 | 58 | OWN_LOCK_WEAK: visible/copy prompt covers 27/83 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 10/47 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/13 |
| PROMPT_P015 | P015 | 灰墙军旧甲片与骨哨道具卡 | 72 | OWN_LOCK_WEAK: visible/copy prompt covers 14/37 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 14/37 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/13 |
| PROMPT_P016 | P016 | 昭明日月星盘徽章与朱赤旗帜基础母版 | 61 | OWN_LOCK_WEAK: visible/copy prompt covers 23/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 12/98 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 1/31 |
| PROMPT_P017 | P017 | 肃明清明黑日白翅徽章与旗帜基础母版 | 67 | OWN_LOCK_WEAK: visible/copy prompt covers 27/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 16/98 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 2/28 |
| PROMPT_P018 | P018 | 北境万兽部落联盟徽章与旗帜基础母版 | 66 | OWN_LOCK_WEAK: visible/copy prompt covers 29/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 13/90 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 1/25 |
| PROMPT_K001 | K001 | 沈维桑分季服装状态板 | 58 | OWN_LOCK_WEAK: visible/copy prompt covers 11/50 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 11/44 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 1/15 |
| PROMPT_K002 | K002 | 晏南枝流亡与身份揭示服装板 | 59 | OWN_LOCK_WEAK: visible/copy prompt covers 12/49 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 12/43 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 0/14 |
| PROMPT_K003 | K003 | 沈照眠村中与清明院服装板 | 71 | OWN_LOCK_WEAK: visible/copy prompt covers 16/45 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 16/39 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 3/14 |
| PROMPT_K004 | K004 | 肃明清明院服制层级板 | 70 | OWN_LOCK_WEAK: visible/copy prompt covers 23/64 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 22/55 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 5/18 |
| PROMPT_K005 | K005 | 北境诸族服装材质层级板 | 70 | OWN_LOCK_WEAK: visible/copy prompt covers 17/49 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 17/43 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 2/13 |
| PROMPT_K006 | K006 | 人族地域群众服装差异板 | 74 | OWN_LOCK_WEAK: visible/copy prompt covers 20/52 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 20/46 type-specific anchors<br>PHYSICAL_DIMENSIONS_WEAK: physical_dimensions coverage 3/16 |
| PROMPT_F001 | F001 | 全剧低魔东方史诗风格板 | 82 | OWN_LOCK_WEAK: visible/copy prompt covers 61/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 62/120 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 0/3 dependency locks |
| PROMPT_F002 | F002 | 第一季地域色彩路线板 | 66 | OWN_LOCK_WEAK: visible/copy prompt covers 44/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 43/120 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 0/3 dependency locks |
| PROMPT_F004 | F004 | 势力符号与禁用标志板 | 73 | OWN_LOCK_WEAK: visible/copy prompt covers 32/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 32/120 type-specific anchors<br>REFERENCE_INPUTS_MISSING: prompt record has depends_on_assets in asset index but no explicit reference image/control inputs for model dispatch |
| PROMPT_F005 | F005 | 16比9横屏构图与动作因果板 | 76 | OWN_LOCK_WEAK: visible/copy prompt covers 59/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 60/120 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 0/3 dependency locks |
| PROMPT_F006 | F006 | 低魔显化与旧驿金赤光规则板 | 81 | OWN_LOCK_WEAK: visible/copy prompt covers 61/120 own lock anchors<br>TYPE_LOCK_WEAK: visible/copy prompt covers 62/120 type-specific anchors<br>DEPENDENCY_LOCK_NOT_VISIBLE: visible/copy prompt visibly carries 0/3 dependency locks |

## 全量逐条评分

| Prompt | Asset | 名称 | 类型 | 总分 | 等级 | 问题代码 |
| --- | --- | --- | --- | ---: | --- | --- |
| PROMPT_C001 | C001 | 沈维桑全剧主角身份卡 | character | 85 | needs_revision | TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C002 | C002 | 晏南枝全剧主角身份卡 | character | 80 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_C003 | C003 | 陆青砾墙下混裔身份卡 | character | 81 | needs_revision | TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C004 | C004 | 薛临墙边墙老墙师身份卡 | character | 78 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C005 | C005 | 沈照眠儿童识别者双状态卡 | character | 86 | needs_revision | TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C006 | C006 | 罗青禾医者母亲身份卡 | character | 77 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C007 | C007 | 白翳清明院监察官身份卡 | character | 78 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C008 | C008 | 厉螳甲军府战斗虫族身份卡 | character | 72 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C009 | C009 | 孟归藏旧书会亡书人身份卡 | character | 74 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_C010 | C010 | 鹿弥霜蹄鹿族萨满身份卡 | character | 77 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_C011 | C011 | 顾怀章复翼者旧臣身份卡 | character | 66 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C012 | C012 | 赫连雪岱白熊族护卫身份卡 | character | 77 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C013 | C013 | 乌岚黑狼族斥候身份卡 | character | 81 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C014 | C014 | 拓跋砚熊白熊族盾卫工匠身份卡 | character | 75 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_C015 | C015 | 青翎鸦见雪羽鸦族斥候身份卡 | character | 76 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C016 | C016 | 肃明基层虫吏层级模板 | character | 74 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C017 | C017 | 混血奴兵清污军户模板 | character | 71 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C018 | C018 | 普通纯虫族小兵模板 | character | 65 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C019 | C019 | 中阶重甲虫士兵模板 | character | 73 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C020 | C020 | 北境攻城兵种群像模板 | character | 71 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_C021 | C021 | 北境共生兽关系模板 | character | 69 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_C022 | C022 | 沈季衡旧驿测绘者档案影像身份卡 | character | 47 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, BODY_METRICS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L001 | L001 | 残阳坳村落与药屋主场景卡 | location | 83 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L002 | L002 | 旧驿暗道白石残段主场景卡 | location | 85 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L003 | L003 | 金河粮磨区与渡船主场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L004 | L004 | 灰烬书院文明断代主场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L005 | L005 | 清明院外署白墙主场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L006 | L006 | 墙下集市无籍者空间主场景卡 | location | 86 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L007 | L007 | 锁喉关边墙主门场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L008 | L008 | 鸣骨岭北境过渡场景卡 | location | 85 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L009 | L009 | 寒鸦堡军府档案主场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L010 | L010 | 月下盟书旧驿主场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L011 | L011 | 坍塌烽燧季终逃亡场景卡 | location | 86 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L012 | L012 | 白曜城与清明中枢伏笔场景卡 | location | 82 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L013 | L013 | 东海断航伏笔场景卡 | location | 78 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_L014 | L014 | 南林南缘红线伏笔场景卡 | location | 87 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L015 | L015 | 西部高原矮人旧盟伏笔场景卡 | location | 87 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_L016 | L016 | 东北沼泽虫族起源伏笔场景卡 | location | 85 | needs_revision | TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P001 | P001 | 半枚日月驿令道具卡 | prop | 72 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P002 | P002 | 日月血牒与月白玉片道具卡 | prop | 67 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P003 | P003 | 清明白册制度道具卡 | prop | 76 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_P004 | P004 | 虫蜡针与清明香追踪道具卡 | prop | 73 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P005 | P005 | 沈照眠草药袋与烧焦发绳道具卡 | prop | 77 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_P006 | P006 | 鹿弥骨笛与血盐袋道具卡 | prop | 77 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P007 | P007 | 月下盟书残页与多族印记道具卡 | prop | 74 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P008 | P008 | 粮牌封蜡与押车绳道具卡 | prop | 68 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P009 | P009 | 旧驿残图与测绘符号道具卡 | prop | 69 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P010 | P010 | 朱赤旗布与日月纹道具卡 | prop | 73 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P011 | P011 | 北境骨铁攻城器具道具卡 | prop | 82 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_P012 | P012 | 墙下黑市通行牌与碎陶护符道具卡 | prop | 65 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P013 | P013 | 肃明黑日白翅派生徽记系统卡 | prop | 64 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P014 | P014 | 昭明日月星盘派生符号系统卡 | prop | 58 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_P015 | P015 | 灰墙军旧甲片与骨哨道具卡 | prop | 72 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_P016 | P016 | 昭明日月星盘徽章与朱赤旗帜基础母版 | prop | 61 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, STORY_CONTINUITY_WEAK |
| PROMPT_P017 | P017 | 肃明清明黑日白翅徽章与旗帜基础母版 | prop | 67 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, STORY_CONTINUITY_WEAK |
| PROMPT_P018 | P018 | 北境万兽部落联盟徽章与旗帜基础母版 | prop | 66 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, STORY_CONTINUITY_WEAK |
| PROMPT_K001 | K001 | 沈维桑分季服装状态板 | costume | 58 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_K002 | K002 | 晏南枝流亡与身份揭示服装板 | costume | 59 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_K003 | K003 | 沈照眠村中与清明院服装板 | costume | 71 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_K004 | K004 | 肃明清明院服制层级板 | costume | 70 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_K005 | K005 | 北境诸族服装材质层级板 | costume | 70 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_K006 | K006 | 人族地域群众服装差异板 | costume | 74 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, PHYSICAL_DIMENSIONS_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_F001 | F001 | 全剧低魔东方史诗风格板 | style | 82 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_F002 | F002 | 第一季地域色彩路线板 | style | 66 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_F003 | F003 | 核心材质触感板 | style | 85 | needs_revision | DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING |
| PROMPT_F004 | F004 | 势力符号与禁用标志板 | style | 73 | high_risk | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_F005 | F005 | 16比9横屏构图与动作因果板 | style | 76 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |
| PROMPT_F006 | F006 | 低魔显化与旧驿金赤光规则板 | style | 81 | needs_revision | OWN_LOCK_WEAK, TYPE_LOCK_WEAK, DEPENDENCY_LOCK_NOT_VISIBLE, REFERENCE_INPUTS_MISSING, STORY_CONTINUITY_WEAK |

## 结论

当前全剧提示词不是完全没有锁，但多数提示词没有达到“剧情 100%、一致性 100%、总体 100 分”的可执行标准。最大共性问题是依赖资产锁没有被显式带入模型输入，也没有独立的参考图/控制图输入清单；这会导致角色、服装、徽章、风格板在后续生成时依赖人工记忆，而不是由提示词管线强制传递。
