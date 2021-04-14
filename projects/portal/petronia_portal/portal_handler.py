"""Handle requests for portal events."""

from typing import List, Sequence
from petronia_common.util import StdRet, join_none_results, RET_OK_NONE
from petronia_ext_lib.extension_loader import send_register_listeners
from petronia_ext_lib.runner import EventRegistryContext, ContextEventObjectTarget
from . import shared_state, native_window_handler, tree
from .events import portal as portal_event
from .state import petronia_portal as portal_state
from .user_messages import report_send_receive_problems


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the portal listeners"""
    return join_none_results(
        send_register_listeners(
            context,
            portal_event.EXTENSION_NAME,
            (
                (
                    portal_event.SetLayoutEvent.FULL_EVENT_NAME,
                    portal_event.SetLayoutEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.SplitPortalEvent.FULL_EVENT_NAME,
                    portal_event.SplitPortalEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.JoinPortalsEvent.FULL_EVENT_NAME,
                    portal_event.JoinPortalsEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.FitWindowEvent.FULL_EVENT_NAME,
                    portal_event.FitWindowEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.FitPortalWindowsEvent.FULL_EVENT_NAME,
                    portal_event.FitPortalWindowsEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.ManageWindowEvent.FULL_EVENT_NAME,
                    portal_event.ManageWindowEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.UnmanageWindowEvent.FULL_EVENT_NAME,
                    portal_event.UnmanageWindowEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.AdjustPortalSizeEvent.FULL_EVENT_NAME,
                    portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.MarkPortalEvent.FULL_EVENT_NAME,
                    portal_event.MarkPortalEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.MoveWindowToPortalEvent.FULL_EVENT_NAME,
                    portal_event.MoveWindowToPortalEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.FocusPortalEvent.FULL_EVENT_NAME,
                    portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
                ),
                (
                    portal_event.RotateActiveWindowEvent.FULL_EVENT_NAME,
                    portal_event.RotateActiveWindowEvent.UNIQUE_TARGET_FQN,
                ),
            ),
        ),

        # set-layout
        context.register_event_parser(
            portal_event.SetLayoutEvent.FULL_EVENT_NAME,
            portal_event.SetLayoutEvent.parse_data,
        ),
        context.register_target(
            portal_event.SetLayoutEvent.FULL_EVENT_NAME,
            portal_event.SetLayoutEvent.UNIQUE_TARGET_FQN,
            SetLayoutEventHandler(context),
        ),

        # split-portal
        context.register_event_parser(
            portal_event.SplitPortalEvent.FULL_EVENT_NAME,
            portal_event.SplitPortalEvent.parse_data,
        ),
        context.register_target(
            portal_event.SplitPortalEvent.FULL_EVENT_NAME,
            portal_event.SplitPortalEvent.UNIQUE_TARGET_FQN,
            SplitPortalEventHandler(context),
        ),

        # join-portals
        context.register_event_parser(
            portal_event.JoinPortalsEvent.FULL_EVENT_NAME,
            portal_event.JoinPortalsEvent.parse_data,
        ),
        context.register_target(
            portal_event.JoinPortalsEvent.FULL_EVENT_NAME,
            portal_event.JoinPortalsEvent.UNIQUE_TARGET_FQN,
            JoinPortalsEventHandler(context),
        ),

        # fit-window
        context.register_event_parser(
            portal_event.FitWindowEvent.FULL_EVENT_NAME,
            portal_event.FitWindowEvent.parse_data,
        ),
        context.register_target(
            portal_event.FitWindowEvent.FULL_EVENT_NAME,
            portal_event.FitWindowEvent.UNIQUE_TARGET_FQN,
            FitWindowEventHandler(context),
        ),

        # fit-portal-windows
        context.register_event_parser(
            portal_event.FitPortalWindowsEvent.FULL_EVENT_NAME,
            portal_event.FitPortalWindowsEvent.parse_data,
        ),
        context.register_target(
            portal_event.FitPortalWindowsEvent.FULL_EVENT_NAME,
            portal_event.FitPortalWindowsEvent.UNIQUE_TARGET_FQN,
            FitPortalWindowsEventHandler(context),
        ),

        # manage-window
        context.register_event_parser(
            portal_event.ManageWindowEvent.FULL_EVENT_NAME,
            portal_event.ManageWindowEvent.parse_data,
        ),
        context.register_target(
            portal_event.ManageWindowEvent.FULL_EVENT_NAME,
            portal_event.ManageWindowEvent.UNIQUE_TARGET_FQN,
            ManageWindowEventHandler(context),
        ),

        # unmanage-window
        context.register_event_parser(
            portal_event.UnmanageWindowEvent.FULL_EVENT_NAME,
            portal_event.UnmanageWindowEvent.parse_data,
        ),
        context.register_target(
            portal_event.UnmanageWindowEvent.FULL_EVENT_NAME,
            portal_event.UnmanageWindowEvent.UNIQUE_TARGET_FQN,
            UnmanageWindowEventHandler(context),
        ),

        # adjust-portal-size
        context.register_event_parser(
            portal_event.AdjustPortalSizeEvent.FULL_EVENT_NAME,
            portal_event.AdjustPortalSizeEvent.parse_data,
        ),
        context.register_target(
            portal_event.AdjustPortalSizeEvent.FULL_EVENT_NAME,
            portal_event.AdjustPortalSizeEvent.UNIQUE_TARGET_FQN,
            AdjustPortalSizeEventHandler(context),
        ),

        # mark-portal
        context.register_event_parser(
            portal_event.MarkPortalEvent.FULL_EVENT_NAME,
            portal_event.MarkPortalEvent.parse_data,
        ),
        context.register_target(
            portal_event.MarkPortalEvent.FULL_EVENT_NAME,
            portal_event.MarkPortalEvent.UNIQUE_TARGET_FQN,
            MarkPortalEventHandler(context),
        ),

        # move-window-to-portal
        context.register_event_parser(
            portal_event.MoveWindowToPortalEvent.FULL_EVENT_NAME,
            portal_event.MoveWindowToPortalEvent.parse_data,
        ),
        context.register_target(
            portal_event.MoveWindowToPortalEvent.FULL_EVENT_NAME,
            portal_event.MoveWindowToPortalEvent.UNIQUE_TARGET_FQN,
            MoveWindowToPortalEventHandler(context),
        ),

        # focus-portal
        context.register_event_parser(
            portal_event.FocusPortalEvent.FULL_EVENT_NAME,
            portal_event.FocusPortalEvent.parse_data,
        ),
        context.register_target(
            portal_event.FocusPortalEvent.FULL_EVENT_NAME,
            portal_event.FocusPortalEvent.UNIQUE_TARGET_FQN,
            FocusPortalEventHandler(context),
        ),

        # rotate-active-window
        context.register_event_parser(
            portal_event.RotateActiveWindowEvent.FULL_EVENT_NAME,
            portal_event.RotateActiveWindowEvent.parse_data,
        ),
        context.register_target(
            portal_event.RotateActiveWindowEvent.FULL_EVENT_NAME,
            portal_event.RotateActiveWindowEvent.UNIQUE_TARGET_FQN,
            RotateActiveWindowEventHandler(context),
        ),
    )


class SetLayoutEventHandler(ContextEventObjectTarget[portal_event.SetLayoutEvent]):
    """Set layout event handler."""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.SetLayoutEvent,
    ) -> bool:
        print("[PORTAL] event to set the layout handler.")
        return False


class SplitPortalEventHandler(ContextEventObjectTarget[portal_event.SplitPortalEvent]):
    """Split the active portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.SplitPortalEvent,
    ) -> bool:
        report_send_receive_problems(handle_split_portal(
            context, event.add_before, event.focus_new, event.new_direction,
        ))
        return False


