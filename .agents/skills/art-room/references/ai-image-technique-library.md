# AI 制图技巧库

本参考文件把网络公开教程、开源图像生成实践、用户提供的短视频截图经验，整理成美术部可自助选择的制作技巧。它总结的是可复用方法，不复制平台创作者的专有文案，也不把某个工具的参数当成唯一标准。

## 使用原则

每次生图前，先判断图片资产要解决什么问题，再选技巧。不要为了炫技叠加控制图。

```text
角色漂移 -> 身份参考、角色卡、脸部/服装细节、转面图
空间漂移 -> 场景母图、俯视图、九宫格、线稿/深度/分割控制
动作漂移 -> 故事板草图、姿态控制、运动轨迹图、首尾帧
风格漂移 -> 风格板、材质板、色彩板、风格参考图
局部错误 -> 遮罩重绘、局部参考、精确覆盖层
信息过载 -> 信息预算、远景简化、负向约束
```

每个技巧都必须被记录到资产或提示词的 `technique_profile` 中：

```text
technique_profile:
  technique_ids:
    - TECH-...
  selection_reason:
    为什么选这些技巧
  reference_image_roles:
    每张参考图的角色：identity / style / structure / pose / depth / mask / motion / material
  control_inputs:
    控制图路径、用途、权重意图、必须保留项、可变化项、禁止入画项
  forbidden_rendered_guides:
    不能出现在最终图里的蓝线、箭头、字母、圆圈、UI、水印、标签等
  fallback_plan:
    如果模型无法稳定执行，降级到哪种更强控制或人工后合成
```

## 技巧菜单

### TECH-REF-01 多参考图角色锁定

用途：
稳定同一角色的脸、发型、体型、服装、饰品和气质。

适用资产：
`character_master_card`、`character_episode_state_card`、`reference_frame`、`shot_override`。

做法：

```text
1. 先做角色母卡：半身肖像、全身、正面、侧面、背面、三分之四。
2. 拆出细节参考：脸部裁切、发型裁切、手部/饰品/服装纹理裁切。
3. 每集状态卡只改变剧情允许变化：伤、汗、灰、血、湿发、服装破损、情绪。
4. 镜头参考帧使用角色母卡 + 本集状态卡，而不是重新发明角色。
```

提示词要点：

```text
保持同一人物身份；保留脸型、眼睛距离、发际线、体型比例、标志饰品；
允许改变表情、姿态、镜头角度和剧情状态；
禁止换脸、换发型核心轮廓、改变年龄感、改变身高体量、随机改服装。
```

QC：
换脸、体型比例变化、服装等级错误、饰品消失、气质变成另一个角色，必须拒绝。

### TECH-REF-02 风格参考与材质参考分离

用途：
让作品风格统一，但不让风格参考吞掉角色身份或场景结构。

适用资产：
`style_reference`、角色卡、场景卡、道具卡、参考帧。

做法：

```text
1. 把风格图的用途限定为色彩、笔触、材质、光线、整体氛围。
2. 不让风格图决定角色身份、场景布局或道具形状。
3. 当模型支持参考强度时，用中低强度；当风格破坏结构时降低风格优先级。
4. 风格参考、身份参考、结构参考分开标注，不混写。
```

QC：
如果风格参考导致角色变脸、场景换结构、道具换形，必须降低风格权重或拆分参考。

### TECH-STRUCT-01 原图转草图 / 线稿复原

用途：
从已有画面抽出结构线稿，用于锁定建筑位置、空间透视、主体轮廓和构图。

适用资产：
`location_scene_master_reference` 的前置控制图、`reference_frame`、`shot_override`。

来自用户截图的可吸收方法：
先把原图转成黑白铅笔线稿；要求线条清晰、楼房位置和空间关系清晰；严格复原原图中的位置和状态；不清楚部分可以忽略；禁止随意添加内容。

标准提示模板：

