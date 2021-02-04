"""Test the module."""

import unittest
import os
import tempfile
import shutil
import json
from .. import reader, platform


class ReaderFuncsTest(unittest.TestCase):
    """Tests the reader functions"""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self._orig_config_path = list(platform.configuration_paths)
        platform.configuration_paths = [self.tempdir]

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)
        platform.configuration_paths = self._orig_config_path

    def test_reader__no_file(self) -> None:
        """Test the reader with no config file."""
        res = reader.read_configuration_file(None)
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
        res = reader.read_configuration_file(config_file)
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
        res = reader.read_configuration_file(config_file)
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
        res = reader.read_configuration_file(config_file)
        self.assertTrue(res.has_error)
        messages = ';'.join([msg.debug() for msg in res.valid_error.messages()])
        self.assertTrue(
            messages.startswith(
                'No boot-file-order defined in the foreman configuration, so foreman cannot start.',
            ),
            messages,
        )

    def test_reader__valid(self) -> None:
        """Test with a config file that does not define a boot order."""
        config_file = os.path.join(self.tempdir, 'conf.ini')
        with open(config_file, 'w') as f:
            f.write('[foreman]\nboot-file-order=a.yaml\n[loader]\nrunner=x')
        res = reader.read_configuration_file(config_file)
        self.assertIsNone(res.error)
        config = res.result
        self.assertEqual(
            ('a.yaml',),
            config.get_boot_config().boot_file_order,
        )

    def test_read_boot_extension_file__error_reading(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_res = reader.read_boot_extension_file(os.path.join(self.tempdir, 'does-not-exist'))
        self.assertIsNotNone(ext_res.error)

    def test_read_boot_extension_file__unexpected_format(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump({
                'name': [1],
                'runtime': {'launcher': 1, 'permissions': []},
                'produces': [1, 2, 3],
                'source-prefixes': ['sss:'],
                'consumes': 3,
                'configuration': 'yes',
            }, f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNotNone(ext_res.error)
        self.assertEqual(6, len(ext_res.error_messages()))

    def test_read_boot_extension_file__bad_doc_count(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump([1, 2], f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNotNone(ext_res.error)
        self.assertEqual(1, len(ext_res.error_messages()))

    def test_read_boot_extension_file__unexpected_consumes_list__item_type(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump({
                'name': 'n1',
                'version': [1, 2, 3],
                'runtime': {'launcher': 'l', 'permissions': {}},
                'produces': [],
                'source-prefixes': ['ssss:'],
                'consumes': [1],
                'configuration': {},
            }, f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNotNone(ext_res.error)
        self.assertEqual(1, len(ext_res.error_messages()))

    def test_read_boot_extension_file__unexpected_consumes_list__bad_event_id(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump({
                'name': 'n1',
                'version': [1, 2, 3],
                'runtime': {'launcher': 'l', 'permissions': {}},
                'produces': [],
                'consumes': [{'event-id': 1}],
                'source-prefixes': ['st:'],
                'configuration': {},
            }, f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNotNone(ext_res.error)
        self.assertEqual(1, len(ext_res.error_messages()))

    def test_read_boot_extension_file__unexpected_consumes_list__bad_target_id(self) -> None:
        """Test read_boot_extension_file but reading fails."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump({
                'name': 'n1',
                'version': [1, 2, 3],
                'runtime': {'launcher': 'l', 'permissions': {}},
                'produces': [],
                'source-prefixes': ['s1:'],
                'consumes': [{'target-id': 1}],
                'configuration': {},
            }, f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNotNone(ext_res.error)
        self.assertEqual(1, len(ext_res.error_messages()))

    def test_read_boot_extension_file__valid(self) -> None:
        """Test read_boot_extension_file with valid input."""
        ext_file = os.path.join(self.tempdir, 'invalid-format.json')
        with open(ext_file, 'w') as f:
            json.dump([{
                'name': 'n1',
                'version': [1, 2, 3],
                'runtime': {'launcher': 'l', 'permissions': {}},
                'produces': ['e1'],
                'source-prefixes': ['s:'],
                'consumes': [
                    {'target-id': 't1'}, {'event-id': 'e1'}, {},
                    {'target-id': 't2', 'event-id': 'e2'},
                ],
                'configuration': {},
            }], f)
        ext_res = reader.read_boot_extension_file(ext_file)
        self.assertIsNone(ext_res.error)
        ext = ext_res.result
        self.assertEqual(
            {(None, 't1'), ('e1', None), (None, None), ('e2', 't2')},
            set(ext.consumes),
        )
        evt = ext.to_start_event()
        self.assertEqual('n1', evt.name)
        self.assertEqual([1, 2, 3], evt.version)
        self.assertEqual(['e1'], evt.send_access.event_ids)
        self.assertEqual(['s:'], evt.send_access.source_id_prefixes)
        self.assertEqual('{}', evt.configuration)
