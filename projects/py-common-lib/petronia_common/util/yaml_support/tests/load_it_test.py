
"""Test the load_it module."""

import unittest
import re
from .. import load_it


class LoadItTest(unittest.TestCase):
    """Test the load_it functions"""
    def setUp(self) -> None:
        self.assertTrue(load_it.YAML_SUPPORTED)

    def test_load_empty(self) -> None:
        """Load an empty document."""
        res = load_it.load_yaml_documents('---')
        self.assertTrue(res.ok)
        self.assertEqual([None], list(res.result))

    def test_load_simple(self) -> None:
        """Load a one document yaml file"""
        res = load_it.load_yaml_documents('one:\n  x: y')
        self.assertTrue(res.ok)
        self.assertEqual(
            [{'one': {'x': 'y'}}],
            list(res.result)
        )

    def test_load_error__1(self) -> None:
        """Load a document that has a problem.  In this case, a function error."""
        res = load_it.load_yaml_documents('one:\n- !Ref')
        self.assertFalse(res.ok)
        self.assertIsNotNone(res.valid_error)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('Invalid YAML format: {e}', messages[0].message)
        self.assertIsNotNone(messages[0].arguments.get('e'))

    def test_load_error__2(self) -> None:
        """Load a document that has a problem.  In this case, a poorly formatted dict item.."""
        res = load_it.load_yaml_documents('one:\nx')
        self.assertFalse(res.ok)
        self.assertIsNotNone(res.valid_error)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('Invalid YAML format: {e}', messages[0].message)
        self.assertIsNotNone(messages[0].arguments.get('e'))

    def test_load_safe(self) -> None:
        """Ensure that the safe version of yaml is used to load the document.
        For details, see https://talosintelligence.com/vulnerability_reports/TALOS-2017-0305
        """
        res = load_it.load_yaml_documents('!!python/object/apply:sys.exit 1')
        self.assertIsNotNone(res.error)
        messages = ';'.join([m.debug() for m in res.valid_error.messages()])
        self.assertTrue(
            'Invalid YAML format' in messages,
            messages
        )

    def test_dump_empty(self) -> None:
        """Dump an empty list of documents"""
        res = load_it.dump_yaml_documents([])
        self.assertEqual('', res.result)

    def test_dump_simple(self) -> None:
        """Dump a simple dictionary."""
        res = load_it.dump_yaml_documents([{"x": "y"}])
        self.assertEqual('x: y', res.result.strip())

    def test_dump_error(self) -> None:
        """Dump an object that cannot be converted into a simple type."""
        # Create a non-trivial object.

        res = load_it.dump_yaml_documents([re.compile('x').match('x')])
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('Could not transform documents to YAML: {e}', messages[0].message)
        self.assertIsNotNone(messages[0].arguments.get('e'))
