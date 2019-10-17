
"""
Common utilities and patterns for platform pre-boot operations.
"""

from .inifile import (
    create_ini_config,
    load_ini_config_from_file,
    load_ini_config_from_text,
    LayeredConfig,
)
from .tmpdir import (
    TEMP_DIR_PATH
)
from .extensions import (
    get_preboot_extension_sets,
)
