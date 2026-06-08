# 第01集 SC001 ComfyUI 完整提示词

## 使用说明

中文：本文件是可直接复制到 ComfyUI prompt 节点的分段组装版提示词。每个镜头复制一组 `positive_prompt` 和 `negative_prompt` 即可，不要再复制 JSON 字段名。中文和英文任选一套使用，不建议同一轮同时混用两套语言。

English: This file contains sectioned, copy-ready assembled prompts for ComfyUI prompt nodes. Copy one `positive_prompt` and one `negative_prompt` per shot; do not copy JSON field names. Use either the Chinese or English pair for a render pass, not both languages mixed together.

## ComfyUI 图片节点配置 / Image Node Binding

中文：ComfyUI 不会自动读取 prompt 里的文件名。下面这些图片必须通过 `Load Image` 或等价图片输入节点接入 workflow，再连接到 FLF2V/I2V、IPAdapter、Reference-only、Redux 或你实际使用的参考图分支。不要只把文件名写进 prompt。

English: ComfyUI cannot automatically read image file names written in a prompt. The following images must be loaded through `Load Image` or equivalent image-input nodes, then connected to FLF2V/I2V, IPAdapter, Reference-only, Redux, or the reference branch used by the actual workflow. Do not rely on file names in the prompt text.

| Asset | Path | Required Node Role | Suggested Binding |
| --- | --- | --- | --- |
| SH001 first frame | `01/assets/reference-frames/r001e01.png` | `PLACEHOLDER_FIRST_FRAME_IMAGE_NODE` | FLF2V primary first-frame input |
| SH001 last frame | `01/assets/reference-frames/r002e01.png` | `PLACEHOLDER_LAST_FRAME_IMAGE_NODE` | FLF2V primary last-frame input |
| SH002 first frame | `01/assets/reference-frames/r003e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | I2V primary image input |
| SH003 first frame | `01/assets/reference-frames/r004e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | I2V primary image input |
| 兽族多兵种母卡 / Beast troop master | `assets/characters/c020m.png` | `PLACEHOLDER_BEAST_TROOP_MASTER_IMAGE_NODE` | Beast reference/IPAdapter branch, SH001 weight about `0.50`, SH002/SH003 background weight about `0.35` |
| 伴生兽母卡 / Companion beast master | `assets/characters/c021m.png` | `PLACEHOLDER_COMPANION_BEAST_MASTER_IMAGE_NODE` | Beast reference/IPAdapter branch, SH001 weight about `0.40`, SH002/SH003 background weight about `0.30` |
| 本集兽族状态卡 / Episode beast state | `01/assets/characters/c020e01.png` | `PLACEHOLDER_EPISODE_BEAST_STATE_IMAGE_NODE` | Beast reference/IPAdapter branch, SH001 weight about `0.55`, SH002/SH003 background weight about `0.40` |

中文：SH001 的首尾帧权重最高；三张兽族参考图只负责锁外形、多兵种和伴生兽多样性，不替代首尾帧。SH002/SH003 里兽族只在墙外背景，因此兽族参考权重必须低于人物身份参考和 I2V 首帧。

English: For SH001, first/last frames are the highest-priority inputs; the three beast references only lock silhouette, troop variety and companion-beast diversity, and must not replace the first/last frames. In SH002/SH003 the beast army is background-only, so beast reference weights must stay lower than the human identity reference and I2V first frame.

## SC001-SH001 FLF2V 节点配置 / FLF2V Node Setup

中文：尾帧不是单独接到解码或视频节点的。`r002e01.png` 只接入 `Wan首尾帧视频` 的 `结束图像`，由该节点生成带首尾帧约束的 positive、negative 和 latent，再交给采样器。

English: The last frame is not connected directly to decode or video output nodes. `r002e01.png` goes into the `end_image` input of the Wan first-last-frame video node; that node then produces conditioned positive, negative and latent outputs for the sampler.

