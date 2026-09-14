# Copies the legal documents from the game repo into the site repo, adding Jekyll front
# matter. Re-runnable: publishing a revision is this script plus a commit, replacing the
# Google Sites paste ritual that CrazyPoly3's docs/legal/README.md describes - paste into a
# Google Doc, Paste special, copy into a Sites text box, re-hyperlink by hand, flatten every
# table because Sites has none.
#
#     python tools/publish_legal.py
#
# It took a pair argument until v3.1.0, when the offline 3.0.x set was removed: that set
# described a build with no account and nothing collected, and shipping online play made it
# a false statement about the app rather than an alternative to choose between. One set
# means there is no longer a wrong one to publish by mistake.
import io, os

from _paths import GAME, SITE, require

SRC_DIR = os.path.join(GAME, "docs", "legal")

# data-deletion.md is the address Google Play's Data safety form demands separately from the
# policy URL, and Play shows it on the public store listing - so it goes up with the other
# two rather than being remembered at submission time.
PAGES = [
    ("privacy-policy.md", "Privacy Policy", "/privacy-policy/"),
    ("terms-and-conditions.md", "Terms and Conditions", "/terms-and-conditions/"),
    ("data-deletion.md", "Deleting Your Data", "/data-deletion/"),
]

require(SRC_DIR, "the legal documents")

for name, title, permalink in PAGES:
    src = require(os.path.join(SRC_DIR, name), name)
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

print("\npublished")
