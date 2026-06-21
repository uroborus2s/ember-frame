# 资产卡与提示词模板

撰写资产设计 JSON、art-image-prompts 逻辑记录或后台图片线程提示词时使用本参考。

## 短文件名规则

所有生成资产文件使用稳定短代码。去掉扩展名后的 basename 不得超过 20 个字符。目录由项目办公室指定，短文件名由美术部维护。

示例：

```text
c001m.png
c001e01.png
p001m.png
p001e01.png
l001m.png
l001e01.png
l001art.png
l001top.png
l001grid.png
f001m.png
r001s02.png
```

语义名称写入 JSON 索引，不写成长文件名。

## 输出路径路由

美术部只定义短文件名、资产类型和最终用途，不定义正式目录。全剧母资产、每集状态资产、控制图、站位图和故事板的正式位置，均由项目办公室在 `project-management.md`、`.project/` 交接契约或当前任务包中指定。

全剧可复用资产逻辑归口：
```text
<project-office-designated character master asset path>
<project-office-designated location master asset path>
<project-office-designated prop master asset path>
<project-office-designated costume master asset path>
<project-office-designated style master asset path>
```

每集状态卡和每集场景方向资产逻辑归口：
```text
<project-office-designated episode character asset path>
<project-office-designated episode location asset path>
<project-office-designated scene master reference path>
<project-office-designated top-view asset path>
<project-office-designated orientation-grid asset path>
<project-office-designated episode prop asset path>
<project-office-designated episode costume asset path>
```

控制图、站位图和故事板逻辑归口：
```text
<project-office-designated control-reference asset path>
<project-office-designated low-poly/blocking asset path>
<project-office-designated shot-blocking asset path>
<project-office-designated motion-path asset path>
<project-office-designated storyboard asset path>
```

不要把 `character_episode_state_card`、`prop_episode_state_card` 或 `location_episode_scene_card` 误归为全剧母资产。不要把 `location_scene_master_reference`、`location_art_top_view` 或 `location_orientation_grid_9` 误归为全剧母资产；这些是根据导演部场景包生成的每集场景资产，正式位置由项目办公室指定。

## 卡片子类型

- `character_master_card`：全剧角色身份卡，锁定脸、骨相、体型、气质和身份锚点。
- `character_episode_state_card`：每集角色状态卡，锁定服装、伤痕、灰尘、情绪、道具和动作状态。
- `character_low_poly_proxy`：角色低模代理，锁体块、比例和站位尺度，不做精修美术。
- `prop_master_card`：可复用物件、旗帜、徽记或道具卡，锁轮廓、材质、比例、标记和用途。
- `prop_episode_state_card`：每集物件状态卡，锁磨损、污渍、损坏、摆放和使用状态。
- `prop_precision_overlay`：精确旗帜、徽记、符号、地图或文字类透明叠加层。
- `location_master_scene_card`：可复用地点卡，锁地理关系、入口、出口、空间布局、光线、材质和行动区域。
- `location_episode_scene_card`：每集地点状态卡，锁当前时间、天气、损坏、调度和连续性锚点。
- `location_scene_master_reference`：重复场景的最终美术母参考，在保留导演部地理关系的同时锁定材质、灯光、陈设和情绪。
- `location_art_top_view`：根据导演部 layout/blockout 和场景母参考生成的美术俯视图。
- `location_orientation_grid_9`：同一场景的 3x3 视觉方向板，固定格子顺序为 `NW, N, NE, W, C, E, SW, S, SE`。
- `location_overhead_annotated_map`：带文字、箭头、机位、动线和区域标注的正交俯视说明图。
- `location_low_poly_blockout`：场景低模空间图，用灰模体块锁空间关系和障碍物。
- `scene_character_blocking_chart`：场景级角色站位图，说明角色、道具、机位和行动路线。
- `shot_character_blocking_chart`：镜头级角色站位图，说明单个镜头的角色朝向、动线、遮挡和机位。
- `motion_path_guide`：摄影机或角色运动轨迹控制图。
- `storyboard_motion_sheet`：动作节奏故事板草图。
- `director_storyboard_board`：用于指导整体表演和镜头推进的导演故事板。
- `style_reference`：风格、色彩、材质、光影和镜头质感参考。
- `reference_frame`：具体镜头参考帧。
- `shot_override`：针对单个镜头的局部覆盖参考帧。

