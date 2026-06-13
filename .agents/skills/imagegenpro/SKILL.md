---
name: imagegenpro
description: 通用导演分镜/参考帧隔离生图流程。用于用 Codex/OpenAI image generation、ComfyUI 或其他生图工具生成、重做、风格统一或局部修正任意项目图片，尤其擅长处理同一场景空间一致性、角色身份一致性、道具/物品站位一致性、镜头连续性、材质光影统一和 candidate 到正式 reference-frame 的晋升；要求主任务先读项目上下文并写清短提示词和压缩参考图，生图任务不读取项目文件、不继承长上下文、不写文件、不做 QC。
---

# ImagegenPro

ImagegenPro 是通用的“隔离生图 + 连续性控制”流程，不是 SC001/R003/R004 专用工具。

主任务负责读项目文件、理解剧情/镜头/角色/物品/场景锁、选择参考图、压缩附件、写短提示词、保存结果、做 QC 和更新记录。生图任务只接收本次需要的提示词和图片附件，只返回图片。

## 适用范围

使用本 skill 处理所有需要图像一致性的生产任务，包括：

- 生成或重做 reference-frame、candidate、keyframe、场景母版、角色状态图、道具图、镜头首尾帧。
- 让多张图保持同一场景空间、同一角色身份、同一物品站位、同一材质和同一光影风格。
- 根据已批准帧统一后续帧的真实感、颗粒密度、光影、材质分离和色调。
- 从 candidate 晋升到正式 reference-frame，或在用户批准后覆盖正式图。
- 将复杂项目上下文压缩成生图工具能执行的短提示词和少量参考图。

不要把本 skill 绑定到某个项目、场景、角色或镜头编号。项目专项要求只能放在“案例锁”或本次任务提示词里。

## 硬边界

- 生图任务不读取文件、不写文件、不搜索、不提交 Git、不查看项目背景、不解释 QC。
- 不把本地文件路径写进图片提示词；路径只给主任务用于加载/复制文件。
- 每次只生成 1 张目标图。相邻镜头、首尾帧、同一镜头多版本都拆成干净任务，避免上下文污染。
- 输出默认先保存为 `candidate` 或版本化文件；不得直接覆盖正式 reference-frame。
- 只有用户或导演明确批准晋升/替换时，才覆盖正式 `reference-frames` 或其他 canonical 资产。
- 若同一生图任务失败、跑偏两次，或参考图集合变化，开新干净任务。
- 不写伪参数如 `weight=100`。用清晰自然语言表达优先级：`Reference priority`、`Hard locks`、`Must avoid`。

## 输入整理

主任务先建立本次图片的“一致性包”：

1. **目标图**：要生成/修正的文件槽位、镜头 ID、用途、是否允许晋升正式图。
2. **空间锁**：场景尺寸、方向、主要建筑/地形、摄像机位置、可见/不可见区域。
3. **角色锁**：角色 ID、年龄/身份、服装、姿态、表情状态、禁止误读。
4. **物品锁**：道具 ID、位置、朝向、材质、徽章/文字/损坏状态、是否必须同一物。
5. **风格锁**：已批准参考帧、光源、颗粒度、真实感、材质分离、色调。
6. **负面锁**：会破坏连续性的错误空间、错误角色、错误道具、错误徽章、错误风格。

如果这些信息已经存在于 `layout.yaml`、scene bible、shot list、asset index、character card、prop card、material lock 或 QC 报告中，主任务读取后压缩为提示词；不要让生图任务自己读这些文件。

## 参考图优先级

给生图任务的附件按下面顺序筛选，优先不超过 6 张，长边不超过 1600 px，单张不超过 2 MB。

1. **结构控制图**：shot guide、depth、lineart、pose、mask、layout、key prop placement，用来锁空间、机位和物品站位。
2. **已批准母版**：scene master、material lock render、style board、approved reference frame，用来锁材质、光影和真实感。
3. **角色/道具卡**：character state card、prop card、emblem card、costume card，用来锁身份与符号来源。
4. **当前图**：现有 candidate/reference 只作为构图或气氛参考；若它与结构控制图冲突，以结构控制图和硬锁为准。

## 通用提示词结构

