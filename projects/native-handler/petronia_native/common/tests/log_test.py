"""Test the module."""

import unittest
import sys
import io
from .. import log


class LogTest(unittest.TestCase):
    """Test the module functions."""

    def setUp(self) -> None:
        self._orig_stdout = sys.stdout
        self._orig_info = log.LOG_INFO
        self._orig_debug = log.LOG_DEBUG
        self._orig_trace = log.LOG_TRACE
        self._outs = [io.StringIO()]

    def tearDown(self) -> None:
        # This protects against the "did not close io" error message.
        for out in self._outs:
            out.close()
        sys.stdout = self._orig_stdout
        log.LOG_INFO = self._orig_info
        log.LOG_DEBUG = self._orig_debug
        log.LOG_TRACE = self._orig_trace

    def test_low_print(self) -> None:
        """Test the low_print function."""
        sys.stdout = self._io()
        log.low_print('this is a message')
        self.assertEqual(
            'this is a message\n',
            sys.stdout.getvalue(),
        )

    def test_info(self) -> None:
        """Test the info function."""
        log.LOG_INFO = True
        sys.stdout = self._io()
        log.info('info {msg} {n}', msg='aaa', n=1234)
        self.assertEqual(
            '[Native  INFO] info aaa 1234\n',
            sys.stdout.getvalue(),
        )
        log.LOG_INFO = False
        sys.stdout = self._io()
        log.info('info {msg} {n}', msg='aaa', n=1234)
        self.assertEqual('', sys.stdout.getvalue())

    def test_debug(self) -> None:
        """Test the info function."""
        log.LOG_INFO = False
        log.LOG_DEBUG = True
        sys.stdout = self._io()
        log.debug('dbg {msg} {n}', msg='aaa', n=1234)
        self.assertEqual(
            '[Native DEBUG] dbg aaa 1234\n',
            sys.stdout.getvalue(),
        )
        log.LOG_DEBUG = False
        sys.stdout = self._io()
        log.debug('dbg {msg} {n}', msg='aaa', n=1234)
        self.assertEqual('', sys.stdout.getvalue())

    def test_trace(self) -> None:
        """Test the info function."""
        log.LOG_TRACE = True
        sys.stdout = self._io()
        log.trace('tt {msg} {n}', msg='aaa', n=1234)
        self.assertEqual(
            '[Native TRACE] tt aaa 1234\n',
            sys.stdout.getvalue(),
        )
        log.LOG_TRACE = False
        sys.stdout = self._io()
        log.trace('tt {msg} {n}', msg='aaa', n=1234)
        self.assertEqual('', sys.stdout.getvalue())

    def test_error(self) -> None:
        """Test the error function."""
        sys.stdout = self._io()
        log.error('err {msg} {n}', msg='aaa', n=1234)
        self.assertEqual(
            '[Native ERROR] err aaa 1234\n',
            sys.stdout.getvalue(),
        )

    def _io(self) -> io.StringIO:
        ret = io.StringIO()
        self._outs.append(ret)
        return ret
