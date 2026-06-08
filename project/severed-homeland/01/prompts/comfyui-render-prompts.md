# 第01集 SC001 ComfyUI 完整提示词

## 使用说明

中文：本文件是可直接复制到 ComfyUI prompt 节点的分段组装版提示词。每个镜头复制一组 `positive_prompt` 和 `negative_prompt` 即可，不要再复制 JSON 字段名。中文和英文任选一套使用，不建议同一轮同时混用两套语言。

English: This file contains sectioned, copy-ready assembled prompts for ComfyUI prompt nodes. Copy one `positive_prompt` and one `negative_prompt` per shot; do not copy JSON field names. Use either the Chinese or English pair for a render pass, not both languages mixed together.

## SC001-SH001

- Method: `FLF2V`
- Duration: `3.5s / 84 frames @ 24fps`
- First frame: `01/assets/reference-frames/r001e01.png`
- Last frame: `01/assets/reference-frames/r002e01.png`
- Style refs: `01/assets/style/f001e01.png`, `01/assets/style/f005e01.png`
- Beast refs: `assets/characters/c020m.png`, `assets/characters/c021m.png`, `01/assets/characters/c020e01.png`
- Output: `01/renders/raw/sc001-sh001.mp4`

### positive_prompt_zh

```text
**风格**
超写实电影质感低魔东方史诗，16:9 横屏宽银幕。冷白暴雪边境，低调高反差，材质与空间以参考帧为准，真实重心、真实速度、自然呼吸、接触反作用。

**目标**
在暴雪中建立锁喉关外墙攻城压力：从攻城方斜后侧低机位的兽潮构图起，落到城头中景偏近的骨钟、黑石女墙和人族守军；墙外兽潮仍在斜下方可见，为切入人族身体代价做转场。

**光影**
斜侧攻城建立镜头布光：冷白暴雪天光压出黑墙巨型剪影，黑墙负补光吞掉墙面和兽潮大暗面；远处暗红火线和火盆亮度克制，从低位反打雪雾、烟尘、攻城队列、旗帜破布、旧铁、巨角边缘、骨钟和守军肩线，形成残酷战场尺度。

**画面内容**
首帧构图是攻城方斜后侧低机位，三分之四角度看同一面锁喉关黑石巨墙；前景只有继承 `C020/C021/E01_C020` 的兽族攻城队列肩背、旧铁甲片、破旗、火盆、雪泥脚步和一截巨兽背脊或巨角，兽潮从画面左前方斜推向右后方城门，城门不居中、军阵不对称，远处墙头只见很小的同一口骨钟和守军剪影。尾帧构图是同一城头中景偏近，画面一半是同一钟架、同一口骨钟、黑石女墙、雪泥墙面、守军肩背、冻裂手、长矛或门闩局部；另一半俯看城外兽族和伴生兽仍朝这面墙攻来。全镜头只允许一面城墙、一个钟架、一口钟。

**运镜**
使用首尾参考帧约束斜侧攻城到同一墙头落点。镜头顺旗杆、烟柱、巨角和同一面黑墙外立面斜爬上墙头，旁白随起镜进入；到达墙头后约 45 度转向人族女墙空间。不正面穿向城门，不穿墙，不做180度调头，不生成远处第二道墙、第二个城门或第二个钟架。骨钟横摆、雪雾吃画面和钟声裂响可作为隐藏剪切点，下一镜切到同一口骨钟旁的年轻军户。

**约束**
人族守军在墙头，兽族攻城方在墙外和墙下；尾帧必须同时读到墙头人族空间和斜下方墙外兽潮方向。兽族士兵和伴生兽必须继承 `C020/c020m.png`、`C021/c021m.png`、`E01_C020/c020e01.png`，并保持多兵种、多伴生兽形态。骨钟属于墙头同一警钟架，残缺淡金旧日月痕只能被裂缝、铜锈和雪泥遮住，不能完整发光。
旧日月痕必须残缺、黯淡、被裂缝、铜锈和雪泥吃掉，不可发光或圣物化。
```

### negative_prompt_zh

```text
**通用负面**
现代服饰，现代建筑，现代武器，枪械，科幻 UI，塑料 CG，过度磨皮，网红脸，武侠强光，魔法光柱，神圣金光，过曝 bloom，镜头光斑滥用，漂浮慢动作，僵硬摆拍，血腥奇观，完整发光徽章，巨龙化猛犸，画面中文字，随机字幕，错误朝代盔甲。

**镜头负面**
不要现代服饰、枪械、科幻 UI、塑料 CG、正面居中城门、左右完全对称军阵、航拍感、游戏飞镜、穿墙、180度调头、远处第二道城墙、第二个钟架、第二只钟、钟架方向变化、城外人族、兽族看镜头列队、纯骨钟特写、看不到墙头守军、看不到墙外兽潮方向、完整发光徽章、巨龙化猛犸、魔法光柱、神圣金光、过曝 bloom、镜头光斑滥用、漂浮慢动作、血腥奇观、画面中文字、随机字幕、战场空间跳变。
```

