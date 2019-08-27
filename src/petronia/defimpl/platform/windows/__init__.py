
"""
Windows platform API handler.

Low-level Windows API should be restricted to the `arch` package.  Those
functions declared in that package can be used elsewhere in this API.

Data structures used by the Windows API can be used throughout the API, but
must not escape this package.
"""

from .bootstrap import bootstrap_windows_platform as start_extension
from .bootstrap import EXTENSION_METADATA
