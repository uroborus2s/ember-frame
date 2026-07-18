# 镜头参考绑定与震撼风格生产方案

本文把 Toonflow 和 ViMax 中最值得吸收的两个机制落到 `short-drama-factory` 的可执行方案中：

- Toonflow 式 `associateAssetsIds`：每个分镜必须显式绑定会被生成器消费的资产。
- ViMax 式 `ReferenceImageSelector`：每个首帧、尾帧或视频任务必须从候选参考图库中选择最相关参考，并记录选择结果。

目标不是继续增加角色卡、场景卡或提示词，而是建立一个强制机制：每次生成前都能证明“本镜头实际消费了哪些资产”，缺少关键引用时直接阻塞。

## 1. 问题定义

当前容易出现的“清空”现象不是资产缺失，而是资产没有进入当前任务上下文：

```text
资产存在于项目目录
  -> 子 agent 没有读取
  -> prompt 没有声明每张参考图的用途
  -> ComfyUI / 视频模型没有收到 image/audio/control paths
  -> 生成结果回到模型默认想象
  -> 角色、场景、声音、动作继续漂移
```

所以新规则是：

```text
没有 shot_reference_binding，就不得生成。
没有 required_refs，就不得生成。
required_refs 路径不存在或状态未通过 QC，就不得生成。
生成 manifest 没有 used_refs，就不得通过 QC。
```

## 2. 新增核心对象

### 2.1 ShotReferenceBinding

每个镜头生成前必须写入一份绑定文件。推荐路径由项目办公室指定，例如：

```text
.project/ledgers/shot-reference-bindings/{shot_id}.json
```

最小结构：

```json
{
  "shot_id": "SC004-SH003",
  "episode_id": "01",
  "binding_version": "v0001",
  "source_storyboard_doc": "director-room/season-01/01/G-P/P-03/P-03.md",
  "required_refs": [
    {
      "ref_id": "REF-C001-IDENTITY",
      "asset_id": "C001",
      "role": "identity",
      "path": "art-room/shared-assets/characters/c001m.png",
      "status": "locked",
      "must_use": true,
      "use_for": "face, hair silhouette, body ratio, signature clothing and accessories",
      "forbidden_use": "do not change scene layout or camera composition"
    },
    {
      "ref_id": "REF-L001-SCENE",
      "asset_id": "L001",
      "role": "scene_master",
      "path": "art-room/shared-assets/locations/l001m.png",
      "status": "locked",
      "must_use": true,
      "use_for": "environment identity, material language, lighting direction",
      "forbidden_use": "do not redraw character identity"
    },
    {
      "ref_id": "REF-L001-CAMERA",
      "asset_id": "L001-CAM",
      "role": "camera_map",
      "path": "director-room/season-01/01/G-P/P-03/assets/camera-map.png",
      "status": "locked",
      "must_use": true,
      "use_for": "camera route, screen direction, anchor positions",
      "forbidden_use": "control-only, guide marks must not appear in final frame"
    }
  ],
  "optional_refs": [
    {
      "ref_id": "REF-STYLE-001",
      "asset_id": "STYLE-001",
      "role": "style",
      "path": "art-room/shared-assets/style/f001m.png",
      "status": "locked",
      "must_use": false,
      "use_for": "color, atmosphere, material mood"
    }
  ],
  "frame_plan": {
    "generation_mode": "FLF2V",
    "first_frame_required": true,
    "last_frame_required": true,
    "first_frame_path": "director-room/season-01/01/G-P/P-03/P-03.png",
    "last_frame_path": "director-room/season-01/01/G-P/P-03/assets/P-03-last.png"
  },
  "control_inputs": [
    {
      "role": "motion_path",
      "path": "director-room/season-01/01/G-P/P-03/assets/motion-path.png",
      "must_use": true,
      "control_only": true
    }
  ],
  "video_prompt_inputs": {
    "visible_goal": "low-angle wide shot of the warrior crossing the wet battlefield",
    "motion_desc": "slow dolly-in, cloak and rain moving, horse steps forward with weight",
    "duration_sec": 4,
    "fps": 24,
    "negative_prompt": "no changed face, no changed armor, no moved gate, no guide lines, no random text"
  },
  "binding_hash": "sha256-to-fill",
  "status": "ready"
}
```

### 2.2 ReferenceSelection

参考图不能全部塞给模型。必须像 ViMax 一样选择最相关的一小组，并记录原因：

```json
{
  "shot_id": "SC004-SH003",
  "target": "first_frame",
  "candidate_refs": [
    "REF-C001-IDENTITY",
    "REF-C001-STATE-E01",
    "REF-L001-SCENE",
    "REF-L001-GRID",
    "REF-L001-CAMERA",
    "REF-MOTION-PATH"
  ],
  "selected_refs": [
    {
      "ref_id": "REF-C001-STATE-E01",
      "rank": 1,
      "reason": "closest current costume and body state"
    },
    {
      "ref_id": "REF-L001-SCENE",
      "rank": 2,
      "reason": "locks battlefield and cyber gate identity"
    },
    {
      "ref_id": "REF-L001-CAMERA",
      "rank": 3,
      "reason": "locks low angle route and center anchor"
    }
  ],
  "model_prompt_prefix": [
    "Image 1 = identity and current costume reference only.",
    "Image 2 = scene and lighting reference only.",
    "Image 3 = camera path control only; guide marks must not render."
  ],
  "status": "ready"
}
```