```text
将参考图转化为黑白铅笔线稿 / clean line art control image。
只保留清晰建筑轮廓、主要透视线、地面边界、固定物位置、主体轮廓。
严格保持原图中建筑、道路、门窗、固定道具和主体的原始位置关系。
参考图中不清晰的远处小物体可以省略。
禁止添加新建筑、新道具、新人物、新文字、新标志。
白底，黑线，无色彩，无阴影，无渲染，无网格，无装饰。
```

QC：
线稿如果擅自改变构图、增加建筑、移动固定物、把不确定细节补成新内容，必须重做。

### TECH-STRUCT-02 ControlNet 结构控制

用途：
用边缘、深度、姿态、分割等结构控制图约束图像生成。

适用资产：
角色姿态、场景布局、道具形状、镜头参考帧。

控制图选择：

```text
Canny / Lineart:
  锁轮廓、建筑边缘、道具外形、构图。

Depth:
  锁前中后景、空间纵深、室内关系、人物与背景距离。

OpenPose / Pose:
  锁人物动作、肢体方向、打斗姿态、多人站位。

Segmentation:
  锁大块区域、建筑/天空/地面/人物/道具分区。

Multi-Control:
  同时需要结构和纵深时，组合 lineart/canny + depth；
  同时需要动作和构图时，组合 pose + depth 或 pose + lineart。
```

使用纪律：

```text
控制图越多，越要说明每张图只控制什么。
不同控制图不要互相矛盾。
强结构控制用于生产稳定性，弱风格控制用于审美统一。
控制图中的蓝线、箭头、字母、圆圈、UI 和标注不得进入最终画面。
```

### TECH-SCENE-01 场景俯视平面图

用途：
锁定空间布局、房间关系、门窗、家具、行动路线和固定道具位置。

适用资产：
`location_art_top_view`、场景控制包前置图、室内/院落/街巷等重复场景。

来自用户截图的可吸收方法：
用纯白背景和黑色线条画古代宅院平面视图；俯视视角；无透视；无色彩、阴影、渲染、网格；清楚划分厅堂、卧房、厨房、书房、庭院、净房等区域，并标出家具布置。

标准提示模板：

```text
生成一张场景俯视平面图，纯白背景，只使用黑色线条。
俯视角度，无透视，无阴影，无渲染，无网格，无颜色。
清晰标出房间 / 区域边界、门窗、固定家具、主要道具、行动路线和光源位置。
空间比例简洁可读，优先服务后续镜头连续性。
禁止画成装饰地图，禁止添加与剧本无关的区域。
```

QC：
如果俯视图和导演部 layout、camera map 或场景母图矛盾，必须拒绝。

### TECH-SCENE-02 场景九宫格多角度一致性

用途：
让同一空间从多个方向都保持同一身份，防止镜头切换后变成另一个房间或另一条街。

适用资产：
`location_orientation_grid_9`、重复出现的室内、院落、街巷、营地、城门、村口。

两种模式：

```text
空间方向模式:
  使用 NW / N / NE / W / C / E / SW / S / SE 九格，
  全部围绕同一个 center_anchor_id。

功能区域模式:
  当需要展示多个房间或区域时，可用 3x3 排列：
  每行一个房间或区域，每格一个视角或细节。
  这种模式只能作为场景卡参考，不能替代 location_orientation_grid_9。
```

提示词要点：

```text
九格必须属于同一场景、同一材质体系、同一时间光线逻辑。
每格需要说明视角、固定锚点、可见门窗、主要家具和禁止漂移项。
不依赖图片里的可读文字标签；精确标签写入 JSON 索引。
```

QC：
任一格像不同地点、家具换边、窗门消失、中心锚点变形或路径拓扑变化，必须拒绝。

### TECH-MOTION-01 轨迹导引图

用途：
把镜头运动或角色运动画在结构图上，给视频生成部或参考帧生成提供运动意图。

适用资产：
`reference_frame`、`shot_override`、视频生成部 I2V/FLF2V 前置参考。

来自用户截图的可吸收方法：
在线稿上添加蓝色轨迹线、箭头、A/B/C 点位，说明摄影机从地面出发，经过路径点，上升或绕行到目标位置；提示词中必须明确蓝线、箭头、圆圈和字母只是指导，不能出现在最终视频或图片中。

标准记录：

