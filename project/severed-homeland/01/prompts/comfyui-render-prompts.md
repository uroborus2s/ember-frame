# 第01集 SC001-SC003 ComfyUI 完整提示词

## 使用说明

中文：本文件是可直接复制到 ComfyUI prompt 节点的分段组装版提示词，当前覆盖 SC001、SC002 与 SC003。每个镜头复制一组 `positive_prompt` 和 `negative_prompt` 即可，不要再复制 JSON 字段名。中文和英文任选一套使用，不建议同一轮同时混用两套语言。

English: This file contains sectioned, copy-ready assembled prompts for ComfyUI prompt nodes, currently covering SC001, SC002 and SC003. Copy one `positive_prompt` and one `negative_prompt` per shot; do not copy JSON field names. Use either the Chinese or English pair for a render pass, not both languages mixed together.

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

中文：尾帧不是单独接到解码或视频节点的。`r002e01.png` 只接入 `Wan首尾帧视频` 的 `结束图像`，由该节点生成带首尾帧约束的 positive、negative 和 latent，再交给采样器。新版 R002 应是同一墙外方向、更近城门、更强第一次撞门并触发门楼内钟声的尾帧，不是墙头转向尾帧，也不要求画面露出骨钟。

English: The last frame is not connected directly to decode or video output nodes. `r002e01.png` goes into the `end_image` input of the Wan first-last-frame video node; that node then produces conditioned positive, negative and latent outputs for the sampler. The new R002 should be the same-exterior-direction, closer-gate, stronger first-impact tail frame that triggers gatehouse bell sound, not a wall-top turning endpoint, and it does not require an on-screen bone bell.

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
在暴雪中建立锁喉关正中对称史诗攻城压力：首帧从墙外攻城方向低机位看城门和黑石巨墙，兽潮、攻城车或破门猛犸压向城门；尾帧仍保持同一墙外方向和当前 R001/R002 的正中史诗构图，更近靠近城门，用第一次重撞城门、浓烈雪雾、碎冰和旧木屑冲画面作为切入墙头空间的转场。骨钟不要求出现在画面中，钟声从门楼内部传出。

**光影**
画面不能全灰全黑。裂云低角度冷白带一点淡金的天光从左上或侧后方切出城墙、攻城车和巨兽轮廓；撞门瞬间的冷白雪雾、碎冰、旧木屑和门闩震动是最强动作亮部，低位暗红火点只做边缘反打，黑石墙保留大面积负补光暗面，形成精美但残酷的高反差战争质感。

**画面内容**
首帧是墙外攻城方向的低机位正中对称史诗构图，允许轻微透视纵深；同一面锁喉关黑石巨墙和城门压在画面中后景，前景是继承已接入兽族参考图的兽族肩背、旧铁盾、破旗、雪泥脚步、攻城车木梁、巨角或破门猛犸局部。尾帧仍是同一墙外方向：镜头比当前 R002 更近靠近城门，攻城车木梁或铁包巨角第一次重撞城门，门闩、旧木、雪尘、碎冰、木屑和黑石边缘被更浓烈地震开；骨钟在门楼内部，画面不强制出现钟架或钟体，守军只读成小剪影和枪线。城内侧、另一边城门、第二道城墙不展开。

**运镜**
使用首尾参考帧约束“墙外低机位正中前推 + 更强撞门冲击”。镜头从兽潮和攻城车后方低位缓慢前推，略微上仰读城门高度；终点压到城门更近处，撞击瞬间让雪雾白亮、碎冰、旧木屑和门闩震动冲出画面。门楼内骨钟声和撞门低频作为隐藏剪切点，下一镜可进入墙头空间。不做 90 度转向，不越过墙脊，不进入城内。

**约束**
人族守军在墙头只作为小剪影和枪线，兽族攻城方只在同一面城墙外侧和城门前方；R001/R002 必须保持同一墙外方向、同一城门、当前正中史诗攻城构图和真实质感。骨钟/钟架不要求在第一镜画面中出现，钟声来自门楼内部。兽族士兵和伴生兽必须继承已接入图片节点的三张兽族参考图，保持多兵种和多伴生兽形态。禁止把城墙读成两边都被攻击的横墙，禁止墙内侧兽潮、另一边城门、第二城门、第二道墙、完整发光旧徽。前景兽潮、中景城门、背景黑石墙和旗帜必须分层清楚，雪雾不能糊成灰白罩，关键轮廓不能被视频涂抹或花屏吃掉。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要现代服饰、枪械、科幻 UI、塑料 CG、航拍感、游戏飞镜、飞到墙后、90度转向、穿墙、越过城墙看向另一边、城墙两侧都被攻击、后城墙厚度变主景、城内侧兽潮、180度调头、远处第二道城墙、第二个城门、城门方向跳变、兽族看镜头列队、强行把可见骨钟或钟架做成画面主体、纯骨钟特写、完整发光徽章、神圣金光、魔法光柱、过曝 bloom、全画面灰黑、无明确撞击亮部中心、雪雾糊成灰白罩、撞击点不在城门、撞击点不亮、碎冰木屑不可见、粒子化噪点、黄色闪粉、数字颗粒、全局高频锐化、视频涂抹、花屏、压缩块、局部融化、关键轮廓糊掉、不可读兽群、镜头光斑滥用、漂浮慢动作、血腥奇观、画面中文字、随机字幕。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, tactile period materials, real body weight, real speed, natural breathing and contact reaction. Match the approved first-frame texture standard: de-particleized photoreal surfaces, no digital speckle, no yellow glitter, clear material separation and physically plausible cold-warm lighting.

**Goal**
Establish Suohou Gate siege pressure in blizzard with the current centered exterior epic composition: the first frame looks from outside the wall at a low frontal angle toward the gate and blackstone wall as the beast tide, siege cart or gate-breaking mammoth presses forward; the last frame keeps the same exterior-side direction, moves closer to the gate, and uses the first heavy gate impact, dense snow blast, ice and timber debris as the transition. The bone bell does not need to appear on screen; its sound comes from inside the gatehouse.

**Lighting**
The image must not become uniformly grey or black. Low storm-break sky light, cold white with a faint pale-gold edge, cuts the wall, siege engine and beast silhouettes from upper-left or side-back; in the tail frame the cold-white snow blast, ice splinters, timber chips and shaking gate bars at impact should become the strongest action highlight, low dark-red fire points provide only edge counterlight, and the blackstone wall keeps large negative-fill shadow masses for refined but brutal high-contrast war lighting.

**Visual Content**
Both first and last frames keep the low centered exterior epic siege composition, with only slight perspective depth. The same Suohou Gate blackstone wall and gate dominate the middle and rear, while the foreground holds beast shoulders, old iron shields, torn banners, snow-mud footsteps, siege-cart beams, horns or partial gate-breaking mammoth forms inherited from the loaded beast references. The last frame moves closer to the gate: the siege-cart beam or iron-wrapped horn hits the gate for the first time, violently shaking gate bars, old timber, snow dust, ice splinters, timber chips and blackstone edges. The bone bell is inside the gatehouse and exists through sound only; no visible bell frame or bell body is required. The inner side, opposite gate and second wall do not open up.

**Camera / Motion**
Use the first and last frames to constrain a low centered exterior push plus stronger gate impact. The camera starts low behind the beast tide and siege engine, slowly pushes forward and tilts slightly up to read the gate height; it ends closer to the gate as bright snow haze, ice splinters, old timber chips and shaking gate bars burst from the impact. The offscreen gatehouse bell sound and low gate impact are the hidden cut point into the following wall-top space. No 90-degree turn, no crossing the wall crown, no entering the interior side.

