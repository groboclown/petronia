"""Test utilities for creating extension data structures."""

from typing import Sequence, Tuple, List
from petronia_common.extension.config import (
    ExtensionDependency,
    StandAloneExtensionMetadata,
    ApiExtensionMetadata,
    ProtocolExtensionMetadata, EventType, EventAccessType,
)
from petronia_common.extension.config.extension_schema import (
    ExtensionRuntime, ImplExtensionMetadata,
)
from petronia_extension_loader.defs import ExtensionInfo


def mk_api_ext(
        name: str,
        default: Tuple[str, int, int, int, int, int, int],
        version: Tuple[int, int, int] = (1, 0, 0),
        depends: Sequence[Tuple[str, int, int, int, int, int, int]] = (),
        events: Sequence[Tuple[str, EventAccessType, EventAccessType]] = (),
) -> ExtensionInfo:
    """Create ExtensionInfo for an API"""
    return ExtensionInfo([], ApiExtensionMetadata(
        name, version, '', '', mk_depend_list(depends), [], [],
        [
            EventType(event_name, 'io', send_access, receive_access, None, None)
            for event_name, send_access, receive_access in events
        ],
        mk_depend(*default),
    ))


def mk_protocol_ext(
        name: str,
        version: Tuple[int, int, int] = (1, 0, 0),
        events: Sequence[Tuple[str, EventAccessType, EventAccessType]] = (),
) -> ExtensionInfo:
    """Create ExtensionInfo for a protocol"""
    return ExtensionInfo([], ProtocolExtensionMetadata(
        name, version, '', '', [], [], [
            EventType(event_name, 'io', send_access, receive_access, None, None)
            for event_name, send_access, receive_access in events
        ],
    ))


def mk_impl_ext(
        name: str,
        version: Tuple[int, int, int] = (1, 0, 0),
        depends: Sequence[Tuple[str, int, int, int, int, int, int]] = (),
        impl: Sequence[Tuple[str, int, int, int, int, int, int]] = (),
) -> ExtensionInfo:
    """Create ExtensionInfo for an implementation"""
    return ExtensionInfo([], ImplExtensionMetadata(
        name, version, '', '', mk_depend_list(depends), [], [],
        mk_depend_list(impl), ExtensionRuntime('x', {}),
    ))


def mk_standalone_ext(
        name: str,
        version: Tuple[int, int, int] = (1, 0, 0),
        depends: Sequence[Tuple[str, int, int, int, int, int, int]] = (),
) -> ExtensionInfo:
    """Create ExtensionInfo for a standalone extension"""
    return ExtensionInfo([], StandAloneExtensionMetadata(
        name, version, '', '', mk_depend_list(depends), [], [],
        ExtensionRuntime('l', {}),
    ))


def mk_depend_list(
        depends: Sequence[Tuple[str, int, int, int, int, int, int]],
) -> List[ExtensionDependency]:
    """Create a dependency list"""
    depends_on: List[ExtensionDependency] = []
    for (
            dep_name, dep_min_major, dep_min_minor, dep_min_patch,
            dep_max_major, dep_max_minor, dep_max_patch,
    ) in depends:
        depends_on.append(mk_depend(
            dep_name,
            dep_min_major, dep_min_minor, dep_min_patch,
            dep_max_major, dep_max_minor, dep_max_patch,
        ))
    return depends_on


def mk_depend(
        dep_name: str,
        dep_min_major: int, dep_min_minor: int, dep_min_patch: int,
        dep_max_major: int, dep_max_minor: int, dep_max_patch: int,
) -> ExtensionDependency:
    """Create a dependency"""
    return ExtensionDependency(
        dep_name, (dep_min_major, dep_min_minor, dep_min_patch),
        None if dep_max_major < 0 else (dep_max_major, dep_max_minor, dep_max_patch),
    )
