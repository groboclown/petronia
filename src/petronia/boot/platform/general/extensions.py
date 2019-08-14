
"""
Basic extensions that should be started by default.
"""

from typing import Dict, List, Iterable, Optional

# Need to add stand-alone extensions that are always on by default.
# These need to load after the initial core list, because that will
# mean a state definition.  These must be loaded after that list.
# So, it may be split into a pre-boot list and a boot list.

# configuration.file
#       needs special setup to load its config from the platform.
#       That will pull from the ini files and defaults.
# default.state
#       should be in the pre-boot list, and is configurable.
#       Not part of this list.

# Extensions that must be loaded before everything else in the
# system in order to implement the core extensions.
# This maps the API name to the default extension, so that
# custom overrides can figure out what NOT to load.
# A "None" value means use the standard default.  Anything
# not in the list does not belong in the preboot sequence.
# see `petronia.boot.bootstrap.core` for the list.
DEFAULT_PREBOOT_EXTENSIONS_1: Dict[str, Optional[str]] = {
    'core.state.api': None,
    'core.extensions.api': None,
    'core.config_persistence.api': None,
}
DEFAULT_PREBOOT_EXTENSIONS_2: Dict[str, Optional[str]] = {
    'core.shutdown.api': None,
    'core.timer.api': None,
}


def get_preboot_extension_sets() -> Iterable[Iterable[str]]:
    # TODO load the defaults from an ini or config file?
    ret: List[Iterable[str]] = []
    ret.append(DEFAULT_PREBOOT_EXTENSIONS_1.keys())
    ret.append(DEFAULT_PREBOOT_EXTENSIONS_2.keys())
    return ret
