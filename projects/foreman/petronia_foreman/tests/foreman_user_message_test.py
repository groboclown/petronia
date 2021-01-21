"""Test the module."""

import unittest
import os
import tempfile
import shutil
import locale
from petronia_common.util import i18n
from .. import user_message
from ..configuration.platform import PlatformSettings, CATEGORY__OSX


class ForemanUserMessageTest(unittest.TestCase):
    """Test the module's functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self.config_dir = os.path.join(self.tempdir, 'configs')
        os.makedirs(self.config_dir, exist_ok=True)
        self.data_dir = os.path.join(self.tempdir, 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        self._init_locale = locale.getlocale(category=locale.LC_CTYPE)
        self._orig_env = os.environ.copy()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        locale.setlocale(locale.LC_CTYPE, self._init_locale[0])
        os.environ.clear()
        os.environ.update(self._orig_env)

    def test_load_translation__found(self) -> None:
        """Test loading translations when they are found."""

        # This uses the translation files stored in the "translations" sub-directory.
        # If those files need to be modified, then run these commands after modifying them:
        # cd (translations dir)
        # python3 -m babel.messages.frontend compile \
        #    --domain=test-messages --directory=. --locale=en --input-file=en.po --use-fuzzy
        # python3 -m babel.messages.frontend compile \
        #    --domain=test-messages --directory=. --locale=fr --input-file=fr.po --use-fuzzy

        parent_dir = os.path.dirname(__file__)
        translation_dir = os.path.join(parent_dir, 'translations')
        self.assertTrue(os.path.isdir(translation_dir))
        settings = PlatformSettings(
            'test', CATEGORY__OSX, (self.config_dir,), (parent_dir, self.data_dir,), 'x',
        )

        # Use a known translation.
        user_message.load_translation(settings, ['en'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc'
        )
        self.assertEqual('ENGLISH [abc] ENGLISH', en_text)

        # Use another known translation.
        user_message.load_translation(settings, ['fr'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc'
        )
        self.assertEqual('FRENCH [abc] FRENCH', en_text)

        # Use an unknown translation.
        user_message.load_translation(settings, ['zn'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc'
        )
        self.assertEqual('Simple test message abc', en_text)

        # System locale; unknown.
        os.environ['LANG'] = 'zn'
        user_message.load_translation(settings)
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc'
        )
        self.assertEqual('Simple test message abc', en_text)

        # System locale; known.
        os.environ['LANG'] = 'en'
        user_message.load_translation(settings)
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc'
        )
        self.assertEqual('ENGLISH [abc] ENGLISH', en_text)
