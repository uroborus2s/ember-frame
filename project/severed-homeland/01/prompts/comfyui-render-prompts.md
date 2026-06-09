# 第01集 SC001 ComfyUI 完整提示词

## 使用说明

中文：本文件是可直接复制到 ComfyUI prompt 节点的分段组装版提示词。每个镜头复制一组 `positive_prompt` 和 `negative_prompt` 即可，不要再复制 JSON 字段名。中文和英文任选一套使用，不建议同一轮同时混用两套语言。

English: This file contains sectioned, copy-ready assembled prompts for ComfyUI prompt nodes. Copy one `positive_prompt` and one `negative_prompt` per shot; do not copy JSON field names. Use either the Chinese or English pair for a render pass, not both languages mixed together.

## ComfyUI 图片节点配置 / Image Node Binding

中文：ComfyUI 不会自动读取 prompt 里的文件名。下面这些图片必须通过 `Load Image` 或等价图片输入节点接入 workflow，再连接到 FLF2V/I2V、IPAdapter、Reference-only、Redux 或你实际使用的参考图分支。不要只把文件名写进 prompt。

English: ComfyUI cannot automatically read image file names written in a prompt. The following images must be loaded through `Load Image` or equivalent image-input nodes, then connected to FLF2V/I2V, IPAdapter, Reference-only, Redux, or the reference branch used by the actual workflow. Do not rely on file names in the prompt text.

| Asset                                | Path                                     | Required Node Role                              | Suggested Binding                                                                                       |
| ------------------------------------ | ---------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| SH001 first frame                    | `01/assets/reference-frames/r001e01.png` | `PLACEHOLDER_FIRST_FRAME_IMAGE_NODE`            | FLF2V primary first-frame input                                                                         |
| SH001 last frame                     | `01/assets/reference-frames/r002e01.png` | `PLACEHOLDER_LAST_FRAME_IMAGE_NODE`             | FLF2V primary last-frame input                                                                          |
| SH002 first frame                    | `01/assets/reference-frames/r003e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE`                    | I2V primary image input                                                                                 |
| SH003 first frame                    | `01/assets/reference-frames/r004e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE`                    | I2V primary image input                                                                                 |
| 兽族多兵种母卡 / Beast troop master  | `assets/characters/c020m.png`            | `PLACEHOLDER_BEAST_TROOP_MASTER_IMAGE_NODE`     | Beast reference/IPAdapter branch, SH001 weight about `0.50`, SH002/SH003 background weight about `0.35` |
| 伴生兽母卡 / Companion beast master  | `assets/characters/c021m.png`            | `PLACEHOLDER_COMPANION_BEAST_MASTER_IMAGE_NODE` | Beast reference/IPAdapter branch, SH001 weight about `0.40`, SH002/SH003 background weight about `0.30` |
| 本集兽族状态卡 / Episode beast state | `01/assets/characters/c020e01.png`       | `PLACEHOLDER_EPISODE_BEAST_STATE_IMAGE_NODE`    | Beast reference/IPAdapter branch, SH001 weight about `0.55`, SH002/SH003 background weight about `0.40` |

中文：SH001 的首尾帧权重最高；三张兽族参考图只负责锁外形、多兵种和伴生兽多样性，不替代首尾帧。SH002/SH003 里兽族只在墙外背景，因此兽族参考权重必须低于人物身份参考和 I2V 首帧。

English: For SH001, first/last frames are the highest-priority inputs; the three beast references only lock silhouette, troop variety and companion-beast diversity, and must not replace the first/last frames. In SH002/SH003 the beast army is background-only, so beast reference weights must stay lower than the human identity reference and I2V first frame.

## Texture Standard / 质感标准

中文：`01/assets/reference-frames/r001e01.png` 是当前批准的 4K 首帧质感标准。后续首尾帧、I2V 首帧和场景资产必须继承它的去粒子化真实材质：不使用黄色闪粉、数字颗粒、全局高频假锐化或同质灰色颗粒表面。

English: `01/assets/reference-frames/r001e01.png` is the approved 4K first-frame texture standard. Later first/last frames, I2V first frames and scene assets must inherit its de-particleized photoreal material language, with no yellow glitter, digital grain, global high-frequency fake sharpening or uniform grey grain surfaces.

## SC001-SH001 FLF2V 节点配置 / FLF2V Node Setup

中文：尾帧不是单独接到解码或视频节点的。`r002e01.png` 只接入 `Wan首尾帧视频` 的 `结束图像`，由该节点生成带首尾帧约束的 positive、negative 和 latent，再交给采样器。新版 R002 应是同一墙外方向的第一次撞门震钟尾帧，不是墙头转向尾帧。