## 角色卡字段

必需设计字段：

```text
asset_id
file
asset_type
asset_subtype
display_name
character_total_card_ref
source_canon_refs
screenwriting_character_refs
identity_lock
body_metrics
episode_state
card_layout
output_format_requirements
technique_profile
continuity_refs
source_refs
usage
```

`character_total_card_ref` 指向项目办公室指定的共享角色总卡。采用导演部全局入口的项目通常是 `director-room/characters/CHAR-*.md`。美术部读取 Section 1 作为源头 canon，读取 Section 2 作为编剧的屏幕角色意图，只写入或更新 Section 3 美术视觉卡，不修改配音或视频执行区块。

`identity_lock` 必须覆盖年龄观感、脸型与五官、眼睛、发型、皮肤质感、身高/体型、动作习惯和禁止提前暴露的未来信息。它不得与源头 canon 或编剧意图矛盾。

`body_metrics` 必须让图像模型看懂比例：

```text
height
weight_build
body_ratio
silhouette
scale_refs
```

除数字外，优先提供可见相对比例，例如“比人类卫兵高一个头”或“体量约为轻甲士兵两倍”。

角色卡输出要求：

```text
output_format_requirements
output_spec_id: OUT-CHAR-TRANSPARENT-THREEVIEW
master_card_background: neutral plain
cutout_background: transparent alpha
required_views: front, side, back, three-quarter when needed
detail_crops: face, hands, wardrobe texture, identity marks
scale_reference_required: true
```

## 道具与物件卡字段

必需设计字段：

```text
asset_id
file
asset_type
asset_subtype
display_name
prop_lock
physical_dimensions
episode_state
card_layout
output_format_requirements
technique_profile
continuity_refs
source_refs
usage
```

`prop_lock` 必须覆盖故事用途、所属角色/阵营、轮廓、比例、尺度、材质、磨损/标记、旗帜/徽记/符号规则，以及禁止提前暴露的未来信息。

`physical_dimensions` 必要时必须包含明确尺度：

```text
length
width
height
scale_reference
weight_feel
material_thickness
```

当单纯数字不足以指导生成时，使用人手、桌面、门洞、身体或携带方式作为参照。

旗帜、徽记、符号、文书、印章和文字类道具必须规划母卡加参考/线稿控制。如果需要精确标记，优先使用透明 PNG/SVG 后期合成，不要要求视频模型发明符号。

道具和物件输出要求：

```text
output_format_requirements
output_spec_id: OUT-PROP-TRANSPARENT-MULTIVIEW 或 OUT-PRECISION-OVERLAY
master_card_background: neutral plain
cutout_background: transparent alpha
required_views: front, side, back, top/bottom when useful
detail_crops: material, markings, mechanism, damage, edges
scale_reference_required: true
```

## 场景卡字段

必需设计字段：

```text
asset_id
file
asset_type
asset_subtype
display_name
location_lock
episode_state
card_layout
output_format_requirements
technique_profile
continuity_refs
source_refs
usage
```

`location_lock` 必须覆盖故事功能、地理关系、入口/出口、空间结构、行动区域、面向摄影机区域、连续性锚点，以及禁止出现的现代或错误元素。

场景和视频帧输出要求：

```text
output_format_requirements
canvas_aspect_ratio: 16:9 or project_defined
background_policy: scene_context or video_frame
composition_layers: foreground, midground, background
camera_requirements: distance, angle, screen direction, light, weather/time
```

## 场景方向字段

`location_scene_master_reference`、`location_art_top_view` 和 `location_orientation_grid_9` 除标准场景字段外，还必须包含：

```text
director_spatial_refs
scene_master_dependency
art_top_view_dependency
orientation_cells
shot_usage
prohibited_spatial_drift
```

`director_spatial_refs` 必须引用相关 `layout.yaml`、技术 `top-view.png`、`camera-map.png`、blockout manifest 和作为证据的镜头导引。美术输出不得改写这些空间事实。

`orientation_cells` 使用以下顺序：

```text
NW | N | NE
W  | C | E
SW | S | SE
```

每格记录：

