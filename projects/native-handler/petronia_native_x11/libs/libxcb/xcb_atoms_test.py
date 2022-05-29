"""Test the module."""

import unittest
import ctypes
from . import xcb_atoms, xcb


class XcbAtomsTest(unittest.TestCase):
    """Test the module and class."""
    def test_find_atoms(self) -> None:
        """Find the atoms."""
        try:
            lib = xcb_native.LibXcb()
        except OSError:
            print("Skipping test - libraries not supported.")
            return
        default_screen = ctypes.c_int(0)
        connection = lib.xcb_connect(xcb_native.NULL_c_char_p, ctypes.byref(default_screen))
        error_code = lib.xcb_connection_has_error(connection)
        self.assertEqual(0, error_code, msg="Failed to connect to xserver")
        atoms_res = xcb_atoms.initialize_atoms(lib, connection)
        self.assertEqual((), atoms_res.error_messages())

        # Ensure the manager atom was set and is a valid number.
        self.assertTrue(atoms_res.result.MANAGER != 0)
