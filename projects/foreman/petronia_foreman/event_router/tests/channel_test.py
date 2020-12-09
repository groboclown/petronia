"""Test the module."""

from typing import List, Tuple
import unittest
import io

from petronia_common.event_stream import to_raw_event_object, to_raw_event_binary, RawBinaryReader
from petronia_common.event_stream.tests.shared import SimpleBinaryWriter
from petronia_common.util import PetroniaReturnError
from .. import channel


class EventChannelTest(unittest.TestCase):
    """Test the EventChannel class."""

    def test_getters(self) -> None:
        """Test the repr, name, and so on methods."""
        ec1 = channel.EventChannel(
            'n1', io.BytesIO(b''), SimpleBinaryWriter(), OnErrorSpy().on_error,
        )
        self.assertEqual(
            'EventChannel(n1)',
            repr(ec1),
        )
        self.assertEqual('n1', ec1.name)
        self.assertTrue(ec1.is_alive())
        self.assertFalse(ec1.contains_handler_id('foo'))
        self.assertFalse(ec1.on_error(PetroniaReturnError()))

    def test_not_alive_actions(self) -> None:
        """Test that actions that require the channel to be alive work as expected."""
        ec1 = channel.EventChannel(
            'n1', io.BytesIO(b''), SimpleBinaryWriter(), OnErrorSpy().on_error,
        )
        ec1.close_access()
        res = ec1.add_handler('x', [], [])
        self.assertTrue(res.has_error)
        self.assertEqual(
            'route n1 is closed',
            '\n'.join(msg.debug() for msg in res.valid_error.messages()),
        )
        res = ec1.add_handler_listener('h1', None, None)
        self.assertTrue(res.has_error)
        self.assertEqual(
            'route n1 is closed',
            '\n'.join(msg.debug() for msg in res.valid_error.messages()),
        )
        res = ec1.remove_handler_listener('h1', None, None)
        self.assertTrue(res.has_error)
        self.assertEqual(
            'route n1 is closed',
            '\n'.join(msg.debug() for msg in res.valid_error.messages()),
        )
        self.assertFalse(ec1.can_produce('e1'))
        self.assertFalse(ec1.can_consume('e1', 's1', 't1'))
        self.assertTrue(ec1.on_error(PetroniaReturnError()))
        self.assertTrue(ec1.consume(to_raw_event_object('e1', 's1', 't1', {})))

    def test_add_remove_handler_listeners(self) -> None:
        """Test add then remove of a handler and listeners."""
        ec1 = channel.EventChannel(
            'n1', io.BytesIO(b''), SimpleBinaryWriter(), OnErrorSpy().on_error,
        )
        res = ec1.add_handler('h1', ['e1'], [('e2', 't2')])
        self.assertTrue(res.ok)
        res = ec1.add_handler_listener('h1', None, None)
        self.assertTrue(res.ok)
        res = ec1.remove_handler_listener('h1', None, None)
        self.assertTrue(res.ok)
        res = ec1.remove_handler_listener('h1', None, None)
        self.assertTrue(res.has_error)
        res = ec1.remove_handler('h1')
        self.assertTrue(res.ok)
        res = ec1.remove_handler('h1')
        self.assertTrue(res.has_error)

    def test_consume_object__with_error(self) -> None:
        """Test sending an object event that causes an error."""
        spy = OnErrorSpy()
        ec1 = channel.EventChannel(
            'n1', io.BytesIO(b''), ErrorBinaryWriter(), spy.on_error,
        )
        # Stop the channel w/ an error
        spy.responses.append(True)
        res = ec1.consume(to_raw_event_object('e1', 's1', 't1', {}))
        self.assertTrue(res)
        self.assertFalse(ec1.is_alive())
        self.assertEqual(1, len(spy.called))
        self.assertEqual('n1', spy.called[0][0])

    def test_consume_binary__with_error(self) -> None:
        """Test sending a binary event that causes an error."""
        spy = OnErrorSpy()
        ec1 = channel.EventChannel(
            'n1', io.BytesIO(b''), ErrorBinaryWriter(), spy.on_error,
        )
        # Do not stop the channel on error
        spy.responses.append(False)
        res = ec1.consume(to_raw_event_binary('e1', 's1', 't1', 2, create_raw_read_stream(b'12')))
        self.assertFalse(res)
        self.assertTrue(ec1.is_alive())
        self.assertEqual(1, len(spy.called))
        self.assertEqual('n1', spy.called[0][0])


def create_raw_read_stream(data: bytes) -> RawBinaryReader:
    """Create a raw binary reader function."""
    stream = io.BytesIO(data)

    def do_read(max_read_count: int = -1) -> bytes:
        return stream.read(max_read_count)

    return do_read


class OnErrorSpy:
    """Spies on-error callbacks."""
    def __init__(self) -> None:
        self.called: List[Tuple[str, PetroniaReturnError]] = []
        self.responses: List[bool] = []

    def on_error(self, channel_name: str, error: PetroniaReturnError) -> bool:
        """On-Error callback."""
        self.called.append((channel_name, error))
        return self.responses.pop(0)


class ErrorBinaryWriter:
    """Generates an error on write."""
    def write(self, data: bytes) -> None:  # pylint: disable=no-self-use
        """Raises the error."""
        raise OSError('bad write')
