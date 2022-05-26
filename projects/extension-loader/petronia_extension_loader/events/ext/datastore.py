# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.datastore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    Any,
    List,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.datastore'
EXTENSION_VERSION = (1, 0, 0)


class StoreDataRequestEvent:
    """
    A request to store data. This is either a fresh add or update of the data. The
    event's source ID is used as the name of the stored data, which has the
    implication that it must be associated with the source extension or implemented
    API.
    """
    __slots__ = ('json',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:store-data:request'
    SHORT_EVENT_NAME = 'store-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store-json'
    UNIQUE_TARGET_REL = 'store-json'

    def __init__(
        self,
        json: str,
    ) -> None:
        self.json = json

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StoreDataRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('json')
        f_json: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='json',
                name='StoreDataRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='StoreDataRequestEvent',
                )
            f_json = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StoreDataRequestEvent(
            json=not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "StoreDataRequestEvent(" + repr(self.export_data()) + ")"


class DeleteDataRequestEvent:
    """
    Deletes the store of data whose ID matches the source ID of the event.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.datastore:delete-data:request'
    SHORT_EVENT_NAME = 'delete-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DeleteDataRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['DeleteDataRequestEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(DeleteDataRequestEvent())

    def __repr__(self) -> str:
        return "DeleteDataRequestEvent(" + repr(self.export_data()) + ")"


class SendStateRequestEvent:
    """
    Tells the API to send out a message with the current state of the requested
    target ID data. Usually only called when an extension first starts and has
    started listening to the data change messages. If the target ID's data is not
    currently stored, then a delete message is sent. The sent message is either a
    `data-updated` event or a `data-removed` event.
    """
    __slots__ = ('store_id',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:send-state:request'
    SHORT_EVENT_NAME = 'send-state:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        store_id: str,
    ) -> None:
        self.store_id = store_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SendStateRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'store_id': self.store_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SendStateRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('store_id')
        f_store_id: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='store_id',
                name='SendStateRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='store_id',
                    type='str',
                    name='SendStateRequestEvent',
                )
            f_store_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SendStateRequestEvent(
            store_id=not_none(f_store_id),
        ))

    def __repr__(self) -> str:
        return "SendStateRequestEvent(" + repr(self.export_data()) + ")"


class DataUpdatedEvent:
    """
    Notification for data that is new or changed. The target ID is always the data
    store ID. The `changed` field must be unique per original `store-data` request;
    if the store data request is identical to the previous store data request, then
    the changed field is still updated.
    """
    __slots__ = ('changed', 'json',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:data-updated'
    SHORT_EVENT_NAME = 'data-updated'

    def __init__(
        self,
        changed: datetime.datetime,
        json: str,
    ) -> None:
        self.changed = changed
        self.json = json

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DataUpdatedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'changed': self.changed.strftime('%Y%m%d:%H%M%S.%f:%z'),
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DataUpdatedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('changed')
        f_changed: datetime.datetime
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='changed',
                name='DataUpdatedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type datetime for structure {name}'),
                    field_name='changed',
                    name='DataUpdatedEvent',
                )
            try:
                f_changed = datetime.datetime.strptime(val, '%Y%m%d:%H%M%S.%f:%z')
            except ValueError:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Invalid date-time format: {value}'),
                    value=val,
                )
        val = data.get('json')
        f_json: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='json',
                name='DataUpdatedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='DataUpdatedEvent',
                )
            f_json = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DataUpdatedEvent(
            changed=not_none(f_changed),
            json=not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "DataUpdatedEvent(" + repr(self.export_data()) + ")"


class DataRemovedEvent:
    """
    Notification for data that is deleted. The target ID is always the data store
    ID. The event does not include a date field, because the event can be sent at
    any time requesting for data that was either already removed or never existed,
    and the extension is not required to maintain a list of all data removed (that
    could lead to memory issues).
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.datastore:data-removed'
    SHORT_EVENT_NAME = 'data-removed'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DataRemovedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['DataRemovedEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(DataRemovedEvent())

    def __repr__(self) -> str:
        return "DataRemovedEvent(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
