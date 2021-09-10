"""Test the module."""

import unittest
import os
import sys
import tempfile
import shutil
from .. import formatted_data_reader


class FormattedDataReaderTest(unittest.TestCase):
    """Test the functions in the module."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_load_structured_file__not_found(self) -> None:
        """Test load_structured_file with the file not existing."""
        filename = os.path.join(self.tempdir, 'x.json')
        self.assertFalse(os.path.isfile(filename))
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)

    def test_load_structured_file__not_supported(self) -> None:
        """Test load_structured_file with a not-supported file type."""
        filename = os.path.join(self.tempdir, 'x.txt')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('abc')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)

    def test_load_structured_file__json(self) -> None:
        """Test test_load_structured_file with a simple json file."""
        filename = os.path.join(self.tempdir, 'x.json')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('{"x":"y"}')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNone(res.error)
        self.assertEqual(
            {'x': 'y'},
            res.value,
        )

    def test_load_structured_file__json_bad(self) -> None:
        """Test test_load_structured_file with an invalid json file."""
        filename = os.path.join(self.tempdir, 'x.json')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('"')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)

    def test_load_structured_file__yaml(self) -> None:
        """Test test_load_structured_file with a simple yaml file."""
        filename = os.path.join(self.tempdir, 'x.yaml')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('x: y')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNone(res.error)
        self.assertEqual(
            ({'x': 'y'},),
            res.value,
        )

    def test_load_structured_file__yaml_bad(self) -> None:
        """Test test_load_structured_file with an invalid yaml file."""
        filename = os.path.join(self.tempdir, 'x.yaml')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('{')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)

    @unittest.skipIf(sys.platform.startswith('win'), 'Not workable on Windows')
    def test_load_structured_file__yaml_not_readable(self) -> None:  # pragma no cover
        """Test test_load_structured_file with a simple yaml file.
        Can't do this with Windows, because the only thing that can be changed is
        the is-read-only flag."""
        filename = os.path.join(self.tempdir, 'x.yaml')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('x: y')
        os.chmod(filename, 0)
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)

    def test_load_structured_file__bad_data_type(self) -> None:
        """Test test_load_structured_file with a file containing a not-supported top-level type."""
        filename = os.path.join(self.tempdir, 'x.json')
        with open(filename, 'w', encoding='utf-8') as f_w:
            f_w.write('"abc"')
        res = formatted_data_reader.load_structured_file(filename)
        self.assertIsNotNone(res.error)
