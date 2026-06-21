# 美术资产输出规格

本文件定义美术部每种输出图片资产必须长什么样。它是硬性规格，不是审美建议。所有 `asset-manifest.json`、`art-image-prompts.json`、`thread-plan.json` 和 QC 报告都必须能追溯到这里的 `output_spec_id`。

## 总原则

```text
最终资产:
  给下游直接作为角色、场景、道具、参考帧使用。
  不允许出现说明文字、箭头、教程 UI、临时标注、蓝线、水印。

控制资产:
  给生成、调度、站位、空间锁定使用。
  可以有标注、箭头、角色编号、机位、路径、比例尺，但必须标明 control-only。

图文解释:
  给人类和下游部门理解空间、动作、站位、资产用途。
  标注必须清晰，不能伪装成最终画面。
```

每个图片资产必须在 `output_format` 中写入或继承：

```text
output_spec_id:
  本文件中的 OUT-... 编号
deliverable_kind:
  交付类型
background_policy:
  transparent_alpha / neutral_plain / scene_context / video_frame /
  diagram_plain / low_poly_scene / annotated_control
alpha_policy:
  required / forbidden / optional
annotation_policy:
  forbidden / required / allowed_control_only / companion_json_only
control_role:
  final_asset / control_reference / diagram / motion_guide /
  low_poly_proxy / precision_overlay
required_views:
  必须出现的视角
qc_checks:
  可验收检查项
```

## 标注策略

```text
annotation_policy="forbidden":
  最终图中禁止任何说明文字、箭头、圈线、点位、UI、水印。
  适用于透明角色卡、道具透明图、场景母图、视频参考帧。

annotation_policy="required":
  资产本身就是说明图，必须有清晰标注。
  适用于场景俯视图、角色站位图、低模说明图、动作故事板。

annotation_policy="allowed_control_only":
  可以有控制线、轨迹、箭头、点位，但只能作为控制图。
  交给最终生图时必须在负向提示词中禁止这些标记入画。

annotation_policy="companion_json_only":
  图片中不依赖可读文字；精确语义写入 JSON 索引。
  适用于场景九宫格方向图。
```

## 角色类资产

### OUT-CHAR-TRANSPARENT-THREEVIEW

用途：
角色母卡和每集状态卡的最低合格输出，用于锁定人物一致性。

适用 subtype：
`character_master_card`、`character_episode_state_card`。

画面要求：

```text
file_format:
  png
background_policy:
  transparent_alpha
alpha_policy:
  required
annotation_policy:
  forbidden
canvas_aspect_ratio:
  2:1 / 3:2 / project_defined
required_views:
  front, side, back
```

视觉要求：

```text
同一角色同一服装状态的正面、侧面、背面三视图。
三视图全身完整，不裁头、不裁脚、不遮挡手部关键轮廓。
三视图使用同一站姿基准，脚底在同一水平线，身体比例一致。
姿态中性，双臂自然或轻微外展，不能使用戏剧化动作。
透明背景，无地面阴影、无摄影棚背景、无装饰、无文字标签。
服装、发型、饰品、伤痕、携带物必须和角色总卡 / 本集状态一致。
```

禁止：

```text
禁止白底冒充透明；
禁止三视图中脸型、身高、体型、服装比例不一致；
禁止把动态海报、半身照、氛围图当角色卡；
禁止给透明图添加名字、箭头、尺寸线、UI 或水印。
```

配套资产：
角色必须另行规划 `OUT-CHAR-DETAIL-CROPS`；常驻角色建议另行规划 `OUT-CHAR-LOWPOLY-PROXY`。

### OUT-CHAR-DETAIL-CROPS

用途：
锁定角色可漂移细节。

要求：

```text
背景:
  neutral_plain 或 transparent_alpha
视图:
  face close-up, hair close-up, hands, signature accessory, costume fabric,
  scars/marks, weapon or carried prop detail
标注:
  允许在说明版中标注，但最终参考裁切图不得遮住细节。
```

QC：
必须能单独看清影响连续性的脸部比例、发型边界、饰品、手、服装纹理和剧情状态。

### OUT-CHAR-LOWPOLY-PROXY

用途：
角色低模代理图，用于身高体量、站位、遮挡、镜头预演和场景比例，不用于审美。

画面要求：

```text
background_policy:
  low_poly_scene 或 neutral_plain
alpha_policy:
  forbidden
annotation_policy:
  required 或 allowed_control_only
control_role:
  low_poly_proxy
required_views:
  front, side, back, three_quarter 或 scene_scale_view
```

低模图应该是什么样：