English: The last frame is not connected directly to decode or video output nodes. `r002e01.png` goes into the `end_image` input of the Wan first-last-frame video node; that node then produces conditioned positive, negative and latent outputs for the sampler. The new R002 should be the same-exterior-direction first gate-impact bell-shock tail frame, not a wall-top turning endpoint.

| Node                    | Setting / Connection                                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| `Load Image` first      | `01/assets/reference-frames/r001e01.png` -> resize/crop 16:9 -> `Wan首尾帧视频 / 起始图像`            |
| `Load Image` last       | `01/assets/reference-frames/r002e01.png` -> same resize/crop -> `Wan首尾帧视频 / 结束图像`            |
| `Wan首尾帧视频` size    | production `1280 x 720`; preview `960 x 544`; do not use `640 x 640` for this shot                    |
| `Wan首尾帧视频` length  | target `84`; if the Wan build requires `4n+1`, use `85` at `24fps`, not `81` at `16fps`               |
| `Wan首尾帧视频` batch   | `1`                                                                                                   |
| `CLIP Text Encode`      | positive/negative prompt -> `Wan首尾帧视频` positive/negative inputs                                  |
| `Wan首尾帧视频` outputs | positive/negative/latent -> `K采样器（高级）` positive/negative/latent image                          |
| `ModelSamplingSD3`      | keep shift `8.0` if required by the workflow template; model output -> `K采样器（高级） / 模型`       |
| `K采样器（高级）`       | seed fixed for test, steps `20` preview or `28` final, cfg `4.0`, sampler `euler`, scheduler `simple` |
| `VAE解码`               | `K采样器` latent -> `VAE解码 / Latent`; same VAE -> `VAE解码 / vae`                                   |
| `创建视频`              | `VAE解码` image sequence -> images, fps `24`                                                          |
| `保存视频`              | filename prefix `01/renders/raw/sc001-sh001`, format/encoder `auto` for test or H.264/MP4 for final   |

中文：如果当前 `Wan首尾帧视频` 节点有 `clip 视觉起始图像` / `clip 视觉结束图像` 输入，就把同一张 resized 首帧/尾帧再走对应的 CLIP Vision Encode 分支后接进去；如果模板没有这两个输入，可以只接 `起始图像` / `结束图像`。采样器建议先只保留一个主采样器，输出接 `VAE解码`；双采样会提高尾帧漂移风险，除非后续专门做二段细化。

### 角色建模参考节点 / Character Reference Nodes

中文：角色建模参考不是接到 `VAE解码` 或 `创建视频`，而是接在采样前的 model/reference 分支。SH001 里人物只是墙头小剪影和枪线，不要让角色参考抢过首尾帧或把镜头拉到墙头近景。

| Reference                                    | Suggested Node Path                                                                                                | Weight / Schedule                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `01/assets/characters/c024ae01.png` 年轻军户 | `Load Image -> CLIP Vision Encode or IPAdapter image input -> Character IPAdapter/reference node -> K采样器 model` | `0.20-0.25`, start `0.60`, end `1.00`; only helps tiny wall-top defender continuity |
| `01/assets/characters/c004e01.png` 薛临墙    | Reserve for SH003; do not use in SH001 unless he is clearly present in the frame                                   | `0.15-0.20`, start `0.70`, end `1.00`                                               |

中文：如果同时有兽族参考和人物参考，建议模型链为：`Checkpoint/LoRA -> ModelSamplingSD3 shift 8.0 -> Character IPAdapter -> Beast IPAdapter -> K采样器 model`。人物参考权重要低于首尾帧，兽族参考也不能把镜头拉回兽群特写。

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
超写实电影质感低魔东方史诗，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，真实古代材质，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
在暴雪中建立锁喉关正面偏斜攻城压力：首帧从墙外攻城方向低机位正向偏斜看城门和黑石巨墙，兽潮、攻城车或破门猛犸压向城门；尾帧仍保持同一墙外方向，用第一次重撞城门、骨钟横摆和雪雾冲画面作为切入墙头身体代价的转场。

**光影**
画面不能全灰全黑。裂云低角度冷白带一点淡金的天光从左上或侧后方切出城墙、攻城车、巨兽轮廓和骨钟边缘；撞门瞬间的冷白雪雾是最亮区域，低位暗红火点只做边缘反打，黑石墙保留大面积负补光暗面，形成精美但残酷的高反差战争质感。