**Constraints**
Human defenders on the wall top are only small silhouettes and spear-line shapes, while beast attackers stay only outside the same wall and in front of the same gate. R001/R002 must preserve the same exterior direction, same gate, centered epic siege composition and tactile realism. The bell frame or bell body does not need to appear in SH001; the bell sound comes from inside the gatehouse. Beast soldiers and companion beasts must inherit the three loaded beast reference images and preserve varied troop and companion-beast types. Never read the wall as attacked from both sides; no beast attackers inside the wall, opposite gate, second gate, second wall or complete glowing old emblem. Foreground beast tide, midground gate and background wall/flags must stay clearly layered; snow haze must not become a grey veil, and key silhouettes must not be eaten by video smearing or glitches.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid modern clothing, firearms, sci-fi UI, plastic CGI, aerial-game feeling, game-like flying camera, flying behind the wall, 90-degree turn, passing through the wall, crossing over the wall to the opposite side, both sides of the wall under attack, rear-wall thickness as the main subject, beast attackers inside the wall, 180-degree turn, distant second wall, second gate, gate direction jump, beast troops posing toward camera, forcing a visible bell or bell frame to become the main subject, pure bone-bell close-up, complete glowing emblem, divine golden light, magic light beam, overexposed bloom, uniformly grey-black image, no clear gate-impact highlight center, snow haze as grey veil, impact away from the gate, dim impact point, missing ice/timber debris, particle-like digital speckle, yellow glitter, global high-frequency sharpening, video smearing, glitching, compression blocks, local melting, blurred key silhouettes, unreadable beast mass, excessive lens flare, floaty slow motion, gore spectacle, text in image, random subtitles.
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

## SC002 ComfyUI Handoff / SC002 可复制提示词

中文：SC002 的 R005-R009 当前候选已被用户视觉 QC 退回，原因是角色一致性与身高差仍未满足。以下 SC002 提示词只保留为历史草稿，不得直接复制到 ComfyUI；必须先按 `C025 -> C017 -> C016 -> C018 -> C019` 同地平线比例链重生角色状态卡，再按 `4096x2304` 重生 R005-R009，之后才能重新进入 I2V/FLF2V 绑定。

English: SC002 current R005-R009 candidates have failed user visual QC because character identity and height hierarchy still do not hold. The SC002 prompts below are retained as historical drafts only and must not be copied directly into ComfyUI; rebuild the episode character cards against the `C025 -> C017 -> C016 -> C018 -> C019` same-ground scale ladder, then regenerate R005-R009 at `4096x2304` before any I2V/FLF2V binding.

| Asset | Path | Required Node Role | Suggested Binding |
| --- | --- | --- | --- |
| SH001 first frame | `01/assets/reference-frames/r005e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | I2V primary image input |
| SH002 first frame | `01/assets/reference-frames/r006e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | I2V primary image input |
| SH003 first frame | `01/assets/reference-frames/r007e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | I2V primary image input |
| SH004 first frame | `01/assets/reference-frames/r008e01.png` | `PLACEHOLDER_FIRST_FRAME_IMAGE_NODE` | FLF2V primary first-frame input |
| SH004 last frame | `01/assets/reference-frames/r009e01.png` | `PLACEHOLDER_LAST_FRAME_IMAGE_NODE` | FLF2V primary last-frame input |
| 粮税小吏 / Grain tax clerk | `01/assets/characters/c016be01.png` | `PLACEHOLDER_CHARACTER_REFERENCE_NODE` | identity/material reference, lower than I2V frame |
| 混血奴兵 / Slave soldier | `01/assets/characters/c017e01.png` | `PLACEHOLDER_CHARACTER_REFERENCE_NODE` | identity/material reference, lower than I2V or FLF2V frames |
| 纯虫族小兵 / Pure insect infantry | `01/assets/characters/c018e01.png` | `PLACEHOLDER_CHARACTER_REFERENCE_NODE` | armed perimeter and height-scale reference; never substitute for clerk or slave soldier |
| 金河粮仓 / Jinhe depot | `01/assets/locations/l003e01.png` | `PLACEHOLDER_LOCATION_REFERENCE_NODE` | geography/material reference |
| 白册 / White register | `01/assets/props/p003e01.png` | `PLACEHOLDER_PROP_REFERENCE_NODE` | line-control/material reference; no readable generated text |
| 粮牌封蜡祖牌 / Grain tag, wax, tablet box | `01/assets/props/p008e01.png` | `PLACEHOLDER_PROP_REFERENCE_NODE` | wax/tag/tablet/jar/cart-rope material reference |

## SC002-SH001

- Method: `I2V`
- Duration: `6s`
- First frame: `01/assets/reference-frames/r005e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc002-sh001.mp4`
- Status: `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11; blocked_do_not_render_until_4096x2304_regeneration`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。金河粮仓清晨冷雾，麦金、河泥褐、湿木灰和虫蜡白分材质呈现，真实重心、真实速度、自然接触反作用。

**目标**
从锁喉关战争压力切到金河征粮制度：用粮袋墙、虫族官吏真实身高差、低位村民和白册夹板建立“粮食已被制度占领”的空间秩序。

**光影**
柔和清晨冷雾作主环境光，低角度逆光穿过粮尘切出粮袋墙、小吏高帽和白册轮廓，窄侧光擦过麻布、湿木和河泥纹理；虫蜡白只作为白册和粮牌的小亮点。少量丁达尔光用于粮尘纵深，不能做成特效光柱。

**画面内容**
清晨麦金冷雾里，金河粮袋堆成墙，虫族粮税小吏站在同一条车道泥地上，继承 C016 骨白面壳、暗色复眼、细触须和白蜡高账吏帽，胸前白册夹板、骨算盘、粮牌和旧铁秤钩随动作轻晃；混血奴兵只在低位押粮或牵绳；纯虫族小兵体型高于奴兵和村民，持短矛或钩镰在车道边封路警戒，形成紧张冲突氛围。

**构图与运镜**
横屏远景按同一泥地上的真实身高差构图：粮袋墙占上半画面并压低天空，粮税小吏站在车道泥地偏中位置，凭 190-210cm 虫族身高压过村民，白册夹板、骨算盘和粮牌形成亮色制度中心；纯虫族小兵 200-230cm 持械封住车道边缘，村民被压成下方窄带，押车通道从右前向左后退进，保留粮仓纵深。从村民眼高真实速度缓慢推进，推进时粮尘和人群只轻微让开，终点停在粮税小吏与白册夹板的层级关系上，不升空、不追美景。

**约束**
粮税小吏必须是虫族低阶官僚，不是人族账房或普通衙役；纯虫族小兵只负责持械封路，不开册、不扣腕、不搬粮；混血奴兵只负责低位押粮/搬运。白册只显示留白、浅刻线或后合成区域，不生成可读文字。粮仓不能变成现代仓库或灰色灾民营，麦金、河泥褐、湿木灰和虫蜡白要分材质。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代仓库，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，画面中文字，随机字幕，随机徽记，随机可读白册文字，错误阵营服制，灰色灾民营，魔法光柱，圣光逆光，大面积恐怖底光，过曝 bloom，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块。

**镜头负面**
不要现代仓库、现代服饰、枪械、科幻 UI、人族账房先生版小吏、欢乐蒸汽朋克、全画面灰色灾民营、无主光方向、过度丁达尔光柱、魔法光柱、过曝 bloom、随机可读白册文字、随机徽记、纯虫族缺少兵器、纯虫族替官吏开册、奴兵变成纯虫族爪手、黄色闪粉、数字颗粒、全局假锐化、塑料麻袋、远景群众逐个清晰、视频涂抹、花屏、压缩块。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Jinhe grain depot in morning cold haze, material separation between wheat gold, river-mud brown, wet wood grey and insect-wax white, real body weight, real speed and natural contact reaction.

**Goal**
Cut from border war pressure into the Jinhe grain-tax system: use the grain-sack wall, true insect-official height scale, low villagers and white register board to establish that grain has already been occupied by bureaucracy.

**Lighting**
Soft morning cold haze acts as the ambient key. Low-angle backlight passes through grain dust to rim the sack wall, clerk hat and register board, while a narrow side light grazes burlap, wet wood and river-mud texture; insect-wax white stays as small highlights on the register and grain tags. Subtle Tyndall light may deepen grain-dust space, never becoming VFX beams.

**Visual Content**
In wheat-gold cold morning haze, Jinhe grain sacks form a wall. The insect grain tax clerk stands on the same muddy cart lane and keeps the C016 bone-white face shell, dark compound eyes, thin feelers and wax-white tall accountant hat; the white register board, bone abacus, grain tags and old iron scale hook sway lightly on his chest. Mixed slave soldiers stay low as rope or grain enforcers. Pure insect infantry, taller than slave soldiers and villagers, hold short spears or hook-sickles at the lane edges as an armed route-blocking perimeter, creating tension.

**Composition and Camera**
Landscape wide composition built on true same-ground height hierarchy: the grain-sack wall occupies the upper half and suppresses the sky, the grain tax clerk stands near center on the same muddy cart lane and towers over villagers through his 190-210 cm insect-official body, while the white register board, bone abacus and grain tags form the bright bureaucratic center; 200-230 cm pure insect infantry hold weapons at the lane edges, villagers are compressed into a low band, and the cart lane recedes from front-right to rear-left for depot depth. A slow real-time push from villager eye height; grain dust and crowd layers only part slightly as the camera moves, ending on the hierarchy between clerk and white register board, with no crane move or beauty-plate drift.

**Constraints**
The grain tax clerk must remain an insect low-ranking bureaucrat, not a human accountant or ordinary magistrate; pure insect infantry only hold weapons and block routes, never opening the register, gripping wrists or moving sacks; mixed slave soldiers only enforce at low status. The white register only shows blank areas, shallow guide lines or post-composite spaces, no readable text. The depot must not become a modern warehouse or grey refugee camp; wheat gold, river-mud brown, wet wood grey and insect-wax white stay materially separated.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern warehouse, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, text in image, random subtitles, random emblems, random readable register text, wrong faction wardrobe, grey refugee camp, magic light shafts, sacred backlight, broad horror bottom light, overexposed bloom, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks.

**Shot Negative**
avoid modern warehouse, modern clothing, firearms, sci-fi UI, human-accountant clerk, cheerful steampunk, all-grey refugee camp, missing key-light direction, excessive Tyndall beams, magic light shafts, overexposed bloom, random readable register text, random emblems, pure insect guards without weapons, pure insect guards doing clerk duties, slave soldiers turning into clawed pure insects, yellow glitter, digital speckle, global fake sharpening, plastic sacks, individually sharp distant crowd, video smearing, glitches, compression blocks.
```

