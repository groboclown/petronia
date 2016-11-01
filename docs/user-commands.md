# Hotkey Commands

All the commands you can run with hotkeys.


## Built-In Command List

#### `quit`

**Arguments**: None

Exits Petronia.  Currently, this is the only way to quit Petronia
(besides running task manager and killing the process).  This means that you
need to be sure to include at least one hot key to terminate the program.


#### `open-start-menu`

**Arguments**: None

Forces the Windows Start Menu to open.  If you have the task bar minimized by
default, then the start menu will appear as if the task bar is visible, but
the task bar may not show itself.

Especially handy if you've disabled Windows from processing the Windows key.


#### `cmd (command parameters)`

**Arguments**: The command-line string equivalent to run.

Executes an external process using the given arguments.  Note that the
backslash (`\`)character must be escaped, once for being within a Python
string, and again due to the parsing of the command line args, so a total of
4 backslashes to equal 1 real backslash.

For example, to run a command prompt with fancy colors and start it in the
root of the file system, use:

```
cmd cmd.exe /c start cmd.exe /E:ON /V:ON /T:17 /K cd \\\\
```


#### `switch-layout (layout name)`

**Arguments**:

* `layout name`: one of the work group layouts.

Switches the currently displayed layout configuration to a different
configuration.


#### `create-current-portal-alias (alias)`

**Arguments**:

* `alias` : alias to call the currently focused portal

Gives the currently focused portal a specific name.


#### `focus-portal-by-alias (alias)`

**Arguments**:

* `alias` : alias of the portal to focus.

Returns the portal focus to the previously aliased portal.  Can also refer
to the original portal name, as specified in the layout definition.

Also, sends that portal's "top" window to the front of the other windows, and
gives it focus.  This allows for quick focus swapping between apps, with more
configurability than the standard Windows <kbd>&#x2756; Win</kbd><kbd>1</kbd>
(and other digits).


#### `move-window-to-other-portal (direction)`

**Arguments**:

* `direction`: one of `north`, `south`, `east`, `west`, `next`, `previous`

Moves the currently active window into another portal adjacent to its current
portal.


#### `move-focus (direction)`

**Arguments**:

* `direction`: one of `north`, `south`, `east`, `west`, `next`, `previous`

Make another portal have the "portal focus", in a relative direction to the
currently focused portal.  The focused portal can be setup through the
`ChromeConfig` to have a distinct border color from the non-focused portals.


#### `maximize`

**Arguments**: None

Maximize the currently active window.


#### `minimize`

**Arguments**: None

Minimize (to the task bar) the currently active window.


#### `load-config (config file)`

**Arguments**:

* `config file` (optional) If given, the name of the config file to load.

Loads the given configuration file to become actively used.  If no config
file is given, then it reloads the current config file.


#### `lock-screen`

**Arguments**: None

Lock the desktop.  Equivalent to <kbd>&#x2756; Win</kbd><kbd>L</kbd>, which
will always be active anyway.


#### `inject-keys [(key name) (press type) ...]`

**Arguments**: pairs of:

* `key name` the key name to press.  Equivalent to the name used in
    [the hotkey definition](keys.md)
* `press type`: either `up` or `down`

Injects a series of keystrokes into the operating system.


#### `switch-top-window (direction)`

**Arguments**:

* `direction`: one of `north`, `south`, `east`, `west`, `next`, `previous`

Switch which window in the currently active portal (the one with the "portal
focus") is on top.

*Not implemented yet.*  The code for this is at `active_portal_manager.py`,
in the `_on_window_zorder_change` method.


#### `change-layout-selection (direction) (change)`

**Arguments**:

* `direction`: one of `north`, `south`, `east`, `west`, `next`, `previous`
* `change`: one of `+`, `-`

Change the current layout selection shape.

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.


#### `join-selected-layout`

**Arguments**: None

Combine the currently selected layouts into a single layout ("un-split")

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.


#### `split (orientation)`

**Argumetns**:

* `orientation`: one of `vertical`, `horizontal`

Split the currently selected layout in the given orientation.

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.



## Custom Commands

The *command* configuration object (`CommandConfig`) allows for registering
custom commands.  Each command must be a `petronia.script.command.Command`
object.

For example, to have a command that changes the output logging level, you
could write it as:

```python

from petronia.system import event_ids, target_ids
from petronia.script.command import Command
from petronia.config import CommandConfig

def change_log_level(bus, level):
    bus.fire(event_ids.LOG__LEVEL_SET, target_ids.LOGGER, {'level': level})

base_config = CommandConfig()
base_config.add_command(Command('set-log-level', change_log_level))
```

Then you can write a hotkey definition:

```
alt + shift + f1 => set-log-level debug
```

If you're writing a command that interacts with the interworkings of Petronia,
then you'll have to send signals through the event bus.

If you really want to get funky, you can reach into the bowels of the winapi
calls and directly query or interact with the windows.  However, this API is
very much use at your own risk.

Otherwise, just use the standard Python API.  If you install custom packages
into your Python installation, then you can use those, as well. 


## Writing a Hotkey to Directly Run Something and Bypass Commands

Not supported, and not planned on being supported.
