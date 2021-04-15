"""Handles native virtual screen change updates."""

from typing import Sequence, Iterable, Callable, Optional
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_ext_lib.datastore import (
    InitCachedInstance,
)
from petronia_ext_lib.runner import EventRegistryContext
from . import shared_state, tree, native_window_handler, user_messages, config_matcher, data_store_reader
from .state import screen as screen_state
from .state import petronia_portal as portal_state


def setup(context: EventRegistryContext) -> StdRet[None]:
    """Setup the handler."""
    data_store_reader.get_cache_store().add_instance_cache(InitCachedInstance(
        screen_state.VirtualScreenState.UNIQUE_TARGET_FQN,
        screen_state.VirtualScreenState.parse_data,
        create_on_virtual_screen_changed(context),
    ))
    return RET_OK_NONE


def create_on_virtual_screen_changed(
        context: EventRegistryContext,
) -> Callable[[Optional[screen_state.VirtualScreenState]], None]:
    def on_virtual_screen_changed(
            v_screen: Optional[screen_state.VirtualScreenState],
    ) -> None:
        """Callback for when the virtual screen data changes."""
        if not v_screen:
            print(f'[PORTAL] virtual screens changed: no virtual screens')
            return
        print(f'[PORTAL] virtual screens changed: {v_screen.export_data()}')

        with shared_state.layout_root() as root:
            changed_windows = root.change_screen_layout(
                config_matcher.get_screen_workspace(
                    shared_state.configuration().workspaces,
                    v_screen.area,
                ),
                get_assigned_windows,
            )
        user_messages.report_send_receive_problems(
            native_window_handler.send_move_windows_event(context, changed_windows)
        )
    return on_virtual_screen_changed


def get_assigned_windows(
        portal: portal_state.Portal,
        available_windows: Sequence[tree.KnownWindow],
) -> Iterable[tree.KnownWindow]:
    """Find the windows that should be assigned to this portal"""
    portal_matchers = tuple(config_matcher.get_portal_matchers(
        portal, shared_state.configuration().default_window_behavior,
    ))
    for window in available_windows:
        # The window must already be managed, and the matcher must be for managed windows.
        if not window.managed:
            continue
        for matcher in portal_matchers:
            if not matcher.managed:
                continue
            if config_matcher.is_window_match(window.managed_native_state, matcher):
                yield window
