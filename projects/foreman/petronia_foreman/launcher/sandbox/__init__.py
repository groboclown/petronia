"""
Windows Sandbox executable.

Reference:
 https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md
 https://chromium.googlesource.com/chromium/src/+/master/sandbox/

The sandbox source must be pulled and compiled.

1. Find the latest Stable branch of chromium:
    https://chromereleases.googleblog.com/search/label/Stable%20updates
2. Download the source for that branch.
    git clone https://chromium.googlesource.com/chromium
3. Follow the environment setup for building.
    https://chromium.googlesource.com/chromium/src/+/master/docs/windows_build_instructions.md
    https://chromium.googlesource.com/chromium/src/+/master/docs/linux/build_instructions.md
4. Checkout the stable branch.
    gclient sync --with_branch_heads -r 58.0.3029.125

... then do some magic.
"""
