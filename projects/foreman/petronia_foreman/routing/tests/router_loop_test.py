"""Test the module."""

import unittest
import unittest.mock
import concurrent.futures
import threading
from petronia_common.util import StdRet, i18n, RET_OK_NONE
from .. import router_loop
from ...configuration import BootExtensionMetadata
from ...event_router import EventRouter
from ...events import foreman
from ...launcher.internal import create_internal_launcher


class RouterLoopLogicTest(unittest.TestCase):
    """Test the class and functions in the module."""

    def setUp(self) -> None:
        self.executor = concurrent.futures.ThreadPoolExecutor()

    def tearDown(self) -> None:
        self.executor.shutdown(wait=True)

    def test_get_categories(self) -> None:
        """Test get_categories"""
        router = EventRouter(threading.Semaphore(), None, self.executor)
        launcher = create_internal_launcher()
        loop = router_loop.RouterLoopLogic({'internal': launcher}, router)
        self.assertEqual((launcher,), loop.get_categories())

    def test_get_router(self) -> None:
        """Test get_router"""
        router = EventRouter(threading.Semaphore(), None, self.executor)
        loop = router_loop.RouterLoopLogic({}, router)
        self.assertIs(router, loop.get_router())

    def test_simple_handler(self) -> None:
        """Test the simple event handler."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        loop = router_loop.RouterLoopLogic({}, router)

        self.assertEqual(
            router_loop.SOFT_STOP_LOOP_ACTION,
            loop.handle_request(router_loop.SOFT_STOP_REQUEST),
        )
        self.assertEqual(
            router_loop.HARD_STOP_LOOP_ACTION,
            loop.handle_request(router_loop.HARD_STOP_REQUEST),
        )
        self.assertEqual(
            router_loop.RESTART_LOOP_ACTION,
            loop.handle_request(router_loop.RESTART_REQUEST),
        )
        router.assert_not_called()

    def test_start_extension__not_registered(self) -> None:
        """Test the simple event handler."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        router.configure_mock(**{
            'inject_event.return_value': RET_OK_NONE,
        })
        loop = router_loop.RouterLoopLogic({}, router)
        res = loop.handle_request(router_loop.ExtensionQueueRequest(
            's1', foreman.LauncherStartExtensionRequestEvent(
                'ext1', [1, 2, 3], [], 'not-registered', foreman.SendEventAccess([], []), None, [],
            ),
        ))
        self.assertEqual(res, router_loop.NONE_LOOP_ACTION)
        router.inject_event.assert_called()

    def test_start_extension__not_registered__send_errors(self) -> None:
        """Test the simple event handler."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        router.configure_mock(**{
            'inject_event.return_value': StdRet.pass_errmsg('x', i18n('f')),
        })
        loop = router_loop.RouterLoopLogic({}, router)
        res = loop.handle_request(router_loop.ExtensionQueueRequest(
            's1', foreman.LauncherStartExtensionRequestEvent(
                'ext1', [1, 2, 3], [], 'not-registered', foreman.SendEventAccess([], []), None, [],
            ),
        ))
        self.assertEqual(res, router_loop.NONE_LOOP_ACTION)
        router.inject_event.assert_called()

    def test_start_boot_extension__not_registered(self) -> None:
        """Test the simple event handler."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        router.configure_mock(**{
            'inject_event.return_value': RET_OK_NONE,
        })
        loop = router_loop.RouterLoopLogic({}, router)
        res = loop.handle_request(router_loop.BootExtensionQueueRequest(
            BootExtensionMetadata(
                'ext1', (1, 2, 3), 'not-registered', [], [], [], {}, {}, [],
            ),
        ))
        self.assertEqual(res, router_loop.NONE_LOOP_ACTION)
        router.inject_event.assert_not_called()

    def test_add_event_listeners(self) -> None:
        """Test the event handler with an add-event-listener event."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        router.configure_mock(**{
            'add_handler_listener.return_value': True,
        })
        loop = router_loop.RouterLoopLogic({}, router)
        res = loop.handle_request(router_loop.AddEventListenersQueueRequest(
            's1', foreman.ExtensionAddEventListenerEvent(
                [foreman.EventTarget('e1', 't1')],
            ),
        ))
        self.assertEqual(res, router_loop.NONE_LOOP_ACTION)
        router.add_handler_listener.assert_called()

    def test_remove_event_listeners(self) -> None:
        """Test the event handler with an remove-event-listener event."""
        router = unittest.mock.Mock(EventRouter(threading.Semaphore(), None, self.executor))
        router.configure_mock(**{
            'remove_handler_listener.return_value': True,
        })
        loop = router_loop.RouterLoopLogic({}, router)
        res = loop.handle_request(router_loop.RemoveEventListenersQueueRequest(
            's1', foreman.ExtensionRemoveEventListenerEvent(
                [foreman.EventTarget('e1', 't1')],
            ),
        ))
        self.assertEqual(res, router_loop.NONE_LOOP_ACTION)
        router.remove_handler_listener.assert_called()
