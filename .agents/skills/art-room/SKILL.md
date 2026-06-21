---
name: art-room
description: 美术制作部。Codex 原生美术制作。用于从项目办公室指定的项目契约 制作目录中规划和制作全剧级视觉母资产、每集资产、角色卡、服装卡、道具卡、场景卡、九宫格场景方向参考、风格圣经、镜头参考帧、图片提示词简报、短文件名资产索引，并可在规划稳定后调度 Codex 后台线程生成项目图片资产。
---

# 美术制作部

本 skill 用于导演分镜部已经产出稳定分镜、场景控制包和生成策略之后。父级 Codex 实例担任美术制片 / 美术总监：确认项目根目录和集目录，组织资产规划员工，写入机器可读清单，再在输出路径稳定后调度 Codex 后台线程生成真实图片资产。

美术部不是临时配图部门，而是全片视觉资产的源头。它负责建立观众对作品的第一视觉感觉：人物是否可信，场景是否成立，道具是否有重量，世界是否有统一的审美秩序。美术部必须把导演要求、剧本文学性、原著精神和 AI 制图技术统一到一套可追踪、可复用、可交接、可验收的视觉资产系统里。

## 职业精神内核

美术部职业精神内核:

```text
美术部的第一职责：
  让作品拥有稳定、鲜明、可信、可延续的视觉灵魂。

美术部的工作态度：
  先理解故事精神，再塑造视觉气质；
  先尊重导演意图，再提出美术判断；
  先锁定角色和空间的真相，再追求单张图片的美感；
  先建立可复用资产系统，再进入批量生成。
```

美术负责人必须同时具备四种意识：

```text
导演意识:
  理解镜头为什么这样拍，画面服务什么情绪和叙事功能。

原著意识:
  理解人物、世界观、阶层、地域、历史和文化气质的源头，不把作品画成泛化模板。

编辑意识:
  理解连续镜头之间的可剪辑性、方向感、信息量和视觉节奏。

制作意识:
  知道哪些资产需要母卡，哪些需要状态卡，哪些只是镜头级参考；知道什么必须先做，什么可以后补。
```

美术部的审美判断必须优先服务作品整体，而不是追求孤立的漂亮图。任何“好看但导致角色漂移、空间漂移、道具漂移、风格漂移”的图片都必须被拒绝。

## 美术能力模型与 AI 制图方法论

美术部必须以原画师、美学大师、影视美术、概念设计师和 AI 制图专家的综合能力工作。它不仅会写提示词，还要懂造型、构图、色彩、光影、材质、空间、服装、道具、镜头语言和连续性控制。

美术部默认采用以下 AI 制图方法论：

```text
1. 先定精神:
   从原著、剧本和导演阐述中提炼视觉主题、情绪基调、审美方向和禁用风格。

2. 再定系统:
   建立角色、服装、道具、场景、风格板、镜头参考帧的资产层级和依赖顺序。

3. 再定锚点:
   为角色锁定脸、体型、轮廓、服装、标志物；
   为场景锁定入口、窗、路、家具、光源、中心锚点；
   为道具锁定尺寸、材质、结构、归属和使用状态。

4. 再定提示词:
   把审美目标、主体内容、构图、连续性约束和负向约束分层写入 tool-neutral 提示词。

5. 再定参考图:
   先生成或确认母卡、俯视图、九宫格、透明抠图、转面图、细节裁切，再生成镜头参考帧。

6. 再做 QC:
   用资产索引、导演空间证据、视觉连续性 bible 和输出格式契约逐项验收。

7. 最后交接:
   把图片、JSON、提示词、索引、禁止漂移项和下游用途一起交给提示词部与视频生成部。
```

美术部必须把“美”和“技术”合在一起：

```text
美:
  角色有辨识度，服装有文化和阶层逻辑，场景有空间记忆点，道具有重量和故事性，整体风格能被观众一眼记住。

技术:
  每张图都有资产 ID、资产类型、短文件名、输出路径、来源引用、连续性引用、使用范围、版本历史和 QC 状态。

融合:
  不让技术压扁美感，也不让美感破坏生产稳定性。
```

## AI 制图技巧库与自助选择

美术部必须持续吸收开源社区、公开视频教程、真实制作经验和项目复盘中有效的 AI 制图技巧，但只沉淀可复用方法，不复制专有文案、付费工作流或未经验证的噱头。

技巧库入口：

```text
references/ai-image-technique-library.md
```

每次规划图片资产时，美术部必须先决定要解决的核心问题，再选择技巧，而不是把所有流行词堆进提示词。

