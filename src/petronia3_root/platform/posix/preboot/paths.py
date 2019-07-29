
import os
from typing import Sequence
from .DISTRO import (
    DISTRIBUTION_PATHS,
    UNSET_DISTRIBUTION_PATHS_VALUE,
    DEFAULT_PATHS,
)

def is_distribution_paths_unset() -> bool:
    """Did the distribution set the paths?"""
    return DISTRIBUTION_PATHS == UNSET_DISTRIBUTION_PATHS_VALUE

def get_distribution_paths() -> Sequence[str]:
    """The distribution-defined paths."""
    paths = DEFAULT_PATHS
    if not is_distribution_paths_unset():
        paths = DISTRIBUTION_PATHS
    return paths.split(os.path.pathsep)

def get_user_paths() -> Sequence[str]:
    """The user's Petronia directory."""
    if 'HOME' in os.environ:
        home = os.environ['HOME']
        return (os.path.join(home, '.petronia'),)
    return os.getcwd()