```text
camera_zone
look_direction
expected_visible_anchors
prohibited_drift
source_refs
```

图片提示词可以要求干净的 3x3 视觉板，但精确标签和镜头映射必须写入 `<project-office-designated location-orientation-index path>`，不要依赖生成图里的文字。

## 场景图片信息预算

当场景卡、建立画面、视频参考帧或镜头覆盖图属于宽景、远景、人群场景、战场、大城市、堡垒、山口、大型室内，或包含大量重复小物体时，使用本节。信息预算防止图像模型给全画面分配同等重要性。

在宽景或群像较多的场景和参考帧记录中加入可选字段：

```text
scene_information_budget:
  shot_scale: distant establishing wide shot | epic wide shot | large group scene | other
  main_visual_functions:
    - large readable shapes
    - lighting and atmosphere
    - clear silhouettes and scale
  detail_priority:
    highest_detail:
      max_elements: 3-5
      examples: central gate, main road, nearest banners, hero silhouette,
        largest creatures, primary light source
    medium_detail: midground masses, wall flags, readable fires, nearest groups
    low_detail: distant soldiers, guards, background towers, far terrain
    impression_only: distant crowds, arrows, tiny weapons, parapet figures,
      far banners, secondary animals or vehicles
  distance_simplification:
    grouped_silhouettes: true
    massing_over_individuals: true
    atmospheric_perspective: fog, smoke, snow, rain, dust, haze, or depth falloff
  forbidden_detail_behavior:
    - equal-detail rendering across the whole frame
    - over-detailed distant figures
    - granular crowd texture
    - particleized stone or architecture
    - noisy micro-detail or AI speckle
    - full-frame ultra-detail
    - visual information overload
```

宽景提示词必须说明：这是一张建立镜头，不是角色表、单位展示、建筑清单、武器目录或徽记校样。只有 `highest_detail` 元素可以获得精细刻画，其余内容必须通过距离、氛围和群组化来简化。

宽景 copy-ready 模板：

```text
This is a true distant establishing wide shot. Prioritize scale, atmosphere,
composition, and silhouette clarity over small object detail. Keep strong depth
layers. Only 3-5 elements may receive high detail. Distant people, creatures,
vehicles, wall figures, weapons, and small banners must read as grouped
silhouettes or masses, not individually readable miniatures. Let fog, smoke,
snow, dust, rain, haze, and atmospheric perspective simplify small forms.
```

宽景负向提示词必须包含：

```text
no equal-detail rendering across the whole frame, no over-detailed distant
soldiers or crowd members, no granular crowd texture, no particleized stone, no
noisy micro-detail, no AI speckle, no smoke pretending to be architectural
detail, no distant objects rendered as sharp individual miniatures, no
full-frame ultra-detail, no cluttered battlefield or city texture, no visual
information overload.
```

## 图片输出格式契约

每份资产计划、清单记录、图片提示词记录、线程提示词和 QC 报告都必须保留以下契约：

```text
output_format:
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

可用策略：

```text
background_policy:
  neutral_plain | transparent_alpha | scene_context | video_frame |
  diagram_plain | low_poly_scene | annotated_control

alpha_policy:
  required | forbidden | optional

annotation_policy:
  forbidden | required | allowed_control_only | companion_json_only

control_role:
  final_asset | control_reference | diagram | motion_guide |
  low_poly_proxy | precision_overlay

canvas_aspect_ratio:
  1:1 | 3:2 | 2:1 | 4:5 | 16:9 | 9:16 | project_defined
```

`composition_layers` 必须始终存在。资产卡和抠图可用 `not_applicable` 或卡片布局层填充 foreground、midground、background。视频参考帧和镜头覆盖图必须描述可见的前景、中景和背景内容。

必需交付行为：

```text
neutral master card:
  neutral_plain background, alpha forbidden, readable shape and scale

transparent character three-view:
  transparent_alpha background, alpha required, front/side/back,
  same scale, same foot baseline, no labels, no shadow

transparent cutout:
  transparent_alpha background, alpha required, clean full silhouette

turnaround sheet:
  neutral_plain background, front/side/back/three-quarter views

detail crop sheet:
  neutral_plain background, visual crops for continuity-critical details

