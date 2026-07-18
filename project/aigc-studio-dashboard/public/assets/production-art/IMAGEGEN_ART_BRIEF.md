# Imagegen 美术资源生产包

目标：优先使用 `$imagegen` 生成达到当前办公室 2.5D 美术程度的资源。固定办公人员必须烘进整张场景图，不再用网页小人、局部帧、光晕或补丁贴图冒充。

## 画布锁

- 画布：`1536x900`
- 机位：固定等距 2.5D 斜俯视
- 风格母版：`scene/office_base.png`
- 输出目录：`scene/candidates/`
- 正式替换前只保存 candidate，不覆盖 canonical 资产

## 已生成候选

- `scene/candidates/office_fixed_staff_imagegen_v001_source.png`
- `scene/candidates/office_fixed_staff_imagegen_v001.png`

用途：固定办公人员整图烘入候选。不是网页贴图。

## 第一批必须资源

| ID | 文件槽位 | 生成方式 | 验收 |
| --- | --- | --- | --- |
| SCN-01 | `scene/candidates/office_fixed_staff_imagegen_v001.png` | imagegen 编辑空办公室底图 | 14 人真正坐在椅子上，和光照/桌椅/遮挡融合 |
| SCN-02 | `scene/candidates/office_fixed_staff_work_00.png` | imagegen 整图生成 | 和 SCN-01 同构图，只允许手部/头肩有微小工作姿态变化 |
| SCN-03 | `scene/candidates/office_fixed_staff_work_01.png` | imagegen 整图生成 | 同上，不允许背景漂移 |
| SCN-04 | `scene/candidates/office_fixed_staff_work_02.png` | imagegen 整图生成 | 同上，不允许新增/丢失人物 |
| CHR-01 | `characters/female_01/master/threeview_imagegen.png` | imagegen 角色三视图 | 透明/纯色背景，四方向 sprite 可用 |
| CHR-02 | `characters/male_01/master/threeview_imagegen.png` | imagegen 角色三视图 | 透明/纯色背景，四方向 sprite 可用 |

## 不做

- 不做局部手部 patch。
- 不做发光/闪烁提示层。
- 不做低模 Blender 最终图。
- 不把人物作为 DOM/SVG 小人放到椅子上。

## Prompt: SCN-01 固定人员场景图

```text
Use case: precise-object-edit
Asset type: production 2.5D web game scene base layer
Task: create a fixed-staff office scene candidate from the provided empty isometric office image.

Reference priority:
1. The provided empty isometric office scene is the hard composition and layout reference.
2. Preserve the same camera angle, room boundaries, glass walls, desks, chairs, monitors, plants, server room, recording booth, lighting direction, and overall warm realistic 2.5D game-art style.

Hard spatial locks:
- Keep the exact same full-office isometric composition and crop.
- Do not move, add, remove, resize, or redesign furniture, walls, glass, doors, plants, monitors, cabinets, server racks, or floor pattern.
- Add seated workers only in existing office chairs.
- Required seated workers: 6 in the upper workstation office, 1 at the left curved monitor console, 1 at the lower-right curved monitor console, and 6 around the bottom meeting table.
- Every worker must be truly seated in a chair, facing the computer monitor or table from the existing chair orientation.
- People must be partially occluded naturally by chair backs, desk edges, monitors, and table fronts where appropriate.

Character locks:
- 14 total seated office workers, mixed professional office staff, roughly half women and half men.
- Back/side/back-three-quarter views from the isometric camera, not front-facing portraits.
- Natural seated posture: shoulders, head, forearms near keyboard/mouse/table; legs mostly hidden by desk/chair.
- Correct small scale matching the room and existing chairs.

Style and lighting locks:
- High-end realistic 2.5D isometric game background art, polished AIGC studio office, same detail density and material richness as the provided scene.
- Match sunlight, shadows, ambient occlusion, glass reflections, monitor glow, warm wood materials, and color grading.
- Workers must look rendered into the room, not pasted on top.

Must avoid:
- No standing people, no floating people, no people on walls, no people on glass, no people on partitions, no people on screens, no people sitting backward unless the existing chair orientation requires a back view toward the camera.
- No cartoon/vector/chibi/simple icon people.
- No UI overlay, no labels, no text, no logo, no watermark.
- No changed camera angle, no cropped-in view, no new rooms.
```

