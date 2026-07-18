# AI 视频技巧库

本文件把优秀开源 AI 视频项目、官方工作流、公开视频教程和项目复盘中可复用的方法，整理为视频生成部可自助选择的技巧库。它只沉淀方法和质量判断，不复制付费教程文案，不把平台 UI、创作者水印、蓝线箭头或未经验证的参数当成内容。

## 使用原则

每个镜头先判断问题，再选择技巧。

```text
角色漂移 -> 首帧身份锁、角色状态卡、短段 I2V、身份参考、局部重跑
场景漂移 -> 场景母图、俯视图、九宫格、低模、深度图、线稿、camera map
动作漂移 -> 故事板、pose、运动轨迹、首尾帧、低模/3D 预演
镜头漂移 -> 导演机位、FLF2V、camera path、运镜强度限制、短段测试
口型漂移 -> 配音时间权威、口型专用流程、近景单独生成
画质失败 -> 重跑源、升级模型或拆段，不用补帧/锐化掩盖
剪辑不可用 -> 生成头尾余量、alternate take、clean plate
```

每个镜头必须记录：

```text
technique_profile:
  technique_ids:
    - VID-I2V-01
  selection_reason:
    为什么选这些技巧
  input_roles:
    每个输入的角色：identity / first_frame / last_frame / structure / depth / pose / mask / motion / audio / style
  control_inputs:
    控制图路径、用途、必须保留项、允许变化项、禁止入画项
  generation_mode:
    I2V / FLF2V / T2V_previs / V2V / lipsync / rerender / composite
  segment_plan:
    分段时长、重叠帧、首尾帧衔接、接剪策略
  fallback_plan:
    失败后重跑、拆段、加强控制、回退上游补资产或标记阻塞
```

## 技巧菜单

### VID-I2V-01 Approved 首帧 I2V

用途：
让通过 QC 的参考帧产生有限、可信的运动，适合表情、环境微动、轻动作、短镜头和建立镜头。

准入：

```text
首帧必须是 OUT-VIDEO-REFERENCE-FRAME 或项目通过 QC 的 first frame。
首帧不得是低模、proxy、标注图、故事板或截图 UI。
首帧必须包含前景、中景、背景、角色状态、道具状态、机位、光线和动作瞬间。
```

提示要点：

```text
只描述这个镜头真实要发生的运动；
限制不该动的角色、道具、家具、门窗和背景；
说明镜头是否固定、轻推、轻摇、跟随或手持；
禁止换脸、换服装、换场景、改变道具状态和生成随机文字。
```

QC：
首帧身份一旦漂移、场景换布景、角色动作无重心，直接失败。

### VID-FLF2V-01 首尾帧锁定

用途：
当动作终点、人物姿态、道具状态、镜头构图或接剪点必须准确时，使用 first-last-frame-to-video。

适用：

```text
角色从坐到站、从站到跪、拿起/放下/夺取道具；
镜头必须从 A 构图到 B 构图；
需要接下一镜头的动作、视线或情绪；
复杂情绪转折或关键命运瞬间。
```

准入：
首帧和尾帧都必须通过 QC，且角色、场景、道具、光线和屏幕方向一致。

失败处理：
中段漂移时缩短时长、增加中间关键帧或拆成多个 FLF2V 段。

### VID-SEG-01 3-5 秒分段生成

用途：
降低长镜头中角色、空间、动作和画质漂移。

规则：

```text
普通镜头默认 3-5 秒；
复杂动作默认 2-3 秒；
说话口型镜头按台词自然停顿切段；
每段必须有明确 start_state 和 end_state；
相邻段保留接剪余量或重叠帧。
```

QC：
每段独立通过角色、场景、动作和可剪辑性 QC 后，才能交给剪辑部拼接。

### VID-PREVIS-01 低模 / 3D 预演

用途：
在生成前验证空间、站位、遮挡、镜头路线和动作重心。

适用：

```text
多人调度、打斗、追逐、跌倒、推拉、复杂室内穿行；
摄影机大幅移动、绕行、升降、穿越空间；
导演要求轴线和空间非常清楚的镜头。
```

