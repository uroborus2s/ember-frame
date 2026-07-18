# AIGC Studio Dashboard 最终美术资产实施文档

## 结论

当前项目能证明交互方向，但还不是最终美术级方案。要达到“美术示意图级别的场景 + 角色样子，并能在走廊行走、坐椅子、站起来继续行走”，需要补齐三类正式资产：

1. 最终美术分层场景。
2. 高质量角色透明动作帧。
3. 可执行的路线、座位、遮挡数据。

推荐最终资源根目录：

```text
public/assets/production-art/
```

当前 `public/assets/25d/` 只作为技术验证或临时预览，不作为最终美术资产目录。

## 资产目录

```text
public/assets/production-art/
  scene/
    office_base.png
    office_shadow.png
    office_foreground.png
    office_glass.png
    walkable_mask.png
    depth_map.png
    scene.json
    top_view_control.png
  characters/
    female_01/
      master/
        threeview.png
        detail_crops.png
      sprites/
        idle_NE/
        idle_NW/
        idle_SE/
        idle_SW/
        walk_NE/
        walk_NW/
        walk_SE/
        walk_SW/
        sit_NE/
        sit_NW/
        sit_SE/
        sit_SW/
        seated_NE/
        seated_NW/
        seated_SE/
        seated_SW/
        stand_NE/
        stand_NW/
        stand_SE/
        stand_SW/
        typing_NE/
        typing_NW/
        typing_SE/
        typing_SW/
      sprite_meta.json
    male_01/
      master/
      sprites/
      sprite_meta.json
```

## 场景资产制作

目标：用 `public/assets/final-art/office-master.png` 的视觉级别做可交互 2.5D 场景，不再用低模图冒充最终画面。

| 资产 | 必须有 | 制作方式 | 验收 |
| --- | --- | --- | --- |
| `office_base.png` | 无角色、无 UI、无标注的办公室底图 | 以 `office-master.png` 为视觉目标，重绘或修补成 clean plate | 画面达到示意图级别；走廊和座位区域完整 |
| `office_shadow.png` | 透明 PNG 阴影层 | 手绘或从分层文件导出接触阴影 | 人物站在地面不漂 |
| `office_foreground.png` | 半墙、桌沿、椅背、前景植物、门框等遮挡物 | 从最终图抠出透明层，必要时手绘补边 | 人物走到桌后、墙后能被正确遮挡 |
| `office_glass.png` | 玻璃反光、透明隔断、玻璃门高光 | 单独透明层，低 alpha | 不遮死角色，只提供玻璃质感 |
| `walkable_mask.png` | 黑白可行走图 | 白色=可走，黑色=墙/桌/服务器/椅子/禁区 | 路线不会穿桌、穿墙 |
| `depth_map.png` | 灰度深度参考 | 近处亮、远处暗，或按项目约定反过来 | z-index 和遮挡排序可查 |
| `top_view_control.png` | 俯视制作图 | 标出墙、门、窗、桌、椅、走廊、座位编号 | 只做制作/QC，不进页面 |
| `scene.json` | 路线、座位、遮挡、尺寸 | 手写或从工具导出 | 页面能直接读取 |

最小 `scene.json` 结构：

```json
{
  "size": [1536, 900],
  "layers": {
    "base": "scene/office_base.png",
    "shadow": "scene/office_shadow.png",
    "foreground": "scene/office_foreground.png",
    "glass": "scene/office_glass.png",
    "walkableMask": "scene/walkable_mask.png",
    "depthMap": "scene/depth_map.png"
  },
  "walkNodes": {
    "hall_a": { "x": 520, "y": 715 },
    "hall_b": { "x": 385, "y": 635 },
    "hall_c": { "x": 280, "y": 570 }
  },
  "walkEdges": [
    ["hall_a", "hall_b"],
    ["hall_b", "hall_c"]
  ],
  "seats": []
}
```

## 角色资产制作

