
"""Test all the event_router modules."""

import asyncio
import unittest
from ..router import EventRouter
from petronia_common.event_stream import (
    RawEvent,
    write_binary_event_to_stream,
)
from petronia_common.event_stream.tests.forwarder_test import (
    MockTarget, create_read_stream, SimpleBinaryWriter,
)
from petronia_common.util import StdRet


class RouterIntegrationTest(unittest.TestCase):
    """Tests how this will all work together.  Let's see how feasible it is to write."""
    def test_intra_channel(self) -> None:
        """Channel 1 creates an event, which is forwarded on to channel 2."""
        monitor = MockTarget(self)

        async def run_test() -> None:
            router = EventRouter(asyncio.Semaphore(), monitor)

            event_data = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                event_data, 'e1', 's1', 't1', 2, b'12',
            )

            channel1_writer = SimpleBinaryWriter()
            channel1_reader = create_read_stream(event_data.getvalue())
            channel2_writer = SimpleBinaryWriter()
            channel2_reader = create_read_stream(b'')

            # Channel 1 has handler h1 which can produce event e1
            ret_channel1 = await router.add_channel('ch1', channel1_reader, channel1_writer)
            self.assertIsNone(ret_channel1.error)
            res = await router.add_handler('ch1', 'h1', ['e1'], [])
            self.assertIsNone(res.error)

            # Channel 2 has handler h2 which can consume event e1 sent to t1.
            ret_channel2 = await router.add_channel('ch2', channel2_reader, channel2_writer)
            self.assertIsNone(ret_channel2.error)
            res = await router.add_handler('ch2', 'h2', [], [('e1', 't1')])
            self.assertIsNone(res.error)

            # Start the processing.  These should both run until an EOF in the reader.
            await ret_channel1.result
            await ret_channel2.result

            # The data read from channel 1's reader should have been sent on to channel 2's writer.
            self.assertEqual(event_data.getvalue(), channel2_writer.getvalue())

        asyncio.run(run_test())


class CallbackMonitor:
    def output_callback(self, event: RawEvent) -> StdRet[None]:
        pass

    def pass_through_cb(self, event: RawEvent) -> bool:
        pass

    def invalid_source_cb(self, event: RawEvent) -> bool:
        pass