| Node | Setting / Connection |
| --- | --- |
| `Load Image` first | `01/assets/reference-frames/r001e01.png` -> resize/crop 16:9 -> `Wan首尾帧视频 / 起始图像` |
| `Load Image` last | `01/assets/reference-frames/r002e01.png` -> same resize/crop -> `Wan首尾帧视频 / 结束图像` |
| `Wan首尾帧视频` size | production `1280 x 720`; preview `960 x 544`; do not use `640 x 640` for this shot |
| `Wan首尾帧视频` length | target `84`; if the Wan build requires `4n+1`, use `85` at `24fps`, not `81` at `16fps` |
| `Wan首尾帧视频` batch | `1` |
| `CLIP Text Encode` | positive/negative prompt -> `Wan首尾帧视频` positive/negative inputs |
| `Wan首尾帧视频` outputs | positive/negative/latent -> `K采样器（高级）` positive/negative/latent image |
| `ModelSamplingSD3` | keep shift `8.0` if required by the workflow template; model output -> `K采样器（高级） / 模型` |
| `K采样器（高级）` | seed fixed for test, steps `20` preview or `28` final, cfg `4.0`, sampler `euler`, scheduler `simple` |
| `VAE解码` | `K采样器` latent -> `VAE解码 / Latent`; same VAE -> `VAE解码 / vae` |
| `创建视频` | `VAE解码` image sequence -> images, fps `24` |
| `保存视频` | filename prefix `01/renders/raw/sc001-sh001`, format/encoder `auto` for test or H.264/MP4 for final |

中文：如果当前 `Wan首尾帧视频` 节点有 `clip 视觉起始图像` / `clip 视觉结束图像` 输入，就把同一张 resized 首帧/尾帧再走对应的 CLIP Vision Encode 分支后接进去；如果模板没有这两个输入，可以只接 `起始图像` / `结束图像`。采样器建议先只保留一个主采样器，输出接 `VAE解码`；双采样会提高尾帧漂移风险，除非后续专门做二段细化。

### 角色建模参考节点 / Character Reference Nodes

中文：角色建模参考不是接到 `VAE解码` 或 `创建视频`，而是接在采样前的 model/reference 分支。SH001 里人物只是墙头中景偏近的守军，不要让角色参考抢过首尾帧。

| Reference | Suggested Node Path | Weight / Schedule |
| --- | --- | --- |
| `01/assets/characters/c024ae01.png` 年轻军户 | `Load Image -> CLIP Vision Encode or IPAdapter image input -> Character IPAdapter/reference node -> K采样器 model` | `0.25-0.30`, start `0.55`, end `1.00`; only helps tail-frame human defender continuity |
| `01/assets/characters/c004e01.png` 薛临墙 | Only add if Xue is visibly present in the SH001 tail frame; otherwise reserve for SH003 | `0.20-0.25`, start `0.65`, end `1.00` |

中文：如果同时有兽族参考和人物参考，建议模型链为：`Checkpoint/LoRA -> ModelSamplingSD3 shift 8.0 -> Character IPAdapter -> Beast IPAdapter -> K采样器 model`。人物参考权重要低于首尾帧，兽族参考权重也不能把镜头拉回兽群特写。

## SC001-SH001

- Method: `FLF2V`
- Duration: `3.5s / 84 frames @ 24fps`
- First frame: `01/assets/reference-frames/r001e01.png`
- Last frame: `01/assets/reference-frames/r002e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Beast refs: `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png`（必须接入图片节点，不只是写进 prompt）
- Output: `01/renders/raw/sc001-sh001.mp4`

### positive_prompt_zh

```text
**风格**
超写实电影质感低魔东方史诗，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，材质与空间以参考帧为准，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
在暴雪中建立锁喉关外墙攻城压力：从攻城方斜后侧低机位的兽潮构图起，沿同一面外墙上升，落到墙头外沿中景偏近的骨钟、黑石女墙和人族守军；镜头仍面向同一个墙外攻城面，墙外兽潮仍在斜下方可见，为切入人族身体代价做转场。

