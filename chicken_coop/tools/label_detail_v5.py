"""Draw text labels with leader lines on models/renders_v5/detail/D*.png using labels.json
(written by models/render_detail_v5.py), and stack the parked-vs-lifted side views.
Usage: python tools/label_detail_v5.py"""
import json
from PIL import Image, ImageDraw, ImageFont

D = r"C:\Lucho\rancho\IA\chicken_coop\models\renders_v5"
try:
    font = ImageFont.truetype("arial.ttf", 30)
    small = ImageFont.truetype("arial.ttf", 34)
except OSError:
    font = small = ImageFont.load_default()

labels = json.load(open(D + r"\detail\labels.json"))
for name, pts in labels.items():
    if not pts:
        continue
    im = Image.open(f"{D}\detail\{name}.png").convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im)
    for text, (px, py, dx, dy) in pts.items():
        ax, ay = px * W, py * H
        tx, ty = ax + dx, ay + dy
        bb = d.textbbox((tx, ty), text, font=font)
        d.rectangle((bb[0] - 8, bb[1] - 5, bb[2] + 8, bb[3] + 5), fill=(255, 255, 255), outline=(30, 30, 30))
        cx = min(max(ax, bb[0]), bb[2]) if False else (bb[0] + bb[2]) / 2
        cy = bb[1] - 5 if ay < bb[1] else (bb[3] + 5 if ay > bb[3] else (bb[1] + bb[3]) / 2)
        d.line((cx, cy, ax, ay), fill=(200, 30, 30), width=3)
        d.ellipse((ax - 7, ay - 7, ax + 7, ay + 7), fill=(200, 30, 30))
        d.text((tx, ty), text, fill=(20, 20, 20), font=font)
    im.save(f"{D}\detail\{name}_labeled.png")

# parked vs lifted, same camera, stacked
a = Image.open(D + r"\07_crank_rest_side.png").convert("RGB")
b = Image.open(D + r"\08e_lifted_side.png").convert("RGB")
W, H = a.size
out = Image.new("RGB", (W, 2 * H), (255, 255, 255))
out.paste(a, (0, 0))
out.paste(b, (0, H))
d = ImageDraw.Draw(out)
for y, t in ((10, "PARKED: wheel flush with the frame bottom"), (H + 10, "LIFTED: wheel stays on the ground, whole coop is 12 cm higher")):
    bb = d.textbbox((20, y), t, font=small)
    d.rectangle((bb[0] - 8, bb[1] - 5, bb[2] + 8, bb[3] + 5), fill=(255, 255, 255), outline=(30, 30, 30))
    d.text((20, y), t, fill=(20, 20, 20), font=small)
d.line((0, H, W, H), fill=(30, 30, 30), width=3)
out.save(D + r"\08g_parked_vs_lifted.png")
print("labeled", len(labels), "detail views + comparison")
