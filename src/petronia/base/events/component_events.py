
"""
The events around component lifecycle creation.
"""

from typing import Generic, Dict, Mapping, Union
from ..internal_.identity_types import (
    ParticipantId, ComponentId,
)
from ..internal_.bus_types import (
    EventBus, EventId, EventCallback,
    ListenerSetup,
)
from ..util.memory import T, readonly_dict

# ---------------------------------------------------------------------------

# Note: not "core".
EVENT_ID_REQUEST_NEW_COMPONENT = EventId('petronia.registrar request-new-component')


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


# ---------------------------------------------------------------------------

EVENT_ID_COMPONENT_CREATED = EventId('petronia.registrar component-created')


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


# ---------------------------------------------------------------------------

EVENT_ID_COMPONENT_CREATION_FAILED = EventId('petronia.registrar component-create-failed')


class ComponentCreationFailedEvent:
    """
    Reports that a component creation attempt failed.
    """
    __slots__ = ('__request_id', '__category', '__error_msg', '__error_values')

    def __init__(
            self, category: str, request_id: int,
            error_msg: str,
            error_values: Dict[str, Union[str, int, float]]
    ):
        self.__request_id = request_id
        self.__category = category
        self.__error_msg = error_msg
        self.__error_values = readonly_dict(error_values)

    @property
    def request_id(self) -> int:
        """Request ID that initiated the creation.  Specific to the creator."""
        return self.__request_id

    @property
    def category(self) -> str:
        """The requested category to create."""
        return self.__category

    @property
    def error_message(self) -> str:
        """The description of the error."""
        return self.__error_msg

    @property
    def error_values(self) -> Mapping[str, Union[str, int, float]]:
        """Extra descriptive values for the error."""
        return self.__error_values


def as_component_creation_failed_listener(
        callback: EventCallback[ComponentCreationFailedEvent]
) -> ListenerSetup[ComponentCreationFailedEvent]:
    """Listener setup for ComponentCreationFailedEvent"""
    return (EVENT_ID_COMPONENT_CREATION_FAILED, callback,)


def send_component_creation_failed_event(
        bus: EventBus,
        target_id: ParticipantId,
        category: str,
        request_id: int,
        error_message: str,
        error_values: Dict[str, Union[str, int, float]]
) -> None:
    bus.trigger(
        EVENT_ID_COMPONENT_CREATION_FAILED,
        target_id,
        ComponentCreationFailedEvent(
            category, request_id,
            error_message, error_values
        )
    )