def handle_split_portal(
        context: EventRegistryContext,
        add_before: bool,
        focus_new: bool,
        new_direction: bool,
) -> StdRet[None]:
    """Handle a request to split the active portal."""
    active_portal_id = shared_state.get_active_portal_id()
    res = shared_state.layout_root().split_portal(
        active_portal_id,
        add_before, new_direction,
    )
    # TODO need to also capture the new active portal ID, so that focus_new can be
    #   correctly used.
    return native_window_handler.send_move_windows_event(context, res)


class JoinPortalsEventHandler(ContextEventObjectTarget[portal_event.JoinPortalsEvent]):
    """Join the active portal with another."""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.JoinPortalsEvent,
    ) -> bool:
        report_send_receive_problems(handle_join_portals(context, event.join_before))
        return False


def handle_join_portals(context: EventRegistryContext, join_before: bool) -> StdRet[None]:
    """Handle a request to join the active portal with an adjacent one."""
    active_portal_id = shared_state.get_active_portal_id()
    res = shared_state.layout_root().join_portals(
        active_portal_id, join_before,
    )
    return native_window_handler.send_move_windows_event(context, res)


class FitWindowEventHandler(ContextEventObjectTarget[portal_event.FitWindowEvent]):
    """Fit the active window within the portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.FitWindowEvent,
    ) -> bool:
        report_send_receive_problems(handle_fit_window(
            context,
            event.position.justify_horizontal,
            event.position.justify_vertical,
            event.position.fit_horizontal,
            event.position.fit_vertical,
        ))
        return False


def handle_fit_window(
        context: EventRegistryContext,
        justify_horizontal: str, justify_vertical: str,
        fit_horizontal: str, fit_vertical: str,
) -> StdRet[None]:
    """Handle the fit window request."""
    window_id = shared_state.get_focused_window_id()
    if window_id:
        res = shared_state.layout_root().refit_window_in_portal(
            window_id,
            portal_state.WindowPortalFit(
                justify_horizontal=justify_horizontal,
                justify_vertical=justify_vertical,
                fit_horizontal=fit_horizontal,
                fit_vertical=fit_vertical,
            ),
        )
        return native_window_handler.send_move_windows_event(context, res)
    return RET_OK_NONE


class FitPortalWindowsEventHandler(ContextEventObjectTarget[portal_event.FitPortalWindowsEvent]):
    """Fit all windows within the active portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.FitPortalWindowsEvent,
    ) -> bool:
        report_send_receive_problems(handle_fit_portal_windows(
            context,
            event.position.justify_horizontal, event.position.justify_vertical,
            event.position.fit_horizontal, event.position.fit_vertical,
        ))
        return False


