# -*- coding: utf-8 -*-
"""Normalise brand logos so they render at a consistent visual size.

The toplist tiles size artwork with object-fit:contain, so a square badge ends up
height-limited and tiny next to a wide wordmark that fills the tile. Each source
logo is trimmed of its transparent/white margin, scaled to a common *area* (so a
wordmark and a badge carry similar visual weight) and centred on one shared
canvas. Every output therefore has the same aspect ratio and renders at the same
size in an unchanged tile.

Originals are left untouched; output goes to logos/norm/.
"""
from PIL import Image, ImageChops
import pathlib

SRC = pathlib.Path("logos")
OUT = SRC / "norm"
CANVAS = (480, 144)          # 3.33:1, matching the 160x48 toplist tile
AREA_FRACTION = 0.62         # of the canvas, before clamping
MAX_W, MAX_H = 0.94, 0.94    # leave a little breathing room inside the tile

FILES = ["spinjo.png", "crownslots.jpg", "madcasino.png", "kingdom.png", "smash.png",
         "rivo.png", "lucky7even.jpg", "lucky-vibe.jpg", "rooster-bet.png",
         "fortune-play.png", "lucky-circus.jpg", "roby-casino.jpg", "spino.jpg",
         "ivibet.png", "ivibet-sportsbook.jpg", "hellspin.jpg", "slotgem.png",
         "betandplay.png"]


def trim(im):
    """Crop away a transparent or near-white margin."""
    im = im.convert("RGBA")
    alpha = im.split()[3]
    if alpha.getextrema()[0] < 250:
        box = alpha.getbbox()
    else:
        bg = Image.new("RGB", im.size, (255, 255, 255))
        diff = ImageChops.difference(im.convert("RGB"), bg)
        box = diff.convert("L").point(lambda p: 255 if p > 12 else 0).getbbox()
    return im.crop(box) if box else im


def normalise(name):
    art = trim(Image.open(SRC / name))
    w, h = art.size
    cw, ch = CANVAS

    scale = ((cw * ch * AREA_FRACTION) / (w * h)) ** 0.5
    scale = min(scale, cw * MAX_W / w, ch * MAX_H / h)
    size = (max(1, round(w * scale)), max(1, round(h * scale)))

    art = art.resize(size, Image.LANCZOS)
    canvas = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    canvas.paste(art, ((cw - size[0]) // 2, (ch - size[1]) // 2), art)

    dest = OUT / (pathlib.Path(name).stem + ".png")
    canvas.save(dest, optimize=True)
    return dest, size


OUT.mkdir(exist_ok=True)
print(f"{'brand':24s} {'rendered':>11s}  {'% of tile w':>11s}")
for n in FILES:
    dest, (w, h) = normalise(n)
    print(f"{dest.name:24s} {w:4d}x{h:<4d}  {w / CANVAS[0] * 100:9.0f}%")
