"""Test the router module."""

from typing import Tuple
import unittest
import asyncio
from petronia_common.event_stream import (
    BinaryWriter,
    to_raw_event_object,
)
from petronia_common.util import StdRet, PetroniaReturnError, i18n
from .. import router


class OnCloseTargetTest(unittest.TestCase):
    """Tests the OnCloseTarget class"""
    def setUp(self) -> None:
        self.count = [0]

    def _callback(self) -> None:
        self.count[0] += 1

    def test_on_eof(self) -> None:
        """Run the on_eof method."""
        target = router.OnCloseTarget(self._callback)
        target.on_eof()
        self.assertEqual(1, self.count[0])

    def test_can_consume(self) -> None:
        """Run the can_consume method."""
        target = router.OnCloseTarget(self._callback)
        self.assertFalse(target.can_consume('x', 'y', 'z'))
        self.assertEqual(0, self.count[0])

    def test_on_error(self) -> None:
        """Run the on_error method."""
        target = router.OnCloseTarget(self._callback)
        self.assertFalse(target.on_error(PetroniaReturnError()))
        self.assertEqual(0, self.count[0])

    def test_consume(self) -> None:
        """Run the consume method."""
        target = router.OnCloseTarget(self._callback)

        async def run_test() -> None:
            res = await target.consume(to_raw_event_object('x', 'y', 'z', {}))
            self.assertFalse(res)
            self.assertEqual(0, self.count[0])

        asyncio.run(run_test())


class EventRouterTest(unittest.TestCase):
    """Tests the router basic functionality."""

    def test_register_channel__blocked(self) -> None:
        """Test register_channel when the registration callback blocks it."""

        async def create_reader_writer() -> StdRet[Tuple[asyncio.StreamReader, BinaryWriter]]:
            raise Exception('Should not be called')

        async def run_test() -> None:
            lock = asyncio.Semaphore()
            event_router = router.EventRouter(lock)
            event_router.add_reservation_callback('ch', lambda _: StdRet.pass_errmsg(
                'x', i18n('expected error'),
            ))
            res = await event_router.register_channel('ch', create_reader_writer)
            self.assertTrue(res.has_error)
            self.assertEqual(
                'expected error',
                res.valid_error.messages()[0].message,
            )

        asyncio.run(run_test())

    def test_close_channel__unregistered(self) -> None:
        """Test register_channel when the registration callback blocks it."""

        async def create_reader_writer() -> StdRet[Tuple[asyncio.StreamReader, BinaryWriter]]:
            raise Exception('Should not be called')

        async def run_test() -> None:
            lock = asyncio.Semaphore()
            event_router = router.EventRouter(lock)
            event_router.add_reservation_callback('ch', lambda _: StdRet.pass_errmsg(
                'x', i18n('expected error'),
            ))
            res = await event_router.register_channel('ch', create_reader_writer)
            self.assertTrue(res.has_error)
            self.assertEqual(
                'expected error',
                res.valid_error.messages()[0].message,
            )

        asyncio.run(run_test())
