
"""
Tests for the event chain helper.
"""

import unittest
from ..test_helper import (
    BasicQueuer,
    load_core_extensions,
    bootstrap_event_bus
)
from ...base import create_singleton_identity
from ...base.events import (
    as_component_created_listener
)
from ..event_chain import EventChainManager, EventHas


class EventChainTest(unittest.TestCase):
    def test_nothing(self) -> None:
        queue = BasicQueuer(self)
        bus = bootstrap_event_bus(queue.pure_queuer)
        load_core_extensions(bus)
        pid = create_singleton_identity('test')
        mgr = EventChainManager(bus, pid)
        mgr.create(
            ).with_total_timeout(
                10
            ).when(
                EventHas(as_component_created_listener)
            ).create_unique_int_as(
                'int1'
            ).create_component_id(
                'id1', 'component_x'
            ).then_handle_with(
            ).run(
                lambda x, y: None
            )

        mgr.setup()

        # TODO check the event handling logic...
