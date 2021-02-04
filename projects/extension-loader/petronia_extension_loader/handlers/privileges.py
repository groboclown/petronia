"""Checks access rights for requests from extensions to perform certain behaviors."""

from typing import Iterable, Set, List, Union
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.extension.config import (
    AbcExtensionMetadata, ApiExtensionMetadata, ImplExtensionMetadata,
    ExtensionDependency, EventType,
)
from ..defs import ExtensionInfo
from ..search import find_best_extension


def get_source_id_prefix_access(
        extension: ExtensionInfo,
) -> Set[str]:
    """Add the valid source-id prefixes that the extension can use as its
    source IDs.  This is restricted to the extension itself, and, if it's
    an implementation, all implemented API extensions."""
    metadata = extension.metadata
    source_id_prefixes: Set[str] = {
        create_source_id_prefix(metadata),
    }

    if isinstance(metadata, ImplExtensionMetadata):
        for implements in metadata.implements:
            source_id_prefixes.add(create_source_id_prefix(implements))

    return source_id_prefixes


def create_source_id_prefix(metadata: Union[AbcExtensionMetadata, ExtensionDependency]) -> str:
    """Create the source-id prefix used in the permissions."""
    return metadata.name + ':'


def add_event_send_access(
        can_send_events: Set[str],
        extension: ExtensionInfo,
        is_implementation: bool,
        searched_extensions: Set[str],
        loaded: Iterable[ExtensionInfo],
) -> StdRet[None]:
    """Get the list of event IDs that the extension has permissions to send.
    This is based on the declared dependencies and implementation and their declared
    event send permissions.  Dependencies declared as implementations must instead
    only look at the implements APIs.

    This should only be called after all the declared dependencies have been loaded.
    """
    if extension.name in searched_extensions:
        return RET_OK_NONE
    searched_extensions.add(extension.name)

    metadata = extension.metadata
    if isinstance(metadata, ApiExtensionMetadata):
        # The only thing that declares events...
        for event in metadata.events:
            if can_send_event(event, is_implementation):
                can_send_events.add(event.name)

    if isinstance(metadata, ImplExtensionMetadata):
        for implements in _get_implemented_apis(metadata, loaded):
            add_event_send_access(can_send_events, implements, True, searched_extensions, loaded)

    # All the extensions have send public access.
    for dep in metadata.depends_on:
        ext = find_best_extension(dep.name, dep.minimum_version, dep.below_version, loaded)
        if not ext:
            # Shouldn't happen... should this problem be reported?
            continue  # pragma no cover
        add_event_send_access(can_send_events, ext, False, searched_extensions, loaded)

    return RET_OK_NONE


def can_send_event(event: EventType, is_implementation: bool) -> bool:
    """Can this event be sent?  If the extension is an implementation, then
    the event can be sent only for .
    """
    # "internal" is registered specially...
    if is_implementation:
        return event.send_access in ("implementations",)
    return event.send_access in ("target", "public",)


def _get_implemented_apis(
        metadata: ImplExtensionMetadata,
        loaded: Iterable[ExtensionInfo],
) -> List[ExtensionInfo]:
    ret: List[ExtensionInfo] = []
    for dep in metadata.implements:
        ext = find_best_extension(dep.name, dep.minimum_version, dep.below_version, loaded)
        if not ext:
            # Shouldn't happen...  Should it be reported?
            continue
        ext_metadata = ext.metadata
        # Really, implements list is supposed to be only APIs...
        if isinstance(ext_metadata, ApiExtensionMetadata):
            ret.append(ext)
        elif isinstance(ext_metadata, ImplExtensionMetadata):
            # Hopefully, everything else that loaded this extension did correct cycle checking.
            ret.extend(_get_implemented_apis(ext_metadata, loaded))
        # StandAlone is ignored if its in the implementation list.
    return ret
