
"""
Bootstrap the hotkey bindings for the layout events.
"""

from typing import List
from ....aid.std import (
    EventBus,
    EventId,
    ParticipantId,
    ErrorReport,
    report_error,
    create_user_error,
)
from ....aid.bootstrap import (
    ANY_VERSION,
    create_singleton_identity,
)
from ....aid.lifecycle import create_module_listener_helper
from ....base.internal_.internal_extension import petronia_extension
from ....base.util.simple_type import (
    PersistTypeSchemaItem,
    PERSISTENT_TYPE_SCHEMA_NAME__DOC,
    PERSISTENT_TYPE_SCHEMA_TYPE__BOOL,
    PERSISTENT_TYPE_SCHEMA_TYPE__STR,
    PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT,
    optional_str, optional_int, optional_bool,
    collect_errors,
)
from ...hotkeys.api import (
    HotkeyEventTriggeredEvent,
    BoundServiceActionSchema,
    as_hotkey_event_triggered_listener,
)
from ..api import (
    RequestMoveResizeFocusedWindowEvent,
    send_request_move_resize_focused_window_event,

    RequestShiftLayoutFocusEvent,
    send_request_shift_layout_focus_event,

    RequestSetFocusedWindowVisibilityEvent,
    send_request_set_window_visibility_event,
)


TARGET_ID_LAYOUT_HOTKEYS = create_singleton_identity("core.layout.binding")

HOTKEY_ACTION_MOVE_ACTIVE = 'move-active'
HOTKEY_ACTION_SHIFT_FOCUS = 'shift-focus'
HOTKEY_ACTION_SET_VISIBILITY = 'set-visible'


def bootstrap_layout_handlers(bus: EventBus) -> None:
    listeners = create_module_listener_helper(bus, TARGET_ID_LAYOUT_HOTKEYS)

    def handler(
        _event_id: EventId,
        _target_id: ParticipantId,
        event_obj: HotkeyEventTriggeredEvent
    ) -> None:
        errors: List[ErrorReport] = []

        # -------------------------------------------------------------------
        if event_obj.data.action == HOTKEY_ACTION_MOVE_ACTIVE:
            dx = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'dx',
                lambda: create_user_error(handler, '"dx" must be a number')
            )) or 0
            dy = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'dy',
                lambda: create_user_error(handler, '"dy" must be a number')
            )) or 0
            dw = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'dw',
                lambda: create_user_error(handler, '"dw" must be a number')
            )) or 0
            dh = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'dh',
                lambda: create_user_error(handler, '"dh" must be a number')
            )) or 0
            dz = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'dz',
                lambda: create_user_error(handler, '"dz" must be a number')
            )) or 0
            send_request_move_resize_focused_window_event(bus, dx, dy, dw, dh, dz)

        # -------------------------------------------------------------------
        elif event_obj.data.action == HOTKEY_ACTION_SHIFT_FOCUS:
            name = collect_errors(errors, optional_str(
                event_obj.data.parameters, 'name',
                lambda: create_user_error(handler, '"name" must be a string')
            )) or ''
            index = collect_errors(errors, optional_int(
                event_obj.data.parameters, 'index',
                lambda: create_user_error(handler, '"index" must be a number')
            )) or 0
            print("DEBUG data {0} -> {1}/{2}".format(event_obj.data.parameters, name, index))
            send_request_shift_layout_focus_event(bus, name, index)

        # -------------------------------------------------------------------
        elif event_obj.data.action == HOTKEY_ACTION_SET_VISIBILITY:
            visible = collect_errors(errors, optional_bool(
                event_obj.data.parameters, 'visible',
                lambda: create_user_error(handler, '"visible" must be true or false')
            )) or False
            send_request_set_window_visibility_event(bus, visible)

        for error in errors:
            report_error(bus, error)

    listeners.listen(TARGET_ID_LAYOUT_HOTKEYS, as_hotkey_event_triggered_listener, handler)
    listeners.bind_hotkey(
        BoundServiceActionSchema(
            TARGET_ID_LAYOUT_HOTKEYS, HOTKEY_ACTION_MOVE_ACTIVE, {
                PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
                    RequestMoveResizeFocusedWindowEvent.__doc__ or '',
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "dx": PersistTypeSchemaItem(
                    "Change in window x position (move)", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
                "dy": PersistTypeSchemaItem(
                    "Change in window y position (move)", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
                "dw": PersistTypeSchemaItem(
                    "Change in window width (resize)", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
                "dh": PersistTypeSchemaItem(
                    "Change in window height (resize)", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
                "dz": PersistTypeSchemaItem(
                    "Change in window z-order (focus)", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
            }
        )
    )
    listeners.bind_hotkey(
        BoundServiceActionSchema(
            TARGET_ID_LAYOUT_HOTKEYS, HOTKEY_ACTION_SHIFT_FOCUS, {
                PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
                    RequestShiftLayoutFocusEvent.__doc__ or '',
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "name": PersistTypeSchemaItem(
                    "Layout focus shift name", PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "index": PersistTypeSchemaItem(
                    "Layout focus shift index", PERSISTENT_TYPE_SCHEMA_TYPE__FLOAT
                ),
            }
        )
    )
    listeners.bind_hotkey(
        BoundServiceActionSchema(
            TARGET_ID_LAYOUT_HOTKEYS, HOTKEY_ACTION_SET_VISIBILITY, {
                PERSISTENT_TYPE_SCHEMA_NAME__DOC: PersistTypeSchemaItem(
                    RequestSetFocusedWindowVisibilityEvent.__doc__ or '',
                    PERSISTENT_TYPE_SCHEMA_TYPE__STR
                ),
                "visible": PersistTypeSchemaItem(
                    "True to make the window visible, False to make it hidden", PERSISTENT_TYPE_SCHEMA_TYPE__BOOL
                ),
            }
        )
    )


EXTENSION_METADATA = petronia_extension({
    "name": "core.layout.binding",
    "type": "standalone",
    "version": (1, 0, 0,),
    "depends": ({
        "extension": "core.hotkeys.api",
        "minimum": ANY_VERSION,
    }, {
        "extension": "core.layout.api",
        "minimum": ANY_VERSION,
    },),
})
