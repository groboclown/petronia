"""
Low-Level Windows API Calls.

Other ideas:

Registry access.
    Includes setting the shell!
    Key: HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon
    Name: Shell
    Type: REG_SZ
    Value: (path to Petronia exe)
"""

# Allow tests to run on non-Windows platforms.
import sys
from . import error_codes_common

if sys.platform.startswith('win'):  # pragma no cover
    from . import native_funcs
    from . import windows_constants