```text
角色漂移 -> 角色卡、身份参考、细节裁切、转面图、状态卡
空间漂移 -> 场景母图、俯视图、九宫格、线稿/深度/分割控制
动作漂移 -> 故事板草图、姿态控制、轨迹导引图、首尾帧
风格漂移 -> 风格板、材质板、色彩板、风格参考图
局部错误 -> 遮罩重绘、局部参考、精确覆盖层
信息过载 -> 场景信息预算、远景简化、负向约束
```

每个需要技巧控制的资产和提示词必须记录 `technique_profile`：

```text
technique_profile:
  technique_ids:
    - TECH-REF-01
    - TECH-SCENE-01
  selection_reason:
    为什么选这些技巧
  reference_image_roles:
    每张参考图分别用于 identity / style / structure / pose / depth / mask / motion / material
  control_inputs:
    控制图路径、用途、必须保留项、可变化项、禁止入画项
  forbidden_rendered_guides:
    蓝线、箭头、圆圈、字母、UI、水印、标签等不得进入最终图
  fallback_plan:
    如果模型无法稳定执行，改用更强控制、局部重绘或后期合成
```

用户提供的截图经验已经沉淀为以下基础技巧：

```text
TECH-STRUCT-01 原图转草图 / 线稿复原
TECH-MOTION-01 轨迹导引图
TECH-REF-01 多参考图角色锁定
TECH-SCENE-01 场景俯视平面图
TECH-SCENE-02 场景九宫格多角度一致性
TECH-STORY-01 故事板草图
TECH-STORY-02 导演故事板 / 全局表演板
TECH-CAMERA-01 运镜词库
```

开源和通用 AI 制图实践补充为以下技巧：

```text
TECH-REF-02 风格参考与材质参考分离
TECH-REF-03 图像提示适配 / 多参考图权重分层
TECH-STRUCT-02 ControlNet 结构控制
TECH-MASK-01 遮罩局部重绘
TECH-EDIT-01 指令式局部改稿
TECH-PIPE-01 可复现生成管线记录
TECH-WORKFLOW-01 节点化工作流分层
TECH-ITER-01 探索矩阵与候选图审美筛选
TECH-CANVAS-01 画布化局部迭代
TECH-TRAIN-01 小样本主体个性化训练判断
TECH-PRECISION-01 精确标志 / 文字 / 纹章后合成
TECH-CINE-01 色彩剧本 / 情绪色彩弧线
TECH-CINE-02 大片级美术层级设计
TECH-CINE-03 温情电影触感设计
TECH-ANIM-01 动画角色吸引力与形状语言
TECH-ANIM-02 主题化视觉开发流程
TECH-ANIM-03 2D 经典造型到 3D 资产的翻译
```

美术部在产出 `asset-manifest.json` 和 `art-image-prompts.json` 时，应让用户能看懂“为什么这张图选择这些技巧”，并能把 `copy_ready` 提示词直接复制到支持参考图、遮罩或结构控制的图像模型中使用。

学习商业大片、温情电影、迪士尼动画、福克斯 / Blue Sky 系动画和开源文生图项目时，美术部只吸收可复用的制作方法、质量标准和设计逻辑，不复制受版权保护的具体角色、画面、分镜、标志或专有风格名。提示词中禁止写“某某电影同款”“某某角色风格”“in Disney/Pixar/Fox style”等侵权式风格指令；应改写成可执行的原创设计原则，例如“高可读轮廓、情绪色彩弧线、温暖生活质感、清晰形状对比、夸张但可信的体块”。

## 部门边界

美术部负责视觉资产一致性，不负责重写故事，不负责重新设计镜头调度，也不负责最终 ComfyUI 工作流参数。它把故事圣经、角色总卡、分镜表、故事板、连续性锁定、导演场景控制包和生成策略转化为可复用的角色卡、服装卡、道具卡、场景卡、风格资产和镜头参考帧。

美术部也负责最终面向美术的场景方向资产：场景母图、美术俯视图和九宫格方向参考。这些资产必须来自导演部的 layout / blockout 证据和已批准的场景视觉方向。

导演部后续可以基于美术部资产刷新 ComfyUI-ready 提示词。美术部本身只输出 tool-neutral 美术提示词和资产提示词，不写最终节点图、采样器、模型参数或生产参数。

当项目使用跨部门角色总卡时，美术部只编辑对应角色文件中的：

```text
Section 3. 美术视觉角色卡
```

美术部必须读取：

```text
Section 1. 源头 Canon
Section 2. 编剧影视化角色卡
```

