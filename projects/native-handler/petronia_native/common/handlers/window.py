"""Handler for Petronia events with native windows."""

from typing import Iterable, Sequence, List, Mapping, Dict, Optional, Generic, TypeVar, Hashable
from petronia_common.util import StdRet, join_none_results, RET_OK_NONE, T
from petronia_common.util import i18n as _
from petronia_ext_lib import datastore, logging
from petronia_ext_lib.runner import EventRegistryContext, EventObjectTarget
from petronia_native.common import defs, user_messages
from ..events.impl import window as window_events


def store_active_windows_state(
        context: EventRegistryContext,
        window_ids: Iterable[str],
) -> StdRet[None]:
    """Store the state of the active windows into the datastore."""
    return datastore.send_store_data(
        context,
        window_events.ActiveWindowsState.UNIQUE_TARGET_FQN,
        window_events.ActiveWindowsState([
            window_events.ActiveIds(wid)
            for wid in window_ids
        ]),
    )


def store_focused_windows_state(
        context: EventRegistryContext,
        focus_groups: Sequence[str],
) -> StdRet[None]:
    """Store the list of windows that have focus into the datastore."""
    return datastore.send_store_data(
        context,
        window_events.FocusedWindowsState.UNIQUE_TARGET_FQN,
        window_events.FocusedWindowsState(list(focus_groups)),
    )


def store_window_details(
        context: EventRegistryContext,
        window_id: str,
        window_state: window_events.WindowState,
) -> StdRet[None]:
    """Store the details for a single window into the datastore."""
    return datastore.send_store_data(
        context,
        window_id,
        window_events.WindowDetailsState(window_state),
    )


def store_global_settings(
        context: EventRegistryContext,
        settings: Mapping[str, str],
        meta_description: Mapping[str, str],
) -> StdRet[None]:
    """Store the global settings into the datastore."""
    return datastore.send_store_data(
        context,
        window_events.GlobalSettingsState.UNIQUE_TARGET_FQN,
        window_events.GlobalSettingsState([
                window_events.NativeMetaValue(key, meta_description.get(key), val)
                for key, val in settings.items()
        ]),
    )


def create_window_state(
        is_active: bool,
        has_focus: int,
        parent_id: Optional[str],
        location: defs.ScreenRect,
        minimized: bool,
        meta: Mapping[str, str],
        meta_description: Mapping[str, str],
) -> window_events.WindowState:
    """Create a window details state object."""
    return window_events.WindowState(
        active=is_active,
        focus=has_focus,
        parent_id=parent_id,
        location=window_events.ScreenDimension(
            location.x, location.y, location.width, location.height,
        ),
        minimized=minimized,
        meta=[
            window_events.NativeMetaValue(key, meta_description.get(key), val)
            for key, val in meta.items()
        ],
    )


def send_window_created_event(
        context: EventRegistryContext,
        window_id: str,
        window_state: window_events.WindowState,
) -> StdRet[None]:
    """Store the state data, and send a window created event notification."""
    return join_none_results(
        store_window_details(context, window_id, window_state),
        context.send_event(
            window_id,
            window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
            window_events.WindowCreatedEvent(window_state),
        ),
    )


def send_window_destroyed_event(
        context: EventRegistryContext,
        window_id: str,
        reason: str,
) -> StdRet[None]:
    """Remove the state data, and send a window destroyed event notification."""
    return join_none_results(
        context.send_event(
            window_id,
            window_events.WindowDestroyedEvent.UNIQUE_TARGET_FQN,
            window_events.WindowDestroyedEvent(reason),
        ),
        datastore.send_delete_data(context, window_id),
    )


def send_window_focused_event(
        context: EventRegistryContext,
        focus_group: int,
        new_focused_window_id: str,
        new_focused_state: Optional[window_events.WindowState],
        old_focused_window_id: Optional[str],
        old_focused_state: Optional[window_events.WindowState],
) -> StdRet[None]:
    """Update the window's state to be the new focus group, and send a focus event."""
    res: List[StdRet[None]] = []
    if old_focused_window_id and old_focused_state:
        old_focused_state.focus = -1
        res.append(datastore.send_store_data(context, old_focused_window_id, old_focused_state))
    if new_focused_window_id and new_focused_state:
        new_focused_state.focus = focus_group
        res.append(datastore.send_store_data(context, new_focused_window_id, new_focused_state))
        res.append(context.send_event(
            new_focused_window_id,
            window_events.WindowFocusedEvent.UNIQUE_TARGET_FQN,
            window_events.WindowFocusedEvent(focus_group),
        ))
    return join_none_results(*res)


