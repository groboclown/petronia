"""Test the module"""

import unittest

from petronia_common.event_stream.tests.shared import SimpleBinaryWriter, create_read_stream
from .. import entrypoint


class TimerEntrypointTest(unittest.TestCase):
    """Test the module functions"""

    def test_it(self) -> None:
        """Run it."""
        res = entrypoint.extension_entrypoint(
            create_read_stream(b''), SimpleBinaryWriter(), {}, [],
        )
        self.assertIsNone(res.error)