## SC002-SH002

- Method: `I2V`
- Duration: `7s`
- First frame: `01/assets/reference-frames/r006e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc002-sh002.mp4`
- Status: `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11; blocked_do_not_render_until_4096x2304_regeneration`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。金河粮仓清晨冷雾，麦金、河泥褐、湿木灰和虫蜡白分材质呈现，真实重心、真实速度、自然接触反作用。

**目标**
把征粮制度压到家庭门槛：半斗杂粮、祖牌小盒、孩子虫蜡手印和奴兵扣腕同框，让“家门被写没”变成可见动作。

**光影**
门外清晨柔光托住人物安全感，窄侧光从门槛斜切，强化湿泥、木缸、粗布、祖牌盒和奴兵腕绑纹理；虫蜡封条上有小面积冷白顶光，制造制度压迫，但避开孩子眼窝。底光只允许作为泥水反光的极弱火场感，不大面积使用。

**画面内容**
混血奴兵的骨白腕绑和五指硬化人手从侧面压入画面，明确扣住成年村民前臂或袖口，不抓脚踝、不抓小腿；祖牌小盒压在门槛边，冷白虫蜡上留着孩子五指手印。衣物是金河农户旧粗布和劳动补丁，表演克制、沉重、不血腥。背景外道上有一名纯虫族小兵持短矛或钩镰站成模糊封路剪影，体型明显高于奴兵和村民。

**构图与运镜**
门槛压迫特写组用斜线构图：前景是散落杂粮、湿泥、祖牌小盒和虫蜡孩子手印，画面一侧切入奴兵骨白腕绑和扣住前臂/袖口的五指手；老人和孩子只给局部姿态，不做猎奇正脸。背景保留粮袋墙、低位人群和纯虫族持械封路剪影的模糊压力。手持后退一步，只跟随前臂被扣住、祖牌盒被压低和孩子手印留在虫蜡上的真实接触反作用；运动短、低、近，动作完成后立刻稳住。

**约束**
奴兵只负责扣腕、押车、执行，不开册；扣腕对象必须读成成人前臂或袖口，不能读成脚踝、小腿或裸足。纯虫族小兵只在背景持械封路，不执行扣腕。祖牌小盒、粮牌封蜡和粮缸属于家庭/制度道具线。儿童威胁必须克制，不能出现直观伤害、血腥或猎奇表情。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代仓库，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，画面中文字，随机字幕，随机徽记，随机可读白册文字，错误阵营服制，灰色灾民营，魔法光柱，圣光逆光，大面积恐怖底光，过曝 bloom，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块。

**镜头负面**
不要直观伤害儿童、不要血腥、不要恐怖片底光大面积照脸、不要奴兵变纯怪物、不要奴兵开白册、不要抓脚踝、不要抓小腿、不要把被抓对象画成裸足、不要纯虫族爪子执行扣腕、不要祖牌盒变成华丽祭器、不要现代陶瓷或塑料桶、不要随机文字、不要猎奇正脸、不要夸张哭喊、不要全画面硬闪光、不要黄色闪粉、数字颗粒、视频涂抹、手指融化、道具粘连。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Jinhe grain depot in morning cold haze, material separation between wheat gold, river-mud brown, wet wood grey and insect-wax white, real body weight, real speed and natural contact reaction.

**Goal**
Push the grain-tax system onto the household threshold: half-measure grain, ancestral tablet box, child wax handprint and slave-soldier grip share the frame so the erasure of the household becomes a visible action.

**Lighting**
Soft morning light from outside preserves restraint around the people, while a narrow side light cuts across the threshold to strengthen wet mud, wooden jar, coarse cloth, tablet box and slave-soldier wrist-binding textures. A small cold-white top light sits on the insect-wax seal to create bureaucratic oppression without darkening the child eye sockets. Bottom light is only a faint mud-water reflection, never broad.

**Visual Content**
A mixed-blood slave soldier hand with bone-white wrist binding and five hardened human fingers presses into frame from the side, clearly gripping an adult villager forearm or sleeve cuff, not an ankle, leg or bare foot. The ancestral tablet box sits low by the threshold, and a cold-white wax surface carries a child's five-finger palm print. Clothes are Jinhe coarse work cloth with repairs; performance is restrained, heavy and non-gory. In the exterior lane background, a taller pure insect infantry guard holds a short spear or hook-sickle as a blurred route-blocking silhouette.

**Composition and Camera**
The coercive threshold close-up uses diagonal pressure: foreground holds spilled grain, wet mud, ancestral tablet box and child wax palm print; one side of frame cuts in the slave soldier bone-white wrist binding and a five-finger hand gripping an adult forearm or sleeve cuff. Elder and child are shown as partial body language, not exploitative front faces. Background keeps blurred pressure from grain sacks, low crowd and a pure insect armed guard blocking the lane. A one-step handheld pullback follows the real contact reaction of the forearm being restrained, the tablet box held low and the wax handprint left behind; the move is short, low and close, settling as soon as the action lands.

**Constraints**
The slave soldier only grips, carts and enforces, never opens the register; the grip target must read as an adult forearm or sleeve cuff, not an ankle, leg or bare foot. Pure insect infantry only blocks the background lane with a weapon and never performs the grip. The ancestral tablet box, grain-tag wax and jar belong to the household/system prop line. Child threat must stay restrained, with no explicit harm, gore or exploitative expression.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern warehouse, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, text in image, random subtitles, random emblems, random readable register text, wrong faction wardrobe, grey refugee camp, magic light shafts, sacred backlight, broad horror bottom light, overexposed bloom, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks.

