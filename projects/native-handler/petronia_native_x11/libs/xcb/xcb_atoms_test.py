"""Test the module."""

import unittest
import ctypes
from . import xcb_atoms, xcb_native


class XcbAtomsTest(unittest.TestCase):
    """Test the module and class."""
    def test_find_atoms(self) -> None:
        """Find the atoms."""
        lib = xcb_native.LibXcb()
        default_screen = ctypes.c_int(0)
        connection = lib.xcb_connect(xcb_native.NULL_c_char_p, ctypes.byref(default_screen))
        error_code = lib.xcb_connection_has_error(connection)
        self.assertEqual(0, error_code, msg="Failed to connect to xserver")
        atoms = xcb_atoms.initialize_atoms(lib, connection)

        # Ensure the manager atom was set and is a valid number.
        self.assertTrue(atoms.MANAGER != 0)
