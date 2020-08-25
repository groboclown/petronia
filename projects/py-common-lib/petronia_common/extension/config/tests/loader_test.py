
"""
Tests out the extension and event loader modules.
"""

# This has a lot of lines in it, because there's a lot of ways to test it.
# pylint: disable=C0302

from typing import List, Sequence, Tuple, Dict, Any
import unittest
from .. import extension_schema
from .. import event_schema
from .. import extension_loader
from ....util import UserMessage, i18n


class ExtensionLoaderTest(unittest.TestCase):
    """Runs the extension loader, and by implication the event loader,
    through data-driven tests."""
    def test_bad_data(self) -> None:
        """Data driven tests with validation problems"""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in BAD_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.load_extension(test_data)
                self.assertFalse(res.ok)
                expected = [
                    UserMessage(i18n(m), **a)
                    for m, a in messages
                ]
                actual = list(res.valid_error.messages())
                self.assertEqual(expected, actual)

    def test_good_data(self) -> None:
        """Data driven tests with valid data, generating extensions"""
        self.maxDiff = None
        for test_name, test_data, expected in GOOD_DATA_TESTS:
            with self.subTest(name=test_name):
                res = extension_loader.load_extension(test_data)
                self.assertIsNone(res.error)
                self.assertTrue(res.ok)
                self.assertEqual(repr(expected), repr(res.result))