```text
motion_guide:
  guide_image_path:
  path_points:
    - A: 起始位置、景别、镜头高度、动作状态
    - B: 经过位置、转向、速度变化、目标主体
    - C: 结束位置、构图、视线方向
  movement_type:
    crane / dolly / pan / tilt / orbit / handheld / FPV / push-in / pull-out
  forbidden_rendered_guides:
    蓝色线条、箭头、圆圈、字母、点位标记、UI、轨迹标签
```

提示词负向约束：

```text
no blue guide lines, no arrows, no circles, no path labels, no letters A B C,
no annotation marks, no UI overlay, no storyboard labels in the final image.
```

QC：
如果最终图出现轨迹线、箭头、字母、点位、教程 UI 或截图水印，必须拒绝。

### TECH-CAMERA-01 运镜词库

用途：
给参考帧和视频生成交接描述镜头运动质感。

常用运镜：

```text
丝滑摇臂镜头:
  平稳、悬浮、纵深推进、从低到高或从高到低，适合展示空间规模。

手持摄影 + 运动模糊:
  呼吸感、临场感、轻微晃动、紧张、不稳定，适合追逐、战斗、惊慌。

FPV 运镜:
  第一人称、穿越、贴近障碍、速度感强，适合冲刺、飞行、坠落、极速移动。

orbit / 环绕:
  围绕角色或中心道具旋转，适合揭示关系、压迫感或神秘仪式。

push-in / pull-out:
  推近强调发现、情绪压迫；拉远强调孤立、失控或空间规模。
```

纪律：
美术部可以描述运镜意图和视觉参考，但不替代导演部的最终镜头调度和视频参数。

### TECH-STORY-01 故事板草图

用途：
用低成本草图先锁动作节奏、镜头类型、人物站位和运动方向。

适用资产：
复杂动作镜头、打斗、追逐、多人调度、空间易混乱镜头。

来自用户截图的可吸收方法：
用 4x3 或 3xN 分镜格；铅笔手绘草稿；少量彩色箭头标注运动轨迹；人物重点突出肢体张力；每格标注镜头类型、表演提示、声音/节奏提示。

标准提示模板：

```text
生成一张手绘风格故事板草图，使用 4x3 布局。
黑白铅笔线稿，快速、有力、松散但动作清楚。
每格突出角色肢体动作张力、站位、运动方向和镜头类型。
使用不同颜色箭头区分摄影机运动、角色运动和效果/冲击力。
不要追求精细光影和色彩；重点是动作逻辑、节奏和可剪辑性。
```

QC：
如果故事板只漂亮但看不出动作方向、镜头类型或前后关系，必须重做。

### TECH-STORY-02 导演故事板 / 全局表演板

用途：
为短片或一组镜头建立完整概念，指导整体表演、角色状态、场景推进和镜头连续性。

适用资产：
关键场景、多镜头段落、复杂表演段落、视频生成前总览。

标准结构：

```text
全局创意指引:
  时长、镜头数量、统一调色板、环境背景、整体情绪。

角色与风格参考:
  角色正面、背面、侧面、特写、放松姿态、服装与道具参考。

环境与场景设计:
  俯视图、运动路径、光源、关键道具、空间限制。

具体故事板:
  每个画面包含镜头类型、景别、运动方式、动作、情绪、声音/节奏提示。
```

QC：
导演故事板必须能让后续部门理解“这一段怎么演”，不能只是图片拼贴。

### TECH-MASK-01 遮罩局部重绘

用途：
修正局部错误，不破坏已通过 QC 的角色、场景和构图。

适用资产：
脸部微修、手部修复、道具形状修复、背景局部替换、去除错误标记。

做法：

```text
1. 保留原图作为结构和风格基底。
2. 只给错误区域画 mask。
3. 提示词说明 mask 内要改什么，mask 外必须保持不变。
4. 重要角色和道具修复后重新过连续性 QC。
```

限制：
遮罩是指导，不保证像素级完全贴合；精确标志、文字和符号仍优先后合成。

### TECH-PRECISION-01 精确标志 / 文字 / 纹章后合成

