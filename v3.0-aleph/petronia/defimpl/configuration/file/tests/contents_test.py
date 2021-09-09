
"""
Tests for deserializing the data
"""

import unittest
from collections.abc import Iterable
from ..contents import (
    deserialize_contents,
    ExtensionConfigurationDetails,
)


class DeserializeContentsTest(unittest.TestCase):

    def test_not_dict(self) -> None:
        self.maxDiff = None
        res = deserialize_contents('x', 'x.txt')

        self.assertIsInstance(res, Iterable)
        self.assertEqual(len(res), 1)
        self.assertIsInstance(res[0], ExtensionConfigurationDetails)
        self.assertEqual(res[0].source_name, 'x.txt')
        self.assertEqual(res[0].name, '')
        err = res[0].err
        self.assertIsNotNone(err)
        assert err is not None  # for mypy
        self.assertEqual(
            err.message,
            'Contents must be either a key-value map to configuration values, or a list of configuration values'
        )
        self.assertEqual(res[0].extension_name, None)
        self.assertEqual(res[0].state_id, None)
        self.assertEqual(res[0].state, None)
        self.assertEqual(res[0].is_enabled, False)

    def test_single_dict_ext(self) -> None:
        self.maxDiff = None
        res = deserialize_contents({
            "Top": {
                "ext": "a.1",
                "enabled": False,
                "properties": {}
            }
        }, 'y.txt')

        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].source_name, 'y.txt')
        self.assertEqual(res[0].name, 'Top')
        self.assertEqual(res[0].extension_name, 'a.1')
        self.assertEqual(res[0].is_enabled, False)
        self.assertEqual(res[0].state_id, 'a.1/setup-configuration')
        self.assertEqual(res[0].state, {})

    def test_single_list_ext(self) -> None:
        self.maxDiff = None
        res = deserialize_contents([{
            "Top": {
                "ext": "a.1",
                "enabled": False,
                "properties": {}
            }
        }], 'y.txt')

        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].source_name, 'y.txt')
        self.assertEqual(res[0].name, 'Top')
        self.assertEqual(res[0].extension_name, 'a.1')
        self.assertEqual(res[0].is_enabled, False)
        self.assertEqual(res[0].state_id, 'a.1/setup-configuration')
        self.assertEqual(res[0].state, {})
