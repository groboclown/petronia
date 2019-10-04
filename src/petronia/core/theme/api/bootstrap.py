
"""
Bootstrap the theme API.
"""

from ....base.bus import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    ExtensionMetadataStruct,
)
from ....base.events import (
    register_event,
)
from ....core.extensions.api import (
    ANY_VERSION,
)


def bootstrap_theme_api(bus: EventBus) -> None:
    """
    Setup the theme.
    """
    # register_event(
    #     bus,
    #     EVENT_ID_TIMER,
    #     QUEUE_EVENT_NORMAL,
    #     TimerEvent,
    #     GLOBAL_TIMER_EVENT
    # )
    pass


EXTENSION_METADATA: ExtensionMetadataStruct = {
    "name": "core.theme.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": [
        {
            "extension": "core.platform.api",
            "minimum": ANY_VERSION,
        }
    ],
    "defaults": [
        {
            "extension": "default.theme",
            "minimum": ANY_VERSION,
        }
    ],
    "authors": ["Petronia"],
}
