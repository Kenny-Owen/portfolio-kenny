import math
from pathlib import Path

from PIL import Image
from rembg import remove

src = Path(r"D:\Portfolio\assets\kenny-profile-source.png")
out = Path(r"D:\Portfolio\assets\kenny-profile.png")

subject = remove(src.read_bytes())
subject = Image.open(__import__("io").BytesIO(subject)).convert("RGBA")
w, h = subject.size

bg = Image.new("RGBA", (w, h))
bp = bg.load()
c1 = (232, 239, 248)
c2 = (230, 238, 255)
c3 = (232, 245, 238)
for y in range(h):
    for x in range(w):
        t = x / (w - 1) * 0.55 + y / (h - 1) * 0.45
        if t < 0.5:
            u = t / 0.5
            r = int(c1[0] + (c2[0] - c1[0]) * u)
            g = int(c1[1] + (c2[1] - c1[1]) * u)
            b = int(c1[2] + (c2[2] - c1[2]) * u)
        else:
            u = (t - 0.5) / 0.5
            r = int(c2[0] + (c3[0] - c2[0]) * u)
            g = int(c2[1] + (c3[1] - c2[1]) * u)
            b = int(c2[2] + (c3[2] - c2[2]) * u)
        bp[x, y] = (r, g, b, 255)

for y in range(h):
    for x in range(w):
        r, g, b, a = bg.getpixel((x, y))
        dx, dy = x - w * 0.2, y - h * 0.15
        dist = math.sqrt(dx * dx + dy * dy) / (w * 0.55)
        if dist < 1:
            strength = (1 - dist) ** 2 * 0.18
            g = min(255, int(g + strength * 18))
            b = min(255, int(b + strength * 38))
        bg.putpixel((x, y), (r, g, b, 255))

result = Image.alpha_composite(bg, subject)
result.convert("RGB").save(out, "PNG", optimize=True)
print("OK", out)
