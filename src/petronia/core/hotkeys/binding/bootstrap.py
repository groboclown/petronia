
"""
Bootstrap the hotkey bindings for the core services.
"""

from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
)
from ....aid.bootstrap import (
    ANY_VERSION,
    create_singleton_identity,
)
from ....aid.lifecycle import create_module_listener_helper
from ....base.internal_.internal_extension import petronia_extension
from ..api import (
    HotkeyEventTriggeredEvent,
    BoundServiceActionSchema,
    as_hotkey_event_triggered_listener,
)
from .handlers import (
    on_shutdown_request,
)


TARGET_ID_HOTKEY_CORE = create_singleton_identity("core.hotkey.binding")

HOTKEY_ACTION_SHUTDOWN = 'shutdown'


def bootstrap_core_handlers(bus: EventBus) -> None:
    listeners = create_module_listener_helper(bus, TARGET_ID_HOTKEY_CORE)

    def handler(
        _event_id: EventId,
        _target_id: ParticipantId,
        event_obj: HotkeyEventTriggeredEvent
    ) -> None:
        if event_obj.data.action == HOTKEY_ACTION_SHUTDOWN:
            on_shutdown_request(bus)

    listeners.listen(TARGET_ID_HOTKEY_CORE, as_hotkey_event_triggered_listener, handler)
    listeners.bind_hotkey(
        BoundServiceActionSchema(
            TARGET_ID_HOTKEY_CORE, HOTKEY_ACTION_SHUTDOWN, {}
        )
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.hotkeys.binding",
    "type": "standalone",
    "version": (1, 0, 0,),
    "depends": ({
        "extension": "core.hotkeys.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.shutdown.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.validation.api",
        "minimum": ANY_VERSION,
    },),
})
