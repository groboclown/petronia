"""Test the module."""

import unittest
from petronia_common.util import UserMessage, i18n
from petronia_common.util.error import SimplePetroniaReturnError
from .. import user_message


class UserMessageTest(unittest.TestCase):
    """Test the functions."""

    def test_display(self) -> None:
        """Test the display function."""
        user_message.display(i18n('test-message'))
        self.assertIsNone(None)

    def test_display_error__0(self) -> None:
        """Test the display_error function."""
        user_message.display_error(SimplePetroniaReturnError())
        self.assertIsNone(None)

    def test_display_error__2(self) -> None:
        """Test the display_error function."""
        user_message.display_error(SimplePetroniaReturnError(
            UserMessage('cat', i18n('my-message1')),
            UserMessage('cat', i18n('my-message2')),
        ))
        self.assertIsNone(None)

    def test_translate(self) -> None:
        """Test the translate function."""
        res = user_message.translate(i18n('message'))
        self.assertEqual('message', res)
