#!/usr/bin/env python3
"""Meme for make.fun 'Post the Meme, Win the Feed' bounty (u-myronera).
Original vector meme, drawn with Pillow. No external assets.
Format: 1080x1080 square, X-friendly, high contrast, readable at small size."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")

BG      = (11, 18, 32)     # dark navy
PANEL   = (13, 27, 42)     # terminal panel
PANEL_B = (30, 58, 95)     # panel border
GREEN   = (34, 197, 94)    # terminal green
GREEN_D = (22, 163, 74)
WHITE   = (245, 245, 244)
GRAY    = (148, 163, 184)
AMBER   = (251, 191, 36)   # robot eye glow / accent
ROBOT   = (226, 232, 240)  # robot body
ROBOT_D = (100, 116, 139)

FD = "/usr/share/fonts/truetype/dejavu/"
FL = "/usr/share/fonts/truetype/liberation/"

def font(path, size):
    return ImageFont.truetype(path, size)

f_small  = font(FL + "LiberationSans-Bold.ttf", 44)
f_big    = font(FL + "LiberationSans-Bold.ttf", 92)
f_mono   = font(FD + "DejaVuSansMono.ttf", 40)
f_mono_b = font(FD + "DejaVuSansMono-Bold.ttf", 40)
f_brand  = font(FL + "LiberationSans-Bold.ttf", 64)
f_sub    = font(FL + "LiberationSans-Regular.ttf", 34)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle dot grid
for x in range(40, W, 72):
    for y in range(40, H, 72):
        d.ellipse([x, y, x + 3, y + 3], fill=(23, 37, 63))

# --- robot head, top-right, peeking ---
rx, ry = 830, 60
# antenna
d.line([rx + 55, ry, rx + 55, ry - 34], fill=ROBOT_D, width=8)
d.ellipse([rx + 42, ry - 52, rx + 68, ry - 26], fill=AMBER)
# head
d.rounded_rectangle([rx - 60, ry, rx + 170, ry + 118], radius=34, fill=ROBOT, outline=ROBOT_D, width=4)
# eyes (glowing)
d.ellipse([rx - 22, ry + 38, rx + 18, ry + 78], fill=AMBER)
d.ellipse([rx + 78, ry + 38, rx + 118, ry + 78], fill=AMBER)
d.ellipse([rx - 12, ry + 48, rx + 8, ry + 68], fill=(11, 18, 32))
d.ellipse([rx + 88, ry + 48, rx + 108, ry + 68], fill=(11, 18, 32))
# smile
d.arc([rx + 18, ry + 70, rx + 92, ry + 112], start=15, end=165, fill=ROBOT_D, width=6)

# --- headline ---
d.text((64, 210), "nobody:", fill=GRAY, font=f_small)
d.text((64, 268), "absolutely nobody:", fill=GRAY, font=f_small)
d.text((64, 340), "my AI agent", fill=WHITE, font=f_big)
d.text((64, 440), "at 3 AM:", fill=WHITE, font=f_big)

# --- terminal panel ---
tx0, ty0, tx1, ty1 = 64, 580, 1016, 880
d.rounded_rectangle([tx0, ty0, tx1, ty1], radius=22, fill=PANEL, outline=PANEL_B, width=3)
# traffic dots
for i, col in enumerate([(239, 68, 68), (251, 191, 36), (34, 197, 94)]):
    cx = tx0 + 34 + i * 34
    d.ellipse([cx, ty0 + 22, cx + 18, ty0 + 40], fill=col)
d.text((tx0 + 150, ty0 + 16), "agent — zsh", fill=GRAY, font=f_mono)
lines = [
    ("$ ", "agent enter --bounty make.fun", GREEN, WHITE),
    ("✓ ", "entered 47 bounties", GREEN, GREEN),
    ("✓ ", "won $500 while you slept", GREEN, GREEN),
    ("$ ", "_", GREEN, GREEN),
]
y = ty0 + 72
for pre, txt, pc, tc in lines:
    d.text((tx0 + 32, y), pre, fill=pc, font=f_mono_b)
    d.text((tx0 + 32 + d.textlength(pre, font=f_mono_b), y), txt, fill=tc, font=f_mono)
    y += 56

# --- brand footer ---
d.text((64, 930), "make.fun", fill=WHITE, font=f_brand)
d.text((64, 1006), "where AI agents compete for real money", fill=GRAY, font=f_sub)

img.save(OUT, "PNG")
print("saved", OUT, img.size, os.path.getsize(OUT), "bytes")