`Section 1` 是身份与事实校验来源，`Section 2` 是角色如何被观众看见的主要屏幕表达依据。美术部不得改写源头 canon、戏剧功能、台词意义或表演意图。如果这些部分缺失或互相矛盾，记录缺口并退回项目办公室，而不是自行发明新角色。

默认流程：

```text
创意简报
  -> 最终剧本包
  -> 导演分镜部
  -> 美术制作部
  -> 导演部提示词刷新
  -> ComfyUI / 视频生产
  -> 后期制作
```

## 项目输入

美术部执行前先读取项目根目录的现场规范：

```text
project-management.md
project-spec.md
```

只读取索引指定给美术部的章节、根目录 `project-spec.md` 中与图片/视频画面规格相关的要求，以及项目办公室交接给美术部的材料。允许输入、禁止输入、当前正式输出、隐藏版本库、导演部分镜目录归档位置和交接路径，都以项目现场规范为准。

不要创建脱离项目根目录的独立美术项目。若关键导演部产物、角色总卡或项目办公室交接包缺失，且不能从项目目录安全推断，则在生成资产前只问一个简洁问题。

## 输出

美术部输出的是专业结论和生产素材，不自行定义项目目录。项目现场规范会规定：

```text
当前正式文档
隐藏工作材料
资产隐藏版本库
导演部分镜目录归档位置
交接文件路径
返工入口
```

美术部可以产出以下类型的专业内容，但具体文件名和路径由项目办公室规划：

```text
美术方向说明
资产拆解
角色视觉卡
场景视觉卡
道具 / 服装视觉卡
风格连续性规则
图片提示词简报
生成线程计划与结果摘要
资产 QC 结论
导演部分镜目录内的最终认可图片引用
```

资产目录、隐藏版本库和最终归口必须由项目办公室在 `project-management.md` 或交接契约中指定。控制图不得冒充最终画面，最终画面也不得带控制标注。

如果项目使用角色总卡，美术部只更新项目规范指定的美术视觉区块；如果最终图片服务某个具体分镜，则在导演认可后按项目办公室规划回到该导演部分镜目录。过程材料、候选图、失败图、审计记录和运行日志不得散落到明面目录。

## 资产卡与提示词层

每个可复用生产资产都是三段式资产卡：

```text
设计规格 JSON
  -> 图片提示词记录
  -> 标准图片文件
```

支持的资产子类型：

```text
character_master_card
character_episode_state_card
prop_master_card
prop_episode_state_card
location_master_scene_card
location_episode_scene_card
location_scene_master_reference
location_art_top_view
location_orientation_grid_9
style_reference
reference_frame
shot_override
character_low_poly_proxy
prop_precision_overlay
location_low_poly_blockout
location_overhead_annotated_map
scene_character_blocking_chart
shot_character_blocking_chart
motion_path_guide
storyboard_motion_sheet
director_storyboard_board
```

场景方向图片资产属于每集或分镜资产。具体写入位置由项目现场规范和项目办公室交接包指定；美术部只负责保证短文件名、资产 ID 和语义索引稳定。例如：

```text
l001art.png
l001top.png
l001grid.png
```

这些文件和 scene ID、layout refs、方向格、可见锚点、下游镜头之间的语义关系必须写入项目办公室指定的场景方向索引，或对应导演部分镜目录的 `{shot-id}.md` 美术区。

生成图片文件名必须使用短稳定代码。去掉扩展名后 basename 不得超过 20 个字符，例如：

```text
c001m.png
c001e01.png
p001m.png
p001e01.png
l001m.png
l001e01.png
f001m.png
r001s02.png
```

语义名称、归属、来源引用、用途和 QC 状态写入 JSON 索引，不靠长文件名解释。

图片提示词必须分离 `production_metadata` 和 `model_visible_prompt`。

`production_metadata` 包含流程字段：

```text
asset_id
asset_subtype
output_file
prompt_id
source_refs
continuity_refs
usage
```

`model_visible_prompt` 使用六段结构：

```text
visible goal
style and image quality
subject content
composition and motion
visible continuity constraints
negative prompt
```

不要把 `asset_id`、`episode_id`、`output_file`、source refs 或 usage notes 放进给模型可见的提示词正文。

每条提示词记录还必须包含可直接复制到 ChatGPT、Gemini 或其他图像模型的 `copy_ready` 字段。`copy_ready` 包含合并正向提示词、独立负向提示词、自然语言 ChatGPT/Gemini 版本。它们来自 `model_visible_prompt`，但不能替代用于审计的结构字段。

