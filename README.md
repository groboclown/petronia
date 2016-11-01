# Petronia: A Python Windows Tiling Window Manager

#### Or: How We Removed Useless Space From Our Windows and Used All That Extra Screen Space To Do Important Things 

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
between different tiles.

You can setup your keys however you like.  You can have a keystroke to
enter a window movement mode, or use hotkeys.

You can also prevent Windows from using the <kbd>&#x2756; Win</kbd> key and
use it for whatever you like.

#### Strip off Useless Borders to See More of What's Important

With a tile layout, and the availability of keys to perform the same actions,
the title bar and resize borders are useless wastes of space.  Remove them and
see more of what's actually important.

<img src="docs/imgs/intellij-chrome-win8.1"></img>
*Windows 8.1 - Look at all that wasted screen space*

<img src="docs/img/intellij-dechromed.png"></img>
*Oh mi gorsh I can see so much more of my work!*


## Current State of the Software

This program is very Alpha.  You run the program in a command shell,
which stays open and spews out logging information.  You configure the
software by writing Python code that sets up the configuration.

Additionally, this was written against 64-bit Windows 8.1.  I'm not sure if
it will work with other versions.  The Windows interfacing code has an
abstraction layer for working with different bit-ness and different versions,
but those haven't been widely tested.


## Running

You'll need to ensure you're running Python 3.5 or higher.  This has been
tested on the python.org release version 3.5.2.  You'll need to install the
proper version of Python for your system.  If you're running a 64-bit OS,
then use the 64-bit Python.  If you are running a 32-bit OS, then use the
32-bit Python.

Then, download the source.  You'll need to configure the setup for your
computer; the example is `user_test_config.py`.  You can name the file
whatever you want, but it should live in the `manager/src` directory.

Once you have your configuration setup, you just run in a cmd prompt:

```
> set Path=(python 3.5.2 directory);%Path%
> cd (petronia dir)\manager\src
> python -u -m petronia.main my_config_file.py
```

Press <kbd>&#x2756; Win</kbd><kbd>F4</kbd> in the cmd window to stop the
program.

*So bleeding edge!*

See the [Getting Started Guide](docs/user-getting-started.md) for details
on how to run and setup your Petronia environment.
