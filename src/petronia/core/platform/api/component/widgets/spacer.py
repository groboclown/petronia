
"""
A widget that adds an arbitrary space between one side of a component and
another.  Only the first spacer is generally used.
"""
from ......base import create_singleton_identity


COMPONENT_ID_CREATE_SPACER = create_singleton_identity('core.platform.api/spacer')


class SpacerWidget:
    """
    A simple widget with no data.
    """
    __slots__ = tuple('placeholder',)

    def __init__(self) -> None:
        pass