输出：

```text
low_poly_blockout
camera_path.json
depth frames
lineart frames
contact sheet
motion notes
```

规则：
低模和预演只做控制证据，不得当最终画面。若预演都看不懂，不能进入最终视频生成。

### VID-DEPTH-01 深度图 / 线稿 / 分割控制

用途：
稳定空间纵深、建筑轮廓、人物与背景距离、前后景遮挡和镜头构图。

选择：

```text
Depth:
  锁前中后景、推拉、走廊、房间纵深、角色和背景距离。

Lineart / Canny:
  锁建筑边缘、道具外形、构图和场景锚点。

Segmentation:
  锁大块区域、天空/地面/人物/道具/建筑分区。

Pose:
  锁人物肢体、手部、打斗姿势、多人站位。
```

纪律：
控制图之间不能矛盾；控制图里的箭头、编号、字母、UI 和标注不得进入最终视频。

### VID-MOTION-01 轨迹导引和 camera path

用途：
让镜头运动可解释、可复现、可 QC。

适用：

```text
导演要求明确运镜；
镜头包含推、拉、摇、移、跟、环绕、升降、穿越空间；
角色和摄影机同时移动；
需要防止视频模型自动变焦、自动绕行、随机换景或空间漂移；
需要给剪辑部固定入点、出点和节奏点。
```

运镜线路图方式列：

```text
MOTION-MAP-TOP-01 俯视线路图
  用途：锁定摄影机在平面空间中的起点、终点、路线、角色位置、门窗、家具和障碍。
  适合：室内调度、院落、街巷、追逐、多人走位。
  必须标明：A/B/C 点、camera facing、角色起止位置、screen left/right 或北向。

MOTION-MAP-SIDE-01 侧视高度图
  用途：锁定摄影机高度变化、俯仰、升降、越过障碍、从低到高或从高到低。
  适合：摇臂、升降、俯冲、低机位起拍、高处下压、跨越门槛或墙体。
  必须标明：高度、俯仰角、主体高度、遮挡物高度。

MOTION-MAP-3D-01 低模三维路径图
  用途：在 3D/blockout 场景里验证摄影机路线、遮挡、空间尺度和角色体量。
  适合：复杂运镜、长镜头、打斗、多人调度、穿越空间。
  输出：camera_path.json、低模预演视频、关键帧 contact sheet、深度图或线稿帧。

MOTION-MAP-ABC-01 A/B/C 关键点路线图
  用途：用少量关键点说明起点、经过点、终点和节奏变化。
  适合：AI 视频提示词、FLF2V 分段、短镜头快速控制。
  必须标明：每个点的景别、主体位置、速度变化、构图终点。

MOTION-MAP-ORBIT-01 环绕罗盘图
  用途：锁定围绕角色、道具或中心锚点的半环绕 / 全环绕路线。
  适合：仪式、对峙、心理包围、关系翻转、展示中心道具。
  必须标明：center_anchor_id、起始方位、结束方位、环绕方向、半径、主体朝向。

MOTION-MAP-DOLLY-01 推拉纵深图
  用途：锁定 push-in / pull-out 在前中后景中的纵深变化。
  适合：逼近真相、人物孤立、情绪压迫、空间释放。
  必须标明：起始景别、终止景别、焦点对象、背景压缩或释放意图。

MOTION-MAP-TRACK-01 平移 / 跟拍路线图
  用途：锁定摄影机和角色的相对速度、平行关系和屏幕方向。
  适合：人物行走对白、追逐、横向穿越空间、并排行动。
  必须标明：角色路线、摄影机路线、相对距离、是否保持同速。

MOTION-MAP-PAN-TILT-01 摇摄 / 俯仰弧线图
  用途：摄影机位置基本固定，但镜头方向发生水平或垂直旋转。
  适合：揭示信息、角色视线带动、从脚到脸、从地面到天空。
  必须标明：起始朝向、结束朝向、旋转角度、揭示对象和停顿点。

MOTION-MAP-HANDHELD-01 手持运动区域图
  用途：规定手持晃动幅度和主体保持区域，避免随机乱晃。
  适合：争吵、逃亡、战斗、主观紧张、纪录感。
  必须标明：主体安全框、允许晃动幅度、禁止丢失动作方向。

MOTION-MAP-FPV-01 第一人称穿越路径图
  用途：锁定第一人称路线、障碍、速度和视线目标。
  适合：奔跑、坠落、飞行、穿门、冲入人群、从角色主观进入空间。
  必须标明：路线高度、速度段、避障点、视线目标、终点构图。

MOTION-MAP-REVEAL-01 遮挡揭示路线图
  用途：用门框、柱子、人物背影、墙体或前景物逐步揭示主体。
  适合：悬疑、登场、发现危险、展示关键道具。
  必须标明：遮挡物、揭示时刻、主体第一次可见的位置和观众注意点。

MOTION-MAP-MATCH-01 接剪匹配路线图
  用途：让本镜头的终点方向、动作和构图服务下一镜头入点。
  适合：动作接剪、视线接剪、转场、同方向运动、多段 FLF2V。
  必须标明：本镜头 end frame、下一镜头 start frame、动作方向、节奏点。
```

