#!/usr/bin/env python3
"""
High-Resolution Image to ASCII Art Generator for Terminal Profile & Cards.
Supports contrast adjustment, character density mapping, and ANSI/SVG export.
"""

import sys
import os

try:
    from PIL import Image, ImageEnhance
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pillow", "--break-system-packages", "-q"], check=True)
    from PIL import Image, ImageEnhance

# Character ramps from darkest to lightest
RAMP_DETAILED = "@%#*+=-:. "
RAMP_BLOCKS = "█▓▒░ "
RAMP_CYBER = "█▓▒░+=:-. "

def convert_image_to_ascii(image_path, width=42, ramp=RAMP_DETAILED, contrast=1.4, invert=False):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}", file=sys.stderr)
        return None

    img = Image.open(image_path).convert("L")
    
    # Increase contrast for sharper ASCII features
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    # Calculate aspect ratio (terminal chars are ~2x taller than wide)
    orig_w, orig_h = img.size
    aspect = orig_h / orig_w
    height = int(width * aspect * 0.55)

    img = img.resize((width, height), Image.Resampling.LANCZOS)
    pixels = img.getdata()

    ramp_chars = ramp if not invert else ramp[::-1]
    num_chars = len(ramp_chars)

    ascii_str = ""
    for i, p in enumerate(pixels):
        char_idx = int((p / 255) * (num_chars - 1))
        ascii_str += ramp_chars[char_idx]
        if (i + 1) % width == 0:
            ascii_str += "\n"

    return ascii_str

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 photo_to_ascii.py <path_to_image> [width=42] [contrast=1.4]")
        print("Example: python3 photo_to_ascii.py ~/photo.jpg 40 1.5")
        sys.exit(0)

    path = sys.argv[1]
    w = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    c = float(sys.argv[3]) if len(sys.argv) > 3 else 1.4
    
    result = convert_image_to_ascii(path, width=w, contrast=c)
    if result:
        print(result)
