---
name: imagegenpro
description: SC001/导演分镜候选图专用隔离生图流程。用于用 Codex/OpenAI image generation 生成或重做 reference-frame candidate，尤其是 severed-homeland 第 01 集 SC001 的 r003/r004 门楼、骨钟、薛临墙、同一城墙空间连续性；要求只给短提示词和压缩参考图，不让生图任务读取项目文件、继承长上下文、写文件、做 QC 或直接覆盖 reference-frames。
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
2. `scene master`：正反场景母版、材质锁相关图，用来统一黑石、旧木、骨钟、雪边和旗帜。
3. `current reference`：现有 reference frame 只作为风格/气氛参考，不作为空间权威。

SC001 空间权威始终是 `layout.yaml` 和同一个 Blender 场景。若现有 reference 与 Blender 控制图冲突，以 Blender 控制图和硬锁为准。

## SC001 硬空间锁

提示词必须包含这些正向锁：

- one exterior blackstone wall, one central timber-and-iron gate, one gatehouse above/behind the gate
- beast attack direction only from outside the wall toward the same gate
- same bone bell visible only in R003/R004, hanging under the same timber frame
- same blackstone parapet and same gatehouse floor for R003/R004
- P017 black-sun white-wing flags on the wall, never random banners
- city behind the wall is only a low-detail distant backplate when visible

提示词必须包含这些禁止项：

- no second wall, no second gate, no extra inner wall in front of the gate
- no attackers inside the wall or inside the gatehouse
- no camera teleport, no 90-degree turn, no 180-degree reverse
- no missing bone bell in R003/R004
- no heroic clean war-god styling for Xue Linqiang
- no text, logo, watermark, caption, UI overlay

不要写伪参数如 `weight=100`。改用清晰的“Reference priority / Hard spatial locks / Must avoid”。

## R003 专用提示结构

目标：重做 `r003e01.candidate.png`，修正“骨钟过大、城市背景过强、三层关系不足”的问题。

必须锁定：

- gatehouse interior tight-medium frame
- foreground broken spear sliding through dirty snow mud
- midground young grey-wall soldier half-collapsed against blackstone rear wall
- background same bone bell swinging under same timber frame
- readable bell chain, timber frame snow, blackstone rear wall
- outside battle pressure only as cold haze through openings

必须避免：

- giant bell close-up as the only subject
- full city panorama as dominant background
- soldier standing, heroic front face, clean armor
- changed bell frame, missing spear, missing collapsed soldier

## R004 专用提示结构

目标：重做 `r004e01.candidate.png`，修正“人物过英雄化、墙前误读成第二道墙”的问题。

必须锁定：

- gatehouse-side rear-three-quarter medium close frame
- Xue Linqiang pressing the same blackstone parapet, facing outward with restrained low-voice command
- cracked frozen hand, coarse wall scarf, old armor, half-dark side profile
- same bone bell remains on the right/rear under the timber roof
- the foreground stone edge is the same wall-top parapet, not another wall
- beast army remains outside/below the wall as distant pressure

必须避免：

- second wall in front of the gate, extra terrace wall, second gate
- clean heroic poster pose, raised war-god staging, overlarge battlefield panorama
- missing bell, missing gatehouse roof/posts, attackers inside gatehouse

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

- 是否仍是一墙一门、一门楼、同一骨钟。
- R003 是否读出断矛、军户、骨钟三层关系。
- R004 是否只有同一墙顶女墙，没有第二道墙。
- 旗帜、黑石、旧木、积雪、骨钟材质是否与场景母版一致。
- 不合格时只重做 candidate，不覆盖 canonical reference frame。