```text
灰模 / clay render / simple low-poly proxy。
只保留大体块：头、躯干、四肢、主要服装外轮廓、巨大饰品或武器体积。
不画真实脸、不画发丝、不画复杂材质、不画花纹细节。
身高线、脚底基线、肩宽、头身比、与门/桌/普通人/守卫的比例可以标注。
用于判断“这个角色占多大空间、和其他人怎么站、镜头里会不会挡住谁”。
```

禁止：

```text
禁止把低模图做成精美角色渲染；
禁止复杂服装细节导致体块不可读；
禁止没有比例参照；
禁止低模比例和角色三视图矛盾。
```

## 道具 / 服装类资产

### OUT-PROP-TRANSPARENT-MULTIVIEW

用途：
锁定道具、武器、饰品、关键服装部件的形状和尺度。

要求：

```text
background_policy:
  transparent_alpha
alpha_policy:
  required
annotation_policy:
  forbidden
required_views:
  front, side, back 或 top, side, three_quarter
```

视觉要求：
道具必须完整、边缘清晰、无投影、无背景、无文字说明。尺度参照单独做说明版，不能压在透明最终图上。

### OUT-PRECISION-OVERLAY

用途：
旗帜、纹章、印章、文字、符号、法阵、地图标记等必须准确的内容。

要求：

```text
file_format:
  svg 或 png
background_policy:
  transparent_alpha
alpha_policy:
  required
annotation_policy:
  forbidden
control_role:
  precision_overlay
```

规则：
精确图形优先 SVG 或透明 PNG 后合成。图像模型只负责材质、位置、透视和留白，不负责自由画准文字和纹章。

## 场景类资产

### OUT-LOCATION-SCENE-MASTER

用途：
场景母图，确定地点的最终美术感觉。

要求：

```text
background_policy:
  scene_context
alpha_policy:
  forbidden
annotation_policy:
  forbidden
canvas_aspect_ratio:
  16:9 / project_defined
required_views:
  approved_mother_view
```

视觉要求：
必须清晰表达地点身份、时代、材质、光线、气氛、主要入口、固定锚点和前中后景。它是美术母图，不是说明图；不得出现文字标签、箭头、路线或 UI。

### OUT-LOCATION-OVERHEAD-ANNOTATED

用途：
场景俯视说明图，锁定空间关系、行动区、门窗、家具、角色站位和机位。

适用 subtype：
`location_art_top_view`、`location_overhead_annotated_map`。

要求：

```text
background_policy:
  diagram_plain
alpha_policy:
  forbidden
annotation_policy:
  required
control_role:
  diagram
canvas_aspect_ratio:
  1:1 / 4:5 / project_defined
required_views:
  top_down_orthographic
```

场景俯视图应该是什么样：

```text
正交俯视，无透视。
白底或浅灰底，黑色 / 深灰线条为主。
可以使用少量颜色区分：角色、机位、光源、行动路线、危险区。
必须标注：房间/区域名称、门、窗、楼梯、固定家具、固定道具、光源、入口/出口、主要路径、行动区、禁入区。
必须有方向：北向或 screen direction，必要时有比例尺。
必须引用导演部 layout / blockout / camera map。
```

禁止：

```text
禁止画成装饰地图；
禁止用透视插画替代俯视图；
禁止为了好看移动门窗、墙体、固定家具；
禁止无标注；
禁止和导演部空间证据矛盾。
```

### OUT-LOCATION-LOWPOLY-BLOCKOUT

用途：
场景低模图，用于空间体块、镜头预演、遮挡关系和深度控制。

适用 subtype：
`location_low_poly_blockout`。

低模图应该是什么样：

```text
灰模 / clay render / low-poly blockout。
墙、门、窗、楼梯、柱子、床、桌、柜、树、桥、祭坛等用简单几何体表示。
只保留大体块和空间关系，不做材质美化、不做复杂纹理、不做氛围光大片。
可输出 top view、three-quarter view、camera view 三类视图。
允许用颜色块或编号区分功能区，但必须标明 control-only。
必须能看出人物和道具在空间中的尺度、遮挡、通行路线。
```

禁止：

```text
禁止把低模图当最终场景概念图；
禁止复杂材质和装饰遮住空间关系；
禁止没有门窗/路径/固定物；
禁止和场景俯视图、导演 layout 矛盾。
```

### OUT-LOCATION-ORIENTATION-GRID-9

用途：
九宫格方向参考，确保同一场景从九个方向仍然是同一个地方。

要求：

```text
background_policy:
  scene_context
alpha_policy:
  forbidden
annotation_policy:
  companion_json_only
control_role:
  final_asset
canvas_aspect_ratio:
  1:1 / project_defined
required_views:
  NW, N, NE, W, C, E, SW, S, SE
```