**光影**
斜侧攻城建立镜头布光：冷白暴雪天光压出黑墙巨型剪影，黑墙负补光吞掉墙面和兽潮大暗面；远处暗红火线和火盆亮度克制，从低位反打雪雾、烟尘、攻城队列、旗帜破布、旧铁、巨角边缘、骨钟和守军肩线，形成残酷战场尺度。

**画面内容**
首帧构图是攻城方斜后侧低机位，三分之四角度看同一面锁喉关黑石巨墙；前景只有继承已接入兽族攻城兵种母卡、伴生兽关系母卡和本集兽族状态卡的兽族攻城队列肩背、旧铁甲片、破旗、火盆、雪泥脚步和一截巨兽背脊或巨角，兽潮从画面左前方斜推向右后方城门，城门不居中、军阵不对称，远处墙头只见很小的同一口骨钟和守军剪影。尾帧构图是同一城头外沿中景偏近，画面一半是同一钟架、同一口骨钟、黑石女墙、雪泥墙面、守军肩背、冻裂手、长矛或门闩局部；另一半从垛口或墙外侧俯看城外兽族和伴生兽仍朝这面墙攻来。城内侧、墙后方和城墙另一边不展开，不出现另一侧也被攻击。全镜头只允许一面城墙、一个钟架、一口钟。

**运镜**
使用首尾参考帧约束斜侧攻城到同一墙头落点。镜头顺旗杆、烟柱、巨角和同一面黑墙外立面斜爬上墙头，旁白随起镜进入；到达墙头后只沿女墙方向做小角度偏转，把骨钟和人族守军带入前景，但镜头视线仍留在同一个墙外攻城面。不越过墙脊看向城内或后墙，不正面穿向城门，不穿墙，不做180度调头，不生成远处第二道墙、第二个城门或第二个钟架。骨钟横摆、雪雾吃画面和钟声裂响可作为隐藏剪切点，下一镜切到同一口骨钟旁的年轻军户。

**约束**
人族守军在墙头，兽族攻城方只在同一面城墙外侧和墙下；尾帧必须同时读到墙头人族空间和斜下方同一侧墙外兽潮方向。禁止把城墙读成两边都被攻击的横墙，禁止出现城内另一侧战场、后城墙厚度主景、墙内侧兽潮。兽族士兵和伴生兽必须继承已接入图片节点的三张兽族参考图：兽族攻城兵种母卡、伴生兽关系母卡、本集暴雪兽族状态卡；必须保持黑牙斧兵、铁角盾墙、雪狼骑、灰皮拖城巨魔、雪羽攀墙斥候、破门猛犸、岩背犀或牦牛、霜狼等多兵种、多伴生兽形态，不能泛化成单一种类兽群。骨钟属于墙头同一警钟架，残缺淡金旧日月痕只能被裂缝、铜锈和雪泥遮住，不能完整发光。
旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要现代服饰、枪械、科幻 UI、塑料 CG、正面居中城门、左右完全对称军阵、航拍感、游戏飞镜、穿墙、越过城墙看向另一边、城墙两侧都被攻击、后城墙厚度变主景、城内侧兽潮、180度调头、远处第二道城墙、第二个钟架、第二只钟、钟架方向变化、城外人族、兽族看镜头列队、纯骨钟特写、看不到墙头守军、看不到墙外兽潮方向、完整发光徽章、巨龙化猛犸、魔法光柱、神圣金光、过曝 bloom、镜头光斑滥用、漂浮慢动作、血腥奇观、画面中文字、随机字幕、战场空间跳变。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, real body weight, real speed, natural breathing, contact reaction.

