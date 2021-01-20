"""
Test the module.
"""

from typing import Dict
import unittest
from .. import launcher_parameters


class LauncherParametersTest(unittest.TestCase):
    """Test out the parameters."""

    def test_get_boot_launcher_produces__not_boot(self) -> None:
        """Test get_boot_launcher_produces with a non-boot launcher."""
        options: Dict[str, str] = {}
        self.assertEqual(
            (),
            launcher_parameters.get_boot_launcher_produces(options),
        )

    def test_get_boot_launcher_produces__is_boot(self) -> None:
        """Test get_boot_launcher_produces with a non-boot launcher."""
        options: Dict[str, str] = {
            launcher_parameters.IS_BOOT_LAUNCHER_OPTION: launcher_parameters.IS_BOOT_LAUNCHER_VALUE,
            launcher_parameters.BOOT_PRODUCES_EVENTS_OPTION_PREFIX + '1': 'a1',
            launcher_parameters.BOOT_PRODUCES_EVENTS_OPTION_PREFIX + '2': 'b2',
            # Skip 3, to make 4 not parsed.
            launcher_parameters.BOOT_PRODUCES_EVENTS_OPTION_PREFIX + '4': 'd4',
        }
        # Use a set, because the returned value is unordered.
        self.assertEqual(
            {'a1', 'b2'},
            set(launcher_parameters.get_boot_launcher_produces(options)),
        )

    def test_get_stop_timeout__default(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {}
        self.assertEqual(
            launcher_parameters.STOP_TIMEOUT_DEFAULT,
            launcher_parameters.get_stop_timeout(options),
        )

    def test_get_stop_timeout__invalid_float(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {
            launcher_parameters.STOP_TIMEOUT_OPTION: 'abc',
        }
        self.assertEqual(
            launcher_parameters.STOP_TIMEOUT_DEFAULT,
            launcher_parameters.get_stop_timeout(options),
        )

    def test_get_stop_timeout__valid_float(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {
            launcher_parameters.STOP_TIMEOUT_OPTION: '1.2',
        }
        self.assertEqual(
            1.2,
            launcher_parameters.get_stop_timeout(options),
        )