def send_window_flashed_event(
        context: EventRegistryContext,
        window_id: str,
) -> StdRet[None]:
    """Send the event that the window is notifying the user for input."""
    return context.send_event(
        window_id,
        window_events.WindowFlashedEvent.UNIQUE_TARGET_FQN,
        window_events.WindowFlashedEvent(),
    )


def send_no_window_id_log_message(
        context: EventRegistryContext,
        source_id: str,
        window_id: str,
        request: str,
) -> StdRet[None]:
    """Send a logging event to inform the user that the requested window is not
    active."""
    return logging.send_user_error(
        context,
        source_id,
        StdRet.pass_errmsg(
            user_messages.TRANSLATION_CATALOG,
            _('request to {request} failed because window {wid} is not active'),
            wid=window_id,
            request=request,
        ).valid_error,
        'window-not-active',
    )


class ActiveWindow(Generic[T]):
    """An active window state."""
    __slots__ = ('__wid', '__int_id', '__hash_id', '__state')

    def __init__(
            self,
            window_id: str,
            native_id: T,
            hashable_native: Hashable,
            state: window_events.WindowState,
    ) -> None:
        self.__wid = window_id
        self.__int_id: T = native_id
        self.__hash_id = hashable_native
        self.__state = state

    @property
    def window_id(self) -> str:
        """Get the window ID."""
        return self.__wid

    @property
    def state(self) -> window_events.WindowState:
        """Get the window state (mutable)."""
        return self.__state

    @property
    def native_id(self) -> T:
        """Get the internal object identification of the native window."""
        return self.__int_id

    @property
    def hashable_native_id(self) -> Hashable:
        """Get the internal object identification of the native window in a type that
        can be used as a dictionary key."""
        return self.__hash_id


NativeWindow = TypeVar('NativeWindow', bound=ActiveWindow)


