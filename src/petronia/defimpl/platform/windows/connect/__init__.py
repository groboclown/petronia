
"""
Connects the Petronia platform requirements with the native interactions.

Because none of the `ctypes` references should be used outside the `arch`
package, this package allows for interaction.
"""

from .windows_hook_event import (
    WindowsHookEvent,
)
from .screen import (
    get_monitors,
    from_user_to_native_screen,
)
from ..arch.native_funcs.windows_common import WindowsErrorMessage
