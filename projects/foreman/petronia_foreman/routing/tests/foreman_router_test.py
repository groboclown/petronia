"""Test the module"""

from typing import Sequence, Tuple, List, Optional
import unittest
import unittest.mock
import configparser
import concurrent.futures
import threading

from petronia_common.event_stream import BinaryWriter, BinaryReader, RawEvent
from petronia_common.util import StdRet, RET_OK_NONE, i18n
from .. import foreman_router
from ..event_handlers import ExtensionLoaderTarget, TargetHandlerRuntimeContext
from ...event_router import EventRouter
from ...event_router.channel import EventFilterResult
from ...events import foreman
from ...launcher.loader import IMPLEMENTATIONS
from ...configuration import RuntimeConfig, BootExtensionMetadata
from ...launcher import RuntimeContext, AbcLauncherCategory


class ForemanRouterTest(unittest.TestCase):
    """Test the ForemanRouter class."""
    def setUp(self) -> None:
        self.router: Optional[foreman_router.ForemanRouter] = None

    def tearDown(self) -> None:
        if self.router:
            self.assertTrue(self.router.stop(2.0))  # pragma no cover
            self.router = None

    def test_not_running(self) -> None:
        """Test the various methods which require the router to be in a running state."""
        self.router = foreman_router.ForemanRouter([])
        self.assertTrue(self.router.stop())
        self.assertTrue(self.router.join())
        self.assertRaisesRegex(
            AttributeError,
            r'router not running',
            self.router.start_extension,
            's1', foreman.LauncherStartExtensionRequestEvent(
                'n1', [1, 2, 3], [], 'r', foreman.SendEventAccess([], []), None, [],
            ),
        )
        self.assertRaisesRegex(
            AttributeError,
            r'router not running',
            self.router.start_boot_extension,
            BootExtensionMetadata(
                'n1', (1, 2, 3), 'r', [], [], [], {}, {}, [],
            ),
        )

    def test_start__normal(self) -> None:
        """Ensure the start method runs right."""
        self.router = foreman_router.ForemanRouter([])
        self.assertTrue(self.router.start())

        # It should be running, so calling again should still return true.
        self.assertTrue(self.router.start())


class ExtensionLoaderCallbackTest(unittest.TestCase):
    """Test the ExtensionLoaderCallback class."""
    def test_use_case(self) -> None:
        """Test the full life-cycle use case."""
        expected = ExtensionLoaderTarget(TargetHandlerRuntimeContext())
        callback = foreman_router.ExtensionLoaderCallback(expected)
        res1 = callback('name1')
        self.assertIsNone(res1.error)
        self.assertIs(expected, res1.value)
        res2 = callback('name2')
        self.assertIsNotNone(res2.error)


class LauncherCategoryStateTest(unittest.TestCase):
    """Test the LauncherCategoryState class"""

    def setUp(self) -> None:
        self._orig_implementations = dict(IMPLEMENTATIONS)

    def tearDown(self) -> None:
        IMPLEMENTATIONS.clear()
        IMPLEMENTATIONS.update(self._orig_implementations)

    def test_getters(self) -> None:
        """Test the getter methods"""
        config = configparser.ConfigParser()
        config.add_section('lc')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        self.assertEqual('lc', lcs.name)

    def test_create_category__with_category_error(self) -> None:
        """Test create_category"""
        config = configparser.ConfigParser()
        config.add_section('lc')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        runtime = unittest.mock.Mock(RuntimeContext())
        executor = concurrent.futures.ThreadPoolExecutor()
        # Ensure nothing is started
        executor.shutdown(wait=True)
        res = lcs.create_category(runtime, executor)
        self.assertIsNotNone(res.error)

    def test_create_category__with_launcher_error(self) -> None:
        """Test create_category"""
        config = configparser.ConfigParser()
        config.add_section('lc')
        config.set('lc', 'runner', 'in-memory')
        config.set('lc', 'extension-load-timeout', 'not-a-number')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        runtime = unittest.mock.Mock(RuntimeContext())
        executor = concurrent.futures.ThreadPoolExecutor()
        # Ensure nothing is started
        executor.shutdown(wait=True)
        res = lcs.create_category(runtime, executor)
        self.assertIsNotNone(res.error)

    def test_create_category__with_bad_init(self) -> None:
        """Test create_category"""
        IMPLEMENTATIONS['bad'] = _create_fails_init
        config = configparser.ConfigParser()
        config.add_section('lc')
        config.set('lc', 'runner', 'bad')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        runtime = unittest.mock.Mock(RuntimeContext())
        executor = concurrent.futures.ThreadPoolExecutor()
        res = lcs.create_category(runtime, executor)
        self.assertIs(FailsInitializationLauncher.ERROR, res)

    def test_create_category__with_bad_executor(self) -> None:
        """Test create_category"""
        config = configparser.ConfigParser()
        config.add_section('lc')
        config.set('lc', 'runner', 'in-memory')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        runtime = unittest.mock.Mock(RuntimeContext())
        executor = concurrent.futures.ThreadPoolExecutor()
        # Ensure nothing is started
        executor.shutdown(wait=True)
        res = lcs.create_category(runtime, executor)
        self.assertIsNotNone(res.error)

    def test_create_category__ok(self) -> None:
        """Test create_category"""
        config = configparser.ConfigParser()
        config.add_section('lc')
        config.set('lc', 'runner', 'in-memory')
        lcs = foreman_router.LauncherCategoryState(RuntimeConfig('lc', config))
        runtime = unittest.mock.Mock(RuntimeContext())
        executor = concurrent.futures.ThreadPoolExecutor()
        res = lcs.create_category(runtime, executor)
        self.assertIsNone(res.error)
        executor.shutdown(wait=True)


