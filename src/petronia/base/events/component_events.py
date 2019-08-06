
"""
The events around component lifecycle creation.
"""

from typing import Generic
from ..internal_.identity_types import (
    ParticipantId, ComponentId,
)
from ..internal_.bus_types import (
    EventBus, EventId, EventCallback,
    ListenerSetup,
)
from ..util.memory import T


# Note: not "core".
EVENT_ID_REQUEST_NEW_COMPONENT = EventId('petronia.registrar request-new-component')
EVENT_ID_COMPONENT_CREATED = EventId('petronia.registrar component-created')


class RequestNewComponentEvent(Generic[T]):
    """
    Asks the component factory to create a new instance.  The target of the
    event is the component factory, which will be called with the request_id
    to allow the called-back target to know which component was created.
    """
    __slots__ = ('_obj', '_target_id', '_request_id',)

    def __init__(
            self, construction_obj: T,
            callback_target_id: ParticipantId, request_id: int
    ) -> None:
        self._obj = construction_obj
        self._target_id = callback_target_id
        self._request_id = request_id

    @property
    def construction_obj(self) -> T:
        """Object for the category's factory to create the component."""
        return self._obj

    @property
    def callback_target_id(self) -> ParticipantId:
        """
        The target that will be notified of the created component.
        """
        return self._target_id

    @property
    def request_id(self) -> int:
        """
        An identifier that tells the target which category creation
        this corresponds to.
        """
        return self._request_id


def as_request_new_component_listener(
        callback: EventCallback[RequestNewComponentEvent[T]]
) -> ListenerSetup[RequestNewComponentEvent[T]]:
    """Listener setup for RequestNewComponentEvent"""
    return (EVENT_ID_REQUEST_NEW_COMPONENT, callback,)


def send_request_new_component(
        bus: EventBus, category_target_id: ParticipantId, construction_obj: T,
        callback_target_id: ParticipantId, request_id: int
) -> None:
    """
    Request for a new instance of a category.
    """
    bus.trigger(
        EVENT_ID_REQUEST_NEW_COMPONENT,
        category_target_id,
        RequestNewComponentEvent(
            construction_obj, callback_target_id, request_id
        )
    )


class ComponentCreatedEvent:
    """
    Reports that a component was created.
    """
    __slots__ = ('__request_id', '__created_id')

    def __init__(self, created_id: ComponentId, request_id: int):
        self.__created_id = created_id
        self.__request_id = request_id

    @property
    def created_id(self) -> ComponentId:
        """ID of the component created by the request."""
        return self.__created_id

    @property
    def request_id(self) -> int:
        """Request ID that initiated the creation.  Specific to the creator."""
        return self.__request_id


def as_component_created_listener(
        callback: EventCallback[ComponentCreatedEvent]
) -> ListenerSetup[ComponentCreatedEvent]:
    """Listener setup for ComponentCreatedEvent"""
    return (EVENT_ID_COMPONENT_CREATED, callback,)

def send_component_created_event(
        bus: EventBus,
        target_id: ParticipantId,
        created_id: ComponentId,
        request_id: int
) -> None:
    bus.trigger(
        EVENT_ID_COMPONENT_CREATED,
        target_id,
        ComponentCreatedEvent(created_id, request_id)
    )
