"""Boot launchers, which have special means for starting a launcher at boot time, for
running without the extension loader events."""

from .abc import AbcBootLauncherCategory
from .win_native import WindowsNativeLauncher, create_windows_native_launcher
from .win_extension_loader import WindowsExtensionLoader, create_windows_extension_loader
