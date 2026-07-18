from PIL import Image
paths=['public/assets/25d/office_foreground.png','public/assets/25d/office_glass.png','public/assets/25d/characters/female_01/walk/00.png']
for p in paths:
 im=Image.open(p); alpha=im.getextrema()[-1] if 'A' in im.mode else 'no alpha'; print(p, im.mode, im.size, alpha)
