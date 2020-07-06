
from typing import List
import unittest
from .. import extension_schema, event_schema
from ....util import UserMessage, i18n


class ExtensionSchemaMiscTest(unittest.TestCase):
    """Extra tests that aren't really covered by the loader_test"""
    def test_validate_dependencies__duplicates(self) -> None:
        deps = (
            extension_schema.ExtensionDependency('n', (1, 0, 0,), None,),
            extension_schema.ExtensionDependency('n', (2, 0, 0,), None,),
        )
        messages: List[UserMessage] = []
        extension_schema.validate_dependencies(deps, messages)
        self.assertEqual(
            [UserMessage(i18n('duplicate dependency: {name}'), name='n')],
            messages,
        )

    def test_dependency_is_within__no_below(self) -> None:
        dep = extension_schema.ExtensionDependency('n', (1, 0, 0,), None)
        self.assertTrue(dep.is_within((1, 2, 0,)))
        self.assertTrue(dep.is_within((1, 0, 0,)))
        self.assertFalse(dep.is_within((0, 0, 0,)))

    def test_dependency_is_within__below(self) -> None:
        dep = extension_schema.ExtensionDependency('n', (1, 0, 0,), (2, 0, 0))
        self.assertTrue(dep.is_within((1, 2, 0,)))
        self.assertTrue(dep.is_within((1, 0, 0,)))
        self.assertFalse(dep.is_within((0, 0, 0,)))
        self.assertFalse(dep.is_within((2, 0, 0,)))
        self.assertFalse(dep.is_within((2, 0, 1,)))

    def test_base_extension_getters(self) -> None:
        ext = extension_schema.StandAloneExtensionMetadata(
            'x', (1, 0, 0,), 'a1', 'd1', [], [], [],
        )
        self.assertEqual('standalone', ext.extension_type)
        self.assertEqual('x', ext.name)
        self.assertEqual((1, 0, 0,), ext.version)
        self.assertEqual('a1', ext.about)
        self.assertEqual('d1', ext.description)

    def test_api_duplicate_events(self) -> None:
        """This is a situation that can't happen via the loader, but can
        happen through the way the event objects are built and passed in."""
        ext = extension_schema.ApiExtensionMetadata(
            name='x', version=(1, 0, 0,), about='a1', description='d1',
            depends=[], licenses=[], authors=[],
            events=[
                event_schema.EventType(
                    'e1', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
                event_schema.EventType(
                    'e1', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
                event_schema.EventType(
                    '-e', 'high', 'public', 'public',
                    event_schema.StructureEventDataType(None, {}),
                ),
            ]
        )
        err = ext.validate_type()
        self.assertIsNotNone(err)
        assert err is not None  # mypy requirement
        self.assertEqual(
            (
                UserMessage(
                    i18n(
                        'extension name ({name}) must be {MIN_EXTENSION_NAME_LENGTH} to '
                        '{MAX_EXTENSION_NAME_LENGTH} long'
                    ),
                    name='x', MIN_EXTENSION_NAME_LENGTH=2, MAX_EXTENSION_NAME_LENGTH=255,
                ),
                UserMessage(i18n('duplicate event name: {name}'), name='e1'),
                UserMessage(
                    i18n('event name ({event_name}) must conform to the pattern `[a-z0-9][a-z0-9-]*`'),
                    event_name='-e',
                )
            ),
            err.messages(),
        )
