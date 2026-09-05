# Where everything is, worked out from this file rather than written down.
#
# The three repositories sit side by side:
#
#     <workspace>/neathippo.com     this site
#     <workspace>/CrazyPoly3        the game
#     <workspace>/Media             the rendered store art
#
# so the site root is this file's grandparent and the other two are its siblings. That
# is the whole reason for this module: the scripts used to hardcode one machine's
# absolute paths, which tied them to that machine, and - since Jekyll copies any file it
# is not told to skip into the built site - would have published that layout on the web
# if the exclude in _config.yml were ever forgotten.
import os

TOOLS = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(TOOLS)
WORKSPACE = os.path.dirname(SITE)

GAME = os.path.join(WORKSPACE, "CrazyPoly3")
MEDIA = os.path.join(WORKSPACE, "Media")


def require(path, what):
    """Fails with the path it wanted rather than a traceback five frames deep.

    These scripts read from two directories this repository does not contain, so "not
    found" is the expected way for them to fail on a machine that has only cloned the
    site - and it should say which directory and where it looked."""
    if not os.path.exists(path):
        raise SystemExit(
            "Could not find %s at:\n    %s\n\n"
            "This script reads from the game repo and the Media folder, which are "
            "expected to sit beside this one:\n"
            "    %s\\neathippo.com\n    %s\\CrazyPoly3\n    %s\\Media"
            % (what, path, WORKSPACE, WORKSPACE, WORKSPACE))
    return path
