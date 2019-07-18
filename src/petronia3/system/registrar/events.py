
"""
Helpers for disposing components.
"""

from typing import Generic, Type
from .registrar_types import CategoryFactory
from ..bus import (
    TypeSafeEventCallback, TypeSafeEventBus,
    EventId, ListenerSetup,
)
from ..participant import (
    ParticipantId,
    ComponentId,
    create_singleton_identity,
)
from ...util.memory import T

TARGET_REGISTRAR = create_singleton_identity('registrar')
EVENT_ID_REGISTER_CATEGORY = EventId('registrar register-category')
EVENT_ID_REQUEST_NEW_CATEGORY_INSTANCE = EventId('registrar request-new-category-instance')
EVENT_ID_COMPONENT_CREATED = EventId('registrar component-created')


class RegisterCategoryEvent(Generic[T]):
    """
    Registers the category with a factory.
    """
    __slots__ = ('_category', '_factory', '_cttype')

    def __init__(
            self, category: str, construction_type: Type[T], factory: CategoryFactory[T]
    ) -> None:
        self._category = category
        self._cttype = construction_type
        self._factory = factory

    @property
    def category(self) -> str:
        return self._category

    @property
    def construction_type(self) -> Type[T]:
        return self._cttype

    @property
    def factory(self) -> CategoryFactory[T]:
        return self._factory


def send_register_category(
        bus: TypeSafeEventBus,
        category: str, construction_type: Type[T], factory: CategoryFactory[T]
) -> None:
    """
    Register a new category.
    """
    bus.trigger(
        EVENT_ID_REGISTER_CATEGORY,
        TARGET_REGISTRAR,
        RegisterCategoryEvent(
            category, construction_type, factory
        )
    )


class RequestNewCategoryInstanceEvent(Generic[T]):
    """
    Asks the registrar to create a new category instance.
    """
    __slots__ = ('_category', '_obj', '_target_id', '_request_id',)

    def __init__(
            self, category: str, construction_obj: T,
            target_id: ParticipantId, request_id: int
    ) -> None:
        self._category = category
        self._obj = construction_obj
        self._target_id = target_id
        self._request_id = request_id

    @property
    def category(self) -> str:
        """The category to create an instance from."""
        return self._category

    @property
    def construction_obj(self) -> T:
        """Object for the category's factory to create the component."""
        return self._obj

    @property
    def target_id(self) -> ParticipantId:
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


def send_request_new_category_instance(
        bus: TypeSafeEventBus, category: str, construction_obj: T,
        target_id: ParticipantId, request_id: int
) -> None:
    """
    Request for a new instance of a category.
    """
    bus.trigger(
        EVENT_ID_REQUEST_NEW_CATEGORY_INSTANCE,
        TARGET_REGISTRAR,
        RequestNewCategoryInstanceEvent(
            category, construction_obj, target_id, request_id
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
        callback: TypeSafeEventCallback[ComponentCreatedEvent]
) -> ListenerSetup[ComponentCreatedEvent]:
    return (EVENT_ID_COMPONENT_CREATED, callback,)
