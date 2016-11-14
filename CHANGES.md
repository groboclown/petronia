# Petronia Change History

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