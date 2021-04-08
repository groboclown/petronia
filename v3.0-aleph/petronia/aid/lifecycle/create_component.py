
"""
Helpers for the create component lifecycle.

These require extensions:
    core.shutdown.api
    core.timer.api
"""


from typing import Callable, List, Dict, Tuple, Generic, Optional
from threading import Lock
from ...base.bus import (
    EventBus,
    EventId,
    ListenerId,
)
from ...base.participant import (
    ParticipantId,
    ComponentId,
    ComponentIdType,
)
from ...base.events import (
    send_request_new_component,
    send_dispose_complete_event,
    as_dispose_complete_listener,
    DisposeCompleteEvent,
    as_component_created_listener,
    as_request_dispose_listener,
    ComponentCreatedEvent,
    as_component_creation_failed_listener,
    ComponentCreationFailedEvent,
)
from ...base.util import T, UserMessage, ValueHolder
from ...base.util import i18n as _
from ...core.shutdown.api import (
    TARGET_ID_SYSTEM_SHUTDOWN,
    as_system_shutdown_listener,
)
from ...core.timer.api import (
    TARGET_TIMER,
    as_timer_listener,
    TimerEvent,
)
from .listener_set import ListenerSet


CREATE_COMPONENT_CATEGORY = 'petronia.aid.lifecycle.create-component'


OnCreatedListener = Callable[[ComponentId], None]
OnCreateFailedListener = Callable[[UserMessage], None]

_TIMEOUT_FAILURE_MESSAGE = UserMessage(_('timed out waiting for creation'))


def create_component_lifecycle_handlers(
        bus: EventBus,
        listeners: ListenerSet,
        category_target_cid: ParticipantId,
        component_data: T,
        create_complete: Optional[Callable[[ComponentId], None]] = None,
        disposed: Optional[Callable[[ComponentId], None]] = None,
        create_failed: Optional[OnCreateFailedListener] = None,
        create_timeout: int = 10
) -> None:
    def on_disposed(_eid: EventId, tid: ParticipantId, _event: DisposeCompleteEvent) -> None:
        if disposed and isinstance(tid, ComponentIdType):
            disposed(tid)
        # Should remove this listener...

    def on_created(cid: ComponentId) -> None:
        if create_complete:
            create_complete(cid)
        if disposed:
            listeners.listen(cid, as_dispose_complete_listener, on_disposed)
        # Should remove this listener...

    create_component(
        bus, category_target_cid, component_data,
        on_created,
        create_failed or (lambda a: None),
        create_timeout
    )


def create_component(
        bus: EventBus,
        category_target_cid: ParticipantId,
        component_data: T,
        on_created: OnCreatedListener,
        on_create_failed: OnCreateFailedListener,
        timeout: int = 10
) -> None:
    cid = bus.create_component_id(CREATE_COMPONENT_CATEGORY)
    listeners: List[ListenerId] = []
    remaining_time = [timeout]

    def dispose(_event_id: EventId, _target_id: ParticipantId, _event: object) -> None:
        remaining_time[0] = -1
        t_l = listeners
        listeners.clear()
        for listener in t_l:
            bus.remove_listener(listener)

    def created(event_id: EventId, target_id: ParticipantId, event: ComponentCreatedEvent) -> None:
        if event.request_id == 0 and remaining_time[0] > 0:
            dispose(event_id, target_id, event)
            on_created(event.created_id)

    def failed(event_id: EventId, target_id: ParticipantId, event: ComponentCreationFailedEvent) -> None:
        if event.request_id == 0 and remaining_time[0] > 0:
            dispose(event_id, target_id, event)
            on_create_failed(event.error_message)

    def tick(event_id: EventId, target_id: ParticipantId, event: TimerEvent) -> None:
        if remaining_time[0] > 0:
            remaining_time[0] -= 1
            if remaining_time[0] <= 0:
                dispose(event_id, target_id, event)
                on_create_failed(_TIMEOUT_FAILURE_MESSAGE)

    listeners.append(bus.add_listener(cid, as_request_dispose_listener, dispose))
    listeners.append(bus.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_listener, dispose))
    listeners.append(bus.add_listener(cid, as_component_created_listener, created))
    listeners.append(bus.add_listener(cid, as_component_creation_failed_listener, failed))
    if timeout <= 0:
        listeners.append(bus.add_listener(TARGET_TIMER, as_timer_listener, tick))
    else:
        remaining_time[0] = 1

    send_request_new_component(bus, category_target_cid, component_data, cid, 0)


