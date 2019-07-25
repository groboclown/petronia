
"""
Setup the loader for the extensions.  This requires adding in additional dependent extensions.
"""

from typing import Sequence
from petronia3.system.bus import (
    EventBus
)


def add_extensions_extension(
        bus: EventBus,
        local_search_dirs: Sequence[str],
        zip_dirs: Sequence[str]
) -> None:
    """
    Adds into the bus the extensions loader and its dependent extensions.
    The directory paths are immutable after initialization, for security
    purposes.  The paths are platform specific.
    """
