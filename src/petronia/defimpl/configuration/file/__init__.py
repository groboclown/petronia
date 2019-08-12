
"""
Extension configuration through files.

This extension will wait for the `platform_state.PlatformConfigurationState`
state event, then start the process of loading the events.  This will help
ensure that loading will only happen after the state extension has started.

It is up to the platform to generate the initial state to trigger the
configuration loading.
"""

from .bootstrap import bootstrap_config_file as setup_extension
from .bootstrap import EXTENSION_METADATA
