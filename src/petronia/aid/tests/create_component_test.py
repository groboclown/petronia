
from typing import List
import unittest
from ..std import (
    ComponentId,
    UserMessage,
    i18n,
    EventId,
    ParticipantId,
    create_singleton_identity,
)
from ..lifecycle.create_component import (
    create_component,
    create_component_lifecycle_handlers,
    ComponentCreator,
)
from ..test_helper import (
    BasicQueuer,
    load_core_extensions,
    bootstrap_event_bus
)
from ...base.events import (
    RequestNewComponentEvent,
    as_request_new_component_listener,
    send_component_created_event,
    send_component_creation_failed_event,
)
from ...core.timer.api.events import (
    send_timer_event
)


class CreateComponentTest(unittest.TestCase):
    def test_std_create(self) -> None:
        queue = BasicQueuer(self)
        bus = bootstrap_event_bus(queue.pure_queuer)
        load_core_extensions(bus)
        event_order: List[str] = []
        category = 't'
        category_listen = create_singleton_identity(category)
        create_cid = bus.create_component_id(category)

        def on_create_pass(cid: ComponentId) -> None:
            event_order.append('create')
            self.assertEqual(cid, create_cid)

        def on_create_fail(msg: UserMessage) -> None:
            self.fail(msg.debug())

        def on_create_request(_eid: EventId, _tid: ParticipantId, obj: RequestNewComponentEvent[str]) -> None:
            self.assertEqual(obj.construction_obj, 'x')
            event_order.append('respond')
            send_component_created_event(bus, obj, create_cid)

        bus.add_listener(category_listen, as_request_new_component_listener, on_create_request)  # type: ignore
        create_component(
            bus,
            category_listen, 'x',
            on_create_pass, on_create_fail
        )

        self.assertEqual(
            event_order,
            ['respond', 'create']
        )

    def test_failure(self) -> None:
        queue = BasicQueuer(self)
        bus = bootstrap_event_bus(queue.pure_queuer)
        load_core_extensions(bus)
        event_order: List[str] = []
        category = 't'
        category_listen = create_singleton_identity(category)

        def on_create_pass(_cid: ComponentId) -> None:
            self.fail("should not create")

        def on_create_fail(msg: UserMessage) -> None:
            event_order.append('error')

        def on_create_request(_eid: EventId, _tid: ParticipantId, obj: RequestNewComponentEvent[str]) -> None:
            self.assertEqual(obj.construction_obj, 'x')
            event_order.append('respond')
            send_component_creation_failed_event(bus, obj, category, UserMessage(i18n('fail')))

        bus.add_listener(category_listen, as_request_new_component_listener, on_create_request)  # type: ignore
        create_component(
            bus,
            category_listen, 'x',
            on_create_pass, on_create_fail
        )

        self.assertEqual(
            event_order,
            ['respond', 'error']
        )

    def test_timeout(self) -> None:
        queue = BasicQueuer(self)
        bus = bootstrap_event_bus(queue.pure_queuer)
        load_core_extensions(bus)
        event_order: List[str] = []
        category = 't'
        category_listen = create_singleton_identity(category)
        create_cid = bus.create_component_id(category)

        def on_create_pass(_cid: ComponentId) -> None:
            self.fail("should not create")

        def on_create_fail(msg: UserMessage) -> None:
            event_order.append('error')

        create_component(
            bus,
            category_listen, 'x',
            on_create_pass, on_create_fail,
            2
        )

        self.assertEqual(event_order, [])
        send_timer_event(bus)
        self.assertEqual(event_order, [])
        send_timer_event(bus)
        self.assertEqual(
            event_order,
            ['error']
        )
