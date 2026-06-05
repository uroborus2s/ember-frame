# 全剧资产提示词一致性复审（修复后）

- 项目：`project/severed-homeland`
- 范围：全剧级 master asset prompts
- 提示词文件：`project/severed-homeland/prompts/series-art-image-prompts.json`
- 资产索引：`project/severed-homeland/assets/asset-index.json`
- 资产/提示词数量：68
- 审计时间：2026-06-05T09:25:28.647Z

## 评分口径

满分 100 需要同时满足：结构合同完整；可见提示含“视觉一致性硬锁”；自身锁、类型锁、依赖锁、剧情连续性锚点完整进入 `model_visible_prompt/copy_ready`，并用语义名称而非原始生产编号表达；metadata 的 `reference_inputs` 与依赖资产一致；精确符号资产有线控/遮罩/透明 PNG/SVG/后合成规则；可见提示未泄露 asset_id、输出路径、source refs 等生产字段。该分数证明提示词资产合同已达标，不替代最终出图后的视觉 QC。

## 总结

- 平均分：100
- 最高分：100
- 最低分：100
- 达到 100 分且无问题：68/68
- 分级：100_ready=68

## 类型统计

| 类型 | 数量 | 平均分 | 最低分 | 最高分 | 100分数量 |
| --- | ---: | ---: | ---: | ---: | ---: |
| character | 22 | 100 | 100 | 100 | 22 |
| location | 16 | 100 | 100 | 100 | 16 |
| prop | 18 | 100 | 100 | 100 | 18 |
| costume | 6 | 100 | 100 | 100 | 6 |
| style | 6 | 100 | 100 | 100 | 6 |

## 问题类型统计

| 问题代码 | 数量 |
| --- | ---: |
| 无 | 0 |

## 全量逐条评分

