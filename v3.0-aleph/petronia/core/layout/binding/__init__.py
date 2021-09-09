"""
Petronia Layout Hotkey Bindings.

Allows for adding hotkey binding to the standard layout events, so that the
different layouts don't need to re-implement all the bindings.  Instead,
they can just listen to the layout API events.

Layout implementations should depend upon this extension.
"""

from .bootstrap import bootstrap_layout_handlers as start_extension
from .bootstrap import EXTENSION_METADATA