用途：
处理旗帜、印章、文字、纹章、法阵、地图标签等需要准确形状的内容。

做法：

```text
1. 先做 prop master card 或 SVG/透明 PNG 精确覆盖层。
2. 生图时只要求留出位置、材质和透视，不要求模型画准文字。
3. 最终用透明覆盖层或后期合成保证准确。
4. QC 比对覆盖层路径、尺寸、位置和透视。
```

QC：
模型自由生成的错字、伪文字、变形标志不能作为最终资产。

## 开源文生图项目学习成果

本节吸收优秀开源项目和论文中的可复用生产方法。它不绑定某个工具，也不把工具参数写死到项目中；美术部只把这些方法转化为资产规划、提示词结构、控制图选择、QC 标准和交接字段。

### TECH-PIPE-01 可复现生成管线记录

来源启发：
Diffusers 的 pipeline 思路、开源推理脚本和可组合模型组件。

用途：
让同一类资产能复现、能比较、能交接，而不是靠一次性玄学提示词。

适用资产：
所有需要批量生成、返工或跨线程协作的资产。

做法：

```text
1. 把生成条件拆成四层：模型可见提示词、参考图/控制图、输出格式契约、QC 标准。
2. 每条提示词必须记录 production_metadata、output_format、technique_profile。
3. 同一资产的候选图只改变一个主要变量：构图、风格、姿态、光线或状态。
4. 保留最终路径、隐藏版本库、废弃原因和下一次可复用经验。
```

QC：
如果一张图无法追溯到 prompt、参考图、控制图、输出规格和版本来源，不得进入正式资产。

### TECH-WORKFLOW-01 节点化工作流分层

来源启发：
ComfyUI 的节点化工作流、图式依赖和可保存 workflow 思维。

用途：
把复杂图片制作拆成可检查的阶段，避免一个提示词同时承担身份、结构、光影、风格、局部修复和精确文字。

适用资产：
复杂角色卡、重复场景、多人镜头、精确道具、镜头参考帧。

工作流分层：

```text
identity layer:
  角色身份、脸、发型、体型、服装核心轮廓。

structure layer:
  姿态、空间、透视、俯视图、线稿、深度、构图。

style layer:
  色彩、光线、材质、笔触、镜头质感。

state layer:
  每集状态、伤痕、污渍、湿度、破损、情绪。

precision layer:
  旗帜、徽记、文字、符号、局部可读图案。

qc layer:
  角色、空间、道具、风格、输出规格逐项验收。
```

纪律：
每层只负责自己的问题。身份参考不能改空间，结构控制不能改角色，风格参考不能改道具形状，精确叠加层不能靠模型自由发挥。

### TECH-ITER-01 探索矩阵与候选图审美筛选

来源启发：
Stable Diffusion WebUI、InvokeAI 和其他创作界面的网格探索、候选比较、局部迭代流程。

用途：
在早期探索阶段快速比较方向，但不让候选图污染正式资产系统。

适用资产：
风格板、角色早期方向、场景氛围方向、镜头参考探索。

做法：

```text
1. 每轮探索只比较一个变量：色彩、光线、材质、剪影、镜头角度或信息密度。
2. 为每个候选图写一句选择理由和一句淘汰理由。
3. 只有通过连续性检查的候选图才能晋升为正式参考。
4. 未选图进入隐藏版本库，不得散落在正式目录。
```

QC：
如果候选图只是“更漂亮”但破坏角色身份、空间关系、道具形状或导演意图，必须淘汰。

### TECH-CANVAS-01 画布化局部迭代

来源启发：
InvokeAI 画布工作流、inpainting/outpainting 和局部创作界面。

用途：
在不破坏已通过 QC 的整体资产时，修正局部错误、扩展画幅或补足边缘空间。

适用资产：
镜头参考帧、场景母图、角色表局部、道具细节。

做法：

```text
1. 锁定已通过 QC 的区域，不重生成整张图。
2. 对错误区域使用 mask 或局部 prompt。
3. outpainting 必须继承原图透视、光源、材质、镜头焦段和空间方向。
4. 局部修复后重新检查整图连续性。
```

