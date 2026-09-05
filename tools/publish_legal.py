# Copies a legal pair from the game repo into the site repo, adding Jekyll front matter.
# Re-runnable: publishing a new revision (or swapping 3.0.x -> the online pair) is this
# script plus a commit, replacing the Google Sites paste ritual that CrazyPoly3's
# docs/legal/README.md describes - paste into a Google Doc, Paste special, copy into a
# Sites text box, re-hyperlink by hand, flatten every table because Sites has none.
#
#     python tools/publish_legal.py 3.0.x     # the offline pair, live today
#     python tools/publish_legal.py online    # the pair in docs/legal/ itself
import io, os, sys

from _paths import GAME, SITE, require

SRC_ROOT = os.path.join(GAME, "docs", "legal")

PAGES = [
    ("privacy-policy.md", "Privacy Policy", "/privacy-policy/"),
    ("terms-and-conditions.md", "Terms and Conditions", "/terms-and-conditions/"),
]

pair = sys.argv[1] if len(sys.argv) > 1 else "3.0.x"
src_dir = SRC_ROOT if pair == "online" else os.path.join(SRC_ROOT, pair)
require(src_dir, "the '%s' legal pair" % pair)

for name, title, permalink in PAGES:
    src = require(os.path.join(src_dir, name), name)
    body = io.open(src, encoding="utf-8").read()

    # The H1 is the layout's job - keeping the markdown's own would print it twice.
    lines = body.split("\n")
    if lines and lines[0].startswith("# "):
        heading = lines[0][2:].strip()
        body = "\n".join(lines[1:]).lstrip("\n")
    else:
        heading = title

    front = (
        "---\n"
        "layout: default\n"
        'title: "%s"\n'
        "permalink: %s\n"
        "---\n\n"
        "# %s\n\n"
    ) % (title, permalink, heading)

    out = os.path.join(SITE, name)
    io.open(out, "w", encoding="utf-8", newline="\n").write(front + body)
    print("%-28s <- %s" % (name, src))

print("\npair published: %s" % pair)