low-poly character proxy:
  low_poly_scene or diagram_plain background, alpha optional/forbidden,
  gray/clay body volumes, scale clarity, no beauty rendering

prop transparent multiview:
  transparent_alpha background, alpha required, clean object edges,
  required side/top/three-quarter views

precision overlay:
  transparent_alpha background, alpha required, exact symbol/edge control

location scene master reference:
  scene_context background, alpha forbidden, 16:9 or project_defined,
  approved final location art look with stable geography

location art top view:
  scene_context or diagram_plain background, alpha forbidden,
  top-down geography matching Director Room layout/blockout evidence

location overhead annotated map:
  annotated_control or diagram_plain background, alpha forbidden,
  top-down orthographic annotated diagram with zones, doors, windows,
  fixed props, cameras, lanes, action zones, and screen direction

location low-poly blockout:
  low_poly_scene background, alpha forbidden, gray/clay geometry,
  readable volumes, no final beauty texture

location orientation grid 9:
  scene_context background, alpha forbidden, 1:1 or project_defined,
  3x3 board in NW/N/NE/W/C/E/SW/S/SE order with consistent anchors

scene or shot character blocking chart:
  annotated_control background, alpha forbidden, top-down or camera-blocking
  diagram with positions, facing arrows, paths, camera, key props, screen direction

motion path guide:
  annotated_control background, alpha forbidden, path points, arrows,
  camera or character route; guide marks are control-only

storyboard motion sheet:
  diagram_plain background, alpha forbidden, rough panels, action direction,
  camera type and timing intent

director storyboard board:
  diagram_plain or scene_context background, alpha forbidden, complete
  performance board for a shot group or scene

video reference frame:
  video_frame background, alpha forbidden, 16:9, foreground/midground/background

shot override frame:
  video_frame background, alpha forbidden, 16:9, exact shot composition
```

## 提示词拆分

每条提示词记录必须把过程元数据和模型可见文本分开：

```text
production_metadata:
  asset_id
  asset_subtype
  output_file
  prompt_id
  source_refs
  continuity_refs
  usage

model_visible_prompt:
  visible_goal
  style_quality
  subject_content
  composition_motion
  visible_continuity
  negative_prompt
```

不要把 `asset_id`、`episode_id`、`output_file`、`source_refs` 或 `usage` 写入 `model_visible_prompt`。

## Copy-Ready 提示词字段

每条 `art-image-prompts.json` 记录都必须包含可复制提示词文本：

```text
copy_ready:
  positive_prompt
  negative_prompt
  chatgpt_image_prompt
  gemini_image_prompt
```

`positive_prompt` 是合并后的可见提示词：可见目标、风格与画质、主体内容、构图与运动、可见连续性。`negative_prompt` 是独立负向提示词。`chatgpt_image_prompt` 和 `gemini_image_prompt` 是可直接复制到对应工具中的完整自然语言指令。它们可以说明输出应为图片，但不得包含文件路径或资产 ID 等过程元数据。

## 六段式可见提示词

1. 可见目标：要创建什么资产卡或参考图。
2. 风格与画质：真实感、电影质感、材质、光线和媒介。
3. 主体内容：身份、物体、地点、服装、损坏、天气或可见状态。
4. 构图与运动：参考板布局、视角、比例细节、自然姿态或场景视点。
5. 可见连续性约束：哪些必须保持不变，哪些不能提前暴露。
6. 负向提示词：不想要的风格、瑕疵、错误标记、错误文字、现代元素、水印和连续性违背。

## 制作依赖

资产计划必须在开始生图前暴露制作顺序：

```text
creation_order
creation_phase
depends_on_assets
blocks_assets
dependency_reason
priority
```

推荐顺序：

```text
style references
-> master character/location/prop cards
-> transparent three-view/detail/scale assets
-> episode state cards
-> location scene master references
-> location art top views
-> location 9-cell orientation grids
-> location overhead annotated maps and low-poly blockouts
-> scene/shot blocking charts and motion path guides
-> precision flags/emblems/symbols/text-like props
-> storyboard boards
-> first/last/reference frames
-> shot overrides
```

硬视觉依赖使用 `depends_on_assets`，例如每集状态卡依赖角色母卡，参考帧依赖角色、道具和场景卡，九宫格依赖场景母参考和美术俯视图。