目标：页面只播放高质量透明 PNG 动作帧。不要在浏览器里实时旋转低模角色。

每个角色必须先有母卡：

| 资产 | 内容 | 验收 |
| --- | --- | --- |
| `master/threeview.png` | 正面、侧面、背面，同一比例、透明背景 | 脸、发型、服装、身高比例一致 |
| `master/detail_crops.png` | 脸、发型、手、工牌、服装材质细节 | 能锁定角色不漂 |

每个角色至少做四个方向：

```text
NE, NW, SE, SW
```

每个方向至少做这些动作：

| 动作 | 帧数 | 用途 |
| --- | ---: | --- |
| `idle_DIR` | 4 | 站立等待 |
| `walk_DIR` | 8 | 走廊行走 |
| `sit_DIR` | 8 | 从站立坐下 |
| `seated_DIR` | 4 | 已坐下静止 |
| `typing_DIR` | 6 | 坐着工作 |
| `stand_DIR` | 8 | 从椅子站起 |

命名规则：

```text
sprites/walk_NE/00.png
sprites/walk_NE/01.png
...
sprites/stand_SW/07.png
```

每一帧必须是透明 PNG，不能带底色、投影背景、文字、编号。

`sprite_meta.json` 必须记录对齐点：

```json
{
  "characterId": "female_01",
  "frameSize": [300, 360],
  "anchors": {
    "walk_NE": { "origin": [150, 330], "anchorType": "feet" },
    "sit_NE": { "origin": [150, 300], "anchorType": "hips" },
    "typing_NE": { "origin": [150, 300], "anchorType": "hips" },
    "stand_NE": { "origin": [150, 300], "anchorType": "hips_to_feet" }
  }
}
```

没有 `origin` 不允许进页面。否则角色走路会抖，坐椅子会漂。

## 座位和椅子朝向

椅子不能只放一个点。每把椅子至少要有：

| 字段 | 作用 |
| --- | --- |
| `approach` | 角色走到椅子旁的站立点 |
| `sit` | 坐下后角色臀部/身体锚点 |
| `facing` | 椅子朝向，取 `NE/NW/SE/SW` |
| `z` | 坐下后的深度排序 |
| `occluders` | 坐下时会挡住角色腿或身体的前景层 |
| `animations` | 这个朝向对应的坐下、坐着、站起动作 |

示例：

```json
{
  "id": "seat_console_01",
  "label": "控制台左座",
  "approach": { "x": 510, "y": 620 },
  "sit": { "x": 485, "y": 560 },
  "facing": "NE",
  "z": 560,
  "occluders": ["office_foreground"],
  "animations": {
    "sit": "sit_NE",
    "seated": "typing_NE",
    "stand": "stand_NE"
  }
}
```

交互流程：

```text
点击椅子
  -> 从当前点沿 walkEdges 走到 seat.approach
  -> 按 seat.facing 切换方向
  -> 播放 seat.animations.sit
  -> 把角色锚点对齐到 seat.sit
  -> 循环 seated 或 typing
  -> 点击起身
  -> 播放 seat.animations.stand
  -> 回到 seat.approach
  -> 继续沿走廊行走
```

## 代码实现方案

最终运行时使用 **React + 2.5D 分层 PNG + 透明角色 sprite + scene.json**。

不使用运行时 3D，不使用 Three.js 预演，不把低模 3D 当作最终生产链路。这个目标要的是美术示意图级别的画面，最终可信度来自正式美术分层图和角色动作帧，不来自实时 3D。

网页最终加载的是 PNG 和 JSON：

```text
React
  -> 读取 scene.json
  -> 渲染 office_base.png
  -> 渲染角色 sprite
  -> 按 z/depth 排序
  -> 渲染 office_foreground.png
  -> 渲染 office_glass.png
```

推荐先沿用当前 `src/Art25DScene.jsx` 的思路，改成读取 `production-art`：