class AbstractWindowHandler(Generic[NativeWindow, T]):
    """Manages the window state according to Petronia events."""
    __slots__ = (
        '__context',
        '__active_windows_by_id', '__active_windows_by_native_id',
        '__focused', '__global_settings',
        '__global_meta_desc', '__window_meta_desc', '__next_id',
    )

    def __init__(
            self,
            initial_global_settings: Mapping[str, str],
            global_meta_desc: Mapping[str, str],
            window_meta_desc: Mapping[str, str],
    ) -> None:
        self.__context: Optional[EventRegistryContext] = None
        self.__next_id = 0
        self.__active_windows_by_id: Dict[str, NativeWindow] = {}
        self.__active_windows_by_native_id: Dict[Hashable, NativeWindow] = {}
        self.__focused: Dict[int, str] = {}
        self.__global_settings = dict(initial_global_settings)
        self.__global_meta_desc = dict(global_meta_desc)
        self.__window_meta_desc = dict(window_meta_desc)

    def register_listeners(self, context: EventRegistryContext) -> StdRet[None]:
        """Register this handler to listen for events with the context.  The global settings
        will need to be updated outside of this call."""
        return join_none_results(
            context.register_event_parser(
                window_events.SetWindowPositionsEvent.FULL_EVENT_NAME,
                window_events.SetWindowSettingsEvent.parse_data,
            ),
            context.register_target(
                window_events.SetWindowPositionsEvent.FULL_EVENT_NAME,
                window_events.SetWindowPositionsEvent.UNIQUE_TARGET_FQN,
                SetWindowPositionsTarget(self),
            ),

            context.register_event_parser(
                window_events.CloseWindowRequestEvent.FULL_EVENT_NAME,
                window_events.CloseWindowRequestEvent.parse_data,
            ),
            context.register_target(
                window_events.CloseWindowRequestEvent.FULL_EVENT_NAME,
                None,
                CloseWindowRequestTarget(self),
            ),

            context.register_event_parser(
                window_events.MinimizeWindowRequestEvent.FULL_EVENT_NAME,
                window_events.MinimizeWindowRequestEvent.parse_data,
            ),
            context.register_target(
                window_events.MinimizeWindowRequestEvent.FULL_EVENT_NAME,
                None,
                MinimizeWindowRequestTarget(self),
            ),

            context.register_event_parser(
                window_events.MaximizeWindowRequestEvent.FULL_EVENT_NAME,
                window_events.MaximizeWindowRequestEvent.parse_data,
            ),
            context.register_target(
                window_events.MaximizeWindowRequestEvent.FULL_EVENT_NAME,
                None,
                MaximizeWindowRequestTarget(self),
            ),

            context.register_event_parser(
                window_events.RestoreWindowRequestEvent.FULL_EVENT_NAME,
                window_events.RestoreWindowRequestEvent.parse_data,
            ),
            context.register_target(
                window_events.RestoreWindowRequestEvent.FULL_EVENT_NAME,
                None,
                RestoreWindowRequestTarget(self),
            ),

            context.register_event_parser(
                window_events.SetWindowSettingsEvent.FULL_EVENT_NAME,
                window_events.SetWindowSettingsEvent.parse_data,
            ),
            context.register_target(
                window_events.SetWindowSettingsEvent.FULL_EVENT_NAME,
                None,
                SetWindowSettingsTarget(self),
            ),

            context.register_event_parser(
                window_events.SetGlobalSettingsEvent.FULL_EVENT_NAME,
                window_events.SetGlobalSettingsEvent.parse_data,
            ),
            context.register_target(
                window_events.SetGlobalSettingsEvent.FULL_EVENT_NAME,
                window_events.SetGlobalSettingsEvent.UNIQUE_TARGET_FQN,
                SetGlobalSettingsTarget(self),
            ),
        )

    def close(self) -> None:
        """Clean up this handler, to help prevent memory issues."""
        self.__context = None

    def is_closed(self) -> bool:
        """Has this been closed?"""
        return self.__context is None

    def get_window_by_id(self, window_id: str) -> Optional[NativeWindow]:
        """Get the window with the id"""
        return self.__active_windows_by_id.get(window_id)

    def get_window_by_native(self, native_id: T) -> Optional[NativeWindow]:
        """Get the window with the id"""
        return self.__active_windows_by_native_id.get(self.hash_native_id(native_id))

    def get_active_windows(self) -> Iterable[NativeWindow]:
        """Get all the active windows known by this object."""
        return tuple(self.__active_windows_by_id.values())

    def replace_native_id(self, old: NativeWindow, new: NativeWindow) -> None:
        """Replace the old representation of the window (as the OS sees it) with a
        new ID.  This performs no state change by itself."""
        if (
                old.hashable_native_id in self.__active_windows_by_native_id
                and new.native_id != old.native_id
                and old.window_id == new.window_id
        ):
            del self.__active_windows_by_native_id[old.hashable_native_id]
            self.__active_windows_by_native_id[new.hashable_native_id] = new

    def update_window_state(self, window: NativeWindow) -> StdRet[None]:
        """Update the window state."""
        if not self.__context:
            return RET_OK_NONE

        wid = window.window_id
        if wid not in self.__active_windows_by_id:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('no active window with id {wid}'),
                wid=wid,
            )

        self.__active_windows_by_id[wid] = window
        self.__active_windows_by_native_id[window.hashable_native_id] = window

        return store_window_details(self.__context, wid, window.state)

    def update_global_settings(self, settings: Mapping[str, str]) -> StdRet[None]:
        """Update the global settings in the datastore."""
        if self.__context:
            return store_global_settings(self.__context, settings, self.__global_settings)
        return RET_OK_NONE

    def create_next_window_id(self) -> str:
        """Create the next window_id; used for creating a new ActiveWindow instance."""
        index = self.__next_id
        self.__next_id += 1
        return f'{window_events.EXTENSION_NAME}:wid-{index}'

    def window_created(
            self, window: NativeWindow,
    ) -> StdRet[None]:
        """Record a window as being created."""
        if not self.__context:
            return RET_OK_NONE

        if window.window_id in self.__active_windows_by_id:
            return StdRet.pass_errmsg(
                user_messages.TRANSLATION_CATALOG,
                _('window id {wid} already registered'),
                wid=window.window_id,
            )

        self.__active_windows_by_id[window.window_id] = window
        self.__active_windows_by_native_id[window.hashable_native_id] = window
        return join_none_results(
            send_window_created_event(self.__context, window.window_id, window.state),
            store_active_windows_state(self.__context, self.__active_windows_by_id.keys()),
        )

    def window_destroyed(self, native_id: T, reason: str) -> StdRet[None]:
        """Record that a window was destroyed."""
        hashable_native_id = self.hash_native_id(native_id)
        wnd = self.__active_windows_by_native_id.get(hashable_native_id)
        if not self.__context or wnd is None:
            return RET_OK_NONE

        del self.__active_windows_by_native_id[hashable_native_id]
        del self.__active_windows_by_id[wnd.window_id]
        return join_none_results(
            store_active_windows_state(self.__context, self.__active_windows_by_id.keys()),
            send_window_destroyed_event(self.__context, wnd.window_id, reason),
        )

    def window_flashing(self, native_id: T) -> StdRet[None]:
        """Send the event notifying that the window is flashing."""
        hashable_native_id = self.hash_native_id(native_id)
        wnd = self.__active_windows_by_native_id.get(hashable_native_id)
        if not self.__context or wnd is None:
            return RET_OK_NONE

        return send_window_flashed_event(self.__context, wnd.window_id)

    def window_focused(self, focus_group: int, native_id: T) -> StdRet[None]:
        """Set the given window as focused for the given focus group.  This will make
        the previously focused window not-focused, and update their states.  If the
        window is already focused for the focus group, this is a no-op."""
        newly_focused_hash = self.hash_native_id(native_id)
        newly_focused = self.__active_windows_by_native_id.get(newly_focused_hash)
        old_focused_id = self.__focused.get(focus_group)
        if not newly_focused or old_focused_id == newly_focused.window_id or not self.__context:
            # no such window, the now-focused window is already focused, or closed.
            return RET_OK_NONE
        self.__focused[focus_group] = newly_focused.window_id
        return send_window_focused_event(
            context=self.__context,
            focus_group=focus_group,
            new_focused_window_id=newly_focused.window_id,
            new_focused_state=newly_focused.state,
            old_focused_window_id=old_focused_id,
            old_focused_state=self.__active_windows_by_id.get(old_focused_id),
        )

    def handle_set_window_positions_event(
            self, event: window_events.SetWindowPositionsEvent,
    ) -> StdRet[None]:
        """Handle a request to set the window positions."""
        if not self.__context:
            return RET_OK_NONE

        res: List[StdRet[None]] = []
        for position in event.window_id_positions:
            window = self.get_window_by_id(position.window_id)
            if window:
                if position.location:
                    res.append(self.on_set_window_position_request(window, position.location))
                else:
                    res.append(self.on_minimize_window_request(window))
            else:
                res.append(send_no_window_id_log_message(
                    self.__context, window_events.SetWindowPositionsEvent.UNIQUE_TARGET_FQN,
                    position.window_id, 'set-position',
                ))
        return join_none_results(*res)

    def handle_close_window_event(self, target_id: str) -> StdRet[None]:
        """Handle a request to close a window."""
        if not self.__context:
            return RET_OK_NONE

        window = self.get_window_by_id(target_id)
        if not window:
            return send_no_window_id_log_message(
                self.__context, window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                target_id, 'close-window',
            )
        return self.on_close_window_request(window)

    def handle_minimize_window_event(self, target_id: str) -> StdRet[None]:
        """Handle a minimize window event."""
        if not self.__context:
            return RET_OK_NONE

        window = self.get_window_by_id(target_id)
        if not window:
            return send_no_window_id_log_message(
                self.__context, window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                target_id, 'minimize-window',
            )
        return self.on_minimize_window_request(window)

    def handle_maximize_window_event(self, target_id: str) -> StdRet[None]:
        """Handle a maximize window event."""
        if not self.__context:
            return RET_OK_NONE

        window = self.get_window_by_id(target_id)
        if not window:
            return send_no_window_id_log_message(
                self.__context, window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                target_id, 'maximize-window',
            )
        return self.on_maximize_window_request(window)

    def handle_restore_window_event(self, target_id: str) -> StdRet[None]:
        """Handle a restore window event."""
        if not self.__context:
            return RET_OK_NONE

        window = self.get_window_by_id(target_id)
        if not window:
            return send_no_window_id_log_message(
                self.__context, window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                target_id, 'restore-window',
            )
        return self.on_restore_window_request(window)

    def handle_set_window_settings_event(
            self, target_id: str, event: window_events.SetWindowSettingsEvent,
    ) -> StdRet[None]:
        """Handle a set window settings event."""
        if not self.__context:
            return RET_OK_NONE

        window = self.get_window_by_id(target_id)
        if not window:
            return send_no_window_id_log_message(
                self.__context, window_events.WindowCreatedEvent.UNIQUE_TARGET_FQN,
                target_id, 'set-window-settings',
            )
        return self.on_set_window_settings(
            window,
            {
                s.key: s.value
                for s in event.settings
            },
        )

    def hash_native_id(self, native_id: T) -> Hashable:
        """Create a hashable version of the native ID.  It must have the same uniqueness
        properties as theo original."""
        raise NotImplementedError

    def on_set_window_position_request(
            self,
            window: NativeWindow,
            new_location: window_events.ScreenDimension,
    ) -> StdRet[None]:
        """Handler for natively setting a window's position."""
        raise NotImplementedError  # pragma no cover

    def on_close_window_request(self, window: NativeWindow) -> StdRet[None]:
        """Handler for natively closing a window.  When the window is closed, the usual
        `window_destroyed` method should be called, but that doesn't need to happen
        within this call."""
        raise NotImplementedError  # pragma no cover

    def on_minimize_window_request(self, window: NativeWindow) -> StdRet[None]:
        """Handler for natively minimizing a window."""
        raise NotImplementedError  # pragma no cover

    def on_maximize_window_request(self, window: NativeWindow) -> StdRet[None]:
        """Handler for natively maximizing a window."""
        raise NotImplementedError  # pragma no cover

    def on_restore_window_request(self, window: NativeWindow) -> StdRet[None]:
        """Handler for natively restoring a window."""
        raise NotImplementedError  # pragma no cover

    def on_set_window_settings(
            self, window: NativeWindow, settings: Mapping[str, str],
    ) -> StdRet[None]:
        """Handler for natively setting a window's metadata.  If the metadata does change, then
        the `update_window_state` method should be called, but it doesn't need to happen
        within this call."""
        raise NotImplementedError  # pragma no cover

    def on_set_global_settings(self, settings: Mapping[str, str]) -> StdRet[None]:
        """Handler for natively setting the global setting.  If the global data does change,
        then the `update_global_settings` method should be called."""
        raise NotImplementedError  # pragma no cover


