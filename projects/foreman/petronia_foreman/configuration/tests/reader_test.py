"""Test the module."""

import unittest
import os
import tempfile
import shutil
from .. import reader
from ..platform import detect_platform


class ReaderFuncsTest(unittest.TestCase):
    """Tests the reader functions"""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self.platform = detect_platform(None).result
        self.platform.config_paths = (self.tempdir,)

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def test_reader__no_file(self) -> None:
        """Test the reader with no config file."""
        res = reader.read_configuration_file(None, self.platform)
        self.assertTrue(res.has_error)
        messages = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertTrue(
            messages.startswith('Could not find configuration file "petronia.ini" in any of '),
            msg=messages,
        )

    def test_reader__bad_file(self) -> None:
        """Test with a bad config file."""
        config_file = os.path.join(self.tempdir, 'conf.ini')
        with open(config_file, 'w') as f:
            f.write('[bad] config\nfile\nvalue = # bad')
        res = reader.read_configuration_file(config_file, self.platform)
        self.assertTrue(res.has_error)
        messages = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertEqual(
            f'Error parsing ini file {config_file}: ["Line 2: \'file\\\\n\'"]',
            messages,
        )

    def test_reader__validation_error(self) -> None:
        """Test with a bad config file."""
        config_file = os.path.join(self.tempdir, 'conf.ini')
        with open(config_file, 'w') as f:
            f.write('[bad-loader]\n')
        res = reader.read_configuration_file(config_file, self.platform)
        self.assertTrue(res.has_error)
        messages = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertEqual(
            '`runner` not specified for launcher bad-loader',
            messages,
        )

    def test_reader__no_boot_order(self) -> None:
        """Test with a config file that does not define a boot order."""
        config_file = os.path.join(self.tempdir, 'conf.ini')
        with open(config_file, 'w') as f:
            f.write('[loader]\nrunner=x')
        res = reader.read_configuration_file(config_file, self.platform)
        self.assertTrue(res.has_error)
        messages = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertTrue(
            messages.startswith(
                'No boot-order defined in the foreman configuration, so foreman cannot start.',
            ),
            messages,
        )

    def test_reader__valid(self) -> None:
        """Test with a config file that does not define a boot order."""
        config_file = os.path.join(self.tempdir, 'conf.ini')
        with open(config_file, 'w') as f:
            f.write('[boot]\nboot-order=loader\n[loader]\nrunner=x')
        res = reader.read_configuration_file(config_file, self.platform)
        self.assertTrue(res.ok)
        config = res.result
        self.assertEqual(
            ('loader',),
            config.get_boot_config().boot_order,
        )
