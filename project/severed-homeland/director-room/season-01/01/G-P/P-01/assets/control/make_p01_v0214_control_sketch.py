from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).with_name("P-01-v0214-F1E-wall-continuity-sketch.png")
W, H = 1920, 1080


def font(size: int) -> ImageFont.FreeTypeFont:
    for p in [
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new("RGB", (W, H), (22, 24, 27))
d = ImageDraw.Draw(img)
f_title = font(40)
f_h = font(30)
f = font(24)
f_s = font(20)

white = (232, 232, 220)
muted = (160, 166, 168)
wall = (64, 68, 70)
wall_hi = (98, 103, 106)
gate = (36, 38, 40)
iron = (130, 132, 125)
beast = (116, 102, 88)
grain = (145, 116, 50)
red = (194, 72, 60)
blue = (78, 146, 210)
green = (94, 166, 118)
yellow = (214, 182, 84)

d.text((40, 28), "P-01 v0214 F1E 控制图：同一城墙 + C021 破门猛犸局部撞门", fill=white, font=f_title)
d.text((40, 84), "目的：观众一眼看懂外部撞门、城头同墙、床弩朝外；不再慢动作，不再新怪物，不再烟尘遮羞。", fill=muted, font=f)

# Left panel: overhead topology
lx, ly, lw, lh = 60, 150, 820, 830
d.rounded_rectangle((lx, ly, lx + lw, ly + lh), radius=18, outline=(86, 90, 94), width=3)
d.text((lx + 24, ly + 20), "A. 俯视拓扑：门洞、城头、粮栈是同一套空间", fill=white, font=f_h)

# wall top
d.rectangle((lx + 120, ly + 300, lx + 720, ly + 400), fill=wall, outline=wall_hi, width=3)
d.text((lx + 300, ly + 330), "同一堵黑石主墙 / 门楼墙顶", fill=white, font=f_s)
# gate
d.rectangle((lx + 360, ly + 210, lx + 480, ly + 500), fill=gate, outline=iron, width=4)
d.text((lx + 350, ly + 176), "黑石主门 / 铁栅", fill=white, font=f_s)
# outside/inside labels
d.text((lx + 55, ly + 236), "城外 Y+", fill=muted, font=f)
d.text((lx + 640, ly + 236), "城内 Y-", fill=muted, font=f)
# beast
d.ellipse((lx + 180, ly + 215, lx + 380, ly + 415), fill=beast, outline=(170, 154, 130), width=4)
d.polygon([(lx + 345, ly + 300), (lx + 420, ly + 280), (lx + 405, ly + 330)], fill=(210, 196, 155))
d.text((lx + 120, ly + 430), "C021 破门猛犸局部\n肩/角/鼻压门\n必须来自 c021m", fill=white, font=f_s)
d.line((lx + 330, ly + 315, lx + 390, ly + 315), fill=red, width=6)
d.text((lx + 276, ly + 132), "撞击点必须清楚", fill=red, font=f_s)
# handler
d.ellipse((lx + 115, ly + 455, lx + 150, ly + 490), fill=green)
d.line((lx + 150, ly + 470, lx + 260, ly + 360), fill=green, width=3)
d.text((lx + 42, ly + 500), "驭兽者 / 骨笛 / 绳环\n只需剪影，证明不是无主怪物", fill=green, font=f_s)
# ballista and walkway
d.rectangle((lx + 500, ly + 260, lx + 630, ly + 290), fill=(92, 70, 50), outline=yellow, width=3)
d.line((lx + 500, ly + 275, lx + 365, ly + 315), fill=yellow, width=4)
d.text((lx + 530, ly + 220), "床弩在城头\n射线朝城外", fill=yellow, font=f_s)
# stair grate and grain
d.rectangle((lx + 585, ly + 430, lx + 690, ly + 520), fill=(42, 45, 47), outline=iron, width=3)
for i in range(6):
    x = lx + 595 + i * 16
    d.line((x, ly + 435, x, ly + 515), fill=iron, width=2)
d.text((lx + 585, ly + 532), "下城楼铁栅锁死", fill=white, font=f_s)
for i in range(5):
    d.ellipse((lx + 620 + (i % 3) * 28, ly + 590 + (i // 3) * 26, lx + 650 + (i % 3) * 28, ly + 616 + (i // 3) * 26), fill=grain)
d.text((lx + 580, ly + 650), "军需粮栈区\n有粮但拿不到", fill=grain, font=f_s)
# camera
d.polygon([(lx + 90, ly + 160), (lx + 130, ly + 190), (lx + 85, ly + 210)], fill=blue)
d.line((lx + 120, ly + 190, lx + 390, ly + 310), fill=blue, width=3)
d.text((lx + 135, ly + 150), "F1E 外侧低机位\n三分之四看同一墙", fill=blue, font=f_s)

# Right panel: frame composition
rx, ry, rw, rh = 960, 150, 900, 830
d.rounded_rectangle((rx, ry, rx + rw, ry + rh), radius=18, outline=(86, 90, 94), width=3)
d.text((rx + 24, ry + 20), "B. F1E 画面构图：用一帧证明同一堵墙", fill=white, font=f_h)

frame = (rx + 70, ry + 95, rx + 830, ry + 620)
d.rectangle(frame, fill=(31, 34, 37), outline=white, width=3)
# vertical wall face
d.rectangle((rx + 410, ry + 120, rx + 710, ry + 610), fill=wall, outline=wall_hi, width=3)
for x in range(rx + 430, rx + 700, 45):
    d.line((x, ry + 120, x - 80, ry + 610), fill=(80, 84, 87), width=2)
d.text((rx + 565, ry + 128), "同一黑石墙面\n从门洞上接城头", fill=white, font=f_s, anchor="ma")
# gate arch
d.rounded_rectangle((rx + 455, ry + 360, rx + 645, ry + 610), radius=70, fill=gate, outline=iron, width=4)
for x in range(rx + 485, rx + 640, 28):
    d.line((x, ry + 390, x, ry + 608), fill=iron, width=3)
d.text((rx + 455, ry + 632), "关闭的主门 / 铁栅", fill=white, font=f_s)
# parapet and soldiers
d.rectangle((rx + 435, ry + 110, rx + 750, ry + 165), fill=wall_hi, outline=iron, width=3)
for i in range(4):
    d.rectangle((rx + 455 + i * 70, ry + 70, rx + 490 + i * 70, ry + 120), fill=wall_hi)
d.rectangle((rx + 585, ry + 80, rx + 715, ry + 100), fill=(92, 70, 50), outline=yellow, width=3)
d.line((rx + 585, ry + 90, rx + 465, ry + 385), fill=yellow, width=3)
d.text((rx + 595, ry + 45), "城头同墙：士兵 / 床弩轮廓", fill=yellow, font=f_s)
# beast partial outside
d.ellipse((rx + 170, ry + 300, rx + 520, ry + 675), fill=beast, outline=(170, 154, 130), width=4)
d.pieslice((rx + 370, ry + 265, rx + 560, ry + 445), start=300, end=80, fill=(210, 196, 155))
d.pieslice((rx + 318, ry + 250, rx + 470, ry + 405), start=300, end=70, fill=(210, 196, 155))
d.text((rx + 105, ry + 682), "只拍 C021 破门猛犸局部\n可见绳环/骨饰/旧伤\n不许新怪物 Boss 化", fill=white, font=f_s)
d.line((rx + 450, ry + 440, rx + 495, ry + 438), fill=red, width=8)
d.text((rx + 345, ry + 245), "肩/角撞门接触点", fill=red, font=f_s)
# handler silhouette
d.ellipse((rx + 185, ry + 240, rx + 215, ry + 270), fill=green)
d.line((rx + 200, ry + 270, rx + 230, ry + 330), fill=green, width=5)
d.line((rx + 215, ry + 286, rx + 335, ry + 380), fill=green, width=3)
d.text((rx + 95, ry + 208), "驭兽者剪影", fill=green, font=f_s)
# bottom rules
rules_y = ry + 660
d.text((rx + 70, rules_y), "F1E 视频要求", fill=white, font=f_h)
rules = [
    "时长 1.2-1.6 秒，真实 1x 速度；不是慢动作，不用尾帧停顿冒充表演。",
    "镜头只轻震，不旋转、不甩镜；门体震、墙上人退半步，动作清楚。",
    "人物和城墙锚点必须清晰；若仍糊脸/糊人/糊门，直接打回。",
    "画面必须同时有：C021 局部、关闭主门、同一墙面、城头床弩/士兵。",
]
for i, txt in enumerate(rules):
    y = rules_y + 48 + i * 38
    d.ellipse((rx + 72, y + 8, rx + 84, y + 20), fill=red if i == 0 else blue)
    d.text((rx + 96, y), txt, fill=white, font=f_s)

d.text((40, 1010), "导演判定：v0213 慢动作 / 糊人 / C021 失锁 / 墙体连续性不清，禁止晋升。v0214 先补 C021 shot-state 与场景连续控制，再允许视频部重跑。", fill=(238, 200, 120), font=f)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