**画面内容**
首帧是墙外攻城方向的低机位正向偏斜构图，约七成正向读城门压力、三成斜向给纵深；同一面锁喉关黑石巨墙和城门压在画面中后景，前景是继承已接入兽族参考图的兽族肩背、旧铁盾、破旗、雪泥脚步、攻城车木梁、巨角或破门猛犸局部。尾帧仍是同一墙外方向：攻城车木梁或铁包巨角第一次重撞城门，门闩、旧木、雪尘、碎冰和黑石边缘被震开；墙头同一钟架和同一口骨钟在上方或侧上方横摆，守军只读成小剪影和枪线。城内侧、另一边城门、第二道城墙不展开。

**运镜**
使用首尾参考帧约束“墙外低机位前推 + 撞门震钟”。镜头从兽潮和攻城车后方低位缓慢前推，略微上仰读城门高度；中段只做轻微避让破旗、烟柱和巨兽肩背的真实运动，终点压到撞门瞬间。骨钟横摆、雪雾白亮冲画面和钟声裂响作为隐藏剪切点，下一镜切到同一口骨钟旁被震倒的年轻军户。不做 90 度转向，不越过墙脊，不进入城内。

**约束**
人族守军在墙头只作为小剪影和枪线，兽族攻城方只在同一面城墙外侧和城门前方；R001/R002 必须保持同一墙外方向、同一城门、同一钟架、同一口骨钟。兽族士兵和伴生兽必须继承已接入图片节点的三张兽族参考图，保持多兵种和多伴生兽形态。禁止把城墙读成两边都被攻击的横墙，禁止墙内侧兽潮、另一边城门、第二钟架、第二口钟、完整发光旧徽。旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。前景兽潮、中景城门、背景钟架必须分层清楚，雪雾不能糊成灰白罩，关键轮廓不能被视频涂抹或花屏吃掉。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要现代服饰、枪械、科幻 UI、塑料 CG、正面完全对称城门海报、左右完全对称军阵、航拍感、游戏飞镜、飞到墙后、90度转向、穿墙、越过城墙看向另一边、城墙两侧都被攻击、后城墙厚度变主景、城内侧兽潮、180度调头、远处第二道城墙、第二个钟架、第二只钟、城门方向跳变、兽族看镜头列队、纯骨钟特写、完整发光徽章、神圣金光、魔法光柱、过曝 bloom、全画面灰黑、无明确亮部中心、雪雾糊成灰白罩、粒子化噪点、黄色闪粉、数字颗粒、全局高频锐化、视频涂抹、花屏、压缩块、局部融化、关键轮廓糊掉、不可读兽群、镜头光斑滥用、漂浮慢动作、血腥奇观、画面中文字、随机字幕。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, tactile period materials, real body weight, real speed, natural breathing and contact reaction. Match the approved first-frame texture standard: de-particleized photoreal surfaces, no digital speckle, no yellow glitter, clear material separation and physically plausible cold-warm lighting.

**Goal**
Establish Suohou Gate siege pressure in blizzard with a front-biased exterior angle: the first frame looks from outside the wall at a low, slightly oblique angle toward the gate and blackstone wall as the beast tide, siege cart or gate-breaking mammoth presses forward; the last frame keeps the same exterior-side direction and uses the first heavy gate impact, swinging bone bell and snow blast as the transition into wall-top bodily cost.

**Lighting**
The image must not become uniformly grey or black. Low storm-break sky light, cold white with a faint pale-gold edge, cuts the wall, siege engine, beast silhouettes and bone-bell rim from upper-left or side-back; the cold-white snow blast at the gate impact is the brightest zone, low dark-red fire points provide only edge counterlight, and the blackstone wall keeps large negative-fill shadow masses for refined but brutal high-contrast war lighting.

**Visual Content**
The first frame is a low, front-biased exterior siege composition, about seventy percent frontal gate pressure and thirty percent oblique depth; the same Suohou Gate blackstone wall and gate dominate the middle and rear, while the foreground holds beast shoulders, old iron shields, torn banners, snow-mud footsteps, siege-cart beams, horns or partial gate-breaking mammoth forms inherited from the loaded beast references. The last frame keeps the same exterior-side direction: the siege-cart beam or iron-wrapped horn hits the gate for the first time, shaking gate bars, old timber, snow dust, ice splinters and blackstone edges; the same wall-top bell frame and same bone bell swing above or upper-side, with defenders only as small silhouettes and spear-line shapes. The inner side, opposite gate and second wall do not open up.

