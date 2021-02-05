"""Test the module"""

import unittest
from petronia_common.util import RET_OK_NONE
from .. import internal
from ..abc import RuntimeContext
from ...events import foreman


class InternalLauncherCategoryTest(unittest.TestCase):
    """Test the module function and InternalLauncherCategory"""

    def test_inherited(self) -> None:
        """Test the inherited (not-overridden) methods."""
        cat = internal.create_internal_launcher()
        self.assertEqual('internal', cat.config.runner)
        self.assertEqual({}, cat.options)

    def test_is_valid(self) -> None:
        """Test the is_valid method."""
        cat = internal.create_internal_launcher()
        self.assertIs(RET_OK_NONE, cat.is_valid())

    def test_initialize(self) -> None:
        """Test the initialize method."""
        cat = internal.create_internal_launcher()
        context = RuntimeContext()
        self.assertIs(RET_OK_NONE, cat.initialize(context))

    def test_start_extension(self) -> None:
        """Test the start_extension method."""
        cat = internal.create_internal_launcher()
        self.assertIs(
            RET_OK_NONE,
            cat.start_extension(
                'h1',
                foreman.LauncherStartExtensionRequestEvent(
                    'n1', [1, 2, 3], [], 'r', foreman.SendEventAccess([], []), None, [],
                ),
            ),
        )

    def test_get_active_handler_ids(self) -> None:
        """Test the get_active_handler_ids method."""
        cat = internal.create_internal_launcher()
        self.assertEqual((), cat.get_active_handler_ids())

    def test_stop_extension(self) -> None:
        """Test the stop_extension method."""
        cat = internal.create_internal_launcher()
        self.assertIs(RET_OK_NONE, cat.stop_extension('h1'))

    def test_stop(self) -> None:
        """Test the stop method."""
        cat = internal.create_internal_launcher()
        self.assertIs(RET_OK_NONE, cat.stop())