记录格式：

```text
movement_type:
  fixed / push-in / pull-out / pan / tilt / dolly / truck / orbit / crane / handheld / FPV
motion_map_type:
  MOTION-MAP-TOP-01 / MOTION-MAP-SIDE-01 / MOTION-MAP-3D-01 / ...
path_points:
  A: 起点机位、景别、高度、主体位置
  B: 经过点、转向、速度变化、主体关系
  C: 终点构图、视线方向、接剪点
speed_curve:
  constant / ease-in / ease-out / accelerate / decelerate / stop-and-reveal
screen_direction:
  left-to-right / right-to-left / toward-camera / away-from-camera / clockwise / counterclockwise
anchor_or_subject:
  被跟随角色、中心道具、中心锚点或揭示对象
edit_function:
  建立空间 / 揭示信息 / 压迫 / 释放 / 跟随行动 / 接剪匹配
forbidden_rendered_guides:
  no blue guide lines, no arrows, no circles, no letters, no labels, no UI overlay
```

QC：
镜头运动必须有起点、过程和终点。随机漂移、无目的绕行、自动变焦、突然换景、主体丢失、屏幕方向错误、环绕半径乱变、手持晃到动作不可读，直接失败。

### VID-TIMELINE-PROMPT-01 分秒时间轴提示词

用途：
把短视频平台常见的“0s-2s / 2s-5s / 5s-7s”分段提示词转成分镜、提示词和视频生成部都能执行的镜头节拍。它适合宏大运镜、穿越空间、追逐、角色近景微表情和需要一镜到底感的镜头。

定位：

```text
时间轴提示词只负责表达导演意图和节拍；
不能替代首帧、尾帧、角色参考、场景母图、motion map、camera path、深度图或低模预演；
超过 5 秒的时间轴提示词必须拆成多个生成段，再由剪辑部拼接；
红线、箭头、字幕、UI 和路线标注只能作为控制说明，不得进入最终画面。
```

准入：

```text
导演签署区已有镜头目的、观众感受、起点状态、终点状态和转场关系；
美术资产区已有通过 QC 的首帧 / 场景参考 / 角色状态；
复杂运镜已有 MOTION-MAP-* 或 camera_path；
近景微表情已有表情边界、身份锁和禁止夸张变形项；
提示词区把模型可见提示词和制作元数据分开。
```

分镜拆分规则：