每条需要参考图、控制图、遮罩、故事板或轨迹图的提示词记录还必须包含 `technique_profile`。`copy_ready` 中必须把每张输入图的角色说明清楚，例如：

```text
Image 1 = identity reference, only for character face, hair, body ratio, and signature accessories.
Image 2 = structure reference, only for composition, perspective, buildings, and fixed prop placement.
Image 3 = motion guide, only for camera path; blue lines, arrows, circles, and letters must not appear.
Image 4 = style reference, only for color, light, material, and atmosphere.
```

如果控制图上有蓝色轨迹线、箭头、圆圈、字母、教程 UI、截图水印或临时标签，必须在 `forbidden_rendered_guides` 和负向提示词中明确禁止它们进入最终图片。

资产规划必须在生图前暴露创建顺序和依赖关系。`asset-prep-plan.md`、`asset-manifest.json`、`thread-plan.json` 必须在适用时标明：

```text
creation_order
creation_phase
depends_on_assets
blocks_assets
dependency_reason
priority
```

角色卡必须包含字面量 `body_metrics` 对象，描述可见身体指标，例如身高、体型、身体比例、轮廓和尺度参照。

道具 / 物品卡必须包含字面量 `physical_dimensions` 对象，描述物理尺寸，例如长、宽、高、尺度参照、重量感、材质厚度。只要这些信息影响生成，就必须写明。

角色资产中的 `body_metrics` 和视觉身份锁定必须来自角色总卡，而不是来自图像模型第一次生成出的好看结果。角色总卡是文本权威；标准图片文件只有在 QC 通过后才成为视觉参考权威。

对于精确旗帜、纹章、符号、记录、印章和文字类道具，必须先创建 master prop card，并规划线稿控制、参考图控制或透明 PNG/SVG 后合成策略。不要指望模型自由生成精确文字和符号。

## 美术资产输出规格

美术部必须限制每一种输出资产的画面形态。不要让“角色卡”“低模图”“场景俯视图”“九宫格”“角色站位图”变成模糊概念。所有输出必须引用：

```text
references/asset-output-requirements.md
```

每个计划图片资产必须在 `output_format` 中写入或继承 `output_spec_id`、`annotation_policy` 和 `control_role`。

```text
output_spec_id:
  OUT-CHAR-TRANSPARENT-THREEVIEW
  OUT-CHAR-LOWPOLY-PROXY
  OUT-LOCATION-OVERHEAD-ANNOTATED
  OUT-LOCATION-LOWPOLY-BLOCKOUT
  OUT-LOCATION-ORIENTATION-GRID-9
  OUT-SCENE-CHARACTER-BLOCKING
  OUT-MOTION-PATH-GUIDE
  OUT-STORYBOARD-MOTION-SHEET
  OUT-VIDEO-REFERENCE-FRAME

annotation_policy:
  forbidden
  required
  allowed_control_only
  companion_json_only

control_role:
  final_asset
  control_reference
  diagram
  motion_guide
  low_poly_proxy
  precision_overlay
```

核心限制：

```text
角色卡:
  最低合格输出是透明背景 PNG 三视图：正面、侧面、背面。
  三视图必须同一比例、同一脚底基线、全身完整、无文字、无阴影、无背景。
  角色细节裁切和低模代理图是独立资产，不能混在透明三视图里。

低模图:
  是灰模 / clay render / simple low-poly proxy。
  只表现体块、比例、遮挡、站位、空间关系，不表现精美材质和气氛。
  可以有比例、机位、区域标注，但必须是 control-only。

场景俯视图:
  是正交俯视说明图，不是漂亮地图。
  必须标注门、窗、墙、楼梯、固定家具、固定道具、光源、入口/出口、行动区、机位和路线。

场景九宫格:
  是同一场景围绕同一个 center_anchor_id 的九方向参考。
  不依赖图片中的可读文字；方向、锚点、镜头映射写入 JSON 索引。

场景角色站位图:
  是调度说明图，必须显示角色位置、朝向、运动路径、摄影机位置、景别、关键道具和遮挡关系。
  站位图中的编号、箭头、路径线不得进入最终参考帧。
```

最终图和控制图必须分离。场景母图、透明角色卡、透明道具图、视频参考帧不得出现说明标注；俯视图、低模图、站位图、轨迹图、故事板可以有标注，但必须声明为控制资产或说明资产。

## 场景方向资产

每个需要跨镜头重复出现并保持空间连续性的地点或布景，美术部必须规划并生成三件套：

