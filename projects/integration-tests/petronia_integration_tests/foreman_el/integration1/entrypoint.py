"""
Entrypoint pattern for extensions started by extension-runner.
"""

from typing import Dict, Any
from petronia_common.util import StdRet


def start_extension(
        _config: Dict[str, Any],
) -> StdRet[None]:
    """Starts the extension."""
    pass
