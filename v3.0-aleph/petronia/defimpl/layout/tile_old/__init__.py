
"""
The Petronia tiling extension.

*OLD CODE - BASED ON THE OLD API THAT DOES NOT EXIST ANYMORE.*

It allows for:
  * splitting the screen up into sections;
  * having different splits depending on the monitor resolution;
  * virtual screens;
  * dynamic splitting, based on per screen settings;
  * overlapping windows.

The UI is split into "portals" and "containers".  A portal is a place where
zero or more UI windows are stored.

Make sure you define the configuration for this extension in order to customize
the layout.


**Key Binding Guide:**

The layout API provides generic key bindings, which, for this layout, have these meanings:

* `move-active`: Adjusts the size and position of the active portal, if possible.
    Only one of `dx` and `dy`, or `dw` and `dh` need be specified; the layout will
    use the correct one for the owning split's direction.
    Moving a portal (dx or dy) means resizing the sibling tile so the active portal
    keeps its ame size.
    The `dz` has a special meaning - it flips the active window within the portal.
* `shift-focus`: Changes the currently focused portal.  Uses the `name` to indicate
    the direction, and `index` to indicate the amount of move.  The direction names
    recognized are 'n', 's', 'e', and 'w'.  An index of 0 will be interpreted as a 1
    (this is due to the way Petronia handles the index if it isn't specified).
    The layout configuration defines whether the focus will wrap-around to the other side.
    If the name is the same as a named portal, then the focus is set to that instead.
* `set-visible`: if `visible` is True, then it minimizes the currently active
    window in the currently active portal.  If `visible` is False, then it restores the
    currently active window; explore what this means on your own!


In addition to the generic layout key binding, the tile layout provides additional key
bindings that are specific to this layout.

"""

from .bootstrap import bootstrap_layout as start_extension
from .bootstrap import EXTENSION_METADATA
from .config.parser import TILE_LAYOUT_CONFIG_SCHEMA as CONFIG_SCHEMA
