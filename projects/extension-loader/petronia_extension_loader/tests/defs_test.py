"""Test the module"""

import unittest

from petronia_common.extension.config.extension_schema import ProtocolExtensionMetadata
from .. import defs


class ExtensionInfoTest(unittest.TestCase):
    """Test the ExtensionInfo class"""

    def test_getters(self) -> None:
        """Test the getter methods"""
        metadata = ProtocolExtensionMetadata(
            'ext-1', (5, 4, 3),
            'about-ext', 'desc-ext', ['lic-1'],
            ['auth-1'], [],
        )
        info = defs.ExtensionInfo(['a', 'b'], metadata)
        self.assertEqual('ext-1', info.name)
        self.assertIs(metadata, info.metadata)
        self.assertEqual(('a', 'b'), info.path)
        self.assertEqual((5, 4, 3), info.version)

    def test_requesters(self) -> None:
        """Test the requester functions"""
        info = defs.ExtensionInfo(['a', 'b'], ProtocolExtensionMetadata(
            'ext-1', (5, 4, 3),
            'about-ext', 'desc-ext', ['lic-1'],
            ['auth-1'], [],
        ))
        self.assertEqual((), info.request_source_ids)
        info.add_request_source_id('s1')
        self.assertEqual(('s1',), info.request_source_ids)
        info.add_request_source_id('s1')
        self.assertEqual(('s1',), info.request_source_ids)
        info.add_request_source_id('s2')
        self.assertEqual({'s1', 's2'}, set(info.request_source_ids))
