
"""
Temp directory helpers.
"""

import tempfile
import atexit

TEMP_DIR = tempfile.TemporaryDirectory(prefix='petronia-')
atexit.register(TEMP_DIR.cleanup)
TEMP_DIR_PATH = TEMP_DIR.name
