# Configuration

You can configure Petronia through json or yaml files.  This document
walks you through the yaml configuration, but it's straightforward to
do the same thing in json.

If you really want control, you can [write the configuration in
Python](user-configuration-py.md).


## The Example Configurations

### `border_config.yaml`

To get you started, take a gander at a configuration file that sets up
your windows without titles, but with borders:
[border_config.yaml](../src/border_config.yaml).  This guy sets
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

### `no_border_config.yaml`

The [no_border_config.yaml](../src/no_border_config.yaml) is very similar to
the [border_config.yaml](#border_configyaml) file, but with borders stripped
off of most windows.  To compensate for this, each portal has a "status"
bar at the bottom to indicate whether it's ative or not.


## Configuration Parts

At the start of your configuration file, you need to describe which
configuration version it's written for.  At the moment, the only supported
version is "1":

```yaml
version: 1
```

After that, there are several sections of configuration that you can configure.

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


### Layout Configuration

Layouts are defined per monitor configuration.  Normally, you'd want one
top-level layout per monitor, but if you need more control, you can use a
single layout to cover all your screens - *but don't expect it to be nice.*

Layouts are defined within a [work group](#work-group-layouts), so that each
[monitor setup](#monitors) can have its own set of layouts.

```yaml
workgroups:

# Work group 1: two screen
- name: two screens
  display:
  - width: 1024
    height: 768
  - width: 1024
    height: 768
  layouts:
    default:
    # First monitor is split into two parts:
    # +-----------+---+
    # |           |   |
    # |           |   |
    # |           |   |
    # +-----------+---+
    - type: horizontal split
      children:
      - name: browsers
        type: portal
        size: 3
      - name: chat
        type: portal
        size: 1
    # The second monitor has just one portal for the whole screen.
    - type: portal
```


#### Monitors

To understand your monitor layout, for use in the configuration, you can run:

```cmd
> detect-monitors
```

Or with the source distribution:

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

```yaml
    # +-----------+
    # |           |
    # |           |
    # +-----------+
    # |           |
    # +-----------+
    - type: vertical split
      children:
      - name: top
        type: portal
        size: 2
      - name: bottom
        type: portal
        size: 1
```

This defines the layout as a "split-layout", which
splits the region from top-to-bottom (vertically).  It then defines 2 child
splits, the first with a size 2 defined as a portal, and the second as a
size 1 portal.  Because there are two children, with their sizes totalling 3,
the first portal will take up 2/3 of the space, and the second 1/3.

You can define a layout as a "vertical split", a "horizontal split", or a
"portal".  You can give a name to any split, but it only has a meaning
when used with portals.

![1.2-1-1 Split](../../master/docs/imgs/split1.png?raw=true)

In this example, the top level is split 3 columns, and the left-hand
side is split into two vertical slices.

```yaml
    - type: vertical split
      children:
      - type: horizontal split
        size: 1
        children:
        - name: left-top - region 1
          size: 1
          type: portal
        - name: left-bottom - region 2
          size: 3
          type: portal
      - name: middle - region 3
        type: portal
        size: 1
      - name: right - region 4
        type: portal
        snap: bottom right
        size: 1
```


#### Splits and Portals of Size 0

If you use a size of 0, then this is considered a "full" split, and it
takes up the size of the parent split.

This allows for having a side-bar window that you tab to on occasion, but
normally want to keep minimized.

If you set a size "0" portal within a top-level layout, It acts as an
alternative to maximizing applications.


#### Snap Alignment for Portals

Portals can also define how windows are positioned within them.  Normally,
windows are resized to fit exactly within the portal.  However, some windows
do not size themselves exactly (such as console windows, which set their size
based on the font size), and some windows may be prevented from being
resized (by disabling the [resize](#display-values) functionality).  In these
cases, the window does not fit as expected, and can be *aligned* within the
portal.

You can specify the alignment along the vertical and horizontal sides with
the `snap` layout attribute.  This value is a human readable string that
declares the alignment.

Examples:

* *top left* (the default alignment): Position the window such that its top
    left corner is flush with the top left corner of the portal. 
* *bottom right*: The window's bottom right corner is flush with the bottom
    right corner of the portal.
* *right*: The window's right edge is against the portal's right edge, and
    is centered vertically.
* *center*: The window is positioned in the middle of the portal.


#### Testing Your Layout

To test out your layout configuration, to see how Petronia will split up
the screens based on the layout definition it finds for your monitors,
you can run:

```cmd
> check-layout (configuration file name) (layout name)
```

Or with the source distribution:

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
> detect-apps
```

Or with the source distribution:

```cmd
> python -m petronia.detect_apps
```

This will list out each visible window for the running applications, and give
you valuable insight into how to distinguish it from other windows.

```yaml
application-setup:
  defaults:
    display: "-title +border +tiled"
  applications:
  - display: "+title +border -tiled"
    matchers:
    # yaml syntax: need to escape the "\"
    - class-name-re: "#\\d+"
      title-re: "\\d+ reminder\\(s\\)"
      exec-path: outlook.exe
```

This registers a single *chrome configuration*, which defines how Petronia
will act upon the matching application window.  In this case, the
`title` value is disabled, so it won't have the title bar, the `border` value
is enabled, so the resize borders appear.  `tiled` is disabled, so it also
will not be managed within the [portal layouts](#splits-and-portals), and
won't react to portal movement key actions.


#### Display Values

The display values can either be expressed as a enabled/disabled set of values
in a string (the *display string*), or as a dictionary of boolean (`true` or
`false`) values.

```yaml
  - display: "+title -border +tiled -resize"
  - has-title: true
    has-border: true
    is-tiled: true
    resizable: false
```

| Display String Key | Dictionary Key | Meaning |
| ------------------ | -------------- | ------- |
| `title`            | `has-title`    | Enable or disable the title bar and related buttons from the top of the window. |
| `border`           | `has-border`   | Enable or disable the resize border surrounding the window. |
| `tiled`            | `is-tiled`     | Enabled means that the window is included in the tile management; Disabled means that the window is not moved or swapped through the tile actions. |
| `resize`           | `resizable`    | Enabled means that the window is resized when put into a tile; Disabled means that the window is kept the same size. |


#### Default Values

The default values in the `defaults` section sets up the display settings
for all applications that are not matched in the `applications` section.


#### Matching an Application Window

An application configuration relies upon a matcher to
define whether a given application window matches the configuration.

With an app matcher, you can define the following attributes:

* `match-returns`: By default, the matcher will report itself as a match.
    If, instead, you want to explicitly omit the matched application, set
    this value to `False`.
* `title`: A string that matches the application window's title, ignoring
    capitalization.
* `title-re`: A Python regular expression that matches the application
    window's title.
* `module-path`: The path of the module that controls the window.
    You can specify "MyModule.dll", and it will match for any module
    that has the "MyModule.dll" file, regardless of its path.
* `module-path-re`: A Python regular expression version of the
    path of the module that controls the window.
* `exec-path`: The path of the executable that created the window.
    You can specify "MyCommand.exe", and it will match for any executable
    that has the "MyCommand.exe" file, regardless of its path.
* `exec-path-re`: A Python regular expression of the path of
    the executable that created the window.
* `class-name`: The specific class name of the window.  Each window generally
    has its own class name, so you can distinguish different windows that
    came from the same executable.
* `class-name-re`: A Python regular expression of the
    `class-name`.


#### Configuring for Chrome and Position

In the examples above, the configuration controls how some application
works with the window decoration and inclusion in the tiling system.

Additionally, you can control in which portal a window should be placed
at layout load time.

```yaml
  - location: [left, main]
    matchers:
    - exec-path: firefox.exe
    - exec-path: chrome.exe
    - exec-path: outlook.exe
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
> detect-keys
```

Or with the source distribution:

```cmd
> python -m petronia.detect_keys
```

to start an application that will monitor your keys, and tell you how to
reference it in your configuration.  Press <kbd>&crarr; Enter</kbd> to
stop the application.


#### Modal Configurations

The key actions allow for switching between keyboard modes.  The initial
keyboard mode is the `default` mode.  You can assign a keystroke combination
to switch to a different mode, which allows for switching between completely
different keyboard hotkeys on the fly.

```yaml
keysets:
  default:
    type: hotkey
    options:
      block-win-key: false
    commands:
      # Switch to the alternate input modes
      "win+~": ['change mode', 'prevent-input']
  prevent-input:
    type: exclusive
    commands:
      "enter": ['change mode', 'default']
```

##### Keyset Type `hotkey`

The "hotkey" modes allows for Petronia to capture a few select keywords out
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


###### Preventing Windows From Using the Windows Key

In the hotkey mode, you can tell Petronia to have Windows ignore the
<kbd>&#x2756; Win</kbd> key:

```yaml
  ignore-win-key-mode:
    type: hotkey
    options:
      block-win-key: true
```

This means tapping <kbd>&#x2756; Win</kbd>
won't trigger the start menu to pop up.  It also means that a few of the
nice [Windows key shortcuts](https://en.wikipedia.org/wiki/Windows_key),
like <kbd>&#x2756; Win</kbd><kbd>R</kbd> to open the run dialog, are not
available.  You'll need to provide your own hotkey actions to provide an
equivalent function.

Note that a few key sequences will always be recognized by Windows, and
can't be overridden or disabled.  This includes
<kbd>&#x2756; Win</kbd><kbd>L</kbd> (lock screen).

Also note that, as of this writing, the command to bring up the start
menu (`open-start-menu`) does not work on standard Windows 8 and Windows 10
computers.


##### Keyset type: `exclusive`

With the exclusive mode, Petronia captures all your Windows input.  This allows
you to have a mode that doesn't require you to hold down a key the whole time.
This will become more useful when the layout management mode is implemented.

You are expected to include a change mode command key (say, <kbd>Esc</kbd>)
to revert back to standard mode.  Without this, you'll be suck in a
non-keyboard Windows computer, and you'll have to stop Petronia through the
Task Manager using your mouse.  *Yuck!*

This mode only recognizes single keys per command.  It doesn't allow for
combo keys like <kbd>&#x21e7; Shift</kbd><kbd>F1</kbd> or
<kbd>&#x2732; Ctrl</kbd><kbd>&#x1f507; Mute</kbd>.


### Component Configuration

Setting up the component configuration allows for selecting individual parts
of the Petronia system to activate.  This is only loaded once, for the initial
configuration file at start time.

This is how you can 'plug' in new capabilities into Petronia.  For example,
you can have some color on a border of the portals:

```yaml
components:
  singletons:
    # In order to indicate which portal is focused, we add a bit of chrome to the
    # bottom of each portal that has a color when active.
    - factory: petronia.components.portal_chrome
      settings:
        position: bottom
        width: 12
        active-color: '#0070f0'
        inactive-color: '#404060'
```

The two inputs to the `components` are:

* `singletons` - Components that listen to events and add some behavior as
    things happen within the Petronia system.
* `extensions` - Additional objects which can be created on the fly, such
    as new layout types.

The goal with the components is to allow for a point of entry for additional
functionality, for for adding in non-standard functionality. 
