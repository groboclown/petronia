"""Test the module."""

from typing import List, Tuple, Dict, Any
import unittest
import time
from petronia_common.event_stream import (
    RawBinaryReader,
    to_raw_event_binary,
    to_raw_event_object, RawEvent, BinaryReader,
    is_raw_event_binary,
    raw_event_id, raw_event_source_id, raw_event_target_id, raw_event_binary_size,
    as_raw_event_object_data, as_raw_event_binary_data_reader,
    write_binary_event_to_stream,
    write_object_event_to_stream,
)
from petronia_common.event_stream.tests.shared import (
    create_raw_reader, create_read_stream, SimpleBinaryWriter,
)
from petronia_common.util import StdRet, UserMessage, i18n, RET_OK_NONE
from petronia_common.util.error import SimplePetroniaReturnError
from .. import registry, main


class AbstractEventForwarderTargetTest(unittest.TestCase):
    """Test the AbstractEventForwarderTargetTest class"""

    def test_on_error__timeout(self) -> None:
        """Test on_error with a time-out"""
        target = main.AbstractEventForwarderTarget(
            'e-1', None, 't-1', 0.001,
        )
        then = time.time() + 0.001
        while time.time() < then:
            time.sleep(0.01)
        self.assertEqual(True, target.on_error(SimplePetroniaReturnError()))

    def test_on_error__not_timed_out(self) -> None:
        """Test on_error with a timer but not timed out"""
        now = time.time()
        target = main.AbstractEventForwarderTarget(
            'e-1', None, 't-1', 10000.0,
        )
        self.assertTrue(now + 10000.0 > time.time())
        self.assertEqual(False, target.on_error(SimplePetroniaReturnError()))

    def test_on_error__no_timer(self) -> None:
        """Test on_error without a timer"""
        target = main.AbstractEventForwarderTarget(
            'e-1', None, 't-1', -1,
        )
        self.assertEqual(False, target.on_error(SimplePetroniaReturnError()))

    def test_can_consume__no_source(self) -> None:
        """Test can_consume with None source id match."""
        target = main.AbstractEventForwarderTarget(
            'e-1', None, 't-1', -1,
        )
        self.assertEqual(False, target.can_consume('x1', 's1', 'tx'))
        self.assertEqual(False, target.can_consume('x1', 's1', 't-1'))
        self.assertEqual(False, target.can_consume('e-1', 's1', 'tx'))
        self.assertEqual(True, target.can_consume('e-1', 's1', 't-1'))

    def test_can_consume__with_source(self) -> None:
        """Test can_consume with None source id match."""
        target = main.EventObjectForwarderTarget(
            'e-1', 's-1', 't-1', -1,
            registry.EventObjectParser(_good_parser),
            MockEventObjectTarget(),
        )
        self.assertEqual(False, target.can_consume('x1', 'sx', 'tx'))
        self.assertEqual(False, target.can_consume('x1', 'sx', 't-1'))
        self.assertEqual(False, target.can_consume('e-1', 'sx', 'tx'))
        self.assertEqual(False, target.can_consume('e-1', 'sx', 't-1'))
        self.assertEqual(False, target.can_consume('x1', 's-1', 'tx'))
        self.assertEqual(False, target.can_consume('x1', 's-1', 't-1'))
        self.assertEqual(False, target.can_consume('e-1', 's-1', 'tx'))
        self.assertEqual(True, target.can_consume('e-1', 's-1', 't-1'))


