
# mypy: allow-any-explicit
# mypy: allow-any-expr

"""
Bootstrap the singleton and adding in the event listeners.
"""

from typing import Any
from .registrar import Registrar
from .events import (
    TARGET_REGISTRAR,

    EVENT_ID_COMPONENT_CREATED,
    ComponentCreatedEvent,

    EVENT_ID_REGISTER_CATEGORY,
    RegisterCategoryEvent,

    EVENT_ID_REQUEST_NEW_CATEGORY_INSTANCE,
    RequestNewCategoryInstanceEvent,
)
from ..bus import (
    TypeSafeEventBus, register_event,
    ListenerSetup, TypeSafeEventCallback,
    EventId,
    QUEUE_EVENT_NORMAL,
    QUEUE_EVENT_NOW,
)
from ..participant import (
    create_component_identity,
    ParticipantId,
)
from ...util.memory import T

def bootstrap_registrar(bus: TypeSafeEventBus) -> None:
    register_event(
        bus,
        EVENT_ID_COMPONENT_CREATED,
        QUEUE_EVENT_NORMAL,
        ComponentCreatedEvent,
        ComponentCreatedEvent(create_component_identity('x'), 1)
    )
    register_event(
        bus,
        EVENT_ID_REGISTER_CATEGORY,
        # Registering a component should be added right away, so that
        # the component can be immediately created.
        QUEUE_EVENT_NOW,
        RegisterCategoryEvent,
        RegisterCategoryEvent('x', object, lambda x: create_component_identity('x'))
    )
    register_event(
        bus,
        EVENT_ID_REQUEST_NEW_CATEGORY_INSTANCE,
        QUEUE_EVENT_NORMAL,
        RequestNewCategoryInstanceEvent,
        RequestNewCategoryInstanceEvent('x', object(), TARGET_REGISTRAR, 1)
    )
    registrar = RegistrarWithListener(bus)

    # Listener IDs are not saved, because the registrar is a singleton and is
    # necessary to remain within the event bus.
    bus.add_listener(
        TARGET_REGISTRAR,
        _as_register_category_listener,
        registrar.on_register_category
    )
    bus.add_listener(
        TARGET_REGISTRAR,
        _as_request_new_category_listener,
        registrar.on_create_new_instance
    )


def _as_register_category_listener(
        callback: TypeSafeEventCallback[RegisterCategoryEvent[T]]
) -> ListenerSetup[RegisterCategoryEvent[T]]:
    return (EVENT_ID_REGISTER_CATEGORY, callback,)


def _as_request_new_category_listener(
        callback: TypeSafeEventCallback[RequestNewCategoryInstanceEvent[T]]
) -> ListenerSetup[RequestNewCategoryInstanceEvent[T]]:
    return (EVENT_ID_REQUEST_NEW_CATEGORY_INSTANCE, callback,)


class RegistrarWithListener(Registrar):
    __slots__ = ('__bus',)
    def __init__(self, bus: TypeSafeEventBus):
        Registrar.__init__(self)
        self.__bus = bus

    def on_register_category(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: RegisterCategoryEvent[T]
    ) -> None:
        self.register_category(
            event.category,
            event.construction_type,
            event.factory
        )

    def on_create_new_instance(
            self,
            eid: EventId, tid: ParticipantId, # pylint: disable=unused-argument
            event: RequestNewCategoryInstanceEvent[T]
    ) -> None:
        component_id = self.create_new_category_instance(
            event.category, event.construction_obj
        )
        if component_id:
            self.__bus.trigger(
                EVENT_ID_COMPONENT_CREATED,
                event.target_id,
                ComponentCreatedEvent(component_id, event.request_id)
            )