class AbstractWindowTarget(EventObjectTarget[T]):
    """window_events.SetWindowPositionsEvent handler"""
    __slots__ = ('_handler',)

    def __init__(self, handler: AbstractWindowHandler) -> None:
        self._handler = handler

    def on_close(self) -> None:
        self._handler.close()

    def on_event(
            self, source: str, target: str, event: T,
    ) -> bool:
        if self._handler.is_closed():
            return True
        user_messages.report_send_receive_problems(self.handle_event(target, event))
        return False

    def handle_event(self, target: str, event: T) -> StdRet[None]:
        """Call into the handler with the event data."""
        raise NotImplementedError  # pragma no cover


class SetWindowPositionsTarget(AbstractWindowTarget[window_events.SetWindowPositionsEvent]):
    """window_events.SetWindowPositionsEvent handler"""

    def handle_event(
            self, target: str, event: window_events.SetWindowPositionsEvent,
    ) -> StdRet[None]:
        return self._handler.handle_set_window_positions_event(event)


class CloseWindowRequestTarget(AbstractWindowTarget[window_events.CloseWindowRequestEvent]):
    """window_events.CloseWindowRequestEvent handler"""

    def handle_event(
            self, target: str, event: window_events.CloseWindowRequestEvent,
    ) -> StdRet[None]:
        return self._handler.handle_close_window_event(target)