| Prompt | Asset | 名称 | 类型 | 总分 | 等级 | 问题代码 |
| --- | --- | --- | --- | ---: | --- | --- |
| PROMPT_C001 | C001 | 沈维桑全剧主角身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C002 | C002 | 晏南枝全剧主角身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C003 | C003 | 陆青砾墙下混裔身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C004 | C004 | 薛临墙边墙老墙师身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C005 | C005 | 沈照眠儿童识别者双状态卡 | character | 100 | 100_ready | 无 |
| PROMPT_C006 | C006 | 罗青禾医者母亲身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C007 | C007 | 白翳清明院监察官身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C008 | C008 | 厉螳甲军府战斗虫族身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C009 | C009 | 孟归藏旧书会亡书人身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C010 | C010 | 鹿弥霜蹄鹿族萨满身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C011 | C011 | 顾怀章复翼者旧臣身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C012 | C012 | 赫连雪岱白熊族护卫身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C013 | C013 | 乌岚黑狼族斥候身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C014 | C014 | 拓跋砚熊白熊族盾卫工匠身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C015 | C015 | 青翎鸦见雪羽鸦族斥候身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_C016 | C016 | 肃明基层虫吏层级模板 | character | 100 | 100_ready | 无 |
| PROMPT_C017 | C017 | 混血奴兵清污军户模板 | character | 100 | 100_ready | 无 |
| PROMPT_C018 | C018 | 普通纯虫族小兵模板 | character | 100 | 100_ready | 无 |
| PROMPT_C019 | C019 | 中阶重甲虫士兵模板 | character | 100 | 100_ready | 无 |
| PROMPT_C020 | C020 | 北境攻城兵种群像模板 | character | 100 | 100_ready | 无 |
| PROMPT_C021 | C021 | 北境共生兽关系模板 | character | 100 | 100_ready | 无 |
| PROMPT_C022 | C022 | 沈季衡旧驿测绘者档案影像身份卡 | character | 100 | 100_ready | 无 |
| PROMPT_L001 | L001 | 残阳坳村落与药屋主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L002 | L002 | 旧驿暗道白石残段主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L003 | L003 | 金河粮磨区与渡船主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L004 | L004 | 灰烬书院文明断代主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L005 | L005 | 清明院外署白墙主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L006 | L006 | 墙下集市无籍者空间主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L007 | L007 | 锁喉关边墙主门场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L008 | L008 | 鸣骨岭北境过渡场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L009 | L009 | 寒鸦堡军府档案主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L010 | L010 | 月下盟书旧驿主场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L011 | L011 | 坍塌烽燧季终逃亡场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L012 | L012 | 白曜城与清明中枢伏笔场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L013 | L013 | 东海断航伏笔场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L014 | L014 | 南林南缘红线伏笔场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L015 | L015 | 西部高原矮人旧盟伏笔场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_L016 | L016 | 东北沼泽虫族起源伏笔场景卡 | location | 100 | 100_ready | 无 |
| PROMPT_P001 | P001 | 半枚日月驿令道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P002 | P002 | 日月血牒与月白玉片道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P003 | P003 | 清明白册制度道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P004 | P004 | 虫蜡针与清明香追踪道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P005 | P005 | 沈照眠草药袋与烧焦发绳道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P006 | P006 | 鹿弥骨笛与血盐袋道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P007 | P007 | 月下盟书残页与多族印记道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P008 | P008 | 粮牌封蜡与押车绳道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P009 | P009 | 旧驿残图与测绘符号道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P010 | P010 | 朱赤旗布与日月纹道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P011 | P011 | 北境骨铁攻城器具道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P012 | P012 | 墙下黑市通行牌与碎陶护符道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P013 | P013 | 肃明黑日白翅派生徽记系统卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P014 | P014 | 昭明日月星盘派生符号系统卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P015 | P015 | 灰墙军旧甲片与骨哨道具卡 | prop | 100 | 100_ready | 无 |
| PROMPT_P016 | P016 | 昭明日月星盘徽章与朱赤旗帜基础母版 | prop | 100 | 100_ready | 无 |
| PROMPT_P017 | P017 | 肃明清明黑日白翅徽章与旗帜基础母版 | prop | 100 | 100_ready | 无 |
| PROMPT_P018 | P018 | 北境万兽部落联盟徽章与旗帜基础母版 | prop | 100 | 100_ready | 无 |
| PROMPT_K001 | K001 | 沈维桑分季服装状态板 | costume | 100 | 100_ready | 无 |
| PROMPT_K002 | K002 | 晏南枝流亡与身份揭示服装板 | costume | 100 | 100_ready | 无 |
| PROMPT_K003 | K003 | 沈照眠村中与清明院服装板 | costume | 100 | 100_ready | 无 |
| PROMPT_K004 | K004 | 肃明清明院服制层级板 | costume | 100 | 100_ready | 无 |
| PROMPT_K005 | K005 | 北境诸族服装材质层级板 | costume | 100 | 100_ready | 无 |
| PROMPT_K006 | K006 | 人族地域群众服装差异板 | costume | 100 | 100_ready | 无 |
| PROMPT_F001 | F001 | 全剧低魔东方史诗风格板 | style | 100 | 100_ready | 无 |
| PROMPT_F002 | F002 | 第一季地域色彩路线板 | style | 100 | 100_ready | 无 |
| PROMPT_F003 | F003 | 核心材质触感板 | style | 100 | 100_ready | 无 |
| PROMPT_F004 | F004 | 势力符号与禁用标志板 | style | 100 | 100_ready | 无 |
| PROMPT_F005 | F005 | 9比16竖屏构图与动作因果板 | style | 100 | 100_ready | 无 |
| PROMPT_F006 | F006 | 低魔显化与旧驿金赤光规则板 | style | 100 | 100_ready | 无 |

## 结论

修复后，全部全剧级资产提示词在提示词合同审计中达到 100 分。下一步仍需在实际图像生成时把 `production_metadata.reference_inputs` 中列出的上游母版图/控制图一并提供给图像模型，并在出图后执行视觉 QC；否则提示词合同 100 分不能自动等同于最终图片 100% 一致。