QC：
局部修复不能让脸、手、服装、门窗、家具、光源、道具比例或画面方向产生二次漂移。

### TECH-REF-03 图像提示适配 / 多参考图权重分层

来源启发：
IP-Adapter 和图像提示适配方法，把图像作为独立提示条件，而不是把所有参考混成一张拼贴。

用途：
让参考图各司其职，稳定身份、结构、风格、材质或状态。

适用资产：
角色卡、风格板、场景母图、镜头参考帧、每集状态卡。

参考图分层：

```text
identity reference:
  角色身份、脸、发型、体型、标志物。

structure reference:
  构图、姿态、空间、透视、固定物位置。

style reference:
  色彩、光影、材质、笔触、整体气质。

state reference:
  伤痕、污渍、服装破损、天气、情绪状态。

material reference:
  金属、布料、皮革、石材、木纹、旧化程度。
```

提示词纪律：
必须说明每张参考图只控制什么、不能控制什么。风格图不能让角色变脸，身份图不能改变场景结构，结构图不能把控制线画进最终图。

### TECH-TRAIN-01 小样本主体个性化训练判断

来源启发：
DreamBooth、LoRA 等主体个性化和低秩微调实践。

用途：
判断什么时候值得为角色、道具、阵营符号或场景做个性化训练 / 小样本适配，而不是每次靠提示词硬撑。

适用资产：
长期主角、核心道具、重要阵营标识、重复出现的标志性场景。

启用条件：

```text
必须满足:
  资产会高频出现；
  文本提示词和参考图仍无法稳定；
  已有合法、可用、项目自有的训练参考；
  项目允许投入额外制作成本。

不得启用:
  参考图版权不清；
  只是单个镜头使用；
  训练会覆盖导演指定风格；
  角色身份还没有文本 canon 和母卡。
```

QC：
个性化模型不能替代资产卡。训练后仍必须使用 `identity_lock`、`output_format` 和连续性 QC。

### TECH-EDIT-01 指令式局部改稿

来源启发：
InstructPix2Pix 和指令式图像编辑方法。

用途：
把导演或用户的改稿意见转成局部、明确、可验收的图像编辑任务。

适用资产：
已接近通过 QC 的角色卡、场景图、道具图、视频参考帧。

改稿格式：

```text
keep:
  必须保持不变的身份、构图、场景、道具、光线和输出规格。

change:
  只改变一个主要问题，例如表情、污渍、袖口、道具位置、门的方向。

avoid:
  不得改变的相邻区域、不得新增的内容、不得出现的控制标记。

acceptance:
  改完后如何判断通过。
```

QC：
如果指令式改稿导致全图重绘、身份漂移、场景换位或道具替换，说明任务拆得太粗，必须改用 mask 或分层重做。

## 大片级美术设计学习成果

本节吸收商业级大片、温情电影、迪士尼动画、福克斯 / Blue Sky 系动画和经典动画制作流程中的可复用美术方法。严禁复制具体角色、镜头、商标、IP 造型或专有画风；只能学习设计逻辑。

### TECH-CINE-01 色彩剧本 / 情绪色彩弧线

来源启发：
动画和商业电影常用 color script，用色彩在全片层面组织情绪、节奏、场景转换和角色心理。

用途：
让每集或每个段落的色彩不是随机好看，而是随剧情推进形成可读情绪曲线。

适用资产：
风格板、场景母图、镜头参考帧、故事板、剪辑节奏参考。

做法：

```text
1. 按剧情段落列出情绪：安全、期待、孤独、危机、亲密、爆发、释怀。
2. 为每段定义主色、辅色、对比色、明度范围、饱和度范围和禁用色。
3. 关键转折点必须有可感知色彩变化，但不能破坏作品整体 palette。
4. 角色状态变化可以通过色温、边缘光、阴影密度和背景色关系表达。
```

提示词要点：
写“清晨低饱和暖色、室内柔和琥珀光、转折后冷青阴影压低安全感”，不要写“某某电影同款配色”。

QC：
如果相邻段落色彩无叙事理由地跳变，或同一地点在连续镜头里色温逻辑断裂，必须退回。