### positive_prompt_en

```text
**Style**
Hyper-realistic cinematic grounded low-magic Eastern epic, 16:9 landscape widescreen. Cold blizzard borderland, low-key high contrast, materials and geography follow the reference frames, real body weight, real speed, natural breathing, contact reaction.

**Goal**
Establish the Suohou Gate outer-wall siege pressure in blizzard: begin from a low diagonal rear-side siege composition and land in a wall-top medium-near composition of bone bell, blackstone parapet and human defenders, with the exterior beast tide still visible below on a diagonal as the transition into human bodily cost.

**Lighting**
Diagonal siege-establishing lighting: cold blizzard sky light silhouettes the massive black wall, black-wall negative fill swallows the wall face and the beast tide's large shadow masses; distant dark-red firelines and braziers stay controlled in brightness and low-counterlight snow haze, smoke, siege ranks, torn banners, old iron, horn edges, bone bell and defender shoulder lines, creating brutal battlefield scale.

**Visual Content**
First-frame composition: low diagonal rear-side siege angle, a three-quarter view of the same Suohou Gate blackstone wall; foreground shows only C020/C021/E01_C020 beast siege shoulders, old iron armor plates, torn banners, brazier fire, snow-mud footsteps and one partial beast spine or horn, with the beast tide pushing from front-left toward the gate at rear-right, the gate not centered and the ranks not symmetrical, while the same wall-top bone bell and defenders are only small silhouettes far away. Last-frame composition: same wall-top medium-near endpoint, split between the same bell frame, same broken bell, blackstone parapet, snow-mud wall surface, defender shoulders, cracked hands, spear or gate-bar details, and a diagonal downward view of exterior beast troops and companion beasts still facing this wall. Only one wall, one bell frame and one bell are allowed through the shot.

**Camera / Motion**
Use first and last reference frames to constrain the move from diagonal siege pressure to the same wall-top landing. The camera climbs along flags, smoke columns, horn shapes and the same exterior black wall toward the bone bell as the voiceover enters, then turns about 45 degrees onto the human parapet; it does not push frontally into the gate, pass through the wall, make a 180-degree turn, or create a distant second wall, second gate or second bell frame. The bell swing, snow haze swallowing the frame and cracked bell sound can act as the hidden cut point into the next shot beside the same bell and young soldier.

**Constraints**
Human defenders stay on the wall top and beast attackers stay outside and below the wall; the last frame must read both the human wall-top space and the exterior beast tide direction below on a diagonal. Beast soldiers and companion beasts must inherit `C020/c020m.png`, `C021/c021m.png`, and `E01_C020/c020e01.png` with varied troop and beast types. The bone bell belongs to the same wall-top bell frame, and faint broken old sun-moon traces must be obscured by cracks, verdigris and snow mud, never complete or glowing.
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid modern clothing, firearms, sci-fi UI, plastic CGI, centered frontal gate, perfectly symmetrical ranks, aerial-game feeling, game-like flying camera, passing through the wall, 180-degree turn, distant second wall, second bell frame, second bell, changed bell-frame direction, humans outside the wall, beast troops posing toward camera, pure bone-bell close-up, missing wall-top defenders, missing exterior beast-tide direction, complete glowing emblem, dragon-like mammoth, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, gore spectacle, text in image, random subtitles, battlefield spatial jumps.
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
骨钟仍在同一墙头警钟架，墙外战场方向不变；旧徽不发光，冻血暗红，儿童化或英雄化脸型都不可出现。
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
The bone bell remains in the same wall-top bell frame and the exterior battlefield direction does not change; the old emblem does not glow, frozen blood is dark red, and no childlike or heroic face treatment appears.
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
薛临墙不是华甲将军或武侠宗师；他是旧墙师，话短、低声、急促但不慌。骨钟、墙缝和枪线必须仍与前两镜同一空间。
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
Xue Linqiang is not an ornate general or wuxia master; he is an old wall master, speaking briefly, low, urgent but controlled. The bell, wall seam and spear line must remain in the same space as the previous two shots.
Old sun-moon traces must be broken, dim, eaten by cracks, verdigris and snow mud, never glowing or sacred.
```

### negative_prompt_en

```text
**Global Negative**
modern clothing, modern architecture, modern weapons, firearms, sci-fi UI, plastic CGI, over-smoothed skin, influencer face, wuxia power glow, magic light beam, divine golden light, overexposed bloom, excessive lens flare, floaty slow motion, stiff posing, gore spectacle, complete glowing emblem, dragon-like mammoth, text in image, random subtitles, wrong-period armor.

**Shot Negative**
avoid grandmaster pose, wuxia glow, divine heroic backlight, overexposed face light, ornate general armor, dialogue text in frame, exaggerated lip movement, younger identity drift, missing bone bell.
```
