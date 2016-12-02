# Hotkey Commands

All the commands you can run with hotkeys.

See also [custom commands](user-custom-commands.md).

Reference: [command_builder.py](../src/petronia/script/command_builder.py)
<!-- that file generates this file -->


## Built-In Command List

### `quit `

**Arguments**: None

Exits Petronia.  Currently, this is the only way to quit Petronia
(besides running task manager and killing the process).  This means that you
need to be sure to include at least one hot key to terminate the program.



### `open-start-menu `

**Arguments**: None

Forces the Windows Start Menu to open.  If you have the task bar minimized by
default, then the start menu will appear as if the task bar is visible, but
the task bar may not show itself.

Especially handy if you've disabled Windows from processing the Windows key.

*HUGE WARNING* Currently, this command doesn't work right for Windows 8 and
Windows 10 users.  If you have the StarDock "Start8" tool running, though,
it will correctly open the start menu.



### `move-focus (direction)`

**Arguments**: 

* `direction` -  one of `north`, `south`, `east`, `west`, `next`, `previous`

Make another portal have the "portal focus", in a relative direction to the
currently focused portal.  The focused portal can be setup through the
`ChromeConfig` to have a distinct border color from the non-focused portals.



### `switch-top-window (direction)`

**Arguments**: 

* `direction` -  one of `north`, `south`, `east`, `west`, `next`, `previous`

Switch which window in the currently active portal (the one with the "portal
focus") is on top.



### `switch-layout (layout_name)`

**Arguments**: 

* `layout_name` -  `layout name`: one of the work group layouts.

Switches the currently displayed layout configuration to a different
configuration.



### `create-current-portal-alias (alias_name)`

**Arguments**: 

* `alias_name` -  alias to call the currently focused portal

Gives the currently focused portal a specific name.



### `focus-portal-by-alias (alias_name)`

**Arguments**: 

* `alias_name` -  alias of the portal to focus.

Returns the portal focus to the previously aliased portal.  Can also refer
to the original portal name, as specified in the layout definition.

Also, sends that portal's "top" window to the front of the other windows, and
gives it focus.  This allows for quick focus swapping between apps, with more
configurability than the standard Windows <kbd>&#x2756; Win</kbd><kbd>1</kbd>
(and other digits).



### `focus-last-flashing-window `

**Arguments**: None

Make the last window that "flashed" (blinked in the task bar) focused and on top
of the other windows.  This works on windows which are managed and not managed by
the tiling system.



### `move-window-to-other-portal (direction)`

**Arguments**: 

* `direction` -  one of `north`, `south`, `east`, `west`, `next`, `previous`

Moves the currently active window into another portal adjacent to its current
portal.



### `change-layout-selection (direction) (change)`

**Arguments**: 

* `direction` -  one of `north`, `south`, `east`, `west`, `next`, `previous`
* `change` -  one of `+`, `-`

Change the current layout selection shape.

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.



### `join-selected-layout `

**Arguments**: None

Combine the currently selected layouts into a single layout ("un-split")

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.



### `split (orientation)`

**Arguments**: 

* `orientation` -  one of `vertical`, `horizontal`

Split the currently selected layout in the given orientation.

*Not implemented yet.*  This will be part of the future feature to allow for
the user to alter the layout shape while Petronia is running.



### `minimize `

**Arguments**: None

Minimize (to the task bar) the currently active window.



### `maximize `

**Arguments**: None

Maximize the currently active window.



### `resize (adjust_x) (adjust_y)`

**Arguments**: 

* `adjust_x` -  integer amount to resize in the x (horizontal) direction; may be negative or 0.
* `adjust_y` -  integer amount to resize in the y (vertical) direction; may be negative or 0.

Resize the currently active window by the given amount.

To make a side bigger, use a positive number.  To make it smaller, use a
negative number.  To keep it the same size, use 0.



### `change-layout (layout_name)`

**Arguments**: 

* `layout_name` -  one of the work group layouts.

Switches the currently displayed layout configuration to a different
configuration.



### `load-config (config_file)`

**Arguments**: 

* `config_file` -  (optional) If given, the name of the config file to load.

Loads the given configuration file to become actively used.  If no config
file is given, then it reloads the current config file.



### `lock-screen `

**Arguments**: None

Lock the desktop.  Equivalent to <kbd>&#x2756; Win</kbd><kbd>L</kbd>, which
will always be active anyway.



### `inject-keys (key_commands)`

**Arguments**: 

* `key_commands` -  series of `key name` and `press type`

Injects a series of keystrokes into the operating system.

The arguments must be a series of "key name" "press type" words.
"key name" refers to the name of the key on the keyboard to
simulate pressing (equivalent to the name used in
[the hotkey definition](keys.md)).  "press type" must be
either `up` or `down`, to indicate whether the key is pressed
*down* or released (the key moves *up*).



### `cmd (cmd_line)`

**Arguments**: 

* `cmd_line` -  The command-line string equivalent to run.

Executes an external process using the given arguments.  Note that the
backslash (`\`) character must be escaped, because they are within a Python
string, so a total of 2 backslashes to equal 1 real backslash.

For example, to run a command prompt with fancy colors and start it in the
root of the file system when you press <kbd>F1</kbd>, use:

```
'f1 => cmd cmd.exe /c start cmd.exe /E:ON /V:ON /T:17 /K cd \'
```



