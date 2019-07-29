
import os
from typing import Sequence


def get_user_paths() -> Sequence[str]:
    """The user's Petronia directory."""
    if 'LOCALAPPDATA' in os.environ:
        home = os.environ['LOCALAPPDATA']
        return (os.path.join(home, 'petronia'),)

    if 'HOME' in os.environ:
        home = os.environ['HOME']
        return (os.path.join(home, '.petronia'),)

    return os.getcwd()