## 3. 新增 Agent

### 3.1 reference-binding-agent

职责：

- 读取导演签署区、美术资产区、提示词区、配音口型区和项目办公室索引。
- 为每个镜头列出必需参考、可选参考和控制输入。
- 判断哪些参考必须进入首帧、尾帧、视频或口型阶段。
- 生成 `ShotReferenceBinding`。

不得：

- 生成图片或视频。
- 重写角色和场景。
- 把控制图当最终画面。
- 在缺资产时用文字替代图片引用。

### 3.2 reference-selector-agent

职责：

- 从 `ShotReferenceBinding` 的候选集中，为本次任务选择最多 8 个引用。
- 输出每张参考图的用途说明。
- 选择结果写入 `ReferenceSelection`。

选择优先级：

```text
当前镜头 first/last frame
  -> 当前集角色状态卡
  -> 角色身份母卡或细节裁切
  -> 当前场景母图 / 俯视图 / 九宫格 / camera map
  -> motion path / pose / depth / lineart
  -> 风格参考
```

### 3.3 reference-consumption-gate-agent

职责：

- 在生成前检查 `required_refs` 是否存在、状态是否通过、路径是否可读。
- 在生成后检查 manifest 是否记录了 `used_refs`。
- 发现缺失时标记 `blocked_missing_required_reference`，不能让视频部继续赌模型。

## 4. 生成前硬闸门

### 4.1 图片 / 首帧闸门

```text
必须有导演签署分镜。
必须有 ShotReferenceBinding。
所有 must_use=true 的 identity / current_state / scene refs 必须存在。
重复场景必须有 scene_master、top_view 或 orientation_grid 中至少一项。
复杂空间镜头必须有 camera_map 或 blocking chart。
提示词必须声明每张参考图用途和禁用用途。
```

### 4.2 视频闸门

```text
I2V 必须有通过 QC 的 first_frame。
FLF2V 必须有通过 QC 的 first_frame 和 last_frame。
复杂动作必须有 start_state、end_state、contact_point、weight_shift、motion_path 或 pose。
复杂运镜必须有 camera path、motion map 或低模预演。
说话镜头必须有 audio_ref、dialogue_id、start_time、end_time 和 lipsync status。
```

### 4.3 生成后闸门

每个 render manifest 必须包含：

```json
{
  "render_id": "SC004-SH003-V001",
  "shot_id": "SC004-SH003",
  "binding_hash": "same-as-input-binding",
  "used_refs": [
    {"ref_id": "REF-C001-STATE-E01", "role": "identity"},
    {"ref_id": "REF-L001-SCENE", "role": "scene_master"},
    {"ref_id": "REF-L001-CAMERA", "role": "camera_map"}
  ],
  "used_control_inputs": ["motion_path"],
  "model": "wan2.2-flf2v",
  "duration_sec": 4,
  "fps": 24,
  "qc_status": "needs_review"
}
```

如果 `used_refs` 少于 `required_refs.must_use`，直接失败。

## 5. 部门落点

| 部门 | 新增责任 |
| --- | --- |
| 项目办公室 | 维护绑定文件路径、状态字段、阻塞类型、返工入口。 |
| 导演部 | 在分镜中明确哪些角色、场景、动作、机位、运镜和控制证据必须被消费。 |
| 美术部 | 资产索引必须声明 `downstream_usage` 和 `reference_roles`。 |
| 提示词部 | 只从 `ReferenceSelection` 生成 copy-ready，不自行猜参考图。 |
| 视频生成部 | 生成前读取绑定文件；生成后写 `used_refs` 和 `binding_hash`。 |
| 剪辑部 | 只接收 reference gate 通过的视频素材。 |

## 6. 和 Toonflow / ViMax 的映射

| 来源 | 可吸收机制 | 本方案落点 |
| --- | --- | --- |
| Toonflow | 分镜 `associateAssetsIds` | `ShotReferenceBinding.required_refs` |
| Toonflow | 工作台按 storyboardId 拉取资产 | 视频生成包按 shot_id 拉取 refs |
| ViMax | character portrait registry | 角色母卡、状态卡、细节裁切进入 candidate refs |
| ViMax | reference image selector | `reference-selector-agent` |
| ViMax | first/last/motion decomposition | `frame_plan` 与 `video_prompt_inputs` |
| ViMax | wrong-output guards | `reference-consumption-gate-agent` 和 manifest 校验 |

## 7. 震撼风格提示词的真实作用

短视频平台常见的“震撼提示词”有效，通常有四个原因：