**Goal**
Establish the Suohou Gate outer-wall siege pressure in blizzard: begin from a low diagonal rear-side siege composition, climb along the same exterior wall face, and land on the exterior edge of the wall top with bone bell, blackstone parapet and human defenders; the camera still faces the same exterior siege side, with the beast tide visible below on a diagonal as the transition into human bodily cost.

**Lighting**
Diagonal siege-establishing lighting: cold blizzard sky light silhouettes the massive black wall, black-wall negative fill swallows the wall face and the beast tide's large shadow masses; distant dark-red firelines and braziers stay controlled in brightness and low-counterlight snow haze, smoke, siege ranks, torn banners, old iron, horn edges, bone bell and defender shoulder lines, creating brutal battlefield scale.

**Visual Content**
First-frame composition: low diagonal rear-side siege angle, a three-quarter view of the same Suohou Gate blackstone wall; foreground shows only beast siege shoulders, old iron armor plates, torn banners, brazier fire, snow-mud footsteps and one partial beast spine or horn inherited from the loaded beast troop master, companion-beast master and episode beast-state references, with the beast tide pushing from front-left toward the gate at rear-right, the gate not centered and the ranks not symmetrical, while the same wall-top bone bell and defenders are only small silhouettes far away. Last-frame composition: same exterior-edge wall-top medium-near endpoint, split between the same bell frame, same broken bell, blackstone parapet, snow-mud wall surface, defender shoulders, cracked hands, spear or gate-bar details, and a diagonal downward view through merlons or along the exterior side toward beast troops and companion beasts still facing this wall. The inner side of the wall, the rear side and the opposite side of the wall do not open up, and there is no second-side attack. Only one wall, one bell frame and one bell are allowed through the shot.

**Camera / Motion**
Use first and last reference frames to constrain the move from diagonal siege pressure to the same wall-top landing. The camera climbs along flags, smoke columns, horn shapes and the same exterior black wall toward the bone bell as the voiceover enters, then makes only a small yaw along the parapet line to bring the bell and human defenders into the foreground while still looking toward the same exterior siege side. It does not cross over the wall crown to look into the city or rear side, push frontally into the gate, pass through the wall, make a 180-degree turn, or create a distant second wall, second gate or second bell frame. The bell swing, snow haze swallowing the frame and cracked bell sound can act as the hidden cut point into the next shot beside the same bell and young soldier.

