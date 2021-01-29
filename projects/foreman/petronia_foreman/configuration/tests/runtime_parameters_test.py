"""
Test the module.
"""

from typing import Dict
import unittest
from .. import runtime_parameters


class LauncherParametersTest(unittest.TestCase):
    """Test out the parameters."""

    def test_get_stop_timeout__default(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {}
        self.assertEqual(
            runtime_parameters.STOP_TIMEOUT_DEFAULT,
            runtime_parameters.get_stop_timeout(options),
        )

    def test_get_stop_timeout__invalid_float(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {
            runtime_parameters.STOP_TIMEOUT_OPTION: 'abc',
        }
        self.assertEqual(
            runtime_parameters.STOP_TIMEOUT_DEFAULT,
            runtime_parameters.get_stop_timeout(options),
        )

    def test_get_stop_timeout__valid_float(self) -> None:
        """Test get_stop_timeout with no value set."""
        options: Dict[str, str] = {
            runtime_parameters.STOP_TIMEOUT_OPTION: '1.2',
        }
        self.assertEqual(
            1.2,
            runtime_parameters.get_stop_timeout(options),
        )
