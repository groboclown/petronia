"""Sends datastore events."""

from typing import Protocol, Dict, Any
import json
from petronia_common.util import StdRet
from ..events import datastore
from ..runner.registry import EventRegistryContext


class StateObject(Protocol):
    """Protocol for all generated state objects."""
    def export_data(self) -> Dict[str, Any]:
        """Export the event object into a JSON-like structure for creating a raw event object."""
        raise NotImplementedError  # pragma no cover


def send_store_data(
        context: EventRegistryContext, data_id: str, data: StateObject,
) -> StdRet[None]:
    """Stores data which is maintained locally in an EventObject style
    value.  These are generated automatically by maintaining its structure
    in the `state-data` section of the extension metadata file."""

    return context.send_event(
        data_id,
        datastore.StoreDataRequestEvent.UNIQUE_TARGET_FQN,
        datastore.StoreDataRequestEvent(
            json.dumps(data.export_data()),
        ),
    )


def send_delete_data(context: EventRegistryContext, data_id: str) -> StdRet[None]:
    """Requests to deletes the data."""

    return context.send_event(
        data_id,
        datastore.DeleteDataRequestEvent.UNIQUE_TARGET_FQN,
        datastore.DeleteDataRequestEvent(),
    )


def send_request_data_state(
        context: EventRegistryContext, source_id: str, data_id: str,
) -> StdRet[None]:
    """Request the extension to send out the current state of the given data ID."""
    return context.send_event(
        source_id,
        datastore.SendStateRequestEvent.UNIQUE_TARGET_FQN,
        datastore.SendStateRequestEvent(data_id),
    )
