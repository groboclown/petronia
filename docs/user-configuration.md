# Configuration

You configure Petronia through a Python script that creates a `Config` object.
It's not simple, and you need to know a bit about programming.  But, oh,
*the power!*

## The Example Configurations

### `user_test_config.py`

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

### `no_chrome_config.py`

The [no_chrome_config.py](../manager/src/no_chrome_config.py) shows an example
where all you care about is removing the nasty Chrome off select windows.  You
still have full access to all the native Windows commands.


## Layout Configuration

Layouts are defined per monitor configuration.  Normally, you'd want one
top-level layout per monitor, but if you need more control, you can use a
single layout to cover all your screens - *but don't expect it to be nice.*

### Monitors

To understand your monitor layout, for use in the configuration, you can run:

```cmd
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

```python
from petronia import config

layout = config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
    config.ChildSplitConfig(5, config.LayoutConfig('right-top', 'portal', None, None)),
    config.ChildSplitConfig(1, config.LayoutConfig('right-bottom', 'portal', None, None)),
])
```

This gives the layout the name "right", defines it as a "split-layout", which
splits the region from top-to-bottom (vertically).  It then defines 2 child
splits, the first with a size 5 defined as a portal, and the second as a
size 1 portal.  Because there are two children, with their sizes totalling 6,
the first portal will take up 5/6 of the space, and the second 1/6.

The two split types are `config.ORIENTATION_VERTIAL` for a top-to-bottom
splitting of windows, and `config.ORIENTATION_HORIZONTAL` for a left-to-right
splitting of windows.


### Top Level Splits

At the top level of a work group, you define the top level splits.  These are
just layout configs, not enclosed in any child split.  These will be assigned
to one per monitor.  If you have just one top-level split defined, then it
will cover all your monitors.


### Testing Your Layout

To test out your layout configuration, to see how Petronia will split up
the screens based on the layout definition it finds for your monitors,
you can run:

```cmd
> python -m petronia.check_layout (work group name)
```


## Application Configuration

To check how Petronia recognizes your applications, you can run

```cmd
> python -m petronia.detect_apps
```

This will list out each visible window for the running applications, and give
you valuable insight into how to distinguish it from other windows.


## Hotkey Configuration

*For reference:*

* [The full list of supported Petronia Commands](user-commands.md)
* [How to name your keys](keys.md)

The hotkey configuration section allows you to map Petronia commands to
keyboard shortcuts.  The hotkey configurations are *modal*, meaning that
you can have multiple keyboard configurations, and switch between them.

To better understand how Petronia maps your key stokes, you can run
 
```cmd
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

to force the task bar Start Menu to open when you hold down the left
<kbd>&#x21e7; Shift</kbd> key and the <kbd>`</kbd> key, followed by the
<kbd>F12</kbd> key.


#### Preventing Windows From Using the Windows Key

In the hotkey mode, you can tell Petronia to have Windows ignore the
<kbd>&#x2756; Win</kbd> key.  This means tapping <kbd>&#x2756; Win</kbd>
won't trigger the start menu to pop up.  It also means that a few of the
nice [Windows key shortcuts](https://en.wikipedia.org/wiki/Windows_key),
like <kbd>&#x2756; Win</kbd><kbd>R</kbd> to open the run dialog, are not
available.  You'll need to provide your own hotkey actions to provide an
equivalent function.

Note that a few key sequences will always be recognized by Windows, and
can't be overridden or disabled.  This includes
<kbd>&#x2756; Win</kbd><kbd>L</kbd> (lock screen).


### `parse_simple_mode_keys`

With the simple mode, Petronia captures all your Windows input.  This allows
you to have a mode that doesn't require you to hold down a key the whole time.
This will become more useful when the layout management mode is implemented.

You are expected to include a change mode command key (say, <kbd>Esc</kbd>)
to revert back to standard mode.  Without this, you'll be suck in a
non-keyboard Windows computer, and you'll have to stop Petronia through the
Task Manager using your mouse.  *Yuck!*

This mode only recognizes single keys per command.  It doesn't allow for
combo keys like <kbd>&#x21e7; Shift</kbd><kbd>F1</kbd> or
<kbd>&#x2732; Ctrl</kbd><kbd>&#x1f507; Mute</kbd>.


## Chrome Configuration

You can configure the general setup for each application, as well as some
global configuration options, in the `ChromeConfig`.

### Global Settings

These settings affect all applications running in the system.

* **border_width** Width of the grabbable resize border.
* **border_padding** Space between the application area and the resize border.
  *Windows Visa and above only.*
* **scrollbar_width** Width for vertical scrollbars.
* **scrollbar_height** Height for horizontal scrollbars.


### Per Application Settings

For the [applications](#Application Configuration) that opt-in to being
managed by Chrome, you can dictate how their chrome will appear.

* **has_title** `True` or `False`, to strip off the title bar and its
  buttons.  Note that even with this removed, you can still open the system
  menu for the window by pressing <kbd>Alt</kbd><kbd>Space</kbd>.  This
  gives you quick access to the minimize, maximize, restore, close, and
  (sometimes) resize actions.
* **has_resize_border** `True` or `False`, to remove the fat resize border.


## Old Doc Stuff


## Configuration Options

The configuration is a Python file that provides the function `load_config()`,
which returns a `petronia.config.Config` object.  Configuration isn't
straightforward (yet), so here's some guides to get it to do what you want.

### Discover Process, Module, and Class Names

There are some applications that just don't do well without the title bar.
For those applications, you can add a regular expression (or exact string
matcher) to an ApplicationConfig.  To test out the names of the applications,
you can run the `petronia.discover_apps` application.

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

