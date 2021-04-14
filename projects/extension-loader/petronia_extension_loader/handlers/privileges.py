"""Checks access rights for requests from extensions to perform certain behaviors."""

from typing import Iterable, Set, List, Tuple, Union, Optional
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.extension.config import (
    AbcExtensionMetadata, ApiExtensionMetadata, ImplExtensionMetadata,
    ExtensionDependency, EventType, ProtocolExtensionMetadata,
    StandAloneExtensionMetadata,
)
from ..defs import ExtensionInfo
from ..search import find_best_extension
from ..events.impl import extension_loader as extension_loader_event
from ..events.ext import foreman_announcement as foreman_event


# Events that all code-able extensions can generate.
IMPLICIT_ALLOWED_EVENTS = (
    extension_loader_event.RegisterExtensionListenersEvent.FULL_EVENT_NAME,
    foreman_event.ExtensionStartupCompleteEvent.FULL_EVENT_NAME,
)


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
        # One of the only thing that declares events...
        for event in metadata.events:
            if can_send_event(event, is_implementation):
                can_send_events.add(_get_event_name(extension.name, event))
    if isinstance(metadata, ProtocolExtensionMetadata):
        # All of the protocol events can be sent.
        for event in metadata.events:
            can_send_events.add(_get_event_name(extension.name, event))

    if isinstance(metadata, ImplExtensionMetadata):
        # All implementations can send these events.
        can_send_events.update(IMPLICIT_ALLOWED_EVENTS)
        for implements in _get_implemented_apis(metadata, loaded):
            # Only add API send access if the owner is an implementation,
            # not for the dependency's implementation.
            add_event_send_access(
                can_send_events, implements, is_implementation, searched_extensions, loaded,
            )

    if isinstance(metadata, StandAloneExtensionMetadata):
        # All stand-alone extensions can send these events.
        can_send_events.update(IMPLICIT_ALLOWED_EVENTS)

    # All the extensions have send public access.
    for dep in metadata.depends_on:
        ext = find_best_extension(dep.name, dep.minimum_version, dep.below_version, loaded)
        if not ext:
            # Shouldn't happen due to preconditions.
            continue
        add_event_send_access(can_send_events, ext, False, searched_extensions, loaded)

    return RET_OK_NONE


def can_send_event(event: EventType, is_implementation: bool) -> bool:
    """Can this event be sent?  If the extension is an implementation, then
    the event can be sent only for .
    """
    # "internal" is registered specially...
    if is_implementation:
        return event.send_access in ("implementations", "target", "public",)
    return event.send_access in ("target", "public",)


def get_valid_listen_event_pairs(  # pylint:disable=too-many-branches
        events: List[Tuple[Optional[str], Optional[str]]],
        extension: ExtensionInfo,
        is_implementation: bool,
        searched_extensions: Set[str],
        loaded: Iterable[ExtensionInfo],
) -> Set[Tuple[Optional[str], Optional[str]]]:
    """Get all event id / target id pairs from the events list that are
    applicable to this extension."""
    ret: Set[Tuple[Optional[str], Optional[str]]] = set()
    if extension.name in searched_extensions:
        return ret
    searched_extensions.add(extension.name)

    metadata = extension.metadata
    if isinstance(metadata, ApiExtensionMetadata):
        # One of the only thing that declares events...
        for event in metadata.events:
            for event_id, target_id in events:
                if event_id == _get_event_name(extension.name, event):
                    if can_listen_event(event, target_id, is_implementation):
                        ret.add((event_id, target_id))
    if isinstance(metadata, ProtocolExtensionMetadata):
        # All of the protocol events can be listened.
        for event in metadata.events:
            for event_id, target_id in events:
                if event_id == _get_event_name(extension.name, event):
                    ret.add((event_id, target_id))

    if isinstance(metadata, ImplExtensionMetadata):
        # All implementations can send this event.
        for implements in _get_implemented_apis(metadata, loaded):
            # Only add API send access if the owner is an implementation,
            # not for the dependency's implementation.
            ret.update(get_valid_listen_event_pairs(
                events, implements, is_implementation, searched_extensions, loaded,
            ))

    # All the extensions have send public access.
    for dep in metadata.depends_on:
        ext = find_best_extension(dep.name, dep.minimum_version, dep.below_version, loaded)
        if not ext:
            # Shouldn't happen due to preconditions.
            continue
        ret.update(get_valid_listen_event_pairs(
            events, ext, False, searched_extensions, loaded,
        ))

    return ret


def can_listen_event(event: EventType, target_id: Optional[str], is_implementation: bool) -> bool:
    """Can this event be listened to?  Events that can only be received by the target
    of the event must have a non-None target."""
    if event.receive_access == 'target':
        return target_id is not None
    if is_implementation:
        return event.receive_access in ("implementations", "public",)
    return event.receive_access == "public"


def _get_implemented_apis(
        metadata: ImplExtensionMetadata,
        loaded: Iterable[ExtensionInfo],
) -> List[ExtensionInfo]:
    ret: List[ExtensionInfo] = []
    for dep in metadata.implements:
        ext = find_best_extension(dep.name, dep.minimum_version, dep.below_version, loaded)
        if not ext:  # pragma no cover
            # Shouldn't happen...  Should it be reported?
            continue  # pragma no cover
        ext_metadata = ext.metadata
        # Implements list is supposed to be only APIs.  So we only check APIs
        if isinstance(ext_metadata, ApiExtensionMetadata):
            ret.append(ext)
    return ret


def _get_event_name(extension_name: str, event: EventType) -> str:
    return extension_name + ':' + event.name