视觉要求：
九格必须围绕同一个 `center_anchor_id`，每格都能看见中心锚点或明确记录允许遮挡。图片里可以有极简方向提示，但不能依赖可读文字；格子意义、可见锚点和镜头映射必须写入 `location-orientation-index.json`。

禁止：
九格像九个不同地点、家具换边、中心锚点变形、门窗消失、路径拓扑变化，必须拒绝。

## 站位 / 调度类资产

### OUT-SCENE-CHARACTER-BLOCKING

用途：
场景角色站位图，说明角色、道具、机位和运动路线在空间中的关系。

适用 subtype：
`scene_character_blocking_chart`、`shot_character_blocking_chart`。

要求：

```text
background_policy:
  annotated_control
alpha_policy:
  forbidden
annotation_policy:
  required
control_role:
  diagram
required_views:
  top_down_blocking 或 camera_blocking_view
```

场景角色站位图应该包含：

```text
场景边界和固定物简图。
角色位置：用圆点、编号、半身小人或低模剪影表示。
角色朝向：用小箭头表示 facing direction。
角色运动：用路径箭头表示起点、经过点、终点。
摄影机：机位编号、镜头方向、景别、运动轨迹。
道具：关键道具位置、角色手持/放置/抢夺状态。
屏幕方向：screen left / screen right 或北向。
遮挡关系：谁在前景、谁在中景、谁被挡住。
```

禁止：

```text
禁止把站位图做成漂亮剧照；
禁止没有角色编号或朝向；
禁止路径和镜头表矛盾；
禁止把站位图中的箭头、编号、字母带入最终参考帧。
```

### OUT-MOTION-PATH-GUIDE

用途：
镜头或角色运动轨迹控制图。

要求：
必须包含 A/B/C 或起点/中点/终点，标明运动类型、速度感、镜头高度变化和最终构图。它是 control-only，最终图和视频不得出现轨迹线、箭头、圆圈、字母。

## 故事板 / 参考帧类资产

### OUT-STORYBOARD-MOTION-SHEET

用途：
动作故事板，用于快速锁定节奏、动作方向和镜头类型。

要求：
3xN 或 4x3 分镜格；黑白铅笔线稿；可用少量彩色箭头说明摄影机、角色、冲击力；每格必须有镜头类型或动作说明。它是说明图，不是最终剧照。

### OUT-DIRECTOR-STORYBOARD-BOARD

用途：
导演故事板 / 全局表演板，用于一组镜头或一个场景的综合表演指导。

要求：
必须包含角色参考、环境参考、俯视调度、镜头序列、色彩/光线基调和表演说明。它是综合控制板，可以有标注，但不得当作最终参考帧。

### OUT-VIDEO-REFERENCE-FRAME

用途：
视频生成参考帧、首帧、尾帧或 shot override。

要求：

```text
background_policy:
  video_frame
alpha_policy:
  forbidden
annotation_policy:
  forbidden
control_role:
  final_asset
canvas_aspect_ratio:
  16:9 / project_defined
required_views:
  camera_view
```

必须包含清晰前景、中景、背景、角色状态、道具状态、场景位置、机位、景别、光线、天气/时间和动作瞬间。不得出现说明文字、箭头、站位编号、轨迹线或教程 UI。

## 风格类资产

### OUT-STYLE-BOARD

用途：
统一作品色彩、光线、材质、镜头质感和禁用风格。

要求：
可以是拼板或多格，但必须标注每格用途：color、lighting、material、lens mood、forbidden style。风格板不能改变角色身份、空间布局或道具形状。

## 最低交付组合

```text
主角:
  OUT-CHAR-TRANSPARENT-THREEVIEW
  OUT-CHAR-DETAIL-CROPS
  OUT-CHAR-LOWPOLY-PROXY（复杂调度或体型特殊时必需）

关键道具:
  OUT-PROP-TRANSPARENT-MULTIVIEW
  OUT-PRECISION-OVERLAY（文字/纹章/符号精确时必需）

重复场景:
  OUT-LOCATION-SCENE-MASTER
  OUT-LOCATION-OVERHEAD-ANNOTATED
  OUT-LOCATION-LOWPOLY-BLOCKOUT（空间复杂或需视频调度时必需）
  OUT-LOCATION-ORIENTATION-GRID-9

复杂多人镜头:
  OUT-SCENE-CHARACTER-BLOCKING
  OUT-MOTION-PATH-GUIDE（有运动路径时必需）
  OUT-STORYBOARD-MOTION-SHEET
  OUT-VIDEO-REFERENCE-FRAME
```
