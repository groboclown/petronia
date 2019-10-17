
# mypy: allow-any-expr
# mypy: allow-any-explicit
# mypy: allow-any-generics

"""
Dispose listener helpers.
"""

from typing import Callable, List, Any
from threading import Lock
from ..std import (
    EventBus,
    ParticipantId,
    ListenerId,
    EventId,
    send_dispose_complete_event,
)
from ..bootstrap import (
    as_request_dispose_listener,
    as_system_shutdown_finalize_listener,
    as_system_shutdown_listener,
    TARGET_ID_SYSTEM_SHUTDOWN,

    ListenerRegistrar,
)


def setup_dispose_handler(
        bus: EventBus,
        component_id: ParticipantId,
        dispose_handler: Callable[[], None],
        is_application: bool = False
) -> None:
    """
    Sets up the dispose listeners so that it correctly handles the dispose
    phase of the component lifecycle.  If `is_application` is True, then the
    dipose handler will be called during the initial shutdown phase, otherwise
    it will be called during the finalize phase.

    The handler argument will need to handle all behavior central to the
    component.  It does not need custom logic for de-registering the dispose
    handlers, and does not need to be concerned about sending the dispose
    complete event.
    """

    handler = _DisposedListenerHandler(bus, component_id, dispose_handler)
    handler.add_listener(component_id, as_request_dispose_listener)
    if is_application:
        handler.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_listener)
    else:
        handler.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_finalize_listener)


class _DisposedListenerHandler:
    __slots__ = ('__lock', '__bus', '_listeners', '_dispose_handler', '__component_id')
    _listeners: List[ListenerId]

    def __init__(
            self,
            bus: EventBus,
            component_id: ParticipantId,
            dispose_handler: Callable[[], None]
    ) -> None:
        self.__bus = bus
        self.__component_id = component_id
        self.__lock = Lock()
        self._dispose_handler = dispose_handler
        self._listeners = []

    def add_listener(
            self,
            target_id: ParticipantId,
            listener_setup: ListenerRegistrar[Any]
    ) -> None:
        self._listeners.append(self.__bus.add_listener(
            target_id, listener_setup, self.event_handler_func
        ))

    def event_handler_func(
            self,
            _event_id: EventId, _target_id: ParticipantId,
            _event_obj: Any
    ) -> None:
        with self.__lock:
            if self._listeners:
                self._dispose_handler()
                for listener in self._listeners:
                    self.__bus.remove_listener(listener)
                self._listeners.clear()
                send_dispose_complete_event(self.__bus, self.__component_id)