BAD_DATA_TESTS: List[Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]]] = [
    (
        'Empty',
        {},
        [(
            'invalid extension type ({extension_type})',
            dict(extension_type=None),
        )],
    ),
    (
        'Bad Name Format',
        {
            'type': 'api', 'name': "bad-api", "version": [1, 0, 5], "about": "s",
            "description": "t", "depends": [], "licenses": [], "authors": [], "events": {},
        },
        [(
            'extension name ({name}) must conform to the pattern [a-z0-9][a-z0-9._]',
            dict(name='bad-api'),
        )],
    ),
    (
        'Bad Name Length',
        {
            'type': 'api', 'name': "x" * 256, "version": [1, 0, 5], "about": "s",
            "description": "t", "depends": [], "licenses": [], "authors": [], "events": {},
        },
        [(
            'extension name ({name}) must be {MIN_EXTENSION_NAME_LENGTH} to '
            '{MAX_EXTENSION_NAME_LENGTH} long',
            dict(name='x' * 256, MIN_EXTENSION_NAME_LENGTH=2, MAX_EXTENSION_NAME_LENGTH=255),
        )],
    ),
    (
        'Bad Version Format - negative',
        {
            'type': 'api', 'name': "bad.version", "version": [-1, 0, 5], "about": "s",
            "description": "t", "depends": [], "licenses": [], "authors": [], "events": {},
        },
        [(
            'version {{version}} must contain only non-negative integers',
            dict(version=[-1, 0, 5]),
        )],
    ),
    (
        'Bad Version Format - incorrect number of values',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1],
            "about": "s", "description": "t",
            "depends": [], "licenses": [], "authors": [], "events": {},
            "runtime": {'launcher': 'core'},
        },
        [(
            'version ({version}) must be in the format [major, minor, patch]',
            dict(version=[1]),
        )],
    ),
    (
        'Bad Version Format - incorrect value type (0)',
        {
            'type': 'standalone', 'name': "bad.version", "version": [None, 0, 0],
            "about": "s", "description": "t",
            "depends": [], "licenses": [], "authors": [], "events": {},
            "runtime": {'launcher': 'core'},
        },
        [(
            'version ({version}) must be in the format [major, minor, patch]',
            dict(version=[None, 0, 0]),
        )],
    ),
    (
        'Bad Version Format - incorrect value type (1)',
        {
            'type': 'impl', 'name': "bad.version", "version": [5, None, 0],
            "about": "s", "description": "t",
            "depends": [], "licenses": [], "authors": [], "events": {}, "implements": [],
            "runtime": {'launcher': 'core'},
        },
        [(
            'version ({version}) must be in the format [major, minor, patch]',
            dict(version=[5, None, 0]),
        )],
    ),
    (
        'Missing about, invalid description',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "description": 1,
            "depends": [], "licenses": [], "authors": [], "events": {},
            "runtime": {'launcher': 'core'},
        },
        [(
            'no `{key}` found in definition',
            dict(key='about'),
        ), (
            '`{key}` must be a string value',
            dict(key='description'),
        )],
    ),
    (
        'Missing licenses, bad authors list',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t",
            "depends": [], "authors": 1, "events": {},
            "runtime": {'launcher': 'core'},
        },
        [(
            '`{key}` must be a list of strings',
            dict(key='licenses'),
        ), (
            '`{key}` must be a list of strings',
            dict(key='authors'),
        )],
    ),
    (
        'Bad authors contents',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [],
            "depends": [], "authors": ['x', 1, 'b'], "events": {},
            "runtime": {'launcher': 'core'},
        },
        [(
            '`{key}` must be a list of strings',
            dict(key='authors'),
        )],
    ),
    (
        'Bad dependency value type',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": 1,
            "runtime": {'launcher': 'core'},
        },
        [(
            '`{key}` must be a list of dictionaries',
            dict(key='depends'),
        )],
    ),
    (
        'Bad dependency value item type',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [1],
            "runtime": {'launcher': 'core'},
        },
        [(
            'dependency must be a dictionary containing the keys '
            '`name`, `minimum`, and possibly `below`',
            {},
        )],
    ),
    (
        'Bad dependency value item - missing minimum',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [{"name": "x"}],
            "runtime": {'launcher': 'core'},
        },
        [(
            'version ({version}) must be in the format [major, minor, patch]',
            dict(version=None),
        )],
    ),
    (
        'Bad dependency value item - bad name',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [{"name": True}],
            "runtime": {'launcher': 'core'},
        },
        [(
            '`{key}` must be a string value', dict(key='name'),
        )],
    ),
    (
        'Bad dependency value item - bad below',
        {
            'type': 'standalone', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [{"name": "x", "minimum": [1, 0, 0], "below": 1}],
            "runtime": {'launcher': 'core'},
        },
        [(
            'version ({version}) must be in the format [major, minor, patch]',
            dict(version=1),
        )],
    ),
    (
        'Bad event type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": 1,
        },
        [('`events` must be a dictionary of event schemas', {})],
    ),
    (
        'Bad event value type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {"x": 1},
        },
        [('event schemas must be dictionaries', {})],
    ),
    (
        'Bad reference value type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {"x": {}}, "references": 1,
        },
        [('`references` must be a dictionary of event data type schemas', {})],
    ),
    (
        'Bad reference entry type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {"x": {}},
            "references": {"x": 1},
        },
        [('references must be a dictionary of event data type dictionaries', {})],
    ),
    (
        'Bad reference type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {"x": {}},
            "references": {"x": {"type": "blah"}},
        },
        [(
            'unknown data type `{data_type}`',
            dict(data_type='blah'),
        )],
    ),
    (
        'Cyclic reference',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {"x": {"fields": {"a": {"type": "reference", "ref": "y"}}}},
            "references": {
                "y": {"type": "reference", "ref": "z"},
                "z": {"type": "reference", "ref": "y"},
            },
        },
        [(
            'cyclic reference `{reference}`',
            dict(reference='z'),
        )],
    ),
    (
        'Event data - bad priority',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    "priority": "blah",
                    'send-access': 'public',
                    'receive-access': 'implementations',
                    'fields': {},
                },
            },
        },
        [(
            '`{priority}` must be a valid priority',
            dict(priority='blah'),
        )],
    ),
    (
        'Event data - missing priority and accesses',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    'fields': {},
                },
            },
        },
        [(
            'no `{key}` found in definition',
            dict(key='priority'),
        ), (
            'no `{key}` found in definition',
            dict(key='send-access'),
        ), (
            'no `{key}` found in definition',
            dict(key='receive-access'),
        )],
    ),
    (
        'Event data - priority, send-access, and receive-access data types',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    "priority": 1,
                    'send-access': True,
                    'receive-access': [1],
                    'fields': {},
                },
            },
        },
        [(
            '`{key}` must be a string value',
            dict(key='priority'),
        ), (
            '`{key}` must be a string value',
            dict(key='send-access'),
        ), (
            '`{key}` must be a string value',
            dict(key='receive-access'),
        )],
    ),
    (
        'Event data - bad receive-access',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    "priority": "io",
                    'send-access': "public",
                    'receive-access': "blah",
                    'fields': {},
                },
            },
        },
        [(
            '`{receive_access}` must be a valid access',
            dict(receive_access='blah'),
        )],
    ),
    (
        'Event data - bad send-access',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    "priority": "io",
                    'send-access': "x",
                    'receive-access': "public",
                    'fields': {},
                },
            },
        },
        [(
            '`{send_access}` must be a valid access',
            dict(send_access='x'),
        )],
    ),
    (
        'Event data - bad resolved reference',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [], "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "reference", "ref": "z"},
                    },
                },
            },
        },
        [(
            'unknown reference `{reference}`',
            dict(reference='z'),
        )],
    ),
    (
        'Event data - bad resolved array reference',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "array", "value-type": {"type": "reference", "ref": "z"}},
                    },
                },
            },
        },
        [(
            'unknown reference `{reference}`',
            dict(reference='z'),
        )],
    ),
    (
        'Event data - bad resolved structure reference',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {
                            "type": "structure",
                            "fields": {"x": {"type": "reference", "ref": "z"}},
                        },
                    },
                },
            },
        },
        [(
            'unknown reference `{reference}`',
            dict(reference='z'),
        )],
    ),
    (
        'Event data - bad resolved selector reference',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {
                            "type": "selector",
                            "type-mapping": {"x": {"type": "reference", "ref": "z"}},
                        },
                    },
                },
            },
        },
        [(
            'unknown reference `{reference}`',
            dict(reference='z'),
        )],
    ),
    (
        'Event data - bad string length types',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "string", "min-length": 'x', 'max-length': [1]},
                    },
                },
            },
        },
        [(
            '`{key}` must be a number',
            dict(key='max-length'),
        ), (
            '`{key}` must be a number',
            dict(key='min-length'),
        )],
    ),
    (
        'Event data - bad int value types',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "int", "min-value": 'x', 'max-value': [1]},
                    },
                },
            },
        },
        [(
            '`{key}` must be a number',
            dict(key='max-value'),
        ), (
            '`{key}` must be a number',
            dict(key='min-value'),
        )],
    ),
    (
        'Event data - bad float value types',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "float", "min-value": 'x', 'max-value': [1]},
                    },
                },
            },
        },
        [(
            '`{key}` must be a number',
            dict(key='max-value'),
        ), (
            '`{key}` must be a number',
            dict(key='min-value'),
        )],
    ),
    (
        'Event data - bad bool description',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "bool", "description": [1]},
                    },
                },
            },
        },
        [('`{key}` must be a string value', dict(key='description'),)],
    ),
    (
        'Event data - bad enum description',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "enum", "description": [1], "values": ["1"]},
                    },
                },
            },
        },
        [('`{key}` must be a string value', dict(key='description'),)],
    ),
    (
        'Event data - bad enum values type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "enum", "description": 'x', "values": True},
                    },
                },
            },
        },
        [('enum values must be a list of strings', {},)],
    ),
    (
        'Event data - bad enum value type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "enum", "description": 'x', "values": [1]},
                    },
                },
            },
        },
        [('enum values must be a list of strings', {},)],
    ),
    (
        'Event data - bad datetime description',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "datetime", "description": [1]},
                    },
                },
            },
        },
        [('`{key}` must be a string value', dict(key='description'),)],
    ),
    (
        'Event data - bad array value type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "array", "value-type": [1]},
                    },
                },
            },
        },
        [('`value-type` must be a dictionary of a data type structure', {},)],
    ),
    (
        'Event data - bad array value structure',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "array", "value-type": {"type": "foo"}},
                    },
                },
            },
        },
        [('unknown data type `{data_type}`', dict(data_type='foo'),)],
    ),
    (
        'Event data - bad structure description',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "structure", "description": [1], "fields": {}},
                    },
                },
            },
        },
        [('`{key}` must be a string value', dict(key='description'),)],
    ),
    (
        'Event data - bad structure fields type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "structure", "description": 'x', "fields": [1]},
                    },
                },
            },
        },
        [('`fields` must be a dictionary of field data type structures', {},)],
    ),
    (
        'Event data - bad structure optional type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "structure", "fields": {
                            "x": {"type": "bool", "optional": 1},
                        }},
                    },
                },
            },
        },
        [('`optional` must be `true` or `false`', {},)],
    ),
    (
        'Event data - bad selector description',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "selector", "description": [1], "type-mapping": {}},
                    },
                },
            },
        },
        [('`{key}` must be a string value', dict(key='description'),)],
    ),
    (
        'Event data - bad selector type-mapping type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "selector", "description": 'x', "type-mapping": [1]},
                    },
                },
            },
        },
        [('`type-mapping` must be a dictionary of data type structures', {},)],
    ),
    (
        'Event data - bad selector type-mapping entry type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "selector", "description": 'x', "type-mapping": {"x": [1]}},
                    },
                },
            },
        },
        [('`type-mapping` must be a dictionary of data type structures', {},)],
    ),
    (
        'Event data - bad selector type-mapping entry type value',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "selector", "description": 'x', "type-mapping": {
                            "x": {"type": "foo"},
                        }},
                    },
                },
            },
        },
        [('unknown data type `{data_type}`', dict(data_type='foo'),)],
    ),
    (
        'Event data - bad reference ref type',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {
                "x": {
                    "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                    'fields': {
                        "a": {"type": "reference", "description": [1], "ref": 1},
                    },
                },
            },
        },
        [
            ('`{key}` must be a string value', dict(key='description'),),
            ('`{key}` must be a string value', dict(key='ref'),),
        ],
    ),
    (
        'Reference depth',
        {
            'type': 'api', 'name': "bad.version", "version": [1, 0, 0],
            "about": "s", "description": "t", "licenses": [], "authors": [],
            "depends": [],
            "events": {"x": {
                "priority": "io", 'send-access': 'public', 'receive-access': 'public',
                'fields': {
                    "a": {
                        "type": "selector",
                        "type-mapping": {"x": {"type": "reference", "ref": "01"}},
                    },
                },
            }},
            "references": {
                "01": {"type": "reference", "ref": "02"},
                "02": {"type": "reference", "ref": "03"},
                "03": {"type": "reference", "ref": "04"},
                "04": {"type": "reference", "ref": "05"},
                "05": {"type": "reference", "ref": "06"},
                "06": {"type": "reference", "ref": "07"},
                "07": {"type": "reference", "ref": "08"},
                "08": {"type": "reference", "ref": "09"},
                "09": {"type": "reference", "ref": "10"},
                "10": {"type": "reference", "ref": "11"},
                "11": {"type": "reference", "ref": "12"},
                "12": {"type": "reference", "ref": "13"},
                "13": {"type": "reference", "ref": "14"},
                "14": {"type": "reference", "ref": "15"},
                "15": {"type": "reference", "ref": "16"},
                "16": {"type": "reference", "ref": "17"},
                "17": {"type": "reference", "ref": "18"},
                "18": {"type": "reference", "ref": "19"},
                "19": {"type": "reference", "ref": "20"},
                "20": {"type": "reference", "ref": "21"},
                "21": {"type": "reference", "ref": "22"},
                "22": {"type": "bool"},
            },
        },
        [(
            'reference depth too deep ({depth})',
            dict(depth=[
                '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                '15', '16', '17', '18', '19', '20', '21',
            ]),
        )],
    ),
]