**Constraints**
Human defenders stay on the wall top, and beast attackers stay only outside and below the same exterior side of the wall; the last frame must read both the human wall-top space and the same-side exterior beast tide direction below on a diagonal. Never read the wall as a horizontal barrier attacked from both sides; do not show an inner-side battlefield, rear-wall thickness as the main subject, or beast attackers inside the wall. Beast soldiers and companion beasts must inherit the three loaded beast reference images: the beast siege troop master, the companion-beast relationship master and the episode blizzard beast-state card. Preserve varied troop and beast types such as black-tooth axe troops, iron-horn shield wall, snow-wolf riders, grey-skinned city-dragging trolls, snow-feather climbers, gate-breaking mammoths, rock-backed rhino or yak forms, and frost wolves; never collapse them into one generic beast crowd. The bone bell belongs to the same wall-top bell frame, and faint broken old sun-moon traces must be obscured by cracks, verdigris and snow mud, never complete or glowing.
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid modern clothing, firearms, sci-fi UI, plastic CGI, centered frontal gate, perfectly symmetrical ranks, aerial-game feeling, game-like flying camera, passing through the wall, crossing over the wall to look at the opposite side, both sides of the wall under attack, rear-wall thickness as the main subject, beast attackers inside the wall, 180-degree turn, distant second wall, second bell frame, second bell, changed bell-frame direction, humans outside the wall, beast troops posing toward camera, pure bone-bell close-up, missing wall-top defenders, missing exterior beast-tide direction, complete glowing emblem, dragon-like mammoth, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, gore spectacle, text in image, random subtitles, battlefield spatial jumps.
```

## SC001-SH002

- Method: `I2V`
- First frame: `01/assets/reference-frames/r003e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc001-sh002.mp4`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，材质与空间以参考帧为准，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
把战场规模压到年轻灰墙军户的身体代价：他跪在同一座骨钟旁，断矛落在雪泥里，带血手掌被冻在裂开的钟面上。

**光影**
身体代价近景布光：光源收窄，不再追求大场面纵深；冷白暴雪主光变成贴近骨钟和手掌的冰青反光，钟裂里吃进冷光，黑墙负补光压住人物肩背和背景；远处火线只保留很弱的低位暖边，勾出暗红冻血、手指和骨钟裂边。

**画面内容**
年轻军户、裂开的骨钟、冻血手掌、断矛、黑石墙头和远处墙外攻城影同框；他跪在雪泥里短促喘息，手指因冻血粘连而微抖，断矛在脚边轻滑半寸，暴雪打在旧甲片和钟面上，反应克制、不英雄化、不猎奇。旧日月刻痕只是一点残缺淡金旧痕，钟裂里吃进冷光，血迹只被弱暖火边勾出暗红，背景战场保持低照度压迫感。

**运镜**
以参考帧为首帧，保持人物贴钟姿态和墙外背景层次。镜头不做大移动，只允许极轻微的压近或稳定手持感，重点锁住手、钟裂和断矛的物理反应。

**约束**
骨钟仍在同一墙头警钟架，墙外战场方向不变；墙外远景兽族和伴生兽继承已接入的兽族攻城兵种母卡、伴生兽关系母卡和本集兽族状态卡，但权重低于年轻军户和 I2V 首帧；旧徽不发光，冻血暗红，儿童化或英雄化脸型都不可出现。
旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要强光圣徽、不要英雄摆拍、不要神圣逆光、不要过曝 bloom、不要过度血腥、不要面部美化、不要现代甲胄、不要骨钟位置漂移、不要背景战场换方向。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, real body weight, real speed, natural breathing, contact reaction.

**Goal**
Compress the battlefield scale into the young grey-wall soldier's bodily cost: he kneels beside the same bone bell, broken spear in snow mud, blooded palm frozen to the cracked bell surface.

**Lighting**
Bodily-cost close-shot lighting: the light sources narrow instead of chasing large-scale depth; cold blizzard key light becomes ice-blue bounce near the bell and palm, cold light sinks into bell cracks, and black-wall negative fill presses down the soldier's shoulders and background; distant fire keeps only a very weak low warm edge on dark frozen blood, fingers and bell cracks.

**Visual Content**
Young soldier, cracked bone bell, frozen blooded palm, broken spear, blackstone wall top and distant exterior siege shadows share the frame; he kneels in snow mud with short breaths, fingers trembling slightly where frozen blood sticks them to the bell, the broken spear sliding a fraction near his foot, blizzard striking old armor plates and bell surface, restrained and neither heroic nor exploitative. The old sun-moon mark is only a faint broken gold trace, cold light sinks into bell cracks, blood is edged dark red only by weak warm fire rim, and the background battlefield stays low-lit and oppressive.

**Camera / Motion**
Use the reference image as first frame, preserving the soldier's bell-contact pose and exterior background layers. The camera does not make a large move, allowing only a very slight push-in or stable handheld feel, locked on the physical reaction of hand, bell crack and broken spear.

**Constraints**
The bone bell remains in the same wall-top bell frame and the exterior battlefield direction does not change; distant exterior beast troops and companion beasts inherit the loaded beast troop master, companion-beast master and episode beast-state references, with lower weight than the young soldier and the I2V first frame; the old emblem does not glow, frozen blood is dark red, and no childlike or heroic face treatment appears.
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid bright sacred emblem, heroic posing, divine backlight, overexposed bloom, excessive gore, beautified face, modern armor, drifting bell position, background battlefield direction change.
```

## SC001-SH003

