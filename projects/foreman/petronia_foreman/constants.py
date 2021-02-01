"""
Constant values.
"""

import re

TRANSLATION_CATALOG = 'petronia.foreman'

INTERNAL_CHANNEL_PATTERN = re.compile(r'^petronia\.core\..*$')
EXTENSION_LOADER_CHANNEL_PATTERN = re.compile(r'.*?.extension_loader$')
