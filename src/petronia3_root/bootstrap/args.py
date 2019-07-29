
"""
User CLI arguments to adjust the initial behavior of Petronia.
"""

from typing import List, Iterable, Optional

class UserArguments:
    """
    User passed-in arguments.

    Does not allow for augmenting the extension paths.
    """
    __slots__ = (
        'platform',
        'preboot_extensions',
        'extensions',
        'only_secure',
    )
    platform: Optional[str]
    preboot_extensions: List[str]
    extensions: List[str]

    def __init__(self) -> None:
        self.platform = None
        self.preboot_extensions = []
        self.extensions = []
        self.only_secure = False


def parse_args(args: Iterable[str]) -> UserArguments:
    """
    Parses the raw sys.argv values.
    """
    # FIXME actually parse those args.
    return UserArguments()