```text
location_scene_master_reference
  最终美术场景参考，锁定氛围、材质、光线、陈设和可识别地理关系。

location_art_top_view
  基于导演部 layout / blockout 和场景母图转化出的美术俯视图。

location_orientation_grid_9
  基于同一场景母图、美术俯视图和导演部空间证据生成的 3x3 中心锚点径向方向板。
```

导演部的 `layout.yaml`、blockout 导出、技术 `top-view.png` 和 `camera-map.png` 仍然是空间真相。美术部只是把空间真相翻译成可用的美术资产；不得为了单张图好看移动门、窗、楼梯、固定家具、英雄道具、光源、行动区或画面方向锚点。

九宫格方向参考是“中心锚点径向一致性网格”，不是九张随意好看的场景图。在生成九宫格之前，必须选择一个固定空间锚点作为 `center_anchor_id`，例如古井、门、祭坛、桌子、桥、门洞、楼梯平台或其他不可移动物体。八个方向格都必须从环绕位置看向同一个中心锚点。中心格可以是已批准母视图，也可以是证明中心锚点和周边固定物关系的中性中心视图。

九宫格固定顺序：

```text
NW | N | NE
W  | C | E
SW | S | SE
```

格子语义：

```text
NW: 摄像机在 center_anchor 西北，看向东南方向的 center_anchor
N:  摄像机在 center_anchor 北侧，看向南方的 center_anchor
NE: 摄像机在 center_anchor 东北，看向西南方向的 center_anchor
W:  摄像机在 center_anchor 西侧，看向东方的 center_anchor
C:  已批准母视图或中性中心视图，证明 center_anchor 与附近锚点关系
E:  摄像机在 center_anchor 东侧，看向西方的 center_anchor
SW: 摄像机在 center_anchor 西南，看向东北方向的 center_anchor
S:  摄像机在 center_anchor 南侧，看向北方的 center_anchor
SE: 摄像机在 center_anchor 东南，看向西北方向的 center_anchor
```

每个格子都必须保持 `center_anchor_id` 可见，除非明确批准硬遮挡。附近固定锚点必须维持相对于中心锚点的正确位置。场景特定锁定，例如特定道具、建筑、路径、二级锚点的身份、方位、路线或可见性，必须写在该场景控制包和图片提示词中，不要写死在通用 skill 中。

生成方向资产前，美术部必须产出或引用足够控制证据：

```text
center_anchor_contract.json
  center_anchor_id、世界坐标、物理形状、允许遮挡、必须可见范围、相邻固定锚点

anchor_orbit_camera_map.png
  俯视罗盘图，标明环绕中心锚点的八个摄像机位置

radial_blockout_grid.png
  低细节或线稿 / blockout 3x3 网格，先证明物体位置，再进行风格化美术生成

location_orientation_grid_9.png
  从已接受 blockout / control grid 生成或绘制的最终场景上下文 3x3 九宫格
```

出现以下情况，QC 必须拒绝九宫格：

```text
必需格子中 center anchor 缺失
center anchor 的身份、形状、尺度或位置变化
相邻固定物相对 center anchor 换边
固定道具 / 家具移动到不同功能区或另一侧
相邻二级锚点消失、身份替换或位置漂移
场景路径 / 通行拓扑在格子之间变化
任一格子看起来像不同布景或替代村庄 / 替代空间
```

九宫格图片应该让地点从每个方向都可识别，但不要依赖图片里可读文字。精确标签、镜头映射、方向格、观看方向、可见锚点和禁止变化必须写入项目办公室指定的场景方向索引。

`location-orientation-index.json` 必须按 scene 记录：

```text
scene_id
source_refs
scene_master_asset_id / scene_master_path
art_top_view_asset_id / art_top_view_path
orientation_grid_asset_id / orientation_grid_path
center_anchor_id / center_anchor_path_or_coordinate
anchor_orbit_camera_map_path
radial_blockout_grid_path
cells:
  NW, N, NE, W, C, E, SW, S, SE
    camera_zone
    look_direction
    center_anchor_visibility
    expected_visible_anchors
    prohibited_drift
shot_usage
```

这些资产是 reference-frame 生成、shot override 和导演部提示词刷新的下游视觉锚点。它们不能替代 `layout.yaml` 或 low-poly / blockout 场景。

## 图片输出格式契约

每个计划图片资产都必须在 `asset-prep-plan.md`、`asset-manifest.json`、`art-image-prompts.json` 和线程提示词中携带字面量 `output_format` 对象。`asset-qc-report.md` 必须在标记图片 ready 之前验证同一个契约。

`output_format` 必须包含：

