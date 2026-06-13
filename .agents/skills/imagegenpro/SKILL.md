---
name: imagegenpro
description: SC001/导演分镜候选图专用隔离生图流程。用于用 Codex/OpenAI image generation 生成或重做 reference-frame candidate，尤其是 severed-homeland 第 01 集 SC001 的 r003/r004 门楼、昭明旧帝国金属警钟、薛临墙、同一城墙空间连续性；要求只给短提示词和压缩参考图，不让生图任务读取项目文件、继承长上下文、写文件、做 QC 或直接覆盖 reference-frames。
---

# ImagegenPro

把生图当成隔离子任务。主任务负责读项目文件、选参考图、压缩附件、写提示词、保存结果和 QC；生图任务只接收提示词和图片附件，只返回图片。

## 硬边界

- 不让生图任务读取文件、写文件、搜索、提交 Git、查看项目背景或解释 QC。
- 不把本地文件路径写进图片提示词。
- 每次只生成 1 张目标图。R003 和 R004 必须拆成两个干净任务。
- 输出先保存为 `candidate`，不得直接覆盖 `01/assets/reference-frames/*.png`。
- 若同一生图任务失败、跑偏两次，或参考图集合变化，开新干净任务。

## 参考图优先级

给生图任务的附件按下面顺序筛选，优先不超过 6 张，长边不超过 1600 px，单张不超过 2 MB。

1. `shot/depth/lineart` 约束图：对应镜头的机位、深度、线稿或关键道具关系图。
2. `scene master`：正反场景母版、材质锁相关图，用来统一黑石、旧木、昭明旧帝国金属警钟、雪边和旗帜。
3. `current reference`：现有 reference frame 只作为风格/气氛参考，不作为空间权威。

SC001 空间权威始终是 `layout.yaml` 和同一个 Blender 场景。若现有 reference 与 Blender 控制图冲突，以 Blender 控制图和硬锁为准。

## SC001 硬空间锁

提示词必须包含这些正向锁：

- one exterior blackstone wall, one central timber-and-iron gate, one gatehouse above/behind the gate
- beast attack direction only from outside the wall toward the same gate
- exterior attackers must inherit `C020` northern siege troop group, `C021` companion-beast relationship, and `E01_C020` episode siege state: multi-branch beast soldiers plus bonded siege beasts, not a generic human army or single-species horde
- same ancient Zhaoming old-empire metal alarm bell visible only in R003/R004, hanging under the same timber frame
- the bell is five-thousand-year-old oxidized metal with cracks, dents, missing rim chips, old repairs, and only broken unreadable fragments derived from `P016` Zhaoming sun-moon astrolabe emblem
- `P018` Northern Beast Alliance marks are allowed only as tiny attack-side shield, hide-banner, tack, or siege-equipment details; never place `P018` on the bell
- same blackstone parapet and same gatehouse floor for R003/R004
- P017 black-sun white-wing flags on the wall, never random banners
- when the camera faces outside from the gatehouse or wall-top, the view beyond the parapet is battlefield snow haze, smoke, attackers and siege pressure only; no houses, town lights, streets, city skyline or playable city backplate

提示词必须包含这些禁止项：

- no second wall, no second gate, no extra inner wall in front of the gate
- no attackers inside the wall or inside the gatehouse
- no human army outside the wall, no generic orc crowd, no single-species horde, no ownerless monster pack
- no camera teleport, no 90-degree turn, no 180-degree reverse
- no missing metal alarm bell in R003/R004
- no complete clean emblem on the bell, no new decorative crest, no `P018` beast emblem on the bell, no ivory/bone bell surface
- no houses, town lights, streets, city skyline, city towers or warm windows in exterior-facing R003/R004 views
- no heroic clean war-god styling for Xue Linqiang
- no text, logo, watermark, caption, UI overlay

不要写伪参数如 `weight=100`。改用清晰的“Reference priority / Hard spatial locks / Must avoid”。

## R003 专用提示结构

目标：重做 `r003e01.candidate.png`，修正“警钟过完整、城市/房屋背景错误、士兵像死亡、三层关系不足”的问题。

必须锁定：

