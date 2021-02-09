"""Sends datastore events."""

import json
from petronia_common.util import StdRet
from ..events import datastore
from ..runner.registry import EventObject, EventRegistryContext


def send_store_data(
        context: EventRegistryContext, data_id: str, data: EventObject,
) -> StdRet[None]:
    """Stores data which is maintained locally in an EventObject style
    value.  These are generated automatically by maintaining its structure
    in the `state-data` section of the extension metadata file."""

    return context.send_event(
        data_id,
        datastore.StoreDataEvent.UNIQUE_TARGET_FQN,
        datastore.StoreDataEvent(
            json.dumps(data.export_data()),
        ),
    )


def send_delete_data(context: EventRegistryContext, data_id: str) -> StdRet[None]:
    """Requests to deletes the data."""

    return context.send_event(
        data_id,
        datastore.DeleteDataEvent.UNIQUE_TARGET_FQN,
        datastore.DeleteDataEvent(),
    )
