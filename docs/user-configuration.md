# Configuration

You configure Petronia through a Python script that creates a `Config` object.
It's not simple, and you need to know a bit about programming.  But, oh,
*the power!*

## The Example Config

To get you started, take a gander at the example config file,
[user_test_config.py](../manager/src/user_test_config.py).  This guy sets
up the configuration in several parts, the [layout](#Layout Configuration),
the [applications](#Application Configuration), the
[hotkeys](#Hotkey Configuration), and the [chrome](#Chrome Configuration).

For the layout, it specifies 3 monitor setups.  Each one is for a different
configuration of monitors - the normal laptop screen, the laptop docked with
2 monitors, and a remote desktop screen.  Each one of these configurations
can have multiple, named *work groups*, though for now it only has one per
monitor setup.  The work group defines how the screen is split up.

The applications define which applications should be excluded from updates.
Some programs, like Chrome or Firefox, do not work right when their borders
and title bar are removed.  Some dialogs, like the Outlook Reminder, don't
work right when put into a tile.

The hotkey section lets you setup different hotkey *modes*, which each have
their own key bindings.

The chrome config defines what to do when an application has been selected
for a strip down.  You can give it a border, or select if you want the
title bars removed.


## Layout Configuration

Layouts are defined per monitor configuration.  Normally, you'd want one
top-level layout per monitor, but if you need more control, you can use a
single layout to cover all your screens - *but don't expect it to be nice.*

### Monitors

To understand your monitor layout, for use in the configuration, you can run:

```(cmd)
> python -m petronia.detect_monitors
```

This tells you how you can specify your monitors in the configuration file.
Note that the order of the monitors is very important.  The first appearing
monitor maps to the first [top-level split](#Top Level Splits).


### Work Groups

You can associate multiple *work groups* of layout configurations for a single
monitor setup.  Eventually, Petronia will allow for switching between layout
work groups, but for now, it just uses the default.


### Splits and Portals

Petronia uses a *split layout* to cut a bit of the screen along a direction.
A *Horizontal split* creates splits left-to-right, each one being a sub-split
or portal.  A *Vertical split* creates splits top-to-bottom, each one being a
sub-split or portal.

Each sub-split has a relative *size*.  If there are two sub-splits, each with
size 1, then they each take up half of the parent.  If the first has a size 2,
and the second a size 1, then the first takes up two-thirds of the parent.

Portals are places where the actual application Windows are put.  These are
the end nodes of the layout tree, and can't be split.

You define a layout like:

```(python)
config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
    config.ChildSplitConfig(5, config.LayoutConfig('right-top', 'portal', None, None)),
    config.ChildSplitConfig(1, config.LayoutConfig('right-bottom', 'portal', None, None)),
])
```

This gives the layout the name "right", defines it as a "split-layout", which
splits the region from top-to-bottom (vertically).  It then defines 2 child
splits, the first with a size 5 defined as a portal, and the second as a
size 1 portal.  Because there are two children, with their sizes totalling 6,
the first portal will take up 5/6 of the space, and the second 1/6.


### Top Level Splits

At the top level of a work group, you define the top level splits.  These are
just layout configs, not enclosed in any child split.  These will be assigned
to one per monitor.  If you have just one top-level split defined, then it
will cover all your monitors.


### Testing Your Layout

To test out your layout configuration, to see how Petronia will split up
the screens based on the layout definition it finds for your monitors,
you can run:

```(cmd)
> python -m petronia.check_layout (work group name)
```


## Application Configuration

To check how Petronia recognizes your applications, you can run

```(cmd)
> python -m petronia.detect_apps
```

This will list out each visible window for the running applications, and give
you valuable insight into how to distinguish it from other windows.


## Hotkey Configuration

The hotkey configuration section allows you to map Petronia commands to
keyboard shortcuts.  The hotkey configurations are *modal*, meaning that
you can have multiple keyboard configurations, and switch between them.

To better understand how Petronia maps your key stokes, you can run
 
```(cmd)
> python -m petronia.detect_keys
```

to start an application that will monitor your keys, and tell you how to
reference it in your configuration.  Whoops.  You just started it.  Now
you'll have to kill it through task manager.


### `parse_hotkey_mode_keys`

The "hotkey mode" allows for Petronia to capture a few select keywords out
of your typing, regardless of which window has focus, to trigger a Petronia
command.

You specify the command, one per line, in an awkward
fashion:

```
key combo => command
```

Key combos are strings of key names, connected with a "+" to require the
keys to be down at once, or "," to string different keystrokes together.

So, you could have

```
alt + f1 => cmd superhelp.exe
```

to run the `superhelp.exe` command when the keys <kbd>Alt</kbd><kbd>F1</kbd>
are held down together, and

```
lshift + twiddle , f12 => win+esc => open-start-menu 
```

to force the task bar Start Menu to open when you hold down the left shift key
and the <kbd>`</kbd> key, followed by the <kbd>F12</kbd> key.


### `parse_simple_mode_keys`




## Chrome Configuration


## Old Doc Stuff

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
matcher) to an ApplicationConfig.  To test out the names of the applications,
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