- gatehouse interior tight-medium frame
- foreground broken spear sliding through dirty snow mud
- midground `E01_C024A` young grey-wall soldier half-collapsed against blackstone rear wall
- background same ancient Zhaoming old-empire metal alarm bell swinging under same timber frame
- bell chain pulled diagonally by aftershock, timber frame snow shaking loose, blackstone rear wall
- young soldier is alive and knocked down by gate impact aftershock: half-open or squinting eyes, visible cold breath, one hand splayed and bracing in snow mud, bent knee, slipping boot, stunned active strain, not dead
- outside battle pressure only as cold snow haze, smoke and siege vibration through openings
- no houses, city lights, streets or city towers visible through openings

必须避免：

- giant bell close-up as the only subject
- full city panorama, houses, warm windows or town skyline as background
- dead corpse pose, blood-pool death read, soldier standing, heroic front face, clean armor
- closed corpse eyes, limp neck, slack dead face, funeral stillness
- complete clean emblem, ivory/bone bell, changed bell frame, missing spear, missing collapsed soldier

## R004 专用提示结构

目标：重做 `r004e01.candidate.png`，修正“人物过英雄化、墙前误读成第二道墙、墙外出现房屋/城市、警钟过完整”的问题。

必须锁定：

- gatehouse-side rear-three-quarter medium close frame
- Xue Linqiang pressing the same blackstone parapet, facing outward with restrained low-voice command
- cracked frozen hand, coarse wall scarf, old armor, half-dark side profile
- same ancient Zhaoming old-empire metal alarm bell remains on the right/rear under the timber roof, visibly swinging after the impact
- bell surface is oxidized dark metal with cracks, dents, old repairs, chipped rim, and broken unreadable Zhaoming sun-moon astrolabe emblem fragments
- the foreground stone edge is the same wall-top parapet, not another wall
- beast army remains outside/below the wall as `C020`/`C021`/`E01_C020` distant pressure: black-tusk axe infantry, horned shield wall, wolf riders, badger sappers, grey troll laborers, siege mammoth/rhino/oxen shapes and other bonded companion beasts; exterior view has snow haze, smoke and siege shapes only, no houses or city lights

必须避免：

- second wall in front of the gate, extra terrace wall, second gate
- clean heroic poster pose, raised war-god staging, overlarge battlefield panorama
- missing bell, complete clean bell emblem, ivory/bone bell, missing gatehouse roof/posts, attackers inside gatehouse
- houses, town lights, city skyline, streets or interior city backplate when looking outside from the gatehouse
- human army outside, generic orc crowd, single-species beast horde, `P018` beast emblem on the bell

## 新建生图任务模板

```text
任务：只根据本消息中的图片提示词和随附参考图生成 1 张图片。

硬限制：
- 不读取文件，不写文件，不搜索，不查看项目背景，不提交 Git。
- 参考图只作为视觉附件使用，不要把附件路径写入图片提示词。
- 只调用生图工具并返回图片，不输出构图分析、QC、背景说明或其他文字。

参考图附件：
<只附本张图必需的压缩参考图>

图片提示词：
Use case: historical-scene
Asset type: SC001 reference-frame candidate
Reference priority: ...
Hard spatial locks: ...
Shot-specific composition: ...
Materials and lighting: ...
Must avoid: ...
```

## 保存和 QC

主任务生成后把图片复制到：

- `01/assets/director-room/shots/SC001-SH002/candidates/r003e01.candidate.png`
- `01/assets/director-room/shots/SC001-SH003/candidates/r004e01.candidate.png`

QC 至少检查：

- 是否仍是一墙一门、一门楼、同一昭明旧帝国金属警钟。
- R003 是否读出断矛、被震倒但活着的军户、横摆警钟三层关系。
- R003 士兵是否继承 `E01_C024A`，半睁眼/眯眼、可见喘息、撑地、屈膝、靴底打滑，不能读成闭眼死亡。
- R004 是否只有同一墙顶女墙，没有第二道墙，墙外没有房屋/城市，并且敌军继承 `C020`/`C021`/`E01_C020` 的兽族士兵与伴生兽攻城关系。
- 旗帜、黑石、旧木、积雪、旧金属警钟和破损 `P016` 昭明残徽是否与场景母版和背景一致；`P018` 只能在攻城方器具或旗面上作远景小标记，不能上钟。
- 不合格时只重做 candidate，不覆盖 canonical reference frame。
