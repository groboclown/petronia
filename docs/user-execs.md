# Guide to the Executables

Petronia supplies several executable files.  This tells you what they do, and
how to use them.


## `petronia.exe` and `petronia-cli.exe`

**Usage:** `petronia [-h] [-l LAYOUT] [-v] [-e EXTENSIONS] configfile`

Window tiling manager for Windows.

The `petronia-cli` is identical to `petronia`, but runs as a terminal program,
for easier monitoring.  Additionally, you need to press <kbd>&crarr; Enter</kbd> in
the console window to end the program.

**Positional arguments:**

* `configfile` - Configuration file for setting up the display.
    Supported formats are: yaml, json, and py.

**Optional arguments:**

* `-h`, `--help` - Show this help message and exit
* `-l` LAYOUT, `--layout` LAYOUT - Initial layout. If not given, the layout
    named `default` is used.
* `-v`, `--version` - Show the version and quit.
* `-e` EXTENSIONS, `--extensions` EXTENSIONS - Directory where the user
    extensions are stored.  Defaults to environment variable `%PETRONIA_USER_DIR%`

**Python Source**

* `petronia.exe` == `python -m petronia.main`
* `petronia-cli.exe` == `python -m petronia.cmd`


## `detect-apps.exe`

**Usage:** `detect-apps`

A cli application.

Displays the information that Petronia uses to match applications against the
[application configuration](user-configuration.md#application-configuration).


## `detect-monitors.exe`

**Usage:** `detect-monitors [-f {yaml|json|py}]`

A cli application.

Displays information, in the given format (defaults to `yaml`), about the
currently active monitors connected to your computer.  If you are running in
a remote desktop environment, it will display information about the remote
desktop display.

**Optional arguments:**

* `-f` - Set the output format, for easy cut-and-paste into your configuration
    file.  Acceptable formats are `yaml`, `json`, and `py`.
    

## `detect-keys.exe`

**Usage:** `detect-keys`

A cli application.

Reports the key names, as known by Petronia for use in the
[hotkey configuration](user-configuration.md#hotkey-configuration).

Press <kbd>&#x2732; Ctrl</kbd><kbd>C</kbd> to stop the application.