class LauncherRuntimeContextTest(unittest.TestCase):
    """Test the LauncherRuntimeContext class"""

    def setUp(self) -> None:
        self.executor = concurrent.futures.ThreadPoolExecutor()

    def tearDown(self) -> None:
        self.executor.shutdown(wait=True)

    def test_register_channel(self) -> None:
        """Test the register_channel method."""
        lock = threading.Semaphore()
        router = EventRouter(lock, None, self.executor)
        lrc = foreman_router.LauncherRuntimeContext(router, self.executor)
        creator = TestableChannelCreator()
        returns: StdRet[Tuple[BinaryReader, BinaryWriter]] = StdRet.pass_errmsg('x', i18n('msg'))
        creator.returns.append(returns)
        res = lrc.register_channel('ch1', creator.creator)
        self.assertEqual(returns, res)
        self.assertEqual(1, creator.called)
        # Was not registered because the creator returned an error.
        self.assertEqual((), router.get_registered_channel_names())

    def test_close_channel(self) -> None:
        """Test the close_channel method."""
        lock = threading.Semaphore()
        router = unittest.mock.Mock(EventRouter(lock, None, self.executor))
        router.configure_mock(**{
            'close_channel.return_value': False,
        })
        lrc = foreman_router.LauncherRuntimeContext(router, self.executor)
        res = lrc.close_channel('ch1')
        self.assertFalse(res)
        router.close_channel.assert_called_with('ch1')

    def test_add_handler(self) -> None:
        """Test the add_handler method."""
        lock = threading.Semaphore()
        router = unittest.mock.Mock(EventRouter(lock, None, self.executor))
        returns: StdRet[None] = StdRet.pass_errmsg('x', i18n('msg'))
        router.configure_mock(**{
            'add_handler.return_value': returns,
        })
        lrc = foreman_router.LauncherRuntimeContext(router, self.executor)
        res = lrc.add_handler('ch1', 'h1', [], [], [])
        self.assertIs(res, returns)
        router.add_handler.assert_called_with('ch1', 'h1', [], [], [])

        # clear the error...
        self.assertIsNotNone(res.error)

    def test_remove_handler(self) -> None:
        """Test the remove_handler method."""
        lock = threading.Semaphore()
        router = unittest.mock.Mock(EventRouter(lock, None, self.executor))
        router.configure_mock(**{
            'remove_handler.return_value': True,
        })
        lrc = foreman_router.LauncherRuntimeContext(router, self.executor)
        res = lrc.remove_handler('h1')
        self.assertTrue(res)
        router.remove_handler.assert_called_with('h1')

    def test_add_internal_event_handler(self) -> None:
        """Test the add_internal_event_handler method."""
        def handler(
            _event_id: str, _event_source_id: str, _event_target_id: str, _event: RawEvent,
        ) -> EventFilterResult:
            raise NotImplementedError  # pragma no cover

        lock = threading.Semaphore()
        router = unittest.mock.Mock(EventRouter(lock, None, self.executor))
        lrc = foreman_router.LauncherRuntimeContext(router, self.executor)
        lrc.add_internal_event_handler('ch1', handler)
        router.add_internal_event_handler.assert_called_with('ch1', handler)


def _create_fails_init(options: RuntimeConfig) -> AbcLauncherCategory:
    return FailsInitializationLauncher(options)


class FailsInitializationLauncher(AbcLauncherCategory):
    """Fails in the ways we want."""
    ERROR: StdRet[None] = StdRet.pass_errmsg('x', i18n('err'))

    def is_valid(self) -> StdRet[None]:
        return RET_OK_NONE  # pragma no cover

    def initialize(self, context: RuntimeContext) -> StdRet[None]:
        return FailsInitializationLauncher.ERROR  # pragma no cover

    def start_extension(
            self, handler_id: str, start_event: foreman.LauncherStartExtensionRequestEvent,
    ) -> StdRet[None]:
        return FailsInitializationLauncher.ERROR  # pragma no cover

    def get_active_handler_ids(self) -> Sequence[str]:
        return []  # pragma no cover

    def stop_extension(self, handler_id: str) -> StdRet[None]:
        return FailsInitializationLauncher.ERROR  # pragma no cover

    def stop(self) -> StdRet[None]:
        return FailsInitializationLauncher.ERROR  # pragma no cover


class TestableChannelCreator:
    """Testable channel creator callback."""
    def __init__(self) -> None:
        self.called = 0
        self.returns: List[StdRet[Tuple[BinaryReader, BinaryWriter]]] = []

    def creator(self) -> StdRet[Tuple[BinaryReader, BinaryWriter]]:
        """The creator callback function."""
        self.called += 1
        return self.returns.pop(0)