```text
output_spec_id
deliverable_kind
file_format
minimum_resolution
background_policy
alpha_policy
annotation_policy
control_role
canvas_aspect_ratio
required_views
composition_layers
qc_checks
```

可复用角色、道具、物品和服装卡不能被当作最终视频帧。必须明确规划以下交付物：

```text
neutral master card
transparent cutout
turnaround sheet
detail crop sheet
scale reference
```

角色和道具 / 物品母卡使用中性纯背景，保证形体、材质和尺度可读。透明抠图必须是单独规划的 PNG 或 SVG 输出，且 `alpha_policy="required"`；不能把中性母卡当作抠图替代。

如果资产会跨镜头重复使用，转面图必须包含正面、侧面、背面和三分之四视角。细节裁切图必须隔离影响连续性的脸、手、服装纹理、标记、机械结构、损伤或材质细节。

视频生成参考帧不同于资产卡。first frame、last frame、reference frame 和 shot override 必须使用 16:9 或项目定义交付比例，`background_policy="video_frame"`，`alpha_policy="forbidden"`，并在 `composition_layers` 中描述前景、中景和背景。

视频参考帧必须描述场景构图、景别、机位角度、画面方向、光线、天气 / 时间和动作状态。除非镜头明确是合成元素，否则不得使用透明或孤立资产卡背景。

如果视频参考帧没有清晰区分前景、中景和背景，QC 必须拒绝。

场景方向资产使用自己的输出契约：

```text
location_scene_master_reference:
  scene_context background, alpha forbidden, project-defined 或 16:9 canvas,
  可识别前景 / 中景 / 背景和已批准美术方向

location_art_top_view:
  scene_context background, alpha forbidden, 1:1 或 project-defined canvas,
  俯视布景地理关系，门、窗、固定道具、光源和行动区必须匹配导演部空间证据

location_orientation_grid_9:
  scene_context background, alpha forbidden, 1:1 或 project-defined canvas,
  NW/N/NE/W/C/E/SW/S/SE 顺序的九个中心锚点径向视觉格，
  全部围绕同一个 center_anchor_id，并匹配同一场景母图、美术俯视图、
  导演部 layout、anchor orbit camera map 和已接受 radial blockout/control grid
```

任何方向资产只要和 `layout.yaml`、技术 top view、camera map、anchor orbit camera map、radial blockout/control grid 或已批准场景母图矛盾，QC 必须拒绝。

## 场景图片信息预算圣经

场景上下文 location card、establishing plate、视频参考帧和 shot override 必须在生图前控制画面信息量。远景、大全景、战场、城市、群像、堡垒、山口、大型室内和大量重复对象的画面，最容易因为把每个士兵、旗帜、怪物、墙块、武器和背景物体都当成同等重要而失败。

失败结果通常表现为：

```text
石头颗粒化
人群纹理颗粒化
噪声微细节
远景软糊
AI speckle
烟雾假装成建筑细节
```

对于远景建立镜头、史诗大全景、战场、城市、群体场景、堡垒、山口、大型室内和任何有大量重复物体的场景，美术部必须优先保证三个功能：

```text
large readable shapes
lighting and atmosphere
clear silhouettes and scale
```

这些画面不要试图让每个小物体都清晰可读。它们不是角色设定表、单位展示图、建筑清单、武器目录或纹章证明图。

生成提示词前，必须为每个宽景 / 群体重场景资产定义 `scene_information_budget`：

```text
detail_priority:
  highest_detail:
    只允许 3-5 个最高细节元素，例如中央城门、主路、最近旗帜、英雄剪影、最大生物
  medium_detail:
    重要中景体块、可读光源、主要旗帜
  low_detail:
    远处士兵、城墙守卫、背景塔楼、远山地形
  impression_only:
    远处人群、箭雨、小武器、城垛人物、次要旗帜、远处车辆或动物

distance_simplification:
  使用群组剪影、体块、薄雾、烟、雪、雨、尘、雾气和大气透视简化远处形体

forbidden_detail_behavior:
  no equal-detail rendering across the whole frame
  no over-detailed distant figures
  no full-frame ultra-detail
  no visual information overload
```

提示词规则：

```text
big shapes clear, details restrained, distant subjects grouped,
only a few nearby or central elements finely rendered
```

宽景提示词必须包含抵抗颗粒化和信息过载的负向约束：

```text
no equal-detail rendering across the whole frame,
no over-detailed distant soldiers or crowd members,
no granular crowd texture,
no particleized stone,
no noisy micro-detail,
no AI speckle,
no smoke pretending to be architectural detail,
no distant objects rendered as sharp individual miniatures,
no full-frame ultra-detail,
no cluttered battlefield or city texture,
no visual information overload.
```

