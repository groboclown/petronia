
from typing import Sequence, List
import os


def get_user_paths() -> Sequence[str]:
    """The user's Petronia directory."""
    ret: List[str] = []
    if 'LOCALAPPDATA' in os.environ:
        ret.append(os.path.join(os.environ['LOCALAPPDATA'], 'petronia'))

    if 'HOME' in os.environ:
        ret.append(os.path.join(os.environ['HOME'], '.petronia'))

    # ret.append(os.getcwd())
    return tuple(ret)
