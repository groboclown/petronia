
"""
Bootstrap the theme API.
"""

from ....aid.bootstrap import (
    EventBus,
    QUEUE_EVENT_NORMAL,
    register_event,
    ANY_VERSION,
)
from ....base.internal_.internal_extension import petronia_extension


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


EXTENSION_METADATA = petronia_extension({
    "name": "core.theme.api",
    "version": (1, 0, 0,),

    "type": "api",
    "depends": ({
        "extension": "core.platform.api",
        "minimum": ANY_VERSION,
    },),
    "defaults": ({
        "extension": "default.theme",
        "minimum": ANY_VERSION,
    },),
})