**Shot Negative**
avoid explicit child harm, gore, broad horror bottom-light on faces, pure-monster slave soldier, slave soldier opening the register, grabbing an ankle, grabbing a leg, bare foot as grip target, pure insect claw performing the grip, ornate shrine-like tablet box, modern ceramic or plastic bucket, random text, exploitative front faces, exaggerated crying, full-frame hard flash, yellow glitter, digital speckle, video smearing, melted fingers, fused props.
```

## SC002-SH003

- Method: `I2V`
- Duration: `7s`
- First frame: `01/assets/reference-frames/r007e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc002-sh003.mp4`
- Status: `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11; blocked_do_not_render_until_4096x2304_regeneration`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。金河粮仓清晨冷雾，麦金、河泥褐、湿木灰和虫蜡白分材质呈现，真实重心、真实速度、自然接触反作用。

**目标**
让“查清明籍”的话术变成可见制度动作：白册、族谱行留白、节状手指、封牌和被扣妇人一起说明家粮被写成官粮。

**光影**
虫蜡白顶光压在白册和小吏脸壳上，形成冷酷制度感，并故意让小吏眼窝更暗；但用窄侧光擦亮节状手指、妇人手腕、旧木桌纹、粮袋麻布和奴兵皮甲，保证皮肤/甲片/石木纹理可读。小槌落点可用小面积硬光，逆光只给高帽、肩线和冷雾轮廓，避免圣光化。

**画面内容**
粮税小吏继承 C016 骨白面壳和暗色复眼，翻开白册，节状手指点过族谱行留白，封牌小槌落在粮袋旁；妇人护住过冬粮被混血奴兵从侧后扣住手腕或前臂。小吏高位冷静，奴兵低位执行，纯虫族小兵在背景车道边持短矛或钩镰封路警戒，体型明显高于奴兵和村民。册页只允许留白、浅刻线、遮罩或后合成区域，不能生成随机可读字。

**构图与运镜**
检查桌中景按“前景证据、中景执行、背景压力”三层构图：前景高细节是白册册页、节状手指、粮牌、虫蜡封条、骨算盘和湿木桌沿；中景是粮税小吏高帽、被扣妇人、奴兵扣腕和粮袋侧面；背景保留粮袋墙、检查口、低位村民、清晨冷雾和纯虫族持械封路线。静态制度镜头，正面略高于桌沿，只有手、封牌小槌、妇人护粮和奴兵扣腕移动；纯虫族只守路不动手，台词只表现说话状态，不让模型生成字幕或口型精确文字。

**约束**
官吏、奴兵、纯虫族小兵、金河家庭四种身份层级必须分明：官吏开册，奴兵扣腕，纯虫族持械封路，家庭护粮低位受压。白册、粮牌、虫蜡封条和骨算盘是制度道具，不是魔法特效。视频只表现说话状态，精确对白来自字幕和配音。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代仓库，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，画面中文字，随机字幕，随机徽记，随机可读白册文字，错误阵营服制，灰色灾民营，魔法光柱，圣光逆光，大面积恐怖底光，过曝 bloom，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块。

**镜头负面**
不要混淆官吏、奴兵和纯虫族职责、不要人族账房版小吏、不要白册随机可读文字、不要字幕入画、不要封牌变魔法符、不要奴兵抢主位、不要纯虫族开册或扣腕、不要纯虫族缺少兵器、不要妇人变华丽贵族、不要全画面顶光黑眼窝导致脸不可读、不要圣光逆光、不要大面积底光、不要过硬假舞台光、不要黄色闪粉、数字颗粒、塑料皮肤、手指融化、脸部花屏、道具比例漂移。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Jinhe grain depot in morning cold haze, material separation between wheat gold, river-mud brown, wet wood grey and insect-wax white, real body weight, real speed and natural contact reaction.

**Goal**
Turn the Qingming-register speech into a visible bureaucratic action: the register, blank genealogy rows, segmented finger, seal tag and pinned woman show household grain being rewritten as state grain.

**Lighting**
Cold insect-wax top light presses onto the register and clerk face shell, creating a cruel bureaucratic feeling and deliberately darkening the clerk eye sockets; a narrow side light still grazes segmented fingers, the woman wrist, old table grain, burlap sack and slave-soldier leather armor so skin, armor and wood textures remain readable. The seal-hammer landing point may take a small hard highlight; backlight only rims hat, shoulders and cold haze, never becoming sacred.

**Visual Content**
The grain tax clerk keeps the C016 bone-white face shell and dark compound eyes, opens the white register, segmented finger crossing blank genealogy rows, and a seal-tag hammer lands beside the grain sack. A woman guarding winter grain is gripped at wrist or forearm from side-rear by a mixed slave soldier. Pure insect infantry guards stand in the background lane with short spears or hook-sickles, visibly taller than slave soldiers and villagers. The clerk stays high and calm, the slave soldier executes below, and woman and villagers are compressed low. Register pages only allow blank space, shallow guide lines, masks or post-composite areas, never random readable text.

**Composition and Camera**
The medium inspection-table shot uses three layers: foreground evidence, midground enforcement, background pressure. Foreground high detail holds register pages, segmented fingers, grain tag, insect-wax seal, bone abacus and wet-wood table edge; midground holds the clerk tall hat, pinned woman, slave-soldier grip and grain sack side; background keeps grain-sack wall, inspection opening, low villagers, morning cold haze and pure insect armed perimeter guards. A locked bureaucratic frame, frontal and slightly above table edge; only hands, seal-hammer, the woman guarding grain and slave-soldier grip move. Pure insect guards only hold the route line. Dialogue is only a speaking state, with no generated subtitles or exact lip text.

**Constraints**
Clerk, slave soldier, pure insect infantry and Jinhe household identities must remain distinct: clerk records, slave soldier grips, pure insect infantry block routes with weapons, household protects grain from a low position. The white register, grain tag, insect-wax seal and bone abacus are bureaucratic props, not magic effects. Video only shows speaking state; exact dialogue belongs to subtitles and voice.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern warehouse, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, text in image, random subtitles, random emblems, random readable register text, wrong faction wardrobe, grey refugee camp, magic light shafts, sacred backlight, broad horror bottom light, overexposed bloom, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks.

**Shot Negative**
avoid mixing clerk, slave-soldier and pure-insect duties, human-accountant clerk, random readable register text, subtitles in frame, magic-symbol seal tag, slave soldier taking the main official position, pure insect opening register or gripping wrist, pure insect guards without weapons, woman turning into an ornate noble, full-frame top light making faces unreadable, sacred backlight, broad bottom light, fake hard stage lighting, yellow glitter, digital speckle, plastic skin, melted fingers, face glitches, drifting prop scale.
```

## SC002-SH004

