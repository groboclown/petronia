"""Helpers for standard extension information."""

from typing import Sequence
from petronia_common.extension.config.extension_schema import ExtensionVersion


def list_as_extension_version(data: Sequence[int]) -> ExtensionVersion:
    """Create the standard extension version data structure."""
    if len(data) >= 3:
        return data[0], data[1], data[2]
    if len(data) == 2:
        return data[0], data[1], 0
    if len(data) == 1:
        return data[0], 0, 0
    return 0, 0, 0