## Prompt: SCN-02/03/04 整图工作动作帧

用 SCN-01 作为参考图，每次生成一张整图，不做局部 patch。

```text
Use case: precise-object-edit
Asset type: full-scene work-animation frame for 2.5D web game
Task: create one full-frame variation of the fixed-staff office scene where seated workers show subtle active working posture.

Reference priority:
1. Use the provided fixed-staff office scene as the hard visual reference.
2. Preserve composition, camera, furniture, walls, monitors, people count, people identity impression, lighting, shadows, and crop.

Hard locks:
- Output the same full office scene.
- Keep all 14 seated workers in the same chairs.
- Only allow tiny natural changes: forearms closer to keyboard, slight head tilt, slight shoulder angle, tiny mouse/keyboard posture variation.
- Do not create local overlays. This must be a complete coherent frame.

Must avoid:
- No background drift, no furniture drift, no camera drift, no extra people, no missing people.
- No glowing effect, no motion streak, no UI, no text, no watermark.
- No standing people, no floating people, no people on walls/glass/partitions.
```

## Prompt: CHR-01 女移动角色三视图

```text
Use case: character-card
Asset type: 2.5D web game walking character master sheet
Task: generate a female office worker character master sheet for sprite production.

Subject:
- One adult female AIGC studio office worker, professional but not formal, navy jacket, light blouse, dark skirt or trousers, simple office shoes.
- Friendly neutral expression, practical hairstyle, no exaggerated anime features.

Composition:
- Four clean poses on one sheet: front, back, left side, right side.
- Full body visible, consistent height and outfit across all views.
- Arms relaxed at sides, feet visible, no sitting pose.

Style:
- Match polished realistic 2.5D isometric office game art.
- Soft painterly-realistic rendering, compatible with the office scene.

Background:
- Perfectly flat solid #00ff00 chroma-key background for local removal.
- No floor plane, no cast shadow, no reflection.

Must avoid:
- No text, no labels, no watermark, no cropped feet, no different outfit between views.
- Do not use #00ff00 anywhere in the character.
```

## Prompt: CHR-02 男移动角色三视图

```text
Use case: character-card
Asset type: 2.5D web game walking character master sheet
Task: generate a male office worker character master sheet for sprite production.

Subject:
- One adult male AIGC studio office worker, professional but not formal, navy or charcoal jacket, light shirt, dark trousers, simple office shoes.
- Neutral focused expression, short practical hairstyle, no exaggerated anime features.

Composition:
- Four clean poses on one sheet: front, back, left side, right side.
- Full body visible, consistent height and outfit across all views.
- Arms relaxed at sides, feet visible, no sitting pose.

Style:
- Match polished realistic 2.5D isometric office game art.
- Soft painterly-realistic rendering, compatible with the office scene.

Background:
- Perfectly flat solid #00ff00 chroma-key background for local removal.
- No floor plane, no cast shadow, no reflection.

Must avoid:
- No text, no labels, no watermark, no cropped feet, no different outfit between views.
- Do not use #00ff00 anywhere in the character.
```

## QC 标准

每张 scene candidate 必须检查：

- 人是否真的坐在椅子上。
- 是否有站立、浮空、墙上、玻璃上、屏幕上的人。
- 人物是否被桌沿、椅背、显示器自然遮挡。
- 是否保持原办公室构图和房间功能区。
- 是否新增、删除、移动了关键家具。
- 是否有 UI、文字、水印。

只有通过 QC 的候选图才能进入 `scene/office_fixed_staff.png`。
