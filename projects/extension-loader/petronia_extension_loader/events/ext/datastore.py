# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:25.444676

"""
Data structures and marshalling for extension petronia.core.api.datastore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint: disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements


from typing import (
    Optional,
    List,
    Dict,
    Any,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    T,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.datastore'
EXTENSION_VERSION = (1, 0, 0)


class StoreDataEvent:
    """
    A request to store data. This is either a fresh add or update of the data. For
    freshly added data, later updates and deletes will only be allowed by events
    whose source ID match the source ID for the add request.
    """
    __slots__ = ('destination', 'json',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:store-data'
    SHORT_EVENT_NAME = 'store-data'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        destination: str,
        json: str,
    ) -> None:
        self.destination = destination
        self.json = json

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'destination': self.destination,
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StoreDataEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_destination: Optional[str] = None
        val = data.get('destination')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='destination',
                name='StoreDataEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='destination',
                    type='str',
                    name='StoreDataEvent',
                ))
            else:
                f_destination = val
        f_json: Optional[str] = None
        val = data.get('json')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='json',
                name='StoreDataEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='StoreDataEvent',
                ))
            else:
                f_json = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StoreDataEvent(
            destination=_not_none(f_destination),
            json=_not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "StoreDataEvent(" + repr(self.export_data()) + ")"


class DeleteDataEvent:
    """
    Deletes the store of data. This request will only be allowed by events whose
    source ID matches the source ID that initially created the data.
    """
    __slots__ = ('destination',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:delete-data'
    SHORT_EVENT_NAME = 'delete-data'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        destination: str,
    ) -> None:
        self.destination = destination

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DeleteDataEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'destination': self.destination,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DeleteDataEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_destination: Optional[str] = None
        val = data.get('destination')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='destination',
                name='DeleteDataEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='destination',
                    type='str',
                    name='DeleteDataEvent',
                ))
            else:
                f_destination = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DeleteDataEvent(
            destination=_not_none(f_destination),
        ))

    def __repr__(self) -> str:
        return "DeleteDataEvent(" + repr(self.export_data()) + ")"


class SendStateEvent:
    """
    Tells the API to send out a message with the current state of the requested
    target ID data. Usually only called when an extension first starts and has
    started listening to the data change messages. If the target ID's data is not
    currently stored, then a delete message is sent.
    """
    __slots__ = ('destination',)
    FULL_EVENT_NAME = 'petronia.core.api.datastore:send-state'
    SHORT_EVENT_NAME = 'send-state'

    UNIQUE_TARGET_FQN = 'petronia.core.api.datastore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        destination: str,
    ) -> None:
        self.destination = destination

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SendStateEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'destination': self.destination,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SendStateEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_destination: Optional[str] = None
        val = data.get('destination')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='destination',
                name='SendStateEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='destination',
                    type='str',
                    name='SendStateEvent',
                ))
            else:
                f_destination = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SendStateEvent(
            destination=_not_none(f_destination),
        ))

    def __repr__(self) -> str:
        return "SendStateEvent(" + repr(self.export_data()) + ")"


class DataUpdateEvent:
    """
    Notification for data that is new or changed. The target ID is always the data
    store destination ID.
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
            'changed': self.changed.strftime('YYYYMMDD:hhmmss.sss:Z'),
            'json': self.json,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DataUpdateEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_changed: Optional[datetime.datetime] = None
        val = data.get('changed')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='changed',
                name='DataUpdateEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type datetime for structure {name}'),
                    field_name='changed',
                    name='DataUpdateEvent',
                ))
            else:
                try:
                    f_changed = datetime.datetime.strptime(val, 'YYYYMMDD:hhmmss.sss:Z')
                except ValueError:
                    errors.append(StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _('Invalid date-time format: {value}'),
                        value=val,
                    ))
        f_json: Optional[str] = None
        val = data.get('json')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='json',
                name='DataUpdateEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='json',
                    type='str',
                    name='DataUpdateEvent',
                ))
            else:
                f_json = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DataUpdateEvent(
            changed=_not_none(f_changed),
            json=_not_none(f_json),
        ))

    def __repr__(self) -> str:
        return "DataUpdateEvent(" + repr(self.export_data()) + ")"


class DataRemovedEvent:
    """
    Notification for data that is deleted. The target ID is always the data store
    ID.
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


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret