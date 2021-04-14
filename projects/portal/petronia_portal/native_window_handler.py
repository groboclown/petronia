"""Handles events that come from the native window extension."""

from typing import Sequence, Union, Optional
from petronia_common.util import StdRet, join_none_results, RET_OK_NONE
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import (
    EventRegistryContext, ContextEventObjectTarget, EventObjectParser,
)
from petronia_ext_lib.datastore import get_event_data_value, send_request_data_state
from petronia_ext_lib.events import datastore as datastore_event
from . import tree, shared_state
from .state import petronia_portal as portal_state
from .events import window as window_event
from .user_messages import report_send_receive_problems


BASE_WINDOW_TARGET_ID = f'{window_event.EXTENSION_NAME}:wid:'


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the handler."""
    return join_none_results(
        send_register_listeners(
            context,
            portal_state.EXTENSION_NAME,
            (
                (
                    window_event.WindowCreatedEvent.FULL_EVENT_NAME,
                    window_event.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowDestroyedEvent.FULL_EVENT_NAME,
                    window_event.WindowDestroyedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowFlashedEvent.FULL_EVENT_NAME,
                    window_event.WindowFlashedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    window_event.WindowFocusedEvent.FULL_EVENT_NAME,
                    window_event.WindowFocusedEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
                    None,
                ),
            ),
        ),

        context.register_event_parser(
            window_event.WindowCreatedEvent.FULL_EVENT_NAME,
            window_event.WindowCreatedEvent.parse_data,
        ),
        context.register_target(
            window_event.WindowCreatedEvent.FULL_EVENT_NAME,
            window_event.WindowCreatedEvent.UNIQUE_TARGET_FQN,
            WindowCreatedHandler(context),
        ),

        context.register_event_parser(
            window_event.WindowDestroyedEvent.FULL_EVENT_NAME,
            window_event.WindowDestroyedEvent.parse_data,
        ),
        context.register_target(
            window_event.WindowDestroyedEvent.FULL_EVENT_NAME,
            window_event.WindowDestroyedEvent.UNIQUE_TARGET_FQN,
            WindowDestroyedHandler(context),
        ),

        context.register_event_parser(
            window_event.WindowFlashedEvent.FULL_EVENT_NAME,
            window_event.WindowFlashedEvent.parse_data,
        ),
        context.register_target(
            window_event.WindowFlashedEvent.FULL_EVENT_NAME,
            window_event.WindowFlashedEvent.UNIQUE_TARGET_FQN,
            WindowFlashedHandler(context),
        ),

        context.register_event_parser(
            window_event.WindowFocusedEvent.FULL_EVENT_NAME,
            window_event.WindowFocusedEvent.parse_data,
        ),
        context.register_target(
            window_event.WindowFocusedEvent.FULL_EVENT_NAME,
            window_event.WindowFocusedEvent.UNIQUE_TARGET_FQN,
            WindowFocusedHandler(context),
        ),

        # Initial startup issue:
        # Need to register for when the windows are created, in case the initial
        # window creation event is missed.
        context.register_target(
            datastore_event.DataUpdateEvent.FULL_EVENT_NAME,
            None, DataStoreUpdate(context),
        ),
        # Ensure the data is sent
        send_request_data_state(
            context, portal_state.EXTENSION_NAME + ':registration',
            window_event.ActiveWindowsState.UNIQUE_TARGET_FQN,
        ),
    )


class WindowCreatedHandler(ContextEventObjectTarget[window_event.WindowCreatedEvent]):
    """Handle window created events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowCreatedEvent,
    ) -> bool:
        print(f"[PORTAL] Detected window creation {target}")
        # TODO see if the window has a configuration.  If so, use that portal target
        #   and fit.
        shared_state.layout_root().register_window(
            target,
            None,  # TODO match window info to a fit.
            event.state,
        )
        active_portal_id = shared_state.get_active_portal_id()
        res = shared_state.layout_root().move_window_to_portal_id(
            target, active_portal_id, True, True,
        )
        report_send_receive_problems(send_move_windows_event(context, res))
        return False