def handle_fit_portal_windows(
        context: EventRegistryContext,
        justify_horizontal: str, justify_vertical: str,
        fit_horizontal: str, fit_vertical: str,
) -> StdRet[None]:
    """Handle the fit window request."""
    active_portal_id = shared_state.get_active_portal_id()
    active_portal = shared_state.layout_root().get_portal_by_id(active_portal_id)
    if active_portal:
        resized_windows: List[tree.KnownWindow] = []
        for wid in active_portal.get_contained_windows():
            resized_windows.extend(
                shared_state.layout_root().refit_window_in_portal(
                    wid,
                    portal_state.WindowPortalFit(
                        justify_horizontal=justify_horizontal,
                        justify_vertical=justify_vertical,
                        fit_horizontal=fit_horizontal,
                        fit_vertical=fit_vertical,
                    ),
                )
            )
        return native_window_handler.send_move_windows_event(context, resized_windows)
    return RET_OK_NONE


class ManageWindowEventHandler(ContextEventObjectTarget[portal_event.ManageWindowEvent]):
    """Make the focused window managed"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.ManageWindowEvent,
    ) -> bool:
        report_send_receive_problems(handle_manage_window(context))
        return False


def handle_manage_window(context: EventRegistryContext) -> StdRet[None]:
    """Handle the request to manage the focused window."""
    window_id = shared_state.get_focused_window_id()
    active_portal_id = shared_state.get_active_portal_id()
    res = shared_state.layout_root().move_window_to_portal_id(
        window_id, active_portal_id, True, True,
    )
    return native_window_handler.send_move_windows_event(context, res)


class UnmanageWindowEventHandler(ContextEventObjectTarget[portal_event.UnmanageWindowEvent]):
    """Unmanage the focused window."""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.UnmanageWindowEvent,
    ) -> bool:
        report_send_receive_problems(handle_unmanage_window(context))
        return False


def handle_unmanage_window(context: EventRegistryContext) -> StdRet[None]:
    """Handle the request to unmanage the focused window."""
    window_id = shared_state.get_focused_window_id()
    res = shared_state.layout_root().remove_window(window_id, False)
    return native_window_handler.send_move_windows_event(context, res)


class AdjustPortalSizeEventHandler(ContextEventObjectTarget[portal_event.AdjustPortalSizeEvent]):
    """Adjust the size of the active portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.AdjustPortalSizeEvent,
    ) -> bool:
        report_send_receive_problems(handle_adjust_portal_size(
            context, event.direction, event.amount,
        ))
        return False


def handle_adjust_portal_size(
        context: EventRegistryContext,
        direction: str, amount: int,
) -> StdRet[None]:
    """Handle the adjust portal size request."""
    delta_x = 0
    delta_y = 0
    if direction == 'vertical':
        delta_y = amount
    elif direction == 'horizontal':
        delta_x = amount
    else:
        # Send a user error?
        return RET_OK_NONE
    active_portal_id = shared_state.get_active_portal_id()
    res = shared_state.layout_root().change_portal_size(active_portal_id, delta_x, delta_y)
    # FIXME re-send portal states
    return native_window_handler.send_move_windows_event(context, res)


