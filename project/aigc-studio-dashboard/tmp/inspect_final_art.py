from PIL import Image
from pathlib import Path
for p in ['public/assets/final-art/office-master.png','public/assets/final-art/female-walksheet-raw.png','public/assets/final-art/female-walksheet-alpha.png']:
    im = Image.open(p)
    alpha = im.getextrema()[-1] if 'A' in im.mode else 'no-alpha'
    print(Path(p).name, im.mode, im.size, alpha)