**Camera / Motion**
Use the first and last frames to constrain an exterior low push plus gate impact and bell shock. The camera starts low behind the beast tide and siege engine, slowly pushes forward and tilts slightly up to read the gate height; the middle only makes small physical adjustments around torn banners, smoke columns and beast shoulders, ending on the gate-impact moment. The swinging bell, bright snow-haze blast and cracked bell sound are the hidden cut point into the next shot beside the same bell and the young soldier knocked down by the shock. No 90-degree turn, no crossing the wall crown, no entering the interior side.

**Constraints**
Human defenders on the wall top are only small silhouettes and spear-line shapes, while beast attackers stay only outside the same wall and in front of the same gate; R001/R002 must preserve the same exterior direction, same gate, same bell frame and same bone bell. Beast soldiers and companion beasts must inherit the three loaded beast reference images and preserve varied troop and companion-beast types. Never read the wall as attacked from both sides; no beast attackers inside the wall, opposite gate, second bell frame, second bell, or complete glowing old emblem. Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred. Foreground beast tide, midground gate and background bell frame must stay clearly layered; snow haze must not become a grey veil, and key silhouettes must not be eaten by video smearing or glitches.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid modern clothing, firearms, sci-fi UI, plastic CGI, perfectly symmetrical frontal-gate poster frame, perfectly symmetrical ranks, aerial-game feeling, game-like flying camera, flying behind the wall, 90-degree turn, passing through the wall, crossing over the wall to the opposite side, both sides of the wall under attack, rear-wall thickness as the main subject, beast attackers inside the wall, 180-degree turn, distant second wall, second bell frame, second bell, gate direction jump, beast troops posing toward camera, pure bone-bell close-up, complete glowing emblem, divine golden light, magic light beam, overexposed bloom, uniformly grey-black image, no clear highlight center, snow haze as grey veil, particle-like digital speckle, yellow glitter, global high-frequency sharpening, video smearing, glitching, compression blocks, local melting, blurred key silhouettes, unreadable beast mass, excessive lens flare, floaty slow motion, gore spectacle, text in image, random subtitles.
```

## SC001-SH002

- Method: `I2V`
- First frame: `01/assets/reference-frames/r003e01.png`（旧“扶钟”构图已废弃，必须先重生为新版半倒墙边构图）
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc001-sh002.mp4`

### positive_prompt_zh

