"""
Low-Level Windows API Calls
"""

# Allow tests to run on non-Windows platforms.
import sys
if sys.platform.startswith('win'):
    from . import funcs
