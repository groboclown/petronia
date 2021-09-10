"""Test the module."""

from typing import List
import unittest
import os
import sys
import tempfile
import shutil
import json
from . import extension_entrypoint
from .. import main, setup


class ExtensionRunnerMainTest(unittest.TestCase):  # pylint:disable=too-many-instance-attributes
    """Test the main function"""
    open_fd: List[int]

    def setUp(self) -> None:
        self._orig_handler = setup.HANDLER_ID
        self._orig_config = list(setup.USER_CONFIG_PATH)
        self._orig_data = list(setup.DATA_PATH)
        self._orig_temp = setup.TEMP_DIR
        self._orig_ext_name = setup.EXTENSION_NAME
        self._orig_entry = setup.ENTRYPOINT_NAME
        self._orig_stdout = sys.stdout
        self._orig_stdin = sys.stdin
        self._orig_sys_path = list(sys.path)
        self.tempdir = tempfile.mkdtemp()
        self.open_fd = []

    def tearDown(self) -> None:
        # Close file descriptors before reassigning stdin/out
        for file_desc in self.open_fd:
            try:
                os.close(file_desc)
            except OSError:
                # ignore; it means something (correctly) closed the file descriptor.
                pass  # pragma no cover

        sys.stdout = self._orig_stdout
        sys.stdin = self._orig_stdin
        sys.path.clear()
        sys.path.extend(self._orig_sys_path)

        # Default TEMP_DIR is the current directory, so never remove that.
        if not os.path.samefile(setup.TEMP_DIR, os.curdir):
            shutil.rmtree(setup.TEMP_DIR, ignore_errors=True)  # pragma no cover
        shutil.rmtree(self.tempdir, ignore_errors=True)

        setup.HANDLER_ID = self._orig_handler
        setup.USER_CONFIG_PATH.clear()
        setup.USER_CONFIG_PATH.extend(self._orig_config)
        setup.DATA_PATH.clear()
        setup.DATA_PATH.extend(self._orig_data)
        setup.TEMP_DIR = self._orig_temp
        setup.EXTENSION_NAME = self._orig_ext_name
        setup.ENTRYPOINT_NAME = self._orig_entry

    def test_main__bad_fileno(self) -> None:
        """Test the main function."""
        res = main.main(['x'])
        self.assertEqual(res, 1)

    def test_main__ok(self) -> None:
        """Test the main function with a normal runtime."""
        config = {'a': 'x', 'b': 'y'}
        config_file = os.path.join(self.tempdir, 'config-file.json')
        with open(config_file, 'w', encoding='utf-8') as f_txt:
            json.dump(config, f_txt)

        input_file = os.path.join(self.tempdir, 'stdin.txt')
        with open(input_file, 'wb') as f_bin:
            f_bin.write(b'')  # yes, really.
        input_fd = os.open(input_file, os.O_RDONLY)
        self.open_fd.append(input_fd)
        output_file = os.path.join(self.tempdir, 'stdout.txt')
        with open(output_file, 'wb') as f_bin:
            f_bin.write(b'')  # yes, really
        output_fd = os.open(output_file, os.O_WRONLY)
        self.open_fd.append(output_fd)
        if sys.platform == "win32":
            # On Windows, the file handle is passed in, not the fd.
            import msvcrt  # type: ignore  # pylint: disable=import-outside-toplevel,import-error  # pragma no cover
            output_fd = msvcrt.get_osfhandle(output_fd)  # pragma no cover  # type: ignore
        extension_entrypoint.init()
        sys.stdin = os.fdopen(input_fd, 'r')
        res = main.main(
            [
                str(output_fd),  # output write handle
                'h1',   # handler
                'cp1',  # user config path
                'dp1',  # data path
                self.tempdir,
                'petronia_extension_runner.tests.extension_entrypoint',  # extension name
                config_file,
                'a', 'b',
            ]
        )
        self.assertIs(0, res)
        self.assertEqual([['a', 'b']], extension_entrypoint.CALLED_ARGS)
        self.assertEqual([config], extension_entrypoint.CALLED_CONFIGS)
