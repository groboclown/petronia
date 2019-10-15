
"""
The Petronia tiling.

It allows for:
  * splitting the screen up into sections;
  * having different splits depending on the monitor resolution
  * virtual screens
  * dynamic splitting, based on per screen settings.
  * overlapping windows.

The UI is split into "portals" and "containers".  A portal is a place where
zero or more UI windows are stored.


"""

from .bootstrap import bootstrap_layout as start_extension
from .bootstrap import EXTENSION_METADATA
from .config.parser import TILE_LAYOUT_CONFIG_SCHEMA as CONFIG_SCHEMA
