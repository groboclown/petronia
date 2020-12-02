"""Test the router module."""

from typing import Tuple
import unittest
import asyncio
import re
from ..router import EventRouter, OnCloseTarget
from petronia_common.event_stream import (
    BinaryWriter,
    write_binary_event_to_stream,
)
from petronia_common.event_stream.tests.forwarder_test import (
    create_read_stream, SimpleBinaryWriter,
)
from petronia_common.util import StdRet


class RouterIntegrationTest(unittest.TestCase):
    """Tests how this will all work together.  Let's see how feasible it is to write."""
    def test_intra_channel(self) -> None:
        """Channel 1 creates an event, which is forwarded on to channel 2."""

        async def run_test() -> None:
            router = EventRouter(asyncio.Semaphore())
            eof_count = [0]
            condition = asyncio.Condition()

            async def notify() -> None:
                async with condition:
                    condition.notify_all()

            def on_eof_callback() -> None:
                eof_count[0] += 1
                asyncio.get_running_loop().create_task(notify())

            router.add_reservation_callback(
                re.compile('.*'),
                lambda x: StdRet.pass_ok(OnCloseTarget(on_eof_callback)),
            )

            event_data = SimpleBinaryWriter()
            await write_binary_event_to_stream(
                event_data, 'e1', 's1', 't1', 2, b'12',
            )

            channel1_writer = SimpleBinaryWriter()
            channel1_reader = create_read_stream(event_data.getvalue())
            channel2_writer = SimpleBinaryWriter()
            channel2_reader = create_read_stream(b'')

            async def create_channel_1() -> StdRet[Tuple[asyncio.StreamReader, BinaryWriter]]:
                return StdRet.pass_ok((channel1_reader, channel1_writer))

            async def create_channel_2() -> StdRet[Tuple[asyncio.StreamReader, BinaryWriter]]:
                return StdRet.pass_ok((channel2_reader, channel2_writer))

            # Channel 1 has handler h1 which can produce event e1
            ret_channel1 = await router.register_channel('ch1', create_channel_1)
            self.assertIsNone(ret_channel1.error)
            res = await router.add_handler('ch1', 'h1', ['e1'], [])
            self.assertIsNone(res.error)

            # Channel 2 has handler h2 which can consume event e1 sent to t1.
            ret_channel2 = await router.register_channel('ch2', create_channel_2)
            self.assertIsNone(ret_channel2.error)
            res = await router.add_handler('ch2', 'h2', [], [('e1', 't1')])
            self.assertIsNone(res.error)

            async with condition:
                await condition.wait_for(lambda: eof_count[0] >= 2)

            # The data read from channel 1's reader should have been sent on to channel 2's writer.
            self.assertEqual(event_data.getvalue(), channel2_writer.getvalue())

        asyncio.run(run_test())
