
"""Test the launch module."""

import unittest
import os
import sys
import asyncio
import configparser
from petronia_common.extension.config.extension_schema import ExtensionRuntime
from .. import launch
from ...configuration import ForemanConfig, detect_platform


class LaunchTest(unittest.TestCase):
    """Test the launch functions."""

    def setUp(self) -> None:
        self.platform = detect_platform(None)
        self.foreman_config = ForemanConfig()
        config = configparser.ConfigParser()
        config.add_section('runner')
        config.set(
            'runner', 'command',
            sys.executable + ' ' +
            os.path.abspath(os.path.join(os.path.dirname(__file__), 'runner.py')) + ' ' +
            '${WRITE_FD}',
        )
        self.foreman_config.load_config(config)

    def test_runner(self) -> None:
        """Run the runner module..."""
        self.assertTrue(self.platform.ok)

        ret_code = [-1]

        def on_exit(code: int) -> None:
            print("Subprocess exited with", code)
            ret_code[0] = code

        async def run_test() -> None:
            ret_process = await launch.run_launcher(
                'r1', ExtensionRuntime('runner', {}),
                self.foreman_config, self.platform.result,
            )
            self.assertIsNone(ret_process.error)
            print("Tester: writing data to write stream.")
            ret_process.result.writer.write(b'1234')
            for coroutine in ret_process.result.get_watchers(on_exit):
                print("Tester: waiting on " + repr(coroutine))
                await coroutine
            result = await ret_process.result.reader.read(100)
            self.assertEqual(b'1234', result)

        self.platform.result.setup_asyncio()
        asyncio.run(run_test())