```text
**风格**
超写实电影质感低魔东方史诗大片，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，真实古代材质，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
把战场规模压到年轻灰墙军户的身体代价：撞门余震把他晃倒，他半倒在同一墙头黑石女墙边，肩背撞墙，武器从手中脱落滑进雪泥，旁边同一口骨钟仍在横摆。

**光影**
身体代价近景要有精美电影光影但不能暖化成英雄片。左上或侧后方裂云冷白带淡金天光给钟架、锁链、头盔、肩甲、脱手武器和雪粒清晰轮廓；撞门方向反射一团冷白雪雾亮部，低位暗红火光只勾手指、武器边缘、钟缘和冻血；黑石墙负补光压住暗面，让脸部半遮、身体姿态清楚，背景降对比退后。

**画面内容**
年轻灰墙军户被撞门震动晃到，半倒在黑石女墙根部或墙边雪泥里，肩背贴墙，身体重心失衡；一只手撑住墙边或雪泥，另一只手刚松开断矛、短枪或长矛残杆。脱手武器斜滑在前景雪泥里，旁边同一口骨钟和钟架正在横摆，锁链拉紧、木架抖雪。人物脸被头盔、围巾、阴影和风雪半遮，不做正脸表情；重点是身体被震倒、武器脱手、钟仍在响。背景保留同一女墙、同一钟架方向、远处守军、墙外火点、雪雾和斜下方攻城压力，但不展开大场面。

**运镜**
以重新生成后的 R003 为首帧，镜头只做轻微余震手持和小幅压近。钟摆继续横晃，锁链微颤，脱手武器在雪泥里轻滑半寸，雪从木架和肩甲上抖落；人物不站起、不英雄化、不再主动扶钟。

**约束**
骨钟仍在同一墙头警钟架，墙外战场方向不变；这条镜头承接 SH001 撞门震钟，不是新场景。墙外远景兽族和伴生兽继承已接入的兽族参考图，但权重低于年轻军户身份参考和 I2V 首帧。旧日月痕只能残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。脱手武器、撑地手、肩背贴墙姿态和横摆骨钟必须清楚；脸可以半遮但不能崩坏变形，风雪不能遮住身体重心。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要扶钟姿势、不要跪着摆拍、不要手掌贴钟圣物化、不要强光圣徽、不要英雄摆拍、不要神圣逆光、不要过曝 bloom、不要全画面灰黑、不要没有主光方向、不要雪雾糊成灰白罩、不要视频涂抹、不要花屏、不要压缩块、不要局部融化、不要糊脸、不要手指融化、不要甲片粘连、不要钟架变形、不要过度血腥、不要正脸变形特写、不要面部美化、不要儿童化脸型、不要现代甲胄、不要骨钟位置漂移、不要背景战场换方向、不要第二道墙、不要第二个钟架。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, tactile period materials, real body weight, real speed, natural breathing and contact reaction. Match the approved first-frame texture standard: de-particleized photoreal surfaces, no digital speckle, no yellow glitter, clear material separation and physically plausible cold-warm lighting.

**Goal**
Compress the battlefield scale into the young grey-wall soldier's bodily cost: the gate-impact shock knocks him off balance, he half-collapses beside the same wall-top blackstone parapet with shoulder and back against the wall, his weapon slips from his hand into the snow mud, and the same bone bell still swings beside him.

**Lighting**
The bodily-cost close shot needs refined cinematographic lighting without becoming a warm heroic plate. Storm-break cold-white sky light with a faint pale-gold edge from upper-left or side-back gives clean rims to bell frame, chains, helmet, shoulder armor, dropped weapon and snow grains; a cold-white snow-haze bounce from the gate-impact direction forms the key highlight, low dark-red fire only edges fingers, weapon, bell rim and frozen blood; blackstone negative fill presses the dark side so the face is half obscured while the body posture stays readable and the background drops in contrast.

**Visual Content**
The young grey-wall soldier no longer braces the bell. He is knocked off balance by the gate-impact shock, half-collapsed at the base of the blackstone parapet or in snow mud beside the wall, shoulder and back against stone, body weight visibly unstable; one hand braces against wall edge or snow mud, while the other has just released a broken spear, short spear or spear shaft. The dropped weapon slides diagonally through foreground snow mud, and the same bone bell and bell frame swing beside him with chain taut and wooden frame shedding snow. His face is half hidden by helmet, scarf, shadow and blizzard, not a readable front-face performance; the emphasis is the body knocked down, weapon slipping loose and bell still ringing. The background keeps the same parapet, same bell-frame direction, distant defenders, exterior fire points, snow haze and diagonal siege pressure below, without opening into a large battlefield tableau.

**Camera / Motion**
Use the regenerated R003 as first frame, allowing only slight aftershock handheld feel and a small push-in. The bell continues to swing sideways, chains tremble, the dropped weapon slides a fraction through snow mud, and snow shakes off the wooden frame and shoulder armor; the soldier does not stand up, does not become heroic, and does not actively brace the bell.

**Constraints**
The bone bell remains in the same wall-top bell frame and the exterior battlefield direction does not change; this shot continues the gate-impact bell shock from SH001 and is not a new location. Distant exterior beast troops and companion beasts inherit the loaded beast references, but their weight stays below the young soldier identity reference and the I2V first frame. Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred. Dropped weapon, bracing hand, shoulder-against-wall posture and swinging bone bell must stay clear; the face may be half obscured but cannot deform, and blizzard must not hide the body weight.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid bracing-the-bell pose, kneeling pose tableau, palm-on-bell sacred-object framing, bright sacred emblem, heroic posing, divine backlight, overexposed bloom, uniformly grey-black image, no key-light direction, snow haze as grey veil, particle-like digital speckle, yellow glitter, global high-frequency sharpening, video smearing, glitching, compression blocks, local melting, blurred face, melted fingers, fused armor plates, warped bell frame, excessive gore, deformed front-face close-up, beautified face, childlike face, modern armor, drifting bell position, background battlefield direction change, second wall, second bell frame.
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
旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。手、侧脸、嘴部短促开口、枪线和骨钟空间锚点必须可读；脸可在半暗中，但不能用风雪或暗部遮掩变形。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要老宗师姿势、不要武侠强光、不要神圣英雄逆光、不要过曝脸光、不要华丽将军甲、不要台词文字入画、不要大幅口型夸张、不要口型融化、不要脸部花屏、不要眼鼻漂移、不要手指糊成团、不要背景枪线糊成灰块、不要视频涂抹、不要压缩块、不要角色变年轻、不要骨钟消失。
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
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred. Hand, side profile, brief mouth opening, spear line and bone-bell spatial anchors must be readable; the face may stay in half-darkness but must not hide deformation behind snow or shadow.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid grandmaster pose, wuxia glow, divine heroic backlight, overexposed face light, ornate general armor, dialogue text in frame, exaggerated lip movement, melted mouth shape, face glitching, drifting eyes or nose, clumped fingers, background spear line blurred into grey blocks, video smearing, compression blocks, younger identity drift, missing bone bell.
```
