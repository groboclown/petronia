"""Test the module."""

import unittest

from petronia_common.event_stream.tests.shared import create_read_stream, SimpleBinaryWriter
from .. import entrypoint


class DataStoreEntrypointTest(unittest.TestCase):
    """Test the entrypoint"""

    def test_entrypoint_ok(self) -> None:
        """Test the entrypoint function where everything is fine."""
        res = entrypoint.extension_entrypoint(
            create_read_stream(b''),
            SimpleBinaryWriter(),
            {}, [],
        )
        self.assertIsNone(res.error)
