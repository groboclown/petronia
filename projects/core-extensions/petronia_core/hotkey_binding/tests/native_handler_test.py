"""Test the module"""

import unittest
from .. import native_handler
from ..events.ext import hotkey as native_hotkey


class NativeHandlerTest(unittest.TestCase):
    """Test the classes and functions in the module"""

    def test_error_to_user_message__empty(self) -> None:
        """Test the error_to_user_message function"""
        src = native_hotkey.Error('i', ['debug'], None, [])
        messages = native_handler.error_to_user_message(src)
        self.assertEqual([], messages)