```js
const ROOT = "/assets/production-art";

const scene = await fetch(`${ROOT}/scene/scene.json`).then((r) => r.json());
```

场景层这样用：

```jsx
<img className="scene-layer" src={`${ROOT}/${scene.layers.base}`} />
<img className="scene-layer shadow-layer" src={`${ROOT}/${scene.layers.shadow}`} />

{characters
  .sort((a, b) => a.z - b.z)
  .map((character) => (
    <img
      className="character-sprite"
      src={`${ROOT}/characters/${character.id}/sprites/${character.action}/${character.frame}.png`}
      style={{
        left: character.x - character.origin[0],
        top: character.y - character.origin[1],
        zIndex: character.z
      }}
    />
  ))}

<img className="scene-layer foreground-layer" src={`${ROOT}/${scene.layers.foreground}`} />
<img className="scene-layer glass-layer" src={`${ROOT}/${scene.layers.glass}`} />
```

角色运行状态只需要这几个：

```text
idle
walking
sitting_down
seated
standing_up
```

点击座位后的逻辑：

```js
function goToSeat(character, seat) {
  character.route = findPath(character.position, seat.approach);
  character.targetSeat = seat.id;
  character.state = "walking";
}

function updateCharacter(character, dt) {
  if (character.state === "walking") {
    moveAlongRoute(character, dt);
    character.action = `walk_${movementDirection(character)}`;
    return;
  }

  if (character.state === "sitting_down") {
    character.action = character.seat.animations.sit;
    playOnce(character, () => {
      character.position = character.seat.sit;
      character.state = "seated";
    });
    return;
  }

  if (character.state === "seated") {
    character.action = character.seat.animations.seated;
    return;
  }

  if (character.state === "standing_up") {
    character.action = character.seat.animations.stand;
    playOnce(character, () => {
      character.position = character.seat.approach;
      character.state = "idle";
    });
  }
}
```

`walkable_mask.png` 的用法：

```text
简单版:
  只用 scene.json 的 walkNodes + walkEdges 走固定路线。

升级版:
  点击任意地面时，读取 walkable_mask.png 判断目标点是否可走，
  再用 A* 在 mask 上寻路。
```

本项目先做简单版。办公室不是开放世界，固定走廊路线足够。

最终技术选型：

| 方案 | 是否采用 | 原因 |
| --- | --- | --- |
| React DOM + PNG 分层 + sprite | 采用 | 能直接使用最终美术图，和当前 `Art25DScene.jsx` 最接近 |
| Canvas/PixiJS 2D 引擎 | 暂不采用 | 当前角色少，React DOM 绝对定位够用 |
| 运行时 Three.js 3D 模型 | 不采用 | 达不到目标美术质感，且坐椅、遮挡、角色动作成本更高 |
| 低模 3D 预演再转 2D | 不采用 | 预演结果不能代表最终美术，不能解决最终资产问题 |

什么时候再换 Canvas/PixiJS：

```text
同屏角色超过 20 个；
需要粒子、复杂点击命中、批量动画；
DOM 图片排序和重绘开始卡顿。
```

## 任务拆分