### TECH-CINE-02 大片级美术层级设计

用途：
建立商业大片式的可读视觉层级，让观众第一眼知道看什么、世界有多大、角色与环境的权力关系是什么。

适用资产：
大型场景、战场、城市、宫殿、飞船、怪物巢穴、史诗建立镜头。

设计层级：

```text
primary read:
  一眼读懂的最大轮廓、主光源、主构图线、角色或地标。

secondary read:
  中景建筑、阵营旗帜、道路、门、桥、主要群众体块。

tertiary texture:
  近处材质、局部旧化、地面痕迹、小道具。

negative space:
  留白、雾、天空、暗部或纯色块，用来让主体可读。
```

做法：
先画大形和光影，再补材质；先锁前中后景，再谈细节；远景用体块和剪影，不要把每个小物体都画成主角。

QC：
如果整张图每个区域同等锐利、同等高细节，或者主体被背景纹理吞掉，必须拒绝。

### TECH-CINE-03 温情电影触感设计

用途：
为亲情、友情、成长、治愈、怀旧或生活流故事建立温暖可信的美术质感。

适用资产：
家庭空间、童年记忆、日常道具、亲密对话场景、温情结尾。

设计原则：

```text
human scale:
  机位更贴近人物身高和手部动作，空间不过度宏大。

tactile props:
  道具有被使用过的痕迹：磨边、折痕、补丁、手写、褪色、旧木纹。

soft contrast:
  低到中等对比，柔和边缘光，阴影有空气感。

memory palette:
  使用有记忆感的暖色、低饱和色、自然材质色，而不是糖水式全画面金黄。

emotional object:
  给一个小物件承载关系变化，例如杯子、围巾、玩具、旧照片、钥匙。
```

QC：
温情不是磨皮和泛黄滤镜。若画面没有可触摸的生活细节、人物尺度和关系道具，只是柔焦漂亮图，必须重做。

### TECH-ANIM-01 动画角色吸引力与形状语言

来源启发：
经典动画角色设计的 appeal、清晰轮廓、形状对比和姿态可读性。

用途：
让角色一眼可辨、适合连续表演，并能在不同镜头距离下保持身份。

适用资产：
角色母卡、表情表、动作故事板、动画风格参考帧。

形状语言：

```text
circle / round:
  亲和、柔软、幼态、安全、温情。

square / block:
  稳定、可靠、力量、迟钝、压迫或守护。

triangle / sharp:
  速度、危险、聪明、紧张、攻击性或精致。
```

做法：
主角、配角、反派、喜剧角色必须有不同的大轮廓和姿态习惯。先用黑色剪影测试可读性，再进入服装纹理。角色表必须包含中性站姿、情绪姿态、动作极限和脸部关键表情。

QC：
如果角色只靠脸漂亮区分，剪影、发型、体型、服装轮廓和姿态习惯没有差异，必须重做。

### TECH-ANIM-02 主题化视觉开发流程

来源启发：
商业动画视觉开发会在正式资产制作前反复探索角色、色彩、设计、构图和故事主题，让每个视觉选择服务主题。

用途：
把“好看风格”变成“服务故事主题的视觉系统”。

适用资产：
美术方向说明、风格圣经、角色卡、场景卡、色彩板。

流程：

```text
theme statement:
  这部作品视觉上要让观众感到什么。

research board:
  真实文化、时代、材质、地域、建筑、服装、自然环境和生活细节。

shape palette:
  本作品常用形状、禁用形状、角色阵营形状差异。

color script:
  情绪段落色彩弧线。

asset bible:
  把探索结果落成角色、场景、道具、材质、光影和 QC 规则。
```

QC：
如果风格板只是漂亮图拼贴，不能解释角色、场景、色彩、材质为何服务主题，不能进入正式制作。

### TECH-ANIM-03 2D 经典造型到 3D 资产的翻译

来源启发：
Fox / Blue Sky 系动画和其他 3D 动画常把 2D 经典图形、漫画感造型和夸张表演翻译成 3D 体块、材质与动画资产。

