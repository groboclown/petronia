
"""
State definition for window objects.
"""


class AllActiveWindowsState:
    """
    All the windows in the system and a high-level view of their state.  This
    overlaps with individual window states.
    """
    __slots__ = ()


class NativeWindowState:
    """
    State for a specific window.
    """
    __slots__ = ()
