
"""
Event bus proxy support.

This handles proper lifecycle support with the event bus.
"""

from typing import List, Tuple, Callable
from threading import Lock
from ...base import (
    EventBus, ListenerId, EventCallback, ParticipantId,
)
from ...base.bus import ListenerRegistrar
from ...base.util import T
from ...core.hotkeys.api import (
    BoundServiceActionSchema,
    send_hotkey_bound_service_announcement,
    send_hotkey_unbind_service_announcement,
)


class ListenerSet:
    """
    Lifecycle support for managing listeners.

    One of these should be created for each component.

    This is thread-safe.
    """

    __slots__ = ('__bus', '_children', '__lock', '__disposed', '_listener_ids', '_bound_hotkeys', '_disposers')

    _listener_ids: List[ListenerId]
    _bound_hotkeys: List[Tuple[ParticipantId, str]]
    _children: List['ListenerSet']
    _disposers: List[Callable[[], None]]

    def __init__(self, bus: EventBus) -> None:
        self.__bus = bus
        self._listener_ids = []
        self._bound_hotkeys = []
        self._children = []
        self._disposers = []
        self.__lock = Lock()
        self.__disposed = False

    @property
    def disposed(self) -> bool:
        return self.__disposed

    def add_dispose_callback(self, callback: Callable[[], None]) -> None:
        if not self.__disposed:
            with self.__lock:
                self._disposers.append(callback)
        else:
            callback()

    def listen(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrar[T],
            callback: EventCallback[T]
    ) -> ListenerId:
        """
        Register a new listener.
        """
        assert not self.__disposed
        with self.__lock:
            listener_id = self.__bus.add_listener(target_id, listener_setup, callback)
            self._listener_ids.append(listener_id)
            return listener_id

    def remove_listener(self, listener_id: ListenerId) -> None:
        """
        Stop listening to the given ID.
        """
        with self.__lock:
            try:
                self._listener_ids.remove(listener_id)
                self.__bus.remove_listener(listener_id)
            except ValueError:
                # The listener_id is not known by our listen list.
                pass

    def bind_hotkey(self, binding: BoundServiceActionSchema) -> None:
        """
        Bind a hotkey schema to this target.
        """
        if not self.__disposed:
            send_hotkey_bound_service_announcement(self.__bus, binding)
            with self.__lock:
                self._bound_hotkeys.append((binding.service, binding.action,))

    def child(self) -> 'ListenerSet':
        """
        Create a child listener set, which can have its own listeners.  The child
        will register any listener to it with the current listener set.  That way,
        child listeners will automatically be disposed when the parent is
        disposed, but the children can be independently disposed without disturbing
        the parent.
        """
        if self.__disposed:
            raise ValueError('already disposed')
        child = ListenerSet(self.__bus)
        with self.__lock:
            self._children.append(child)
        return child

    def dispose(self) -> None:
        """
        De-register all the active listeners.
        """
        if self.__disposed:
            return
        with self.__lock:
            self.__disposed = True
            for service, action in self._bound_hotkeys:
                send_hotkey_unbind_service_announcement(self.__bus, service, action)
            for listener_id in self._listener_ids:
                self.__bus.remove_listener(listener_id)
            self._listener_ids.clear()
            self._bound_hotkeys.clear()
            for child in self._children:
                child.dispose()
            self._children.clear()
            for callback in self._disposers:
                callback()
            self._disposers.clear()
