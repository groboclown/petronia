"""Test the router module."""

from typing import Tuple
import unittest
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.event_stream import (
    BinaryWriter,
    write_binary_event_to_stream, BinaryReader,
)
from petronia_common.event_stream.tests.shared import (
    create_read_stream, SimpleBinaryWriter,
)
from petronia_common.util import StdRet
from ..router import EventRouter, OnCloseTarget


class RouterIntegrationTest(unittest.TestCase):
    """Tests how this will all work together.  Let's see how feasible it is to write."""
    def test_intra_channel(self) -> None:  # pylint: disable=too-many-locals
        """Channel 1 creates an event, which is forwarded on to channel 2."""

        executor = ThreadPoolExecutor()
        router = EventRouter(threading.Semaphore(), executor=executor)
        eof_count = [0]
        condition = threading.Condition()

        def notify() -> None:
            with condition:
                condition.notify_all()

        def on_eof_callback() -> None:
            eof_count[0] += 1
            executor.submit(notify)

        router.add_reservation_callback(
            re.compile('.*'),
            lambda x: StdRet.pass_ok(OnCloseTarget(on_eof_callback)),
        )

        event_data = SimpleBinaryWriter()
        write_binary_event_to_stream(
            event_data, 'e1', 's1', 't1', 2, b'12',
        )

        # Reader represents pulling an event that was created by a channel.
        # Writer represents sending an event to a channel.
        channel1_writer = SimpleBinaryWriter()
        channel1_reader = create_read_stream(event_data.getvalue())
        channel2_writer = SimpleBinaryWriter()
        channel2_reader = create_read_stream(b'')

        # In this model, channel 1 creates an event that is consumed by
        # channel 2.  So, channel 2 must be registered first so it can
        # receive the event.

        def create_channel_1() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((channel1_reader, channel1_writer))

        def create_channel_2() -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
            return StdRet.pass_ok((channel2_reader, channel2_writer))

        # Channel 2 has handler h2 which can consume event e1 sent to t1.
        ret_channel2 = router.register_channel('ch2', create_channel_2)
        self.assertIsNone(ret_channel2.error)
        res = router.add_handler('ch2', 'h2', [], [('e1', 't1')])
        self.assertIsNone(res.error)

        # Channel 1 has handler h1 which can produce event e1
        ret_channel1 = router.register_channel('ch1', create_channel_1)
        self.assertIsNone(ret_channel1.error)
        res = router.add_handler('ch1', 'h1', ['e1'], [])
        self.assertIsNone(res.error)

        with condition:
            condition.wait_for(lambda: eof_count[0] >= 2)
        executor.shutdown(True)

        # The data read from channel 1's reader should have been sent on to channel 2's writer.
        self.assertEqual(event_data.getvalue(), channel2_writer.getvalue())