- Method: `I2V`
- First frame: `01/assets/reference-frames/r004e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc001-sh003.mp4`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，材质与空间以参考帧为准，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
表现薛临墙在同一墙头空间内低声提醒敌人逼近：他手压黑石墙缝，脸转向门线和枪线，嘴部只做短句开口状态，语气压低、急促但不慌。

**光影**
战场口令中近景布光：重点是人物可读性和压迫，不做英雄逆光；冷白暴雪主光只给额骨、鼻梁和手背一点硬冷边，黑墙负补光吞掉半张脸和墙体，远处火线低位暖边更集中地切出侧脸、冻裂手和旧甲片，雪雾烟尘把枪线和门线分层。

**画面内容**
薛临墙占前景，冻裂粗手压住黑石女墙，骨钟在旁；他说短句时嘴部只轻开一次，呼吸在风雪里压住，眼线从骨钟转向门线，旧甲片和粗麻墙巾被风雪轻轻扯动，表演压低、实际、非英雄摆拍。墙头守军、枪线、门闩和墙外战场在中后景保持可读，几名守军随他的视线转向门线，火线暖边只服务于命令瞬间的脸、手、眼线和战场方向。

**运镜**
以参考帧为首帧，做小幅锁定推进到手、嘴和眼线；镜头运动克制，不追随大动作，精确台词不进入画面文字。

**约束**
薛临墙不是华甲将军或武侠宗师；他是旧墙师，话短、低声、急促但不慌。骨钟、墙缝和枪线必须仍与前两镜同一空间。墙外远景兽族和伴生兽继承已接入的兽族攻城兵种母卡、伴生兽关系母卡和本集兽族状态卡，但权重低于薛临墙身份参考和 I2V 首帧。
旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要老宗师姿势、不要武侠强光、不要神圣英雄逆光、不要过曝脸光、不要华丽将军甲、不要台词文字入画、不要大幅口型夸张、不要角色变年轻、不要骨钟消失。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, real body weight, real speed, natural breathing, contact reaction.

**Goal**
Show Xue Linqiang giving a low warning that the enemy is coming up in the same wall-top space: his hand presses the blackstone seam, face turned toward gate line and spear line, mouth only in a short speaking state, tone low, urgent but controlled.

**Lighting**
Battlefield-command close-medium lighting: prioritize character readability and pressure, with no heroic backlight; cold blizzard key light gives only a hard cold edge on brow, nose bridge and hand back, black-wall negative fill swallows half the face and wall mass, low distant fireline more tightly cuts the side profile, cracked hand and old armor plates, and snow-smoke haze layers spear line and gate line.

**Visual Content**
Xue Linqiang fills the foreground, cracked broad hand pressing the blackstone parapet, bone bell beside him; as he speaks the short warning, his mouth opens only once, his breath stays low in the blizzard, his eye-line shifts from the bell toward the gate line, and old armor plates and coarse wall scarf tug lightly in the wind, with a low, practical, non-heroic performance. Wall defenders, spear line, gate bar and exterior battlefield remain readable in middle and background, with several defenders following his eye-line toward the gate, while the warm fire edge serves only the command moment's face, hand, eye-line and battlefield direction.

**Camera / Motion**
Use the reference image as first frame, with a small locked push toward hand, mouth and eye-line; camera motion stays restrained and does not follow large action, with no exact dialogue text in the image.

**Constraints**
Xue Linqiang is not an ornate general or wuxia master; he is an old wall master, speaking briefly, low, urgent but controlled. The bell, wall seam and spear line must remain in the same space as the previous two shots. Distant exterior beast troops and companion beasts inherit the loaded beast troop master, companion-beast master and episode beast-state references, with lower weight than the Xue Linqiang identity reference and the I2V first frame.
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid grandmaster pose, wuxia glow, divine heroic backlight, overexposed face light, ornate general armor, dialogue text in frame, exaggerated lip movement, younger identity drift, missing bone bell.
```
