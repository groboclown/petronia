"""Parse all kinds of user values."""

from typing import Tuple, Union, Optional


def parse_extension_name_version(  # pylint:disable=too-many-return-statements
        name_version: str,
) -> Union[
     Tuple[str, None, None, None],
     Tuple[str, int, None, None],
     Tuple[str, int, int, Optional[int]],
 ]:
    """Split the name_version string into an extension name and major, minor, patch
    version information.  If one of those is not given, then it is None."""
    col_pos = name_version.find(':')
    if col_pos > 0:
        name = name_version[:col_pos]
        version_parts = name_version[col_pos + 1:].split('.')
        if len(version_parts) <= 0:  # pragma no cover
            # split should always return at least a length 1 array, but just in case...
            return name, None, None, None  # pragma no cover
        major = _parse_int(version_parts[0])
        if major is None:
            return name, None, None, None
        if len(version_parts) <= 1:
            return name, major, None, None
        minor = _parse_int(version_parts[1])
        if minor is None:
            return name, major, None, None
        if len(version_parts) <= 2:
            return name, major, minor, None
        return name, major, minor, _parse_int(version_parts[2])
    # No version part given.
    return name_version, None, None, None


def _parse_int(val: str) -> Optional[int]:
    try:
        return int(val)
    except ValueError:
        return None
