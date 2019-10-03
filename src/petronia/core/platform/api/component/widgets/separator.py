
"""
Insert a visual separator.  Some platforms may allow for the user to move it.
"""

from ......base import create_singleton_identity

COMPONENT_ID_CREATE_SEPARATOR = create_singleton_identity('core.platform.api/separator')


class SeparatorWidget:
    """
    Simple, no-data separator.  The display is up to the current theme.
    """

    __slots__ = ()

    def __init__(self) -> None:
        pass
