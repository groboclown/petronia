"""Test the module"""

import unittest
import platform
from .. import funcs_win7
from ..supported_functions import Functions
from ..funcs_any_win import window__find_handles, window__get_process_id


def _is_not_supported() -> bool:
    if platform.system() != 'Windows':  # pragma no cover
        return True  # pragma no cover
    release = platform.release()  # pragma no cover
    return release.lower() not in (  # pragma no cover
        '7',
        '8', '8.1',
        '10',
    )


class FuncsWin7Test(unittest.TestCase):
    """Test the module functions."""

    def test_load_functions__win7(self) -> None:
        """Test the load_functions function when the env is win7"""
        func = Functions()
        self.assertIsNone(func.process.get_executable_filename)
        funcs_win7.load_functions({'system': 'windows', 'release': '7'}, func)
        self.assertIsNotNone(func.process.get_executable_filename)

    def test_load_functions__other(self) -> None:
        """Test the load_functions function when the env is not win7"""
        func = Functions()
        self.assertIsNone(func.process.get_executable_filename)
        funcs_win7.load_functions({'system': 'windows', 'release': '9'}, func)
        self.assertIsNone(func.process.get_executable_filename)

    @unittest.skipIf(_is_not_supported(), 'Not running at least Windows 7')
    def test_process__get_executable_filename(self) -> None:
        """Test getting the executable filename for a thread PID."""
        handles = list(window__find_handles())
        if not handles:  # pragma no cover
            print('Skipping test - no window handles.')  # pragma no cover
            return  # pragma no cover
        tpid = window__get_process_id(handles[0])  # pragma no cover
        filename = funcs_win7.process__get_executable_filename(tpid)  # pragma no cover
        self.assertIsNone(filename.error)
        print(filename.result)  # pragma no cover

    @unittest.skipIf(_is_not_supported(), 'Not running at least Windows 7')
    def test_process__get_all_pids(self) -> None:
        """Test process__get_all_pids"""
        pids = funcs_win7.process__get_all_pids()
        self.assertIsNone(pids.error)
        # There will always be at least 1 process.
        self.assertGreater(len(pids.result), 0)