用途：
当项目需要动画感、漫画感、家庭喜剧或温情冒险质感时，让造型夸张但仍能进入 3D / 视频生成。

适用资产：
动画角色卡、群像角色组、道具卡、风格板、故事板。

翻译原则：

```text
2D silhouette first:
  先保证平面剪影可读，再建立 3D 体块。

graphic simplification:
  保留大形和节奏，减少无叙事意义的小纹理。

expressive proportions:
  夸张头身比、手脚比例或道具体量，但必须在同一世界规则内统一。

material restraint:
  材质服务形状，不让真实纹理压垮图形感。

ensemble contrast:
  群像角色必须在身高、体块、节奏、服装大形和姿态上形成互补。
```

QC：
如果 3D 化后角色失去原本的大形节奏，或真实材质让造型变脏变碎，必须回到低模和剪影阶段重做。

### TECH-COPYRIGHT-01 商业风格吸收纪律

用途：
学习商业大片和知名动画时保护项目原创性，避免提示词和资产产生侵权式模仿。

必须遵守：

```text
禁止:
  使用具体电影名、角色名、品牌名、工作室名作为风格指令；
  复刻受保护角色造型、服装、配色、标志、场景布局或镜头；
  把截图、海报、剧照当成可直接生成的内容目标。

允许:
  抽象成原创设计原则；
  学习色彩剧本、造型层级、剪影可读性、材质节制、情绪触感；
  引用公开方法来源做学习锚点；
  为项目自己的角色、世界观和导演意图重建视觉规则。
```

改写示例：

```text
不要写:
  in Disney style, like a Pixar movie, Fox animation style, Avatar-like world.

改写为:
  family animated feature visual development, clear appealing silhouettes,
  warm emotional color script, readable shape language,
  stylized but physically believable materials, strong foreground-midground-background staging.
```

## 技巧选择矩阵

```text
资产类型: character_master_card
优先技巧: TECH-REF-01
可选技巧: TECH-REF-02, TECH-REF-03, TECH-ANIM-01, TECH-MASK-01
必须输出: 多视角、细节裁切、透明抠图、尺度参考

资产类型: location_art_top_view
优先技巧: TECH-SCENE-01
可选技巧: TECH-STRUCT-01, TECH-STRUCT-02
必须输出: 俯视平面、门窗/家具/行动区、导演部空间证据引用

资产类型: location_orientation_grid_9
优先技巧: TECH-SCENE-02
可选技巧: TECH-SCENE-01, TECH-STRUCT-02
必须输出: 九格同场景、中心锚点、每格可见锚点、禁止漂移项

资产类型: reference_frame / shot_override
优先技巧: TECH-STORY-01, TECH-MOTION-01, TECH-CINE-02
可选技巧: TECH-REF-01, TECH-REF-03, TECH-STRUCT-02, TECH-CAMERA-01, TECH-CANVAS-01
必须输出: 16:9、前中后景、镜头方向、动作状态、禁止导引线入画

资产类型: style_reference
优先技巧: TECH-REF-02, TECH-CINE-01, TECH-ANIM-02
可选技巧: TECH-CINE-03, TECH-ANIM-03, TECH-MASK-01
必须输出: 色彩、材质、光线、镜头质感、禁用风格、情绪色彩弧线

资产类型: precision prop / emblem / text-like prop
优先技巧: TECH-PRECISION-01
可选技巧: TECH-STRUCT-01, TECH-MASK-01
必须输出: 精确覆盖层或线稿控制，不依赖模型自由绘制

资产类型: warm emotional scene / family interior
优先技巧: TECH-CINE-03, TECH-CINE-01
可选技巧: TECH-CANVAS-01, TECH-EDIT-01
必须输出: 人物尺度、触感道具、生活痕迹、柔和但不糊的光影

资产类型: animated feature character group
优先技巧: TECH-ANIM-01, TECH-ANIM-03
可选技巧: TECH-REF-03, TECH-STORY-01
必须输出: 群像剪影差异、形状语言、姿态习惯、低模比例验证

资产类型: production workflow / batch generation
优先技巧: TECH-PIPE-01, TECH-WORKFLOW-01
可选技巧: TECH-ITER-01, TECH-TRAIN-01
必须输出: 可追溯管线、变量控制、候选筛选理由、隐藏版本记录
```

