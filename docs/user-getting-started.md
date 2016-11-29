# User Guide: Getting Started with Petronia


## Find the Stuff

First thing, you need to get the stuff that allows you to run Petronia.

1. Make sure you're running Windows.  Petronia is for Windows.
2. [Download the latest version of Petronia](https://github.com/groboclown/petronia/releases)
    for your computer.
     * Use the x64 version if you're running a 64-bit Windows.
     * Use the x86 version if you're running a 32-bit or 64-bit Windows.
        **Use this one if you're not sure.**


## Install the Stuff

Unzip the distribution into a place on your hard drive.


## Run the Stuff

Start up a command prompt.  You can do this through a bunch of ways, but
probably the easiest is <kbd>&#x2756; Win</kbd><kbd>r</kbd> to open the
**Run** dialog, type in `cmd` in the text field, and click **OK**.

Then, in the command prompt, enter:

```cmd
> cd (petronia directory)\src
> petronia-cli example-configs\user_test_config.yaml
```

The `user_test_config.yaml` argument tells Petronia where to find your
configuration file.

Press <kbd>&crarr; Enter</kbd> in the command prompt to stop it.


## What Just Happened?

If everything went well, Petronia tried to find the best match of your
computer's monitor resolution to what's in the configuration.  It then
shoved all your precious program windows into the first region.  It probably
also stripped off the borders and title bars, as well.  If things didn't
go well, then you're stuck staring at a Python stack trace.  *So it goes.
Those who are Great [open bugs](https://github.com/groboclown/petronia/issues).
Those who are Strong fix it.   The Best send push requests with the fixes.*

You'll also notice that your trusty <kbd>&#x2756; Win</kbd> key now doesn't
work how you're used to.  Instead, it gives you some control over your window
layout.

 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>&uarr;</kbd> - Move the currently active
    window to the [portal](user-configuration.md#splits-and-portals) *north* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>&darr;</kbd> - Move the currently active
    window to the [portal](user-configuration.md#splits-and-portals) *south* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>&larr;</kbd> - Move the currently active
    window to the [portal](user-configuration.md#splits-and-portals) *west* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>&rarr;</kbd> - Move the currently active
    window to the [portal](user-configuration.md#splits-and-portals) *east* of where it's at now.
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>Page Up</kbd> - Move the currently active window
    to the *next* [portal](user-configuration.md#splits-and-portals).
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>Page Down</kbd> - Move the currently active
    window to the *previous* [portal](user-configuration.md#splits-and-portals).
 * <kbd>&#x2756; Win</kbd> plus one of <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>,
    <kbd>&larr;</kbd>, <kbd>&rarr;</kbd><kbd>Page Up</kbd> or <kbd>Page Down</kbd> 
    changes the focused portal to another one adjacent to the currently active portal.
 * <kbd>&#x2756; Win</kbd><kbd>,/&lt;</kbd> Flip to the previous window in the
    current portal.
 * <kbd>&#x2756; Win</kbd><kbd>./&gt;</kbd> Flip to the next window in the
    current portal.
 * <kbd>&#x2756; Win</kbd><kbd>Tab</kbd> Minimize the currently active window. 
 * <kbd>&#x2756; Win</kbd><kbd>Launch App 1</kbd> Start a command prompt
    window.  This is usually the extra media button that looks like a
    computer.
 * <kbd>&#x2756; Win</kbd><kbd>Esc</kbd> Open up the Windows start menu.
    Since the Windows key has been preempted, this explicit remapping of the
    functionality becomes necessary.
 * <kbd>&#x2756; Win</kbd><kbd>~</kbd> Switch over to Windows Classic mode.
 * <kbd>&#x2756; Win</kbd><kbd>F11</kbd> Switch to Resize Mode.  This allows
    you to resize the active window using the keyboard.  Press
    <kbd>Esc</kbd> to return to the default hotkey mode.
 * <kbd>&#x2756; Win</kbd><kbd>Alt</kbd><kbd>F2</kbd> Reload the current
    configuration file.
 * <kbd>&#x2756; Win</kbd><kbd>&#x21e7; Shift</kbd><kbd>0-9</kbd> Save the
    current [portal](user-configuration.md#splits-and-portals) as associated
    with this number key, for quick re-focusing.
 * <kbd>&#x2756; Win</kbd><kbd>0-9</kbd> Focus on the top window in the
    [portal](user-configuration.md#splits-and-portals) that was previously
    saved with the
    <kbd>&#x2756; Win</kbd><kbd>&#x21e7; Shift</kbd><kbd>0-9</kbd> hotkey.
 * <kbd>&#x2756; Win</kbd><kbd>P</kbd> Start up a new command prompt with a
    blue background, white text, and in the root directory.
 * <kbd>&#x2756; Win</kbd><kbd>E</kbd> Start Windows Explorer to browse
    your files.
 * <kbd>&#x2756; Win</kbd><kbd>F4</kbd> This is supposed to quit Petronia.
    If you started it with `petronia-cli`, this will partially stop
    the application, but it won't fully terminate.  If you instead ran
    `petronia`, then this should stop the application.

If you press <kbd>&#x2756; Win</kbd><kbd>~</kbd>, the keyboard shortcuts will
switch over to the Windows Classic mode.  Here, you can use the Windows keys
as Microsoft wants you to.  This means that the only special key sequence that
Petronia recognizes now is another <kbd>&#x2756; Win</kbd><kbd>~</kbd> to put
it back into the default mode.

If you press <kbd>&#x2756; Win</kbd><kbd>F11</kbd>, Petronia switches to
resize mode.  In this mode, Petronia captures all of your key presses (except
for some critical Windows ones).  You can use the arrow keys (and a few
others) to resize the currently active window.  When you're finished
resizing, press <kbd>&crarr; Enter</kbd> or <kbd>Esc</kbd> to end resize mode,
and return to the default mode.


## Where To Go From Here

At this point, I bet you just can't wait to dive into the configuration to
get your computer working how you want.

[Go for it.](user-configuration.md)  Start writing your own configuration now.
That's what I would do.

You'll have to shut down Petronia and restart it with the new configuration,
and restart it for each update.  *There is a secret mojo sauce that allows
you to reload the configuration on the fly, but you'll have to either edit
the current file, or tell the configuration file about the other file.*

Additionally, you can switch to the standard executable:

```cmd
> petronia user_test_config.yaml
```

In this mode, you can simply press <kbd>&#x2756; Win</kbd><kbd>F4</kbd>
(or whichever key combination you have mapped to the `quit` command) to stop
the program.  *Note that this is experimental, and issues have come up where
to really stop it you have to kill the Python process.  So, use at your own
risk.*