```text
timeline_prompt:
  global_lens_style:
    画幅、镜头感、焦段、光线、色彩、质感、速度基调
  shot_anchor:
    主体、场景中心锚点、路线终点、观众注意点
  route_or_motion_ref:
    motion map / camera path / 首尾帧 / 低模预演 / 参考图路径
  time_slices:
    - slice_id: S01-A
      time_range: 0s-2s
      storyboard_fragment:
        本段在分镜里的叙事功能
      start_state:
        本段起点的角色、场景、镜头和情绪状态
      end_state:
        本段终点的角色、场景、镜头和情绪状态
      camera_beat:
        镜头运动、速度曲线、景别变化、焦点变化
      action_beat:
        角色动作、道具互动、重心或环境运动
      expression_beat:
        眼神、嘴角、呼吸、停顿等微表情变化；无近景时写 none
      control_refs:
        首帧、尾帧、motion map、pose、depth、lineart、mask
      model_visible_prompt:
        可直接给模型的短提示词，只写画面里应发生的事
      negative_prompt:
        禁止漂移、禁止 UI/红线/箭头/文字、水印和错误动作
      edit_out:
        本段推荐出点、接下一段的动作/视线/声音/构图依据
```

宏大运镜提示词骨架：

```text
global_lens_style:
  cinematic aerial establishing shot, wide lens, high detail environment,
  clear route through the space, stable subject and landmarks.

time_slices:
  0s-2s:
    camera starts from a high wide view, gliding forward along the marked route,
    establishing terrain, water, roads and the distant final landmark.
  2s-5s:
    camera descends and accelerates, passing over foreground structures,
    keeping the destination landmark locked in the upper frame.
  5s-8s:
    camera threads through gates, bridges or streets, parallax increases,
    foreground elements pass by without blocking the route.
  8s-12s:
    camera rises and eases out toward the final landmark,
    ending on a readable heroic wide composition.
```

近景微表情提示词骨架：

```text
global_lens_style:
  intimate close-up, shallow depth of field, stable identity, soft key light,
  very subtle facial performance, no exaggerated expression.

time_slices:
  0s-1s:
    eyes remain still, breath barely visible, lips relaxed.
  1s-2.5s:
    eyelids soften, gaze slowly shifts toward the camera, mouth corners move slightly.
  2.5s-4s:
    a restrained smile almost appears then fades, breathing calms, head movement minimal.
```

分镜落地：

```text
导演签署区:
  只写镜头目的、观众视线、运镜走向、微表情边界和 QC，不写模型参数。

提示词区:
  写 timeline_prompt、time_slice_prompts、model_visible_prompt、negative_prompt、control_refs。

视频生成区:
  把 time_slices 转成 segment_plan；每段 2-5 秒，写首尾帧、控制图、工具、参数、失败重跑策略。
```

QC：
时间轴提示词必须能被拆成可生成的短段。若出现以下问题直接失败：分秒描述只堆形容词、没有 start_state/end_state、没有镜头起点终点、没有接剪依据、微表情超过模型可控范围、红线箭头或字幕进入画面、长镜头一次生成导致角色或空间漂移。

### VID-ACTION-01 动作重心和受力拆解

用途：
防止“人物在画面里飘”“脚滑地”“打击没重量”“拿东西没有接触”。

动作提示必须写清：

```text
start_pose
contact_point
weight_shift
force_direction
prop_interaction
end_pose
reaction_or_follow_through
```

适用：
奔跑、转身、跌倒、打斗、抢夺、推门、搬物、跪下、起身、拥抱、摔碎、拉扯。

QC：
看不出重心转移、手没有真实接触道具、脚步滑动或身体无惯性，必须重跑或补 pose/低模。

### VID-V2V-01 局部重跑 / 视频到视频修正

用途：
在构图和动作基本通过时，修复局部闪烁、嘴部、手部、道具或背景错误。

限制：

```text
不能用 V2V 改变导演镜头目的；
不能让 V2V 重设角色身份、场景布局或道具状态；
mask 外区域必须保持；
修完必须重新过完整 QC。
```

失败处理：
如果 V2V 破坏已通过区域，回到原素材重新生成，不再继续叠修。

### VID-EDIT-01 可剪辑素材设计

用途：
让视频不是单段“好看动图”，而是剪辑部可直接使用的镜头素材。

要求：

```text
head_handles: 6-12 帧或项目要求
tail_handles: 6-12 帧或项目要求
recommended_in
recommended_out
rhythm_point
audio_sync_point
alternate_take_when_needed
clean_plate_when_needed
```

