# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-09T22:29:00.124385+00:00

"""
Data structures and marshalling for extension petronia.core.api.datastore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint: disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements


from typing import (
    Any,
    Dict,
    List,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    StdRet,
    not_none,
    STANDARD_PETRONIA_CATALOG,
)

EXTENSION_NAME = 'petronia.core.api.datastore'
EXTENSION_VERSION = (1, 0, 0)


class StoreDataEvent:
    """
    A request to store data. This is either a fresh add or update of the data. The
    event's source ID is used as the name of the stored data, which has the
    implication that it must be associated with the source extension or implemented
    API.
    """
    __slots__ = ('json',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:store-data'
    SHORT_EVENT_NAME = 'store-data'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        json: str,
    ) -> None:
        self.json = json

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StoreDataEvent']:  # pylint: disable=R0912,R0911
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
                name='StoreDataEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='StoreDataEvent',
                )
            f_json = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StoreDataEvent(
            json=not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "StoreDataEvent(" + repr(self.export_data()) + ")"


class DeleteDataEvent:
    """
    Deletes the store of data whose ID matches the source ID of the event.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.datastore:delete-data'
    SHORT_EVENT_NAME = 'delete-data'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DeleteDataEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['DeleteDataEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(DeleteDataEvent())

    def __repr__(self) -> str:
        return "DeleteDataEvent(" + repr(self.export_data()) + ")"


class SendStateEvent:
    """
    Tells the API to send out a message with the current state of the requested
    target ID data. Usually only called when an extension first starts and has
    started listening to the data change messages. If the target ID's data is not
    currently stored, then a delete message is sent. The sent message is either a
    `data-update` event or a `data-removed` event.
    """
    __slots__ = ('store_id',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:send-state'
    SHORT_EVENT_NAME = 'send-state'

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
        return SendStateEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'store_id': self.store_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SendStateEvent']:  # pylint: disable=R0912,R0911
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
                name='SendStateEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='store_id',
                    type='str',
                    name='SendStateEvent',
                )
            f_store_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SendStateEvent(
            store_id=not_none(f_store_id),
        ))

    def __repr__(self) -> str:
        return "SendStateEvent(" + repr(self.export_data()) + ")"


class DataUpdateEvent:
    """
    Notification for data that is new or changed. The target ID is always the data
    store ID. The `changed` field must be unique per original `store-data` request;
    if the store data request is identical to the previous store data request, then
    the changed field is still updated.
    """
    __slots__ = ('changed', 'json',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:data-update'
    SHORT_EVENT_NAME = 'data-update'

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
        return DataUpdateEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'changed': self.changed.strftime('%Y%m%d:%H%M%S.%f:%z'),
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DataUpdateEvent']:  # pylint: disable=R0912,R0911
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
                name='DataUpdateEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type datetime for structure {name}'),
                    field_name='changed',
                    name='DataUpdateEvent',
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
                name='DataUpdateEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='DataUpdateEvent',
                )
            f_json = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DataUpdateEvent(
            changed=not_none(f_changed),
            json=not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "DataUpdateEvent(" + repr(self.export_data()) + ")"


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