1. 模型本身审美先验强，见过大量电影感、游戏 CG、概念设计、广告大片语汇。
2. 提示词堆了高价值视觉锚点：低角度、远景、冷色、雨雾、巨型城门、披风、金属纹理、电光、千人场面。
3. 它更适合生成单张概念图或短镜头气氛，不等于能稳定拍成连续叙事。
4. 平台展示通常经过筛选、重跑、补帧、剪辑、调色、锐化和音乐包装。

所以它不是“只靠提示词赢”，而是：

```text
强模型审美先验
  + 高频视觉关键词
  + 低角度 / 大尺度 / 雨雾遮瑕
  + 多次抽卡筛选
  + 后期包装
```

## 8. 把示例提示词改成可生产结构

原始写法很有冲击力，但生产中容易失控。应拆成资产与镜头合同：

```text
世界风格:
  复古港式武侠电影质感、赛博江湖、青蓝黑金冷色、高对比光影、雨雾。

场景资产:
  破败古战场、巨型赛博城门、青石广场、中央机械比武台、霓虹幡旗、全息榜。

角色资产:
  半遮面机甲武士、黑色斗篷、暗金机甲纹路、巨型横刀、机械战马。

镜头:
  低角度远景或高空俯视全景，只选一个主镜头目的。

动作:
  马蹄踏碎电光、披风狂舞、刀身冷光。每个 3-5 秒镜头只保留一个主动作。

信息预算:
  最高细节只给武士、战马、巨型城门、中央高台、最近旗帜。
  远处千人侠客只做群组剪影和体块，不逐个清晰刻画。

负向:
  no equal-detail rendering, no granular crowd texture, no random text,
  no changed armor, no melted horse legs, no guide lines, no UI overlay.
```

注意：生产文件中不建议直接写品牌化或特定片厂式表达。应把它转译为可执行原创原则，例如“复古港式武侠布景、棚拍式戏剧光、低机位英雄化构图、青蓝黑金赛博材质、雨雾大气透视”。

## 9. 免费模型能否达到这种效果

免费 / 开源模型可以做出接近的单镜头或概念图，但难点在稳定性和成本：

```text
能做到:
  单张史诗概念图
  3-5 秒气氛镜头
  I2V 轻运动
  FLF2V 首尾帧过渡
  局部候选筛选

容易吃力:
  千人复杂群像的清晰可控
  15 秒连续宏大运镜
  稳定角色脸和服装跨镜头不漂
  机械马腿、横刀、斗篷、雨雾、电光同时可信运动
  口型、表情、动作、摄影机同时稳定
```

当前推荐策略：

```text
图像母资产:
  强图像模型或商业图像模型优先，用于首帧、尾帧、角色、场景母图。

开源视频:
  Wan2.2 / LTX-Video / VideoX-Fun 做 I2V、FLF2V、短段、控制实验。

商业视频:
  用于需要更强审美、自然运动和少调参的英雄镜头。

后期:
  补帧、剪辑、调色、音效、音乐、锐化只增强已通过结构 QC 的素材。
```

结论：

```text
免费模型不是完全做不到，但不能靠一句魔法提示词稳定做到。
要靠强首帧、强尾帧、短段生成、参考绑定、控制图、候选筛选和后期包装。
商业模型的优势是审美先验、运动自然度和容错率；开源模型的优势是可控、可复现、可批量和可纳入本地流程。
```

## 10. MVP 任务拆解

### P0: 合同与校验

- 新增 `ShotReferenceBinding` JSON schema。
- 新增 `ReferenceSelection` JSON schema。
- 新增 `blocked_missing_required_reference` 状态。
- 新增生成前校验：缺 must-use 引用直接阻塞。

### P1: 绑定器

- 从共享分镜文档读取导演、美术、提示词、配音、视频区块。
- 从资产索引读取角色、场景、道具、控制图路径。
- 为每个镜头生成绑定文件。

### P2: 选择器

- 候选参考超过 8 张时，先按角色、场景、构图、动作用途筛选。
- 生成 `model_prompt_prefix`。
- 缓存选择结果，并在资产 hash 变化时自动失效。

### P3: 生成接入

- ComfyUI/Wan 工作流 patcher 读取绑定文件。
- I2V 只允许使用绑定的 first frame。
- FLF2V 只允许使用绑定的 first/last frame。
- 视频 manifest 必须记录 `used_refs`。

### P4: 回归测试

必须覆盖：

- 资产存在但未绑定时阻塞。
- 路径失效时阻塞。
- 续跑时仍注入已有 new-camera / first-frame 引用。
- selector 选出越界 ref index 时失败重试。
- manifest 缺 `binding_hash` 或 `used_refs` 时 QC 失败。

## 11. 来源

- Toonflow: `src/agents/productionAgent/tools.ts`, `src/routes/production/workbench/getGenerateData.ts`
- ViMax: `pipelines/script2video_pipeline.py`, `agents/reference_image_selector.py`, `tests/test_wrong_output_guards.py`
- Wan2.2: https://github.com/Wan-Video/Wan2.2
- ComfyUI Wan2.2: https://docs.comfy.org/tutorials/video/wan/wan2_2
- LTX-Video: https://github.com/Lightricks/LTX-Video
- Qwen-Image: https://github.com/QwenLM/Qwen-Image
