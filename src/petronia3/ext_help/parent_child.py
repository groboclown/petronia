
"""
Helpers for parent-child relationships.

Requires the `core.registrar` extension.
"""

from typing import Dict, Callable, Optional, Sequence
from threading import Lock

from ..system.participant import ParticipantId
from ..system.events import (
    RequestDisposeEvent,
    DisposeCompleteEvent,
    ComponentCreatedEvent,
    as_request_dispose_listener,
    as_dispose_complete_listener,
    as_component_created_listener,
    send_dispose_complete_event,
    send_request_dispose_event,
    send_request_new_component,
)
from ..system.bus import (
    EventId,
    EventBus,
    ListenerId,
)
from ..util.memory import T


class Parent:
    """
    Manages a parent which has children.  It does not maintain any
    parent ID itself.

    Handles dispose event processing.  When this parent is disposed, its
    children are triggered to be disposed, too.  This means all registered
    children must be included in the dispose events in order for this to
    work right.
    """

    # child ID -> dispose completed listener ID
    _children: Dict[ParticipantId, ListenerId]
    _dispose_listener: Optional[ListenerId]
    _child_created_listener: Optional[ListenerId]

    __slots__ = (
        '_children', '_bus', '_on_dispose', '_dispose_listener', '_id',
        '_disposed', '__lock', '_on_child_disposed',
        '_child_created_listener',
    )

    def __init__(
            self, my_id: ParticipantId, bus: EventBus,
            on_dispose: Optional[Callable[[], None]] = None,
            on_child_disposed: Optional[Callable[[ParticipantId], None]] = None
    ) -> None:
        self._bus = bus
        self._id = my_id
        self._children = {}
        self._on_dispose = on_dispose
        self._on_child_disposed = on_child_disposed
        self._dispose_listener = bus.add_listener(
            my_id, as_request_dispose_listener, self.__on_request_dispose_self
        )
        self._child_created_listener = bus.add_listener(
            my_id, as_component_created_listener, self.__on_child_created
        )
        self.__lock = Lock()
        self._disposed = 0

    @property
    def is_disposed(self) -> bool:
        """Has the dispose event lifecycle completed?"""
        return self._disposed > 1

    @property
    def children_ids(self) -> Sequence[ParticipantId]:
        """All the child IDs registered and not disposed."""
        return tuple(self._children.keys())

    def create_child(self, category: ParticipantId, construct_obj: T) -> None:
        """
        Begins the request chain to create a child in the given category.

        Currently, there is no tracking between this request and the generated child.
        """
        send_request_new_component(
            self._bus, category, construct_obj, self._id, 0
        )

    def __on_child_created(
            self,
            eid: EventId, tid: ParticipantId, event: ComponentCreatedEvent # pylint: disable=unused-argument
    ) -> None:
        child_id = event.created_id
        with self.__lock:
            if child_id not in self._children:
                self._children[child_id] = self._bus.add_listener(
                    child_id, as_dispose_complete_listener,
                    self.__on_child_dispose_complete
                )

    def __on_child_dispose_complete(
            self,
            eid: EventId, tid: ParticipantId, event: DisposeCompleteEvent # pylint: disable=unused-argument
    ) -> None:
        with self.__lock:
            if tid in self._children:
                self._bus.remove_listener(self._children[tid])
                del self._children[tid]
                try:
                    if self._on_child_disposed:
                        self._on_child_disposed(tid)
                finally:
                    if self._disposed == 1 and not self._children:
                        # In the process of disposing (== 1) and no remaining children to dispose,
                        # so clean ourself up.
                        self.__final_dispose()

    def __on_request_dispose_self(
            self,
            eid: EventId, tid: ParticipantId, event: RequestDisposeEvent # pylint: disable=unused-argument
    ) -> None:
        with self.__lock:
            if self._disposed > 1:
                return
            self._disposed = 1
            if self._children:
                for child_id in self._children:
                    send_request_dispose_event(self._bus, child_id)
            else:
                self.__final_dispose()

    def __final_dispose(self) -> None:
        # Must be run with a lock allocated outside this method.
        if self._disposed < 2:
            try:
                if self._on_dispose:
                    self._on_dispose()
                if self._dispose_listener:
                    self._bus.remove_listener(self._dispose_listener)
                    self._dispose_listener = None
                if self._child_created_listener:
                    self._bus.remove_listener(self._child_created_listener)
                    self._child_created_listener = None
            finally:
                self._disposed = 2
                send_dispose_complete_event(self._bus, self._id)
