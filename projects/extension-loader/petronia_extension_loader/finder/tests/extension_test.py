"""Tests for the module"""

import unittest
import os
import tempfile
import shutil
import json
from .. import extension


class ExtensionTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_find_extension_dirs__no_dirs(self) -> None:
        """Test find_extension_dirs"""
        res = extension.find_extension_dirs('')
        self.assertEqual((), tuple(res))

    def test_find_extension_dirs__many_paths__some_dont_exist(self) -> None:
        """Test find_extension_dirs"""
        ed1_base = os.path.join(self.tempdir, 'exists-1')
        ed1 = os.path.join(ed1_base, 'extensions')
        os.makedirs(ed1)
        ed2_base = os.path.join(self.tempdir, 'exists-2')
        ed2 = os.path.join(ed2_base, 'plugins')
        os.makedirs(ed2)
        ed3 = os.path.join(ed2_base, 'plug-ins')
        os.makedirs(ed3)
        not_ed4 = os.path.join(self.tempdir, 'does-not-exist')

        res = extension.find_extension_dirs(os.pathsep.join([
            ed1_base, ed2_base, not_ed4,
        ]))
        self.assertEqual({ed1, ed2, ed3}, set(res))

    def test_find_installed_extensions__no_dirs(self) -> None:
        """Test find_installed_extensions"""
        res = extension.find_installed_extensions([])
        self.assertEqual(([], {}), res)

    def test_find_installed_extensions__dirs_no_extensions(self) -> None:
        """Test find_installed_extensions"""
        with open(os.path.join(self.tempdir, 'some-file'), 'w') as f:
            f.write('x')
        dr2 = os.path.join(self.tempdir, 'exists-dir')
        os.makedirs(dr2)
        res = extension.find_installed_extensions([
            self.tempdir, dr2, os.path.join(self.tempdir, 'does-not-exist'),
        ])
        self.assertEqual(([], {}), res)

    def test_find_installed_extensions__zip(self) -> None:
        """Test find_installed_extensions"""
        zip_filename = os.path.join(self.tempdir, 'the-file-name-20.30.99.zip')
        with open(zip_filename, 'w') as f:
            f.write('x')
        extensions, errors = extension.find_installed_extensions([self.tempdir])
        self.assertEqual([], extensions)
        self.assertEqual({'the-file-name-20.30.99.zip'}, set(errors.keys()))
        self.assertEqual(
            [
                f'Errors found in extension defined in {zip_filename}',
                f'zip extension found ({zip_filename}) '
                f'but zip extension loading is not supported yet',
            ],
            [m.debug() for m in errors['the-file-name-20.30.99.zip']],
        )

    def test_find_installed_extensions__flat_valid_invalid(self) -> None:
        """Test find_installed_extensions with flat files that are both
        valid and invalid."""
        valid_flat_filename_1 = os.path.join(self.tempdir, 'valid1-extension.json')
        valid_flat_filename_2 = os.path.join(self.tempdir, 'valid2-extension.json')
        invalid_flat_filename_1 = os.path.join(self.tempdir, 'invalid1-extension.json')
        invalid_flat_filename_2 = os.path.join(self.tempdir, 'invalid2-extension.json')
        invalid_flat_filename_3 = os.path.join(self.tempdir, 'invalid3-extension.json')

        valid_config = {
            'name': 'my.extension',
            'type': 'api',
            'version': [1, 0, 0],
            'about': 'about1',
            'description': 'description1',
            'licenses': ['lic1'],
            'authors': ['auth1'],
            'default': {'name': 'm.e', 'minimum': [1, 0, 0]},
            'depends': [],
            'events': [],
        }

        with open(valid_flat_filename_1, 'w') as f:
            json.dump(valid_config, f)
        valid_config['name'] = 'my.other'
        with open(valid_flat_filename_2, 'w') as f:
            json.dump([valid_config], f)
        with open(invalid_flat_filename_1, 'w') as f:
            f.write('[')
        with open(invalid_flat_filename_2, 'w') as f:
            f.write('[]')
        with open(invalid_flat_filename_3, 'w') as f:
            f.write('{"name":"x"}')

        extensions, errors = extension.find_installed_extensions([self.tempdir])
        self.assertEqual(2, len(extensions))
        self.assertEqual({'my.extension', 'my.other'}, {extensions[0].name, extensions[1].name})
        self.assertEqual(
            {
                'invalid1-extension.json',
                'invalid2-extension.json',
                'invalid3-extension.json',
            },
            set(errors.keys()),
        )