- Method: `FLF2V`
- Duration: `8s`
- First frame: `01/assets/reference-frames/r008e01.png`
- Last frame: `01/assets/reference-frames/r009e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Output: `01/renders/raw/sc002-sh004.mp4`
- Status: `failed_user_visual_qc_identity_height_scale_relock_required_2026-06-11; blocked_do_not_render_until_4096x2304_regeneration`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕。金河粮仓清晨冷雾，麦金、河泥褐、湿木灰和虫蜡白分材质呈现，真实重心、真实速度、自然接触反作用。

**目标**
用押车离开完成征粮制度结果：粮袋被拖走，祖牌小盒和虫蜡手印留在泥里，旁白落下“良户成逃籍”。

**光影**
清晨低角逆光从押车离开的方向打出粮袋、车轮、奴兵肩线和冷雾轮廓，增加电影感和空气感；侧光掠过泥水、车辙、祖牌盒和麻袋，强化触感。妇人和孩子只吃柔和天光，不用硬光审判；虫蜡手印保持小面积冷白亮点。丁达尔光只沿车道给纵深，不能盖住家门。

**画面内容**
混血押车奴兵用五指硬化人手和绳索把粮袋搬上木车，车轮从祖牌小盒旁压过泥水；纯虫族小兵持短矛或钩镰分列车道两侧封路警戒，体型高于奴兵和村民，不搬粮、不扣腕。妇人跪在门槛边，孩子手印仍粘着虫蜡白。首帧读到粮袋刚被搬上车，终帧读到粮车离开后的空门槛、车辙和冷雾，情绪克制，不做英雄追车或夸张哭喊。

**构图与运镜**
FLF2V 首帧到终帧使用同一门槛后方三分构图：首帧前景是祖牌小盒、虫蜡冷白手印和泥水，粮袋正被混血奴兵搬上车；中景妇人与孩子低在门槛，奴兵和车轮横向离开，纯虫族持械守住车道两侧；终帧车已退到远处冷雾里，前景仍是空门槛、祖牌盒和车辙，远处纯虫族守卫退成压迫剪影，家门还在但家粮不在。粮车和奴兵横向离开，镜头不追车，固定在家门后方并极慢后收，强调“粮走了，家留空”；尾段让车轮声盖过哭声。

**约束**
首尾帧必须保持同一门槛、同一祖牌小盒、同一押车方向、同一纯虫族持械封路线和同一清晨冷雾；粮车可以离开画面纵深，但镜头不能追成动作片。纯虫族不搬粮、不扣腕，只维持封路压力。家门留空是结尾信息。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代仓库，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，画面中文字，随机字幕，随机徽记，随机可读白册文字，错误阵营服制，灰色灾民营，魔法光柱，圣光逆光，大面积恐怖底光，过曝 bloom，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块。

**镜头负面**
不要追车英雄镜头、不要押车变战车、不要现代车轮、不要夸张哭喊、不要大面积底光火场感、不要圣光式逆光、不要车离开后换地理、不要祖牌盒消失、不要孩子手印变血手印、不要纯虫族搬粮、不要纯虫族缺少兵器、不要奴兵变纯虫族爪手、不要粮袋漂浮、不要泥水塑料感、不要黄色闪粉、数字颗粒、过度丁达尔光、视频涂抹、花屏、压缩块、人物融化。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Jinhe grain depot in morning cold haze, material separation between wheat gold, river-mud brown, wet wood grey and insect-wax white, real body weight, real speed and natural contact reaction.

**Goal**
Complete the result of the grain-tax system through the cart leaving: sacks are dragged away, ancestral tablet box and wax handprint remain in mud, and voiceover lands that a lawful household becomes fugitive registry.

**Lighting**
Low morning backlight from the cart-exit direction rims sacks, wheels, slave-soldier shoulders and cold haze for cinema and air; side light skims mud water, wheel ruts, tablet box and burlap for tactile texture. Woman and child receive only soft sky light, not hard judgmental light; the insect-wax handprint stays a small cold-white highlight. Tyndall light only follows the cart lane for depth and must not cover the doorway.

**Visual Content**
Mixed slave soldiers use hardened five-finger human hands and ropes to load grain sacks onto a wooden cart, wheel cutting mud beside the ancestral tablet box. Pure insect infantry stand on both sides of the cart lane with short spears or hook-sickles, taller than slave soldiers and villagers, enforcing the perimeter without moving sacks or gripping wrists. The woman kneels at the threshold, the child handprint still cold-white with wax. First frame reads sacks just loaded onto the cart; last frame reads the empty threshold, wheel ruts and cold haze after the cart leaves. Emotion stays restrained, with no heroic chase or exaggerated crying.

**Composition and Camera**
The FLF2V first-to-last frames use the same rear-threshold thirds composition: first frame foreground holds tablet box, cold-white wax handprint and mud water as mixed slave soldiers load grain sacks onto the cart; midground keeps woman and child low at the threshold while slave soldiers and cart wheels exit laterally, with pure insect armed guards holding both sides of the lane. By the last frame the cart recedes into cold haze, foreground remains empty threshold, tablet box and wheel ruts, and distant pure insect guards become oppressive silhouettes: the doorway stands but household grain is gone. The cart and slave soldiers exit laterally while the camera does not chase; it holds behind the household threshold with a very slow pullback, stressing that grain leaves while the home remains hollow. Wheel sound overtakes crying at the end.

**Constraints**
First and last frames must preserve the same threshold, same ancestral tablet box, same cart-exit direction, same pure-insect armed perimeter and same morning cold haze; the cart may recede into depth, but the camera must not turn it into an action chase. Pure insect infantry never move sacks or grip wrists; they only maintain route-blocking pressure. The hollow doorway is the final information.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern warehouse, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, text in image, random subtitles, random emblems, random readable register text, wrong faction wardrobe, grey refugee camp, magic light shafts, sacred backlight, broad horror bottom light, overexposed bloom, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks.

**Shot Negative**
avoid heroic cart chase, cart becoming a war chariot, modern wheels, exaggerated crying, broad fire-like bottom light, sacred backlight, geography changing after cart leaves, missing tablet box, child handprint turning bloody, pure insect soldiers moving sacks, pure insect guards without weapons, slave soldiers turning into clawed pure insects, floating sacks, plastic mud water, yellow glitter, digital speckle, excessive Tyndall beams, video smearing, glitches, compression blocks, melting figures.
```

## SC003 Reference Binding / SC003 参考图接入

中文：SC003 的四张核心密室参考帧 `r010e01.png` 到 `r013e01.png` 已通过高分复评，本轮直接作为主 I2V 图像输入。角色、地点和道具图片只接入 IPAdapter、Reference-only、Redux 或等价参考分支，权重必须低于主 I2V 帧。`r014e01.png` 是残阳坳封锁线匹配目标，只能用于后续剪辑或经明确批准后的 FLF2V 尾帧测试，不能混入本轮 SC003 密室 I2V。

English: The four core SC003 room reference frames `r010e01.png` through `r013e01.png` have passed high-score review and should be loaded directly as primary I2V image inputs for this pass. Character, location and prop images should only feed IPAdapter, Reference-only, Redux or equivalent support branches at lower weight than the primary I2V frame. `r014e01.png` is the Canyangao blockade match target and may only be used for a later edit or explicitly approved FLF2V tail test; it must not be blended into this SC003 room I2V pass.

| Image | Path | Node Role | Suggested Use |
| --- | --- | --- | --- |
| SC003-SH001 first frame | `01/assets/reference-frames/r010e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | Approved primary I2V frame; locks map, red cord, oil lamp and rain edge. |
| SC003-SH002 first frame | `01/assets/reference-frames/r011e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | Approved primary I2V frame; locks Gu/Yan table divide and face-reveal control. |
| SC003-SH003 first frame | `01/assets/reference-frames/r012e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | Approved primary I2V frame; locks genealogy, stopped fingers and untouched gap. |
| SC003-SH004 first frame | `01/assets/reference-frames/r013e01.png` | `PLACEHOLDER_I2V_IMAGE_NODE` | Approved primary I2V transition-start frame; locks red cord north end, droplet, dim oil lamp and line direction. |
| SC003-SH004 optional match target | `01/assets/reference-frames/r014e01.png` | optional later `PLACEHOLDER_LAST_FRAME_IMAGE_NODE` | Use only after explicit approval for edit/FLF2V tail testing; do not feed into this I2V room pass. |
| Yan Nanzhi state | `01/assets/characters/c002e01.png` | `PLACEHOLDER_CHARACTER_REFERENCE_NODE` | Identity, veil, robe and face-reveal-control support only. |
| Gu Huaizhang state | `01/assets/characters/c011e01.png` | `PLACEHOLDER_CHARACTER_REFERENCE_NODE` | Identity, old-minister posture and hand material support only. |
| Southern red-line room | `01/assets/locations/l014e01.png` | `PLACEHOLDER_LOCATION_REFERENCE_NODE` | Location and humid material reference only. |
| Old relay map redline | `01/assets/props/p009e01.png` | `PLACEHOLDER_PROP_REFERENCE_NODE` | Map, red cord, paper and pin material reference only. |
| Moon-white jade and blood genealogy | `01/assets/props/p002e01.png` | `PLACEHOLDER_PROP_REFERENCE_NODE` | Jade, genealogy, wax and old-paper material reference only. |
## SC003-SH001 Red line map

- Method: `I2V`
- Duration: `7s / 168 frames @ 24fps`
- First frame: `01/assets/reference-frames/r010e01.png`（approved highscore reference, use as primary I2V image input）
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`, `01/assets/style/f006e01.png`
- Output: `01/renders/raw/sc003-sh001.mp4`
- Status: `needs_config_motion_test`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕，视频生成优先保持已通过参考帧的构图、角色尺度和材质，不做重新构图。SC003 固定为雨夜南方红线空间：潮湿暖暗、朱赤红线、月白冷反光、真实纸纤维、蜡封、旧木、湿油布、水滴和布料材质。动作必须是低幅度、真实速度、可拍摄的微动；光源固定为左下低位油灯暖窄侧光、右上雨夜/月白冷反光、四角负补光，不新增圣光、魔法光束或舞台聚光。

