
"""
All events for the theme.

The state is, of course, setup with the configuration and state API.

Widgets are created using the standard Petronia create component
lifecycle events.  However, after a custom widget is created,
it needs to be added into a parent.  The widget tree is associated
with an owning, native window ComponentID, or with a named top-level
Petronia widget (such as a task bar).

Usually, the end-user doesn't directly ask for the creation of the
low-level widgets.  This is usually some extension that creates
the higher level widgets.
"""

from ....aid.std import (
    EventBus,
    EventCallback,
    EventId,
    create_singleton_identity,
)
