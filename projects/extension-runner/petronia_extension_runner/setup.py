"""
Sets up the runner.
"""
from typing import Optional
from petronia_common.util import StdRet


def initialize(  # pylint:disable=keyword-arg-before-vararg
        _user_config_path: Optional[str] = None,
        _data_path: Optional[str] = None,
        _temp_dir: Optional[str] = None,
        *_others: str,
) -> StdRet[None]:
    """Initialize the user settings.  Can be called multiple times."""
    raise NotImplementedError