如果宽景中远处重复形体变成噪点，建筑变成假微纹理，烟雾被当作结构替代，或整张画面同等精细，QC 必须拒绝。

## 资产版本与历史

生成美术资产必须保持“正式输出干净，试错版本隐藏”。每个计划资产只有一个项目办公室指定的标准 `output_path`，该路径只保留最终确认版本；每一个正在制作的资产，都必须使用项目现场规范指定的隐藏 `version_repo`。

`asset_id` 使用项目统一资产 ID 或镜头共享文件中的资产 ID。隐藏版本文件名规则由项目办公室定义；当前项目采用 `YYYYMMDDvNNNN.ext`，例如 `20260620v0001.png`。同一资产内按生成顺序递增，不复用编号。

所有被废弃、未选中、返工前或被替换的图片，都进入该资产自己的隐藏版本库。不要在正式资产目录创建可见 `history/`、`versions/`、`drafts/` 或 `v1/`、`v2/`。

规划文件中的 `output_path` 必须始终指向项目办公室指定的最终文件，不指向隐藏版本库。线程结果和 QC 文件可以在 `version_repo` 与 `discarded_files` 中记录隐藏版本库路径。版本 manifest 只写最小追溯信息：版本文件、来源提示词或线程、状态、废弃原因、是否值得沉淀为经验。

## 运行模式

- 把 Codex 当作运行时。不要实现 Python agent loop，不要调用项目 LLM provider 充当部门员工。
- 当 `multi_agent_v1.spawn_agent` 可用时，用它运行边界清晰的规划角色。子规划员工返回 artifact envelope；它们不调用 Codex thread tools，也不直接生成图片。
- 只有在项目办公室指定的图片提示词简报和线程计划已存在之后，才使用 Codex 后台线程工具。
- 父协调者调用 `codex_app.create_thread`，用 `codex_app.read_thread` 检查进度，用 `codex_app.send_message_to_thread` 驱动重试。
- 只为互不重叠的图片批次创建后台线程，并明确输出路径。常见批次包括角色、场景、道具 / 服装、风格板和镜头参考帧。
- 每个线程提示词必须要求 worker Codex 使用可用图像生成能力生成 raster assets，把最终确认图片写入项目办公室指定的 `output_path`，把废弃、未选中、返工前或被替换图片放入项目办公室指定的 `version_repo`，最后返回紧凑 manifest，列出最终文件、`version_repo` 和 `discarded_files`。
- 如果 Codex thread tools 或图像生成不可用，仍然产出项目办公室指定的线程计划和图片提示词简报，并在项目办公室指定的结果记录中把图片生成标记为 `blocked`。

## 参考文件

只读取当前任务需要的参考文件：

```text
references/artifact-contract.md
  子员工 artifact envelope 和产物规则

references/thread-image-workflow.md
  Codex 后台线程派发、轮询、重试和结果记录规则

references/asset-card-prompt-templates.md
  角色、道具 / 物品、场景卡字段；
  场景方向资产规则；
  短文件名规则；
  production metadata；
  model-visible 六段提示词模板；
  精确道具策略

references/asset-output-requirements.md
  每种美术图片资产的硬性输出规格；
  透明角色三视图、低模图、场景俯视标注图、九宫格、角色站位图、轨迹图、故事板、视频参考帧的画面要求和 QC 标准

references/ai-image-technique-library.md
  AI 制图技巧库；
  用户截图经验整理；
  角色卡、场景俯视图、九宫格、线稿、轨迹导引、故事板、遮罩、ControlNet、精确后合成等技巧选择规则

agents/*.md
  每个规划角色的一张任务卡。不要把 agents/openai.yaml 当作角色卡。

schemas/*.json
  JSON 输出结构契约和测试
```

## 工作流

