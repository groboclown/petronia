"""Handles events that come from the native window extension."""

from typing import Sequence, List, Tuple, Union, Optional
from petronia_common.util import StdRet, join_none_results, RET_OK_NONE
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import (
    EventRegistryContext, ContextEventObjectTarget, EventObjectParser,
)
from petronia_ext_lib.datastore import get_event_data_value, send_request_data_state
from petronia_ext_lib.events import datastore as datastore_event
from . import tree, shared_state, config_matcher
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

        report_send_receive_problems(update_window_state(context, target, event.state))
        return False


class WindowDestroyedHandler(ContextEventObjectTarget[window_event.WindowDestroyedEvent]):
    """Handle window destroyed events."""

    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: window_event.WindowDestroyedEvent,
    ) -> bool:
        print(f"[PORTAL] Detected window destroyed {target}")
        with shared_state.layout_root() as root:
            root.remove_window(target, True)
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
            report_send_receive_problems(update_window_focus(target))
        return False


class DataStoreUpdate(ContextEventObjectTarget[datastore_event.DataUpdateEvent]):
    """Handles datastore update events."""
    ACTIVE_WINDOW_PARSER = EventObjectParser(window_event.ActiveWindowsState.parse_data)
    WINDOW_STATE_PARSER = EventObjectParser(window_event.WindowDetailsState.parse_data)

    def on_context_event(
            self, context: EventRegistryContext, source: str, target: str,
            event: datastore_event.DataUpdateEvent,
    ) -> bool:
        if target == window_event.ActiveWindowsState.UNIQUE_TARGET_FQN:
            active_res = get_event_data_value(event, DataStoreUpdate.ACTIVE_WINDOW_PARSER)
            if active_res.has_error:
                # Logging?
                print(f'[PORTAL] Format error for event data: {event.json}')
                report_send_receive_problems(active_res)
            else:
                report_send_receive_problems(on_active_window_ids_changed(
                    context, active_res.result,
                ))
        elif target.startswith(BASE_WINDOW_TARGET_ID):
            window_res = get_event_data_value(event, DataStoreUpdate.WINDOW_STATE_PARSER)
            if window_res.has_error:
                # Logging?
                print(f'[PORTAL] Format error for event {target}: {event.json}')
                report_send_receive_problems(window_res)
            else:
                on_window_state_change(context, target, window_res.result.state)

        # Though this one is stored in the state, the focus event is tracked instead.
        # window_events.FocusedWindowsState.UNIQUE_TARGET_FQN
        # For the initialization problem (at startup, which window has focus?), that's tracked by
        # the window state collection above.

        return False


def on_active_window_ids_changed(
        context: EventRegistryContext,
        active_ids: Optional[window_event.ActiveWindowsState],
) -> StdRet[None]:
    """Handler for when the active window IDs data changes."""
    if not active_ids:
        return RET_OK_NONE
    print(f"[PORTAL] active window IDs updated")
    ret: List[StdRet[None]] = []
    # If an active ID is not in the list of known windows, send out a request to get the
    # data store update.
    with shared_state.layout_root() as root:
        for active_id in active_ids.active_ids:
            window = root.get_window_by_id(active_id.window_id)
            if not window:
                ret.append(send_request_data_state(
                    context, portal_state.EXTENSION_NAME + ':window-state', active_id.window_id,
                ))
    return join_none_results(*ret)


def on_window_state_change(
        context: EventRegistryContext,
        window_id: str, window_state: window_event.WindowState,
) -> StdRet[None]:
    """Handler for when a window state changes."""
    print(f"[PORTAL] encountered window state for {window_id}")
    res_window = update_window_state(context, window_id, window_state)
    if res_window.has_error:
        return res_window.forward()

    # If the window has the focus value set, then update focused window information.
    if window_state.focus >= 0:
        res_focus = update_window_focus(window_id)
        if res_focus.has_error:
            return res_focus
    return RET_OK_NONE


def update_window_focus(new_focused_window_id: str) -> StdRet[None]:
    """Update the focus to a new window."""
    old_focused_window_id = shared_state.get_focused_window_id()
    if new_focused_window_id == old_focused_window_id:
        # Nothing to do
        return RET_OK_NONE

    with shared_state.layout_root() as root:
        nkw = root.get_window_by_id(new_focused_window_id)
        if not nkw:
            return RET_OK_NONE
        shared_state.set_focused_window_id(nkw.target_id)
        owning_portal = root.get_portal_by_id(nkw.owning_portal_id)
        if not owning_portal:
            # Not managed...
            return RET_OK_NONE

    shared_state.set_active_portal_id(owning_portal.portal_id)
    # TODO send the active portal state
    return RET_OK_NONE


def update_window_state(
        context: EventRegistryContext,
        window_id: str, state: window_event.WindowState,
) -> StdRet[tree.KnownWindow]:
    """Register a window, or update an existing one."""
    with shared_state.layout_root() as root:
        known_window = root.get_window_by_id(window_id)
        if not known_window:
            # Find appropriate window matchers for it, and which portal it's assigned to.
            fit, assigned_portal_id, managed = get_window_setup(state)

            known_window = root.register_window(
                window_id,
                fit,
                state,
            )
            print(f'[PORTAL] created window for {window_id}; moving into portal {assigned_portal_id}')
            res = send_move_windows_event(
                context,
                root.move_window_to_portal_id(
                    window_id, assigned_portal_id, True, managed,
                ),
            )
            if res.has_error:
                return res.forward()
        else:
            print(f'[PORTAL] updating state for known window {window_id}')
            known_window.update_native_state(state)

    if not known_window:  # pragma no cover
        raise ValueError('register window returned None?')  # pragma no cover
    return StdRet.pass_ok(known_window)


def send_move_windows_event(
        context: EventRegistryContext, changed_windows: Sequence[tree.KnownWindow],
) -> StdRet[None]:
    """Move the windows to a new position."""
    if not changed_windows:
        return RET_OK_NONE

    window_positions = [
        window_event.WindowIdPositions(
            known.target_id,
            window_event.ScreenDimension(
                known.pos_x, known.pos_y, known.pos_w, known.pos_h,
            ),
        )
        for known in changed_windows
    ]
    print(f'[PORTAL] moving windows: {[w.export_data() for w in window_positions]}')
    return context.send_event(
        portal_state.EXTENSION_NAME + ':move-windows',
        window_event.SetWindowPositionsEvent.UNIQUE_TARGET_FQN,
        window_event.SetWindowPositionsEvent(window_positions),
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


def get_window_setup(window: window_event.WindowState) -> Tuple[
    Optional[portal_state.WindowPortalFit], int, bool,
]:
    """Match the window to the configuration's window matchers.  Returns the
    matching user-defined portal fit (if any), the portal to assign it to,
    and whether to manage it."""
    fit: Optional[portal_state.WindowPortalFit] = None
    portal_id = -1
    managed = True
    with shared_state.layout_root() as root:
        for matcher in shared_state.configuration().default_window_behavior:
            if config_matcher.is_window_match(window, matcher):
                # Found a matcher.
                if matcher.initial_portal:
                    matching_portal = root.get_portal_by_alias(matcher.initial_portal)
                    if matching_portal:
                        portal_id = matching_portal.portal_id
                fit = matcher.fit or fit
                if matcher.managed is not None:
                    managed = matcher.managed
                # Keep looking.  Should have a closest match, maybe?
        if portal_id == -1:
            portal_id = root.get_default_portal().portal_id
    return fit, portal_id, managed
