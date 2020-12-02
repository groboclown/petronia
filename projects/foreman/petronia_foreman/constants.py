"""
Constant values.
"""

import re

TRANSLATION_CATALOG = 'petronia.foreman'

EXTENSION_LOADER_CHANNEL = 'extension-loader'

INTERNAL_CHANNEL_PATTERN = re.compile(r'^petronia\.core\..*$')