**目标**
用桌面红线建立南方旧礼法把晏南枝推向北境的路线压力。

**光影**
低位油灯从左下擦过纸面，形成温暖窄侧光，凸出纸纤维、朱赤线绒毛、铜钉氧化边和湿木纹；右上雨夜月白冷反光只点水滴、油布折痕和地图裂缝。四角负补光压暗，保留潮湿暖暗，不做全局提亮。

**画面内容与动作**
参考帧构图保持不变：旧驿残图铺满横屏，朱赤红线从下方南缘斜向上方北境，铜钉、防潮卷轴筒、湿木桌沿和油布雨滴分层清楚。0-2 秒几乎静止，只允许油灯轻闪、雨滴敲油布和桌角水珠缓慢坠落；2-5 秒镜头沿红线向北极慢推进，焦点从下方线钉滑到上方北境水滴；5-7 秒停在红线北端和水滴，红线被水打湿略暗，但不发光。

**构图与运镜**
斜上俯角桌面特写，南缘在下方前景、北境在上方深处。运镜是低速真实前推，不旋转地图、不升空、不横摇搜索；跟焦只做一次，从南缘线钉到北境水滴。红线始终是物理绳线和政治压力，不变成导航线。

**连续性约束**
纸、线、铜、油布、旧木和水滴必须分材质；顾怀章只允许以画外袖缘或压角边缘存在，不能让人物手臂抢走红线。地图上不要生成可读现代文字，路线信息靠线、钉和水滴方向表达。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，随机可读文字，随机字幕，魔法光柱，神圣金光，过曝 bloom，广域恐怖底光，假舞台硬光，全局灰黑欠曝，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块，画面漂移，物体融化，参考帧构图被重做。

**镜头负面**
不要现代地图标注、清晰现代字体、电子导航线、高魔法发光路线、漂浮红线、地图旋转、升空俯拍、镜头穿桌、油灯变舞台聚光、丁达尔光柱遮住地图、塑料纸面、随机文字、全局提亮、全局灰黑欠曝。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Video generation must preserve the approved reference-frame composition, character scale and tactile materials instead of rebuilding the shot. SC003 is locked to the rainy southern red-line space: humid warm darkness, vermilion cord, moon-white cool reflections, real paper fibers, wax seal, old wood, wet oilcloth, droplets and cloth texture. Motion must stay small, real-time and filmable. The fixed lighting recipe is low warm narrow oil-lamp side light from lower-left, cool rainy moon-white bounce from upper-right, and corner negative fill, with no sacred light, magic beams or stage spotlight.

**Goal**
Establish the route pressure of southern old ritual pushing Yan Nanzhi toward the northern border through the tabletop red cord.

**Lighting**
A low oil lamp from lower-left skims the paper as warm narrow side light, revealing paper fibers, vermilion cord fuzz, oxidized brass-pin edges and wet wood grain. Cool moon-white rain bounce from upper-right only catches droplets, oilcloth folds and map cracks. Corner negative fill preserves humid warm darkness without global brightening.

**Visual Content and Action**
Keep the reference-frame composition intact: the damaged relay map fills the widescreen frame, the vermilion cord runs from the southern lower edge toward the northern upper depth, and brass pins, moisture-proof scroll tube, wet table edge and oilcloth rain droplets stay clearly layered. From 0-2s the frame is almost still, with only oil-lamp flicker, rain tapping oilcloth and a slow table-corner droplet. From 2-5s the camera pushes very slowly north along the cord, pulling focus from the lower brass pin to the northern rain dot. From 5-7s it settles on the cord north end and droplet; the wet cord darkens slightly but never glows.

**Composition and Camera**
Overhead-oblique tabletop close-up, with the southern edge in the lower foreground and the northern border receding upward. Use a slow real-time push only: no map rotation, no crane-up, no searching pan. Make a single focus pull from the southern pin to the northern rain dot. The cord remains physical rope and political pressure, never a navigation line.

**Continuity Constraints**
Paper, cord, brass, oilcloth, old wood and droplets must separate by material. Gu may only exist as an off-frame sleeve edge or map-corner pressure; no arm should steal focus from the cord. Do not generate readable modern text on the map; route information is carried by cord, pins and droplet direction.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, random readable text, random subtitles, magic light shafts, divine golden light, overexposed bloom, broad horror bottom light, fake hard stage lighting, flat grey underexposure, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks, drifting composition, melting objects, rebuilt reference-frame composition.

**Shot Negative**
avoid modern map labels, clean modern typography, electronic navigation line, high-magic glowing route, floating red cord, rotating map, crane-up aerial view, camera passing through the table, oil lamp becoming a stage spotlight, Tyndall beams hiding the map, plastic paper surface, random text, global brightening, flat grey underexposure.
```

## SC003-SH002 Evidence question

- Method: `I2V`
- Duration: `8s / 192 frames @ 24fps`
- First frame: `01/assets/reference-frames/r011e01.png`（approved highscore reference, use as primary I2V image input）
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`, `01/assets/style/f006e01.png`
- Output: `01/renders/raw/sc003-sh002.mp4`
- Status: `needs_config_motion_test`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕，视频生成优先保持已通过参考帧的构图、角色尺度和材质，不做重新构图。SC003 固定为雨夜南方红线空间：潮湿暖暗、朱赤红线、月白冷反光、真实纸纤维、蜡封、旧木、湿油布、水滴和布料材质。动作必须是低幅度、真实速度、可拍摄的微动；光源固定为左下低位油灯暖窄侧光、右上雨夜/月白冷反光、四角负补光，不新增圣光、魔法光束或舞台聚光。

**目标**
交代旧臣把皇血证据压给晏南枝，同时保留她对证据能否换来北门的怀疑。

**光影**
顾怀章在左侧油灯暖侧光里，老手、朱赤衣纹、卷轴边和地图纸纹被擦亮；晏南枝在右侧阴影里，只吃玉片和雨夜的窄冷边，勾指节、面纱边、下颌线和冷灰衣料。红线附近加深负补光，形成两人之间的政治边界；不要美颜柔光揭全脸。

**画面内容与动作**
参考帧构图保持低桌沿双人中近景：顾怀章在左侧灯边压住旧驿图，晏南枝在右侧阴影后半步，红线横在两人之间。0-2 秒锁住两人的手和红线；2-4 秒顾怀章手掌微压地图，袖口轻微下沉，像把证据压到桌面；4-6 秒晏南枝握玉片的指节收紧半拍，下颌在面纱下极小幅度动，表现回答前的克制；6-8 秒焦点从顾怀章压图手滑到晏南枝玉片手，再回到红线边界。

**构图与运镜**
低桌沿锁镜，不追脸、不推成肖像、不做华丽揭面。只允许一次极轻微跟焦和人物呼吸微动；台词由音频/字幕完成，视频只表现弱口部状态和下颌克制，不生成精确口型文字。