| ID | 任务 | 产物 | 依赖 | 完成标准 |
| --- | --- | --- | --- | --- |
| ART-01 | 锁定最终画布和机位 | `scene/scene-size.md` 或写入 `scene.json` | 无 | 画布尺寸、固定镜头、角色缩放比例确认 |
| ART-02 | 制作办公室 clean plate | `office_base.png` | ART-01 | 无人物、无标注、示意图级别 |
| ART-03 | 制作前景遮挡层 | `office_foreground.png` | ART-02 | 桌沿、椅背、半墙、门框能遮挡角色 |
| ART-04 | 制作玻璃层 | `office_glass.png` | ART-02 | 玻璃质感单独透明层 |
| ART-05 | 制作阴影层 | `office_shadow.png` | ART-02 | 角色站立和坐下不漂 |
| ART-06 | 绘制可走区域 | `walkable_mask.png` | ART-02 | 走廊可走，家具禁走 |
| ART-07 | 制作深度参考 | `depth_map.png` | ART-02 | 可辅助 z-index 和遮挡排序 |
| ART-08 | 标座位和路线 | `top_view_control.png` | ART-02 | 每把椅子、走廊、禁区都有编号 |
| ART-09 | 写场景数据 | `scene.json` | ART-06, ART-08 | 页面可读取路线和座位 |
| CHR-01 | 女角色母卡 | `female_01/master/*` | ART-01 | 三视图和细节图通过 |
| CHR-02 | 男角色母卡 | `male_01/master/*` | ART-01 | 三视图和细节图通过 |
| CHR-03 | 女角色四方向走路 | `female_01/sprites/walk_*` | CHR-01 | 四方向各 8 帧 |
| CHR-04 | 男角色四方向走路 | `male_01/sprites/walk_*` | CHR-02 | 四方向各 8 帧 |
| CHR-05 | 女角色坐下/坐着/站起 | `female_01/sprites/sit_*`, `seated_*`, `stand_*` | CHR-01, ART-09 | 四方向完整 |
| CHR-06 | 男角色坐下/坐着/站起 | `male_01/sprites/sit_*`, `seated_*`, `stand_*` | CHR-02, ART-09 | 四方向完整 |
| CHR-07 | 打字动作 | `typing_*` | CHR-05, CHR-06 | 每方向 6 帧 |
| CHR-08 | 写角色元数据 | `sprite_meta.json` | CHR-03 到 CHR-07 | 每组动作有 origin |
| DEV-01 | 页面切换到 `production-art` | React 读取新目录 | ART-09, CHR-08 | 不再读取低模最终图 |
| DEV-02 | 实现路径移动 | walkEdges 路径行走 | DEV-01 | 角色不穿墙、不跳点 |
| DEV-03 | 实现座位状态机 | sit/seated/stand | DEV-02 | 能坐下、停留、站起 |
| QC-01 | 场景 QC | QC 记录 | ART-02 到 ART-09 | 对照示意图和 mask 检查 |
| QC-02 | 角色 QC | QC 记录 | CHR-01 到 CHR-08 | 角色不漂、动作不抖 |
| QC-03 | 交互 QC | 截图或录屏 | DEV-01 到 DEV-03 | 走廊行走、坐椅、起身闭环成立 |

## 资产 Checklist

### Scene

- [ ] `public/assets/production-art/scene/office_base.png`
- [ ] `public/assets/production-art/scene/office_shadow.png`
- [ ] `public/assets/production-art/scene/office_foreground.png`
- [ ] `public/assets/production-art/scene/office_glass.png`
- [ ] `public/assets/production-art/scene/walkable_mask.png`
- [ ] `public/assets/production-art/scene/depth_map.png`
- [ ] `public/assets/production-art/scene/top_view_control.png`
- [ ] `public/assets/production-art/scene/scene.json`

### Female 01