GOOD_DATA_TESTS: List[Tuple[str, Dict[str, Any], extension_schema.AbcExtensionMetadata]] = [
    (
        'Simplest Api',
        {
            'type': 'api', 'name': "simplest.api", "version": [1, 0, 5],
            "about": "s", "description": "t", "licenses": [], "authors": [],
        },
        extension_schema.ApiExtensionMetadata(
            name="simplest.api", version=(1, 0, 5), about="s", description="t",
            depends=[], licenses=[], authors=[], events=[], default_implementation=None,
        ),
    ),
    (
        'Api With Events, Dependencies, and References',
        {
            'type': 'api', 'name': "api.with.events", "version": [2, 1, 5],
            "about": "s1", "description": "t1",
            "depends": [
                {
                    "name": "abc",
                    "minimum": [1, 2, 3],
                },
                {
                    "name": "def",
                    "minimum": [3, 5, 6],
                    "below": [6, 0, 0],
                },
            ], "licenses": [], "authors": [],
            "default": {"name": "axl", "minimum": [5, 4, 3], "below": [4, 4, 100]},
            "events": {
                "e1": {
                    'priority': 'io',
                    'send-access': 'public',
                    'receive-access': 'implementations',
                    'fields': {
                        'first': {
                            'optional': True,
                            'type': 'structure',
                            'fields': {
                                'f1': {
                                    'type': 'reference',
                                    'ref': 'x',
                                },
                                'f2': {
                                    'type': 'int',
                                },
                                'f3': {
                                    'type': 'string',
                                },
                                'f4': {
                                    'type': 'float',
                                    'min-value': -5.2,
                                    'optional': False,
                                },
                                'f5': {
                                    'type': 'array',
                                    'value-type': {'type': 'int', 'min-value': 5, 'max-value': 6},
                                },
                                'f6': {
                                    'type': 'enum',
                                    'values': ['a', 'b'],
                                },
                                'f7': {
                                    'type': 'datetime',
                                },
                                'f8': {
                                    'type': 'selector',
                                    'type-mapping': {
                                        'x': {'type': 'bool'},
                                        'y': {'type': 'reference', 'ref': 'y'},
                                    },
                                },
                                'f9': {
                                    'type': 'selector',
                                    'type-mapping': {
                                        'x': {'type': 'bool'},
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "references": {
                'x': {
                    'type': 'array',
                    'min-length': 1,
                    'max-length': 5,
                    'value-type': {
                        'type': 'reference',
                        'ref': 'y',
                    },
                },
                'y': {
                    'type': 'reference',
                    'ref': 'z',
                },
                'z': {
                    'type': 'bool',
                },
            },
        },
        extension_schema.ApiExtensionMetadata(
            name="api.with.events", version=(2, 1, 5), about="s1", description="t1",
            depends=[
                extension_schema.ExtensionDependency('abc', (1, 2, 3,), None),
                extension_schema.ExtensionDependency('def', (3, 5, 6,), (6, 0, 0,)),
            ], licenses=[], authors=[],
            default_implementation=extension_schema.ExtensionDependency(
                'axl', (5, 4, 3,), (4, 4, 100,),
            ),
            events=[
                event_schema.EventType(
                    name='e1', priority='io', send_access='public',
                    receive_access='implementations',
                    structure=event_schema.StructureEventDataType(
                        None, {
                            'first': event_schema.StructureFieldType(
                                event_schema.StructureEventDataType(
                                    description=None, field_types={
                                        'f1': event_schema.StructureFieldType(
                                            event_schema.ArrayEventDataType(
                                                None,
                                                event_schema.BoolEventDataType(None),
                                                1, 5,
                                            ),
                                            False,
                                        ),
                                        'f2': event_schema.StructureFieldType(
                                            event_schema.IntEventDataType(
                                                None,
                                                event_schema.DEFAULT_MIN_INT_VALUE,
                                                event_schema.DEFAULT_MAX_INT_VALUE,
                                            ),
                                            False,
                                        ),
                                        'f3': event_schema.StructureFieldType(
                                            event_schema.StringEventDataType(
                                                None,
                                                event_schema.DEFAULT_MIN_STRING_LENGTH,
                                                event_schema.DEFAULT_MAX_STRING_LENGTH,
                                            ),
                                            False,
                                        ),
                                        'f4': event_schema.StructureFieldType(
                                            event_schema.FloatEventDataType(None, -5.2, None),
                                            False,
                                        ),
                                        'f5': event_schema.StructureFieldType(
                                            event_schema.ArrayEventDataType(
                                                None,
                                                event_schema.IntEventDataType(None, 5, 6),
                                                event_schema.DEFAULT_MIN_ARRAY_LENGTH,
                                                event_schema.DEFAULT_MAX_ARRAY_LENGTH,
                                            ),
                                            False,
                                        ),
                                        'f6': event_schema.StructureFieldType(
                                            event_schema.EnumEventDataType(
                                                None, ['a', 'b'],
                                            ),
                                            False,
                                        ),
                                        'f7': event_schema.StructureFieldType(
                                            event_schema.DatetimeEventDataType(None),
                                            False,
                                        ),
                                        'f8': event_schema.StructureFieldType(
                                            event_schema.SelectorEventDataType(
                                                None, {
                                                    "x": event_schema.BoolEventDataType(None),
                                                    "y": event_schema.BoolEventDataType(None),
                                                },
                                            ),
                                            False,
                                        ),
                                        'f9': event_schema.StructureFieldType(
                                            event_schema.SelectorEventDataType(
                                                None, {
                                                    "x": event_schema.BoolEventDataType(None),
                                                },
                                            ),
                                            False,
                                        ),
                                    },
                                ), True,
                            ),
                        },
                    ),
                ),
            ],
        ),
    ),
    (
        'Simple Implementation',
        {
            "type": "impl", "name": "simple_impl", "version": [0, 0, 1],
            "about": "a", "description": "d",
            "depends": [], "licenses": [], "authors": [], "implements": [],
            "runtime": {'launcher': 'core'},
        },
        extension_schema.ImplExtensionMetadata(
            name="simple_impl", version=(0, 0, 1),
            about="a", description="d",
            depends=[], licenses=[], authors=[], implements=[],
            runtime=extension_schema.ExtensionRuntime('core', {}),
        ),
    ),
    (
        'Simple Standalone',
        {
            "type": "standalone", "name": "simple_standalone", "version": [0, 0, 0],
            "about": "x", "description": "y",
            "depends": [], "licenses": ["M", "I"], "authors": ["Z", "b"],
            "runtime": {'launcher': 'core', 'permissions': {'b': ['1', '2']}},
        },
        extension_schema.StandAloneExtensionMetadata(
            name="simple_standalone", version=(0, 0, 0),
            about="x", description="y",
            depends=[], licenses=["M", "I"], authors=["Z", "b"],
            runtime=extension_schema.ExtensionRuntime('core', {'b': ['1', '2']}),
        ),
    ),
]
