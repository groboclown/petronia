
"""
API and states for associating and manipulating top-level application windows
with tiles defined by the tile implementation.

Along with windows, other UI components can be added to tiles.  In order to
allow backgrounds or borders, some of the added windows can be assigned to
"background" status.  This means that they must always have a lower z-order
than the non-background windows.

Events are used to control the window assignment and window z-order.
The changes to the window assignments are only broadcast through
state updates.
"""

from .bootstrap import bootstrap_layout_window_api as start_extension
from .bootstrap import EXTENSION_METADATA
