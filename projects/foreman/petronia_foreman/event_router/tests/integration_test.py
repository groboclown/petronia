"""Test the router module."""

from typing import Tuple
import unittest
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from petronia_common.event_stream import (
    BinaryWriter,
    write_binary_event_to_stream, BinaryReader, EventForwarderTarget,
)
from petronia_common.event_stream.tests.shared import SimpleBinaryWriter
from petronia_common.util import StdRet
from petronia_common.util.input_buffer import StreamedBinaryReader
from ..router import EventRouter, OnCloseTarget


class RouterIntegrationTest(unittest.TestCase):
    """Tests how this will all work together.  Let's see how feasible it is to write."""

    def test_intra_channel_multiple(self) -> None:
        """Run the intra-channel test multiple times.  An occasional thread locking
        state has been seen, and this helps check that it doens't still happen."""
        for _ in range(50):
            # print(f"!!!!!!! running {i}")
            self.test_intra_channel()

    def test_intra_channel(self) -> None:  # pylint: disable=too-many-locals
        """Channel 1 creates an event, which is forwarded on to channel 2."""

        executor = ThreadPoolExecutor(4)
        try:
            router = EventRouter(threading.Semaphore(), executor=executor)
            eof_count = [0]
            condition = threading.Condition()

            def on_reservation(_channel_name: str) -> StdRet[EventForwarderTarget]:
                def on_eof_callback() -> None:
                    eof_count[0] += 1
                    # print(f"Encountered EOF {eof_count[0]} in {channel_name}")
                    with condition:
                        # print("Test calling notify all.")
                        condition.notify_all()
                ret = OnCloseTarget(on_eof_callback)
                # print(f"Test: registering channel {channel_name} with target {ret}")
                return StdRet.pass_ok(ret)

            router.add_reservation_callback(
                re.compile('.*'),
                on_reservation,
            )

            event_data = SimpleBinaryWriter()
            write_binary_event_to_stream(
                event_data, 'e1', 's1', 't1', 2, b'12',
            )

            # Reader represents pulling an event that was created by a channel.
            # Writer represents sending an event to a channel.
            channel1_writer = SimpleBinaryWriter()
            # Channel 1 reader: if it produces data immediately, then it can
            #   have an event read before the handler is registered to allow it
            #   to be produced.
            channel1_reader = StreamedBinaryReader()
            channel2_writer = SimpleBinaryWriter()
            # Channel 2 reader: if we have a simple reader that reaches EOF immediately,
            # then the channel itself is closed off as soon as EOF is reached.  We only
            # want it closed AFTER the events are processed.
            channel2_reader = StreamedBinaryReader()

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
            # Registered after consumer, so that the produced event has a chance to
            # be consumed.
            ret_channel1 = router.register_channel('ch1', create_channel_1)
            self.assertIsNone(ret_channel1.error)
            res = router.add_handler('ch1', 'h1', ['e1'], [])
            self.assertIsNone(res.error)

            # Now that channel 1 is registered to be able to produce the event,
            # have it produce the eent.
            channel1_reader.feed_data(event_data.getvalue())
            channel1_reader.feed_eof()

            # print(f"Test: waiting for eof count to reach 2")
            loop_count = 0
            with condition:
                while eof_count[0] < 2:
                    loop_count += 1
                    condition.wait_for(lambda: eof_count[0] >= 2, 0.2)
                    if len(channel2_writer.getvalue()) > 0:
                        # print("Test: Closing readers")
                        channel1_reader.feed_eof()
                        channel2_reader.feed_eof()
                    elif loop_count > 10:
                        print("Test: waited 5 seconds without channel 2 sending to writer")
                    self.assertTrue(loop_count < 20, "Tried for 4 seconds for the test to finish.")

            # The data read from channel 1's reader should have been sent on to channel 2's writer.
            self.assertEqual(event_data.getvalue(), channel2_writer.getvalue())
        finally:
            executor.shutdown(True)