## 参考图角色命名

提示词中必须明确每张输入图的角色，不要只写“参考图”。

```text
Image 1 = identity reference:
  只用于角色身份、脸、发型、体型、标志物。

Image 2 = structure reference:
  只用于构图、透视、建筑位置、道具位置。

Image 3 = motion guide:
  只用于镜头路径或角色运动，导引线不得入画。

Image 4 = style reference:
  只用于色彩、光线、材质、笔触和整体气质。

Image 5 = mask:
  只用于局部编辑范围。
```

## 通用负向约束库

按需要追加，不要机械全塞。

```text
控制图禁入画:
  no blue guide lines, no arrows, no circles, no letters, no labels,
  no route marks, no UI overlay, no tutorial screenshot, no watermark.

角色一致性:
  no face swap, no age change, no changed hairstyle silhouette,
  no changed body ratio, no random costume redesign, no missing signature accessory.

场景一致性:
  no moved doors, no swapped windows, no relocated fixed furniture,
  no changed anchor object, no alternate room layout, no impossible perspective.

故事板草图:
  no polished poster rendering, no decorative illustration replacing storyboard,
  no unclear action direction, no missing camera type.

宽景信息预算:
  no equal-detail rendering across the whole frame, no over-detailed distant figures,
  no granular crowd texture, no particleized stone, no AI speckle,
  no visual information overload.
```

## 交接要求

交给提示词部和视频生成部时，不能只交最终图。必须交：

```text
canonical image path
technique_profile
reference_image_roles
control_inputs
forbidden_rendered_guides
copy_ready prompt
negative prompt
QC status
downstream usage
```

## 公开资料锚点

这些链接用于追溯通用方法来源。实际项目执行时仍以本 skill 的资产契约、导演部空间证据和项目连续性规则为准。

```text
ComfyUI GitHub:
  https://github.com/Comfy-Org/ComfyUI

AUTOMATIC1111 Stable Diffusion WebUI:
  https://github.com/AUTOMATIC1111/stable-diffusion-webui

InvokeAI GitHub:
  https://github.com/invoke-ai/InvokeAI

Hugging Face Diffusers GitHub:
  https://github.com/huggingface/diffusers

ControlNet paper:
  https://arxiv.org/abs/2302.05543

Hugging Face Diffusers ControlNet guide:
  https://huggingface.co/docs/diffusers/using-diffusers/controlnet

IP-Adapter paper:
  https://arxiv.org/abs/2308.06721

Hugging Face Diffusers IP-Adapter guide:
  https://huggingface.co/docs/diffusers/using-diffusers/ip_adapter

DreamBooth paper:
  https://arxiv.org/abs/2208.12242

InstructPix2Pix paper:
  https://arxiv.org/abs/2211.09800

OpenAI Image generation guide:
  https://developers.openai.com/api/docs/guides/image-generation

OpenAI GPT Image prompting guide:
  https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

Walt Disney Animation visual development:
  https://disneyanimation.com/process/visual-development/

Walt Disney Animation visual development artist:
  https://disneyanimation.com/team/visual-development-artist/

Pixar in a Box:
  https://www.pixar.com/pixar-in-a-box

Khan Academy Pixar color scripts:
  https://www.khanacademy.org/computing/pixar/art-of-lighting/introduction-to-virtual-lighting/v/colorscripts

Khan Academy Pixar art of lighting:
  https://www.khanacademy.org/computing/pixar/art-of-lighting

Disney / Pixar Finding Nemo color script:
  https://video.disney.com/watch/journey-into-finding-nemo-s-color-script-color-script-chronicles-pixar-5d6ada83eb684ebd6b4f2a72

Blue Sky Studios and The Peanuts Movie:
  https://svatheatre.com/events/blue-sky-studios-and-the-making-of-the-peanuts-movie/

SIGGRAPH blog on The Peanuts Movie:
  https://blog.siggraph.org/2015/10/behind-the-peanuts-movie.html/
```
