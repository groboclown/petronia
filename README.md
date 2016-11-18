# Petronia: A Python Windows Tiling Window Manager

#### Or: How We Retrained Windows To Be Useful

## Version 2 Is Out!

* [petronia-2.0-x64.zip](https://github.com/groboclown/petronia/releases/download/v1.2/petronia-2.0-x64.zip)
    (12.3 MB) Pre-bundled Python 3.5 and Petronia in a handy-dandy 64-bit executable.
    **For x64 Windows Computers Only**
* [petronia-2.0-x86.zip](https://github.com/groboclown/petronia/releases/download/v1.2/petronia-2.0-x86.zip)
    (11.6 MB) Pre-bundled Python 3.5 and Petronia in a handy-dandy executable.
    **For 32-bit and 64-bit Windows Computers**
* [petronia-2.0-src.zip](https://github.com/groboclown/petronia/archive/v2.0.zip) (< 1 MB)
    The source distribution, for users who want to see what's happening, and to use their
    own installed version of Python.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=SRBJnFcBuqI" target="_blank"><img src="http://img.youtube.com/vi/SRBJnFcBuqI/0.jpg" alt="Introduction to Petronia" width="240" height="180" border="10" /></a>

#### Manage Your Windows as Tiles

[Tiles](https://en.wikipedia.org/wiki/Tiling_window_manager) allow you
to divide up your monitors into distinct areas for your applications.

Petronia can carve up your screen into a variety of
rectangular shapes, while still accommodating floating windows for the
windows that work best in them, or overlapping full-screen windows.

Petronia also allows for different tile layouts per monitor layout, so
your laptop can look good by itself or docked with 3 additional monitors.

Really, it's up to you on how to setup your screen.

#### Easily Move Windows Between Tiles

Petronia gives you control.  With easy key strokes, you can move a window
between different tiles.  You can flip between windows within a tile.
You can change to a window within another tile.  *So many options!*

You can setup your keys however you like.  You can have a keystroke to
enter a window movement mode, or use hotkeys.

You can also prevent Windows from using the <kbd>&#x2756; Win</kbd> key and
use it for whatever you like.

#### Strip off Useless Borders to See More of What's Important

With a tile layout, and the availability of keys to perform the same actions,
the title bar and resize borders are useless wastes of space.  Remove them and
see more of what's actually important.

![Windows 8.1 Chrome](../master/docs/imgs/intellij-chrome-win8.1.png?raw=true)

*Windows 8.1 - Look at all that wasted screen space*

![Without Chrome](../master/docs/imgs/intellij-dechromed.png?raw=true)

*Windows 8.1 stripped of all the chrome - Oh mi gorsh I can see so much more of my work!*


## Current State of the Software

This program is very Alpha.  You run the program in a command shell,
which stays open and spews out logging information.  You configure the
software by writing Python code that sets up the configuration.

Additionally, this was written against 64-bit Windows 8.1.  I'm not sure if
it will work with other versions.  The Windows interfacing code has an
abstraction layer for working with different bit-ness and different versions,
but those haven't been widely tested.


## Running

You have two ways to run Petronia, either from source, or from a pre-bundled
executable.

See the [Getting Started Guide](docs/user-getting-started.md) for details
on how to run and setup your Petronia environment.

### I Don't Like Source Code

[Download the latest release](https://github.com/groboclown/petronia/releases)
for your platform (64-bit or 32-bit) and uncompress it to a directory on your
computer using a tool like 7-zip, or WinZip, or unzip.

From a command-prompt, you can run:

```cmd
> petronia example-configs\user_test_config.py
```

Or, drag a configuration file on top of the `petronia.exe` file.  Press
<kbd>&#x2756; Win</kbd><kbd>F4</kbd> to stop the program.


### I Like Pain

You'll need to ensure you're running Python 3.5 or higher.  This has been
tested on the python.org release version 3.5.2.  You'll need to install the
proper version of Python for your system.  If you're running a 64-bit OS,
then use the 64-bit Python.  If you are running a 32-bit OS, then use the
32-bit Python.

Then, download the source.  You'll need to configure the setup for your
computer; the example is `user_test_config.py`.  You can name the file
whatever you want, but it should live in the `src` directory.

Once you have your configuration setup, you just run in a cmd prompt:

```cmd
> set Path=(python 3.5.2 directory);%Path%
> cd (petronia dir)\src
> python -u -m petronia.cmd my_config_file.py
```

Press <kbd>&crarr; Enter</kbd> in the command window to stop the program.

*So bleeding edge!*
