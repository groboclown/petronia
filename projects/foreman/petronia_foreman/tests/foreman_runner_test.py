"""Tests the module."""

import unittest
import configparser
from .. import foreman_runner
from ..configuration import ForemanConfig, platform
from ..configuration.foreman import BOOT_SECTION


class ForemanRunnerTest(unittest.TestCase):
    """Test the ForemanRunner class."""

    def test_initialize(self) -> None:
        """Test the initialize method."""
        platform_res = platform.initial_setup(None)
        self.assertIsNone(platform_res.error)
        conf = configparser.ConfigParser()
        conf.add_section(BOOT_SECTION)
        foreman_config = ForemanConfig()
        res = foreman_config.load_config(conf)
        self.assertIsNone(res.error)
        runner = foreman_runner.ForemanRunner(foreman_config)
        ret = runner.initialize()
        self.assertEqual(0, ret)
