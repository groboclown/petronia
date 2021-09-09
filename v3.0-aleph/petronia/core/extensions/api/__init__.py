
"""
General, public, extensions API.
"""

from .defs import (
    ExtensionVersion,
    LoadedExtension,
    is_version_valid,
    ANY_VERSION,
    MAX_DEWEY_VERSION,
)
from .state import (
    ExtensionState,
)
from .events import (
    ExtensionLoadedEvent,
    as_extension_loaded_listener,
    send_request_load_extension_event,
)
from .impl_def import (
    ExtensionLoaderSetup,
    ExtensionLoaderBootstrapFunction,
    EXTENSION_LOADER_MODULE_BOOTSTRAP_FUNCTION_NAME,
)

from .bootstrap import bootstrap_extensions_api as start_extension
from .bootstrap import EXTENSION_METADATA
