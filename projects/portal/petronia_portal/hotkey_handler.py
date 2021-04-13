"""Handler for hotkey events."""

from petronia_common.util import StdRet, join_none_results
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from . import portal_handler
from .state import petronia_portal as portal_state
from .events import portal as portal_event
from .events import hotkey_binding as hotkey_event
from .user_messages import report_send_receive_problems


SPLIT_PORTAL__ADD_BEFORE = 'add_before'
SPLIT_PORTAL__FOCUS_NEW = 'focus_new'
SPLIT_PORTAL__NEW_DIRECTION = 'new_direction'
JOIN_PORTALS__JOIN_BEFORE = 'join_before'
FIT__JUSTIFY_HORIZONTAL = 'justify_horizontal'
FIT__JUSTIFY_VERTICAL = 'justify_vertical'
FIT__FIT_HORIZONTAL = 'fit_horizontal'
FIT__FIT_VERTICAL = 'fit_vertical'
ADJUST_PORTAL_SIZE__AMOUNT = 'amount'
ADJUST_PORTAL_SIZE__DIRECTION = 'direction'
MARK_PORTAL__NAME = 'name'
MOVE_WINDOW__TARGET = 'target'
MOVE_WINDOW__MOVE_FOCUS = 'move_focus'
FOCUS_PORTAL__TARGET = 'target'
FOCUS_PORTAL__WRAP = 'wrap'
ROTATE_WINDOW__DIRECTION = 'direction'


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the hotkey listeners"""
    return join_none_results(
        send_register_listeners(
            context,
            portal_state.EXTENSION_NAME,
            (
                (
                    hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
                    None,
                ),
            ),
        ),
        context.register_event_parser(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            hotkey_event.HotkeyFiredEvent.parse_data,
        ),


        # split-portal
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.SplitPortalEvent.FULL_EVENT_NAME,
                portal_event.SplitPortalEvent.__doc__,
                portal_event.SplitPortalEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        SPLIT_PORTAL__ADD_BEFORE,
                        'Set to "true" to add the new portal logically before the currently '
                        'active portal.  The windows will remain in the portal "after" the '
                        'new one.',
                        'false',
                    ),
                    hotkey_event.EventParameterDescription(
                        'focus_new',
                        'If "true", then put the focus on the newly created portal.',
                        'false',
                    ),
                    hotkey_event.EventParameterDescription(
                        'new_direction',
                        'If "true", then the new portal will change the direction from the '
                        'previous one (if it was splitting vertically, then the split will '
                        'happen horizontally).',
                        'true',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
            SplitPortalHotkeyHandler(context),
        ),


        # join-portals
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.JoinPortalsEvent.FULL_EVENT_NAME,
                portal_event.JoinPortalsEvent.__doc__,
                portal_event.JoinPortalsEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        JOIN_PORTALS__JOIN_BEFORE,
                        'Set to "true" to join the active portal with the portal that is '
                        'logically "before".',
                        'false',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.JoinPortalsEvent.UNIQUE_TARGET_FQN,
            JoinPortalsHotkeyHandler(context),
        ),

        # fit-window
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.FitWindowEvent.FULL_EVENT_NAME,
                portal_event.FitWindowEvent.__doc__,
                portal_event.FitWindowEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        FIT__JUSTIFY_HORIZONTAL,
                        'Can be "left", "center" or "right"',
                        'left',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__JUSTIFY_VERTICAL,
                        'Can be "top", "center" or "bottom"',
                        'top',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__FIT_HORIZONTAL,
                        'Can be "shrink", "stretch", "fit", or "none"',
                        'fit',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__FIT_VERTICAL,
                        'Can be "shrink", "stretch", "fit", or "none"',
                        'fit',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.FitWindowEvent.UNIQUE_TARGET_FQN,
            FitWindowHotkeyHandler(context),
        ),

        # fit-portal-windows
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.FitPortalWindowsEvent.FULL_EVENT_NAME,
                portal_event.FitPortalWindowsEvent.__doc__,
                portal_event.FitPortalWindowsEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        FIT__JUSTIFY_HORIZONTAL,
                        'Can be "left", "center" or "right"',
                        'left',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__JUSTIFY_VERTICAL,
                        'Can be "top", "center" or "bottom"',
                        'top',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__FIT_HORIZONTAL,
                        'Can be "shrink", "stretch", "fit", or "none"',
                        'fit',
                    ),
                    hotkey_event.EventParameterDescription(
                        FIT__FIT_VERTICAL,
                        'Can be "shrink", "stretch", "fit", or "none"',
                        'fit',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.FitPortalWindowsEvent.UNIQUE_TARGET_FQN,
            FitPortalWindowsHotkeyHandler(context),
        ),

        # manage-window
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.ManageWindowEvent.FULL_EVENT_NAME,
                portal_event.ManageWindowEvent.__doc__,
                portal_event.ManageWindowEvent.UNIQUE_TARGET_FQN,
                [],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.ManageWindowEvent.UNIQUE_TARGET_FQN,
            ManageWindowHotkeyHandler(context),
        ),

        # unmanage-window
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.UnmanageWindowEvent.FULL_EVENT_NAME,
                portal_event.UnmanageWindowEvent.__doc__,
                portal_event.UnmanageWindowEvent.UNIQUE_TARGET_FQN,
                [],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.UnmanageWindowEvent.UNIQUE_TARGET_FQN,
            UnmanageWindowHotkeyHandler(context),
        ),

        # adjust-portal-size
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.AdjustPortalSizeEvent.FULL_EVENT_NAME,
                portal_event.AdjustPortalSizeEvent.__doc__,
                portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        ADJUST_PORTAL_SIZE__AMOUNT,
                        'Amount to change.  This should be in virtual screen pixels.', '1',
                    ),
                    hotkey_event.EventParameterDescription(
                        ADJUST_PORTAL_SIZE__DIRECTION,
                        'Direction to make the adjustment.  One of "vertical" or "horizontal"',
                        'horizontal',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
            AdjustPortalSizeHotkeyHandler(context),
        ),

        # mark-portal
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.MarkPortalEvent.FULL_EVENT_NAME,
                portal_event.MarkPortalEvent.__doc__,
                portal_event.MarkPortalEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        MARK_PORTAL__NAME,
                        'Alias of the portal', '',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
            MarkPortalHotkeyHandler(context),
        ),

        # move-window-to-portal
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.MoveWindowToPortalEvent.FULL_EVENT_NAME,
                portal_event.MoveWindowToPortalEvent.__doc__,
                portal_event.MoveWindowToPortalEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        MOVE_WINDOW__TARGET,
                        'The target portal to move the active window into.  This can either be '
                        'one of the reserved direction names, or a marked portal name.  '
                        'Reserved direction names are "previous", "next", "up", "down", '
                        '"left", "right", "north", "south", "east", "west".',
                        'next',
                    ),
                    hotkey_event.EventParameterDescription(
                        MOVE_WINDOW__MOVE_FOCUS,
                        'If "true", then the focused portal moves with the active window.  '
                        'If "false", then the focused portal remains focused, and the active '
                        'window becomes the next one in the current portal.',
                        'true',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
            MoveWindowToPortalHotkeyHandler(context),
        ),

        # focus-portal
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.FocusPortalEvent.FULL_EVENT_NAME,
                portal_event.FocusPortalEvent.__doc__,
                portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        FOCUS_PORTAL__TARGET,
                        'The target portal to move the active window into.  This can either be '
                        'one of the reserved direction names, or a marked portal name.  '
                        'Reserved direction names are "previous", "next", "up", "down", '
                        '"left", "right", "north", "south", "east", "west".',
                        None,
                    ),
                    hotkey_event.EventParameterDescription(
                        FOCUS_PORTAL__WRAP,
                        'One of "wrap-screen", "wrap-block", or "none"',
                        'wrap-screen',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
            FocusPortalHotkeyHandler(context),
        ),

        # rotate-active-window
        context.send_event(
            portal_event.EXTENSION_NAME + ':registration',
            hotkey_event.ExtensionEventRegisterEvent.UNIQUE_TARGET_FQN,
            hotkey_event.ExtensionEventRegisterEvent(
                portal_event.RotateActiveWindowEvent.FULL_EVENT_NAME,
                portal_event.RotateActiveWindowEvent.__doc__,
                portal_event.RotateActiveWindowEvent.UNIQUE_TARGET_FQN,
                [
                    hotkey_event.EventParameterDescription(
                        ROTATE_WINDOW__DIRECTION,
                        'Direction to rotate.  One of "backward" or "forward"',
                        'forward',
                    ),
                ],
            ),
        ),
        context.register_target(
            hotkey_event.HotkeyFiredEvent.FULL_EVENT_NAME,
            portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
            RotateActiveWindowHotkeyHandler(context),
        ),
    )


class SplitPortalHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Split hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_split_portal(
            context,
            get_bool(event, SPLIT_PORTAL__ADD_BEFORE, False),
            get_bool(event, SPLIT_PORTAL__FOCUS_NEW, False),
            get_bool(event, SPLIT_PORTAL__NEW_DIRECTION, False),
        ))
        return False


class JoinPortalsHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Join hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_join_portals(
            context,
            get_bool(event, JOIN_PORTALS__JOIN_BEFORE, False),
        ))
        return False


class FitWindowHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit window hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_fit_window(
            context,
            justify_horizontal=get_str(event, FIT__JUSTIFY_HORIZONTAL, 'left'),
            justify_vertical=get_str(event, FIT__JUSTIFY_VERTICAL, 'top'),
            fit_horizontal=get_str(event, FIT__FIT_HORIZONTAL, 'fit'),
            fit_vertical=get_str(event, FIT__FIT_VERTICAL, 'fit'),
        ))
        return False


class FitPortalWindowsHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_fit_portal_windows(
            context,
            justify_horizontal=get_str(event, FIT__JUSTIFY_HORIZONTAL, 'left'),
            justify_vertical=get_str(event, FIT__JUSTIFY_VERTICAL, 'top'),
            fit_horizontal=get_str(event, FIT__FIT_HORIZONTAL, 'fit'),
            fit_vertical=get_str(event, FIT__FIT_VERTICAL, 'fit'),
        ))
        return False


class ManageWindowHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_manage_window(
            context,
        ))
        return False


class UnmanageWindowHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_unmanage_window(
            context,
        ))
        return False


class AdjustPortalSizeHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_adjust_portal_size(
            context,
            get_str(event, ADJUST_PORTAL_SIZE__DIRECTION, 'horizontal'),
            get_int(event, ADJUST_PORTAL_SIZE__AMOUNT, 1),
        ))
        return False


class MarkPortalHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_mark_portal(
            context,
            get_str(event, MARK_PORTAL__NAME, ''),
        ))
        return False


class MoveWindowToPortalHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_move_window_to_portal(
            context,
            get_str(event, MOVE_WINDOW__TARGET, ''),
            get_bool(event, MOVE_WINDOW__MOVE_FOCUS, True),
        ))
        return False


class FocusPortalHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_focus_portal(
            context,
            get_str(event, FOCUS_PORTAL__TARGET, ''),
            get_str(event, FOCUS_PORTAL__WRAP, 'wrap-screen'),
        ))
        return False


class RotateActiveWindowHotkeyHandler(ContextEventObjectTarget[hotkey_event.HotkeyFiredEvent]):
    """Fit portal hotkey"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: hotkey_event.HotkeyFiredEvent,
    ) -> bool:
        report_send_receive_problems(portal_handler.handle_rotate_active_window(
            context,
            get_str(event, ROTATE_WINDOW__DIRECTION, ''),
        ))
        return False


def get_bool(event: hotkey_event.HotkeyFiredEvent, key: str, default_value: bool) -> bool:
    """Get the event key as a boolean"""
    for param in event.event.parameters:
        if param.key == key:
            # This needs to be put into the common lib.
            if param.value.lower() in ('1', 'yes', 'true', 'on', 'active', 'activated'):
                return True
            return False
    return default_value


def get_int(event: hotkey_event.HotkeyFiredEvent, key: str, default_value: int) -> int:
    """Get the event key as an int"""
    for param in event.event.parameters:
        if param.key == key:
            try:
                return int(param.value)
            except ValueError:
                pass
    return default_value


def get_str(event: hotkey_event.HotkeyFiredEvent, key: str, default_value: str) -> str:
    """Get the event key as a str"""
    for param in event.event.parameters:
        if param.key == key:
            # This needs to be put into the common lib.
            return param.value
    return default_value
