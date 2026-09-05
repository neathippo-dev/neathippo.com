# Builds web copies of the Play Store screenshots for the landing page.
#
# The source set is what CrazyPoly3/tools/screenshots.py renders (1920x1080 PNG, ~11MB
# for eight), which is right for Play and far too heavy for a page. These are 720px wide
# - twice the ~340px a card occupies in the two-column grid, so they stay sharp on a 2x
# display - and WebP, which is what makes the whole set cost less than one of the
# originals.
#
# Re-runnable: re-render the shots, run this, commit.
#
#     python tools/make_shots.py
import os
from PIL import Image

from _paths import MEDIA, SITE, require

SRC = os.path.join(MEDIA, "PlayStoreGraphics", "Screenshots", "CrazyPoly3", "en", "phone")
DST = os.path.join(SITE, "assets", "screenshots")
WIDTH = 720
QUALITY = 80

# The Play listing's feature graphic, reused as the page's hero. Rendered by
# CrazyPoly3/tools/feature_graphic.py at exactly 1024x500 (Play's rule), which is also
# the widest it is ever shown here - the text column is 46rem - so it is not resized,
# only re-encoded. Note the logo baked into it reads "CrazyPoly Online": that is the
# game's own Logo.svg as of v3.1.0, not something added for the banner.
FEATURE_SRC = os.path.join(MEDIA, "PlayStoreGraphics", "FeaturedGraphics", "CrazyPoly3",
                           "feature_graphic_en.png")
FEATURE_DST = os.path.join(SITE, "assets", "feature-graphic.webp")

# The names are the ones SHOTS uses in CrazyPoly3/tools/screenshots.py, which is what
# rendered the sources. Six of the eight it produces: enough to show the loop, the one
# mechanic nobody expects, and the second theme, without turning the page into a gallery.
# The captions are deliberately not here - they are page copy, and live in index.md so
# there is only ever one copy of them to edit.
SHOTS = ["table", "buy", "deal", "rob", "bank", "west_table"]

require(SRC, "the rendered screenshots")
os.makedirs(DST, exist_ok=True)

total = 0
for name in SHOTS:
    src = os.path.join(SRC, name + ".png")
    im = Image.open(src).convert("RGB")
    h = round(im.height * WIDTH / im.width)
    im = im.resize((WIDTH, h), Image.LANCZOS)
    out = os.path.join(DST, name + ".webp")
    im.save(out, "WEBP", quality=QUALITY, method=6)
    size = os.path.getsize(out)
    total += size
    print("%-14s %dx%d  %6.1f KB" % (name, WIDTH, h, size / 1024))

print("\ntotal %.0f KB for %d shots" % (total / 1024, len(SHOTS)))

require(FEATURE_SRC, "the feature graphic")
feature = Image.open(FEATURE_SRC).convert("RGB")
feature.save(FEATURE_DST, "WEBP", quality=QUALITY, method=6)
print("feature       %dx%d  %6.1f KB" % (
    feature.width, feature.height, os.path.getsize(FEATURE_DST) / 1024))