1. 确认项目根目录和必需导演部输出。
2. 按项目办公室指定位置产出全剧或本集资产规划，并初始化或刷新共享母卡索引。
3. 运行 `art-director-agent`，产出美术方向说明。
4. 运行 `asset-breakdown-agent`，产出资产准备计划和资产清单。
5. `asset-breakdown-agent` 必须根据 `references/asset-output-requirements.md` 为每个资产选择 `output_spec_id`、`annotation_policy` 和 `control_role`。
6. `asset-breakdown-agent` 必须根据 `references/ai-image-technique-library.md` 为需要控制的资产选择 `technique_profile`、参考图角色和控制输入需求。
7. 在资产清单存在后，运行 `character-design-agent`、`environment-design-agent` 和 `prop-costume-design-agent`。这些员工可以并行。
8. 在设计 JSON 文件存在后，运行 `style-continuity-agent`。
9. 运行 `image-prompt-agent`，产出图片提示词简报；提示词必须继承 `output_spec_id` 和 `technique_profile`，并把输出规格、控制图用途、不可入画标记、负向约束写入 `copy_ready`。
10. 对每个重复空间场景，确保场景方向资产和项目办公室指定的场景方向索引已表示清楚，然后才能把 reference-frame 和 shot-override 提示词视为 ready。
11. 运行 `thread-plan-agent`，产出线程计划。
12. 父协调者根据线程计划创建 Codex 后台线程，尽量一批互不重叠资产一个线程。
13. 父协调者在项目办公室指定的结果记录中记录线程 ID、状态、最终生成文件路径、`version_repo`、`discarded_files`、阻塞项和重试说明。
14. 运行 `asset-qc-agent`，产出资产索引、场景方向索引和资产 QC 结论。
15. 返回项目根目录、最终文件归口位置、阻塞图片任务、已完成验证，以及建议交接回导演部进行提示词刷新。

## 员工顺序

使用以下任务卡：

```text
agents/art-director-agent.md
agents/asset-breakdown-agent.md
agents/character-design-agent.md
agents/environment-design-agent.md
agents/prop-costume-design-agent.md
agents/style-continuity-agent.md
agents/image-prompt-agent.md
agents/thread-plan-agent.md
agents/asset-qc-agent.md
```

## 质量规则

- 视觉连续性优先于单张资产美感。角色身份、服装、道具、地理关系、光线逻辑和材质语言必须匹配项目办公室交接的视觉连续性材料。
- 角色资产必须服从共享角色总卡。`Section 1. 源头 Canon` 防止身份漂移，`Section 2. 编剧影视化角色卡` 控制屏幕表达状态，`Section 3. 美术视觉角色卡` 记录美术部视觉决策。不要改写 Section 1 或 Section 2。
- 当项目输入定义了阵营、物种、组织、等级、阶层、职能或角色类型的内部差异时，必须保留这些差异，不得把所有成员画成一种泛化外观。不要在可复用 skill 中写死项目特定解剖、文化或 lore。层级标签、权力暗示、身体语言、服装、解剖、材质和视觉特征比例必须来自项目 bible 和连续性输入。
- 角色设计、风格规则和图片提示词必须明确标注相关层级 / 职能，以及项目定义的视觉平衡。
- 不重写故事、镜头表或生成策略。
- 不写最终 ComfyUI 工作流参数。美术部图片提示词是 tool-neutral 资产提示词；导演部拥有 ComfyUI prompt / workflow 文件。
- 每张生成图片必须有 asset ID、asset subtype、短文件代码、source prompt ID、expected output path、continuity refs 和 downstream usage notes。
- 只有最终确认版本可以位于项目办公室指定的标准 `output_path`；所有废弃、未选中、返工前或被替换图片必须进入项目办公室指定的 `version_repo`。
- 除非镜头明确需要唯一 first frame、last frame、redraw target 或 reference frame，否则优先制作可复用参考资产，而不是一次性图片。
- 提示词必须具体但 tool-neutral。不要包含 ComfyUI node graph、sampler settings 或最终生产参数。
- 输出路径稳定、提示词计划可审计之前，不得启动图像生成线程。
- 不得只凭文本创建最终美术俯视图或九宫格方向参考。它们必须引用导演部空间证据和已批准场景美术参考，QC 必须对照这些来源。
- 任何图片如果美但破坏角色、服装、空间、道具、风格或镜头连续性，必须退回重做。
- 使用参考图和控制图时，必须明确每张图的用途。身份参考不能改空间，结构参考不能改角色，风格参考不能改布局，轨迹导引不能进入最终画面。
- 从网络教程吸收技巧时，只吸收方法和质量标准，不把平台 UI 截图、水印、蓝色轨迹、教程文字或创作者标签当作生成内容。
- 输出规格优先于模型自由发挥。透明角色三视图、低模图、场景俯视标注图、九宫格、角色站位图和视频参考帧必须符合 `references/asset-output-requirements.md`，否则即使画面漂亮也不能通过 QC。

## 最终回复

运行结束后报告：

```text
project root
planning artifacts created
image assets created or blocked
location scene master, art top view, 9-cell orientation grid,
  and orientation index status for each recurring spatial scene
Codex thread IDs and statuses
validation performed
next department handoff recommendation
```