class WindowDestroyedHandler(ContextEventObjectTarget[window_event.WindowDestroyedEvent]):
    """Handle window destroyed events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowDestroyedEvent,
    ) -> bool:
        print(f"[PORTAL] Detected window destroyed {target}")
        shared_state.layout_root().remove_window(target, True)
        return False


class WindowFlashedHandler(ContextEventObjectTarget[window_event.WindowFlashedEvent]):
    """Handle window flashed events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowFlashedEvent,
    ) -> bool:
        print(f"[PORTAL NOT IMPLEMENTED] Detected window flashed {target}")
        return False


class WindowFocusedHandler(ContextEventObjectTarget[window_event.WindowFocusedEvent]):
    """Handle window focus events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowFocusedEvent,
    ) -> bool:
        print(f"[PORTAL] Detected window focused {target}")
        if event.keyboard_focus >= 0:
            shared_state.set_focused_window_id(target)
            nkw = shared_state.layout_root().get_window_by_id(target)
            if nkw and nkw.owning_portal_id >= 0:
                # TODO set the active portal state
                shared_state.set_active_portal_id(nkw.owning_portal_id)
        return False


class DataStoreUpdate(ContextEventObjectTarget[datastore_event.DataUpdateEvent]):
    """Handles datastore update events."""
    ACTIVE_WINDOW_PARSER = EventObjectParser(window_event.ActiveWindowsState.parse_data)
    WINDOW_STATE_PARSER = EventObjectParser(window_event.WindowState.parse_data)

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.DataUpdateEvent,
    ) -> bool:
        if target == window_event.ActiveWindowsState.UNIQUE_TARGET_FQN:
            active_res = get_event_data_value(event, DataStoreUpdate.ACTIVE_WINDOW_PARSER)
            if active_res.has_error:
                # Logging?
                report_send_receive_problems(active_res)
            else:
                # If there are any window IDs here that are not known, then a create was
                # missed, and the get-data for its state should be sent.
                print(
                    f'[PORTAL NOT IMPLEMENTED] received active window IDs: '
                    f'{active_res.result.active_ids}'
                )
        elif target.startswith(BASE_WINDOW_TARGET_ID):
            window_res = get_event_data_value(event, DataStoreUpdate.WINDOW_STATE_PARSER)
            if window_res.has_error:
                # Logging?
                report_send_receive_problems(window_res)
            else:
                # If the window ID is not known, then create the window.  Otherwise, ignore it.
                print(f'[PORTAL NOT IMPLEMENTED] received window state ID: {target}')

        return False


def on_active_window_ids_changed(active_ids: Optional[window_event.ActiveWindowsState]) -> None:
    """Callback for when the active window IDs data changes."""
    if not active_ids:
        return
    print(f"[PORTAL NOT IMPLEMENTED] active window IDs: {active_ids.active_ids}")
    # If an active ID is not in the list of known windows, send out a request to get the
    # data store update.


def send_move_windows_event(
        context: EventRegistryContext, changed_windows: Sequence[tree.KnownWindow],
) -> StdRet[None]:
    """Move the windows to a new position."""
    if not changed_windows:
        return RET_OK_NONE

    return context.send_event(
        portal_state.EXTENSION_NAME + ':move-windows',
        window_event.SetWindowPositionsEvent.UNIQUE_TARGET_FQN,
        window_event.SetWindowPositionsEvent([
            window_event.WindowIdPositions(
                known.target_id,
                window_event.ScreenDimension(
                    known.pos_x, known.pos_y, known.pos_w, known.pos_h,
                ),
            )
            for known in changed_windows
        ]),
    )


def send_set_window_focused_event(
        context: EventRegistryContext, focused_window: Union[str, tree.KnownWindow],
) -> StdRet[None]:
    """Set the given window as having focus."""
    window_id: str
    if isinstance(focused_window, tree.KnownWindow):
        window_id = focused_window.target_id
    else:
        window_id = focused_window
    return context.send_event(
        portal_state.EXTENSION_NAME + ':focus-window',
        window_id,
        window_event.SetFocusedWindowEvent(0),
    )
