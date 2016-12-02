# Petronia Change History

## :: v2.2.1 ::

### Overview

* Bug fixes.

### Details

* Bug fixes.
    * Portal chrome now correctly closes the chrome bits on
        a layout change. (#8)


## :: v2.2 ::

### Overview

* Added "resizable" flag for applications.
* Added "snap" option to portals.
* detect-monitors command now supports different output formats.
* Added user extensions directory support.
* Changed how you specify the layout argument at the command line.
* Documentation improvements.
* Bug fixes.

### Details

* Added "resizable" flag for applications.
    * Applications can set a "resizable" flag (defaults to on), to specify
        whether the matching window should be resized to fit into the
        portal.  Before, the matching window would have to be excluded from
        tiling control in order to not be resized.
    * Updated "no_border_config" and "border_config" to use the flag.
* Added "snap" option to portals.
    * Windows that do not fully fit within a portal are now "snapped" into
        a relative position within the portal.  By default (and the original
        behavior), the window snaps to the top-left corner of a portal.  Now
        it can be positioned relative to any corner or side.
    * Updated "no_border_config" and "border_config" to use the flag.
* detect-monitors command now supports different output formats.
    * Run with "-f (format)" to output in a different format.
    * Supported formats are: `yaml`, `json`, and `py`.
    * Format now defaults to `yaml` instead of python.
* Added user extensions directory support.
    * You can either use the `%PETRONIA_USER_DIR%` environment variable, or
        the `-e` command-line argument, to specify where Petronia should look
        for user extensions.  This allows for adding in components to your
        configuration.
* Changed how you specify the layout argument at the command line.
    * It used to be that the layout name was the optional second argument.  Now,
        you must specify it with the `-l` or `--layout` argument.
    * The check-layout command is unchanged.
    * Command-line parsing for cmd and main now use argparse to grant the
        ability to have more complex arguments.  Unfortunately, this lead to
        the backwards incompatibility with the layout name.
* Documentation improvements.
    * Cleaning up to better reflect the current version.
* Bug fixes.
    * Fix portal chrome from staying on top of overlay windows.
    * Improved portal chrome to not have the annoying white border in
        Windows 8. (#6)
    * Portal chrome windows no longer shows up on the task bar.
    * Correctly associated portals to their aliases.  This information wasn't
        being passed to the portal factory before.
    * Hide the "KeyboardInterrupt" exception from users when running the
        detect-keys command, because this is an expected action.


## :: v2.1 ::

### Overview

* `render_active_portal` is finally gone.
* Updated documentation to reference the yaml files.
* Added component configuration in dictionary-based configuration files.
* Added `portal_chrome` component.
* Bug fixes.

### Details

* `render_active_portal` is finally gone.
    * It's been removed.  You can't use it anymore.  Use the `portal_chrome`
        instead.
* Updated documentation to reference the yaml files.
    * Documentation has been rearranged to make the yaml config file format
        front and center.
    * Included more example configurations.
* Added component configuration in dictionary-based configuration files.
    * Dictionary-based config files (json, yaml) can now specify the
        configuration and setup for components.
    * Started the path for allowing external components.
* Added `portal_chrome` component.
    * Shows the active and inactive portals.
* Bug fixes.
    * So many bugs.  Actually, they just weren't tracked well.


## :: v2.0 ::

### Overview

* Configuration now allowed as yaml and json files!
* Added new user command: `focus-last-flashing-window`
* Switched from `parse_simple_mode` to `parse_exclusive_mode`
* Chrome configuration backwards-incompatible changes
* Windows not owned by tiling management can now receive commands.
* Bug Fixes

### Details

* Configuration now allowed as yaml and json files!
    * You can write your configuration files as yaml or json files now.
    * Updated example to include a yaml and json version.
* Added new user command: `focus-last-flashing-window`
    * You can now bind a key that will raise the most recently "flashing"
        window to the top, and give it focus.
* Switched from `parse_simple_mode` to `parse_exclusive_mode`
    * Exclusive mode more explicitly describes the purpose of the mode.
* Chrome configuration backwards-incompatible changes
    * The "chrome" configuration was mostly placeholders for future
        functionality.  Now that more of the design is in place, this is
        now a holder for other components to reference.
        Configurations don't use it anymore.
    * Removed 'color' property from the chrome border.
    * Borders are set by the classes that manage portal borders themselves.
    * Moved the decoration of windows into the application settings, to allow
        for more flexibility on a per-application basis.
    * Application setup now has `default_has_border` and `default_has_title`,
        replacing the original `default_is_managed_chrome`
* Windows not owned by tiling management can now receive commands.
    * Added ability to send some user commands to windows not in the tiling
        management.
* Bug fixes
    * Portals now correctly remove listeners for closed windows.


## :: v1.2 ::

### Overview

* Chrome config no longer uses border 'width' attribute.
* Bug fixes

### Details

* Chrome config no longer uses border 'width' attribute.
    * The 'width' attribute on the Chrome configuration borders was always
        intended as a placeholder.  Now, it's not needed, and has been
        removed.
* Bug fixes
    * When a window is destroyed, the event is now passed to all the
        components (#4)
    * `render_active_portal` now draws the windows a bit more accurately,
        without rendering refresh glitches.  It's still not good.
    * Changing window focus in the current portal to previous
        (`switch-top-window previous`) now correctly moves to the previous
        window.
    * Fixed issues around finding windows that aren't owned by the
        user.  Now, all visible windows should be managed that are only owned
        by the current window.  This also fixes problems with adding certain
        applications that were incorrectly recognized as not owned.


## :: v1.1 ::

### Overview

* Move window improvements.
* Swap window within the same portal.
* Component configuration documentation.
* Added "flashing" capabilities to the `render_active_portal` plugin.


### Details

* Move window improvements.
    * When you move a window between portals, it now has a better chance
        of remaining on top of the other windows after the move.  There's
        still some cases where it doesn't work, though. (#1)
* Swap window within the same portal.
    * You can now swap between focused windows within the same portal.
        Use the `["switch-top-window", "previous"]` and
        `["switch-top-window", "next"]` commands.
* Added documentation for the Component configuration.
    * Included note about the `render_active_portal`.
    * `render_active_portal` now available from the executable distribution.
* Added "flashing" capabilities to the `render_active_portal` plugin.
    * When a window indicates that it should "flash", the
        `render_active_portal` plugin will flash the border color of the
        portal that contains the flashing window.
* General documentation improvements.


## :: v1.0 ::

### Overview

* Initial release.

### Details

* Initial public release.