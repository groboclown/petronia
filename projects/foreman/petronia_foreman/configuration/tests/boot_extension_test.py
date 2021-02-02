"""Tests the module."""

import unittest
from .. import boot_extension
from ...events import foreman


class BootExtensionMetadataTest(unittest.TestCase):
    """Test the BootExtensionMetadata class."""

    def test_consumes(self) -> None:
        """Test the consumes property."""
        bed = boot_extension.BootExtensionMetadata(
            'n1', (2, 3, 1), 'r1', ('p1', 'p2'), ((None, None), ('c1a', 'c1b')),
            {'x': ['p1', 'p2']}, {'c1': []}, ['l1', 'l2'],
        )
        self.assertEqual(
            ((None, None), ('c1a', 'c1b')),
            bed.consumes,
        )

    def test_to_start_event(self) -> None:
        """Test the to_start_event function."""
        bed = boot_extension.BootExtensionMetadata(
            'n1', (2, 3, 1), 'r1', ('p1', 'p2'), ((None, None), ('c1a', 'c1b')),
            {'x': ['p1', 'p2']}, {'c1': []}, ['l1', 'l2'],
        )
        event = bed.to_start_event()
        self.assertEqual('n1', event.name)
        self.assertEqual([2, 3, 1], event.version)
        self.assertEqual(['l1', 'l2'], event.location)
        self.assertEqual('r1', event.runtime)
        self.assertEqual(['p1', 'p2'], event.send_access)
        self.assertEqual('{"c1": []}', event.configuration)
        self.assertEqual(
            repr([foreman.ExtensionPermission('x', ['p1', 'p2'])]),
            repr(event.permissions)
        )
