# Configuration

You configure Petronia through a Python script that provides a
`load_config()` function, which in turn creates a `petronia.config.Config`
object.  It's not simple, and you need to know a bit about programming.  But,
oh, *the power!*


## The Example Configurations

### `user_test_config.py`

To get you started, take a gander at the example config file,
[user_test_config.py](../src/user_test_config.py).  This guy sets
up the configuration in several parts, the [layout](#layout-configuration),
the [applications](#application-configuration), the
[hotkeys](#hotkey-configuration), and the [chrome](#chrome-configuration).

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

The [no_chrome_config.py](../src/no_chrome_config.py) shows an example
where all you care about is removing the nasty Chrome off select windows.  You
still have full access to all the native Windows commands.

Of specific interest to this configuration is how it detects applications for
exclusion from the chrome stripping.

### `simple_config.py`

The [simple_config.py](../src/simple_config.py) provides an extremely simple, but
not too useful, configuration that strips off the chrome and registers a quit
key.  It's about as simple as you can get.


## Configuration Parts

There are several sections of configuration that you can configure.

* [Component Configuration](#component-configuration) - Defines which
    Petronia components will be active.
* [Layout Configuration](#layout-configuration) - How the screen is split up
    for different monitors.
* [Chrome Configuration](#chrome-configuration) - How the windows are
    modified, and some other system-wide settings for the appearance of
    windows.
* [Hotkey Configuration](#hotkey-configuration) - Registered key modes, and
    actions associated with keys.
* [Application Configuration](#application-configuration) - Application
    specific configuration, to select how different windows work with the
    chrome and layout configurations.



### Component Configuration

Setting up the component configuration allows for selecting individual parts
of the Petronia system to activate.  This is only loaded once, for the initial
configuration file at start time.

*At the moment there is nothing to be done here.*  This will eventually allow
for pluggable behaviors.


### Layout Configuration

Layouts are defined per monitor configuration.  Normally, you'd want one
top-level layout per monitor, but if you need more control, you can use a
single layout to cover all your screens - *but don't expect it to be nice.*

Layouts are contained in a `DisplayWorkGroupsConfig`.  This allows you to
define a [work group](#work-group-layouts) for each [monitor setup](#monitors).

```python
from petronia import config

layouts_by_display = config.DisplayWorkGroupsConfig(groups=[
    # First monitor group
    {
        # Monitors; optional if you use the same monitor setup and resolution everywhere.
        'monitors': [config.MonitorResConfig(1024, 768), config.MonitorResConfig(4096, 1024)],
        'workgroup': config.WorkGroupConfig({
            # The layout to use at startup.
            'default': [
                # First layout is assigned to first monitor
                config.LayoutConfig('primary', 'split-layout', config.ORIENTATION_HORIZONTAL, [
                    config.ChildSplitConfig(2, config.LayoutConfig('main', 'portal', None, None)),
                    config.ChildSplitConfig(1, config.LayoutConfig('main-right', 'portal', None, None)),
                ]),
                
                # Second layout is assigned to second monitor
                config.LayoutConfig('secondary', 'portal', None, None),
            ]
        })
    },
])
```


#### Monitors

To understand your monitor layout, for use in the configuration, you can run:

```cmd
> python -m petronia.detect_monitors
```

This tells you how you can specify your monitors in the configuration file.
Note that the order of the monitors is very important.  The first appearing
monitor maps to the first [top-level split](#top-level-splits).

Petronia will attempt to find the best matched monitor layout in the configuration
for your current monitor arrangement.

If you only have one setup for your monitors, then you can omit this section.
It's only important if you find yourself changing multiple resolutions
regularly, or move between locations where you have different monitor setups.


#### Work Group Layouts

You can associate multiple layout configurations for a single
monitor setup.  When Petronia starts up, it uses the layout named `default`,
unless you specified one at the command line.

You can swap to a different layout within the current work group by creating a
hotkey that runs the [layout-name](user-commands.md#change-layout-layout_name)

Each layout should have one [top level split](#top-level-splits) per monitor,
or one top level split for all your monitors (which isn't supported well).


#### Top Level Splits

At the top level of a work group, you define the top level splits.  These are
just layout configs, not enclosed in any child split.  These will be assigned
to one per monitor.  If you have just one top-level split defined, then it
will cover all your monitors.

Within the top level split, you can configure your
[splits and portals](#splits-and-portals).


#### Splits and Portals

Petronia uses a *split layout* to cut a bit of the screen along a direction.
A *Horizontal split* creates splits left-to-right, each one being a sub-split
or portal.  A *Vertical split* creates splits top-to-bottom, each one being a
sub-split or portal.

Each sub-split has a relative *size*.  If there are two sub-splits, each with
size 1, then they each take up half of the parent.  If the first has a size 2,
and the second a size 1, then the first takes up two-thirds of the parent.

Portals are places where the actual application Windows are put.  These are
the end nodes of the layout tree, and can't be split.

You define a layout section like:

```python
from petronia import config

layout = config.LayoutConfig('right', 'split-layout', config.ORIENTATION_VERTICAL, [
    config.ChildSplitConfig(5, config.LayoutConfig('top', 'portal', None, None)),
    config.ChildSplitConfig(1, config.LayoutConfig('bottom', 'portal', None, None)),
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

![1.2-1-1 Split](../../master/docs/imgs/split1.png?raw=true)

In this example, the top level is split 3 columns, and the left-hand
side is split into two vertical slices.

```python
from petronia import config

layout = config.LayoutConfig('screen', 'split-layout', config.ORIENTATION_VERTICAL, [
    config.ChildSplitConfig(1, config.LayoutConfig('left-parent', 'split-layout', config.ORIENTATION_HORIZONTAL, [
        # 1/4 of the left-hand side
        config.ChildSplitConfig(1, config.LayoutConfig('left-top: region 1', 'portal', None, None)),
        
        # 3/4 of the left-hand side
        config.ChildSplitConfig(3, config.LayoutConfig('left-bottom: region 2', 'portal', None, None)),
    ])),
    config.ChildSplitConfig(1, config.LayoutConfig('middle: region 3', 'portal', None, None)),
    config.ChildSplitConfig(1, config.LayoutConfig('right: region 4', 'portal', None, None)),
])
```


#### Splits and Portals of Size 0

If you use a size of 0, then this is considered a "full" split, and it
takes up the size of the parent split.

This allows for having a side-bar window that you tab to on occasion, but
normally want to keep minimized.

If you set a size "0" portal within a top-level layout, It acts as an
alternative to maximizing applications.


#### Testing Your Layout

To test out your layout configuration, to see how Petronia will split up
the screens based on the layout definition it finds for your monitors,
you can run:

```cmd
> python -m petronia.check_layout (configuration file name) (layout name)
```

(layout name is optional)

This will display the best-matched work group's layout, broken down by pixels.


### Application Configuration

You may wish to have specific applications loaded in certain portals. Also,
some applications may not work nice when displayed without borders,
or if assigned to a portal.  The Application Configuration allows you to set
up this association.

To check how Petronia recognizes your applications, you can run

```cmd
> python -m petronia.detect_apps
```

This will list out each visible window for the running applications, and give
you valuable insight into how to distinguish it from other windows.

```python
from petronia import config

applications = config.ApplicationListConfig([
    config.ApplicationChromeConfig(is_managed_chrome=False, is_tiled=False, app_matchers=[
        config.AppMatcher(class_name_re=r'#\d+', title_re=r'\d+ reminder\(s\)', exec_path='outlook.exe'),
    ])
])
```

This registers a single *chrome configuration*, which defines how Petronia
will act upon the matching application window.  In this case, the
`is_matched_chrome` value is `False`, so it won't have the title bar
and resize borders be affected by the
[chrome configuration](#chrome-configuration).  Additionally, `is-tiled` is
set to `False`, so it also will not be managed within the
[portal layouts](#splits-and-portals), and won't react to portal movement
key actions.


#### Matching an Application Window

An application configuration relies upon a `config.AppMatcher` instance to
define whether a given application window matches the configuration.

With an app matcher, you can define the following attributes:

* `match_returns`: By default, the matcher will report itself as a match.
    If, instead, you want to explicitly omit the matched application, set
    this value to `False`.
* `title`: A string that matches the application window's title, ignoring
    capitalization.
* `title_re`: A Python regular expression that matches the application
    window's title.  Can either be a proper compiled (`re.compile`)
    regular expression, or a string of the regular expression.
* `module_path`: The path of the module that controls the window.
    You can specify "MyModule.dll", and it will match for any module
    that has the "MyModule.dll" file, regardless of its path.
* `module_path_re`: A Python regular expression (string or re) version of the
    path of the module that controls the window.
* `exec_path`: The path of the executable that created the window.
    You can specify "MyCommand.exe", and it will match for any executable
    that has the "MyCommand.exe" file, regardless of its path.
* `exec_path_re`: A Python regular expression (string or re) of the path of
    the executable that created the window.
* `class_name`: The specific class name of the window.  Each window generally
    has its own class name, so you can distinguish different windows that
    came from the same executable.
* `class_name_re`: A Python regular expression (string or re) of the
    `class_name`.

To find the class name, module path, and executable path, for all visible
windows, run:

```cmd
> python -m petronia.detect_apps
```


#### Configuring for Chrome and Position

In the examples above, the configuration controls how some application
works with the window decoration and inclusion in the tiling system through
the `config.ApplicationChromeConfig`.

Additionally, you can control in which portal a window should be placed
at layout load time with `config.ApplicationPositionConfig`.

```python
from petronia import config

config.ApplicationPositionConfig(
    portal_names=['left', 'main'],
    app_matchers=[
        config.AppMatcher(exec_path='firefox.exe'),
        config.AppMatcher(exec_path='chrome.exe'),
        config.AppMatcher(exec_path='explorer.exe'),
        config.AppMatcher(exec_path='outlook.exe'),
    ]
)
```

In this position configuration, the list of matched windows will be placed
into the `left` portal, if it exists.  If the `left` portal isn't in the
current layout, then the `main` portal is used.


#### Multiple Matching Applications

Application configurations are *ordered*.  That is, the first Application
configuration to match an application window will have its setup be used
for that window.

Because of this, you should try to organize your application configurations
from *most specific* to *least specific*.



### Hotkey Configuration

*For reference:*

* [The full list of supported Petronia Commands](user-commands.md)
* [How to name your keys](user-keys.md)

The hotkey configuration section allows you to map Petronia commands to
keyboard shortcuts.  The hotkey configurations are *modal*, meaning that
you can have multiple keyboard configurations, and switch between them.

To better understand how Petronia maps your key stokes, you can run
 
```cmd
> python -m petronia.detect_keys
```

to start an application that will monitor your keys, and tell you how to
reference it in your configuration.  Press <kbd>&crarr; Enter</kbd> to
stop the application.


#### `parse_hotkey_mode_keys`

The "hotkey mode" allows for Petronia to capture a few select keywords out
of your typing, regardless of which window has focus, to trigger a Petronia
command.

You specify the command as a key to command mapping.  Each command is a list
in the form `(command name, argument 1, argument 2, ...)`

```
"key-combo": ["command", "arg1"],
```

Key combos are strings of key names, connected with a "+" to require the
keys to be down at once, or "," to string different keystrokes together.

So, you could have

```
"alt + f1": ["cmd", "superhelp.exe"]
```

to run the `superhelp.exe` application when the keys <kbd>Alt</kbd><kbd>F1</kbd>
are held down together.

```
"lshift + twiddle , f12": ["open-start-menu"] 
```

to force the task bar Start Menu to open when you hold down the left
<kbd>&#x21e7; Shift</kbd> key and the <kbd>`</kbd> key, followed by the
<kbd>F12</kbd> key.


##### Preventing Windows From Using the Windows Key

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


#### `parse_simple_mode_keys`

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


### Chrome Configuration

You can configure the general setup for each application, as well as some
global configuration options, in the `ChromeConfig`.

#### Global Settings

These settings affect all applications running in the system.

* **border_width** Width of the grabbable resize border.
* **border_padding** Space between the application area and the resize border.
  *Windows Visa and above only.*
* **scrollbar_width** Width for vertical scrollbars.
* **scrollbar_height** Height for horizontal scrollbars.


#### Per Application Settings

For the [applications](#application-configuration) that opt-in to being
managed by Chrome, you can dictate how their chrome will appear.

* **has_title** `True` or `False`, to strip off the title bar and its
  buttons.  Note that even with this removed, you can still open the system
  menu for the window by pressing <kbd>Alt</kbd><kbd>Space</kbd>.  This
  gives you quick access to the minimize, maximize, restore, close, and
  (sometimes) resize actions.
* **has_resize_border** `True` or `False`, to remove the fat resize border.