**连续性约束**
晏南枝保持遮面、冷灰流亡外袍、黑发红线和克制站姿；顾怀章是旧臣压力，不是慈祥引路人。玉片亮度低于红线与顾怀章压图手，不能变法器；红线不能消失，二人站位不能互换。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，随机可读文字，随机字幕，魔法光柱，神圣金光，过曝 bloom，广域恐怖底光，假舞台硬光，全局灰黑欠曝，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块，画面漂移，物体融化，参考帧构图被重做。

**镜头负面**
不要晏南枝全脸华丽揭示、网红脸、现代妆容、艳俗宫装、玉片变法器、玉片强过红线、神圣逆光、魔法光柱、广域恐怖底光、油灯过曝、背景全黑吞掉动作、红线消失、两人站位互换、字幕入画、精确口型文字、脸部花屏、手指融化、衣料塑料感。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Video generation must preserve the approved reference-frame composition, character scale and tactile materials instead of rebuilding the shot. SC003 is locked to the rainy southern red-line space: humid warm darkness, vermilion cord, moon-white cool reflections, real paper fibers, wax seal, old wood, wet oilcloth, droplets and cloth texture. Motion must stay small, real-time and filmable. The fixed lighting recipe is low warm narrow oil-lamp side light from lower-left, cool rainy moon-white bounce from upper-right, and corner negative fill, with no sacred light, magic beams or stage spotlight.

**Goal**
Show the old minister pressing royal-blood evidence onto Yan while preserving her doubt about whether evidence can open the northern gate.

**Lighting**
Gu Huaizhang stays in warm oil-lamp side light on the left, grazing aged hand skin, vermilion robe grain, scroll edge and map paper. Yan Nanzhi stays in right-side shadow, receiving only a narrow cool edge from jade and rainy night on knuckles, veil edge, jawline and cold-grey cloth. Deepen negative fill around the red cord as the political boundary between them; no beauty soft light may reveal her full face.

**Visual Content and Action**
Keep the low table-edge two-shot from the reference frame: Gu Huaizhang is on the left lamp side pressing the old relay map, Yan Nanzhi is half a step back in right-side shadow, and the red cord lies between them. From 0-2s lock on both hands and the cord. From 2-4s Gu presses the map slightly and his sleeve lowers a fraction, as if pinning the evidence to the table. From 4-6s Yan tightens fingers around the jade by half a beat, with a tiny jaw movement under the veil before answering. From 6-8s focus shifts from Gu pressing hand to Yan jade hand, then returns to the red-cord boundary.

**Composition and Camera**
Locked low table-edge frame: do not chase faces, turn into a portrait, or glamorously reveal Yan. Allow only one very small focus shift and breath-level body motion. Dialogue is handled by audio/subtitles; video only shows weak speaking state and restrained jaw motion, never exact lip-text generation.

**Continuity Constraints**
Yan remains veiled, in cold-grey exile robe with black hair and red cord, holding a restrained ritual posture. Gu reads as old-minister pressure, not a kindly guide. The jade must stay dimmer than the red cord and Gu pressing hand and must not become a magic weapon. The red cord cannot disappear, and the two character positions cannot swap.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, random readable text, random subtitles, magic light shafts, divine golden light, overexposed bloom, broad horror bottom light, fake hard stage lighting, flat grey underexposure, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks, drifting composition, melting objects, rebuilt reference-frame composition.

**Shot Negative**
avoid full glamorous Yan face reveal, influencer face, modern makeup, vulgar palace costume, jade becoming a magic weapon, jade brighter than the cord, sacred backlight, magic light shafts, broad horror bottom light, overexposed oil lamp, background blackness swallowing action, missing red cord, swapped character positions, subtitles in frame, exact lip-text generation, face glitches, melted fingers, plastic cloth.
```

## SC003-SH003 Blood genealogy not taken

- Method: `I2V`
- Duration: `9s / 216 frames @ 24fps`
- First frame: `01/assets/reference-frames/r012e01.png`（approved highscore reference, use as primary I2V image input）
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`, `01/assets/style/f006e01.png`
- Output: `01/renders/raw/sc003-sh003.mp4`
- Status: `needs_config_motion_test`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕，视频生成优先保持已通过参考帧的构图、角色尺度和材质，不做重新构图。SC003 固定为雨夜南方红线空间：潮湿暖暗、朱赤红线、月白冷反光、真实纸纤维、蜡封、旧木、湿油布、水滴和布料材质。动作必须是低幅度、真实速度、可拍摄的微动；光源固定为左下低位油灯暖窄侧光、右上雨夜/月白冷反光、四角负补光，不新增圣光、魔法光束或舞台聚光。

**目标**
把血牒、旧歌和晏南枝未接的手拍成希望与危险并存的停顿。

**光影**
左侧低位油灯掠过血牒，突出破损纸纤维、潮痕、旧蜡封、暗红旧印和桌面水痕；右侧阴影由月白玉片给指尖和面纱下缘一条窄冷边。暖光到冷光的交界必须落在红线与未接触空隙处，强调她没有接。

**画面内容与动作**
参考帧构图保持手部插入特写：前景红线虚焦横过下沿，中景半卷血牒、蜡封和一指宽空隙最清楚，右后方玉片只露小冷反光。0-3 秒顾怀章的手把半卷血牒从左侧暖灯区推过红线 2-3 厘米，纸边和蜡封轻擦湿桌；3-5 秒血牒在晏南枝指尖前停住，顾怀章的手退开；5-9 秒镜头保持在空隙上，晏南枝指尖只有微颤和呼吸带来的阴影，不触碰、不抓卷。

**构图与运镜**
桌面高度极小幅推进，终点落在“指尖没有接触血牒”的空隙。推进后保持静止，只允许火光、雨影、纸边停顿和呼吸微动；动作因果必须清楚，血牒不能漂浮，手不能突然跳变。

**连续性约束**
血牒是旧帝国合法性与旧债压力，不是胜利圣物；晏南枝的迟疑比道具更重要。中心空隙必须始终可见，纸纤维、蜡封、潮痕、桌面水迹、指节和面纱边缘必须清晰。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，随机可读文字，随机字幕，魔法光柱，神圣金光，过曝 bloom，广域恐怖底光，假舞台硬光，全局灰黑欠曝，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块，画面漂移，物体融化，参考帧构图被重做。

**镜头负面**
不要完整圣旨光效、皇权胜利感、血牒发光漂浮、手突然抓卷、指尖碰到血牒、空隙消失、手指融化、血腥奇观、随机可读文字、现代纸张、塑料蜡封、神圣逆光、魔法光柱、大面积底光、全局灰黑欠曝、视频涂抹、花屏。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Video generation must preserve the approved reference-frame composition, character scale and tactile materials instead of rebuilding the shot. SC003 is locked to the rainy southern red-line space: humid warm darkness, vermilion cord, moon-white cool reflections, real paper fibers, wax seal, old wood, wet oilcloth, droplets and cloth texture. Motion must stay small, real-time and filmable. The fixed lighting recipe is low warm narrow oil-lamp side light from lower-left, cool rainy moon-white bounce from upper-right, and corner negative fill, with no sacred light, magic beams or stage spotlight.

**Goal**
Render the blood genealogy, old song and Yan Nanzhi stopped hand as a pause where hope and danger coexist.

**Lighting**
A low oil lamp from the left grazes the genealogy, revealing torn paper fibers, moisture stains, old wax seal, dark-red old marks and water trails on the table. The right-side shadow receives only a narrow moon-white jade edge on fingertips and veil lower edge. The warm-to-cool boundary must fall on the red cord and untouched gap, stressing that she has not taken it.

**Visual Content and Action**
Keep the hand insert close-up from the reference frame: foreground red cord crosses the lower edge out of focus, midground half-rolled genealogy, wax seal and one-finger gap are the clearest information, and the rear-right jade appears only as a small cool reflection. From 0-3s Gu hand pushes the half-rolled genealogy 2-3 cm from warm left light across the red cord, with paper edge and wax seal scraping the wet table. From 3-5s the genealogy stops before Yan fingertips and Gu hand retreats. From 5-9s the shot holds on the gap; Yan fingertips show only a tiny tremor and breath shadow, never touching or grabbing the scroll.