class MinimizeWindowRequestTarget(AbstractWindowTarget[window_events.MinimizeWindowRequestEvent]):
    """window_events.MinimizeWindowRequestEvent handler"""

    def handle_event(
            self, target: str, event: window_events.MinimizeWindowRequestEvent,
    ) -> StdRet[None]:
        return self._handler.handle_minimize_window_event(target)


class MaximizeWindowRequestTarget(AbstractWindowTarget[window_events.MaximizeWindowRequestEvent]):
    """window_events.MaximizeWindowRequestEvent handler"""

    def handle_event(
            self, target: str, event: window_events.MaximizeWindowRequestEvent,
    ) -> StdRet[None]:
        return self._handler.handle_maximize_window_event(target)


class RestoreWindowRequestTarget(AbstractWindowTarget[window_events.RestoreWindowRequestEvent]):
    """window_events.RestoreWindowRequestEvent handler"""

    def handle_event(
            self, target: str, event: window_events.RestoreWindowRequestEvent,
    ) -> StdRet[None]:
        return self._handler.handle_restore_window_event(target)


class SetWindowSettingsTarget(AbstractWindowTarget[window_events.SetWindowSettingsEvent]):
    """window_events.SetWindowSettingsEvent handler"""

    def handle_event(
            self, target: str, event: window_events.SetWindowSettingsEvent,
    ) -> StdRet[None]:
        return self._handler.handle_maximize_window_event(target)


class SetGlobalSettingsTarget(AbstractWindowTarget[window_events.SetGlobalSettingsEvent]):
    """window_events.SetGlobalSettingsEvent handler"""

    def handle_event(
            self, target: str, event: window_events.SetGlobalSettingsEvent,
    ) -> StdRet[None]:
        return self._handler.handle_maximize_window_event(target)
