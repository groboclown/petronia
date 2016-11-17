# Petronia Change History

## :: v1.3 ::

### Overview

* Added new user command: `focus-last-flashing-window`
* Windows not owned by tiling management can now receive commands.
* Bug Fixes

### Details

* Added new user command: `focus-last-flashing-window`
    * You can now bind a key that will raise the most recently "flashing"
        window to the top, and give it focus.
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