```text
Use case: historical-scene / storyboard-keyframe / character-card / prop-card / style-match
Asset type: <project/episode/scene/shot/image-slot>
Task: generate / edit / style-match / local-fix / promote-ready candidate

Reference priority:
1. <structure/control image role>
2. <approved scene/style reference role>
3. <character/prop identity reference role>
4. <current image role, if any>

Hard spatial locks:
- <one scene, one direction, fixed architecture/terrain/camera rules>

Character locks:
- <character IDs, identity, posture, expression, action state, forbidden misread>

Prop and material locks:
- <prop IDs, exact position/orientation/material/emblem/damage rules>

Style and lighting locks:
- <approved frame style, realism level, grain/noise policy, color and light hierarchy>

Shot-specific composition:
- <foreground/midground/background and camera framing>

Must avoid:
- <space errors, identity drift, prop drift, wrong symbol, text/logo/watermark, cheap artifacts>
```

## 一致性 QC

主任务收到图后至少检查：

- **空间一致性**：是否仍是同一场景、同一方向、同一机位逻辑；是否出现第二空间、错误建筑、错误入口、错误远景。
- **角色一致性**：角色年龄、身份、服装、脸部、姿态、动作状态是否和角色卡/镜头描述一致；是否产生死亡/受伤/情绪等误读。
- **物品站位一致性**：关键道具是否在同一位置、同一高度、同一朝向、同一材质；徽章/文字/破损状态是否来自正确资产。
- **镜头连续性**：相邻帧是否能放在同一空间内顺切；首尾帧是否保留同一动作轴线。
- **风格一致性**：颗粒、锐化、真实感、光影、色调、材质分离是否匹配已批准参考帧。
- **交付边界**：candidate 未经批准不得覆盖正式帧；用户明确要求替换正式图时，先保存/归档旧图，再覆盖并更新记录。

不合格时只重做 candidate 或局部修图，不盲目改正式 reference-frame。

## 常见任务策略

### 生成新镜头

- 先用结构控制图锁机位和空间，再用已批准帧锁风格。
- 提示词只写本镜头必需内容，不把整个项目设定塞进去。
- 关键角色和关键道具用 ID + 可见状态 + 禁止误读表达。

### 统一风格

- 以已批准帧为风格目标，明确“只改风格/材质/光影，不改构图和空间关系”。
- 指出要减少或增加的具体风格项：颗粒密度、数字噪点、锐化、雪雾、材质分离、暗部层次、边缘光。
- QC 时对比源图和风格目标，确认没有漂移角色、道具和空间。

### 晋升正式图

- 只有用户/导演明确说“替换正式图”“晋升 reference-frame”“这张没问题”时执行。
- 覆盖前归档旧 candidate 或旧正式图，或至少保留生成源路径。
- 覆盖后让 candidate mirror 与正式图保持一致，并用 hash 或尺寸检查确认。
- 更新任务清单、资源索引、QC、反馈日志和报告，避免仍写“pending QC”。

## 项目案例锁：severed-homeland / 01 / SC001

以下只是案例，不是本 skill 的通用触发范围。处理其他图片时，应建立对应项目自己的案例锁。

### SC001 通用空间锁

- one exterior blackstone wall, one central timber-and-iron gate, one gatehouse above/behind the gate
- beast attack direction only from outside the wall toward the same gate
- exterior attackers inherit `C020` northern siege troop group, `C021` companion-beast relationship, and `E01_C020` episode siege state
- same ancient Zhaoming old-empire metal alarm bell visible only where the shot requires it, hanging under the same timber frame
- bell is five-thousand-year-old oxidized metal with cracks, dents, missing rim chips, old repairs, and broken unreadable fragments derived from `P016`
- `P018` Northern Beast Alliance marks are allowed only as tiny attack-side shield, hide-banner, tack, or siege-equipment details; never on the bell
- P017 black-sun white-wing flags on the wall, never random banners

### SC001 常见禁止项

- no second wall, no second gate, no extra inner wall in front of the gate
- no attackers inside the wall or inside the gatehouse unless the script explicitly says the wall has fallen
- no human army outside the wall, no generic single-species horde, no ownerless monster pack
- no camera teleport, no 90-degree turn, no 180-degree reverse
- no complete clean emblem on the bell, no new decorative crest, no `P018` beast emblem on the bell, no ivory/bone bell surface
- no houses, town lights, streets, city skyline, city towers or warm windows in exterior-facing gatehouse/wall-top views
- no heroic clean war-god styling for Xue Linqiang
- no text, logo, watermark, caption, UI overlay

### SC001 R003/R004 示例

- R003: gatehouse interior, foreground broken spear, `E01_C024A` young grey-wall soldier alive after aftershock, same swinging Zhaoming metal alarm bell.
- R004: gatehouse-side rear-three-quarter view, Xue Linqiang pressing the same parapet, exterior C020/C021/E01_C020 siege pressure, same old metal alarm bell in background.

这些示例用于说明如何写锁，不应让 imagegenpro 只服务这两个镜头。
