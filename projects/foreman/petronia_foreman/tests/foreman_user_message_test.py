"""Test the module."""

from typing import Optional
import unittest
import os
import sys
import io
import tempfile
import shutil
from petronia_common.util import i18n, UserMessage
from petronia_common.util.error import SimplePetroniaReturnError, ExceptionPetroniaReturnError
from .. import user_message
from ..configuration import platform


class ForemanUserMessageTest(unittest.TestCase):
    """Test the module's functions."""

    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp()
        self.config_dir = os.path.join(self.tempdir, 'configs')
        os.makedirs(self.config_dir, exist_ok=True)
        self.data_dir = os.path.join(self.tempdir, 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        self._orig_env = os.environ.copy()
        self._orig_stdout = sys.stdout
        self._orig_data_paths = list(platform.data_paths)
        self._orig_debug = user_message.DEBUG

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir, ignore_errors=True)
        os.environ.clear()
        os.environ.update(self._orig_env)
        sys.stdout = self._orig_stdout
        platform.data_paths.clear()
        platform.data_paths.extend(self._orig_data_paths)
        user_message.DEBUG = self._orig_debug

    def test_load_translation__not_found(self) -> None:
        """Test loading translations when they are found."""
        # Translation directory not find
        platform.data_paths.clear()
        platform.data_paths.append(self.data_dir)
        user_message.load_translation()
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('Simple test message abc', en_text)

        # Catalog file not found
        os.makedirs(os.path.join(self.data_dir, 'translations'))
        self.assertFalse(os.path.isfile(
            os.path.join(self.data_dir, 'translations', 'catalog.list'),
        ))
        user_message.load_translation()
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('Simple test message abc', en_text)

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
        platform.data_paths.clear()
        platform.data_paths.extend([parent_dir, self.data_dir])

        # Use a known translation.
        user_message.load_translation(['en'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('ENGLISH [abc] ENGLISH', en_text)

        # Use another known translation.
        user_message.load_translation(['fr'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('FRENCH [abc] FRENCH', en_text)

        # Use an unknown translation.
        user_message.load_translation(['zn'])
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('Simple test message abc', en_text)

        # System locale; unknown.
        # Note for the unit test: LANG is for Windows, but Unix uses ... many.
        _set_env_language('zn')
        user_message.load_translation()
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('Simple test message abc', en_text)

        # System locale; known.
        _set_env_language('en')
        user_message.load_translation()
        en_text = user_message.translate(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual('ENGLISH [abc] ENGLISH', en_text)

    def test_display__translated(self) -> None:
        """Just a simple print with a translated message."""
        parent_dir = os.path.dirname(__file__)
        platform.data_paths.clear()
        platform.data_paths.extend([parent_dir, self.data_dir])
        user_message.load_translation(['en'])
        sys.stdout = io.StringIO()
        user_message.display(
            'test-messages', i18n('Simple test message {text}'),
            text='abc',
        )
        self.assertEqual(
            'ENGLISH [abc] ENGLISH\n',
            sys.stdout.getvalue(),
        )

    def test_local_display(self) -> None:
        """Test local_display."""
        sys.stdout = io.StringIO()
        user_message.local_display(i18n('abc'))
        self.assertEqual(
            'abc\n',
            sys.stdout.getvalue(),
        )

    def test_display_error__not_error(self) -> None:
        """Test local_display."""
        sys.stdout = io.StringIO()
        err = SimplePetroniaReturnError(
            UserMessage('x', i18n('def')),
            UserMessage('x', i18n('123')),
        )
        user_message.display_error(err)
        self.assertEqual(
            'def\n123\n',
            sys.stdout.getvalue(),
        )

    def test_display_error__not_debug(self) -> None:
        """Test local_display."""
        user_message.DEBUG = False
        sys.stdout = io.StringIO()
        exp = OSError('err')
        err = ExceptionPetroniaReturnError(
            UserMessage('x', i18n('def')),
            exp,
        )
        user_message.display_error(err, debug=False)
        self.assertEqual(
            'def\n',
            sys.stdout.getvalue(),
        )

    def test_display_error__debug(self) -> None:
        """Test local_display."""
        sys.stdout = io.StringIO()
        exp: Optional[OSError] = None
        try:
            raise OSError('my custom err')
        except OSError as ose:
            exp = ose
        assert exp is not None  # nosec  # forced by mypy
        err = ExceptionPetroniaReturnError(
            UserMessage('x', i18n('def')),
            exp,
        )
        user_message.display_error(err, debug=True)
        self.assertEqual(
            'def\n',
            sys.stdout.getvalue().splitlines(keepends=True)[0],
        )
        self.assertTrue('OSError' in sys.stdout.getvalue())
        self.assertTrue('my custom err' in sys.stdout.getvalue())
        self.assertTrue('test_display_error__debug' in sys.stdout.getvalue())


def _set_env_language(lang: str) -> None:
    # Note for the unit test: There is a hierarchy of OS environment settings that
    # dictate the selected language from gettext.  This attempts to set all of those,
    # so that a pesky OS environment that may already be set doesn't interfere with
    # the unit test expected operation.
    os.environ['LANG'] = lang
    os.environ['LANGUAGE'] = lang
    os.environ['LC_ALL'] = lang
    os.environ['LC_MESSAGES'] = lang
