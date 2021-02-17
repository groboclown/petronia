"""Test the module."""

from typing import Tuple, Sequence, List
import unittest
from .. import message_loop
from ..arch.native_funcs import (
    WINDOWS_FUNCTIONS,
    SHELL__CANCEL_CALLBACK_CHAIN
)


class WindowsMessageLoopTest(unittest.TestCase):
    """Test the WindowsMessageLoop class."""

    def setUp(self) -> None:
        self._orig_inject = WINDOWS_FUNCTIONS.shell.inject_scancode

    def tearDown(self) -> None:
        WINDOWS_FUNCTIONS.shell.inject_scancode = self._orig_inject

    def test_dispose_not_running(self) -> None:
        """Test the dispose when the thread is not running or initialized."""
        loop = message_loop.WindowsMessageLoop()
        self.assertFalse(loop.is_running())
        loop.dispose(2.0)
        self.assertFalse(loop.is_running())

    def test_key_handler_inject_no_function(self) -> None:
        """Test the key handler callback."""
        WINDOWS_FUNCTIONS.shell.inject_scancode = None

        key_called: List[int] = []

        def key_callback(
                vk_code: int,
                _scan_code: int,
                _is_key_up: bool,
                _is_key_injected: bool
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
                _is_key_injected: bool
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
