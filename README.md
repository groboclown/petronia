# Petronia: A Python Windows Tiling Window Manager

A program that manages your Windows windows in a tiling manner.

It can strip off the excess borders and title from windows, and arrange them
in *tiles*, that is, non-overlapping views.

You can manage your tiles on a per monitor configuration.  If you have a
laptop that you dock, each configuration (docked, non-docked) will have its
own layout.  If you remote desktop into your computer, the remote desktop
login can have its own layout.

The keyboard shortcuts are *global* and *modal*.  When you enter a shortcut,
it will run regardless of which window is active.  You can switch between
different input modes, which allows for the same keystrokes to act
differently, and some modes can be setup to be the exclusive input for the
system - they don't allow keys to be used by any other application.


## Current State of the Software

This program is currently very Alpha.  You run the program in a command shell,
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

Press <kbd>Enter</kbd> in the cmd window to stop the program.

## The Example Config

The example config file does several things.

* Disables the Windows Shell from interpreting the <kbd>Win</kbd> key.
    * This means the standard Windows hotkeys, like <kbd>win</kbd><kbd>d</kbd>
        (show desktop), <kbd>win</kbd><kbd>r</kbd> (run command dialog), and
        so on, won't be available.
* Strips off the borders from the Windows, except for Firefox, Chrome,
    Explorer, and Outlook.
* Splits the screen into tiles, depending on the monitor size.
* Installs key handlers.
    * <kbd>win</kbd><kbd>esc</kbd>: show the start menu.
    * <kbd>win</kbd><kbd>left</kbd> (or any other arrow key): move the
        currently focused window to another tile.  *It can be hard to
        tell, at times, which window has the focus.*

Even though the chrome is gone from windows, you can still use
<kbd>alt</kbd><kbd>space</kbd> to open the window's system menu, and
select Minimize, Restore, Maximize, or Close.

Likewise, you can use <kbd>alt</kbd><kbd>tab</kbd> to move between windows.


## Configuration Options

The configuration is a Python file that provides the function `load_config()`,
which returns a `petronia.config.Config` object.  Configuration isn't
straightforward (yet), so here's some guides to get it to do what you want.

### Discover Process, Module, and Class Names

There are some applications that just don't do well without the title bar.
For those applications, you can add a regular expression (or exact string
matcher) to the ApplicationConfig.  To test out the names of the applications,
you can run the `petronia.discover_apps` application.

### Monitor Order and Size

To determine your current monitor configuration, you can run the
`petronia.detect_monitors` application.  It will output the lines needed
for your configuration to match the current monitor setup.

### Layouts

The next big thing to configure is the "feel" of your layout.  Your layout
has 2 general items: *splits* and *portals*.  Portals are where the windows
end up; these are the "sink nodes" in the layout graph.  The splits are
how the screen is divided up; splits can be vertical or horizontal.

* Portal - the end node of a split.  Use a `None` layout to define a
    portal.
* Horizontal split - Splits the layout area into horizontal bars, like layers
    on a cake.
* Vertical split - splits the screen into vertical bars.

Each child in a layout has a relative "size".  If there are two splits, each
with a size of 1, then they each take up half the screen.  If one has a size
of 2, and the other a size of 1, then the 2 will take up 2/3 of the area,
and the other will take up 1/3 of the area.

If you set a child size of "0", then it will be considered "floating", and
will take up the size of the entire owning layout.  This is how you can
create a full screen layout, or an overlapping side-bar.


## Future Notes if this ever becomes a full-on Shell program

To close Windows Explorer as the current shell:

1. Press <kbd>Ctrl</kbd><kbd>Shift</kbd> while right-clicking on the task bar.
       This will bring up a context menu that lets you stop Windows Explorer.
2. From the context menu, select **Exit Explorer**.

To restart Windows Explorer as the current shell:

1. Stop Petronia.
2. Press <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Del</kbd>, select "Task Manager".
3. From Task Manager, select **File** -> **Run new task**
4. From this new Create New Task dialog, enter "explorer", and click **OK**. 