- [ ] `characters/female_01/master/threeview.png`
- [ ] `characters/female_01/master/detail_crops.png`
- [ ] `characters/female_01/sprites/idle_NE/00-03.png`
- [ ] `characters/female_01/sprites/idle_NW/00-03.png`
- [ ] `characters/female_01/sprites/idle_SE/00-03.png`
- [ ] `characters/female_01/sprites/idle_SW/00-03.png`
- [ ] `characters/female_01/sprites/walk_NE/00-07.png`
- [ ] `characters/female_01/sprites/walk_NW/00-07.png`
- [ ] `characters/female_01/sprites/walk_SE/00-07.png`
- [ ] `characters/female_01/sprites/walk_SW/00-07.png`
- [ ] `characters/female_01/sprites/sit_NE/00-07.png`
- [ ] `characters/female_01/sprites/sit_NW/00-07.png`
- [ ] `characters/female_01/sprites/sit_SE/00-07.png`
- [ ] `characters/female_01/sprites/sit_SW/00-07.png`
- [ ] `characters/female_01/sprites/seated_NE/00-03.png`
- [ ] `characters/female_01/sprites/seated_NW/00-03.png`
- [ ] `characters/female_01/sprites/seated_SE/00-03.png`
- [ ] `characters/female_01/sprites/seated_SW/00-03.png`
- [ ] `characters/female_01/sprites/typing_NE/00-05.png`
- [ ] `characters/female_01/sprites/typing_NW/00-05.png`
- [ ] `characters/female_01/sprites/typing_SE/00-05.png`
- [ ] `characters/female_01/sprites/typing_SW/00-05.png`
- [ ] `characters/female_01/sprites/stand_NE/00-07.png`
- [ ] `characters/female_01/sprites/stand_NW/00-07.png`
- [ ] `characters/female_01/sprites/stand_SE/00-07.png`
- [ ] `characters/female_01/sprites/stand_SW/00-07.png`
- [ ] `characters/female_01/sprite_meta.json`

### Male 01

- [ ] `characters/male_01/master/threeview.png`
- [ ] `characters/male_01/master/detail_crops.png`
- [ ] `characters/male_01/sprites/idle_NE/00-03.png`
- [ ] `characters/male_01/sprites/idle_NW/00-03.png`
- [ ] `characters/male_01/sprites/idle_SE/00-03.png`
- [ ] `characters/male_01/sprites/idle_SW/00-03.png`
- [ ] `characters/male_01/sprites/walk_NE/00-07.png`
- [ ] `characters/male_01/sprites/walk_NW/00-07.png`
- [ ] `characters/male_01/sprites/walk_SE/00-07.png`
- [ ] `characters/male_01/sprites/walk_SW/00-07.png`
- [ ] `characters/male_01/sprites/sit_NE/00-07.png`
- [ ] `characters/male_01/sprites/sit_NW/00-07.png`
- [ ] `characters/male_01/sprites/sit_SE/00-07.png`
- [ ] `characters/male_01/sprites/sit_SW/00-07.png`
- [ ] `characters/male_01/sprites/seated_NE/00-03.png`
- [ ] `characters/male_01/sprites/seated_NW/00-03.png`
- [ ] `characters/male_01/sprites/seated_SE/00-03.png`
- [ ] `characters/male_01/sprites/seated_SW/00-03.png`
- [ ] `characters/male_01/sprites/typing_NE/00-05.png`
- [ ] `characters/male_01/sprites/typing_NW/00-05.png`
- [ ] `characters/male_01/sprites/typing_SE/00-05.png`
- [ ] `characters/male_01/sprites/typing_SW/00-05.png`
- [ ] `characters/male_01/sprites/stand_NE/00-07.png`
- [ ] `characters/male_01/sprites/stand_NW/00-07.png`
- [ ] `characters/male_01/sprites/stand_SE/00-07.png`
- [ ] `characters/male_01/sprites/stand_SW/00-07.png`
- [ ] `characters/male_01/sprite_meta.json`

### Data

- [ ] `scene.json` includes all walk nodes.
- [ ] `scene.json` includes all walk edges.
- [ ] `scene.json` includes every clickable chair.
- [ ] Every seat has `approach`.
- [ ] Every seat has `sit`.
- [ ] Every seat has `facing`.
- [ ] Every seat has `z`.
- [ ] Every seat has sit/seated/stand animation names.
- [ ] Every animation group has an `origin` in `sprite_meta.json`.
- [ ] Final page uses `production-art`, not `25d`, for final mode.

## 不做的事

- 不继续把低模 Blender 角色当最终角色。
- 不用旋转 PNG 伪造椅子朝向。
- 不用单张 `office-master.png` 直接当完整可交互场景。
- 不在最终图里放箭头、编号、路线、UI 标记。
