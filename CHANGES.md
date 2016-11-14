# Petronia Change History

## :: v1.2 ::

### Overview

* Bug fixes

### Details

* Bug fixes
    * When a window is destroyed, the event is now passed to all the
        components (#4)
    * `render_active_portal` now draws the windows a bit more accurately,
        without rendering refresh glitches.
    * Changing window focus in the current portal to previous
        (`switch-top-window previous`) now correctly moves to the previous
        window.


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