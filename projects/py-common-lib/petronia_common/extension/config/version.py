
"""
Version tools.
"""

from typing import Tuple

ExtensionVersion = Tuple[int, int, int]


def cmp_extension(first: ExtensionVersion, second: ExtensionVersion) -> int:
    """
    Returns < 0 if first is an earlier version than second, > 0 if first is
    a later version than second, and == 0 if they are the same version.

    :param first:
    :param second:
    :return:
    """
    for i in (0, 1, 2):
        diff = first[i] - second[i]
        if diff != 0:
            return diff
    return 0
