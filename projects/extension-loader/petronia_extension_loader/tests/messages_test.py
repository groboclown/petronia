"""Test the module."""

import unittest
import sys
import io
from petronia_common.util import StdRet, UserMessage, i18n
from petronia_common.util.error import SimplePetroniaReturnError
from .. import messages


class ExtensionLoaderMessagesTest(unittest.TestCase):
    """Test the functions in the messages module."""

    def setUp(self) -> None:
        self._orig_stdout = sys.stdout

    def tearDown(self) -> None:
        sys.stdout = self._orig_stdout

    def test_low_println(self) -> None:
        """Test low_println"""
        sys.stdout = io.StringIO()
        messages.low_println('my text')
        self.assertEqual('my text\n', sys.stdout.getvalue())

    def test_display_message__no_messages(self) -> None:
        """Test display_message"""
        sys.stdout = io.StringIO()
        messages.display_message(StdRet.pass_error(SimplePetroniaReturnError()))
        self.assertEqual('', sys.stdout.getvalue())

    def test_display_message__messages(self) -> None:
        """Test display_message"""
        sys.stdout = io.StringIO()
        messages.display_message(
            StdRet.pass_error(SimplePetroniaReturnError(UserMessage('c', i18n('m1')))),
            'm2',
        )
        self.assertEqual('m2\nm1\n', sys.stdout.getvalue())

    def test_display_message__error(self) -> None:
        """Test display_message"""
        sys.stdout = io.StringIO()
        try:
            raise IOError('my err')
        except IOError as ioe:
            err = ioe
        messages.display_message(StdRet.pass_exception(i18n('s1s'), err))
        self.assertTrue('s1s' in sys.stdout.getvalue())
        self.assertTrue('my err' in sys.stdout.getvalue())
        self.assertTrue('IOError' in sys.stdout.getvalue())