class MarkPortalEventHandler(ContextEventObjectTarget[portal_event.MarkPortalEvent]):
    """Assign a mark to the active portal."""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.MarkPortalEvent,
    ) -> bool:
        report_send_receive_problems(handle_mark_portal(context, event.name))
        return False


def handle_mark_portal(_context: EventRegistryContext, name: str) -> StdRet[None]:
    """Handle the assign a portal a mark."""
    active_portal_id = shared_state.get_active_portal_id()
    active_portal = shared_state.layout_root().get_portal_by_id(active_portal_id)
    old_alias_portal = shared_state.layout_root().get_portal_by_alias(name)
    if old_alias_portal:
        # TODO send portal state update
        old_alias_portal.remove_alias(name)

    if active_portal:
        # TODO send portal state update
        active_portal.add_alias(name)

    return RET_OK_NONE


class MoveWindowToPortalEventHandler(ContextEventObjectTarget[portal_event.MoveWindowToPortalEvent]):
    """Move the focused window to another portal."""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.MoveWindowToPortalEvent,
    ) -> bool:
        report_send_receive_problems(handle_move_window_to_portal(
            context, event.target, event.move_focus,
        ))
        return False


def handle_move_window_to_portal(
        context: EventRegistryContext, target: str, move_focus: bool,
) -> StdRet[None]:
    """Handle the request to move the window to another portal"""
    window_id = shared_state.get_focused_window_id()
    active_portal_id = shared_state.get_active_portal_id()
    active_portal = shared_state.layout_root().get_portal_by_id(active_portal_id)
    target_portal_id = shared_state.layout_root().get_target_portal(active_portal_id, target)
    if target_portal_id >= 0:
        res = shared_state.layout_root().move_window_to_portal_id(
            window_id, target_portal_id, True, False,
        )
        res_focus: StdRet[None]
        if move_focus:
            shared_state.set_active_portal_id(target_portal_id)
            res_focus = native_window_handler.send_set_window_focused_event(context, window_id)
        elif active_portal and active_portal.window_order:
            res_focus = native_window_handler.send_set_window_focused_event(
                context, active_portal.window_order[0],
            )
        else:
            res_focus = RET_OK_NONE
        return join_none_results(
            res_focus,
            native_window_handler.send_move_windows_event(context, res)
        )
    return RET_OK_NONE


class FocusPortalEventHandler(ContextEventObjectTarget[portal_event.FocusPortalEvent]):
    """Move the focus to a different portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.FocusPortalEvent,
    ) -> bool:
        report_send_receive_problems(handle_focus_portal(context, event.target, event.wrap))
        return False


def handle_focus_portal(context: EventRegistryContext, target: str, _wrap: str) -> StdRet[None]:
    """Handle a request to move the focused portal."""
    active_portal_id = shared_state.get_active_portal_id()
    # TODO include wrap mode in search
    target_portal_id = shared_state.layout_root().get_target_portal(active_portal_id, target)
    if target_portal_id >= 0:
        shared_state.set_active_portal_id(target_portal_id)
        # TODO update portal state
        target_portal = shared_state.layout_root().get_portal_by_id(target_portal_id)
        if target_portal and target_portal.window_order:
            return native_window_handler.send_set_window_focused_event(
                context, target_portal.window_order[0],
            )
    return RET_OK_NONE


class RotateActiveWindowEventHandler(ContextEventObjectTarget[portal_event.RotateActiveWindowEvent]):
    """Rotate through the windows in the current portal"""
    def on_context_event(
            self, context: EventRegistryContext,
            source: str, target: str, event: portal_event.RotateActiveWindowEvent,
    ) -> bool:
        report_send_receive_problems(handle_rotate_active_window(context, event.direction))
        return False


def handle_rotate_active_window(context: EventRegistryContext, direction: str) -> StdRet[None]:
    """Handle rotating the focused windows within the active portal."""
    active_portal_id = shared_state.get_active_portal_id()
    active_portal = shared_state.layout_root().get_portal_by_id(active_portal_id)
    res: Sequence[tree.KnownWindow] = []
    if active_portal:
        if direction.lower() in ('forward', 'forwards'):
            res = active_portal.rotate_windows_forward()
        elif direction.lower() in ('backward', 'backwards', 'reverse'):
            res = active_portal.rotate_windows_backward()
    if res:
        return native_window_handler.send_set_window_focused_event(context, res[0])
    return RET_OK_NONE
