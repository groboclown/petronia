"""Test that the extension files and modules are setup right for loading."""
import importlib
import unittest
import os
import sys
from petronia_common.extension.config import load_extension
from petronia_common.util import load_structured_file


CORE_EXTENSION_FILES = (
    'core-datastore-extension.yaml',
    'core-timer-extension.yaml',
    'core-file-logger-extension.yaml',
)


class CoreExtensionTest(unittest.TestCase):
    """Test extension file loading and module entrypoints."""
    def test_extension_files_modules(self) -> None:
        """Test that the extension loader package that matches the extension doc exists."""
        for ext_filename in CORE_EXTENSION_FILES:
            with self.subTest(ext_filename):
                filename = ''
                for pel in sys.path:
                    fqn = os.path.join(pel, ext_filename)
                    if os.path.isfile(fqn):
                        filename = fqn
                self.assertIsNot('', filename)
                contents_res = load_structured_file(filename)
                self.assertIsNone(contents_res.error)
                contents = contents_res.result
                extension_info = load_extension(list(contents)[0])
                self.assertIsNone(extension_info.error)
                module = importlib.import_module(extension_info.result.name)
                self.assertTrue(hasattr(module, 'extension_entrypoint'))
                self.assertTrue(
                    callable(getattr(module, 'extension_entrypoint'))
                )
