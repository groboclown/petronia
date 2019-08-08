
"""
Container UI components.  It contains zero or more widgets arranged
according to the container's setup.
"""

class GridContainer:
    """
    A low-level container that is NxM grid.

    Container UI components.  It contains zero or more widgets arranged
    according to the container's setup.

    This can be used to create toolbars, drop-down menus, dialogs, and other
    elements.  Because a container is not itself a widget, they cannot be
    embedded inside each other.

    Containers use a "grid" layout.  An item inserted into the grid is assumed
    to take up the entire defined area.  Items can take up multiple parts of the
    grid, and they can overlap each other.  Likewise, items will be restricted to
    drawing within the confines of the declared grid size.

    The container size itself is in screen units.
    """
    __slots__ = ()
    def __init__(self) -> None:
        pass


class FlowContainer:
    """
    A container that has a start and end section, each of which can
    contain any number of widgets.  The widgets will line up one after the
    other.  There is a chance that the two sections will overlap.

    The container can either be vertical or horizontal in orientation.
    """
    __slots__ = ()
    def __init__(self) -> None:
        pass
