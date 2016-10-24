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
> cd (Cormorant dir)\manager\src
> python -u -m petronia.main my_config_file.py
```

Press <kbd>Enter</kbd> in the cmd window to stop the program.

## The Example Config

The example config file does several things.

* Disables the Windows Shell from interpreting the <kbd>Win</kbd> key.
    * This means the standard Windows hotkeys, like <kbd>win</kbd><kbd>d</kbd>
        (show desktop), <kbd>win</kbd><kbd>r</kbd> (run command dialog), and
        so on, won't be available.
* Strips off the borders from the Windows, except for Firefox, Chrome, and
  Outlook.
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


## Future Notes if this ever becomes a full-on Shell program

To close Windows Explorer as the current shell:

1. Press <kbd>Ctrl</kbd><kbd>Shift</kbd> while right-clicking on the task bar.
       This will bring up a context menu that lets you stop Windows Explorer.
2. From the context menu, select **Exit Explorer**.

To restart Windows Explorer as the current shell:

1. Stop Cormorant.
2. Press <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Del</kbd>, select "Task Manager".
3. From Task Manager, select **File** -> **Run new task**
4. From this new Create New Task dialog, enter "explorer", and click **OK**. 
