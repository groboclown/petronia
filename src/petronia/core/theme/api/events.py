
"""
All events for the theme.

The state is, of course, setup with the configuration and state API.

The remaining events relate to the layer on top of the platform API's widgets
in the different places the theme permits.
"""

from ....aid.simp import (
    EventBus,
    EventCallback,
    EventId,
    create_singleton_identity,
)


class RequestNewWindowEvent:
    """
    Create a new window along with its tree of widgets.

    The window can be given a unique string name, such as "task bar",
    so that other extensions can dynamically add widgets to it.  Likewise,
    panel widgets inside the window can be assigned locally-unique names, so
    other extensions can add to them.  Each interactive widget is stored in
    the state with the component ID, so that its events can be directly
    listened to.
    """

    __slots__ = (
        '__global_name', '__widget_tree',
        # TODO need to allow adding to the NativeWindowState name data
        #   so that the theme matcher can work with it.
    )


# ---------------------------------------------------------------------------

class RequestAddWidgetToWindowEvent:
    """
    Add a widget (or widget tree) to
    """

    __slots__ = (

    )