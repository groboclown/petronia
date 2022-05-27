# Petronia: A Cross-Platform Tiling Window Manager

**This is the v3 branch, which is still being developed.**

[![dev branch build](https://travis-ci.com/groboclown/petronia.svg?branch=windows-handler)](https://travis-ci.com/github/groboclown/petronia) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![license: MIT](https://img.shields.io/badge/license-MIT-brightgreen)](https://github.com/groboclown/petronia) ![platforms: win-64 & linux-64](https://img.shields.io/badge/platforms-win--64%20%7C%20linux--64-informational)

## V3 Status

* 2022-May - Development is back!
* Petronia on Windows is workable.  Not great.
* Petronia on X11 has started.  It can become the window manager, but that's about it so far.
* Petronia on Wayland is planned.
* Once minimal support for X11 is in place, the [TODO](TODO.md) list will be attacked.

Running V3:

To run V3, you'll need to download the source and checkout the `dev` branch.  Then, depending on your operating system, run:

* Windows (only tested on Windows 10, but should be usable all the way back to Windows 2000)
  1. Ensure Python 3.9 or later is installed.
  2. Open a cmd prompt.
  3. `cd (petronia source directory)`
  4. `python -m venv .venv`
     * If the python program isn't found, you'll need to use the Python install path.
  5. `python -m pip install -r bin/requirements`
  6. `.venv\Scripts\activate.bat`
  7. `windows-test.bat`
* Linux with X11
  1. Ensure Python 3.9 or later is installed, along with libxcb and Xephyr.
  2. `cd (petronia source directory)`
  3. `python3 -m venv .venv`
  4. `source .venv/bin/activate`
  5. `./linux-x11-test.sh --xephyr 800x600 :1`
    * By adding the `--xephyr 800x600 :1`, you will launch an X server inside an X server to allow for testing out Petronia.


## Previous Release: v2.2

* [petronia-2.2-x64.zip](https://github.com/groboclown/petronia/releases/download/v2.2/petronia-2.2-x64.zip)
    (12.4 MB) Pre-bundled Python 3.5 and Petronia in a handy-dandy 64-bit executable.
    **For x64 Windows Computers Only**
* [petronia-2.2-x86.zip](https://github.com/groboclown/petronia/releases/download/v2.2/petronia-2.2-x86.zip)
    (11.7 MB) Pre-bundled Python 3.5 and Petronia in a handy-dandy executable.
    **For 32-bit and 64-bit Windows Computers**
* [petronia-2.2-src.zip](https://github.com/groboclown/petronia/archive/v2.2.zip) (< 1 MB)
    The source distribution, for users who want to see what's happening, and to use their own installed version of Python.

## v2.2 Advertisement Video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=SRBJnFcBuqI" target="_blank"><img src="http://img.youtube.com/vi/SRBJnFcBuqI/0.jpg" alt="Introduction to Petronia" width="240" height="180" border="10" /></a>


#### Manage Your Windows as Tiles

[Tiles](https://en.wikipedia.org/wiki/Tiling_window_manager) allow you to divide up your monitors into distinct areas for your applications.

Petronia can carve up your screen into a variety of rectangular shapes, while still accommodating floating windows for the windows that work best in them, or overlapping full-screen windows.

Petronia also allows for different tile layouts per monitor layout, so your laptop can look good by itself or docked with 3 additional monitors.

Really, it's up to you on how to setup your screen.

#### Easily Move Windows Between Tiles

Petronia gives you control.  With easy key strokes, you can move a window between different tiles.  You can flip between windows within a tile.
You can change to a window within another tile.  *So many options!*

You can setup your keys however you like.  You can have a keystroke to enter a window movement mode, or use hotkeys.

You can also prevent Windows from using the <kbd>&#x2756; Win</kbd> key and use it for whatever you like.

#### Strip off Useless Borders to See More of What's Important

With a tile layout, and the availability of keys to perform the same actions, the title bar and resize borders are useless wastes of space.  Remove them and see more of what's actually important.

![Windows 8.1 Chrome](../docs/imgs/intellij-chrome-win8.1.png?raw=true)

*Windows 8.1 - Look at all that wasted screen space*

![Without Chrome](../docs/imgs/intellij-dechromed.png?raw=true)

*Windows 8.1 stripped of all the chrome - Oh mi gorsh I can see so much more of my work!*


## v3.0 Information


### Current State of the Software

v3.0 is in an "alpha" stage of development.  It misses key features that prevents it from creating a working environment.

If you find issues with your environment, please [file a bug](https://github.com/groboclown/petronia/issues), and be sure to include which version of Windows you're using, and whether it's 32-bit or 64-bit.