class EventObjectForwarderTargetTest(unittest.TestCase):
    """Test the EventObjectForwarderTarget class"""

    def test_on_eof(self) -> None:
        """Test the on_eof method."""
        mock = MockEventObjectTarget()
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', -1,
            registry.EventObjectParser(_good_parser), mock,
        )
        target.on_eof()
        self.assertEqual(
            [('on_close', '', '', MockEventObjectTarget.STATIC_OBJ)],
            mock.call_order,
        )

    def test_consume__not_object(self) -> None:
        """Test consume."""
        mock = MockEventObjectTarget()
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', -1,
            registry.EventObjectParser(_good_parser), mock,
        )
        self.assertEqual(
            False,
            target.consume_binary(
                'e-1', 's-1', 't-1', 2, create_raw_reader(b'12'),
            ),
        )
        # Should never reach the caller.
        self.assertEqual(
            [],
            mock.call_order,
        )

    def test_consume__valid_false__no_expiration(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventObjectTarget()
        mock.returns.append(False)
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', -1,
            registry.EventObjectParser(_good_parser), mock,
        )
        self.assertEqual(
            False,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mock.call_order,
        )

    def test_consume__valid_false__expired(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventObjectTarget()
        mock.returns.append(False)
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', 0.001,
            registry.EventObjectParser(_good_parser), mock,
        )
        then = time.time() + 0.001
        while time.time() < then:
            time.sleep(0.01)
        self.assertEqual(
            True,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mock.call_order,
        )

    def test_consume__valid_false_not_expired(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventObjectTarget()
        mock.returns.append(False)
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', 1000.0,
            registry.EventObjectParser(_good_parser), mock,
        )
        self.assertEqual(
            False,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mock.call_order,
        )

    def test_consume__valid_true(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventObjectTarget()
        mock.returns.append(True)
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', -1,
            registry.EventObjectParser(_good_parser), mock,
        )
        self.assertEqual(
            True,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mock.call_order,
        )

    def test_consume__bad_parsing(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventObjectTarget()
        mock.returns.append(True)
        target = main.EventObjectForwarderTarget(
            'e-1', None, 't-1', -1,
            registry.EventObjectParser(_bad_parser), mock,
        )
        self.assertEqual(
            False,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        self.assertEqual(
            [],
            mock.call_order,
        )


class EventBinaryForwarderTargetTest(unittest.TestCase):
    """Test the EventBinaryForwarderTarget class"""

    def test_on_eof(self) -> None:
        """Test the on_eof method."""
        mock = MockEventBinaryTarget()
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', -1,
            mock,
        )
        target.on_eof()
        self.assertEqual(
            [('on_close', '', '', b'')],
            mock.call_order,
        )

    def test_consume__not_binary(self) -> None:
        """Test consume."""
        mock = MockEventBinaryTarget()
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', -1,
            mock,
        )
        self.assertEqual(
            False,
            target.consume_object(
                'e-1', 's-1', 't-1', {},
            ),
        )
        # Should never reach the caller.
        self.assertEqual(
            [],
            mock.call_order,
        )

    def test_consume__valid_false__no_expiration(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventBinaryTarget()
        mock.returns.append(False)
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', -1,
            mock,
        )
        self.assertEqual(
            False,
            target.consume_binary(
                'e-1', 's-1', 't-1', 2, create_raw_reader(b'12'),
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', b'12')],
            mock.call_order,
        )

    def test_consume__valid_false__expired(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventBinaryTarget()
        mock.returns.append(False)
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', 0.001,
            mock,
        )
        then = time.time() + 0.001
        while time.time() < then:
            time.sleep(0.01)
        self.assertEqual(
            True,
            target.consume_binary(
                'e-1', 's-1', 't-1', 2, create_raw_reader(b'21'),
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', b'21')],
            mock.call_order,
        )

    def test_consume__valid_false_not_expired(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventBinaryTarget()
        mock.returns.append(False)
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', 1000.0,
            mock,
        )
        self.assertEqual(
            False,
            target.consume_binary(
                'e-1', 's-1', 't-1', 2, create_raw_reader(b'32'),
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', b'32')],
            mock.call_order,
        )

    def test_consume__valid_true(self) -> None:
        """Test consume, with a valid consumption, but returning false, and no expiration."""
        mock = MockEventBinaryTarget()
        mock.returns.append(True)
        target = main.EventBinaryForwarderTarget(
            'e-1', None, 't-1', -1,
            mock,
        )
        self.assertEqual(
            True,
            target.consume_binary(
                'e-1', 's-1', 't-1', 3, create_raw_reader(b'123'),
            ),
        )
        self.assertEqual(
            [('on_event', 's-1', 't-1', b'123')],
            mock.call_order,
        )


class EventRegistryContextImplTest(unittest.TestCase):
    """Test the EventRegistryContextImpl class"""

    def test_receive_loop(self) -> None:
        """Test out registering an event object, registering an object handler, then receiving
        the event."""
        impl = main.EventRegistryContextImpl(
            _events_as_reader(
                # Send two of these objects, but with the target returning True
                # first, only the first one is consumed.
                to_raw_event_object('e-1', 's-1', 't-1', {}),
                to_raw_event_object('e-1', 's-2', 't-1', {}),

                # Same thing, but for binary events.
                to_raw_event_binary('e-2', 's-4', 't-1', 1, create_raw_reader(b'x')),
                to_raw_event_binary('e-2', 's-5', 't-1', 1, create_raw_reader(b'y')),
            ),
            SimpleBinaryWriter(),
        )
        res = impl.register_event('e-1', registry.EventObjectParser(_good_parser))
        self.assertIsNone(res.error)
        mock = MockEventObjectTarget()
        mock.returns.append(True)
        impl.register_target('e-1', 't-1', mock)
        mock_bin = MockEventBinaryTarget()
        mock_bin.returns.append(True)
        impl.register_binary_target('e-2', 't-1', mock_bin)
        impl.run()
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mock.call_order,
        )
        self.assertEqual(
            [('on_event', 's-4', 't-1', b'x')],
            mock_bin.call_order,
        )

    def test_register_target__no_parser(self) -> None:
        """Test register_target when there is no parser for the given event ID."""
        impl = main.EventRegistryContextImpl(create_read_stream(b''), SimpleBinaryWriter())
        res = impl.register_target('not-registered', 't1', MockEventObjectTarget())
        self.assertTrue(res.has_error)
        self.assertEqual(
            'No registered parser for not-registered',
            ';'.join([m.debug() for m in res.valid_error.messages()]),
        )

    def test_send_event(self) -> None:
        """Test sending an object event."""
        writer = SimpleBinaryWriter()
        impl = main.EventRegistryContextImpl(create_read_stream(b''), writer)
        res = impl.send_event('s-1', 't-1', TestEvent())
        self.assertIsNone(res.error)
        expected = SimpleBinaryWriter()
        write_object_event_to_stream(
            expected,
            TestEvent.FULL_EVENT_NAME, 's-1', 't-1', {'x': 'y'},
        )
        self.assertEqual(expected.getvalue(), writer.getvalue())

    def test_send_binary_event(self) -> None:
        """Test sending an object event."""
        writer = SimpleBinaryWriter()
        impl = main.EventRegistryContextImpl(create_read_stream(b''), writer)
        res = impl.send_binary_event('s-1', 't-1', 'e-1', b'1234')
        self.assertIsNone(res.error)
        expected = SimpleBinaryWriter()
        write_binary_event_to_stream(
            expected,
            'e-1', 's-1', 't-1', 4, b'1234',
        )
        self.assertEqual(expected.getvalue(), writer.getvalue())


class ExtensionRunnerTest(unittest.TestCase):
    """Test the extension_runner function."""

    def test_failed_factory(self) -> None:
        """Test out the situation where a factory returns an error."""
        def factory0(_state: str, _context: registry.EventRegistryContext) -> StdRet[None]:
            return RET_OK_NONE

        def factory1(_state: str, _context: registry.EventRegistryContext) -> StdRet[None]:
            return StdRet.pass_error(BAD_ERROR)

        def factory2(_state: str, _context: registry.EventRegistryContext) -> StdRet[None]:
            # Should never be reached
            raise NotImplementedError  # pragma no cover

        res = main.extension_runner(
            create_read_stream(b''),
            SimpleBinaryWriter(),
            's',
            factory0, factory1, factory2,
        )
        self.assertTrue(res.has_error)
        self.assertEqual(
            BAD_ERROR.messages(),
            res.valid_error.messages(),
        )

    def test_simple_runner_read(self) -> None:
        """Test out registering an event object, registering an object handler, then receiving
        the event."""
        factory_called = [False, False]
        mocks = [MockEventObjectTarget('0'), MockEventObjectTarget('1')]

        def factory0(state: List[int], context: registry.EventRegistryContext) -> StdRet[None]:
            state[0] += 1
            factory_called[0] = True
            context.register_event('e-1', registry.EventObjectParser(_good_parser))
            mocks[0].returns.append(True)
            context.register_target('e-1', 't-1', mocks[0])
            return RET_OK_NONE

        def factory1(state: List[int], context: registry.EventRegistryContext) -> StdRet[None]:
            state[0] += 1
            factory_called[1] = True
            context.register_event('e-2', registry.EventObjectParser(_good_parser))
            mocks[1].returns.append(False)
            mocks[1].returns.append(True)
            context.register_target('e-2', 't-1', mocks[1])
            return RET_OK_NONE

        shared_state = [0]
        res = main.extension_runner(
            _events_as_reader(
                # Send two of these objects, but with the target returning True
                # first, only the first one is consumed.
                to_raw_event_object('e-1', 's-1', 't-1', {}),
                to_raw_event_object('e-1', 's-2', 't-1', {}),

                # For the second target, it should consume the first 2.
                to_raw_event_object('e-2', 's-3', 't-1', {}),
                to_raw_event_object('e-2', 's-4', 't-1', {}),
                to_raw_event_object('e-2', 's-5', 't-1', {}),
            ),
            SimpleBinaryWriter(),
            shared_state,
            factory0, factory1,
        )
        self.assertIsNone(res.error)
        self.assertEqual(
            [True, True],
            factory_called,
        )
        self.assertEqual([2], shared_state)
        self.assertEqual(
            [('on_event', 's-1', 't-1', GOOD_OBJECT)],
            mocks[0].call_order,
        )
        self.assertEqual(
            [
                ('on_event', 's-3', 't-1', GOOD_OBJECT),
                ('on_event', 's-4', 't-1', GOOD_OBJECT),
            ],
            mocks[1].call_order,
        )


class MockEventObjectTarget(registry.EventObjectTarget[object]):
    """Mock EventObjectTarget instance."""
    STATIC_OBJ = object()

    __slots__ = ('call_order', 'returns', 'name')

    def __init__(self, name: str = 'x') -> None:
        self.name = name
        self.returns: List[bool] = []
        self.call_order: List[Tuple[str, str, str, object]] = []

    def on_event(self, source: str, target: str, event: object) -> bool:
        self.call_order.append(('on_event', source, target, event))
        return self.returns.pop(0)

    def on_close(self) -> None:
        self.call_order.append(('on_close', '', '', MockEventObjectTarget.STATIC_OBJ))


class MockEventBinaryTarget(registry.EventBinaryTarget):
    """Mock EventBinaryTarget instance."""

    __slots__ = ('call_order', 'returns',)

    def __init__(self) -> None:
        self.returns: List[bool] = []
        self.call_order: List[Tuple[str, str, str, bytes]] = []

    def on_event(self, source: str, target: str, size: int, reader: RawBinaryReader) -> bool:
        self.call_order.append(('on_event', source, target, reader(size)))
        return self.returns.pop(0)

    def on_close(self) -> None:
        self.call_order.append(('on_close', '', '', b''))


GOOD_OBJECT = object()


def _good_parser(_data: Dict[str, Any]) -> StdRet[object]:
    return StdRet.pass_ok(GOOD_OBJECT)


BAD_ERROR = SimplePetroniaReturnError(UserMessage('x', i18n('y')))


def _bad_parser(_data: Dict[str, Any]) -> StdRet[object]:
    return StdRet.pass_error(BAD_ERROR)


def _events_as_reader(*events: RawEvent) -> BinaryReader:
    writer = SimpleBinaryWriter()
    for event in events:
        if is_raw_event_binary(event):
            write_binary_event_to_stream(
                writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                raw_event_binary_size(event),
                as_raw_event_binary_data_reader(event),
            )
        else:
            write_object_event_to_stream(
                writer,
                raw_event_id(event),
                raw_event_source_id(event),
                raw_event_target_id(event),
                as_raw_event_object_data(event),
            )
    return create_read_stream(writer.getvalue())


class TestEvent:
    """
    Follows the pattern of an event generated from an extension yaml file.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'my.extension:test'
    SHORT_EVENT_NAME = 'test'

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return TestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {'x': 'y'}