class ComponentCreator(Generic[T]):
    __slots__ = (
        '__bus', '__target_cid',
        '__listeners', '__cid', '__disposed',
        '__index', '__timeout', '_waiting',
        '__lock',
    )
    _waiting: Dict[int, Tuple[int, OnCreatedListener, OnCreateFailedListener]]

    def __init__(
            self,
            bus: EventBus,
            category_target_cid: ParticipantId,
            timeout_ticks: int = 10
    ) -> None:
        self.__disposed = False
        self.__cid = bus.create_component_id(CREATE_COMPONENT_CATEGORY)
        self.__bus = bus
        self.__target_cid = category_target_cid
        self.__timeout = timeout_ticks
        self.__index = 0
        self.__lock = Lock()
        self._waiting = {}
        self.__listeners = [
            bus.add_listener(TARGET_ID_SYSTEM_SHUTDOWN, as_system_shutdown_listener, lambda a, b, c: self.dispose()),
            bus.add_listener(self.__cid, as_request_dispose_listener, lambda a, b, c: self.dispose()),
            bus.add_listener(TARGET_TIMER, as_timer_listener, self._on_tick),
            bus.add_listener(self.__cid, as_component_created_listener, self._on_created),
            bus.add_listener(self.__cid, as_component_creation_failed_listener, self._on_failed),
        ]

    def create(self, data: T, on_create: OnCreatedListener, on_fail: OnCreateFailedListener) -> None:
        with self.__lock:
            index = self.__index
            self.__index += 1
            self._waiting[index] = (self.__timeout, on_create, on_fail,)
            send_request_new_component(self.__bus, self.__target_cid, data, self.__cid, index)

    def dispose(self) -> None:
        with self.__lock:
            if not self.__disposed:
                self.__disposed = True
                for listener in self.__listeners:
                    self.__bus.remove_listener(listener)
                self.__listeners.clear()
                send_dispose_complete_event(self.__bus, self.__cid)

    def _on_created(self, _eid: EventId, _tid: ParticipantId, event: ComponentCreatedEvent) -> None:
        callback: Optional[OnCreatedListener] = None
        with self.__lock:
            if self.__disposed:
                return
            if event.request_id in self._waiting:
                callback = self._waiting[event.request_id][1]
                del self._waiting[event.request_id]
        if callback:
            callback(event.created_id)

    def _on_failed(self, _eid: EventId, _tid: ParticipantId, event: ComponentCreationFailedEvent) -> None:
        callback: Optional[OnCreateFailedListener] = None
        with self.__lock:
            if self.__disposed:
                return
            if event.request_id in self._waiting:
                callback = self._waiting[event.request_id][2]
                del self._waiting[event.request_id]
        if callback:
            callback(event.error_message)

    def _on_tick(self, _eid: EventId, _tid: ParticipantId, _obj: TimerEvent) -> None:
        """
        On a timer tick, count down each waiting item until its end-of-life is reached, at which point
        this will fail the waiting callbacks.

        :param _eid:
        :param _tid:
        :param _obj:
        :return:
        """
        to_fail: List[OnCreateFailedListener] = []
        with self.__lock:
            if self.__disposed:
                return
            to_delete: List[int]
            for key, value in self._waiting.items():
                remaining = value[0] - 1
                if remaining <= 0:
                    to_delete.append(key)
                    to_fail.append(value[2])
                else:
                    # Tuples are read-only, so updating the tick requires creating a new tuple.
                    self._waiting[key] = (remaining, value[1], value[2])
            for key in to_delete:
                del self._waiting[key]
        for callback in to_fail:
            callback(_TIMEOUT_FAILURE_MESSAGE)
