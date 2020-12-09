
"""Test the launch module."""

import unittest
import os
import sys
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from .. import launch
from ...configuration import detect_platform


class LaunchTest(unittest.TestCase):
    """Test the launch functions."""

    def setUp(self) -> None:
        self.platform = detect_platform(None)
        self.runner_cmd = (
            sys.executable + ' ' +
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'runner.py')) + ' ' +
            '${WRITE_FD} 4'
        )

    def test_runner(self) -> None:
        """Run the runner module..."""
        self.assertTrue(self.platform.ok)

        ret_code = [-1]

        def on_exit(code: int) -> None:
            print("Subprocess exited with", code)
            ret_code[0] = code

        ret_process = launch.run_launcher(
            'r1', ExtensionRuntime('runner', {}),
            self.runner_cmd, dict(os.environ), self.platform.result,
        )

        self.assertIsNone(ret_process.error)
        print("Tester: writing data to write stream.")
        ret_process.result.write(b'1234')
        # Without the close_writer, the process could wait forever.
        print("Tester: closing writer")
        ret_process.result.close_writer()
        print("Tester: reading too much data")
        print("Tester: watching process")
        ret_process.result.watch_process(on_exit)
        self.assertEqual(0, ret_code[0])
        result = ret_process.result.reader.read(100)
        self.assertEqual(b'1234', result)