QC：
没有可用入点/出点、动作在第一帧或最后一帧被截断、关键情绪点不可剪，不能通过 QC。

### VID-QUALITY-01 源质量优先

用途：
防止用补帧、锐化、降噪、调色掩盖源视频错误。

规则：

```text
结构错误 -> 重跑，不后期修。
身份漂移 -> 重跑或回美术，不换脸糊弄。
空间漂移 -> 回控制图，不靠剪辑跳过。
低清糊脸 -> 重跑高质量源，不靠锐化伪细节。
低 fps 可读但源正确 -> 可补帧，但必须标记为后期增强，不改变 QC 判断。
```

## 技术选择矩阵

```text
镜头类型: 建立镜头 / 空间交代
优先技巧: VID-I2V-01, VID-DEPTH-01, VID-EDIT-01
控制需求: 场景母图、俯视图、九宫格、深度图

镜头类型: 角色近景 / 情绪微动
优先技巧: VID-I2V-01, VID-SEG-01
控制需求: 角色状态卡、通过 QC 的首帧、表情边界、轻运动

镜头类型: 动作起止明确
优先技巧: VID-FLF2V-01, VID-ACTION-01, VID-SEG-01
控制需求: 通过 QC 的首帧、通过 QC 的尾帧、pose / motion guide

镜头类型: 复杂运镜
优先技巧: VID-PREVIS-01, VID-MOTION-01, VID-TIMELINE-PROMPT-01, VID-DEPTH-01
控制需求: camera path、低模、深度、线稿、分段、time_slices

镜头类型: 多人调度 / 打斗 / 追逐
优先技巧: VID-PREVIS-01, VID-ACTION-01, VID-SEG-01, VID-TIMELINE-PROMPT-01, VID-DEPTH-01
控制需求: 站位图、pose、低模、动作故事板、time_slices

镜头类型: 近景微表情 / 细微表演
优先技巧: VID-I2V-01, VID-SEG-01, VID-TIMELINE-PROMPT-01
控制需求: 通过 QC 的首帧、角色状态卡、表情边界、低运动强度、2-4 秒短段

镜头类型: 对白口型
优先技巧: LIP-SYNC-01, LIP-SHOT-01, VID-SEG-01
控制需求: lipsync handoff、音频、角色状态、嘴部清晰首帧

镜头类型: 局部错误修复
优先技巧: VID-V2V-01
控制需求: mask、原视频、局部提示、完整回归 QC
```

## 通用负向约束

按镜头需要选择，不要机械全塞：

```text
角色一致性:
  no face swap, no age change, no changed hairstyle silhouette,
  no changed body ratio, no random costume redesign, no missing signature accessory.

场景一致性:
  no moved doors, no swapped windows, no relocated fixed furniture,
  no changed center anchor, no alternate room layout, no impossible perspective.

控制图禁入画:
  no blue guide lines, no arrows, no circles, no letters, no labels,
  no route marks, no UI overlay, no tutorial screenshot, no watermark.

动作可信:
  no floating body, no sliding feet, no weightless movement,
  no disconnected hand contact, no melting limbs, no rubber weapons.

视频质量:
  no random text, no fake subtitles, no flicker, no frame jump,
  no smeared face, no temporal crawling texture, no AI speckle.
```

## 学习来源边界

本库吸收的公开方法包括：

- Wan2.1 / Wan2.2 的 I2V、FLF2V 和高帧率开源视频生成思路；
- ComfyUI 官方 Wan 视频示例中的首尾帧工作流；
- HunyuanVideo、HunyuanVideo-I2V、CogVideoX、LTX-Video、Mochi 等开源项目的工具能力划分；
- Runway 官方提示指南中的镜头运动、动作和提示结构经验；
- 项目本地失败复盘：角色漂移、场景漂移、动作无重心、低清硬救、口型失败和不可剪素材。

具体来源列表见 `references/source-learning-index.md`。执行项目时，必须回到当前导演分镜、通过 QC 的美术资产、配音交接和工具能力报告。
