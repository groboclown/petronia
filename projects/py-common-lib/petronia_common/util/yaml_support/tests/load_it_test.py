
import unittest
import re
from .. import load_it


class LoadItTest(unittest.TestCase):
    def setUp(self) -> None:
        self.assertTrue(load_it.YAML_SUPPORTED)

    def test_load_empty(self) -> None:
        res = load_it.load_yaml_documents('---')
        self.assertTrue(res.ok)
        self.assertEqual([None], list(res.result))

    def test_load_simple(self) -> None:
        res = load_it.load_yaml_documents('one:\n  x: y')
        self.assertTrue(res.ok)
        self.assertEqual(
            [{'one': {'x': 'y'}}],
            list(res.result)
        )

    def test_load_error(self) -> None:
        res = load_it.load_yaml_documents('one:\n- !Ref')
        self.assertFalse(res.ok)
        self.assertIsNotNone(res.valid_error)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('Invalid YAML format: {e}', messages[0].message)
        self.assertIsNotNone(messages[0].arguments.get('e'))

    def test_dump_empty(self) -> None:
        res = load_it.dump_yaml_documents([])
        self.assertEqual('', res.result)

    def test_dump_simple(self) -> None:
        res = load_it.dump_yaml_documents([{"x": "y"}])
        self.assertEqual('x: y', res.result.strip())

    def test_dump_error(self) -> None:
        # Create a non-trivial object.

        res = load_it.dump_yaml_documents([re.compile('x').match('x')])
        self.assertFalse(res.ok)
        messages = res.valid_error.messages()
        self.assertEqual(1, len(messages))
        self.assertEqual('Could not transform documents to YAML: {e}', messages[0].message)
        self.assertIsNotNone(messages[0].arguments.get('e'))
