"""Test the module"""

import unittest
import io
import sys
from petronia_common.util import StdRet, i18n
from .. import user_messages


class PortalUserMessagesTest(unittest.TestCase):
    """Test the module functions."""

    def setUp(self) -> None:
        self._orig_stderr = sys.stderr

    def tearDown(self) -> None:
        if self._orig_stderr != sys.stderr:  # pragma no cover
            # proper cleanup.
            sys.stderr.close()
        sys.stderr = self._orig_stderr

    def test_report_send_receive_problems__no_error(self) -> None:
        """Test the report_send_receive_problems function"""
        sys.stderr = io.StringIO()
        user_messages.report_send_receive_problems(StdRet.pass_ok('x'))
        self.assertEqual('', sys.stderr.getvalue())

    def test_report_send_receive_problems__error_msg(self) -> None:
        """Test the report_send_receive_problems function"""
        sys.stderr = io.StringIO()
        user_messages.report_send_receive_problems(StdRet.pass_errmsg('c', i18n('m {x}'), x=1))
        self.assertEqual('[portal ERROR] m 1\n', sys.stderr.getvalue())

    def test_report_send_receive_problems__exception(self) -> None:
        """Test the report_send_receive_problems function"""
        try:
            raise ValueError()
        except ValueError as err:
            error = err
        sys.stderr = io.StringIO()
        user_messages.report_send_receive_problems(
            StdRet.pass_exception('c', i18n('m {x}'), error, x=1),
        )
        self.assertTrue(sys.stderr.getvalue().startswith('[portal ERROR] m 1\n'))
        self.assertTrue('ValueError' in sys.stderr.getvalue())