**Composition and Camera**
Use a tiny table-height push whose endpoint is the gap where the fingertips do not touch the genealogy. After the push, hold still; allow only fire flicker, rain shadow, paper-edge settling and breath micro-motion. Action causality must stay clear: the genealogy cannot float and hands cannot jump.

**Continuity Constraints**
The genealogy is old-imperial legitimacy and debt pressure, not a triumphant sacred object; Yan hesitation matters more than the prop. The central gap must remain visible, with clear paper fibers, wax seal, moisture stains, table water trails, knuckles and veil edge.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, random readable text, random subtitles, magic light shafts, divine golden light, overexposed bloom, broad horror bottom light, fake hard stage lighting, flat grey underexposure, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks, drifting composition, melting objects, rebuilt reference-frame composition.

**Shot Negative**
avoid perfect sacred edict glow, triumphant royal legitimacy tone, glowing or floating genealogy, hand suddenly grabbing the scroll, fingertips touching the genealogy, disappearing gap, melted fingers, gore spectacle, random readable text, modern paper, plastic wax seal, sacred backlight, magic light shafts, broad bottom light, flat grey underexposure, video smearing, glitches.
```

## SC003-SH004 Road not necessarily throne

- Method: `I2V`
- Duration: `9s / 216 frames @ 24fps`
- First frame: `01/assets/reference-frames/r013e01.png`（approved highscore reference, use as primary I2V image input）
- Optional match target: `01/assets/reference-frames/r014e01.png`（only for later approved edit/FLF2V tail test, not part of this I2V pass）
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`, `01/assets/style/f006e01.png`
- Output: `01/renders/raw/sc003-sh004.mp4`
- Status: `needs_config_motion_test_optional_match_target`

### positive_prompt_zh

```text
**风格**
超写实电影级低魔东方史诗，16:9 横屏宽银幕，视频生成优先保持已通过参考帧的构图、角色尺度和材质，不做重新构图。SC003 固定为雨夜南方红线空间：潮湿暖暗、朱赤红线、月白冷反光、真实纸纤维、蜡封、旧木、湿油布、水滴和布料材质。动作必须是低幅度、真实速度、可拍摄的微动；光源固定为左下低位油灯暖窄侧光、右上雨夜/月白冷反光、四角负补光，不新增圣光、魔法光束或舞台聚光。

**目标**
用红线北端的图形转场首镜，准备把“路”在剪辑中反转成残阳坳封锁线。

**光影**
雨夜油灯被压暗，只保留低位暖边照亮红线纤维和水滴边缘；右上月白冷反光给纸裂和晏南枝虚焦剪影一条窄冷边。尾端只让暖暗轻微下降，预留下一镜残阳坳土褐与虫蜡冷白的剪辑入口，不在本镜提前生成圣光封锁线。

**画面内容与动作**
参考帧构图保持红线北端特写：红线北端和线钉在上三分之一，雨滴压在朱赤线和北境纸纹交界，油灯暖边低而暗，晏南枝遮面剪影只在远侧边缘虚焦。0-3 秒雨滴在红线纤维上变重，朱赤线被水打湿更深；3-6 秒镜头贴地图高度沿线端做短距离匹配移动，纸裂和水滴边缘保持清楚；6-9 秒曝光轻微下落，雨声准备切到人声，画面仍停留在南方红线密室，不提前跳到村口。

**构图与运镜**
本轮按 R013 做 I2V 转场首镜，而不是强制 R013->R014 的 FLF2V。运镜是贴近地图的短匹配移动，线条方向为后续剪辑保留；不做梦幻溶解、不全黑、不出现皇座或村口完整画面。若后续要 FLF2V，必须先确认/重做正确的封锁线终帧，再接入尾帧节点。

**连续性约束**
旧帝国路线期待在这里开始转成制度封锁压力，但本镜仍属于 L014 南方雨夜图桌。线条方向、红线纤维、水滴边缘、纸裂和冷暖尾端必须清楚；晏南枝只读剪影和遮面，不完整揭脸。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，随机可读文字，随机字幕，魔法光柱，神圣金光，过曝 bloom，广域恐怖底光，假舞台硬光，全局灰黑欠曝，黄色闪粉，数字颗粒，全局高频假锐化，视频涂抹，花屏，压缩块，画面漂移，物体融化，参考帧构图被重做。

**镜头负面**
不要皇座幻象、梦幻溶解、字卡解释、红线发光变法阵、圣光式逆光、魔法光柱、过曝 bloom、全黑转场、线条方向断裂、提前跳到完整残阳坳村口、晏南枝完整正脸、随机文字、油灯舞台化、视频涂抹、花屏、R014 村口画面直接混入本镜。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Video generation must preserve the approved reference-frame composition, character scale and tactile materials instead of rebuilding the shot. SC003 is locked to the rainy southern red-line space: humid warm darkness, vermilion cord, moon-white cool reflections, real paper fibers, wax seal, old wood, wet oilcloth, droplets and cloth texture. Motion must stay small, real-time and filmable. The fixed lighting recipe is low warm narrow oil-lamp side light from lower-left, cool rainy moon-white bounce from upper-right, and corner negative fill, with no sacred light, magic beams or stage spotlight.

**Goal**
Use the red-cord north-end transition-start shot to prepare an editorial reversal from road to the Canyangao checkpoint line.

**Lighting**
The rainy-night oil lamp is dimmed, leaving only a low warm edge on cord fibers and droplet rims. Cool moon-white bounce from upper-right gives paper cracks and Yan out-of-focus silhouette a narrow cold edge. At the tail, humid warm darkness drops slightly to leave an editorial opening for Canyangao earth brown and insect-wax cold white in the next shot; this shot must not generate sacred checkpoint light early.

**Visual Content and Action**
Keep the reference-frame close-up of the red cord north end: the cord end and pin sit near the upper third, a rain droplet presses on the boundary between vermilion fiber and northern paper grain, the oil-lamp warm edge is low and dim, and Yan veiled silhouette is only an out-of-focus far-edge weight. From 0-3s the droplet grows heavier on the cord fibers and the wet vermilion darkens. From 3-6s the camera makes a short map-level match move along the cord end while paper cracks and droplet rim stay readable. From 6-9s exposure lowers slightly and rain sound prepares to cut into crowd voice, but the image remains inside the southern red-line room and does not jump to the village gate early.

**Composition and Camera**
For this pass, use R013 as an I2V transition-start shot, not a forced R013-to-R014 FLF2V. The camera performs a short map-level match move, preserving line direction for a later edit. No dreamy dissolve, no full black, no throne vision, no complete village-gate image inside this shot. If a later FLF2V pass is needed, first approve or rebuild a correct blockade-line last frame before connecting it to the last-frame node.

**Continuity Constraints**
The old-imperial road expectation begins turning into bureaucratic blockade pressure here, but this shot still belongs to the L014 southern rainy-night map table. Line direction, cord fibers, droplet edge, paper cracks and the warm-cool tail must stay clear. Yan reads only as veiled silhouette, never full face.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, random readable text, random subtitles, magic light shafts, divine golden light, overexposed bloom, broad horror bottom light, fake hard stage lighting, flat grey underexposure, yellow glitter, digital speckle, global high-frequency fake sharpening, video smearing, glitches, compression blocks, drifting composition, melting objects, rebuilt reference-frame composition.

**Shot Negative**
avoid throne vision, dreamy dissolve, explanatory title card, red cord glowing into a magic array, sacred backlight, magic light shafts, overexposed bloom, full black transition, broken line direction, early jump to a complete Canyangao village gate, full Yan face reveal, random text, stage-like oil lamp, video smearing, glitches, R014 village-gate image blended directly into this shot.
```
