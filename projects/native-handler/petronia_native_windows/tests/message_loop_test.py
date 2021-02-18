"""Test the module."""

from typing import Tuple, Sequence, List, cast
import unittest
import time

from petronia_common.util import not_none
from .. import message_loop
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
    SHELL__CANCEL_CALLBACK_CHAIN
)
from ..arch.native_funcs.windows_common import DWORD, HWND, LPARAM, WPARAM


class WindowsMessageLoopTest(unittest.TestCase):
    """Test the WindowsMessageLoop class."""

    def setUp(self) -> None:
        self._orig_inject = WINDOWS_FUNCTIONS.shell.inject_scancode
        self.running: List[message_loop.WindowsMessageLoop] = []

    def tearDown(self) -> None:
        WINDOWS_FUNCTIONS.shell.inject_scancode = self._orig_inject
        for loop in self.running:
            loop.dispose(2.0)

    def test_dispose_not_running(self) -> None:
        """Test the dispose when the thread is not running or initialized."""
        loop = message_loop.WindowsMessageLoop()
        self.assertFalse(loop.is_running())
        loop.dispose(2.0)
        self.assertFalse(loop.is_running())

    def test_key_handler_no_function(self) -> None:
        """Test the key handler callback."""
        WINDOWS_FUNCTIONS.shell.inject_scancode = None
        loop = message_loop.WindowsMessageLoop()
        res = loop.message_key_handler(2, 3, True, False)
        self.assertEqual(None, res)

    def test_key_handler_no_inject(self) -> None:
        """Test the key handler callback."""
        WINDOWS_FUNCTIONS.shell.inject_scancode = None

        key_called: List[int] = []

        def key_callback(
                vk_code: int,
                _scan_code: int,
                _is_key_up: bool,
                _is_key_injected: bool,
        ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
            key_called.append(vk_code)
            return True, [(1, False)]

        loop = message_loop.WindowsMessageLoop()
        loop.set_key_handler(key_callback)
        res = loop.message_key_handler(2, 3, True, False)
        self.assertEqual(SHELL__CANCEL_CALLBACK_CHAIN, res)
        self.assertEqual(
            [2],
            key_called,
        )

    def test_key_handler_inject_with_function(self) -> None:
        """Test the key handler callback."""
        inject_called: List[int] = []

        def inject(vk_code: int, _is_up: bool) -> bool:
            inject_called.append(vk_code)
            return False

        WINDOWS_FUNCTIONS.shell.inject_scancode = inject

        key_called: List[int] = []

        def key_callback(
                vk_code: int,
                _scan_code: int,
                _is_key_up: bool,
                _is_key_injected: bool,
        ) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
            key_called.append(vk_code)
            return False, [(1, False)]

        loop = message_loop.WindowsMessageLoop()
        loop.set_key_handler(key_callback)
        res = loop.message_key_handler(2, 3, True, False)
        self.assertIsNone(res)
        self.assertEqual(
            [2],
            key_called,
        )
        self.assertEqual(
            [1],
            inject_called,
        )

    def test_message_handler(self) -> None:
        """Call a message handler."""

        called: List[int] = []

        def callback(_hwnd: HWND, mid: int, _wparam: WPARAM, _lparam: LPARAM) -> bool:
            called.append(mid)
            return True

        loop = message_loop.WindowsMessageLoop()
        loop.add_message_handler((False, 1, callback))
        loop.add_message_handler((True, 2, callback))
        loop.message_shell_handler(cast(HWND, 1), 10, cast(WPARAM, 1), cast(LPARAM, 17))
        loop.message_shell_handler(cast(HWND, 1), 20, cast(WPARAM, 2), cast(LPARAM, 17))
        loop.message_shell_handler(cast(HWND, 1), 30, cast(WPARAM, 3), cast(LPARAM, 17))
        self.assertEqual([20], called)

    @unittest.skipIf(
        WINDOWS_FUNCTIONS.window.get_process_id is None, 'get_process_id not supported',
    )
    def test_thread(self) -> None:
        """Test the thread execution with an on-exit callback."""

        on_exit_called: List[bool] = []

        def on_exit() -> None:
            on_exit_called.append(True)

        loop = message_loop.WindowsMessageLoop()
        loop.set_on_exit_callback(on_exit)
        self.running.append(loop)
        loop.start()
        expires = time.time() + 2.0
        while not loop.is_running() and time.time() < expires:  # pragma no cover
            time.sleep(1.0)  # pragma no cover
        self.assertTrue(loop.is_running())
        self.assertIsNotNone(loop.hwnd)

        get_process_id = WINDOWS_FUNCTIONS.window.get_process_id
        assert get_process_id  # nosec  # mypy requirement
        windows_pid = get_process_id(not_none(loop.hwnd))
        self.assertIsInstance(windows_pid, DWORD)

        loop.dispose(2.0)
        expires = time.time() + 2.0
        while loop.is_alive() and time.time() < expires:  # pragma no cover
            time.sleep(1.0)  # pragma no cover
        self.assertFalse(loop.is_alive())
        self.assertIsNone(loop.hwnd)

        self.assertEqual([True], on_exit_called)

        # Just one more state thing to check.
        loop.start()
        self.assertFalse(loop.is_alive())
