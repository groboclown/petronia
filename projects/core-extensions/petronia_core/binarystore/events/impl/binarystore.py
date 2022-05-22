# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.binarystore version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    cast,
    Dict,
    SupportsFloat,
    List,
    Any,
    SupportsInt,
    Union,
    Optional,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    collect_errors_from,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.binarystore'
EXTENSION_VERSION = (1, 0, 0)


class StoreDataRequestEvent:
    """
    A request to store data. The event's source ID is used as the name of the stored
    data, which has the implication that it must be associated with the source
    extension or implemented API. This request includes meta-data about the binary
    data. The extension may refuse the request.
    """
    __slots__ = ('mime_type',)
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:store-data:request'
    SHORT_EVENT_NAME = 'store-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.binarystore:store-bin'
    UNIQUE_TARGET_REL = 'store-bin'

    def __init__(
        self,
        mime_type: str,
    ) -> None:
        self.mime_type = mime_type

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'mime_type': self.mime_type,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StoreDataRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('mime_type')
        f_mime_type: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='mime_type',
                name='StoreDataRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='mime_type',
                    type='str',
                    name='StoreDataRequestEvent',
                )
            f_mime_type = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StoreDataRequestEvent(
            mime_type=not_none(f_mime_type),
        ))

    def __repr__(self) -> str:
        return "StoreDataRequestEvent(" + repr(self.export_data()) + ")"


class StoreDataAllowedEvent:
    """
    Response from the extension to the "store-data:request" event when the binary
    data will be allowed. When the sender of "store-data:request" receives this
    event, the follow up "store-data:data" response is sent. The target ID for this
    event is the ID passed as the source ID of the initial "store-data:request".
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:store-data:allowed'
    SHORT_EVENT_NAME = 'store-data:allowed'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataAllowedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['StoreDataAllowedEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(StoreDataAllowedEvent())

    def __repr__(self) -> str:
        return "StoreDataAllowedEvent(" + repr(self.export_data()) + ")"


class MessageArgumentValue:
    """
    A replacement value for a named argument in the message.
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            List[int],
            float,
            List[bool],
            str,
            List[float],
            int,
            List[str],
            bool,
            datetime.datetime,
            List[datetime.datetime],
        ],
    ) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        """Name of the selector type."""
        return self.__name

    @property
    def value(self) -> Union[
            List[int],
            float,
            List[bool],
            str,
            List[float],
            int,
            List[str],
            bool,
            datetime.datetime,
            List[datetime.datetime],
    ]:
        """The selector value."""
        return self.__value

    def __repr__(self) -> str:
        return 'MessageArgumentValue(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0912
        """Create the event data structure, ready for marshalling."""
        if self.__name == 'string':
            return {
                '^': self.__name,
                '$':
                    cast(str, self.__value),
            }
        if self.__name == 'int':
            return {
                '^': self.__name,
                '$':
                    cast(int, self.__value),
            }
        if self.__name == 'float':
            return {
                '^': self.__name,
                '$':
                    cast(float, self.__value),
            }
        if self.__name == 'bool':
            return {
                '^': self.__name,
                '$':
                    cast(bool, self.__value),
            }
        if self.__name == 'datetime':
            return {
                '^': self.__name,
                '$':
                    cast(datetime.datetime, self.__value).strftime('%Y%m%d:%H%M%S.%f:%z'),
            }
        if self.__name == 'string_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[str], self.__value)),
            }
        if self.__name == 'int_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[int], self.__value)),
            }
        if self.__name == 'float_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[float], self.__value)),
            }
        if self.__name == 'bool_list':
            return {
                '^': self.__name,
                '$':
                    list(cast(List[bool], self.__value)),
            }
        if self.__name == 'datetime_list':
            return {
                '^': self.__name,
                '$':
                    [dtv.strftime('%Y%m%d:%H%M%S.%f:%z') for dtv in cast(List[datetime.datetime], self.__value)],
            }
        raise RuntimeError('invalid inner type: ' + repr(self.__name))  # pragma no cover

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MessageArgumentValue']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        selector_name = data.get('^', data.get('type'))
        val = data.get('$', data.get('value'))
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('selector for {name} value must have ^ and $ keys, or "type" and "value" keys'),
                name='MessageArgumentValue',
            )
        if selector_name == 'string':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='string',
                    type='str',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                val,
            ))
        if selector_name == 'int':
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='int',
                    type='int',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                int(val),
            ))
        if selector_name == 'float':
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='float',
                    type='float',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                float(val),
            ))
        if selector_name == 'bool':
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='bool',
                    type='bool',
                    name='MessageArgumentValue',
                )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                val,
            ))
        if selector_name == 'datetime':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Value must be of type datetime for selector {name}'),
                    field_name='datetime',
                    name='MessageArgumentValue',
                )
            try:
                dt_val = datetime.datetime.strptime(val, '%Y%m%d:%H%M%S.%f:%z')
                return StdRet.pass_ok(MessageArgumentValue(
                    selector_name,
                    dt_val,
                ))
            except ValueError:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Invalid date-time format: {value}'),
                    value=val,
                )
        if selector_name == 'string_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='string_list',
                    type='List[str]',
                    name='MessageArgumentValue',
                )
            ret_val_str: List[str] = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='string_list',
                        type='str',
                        name='MessageArgumentValue',
                    )
                ret_val_str.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_str,
            ))
        if selector_name == 'int_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='int_list',
                    type='List[int]',
                    name='MessageArgumentValue',
                )
            ret_val_int: List[int] = []
            for item in val:
                if not isinstance(item, int):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='int_list',
                        type='int',
                        name='MessageArgumentValue',
                    )
                ret_val_int.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_int,
            ))
        if selector_name == 'float_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='float_list',
                    type='List[float]',
                    name='MessageArgumentValue',
                )
            ret_val_float: List[float] = []
            for item in val:
                if not isinstance(item, float):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='float_list',
                        type='float',
                        name='MessageArgumentValue',
                    )
                ret_val_float.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_float,
            ))
        if selector_name == 'bool_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='bool_list',
                    type='List[bool]',
                    name='MessageArgumentValue',
                )
            ret_val_bool: List[bool] = []
            for item in val:
                if not isinstance(item, bool):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='bool_list',
                        type='bool',
                        name='MessageArgumentValue',
                    )
                ret_val_bool.append(item)
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_bool,
            ))
        if selector_name == 'datetime_list':
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for selector {name}'),
                    field_name='datetime_list',
                    type='List[datetime.datetime]',
                    name='MessageArgumentValue',
                )
            ret_val_datetime_datetime: List[datetime.datetime] = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='datetime_list',
                        type='datetime.datetime',
                        name='MessageArgumentValue',
                    )
                try:
                    ret_val_datetime_datetime.append(datetime.datetime.strptime(item, '%Y%m%d:%H%M%S.%f:%z'))
                except ValueError:
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _('Invalid date-time format: {value}'),
                        value=val,
                    )
            return StdRet.pass_ok(MessageArgumentValue(
                selector_name,
                ret_val_datetime_datetime,
            ))
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('Invalid selector name {name} for {nc}'),
            name=selector_name,
            nc='MessageArgumentValue',
        )


class MessageArgument:
    """
    An argument to be inserted into the localizable message.
    """
    __slots__ = ('name', 'value',)

    def __init__(
        self,
        name: str,
        value: MessageArgumentValue,
    ) -> None:
        self.name = name
        self.value = value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'value': self.value.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MessageArgument']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('name')
        f_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='MessageArgument',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='MessageArgument',
                )
            f_name = val
        val = data.get('value')
        f_value: MessageArgumentValue
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='value',
                name='MessageArgument',
            )
        else:
            parsed_value = MessageArgumentValue.parse_data(val)
            if parsed_value.has_error:
                return parsed_value.forward()
            if parsed_value.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='value',
                )
            f_value = parsed_value.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MessageArgument(
            name=not_none(f_name),
            value=not_none(f_value),
        ))

    def __repr__(self) -> str:
        return "MessageArgument(" + repr(self.export_data()) + ")"


class LocalizableMessage:
    """
    A localizable message for user display.
    """
    __slots__ = ('catalog', 'message', 'arguments',)

    def __init__(
        self,
        catalog: str,
        message: str,
        arguments: Optional[List[MessageArgument]],
    ) -> None:
        self.catalog = catalog
        self.message = message
        self.arguments = arguments

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'catalog': self.catalog,
            'message': self.message,
            'arguments': None if self.arguments is None else [v.export_data() for v in self.arguments],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LocalizableMessage']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('catalog')
        f_catalog: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='catalog',
                name='LocalizableMessage',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='catalog',
                    type='str',
                    name='LocalizableMessage',
                )
            f_catalog = val
        val = data.get('message')
        f_message: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='message',
                name='LocalizableMessage',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='message',
                    type='str',
                    name='LocalizableMessage',
                )
            f_message = val
        val = data.get('arguments')
        f_arguments: Optional[List[MessageArgument]] = None
        if val is not None:
            f_arguments = []
            for item in val:
                parsed_arguments = MessageArgument.parse_data(item)
                if parsed_arguments.has_error:
                    return parsed_arguments.forward()
                f_arguments.append(parsed_arguments.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LocalizableMessage(
            catalog=not_none(f_catalog),
            message=not_none(f_message),
            arguments=f_arguments,
        ))

    def __repr__(self) -> str:
        return "LocalizableMessage(" + repr(self.export_data()) + ")"


class StoreDataRefusedEvent:
    """
    Response from the extension to the "store-data:request" event when the binary
    data storage is not allowed.
    """
    __slots__ = ('reason',)
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:store-data:refused'
    SHORT_EVENT_NAME = 'store-data:refused'

    def __init__(
        self,
        reason: LocalizableMessage,
    ) -> None:
        self.reason = reason

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StoreDataRefusedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'reason': self.reason.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StoreDataRefusedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('reason')
        f_reason: LocalizableMessage
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='reason',
                name='StoreDataRefusedEvent',
            )
        else:
            parsed_reason = LocalizableMessage.parse_data(val)
            if parsed_reason.has_error:
                return parsed_reason.forward()
            if parsed_reason.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='reason',
                )
            f_reason = parsed_reason.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StoreDataRefusedEvent(
            reason=not_none(f_reason),
        ))

    def __repr__(self) -> str:
        return "StoreDataRefusedEvent(" + repr(self.export_data()) + ")"


class StoreDataDataEvent:
    """
    Binary event
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:store-data:data'
    SHORT_EVENT_NAME = 'store-data:data'

    UNIQUE_TARGET_FQN = 'petronia.core.api.binarystore:store-bin'
    UNIQUE_TARGET_REL = 'store-bin'


class DeleteDataRequestEvent:
    """
    Deletes the store of data whose ID matches the source ID of the event.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:delete-data:request'
    SHORT_EVENT_NAME = 'delete-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.binarystore:store'
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


class DescribeDataRequestEvent:
    """
    Tells the API to send out a message with the description of the data for the
    store_id. In all cases, a "data-description" response is sent, even if the ID
    was never stored.
    """
    __slots__ = ('store_id',)
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:describe-data:request'
    SHORT_EVENT_NAME = 'describe-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.binarystore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        store_id: str,
    ) -> None:
        self.store_id = store_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DescribeDataRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'store_id': self.store_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DescribeDataRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='DescribeDataRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='store_id',
                    type='str',
                    name='DescribeDataRequestEvent',
                )
            f_store_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DescribeDataRequestEvent(
            store_id=not_none(f_store_id),
        ))

    def __repr__(self) -> str:
        return "DescribeDataRequestEvent(" + repr(self.export_data()) + ")"


class DataDescriptionEvent:
    """
    Notification for data stored. The target ID is always the data store ID. This
    event is safe to listen to on a broad, continuous way. The event is sent either
    when a request for the description is sent through a "describe-data:request"
    event, or when data is added or removed.
    """
    __slots__ = ('state', 'mime_type', 'sha256', 'size',)
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:data-description'
    SHORT_EVENT_NAME = 'data-description'

    def __init__(
        self,
        state: str,
        mime_type: Optional[str],
        sha256: Optional[str],
        size: Optional[int],
    ) -> None:
        self.state = state
        self.mime_type = mime_type
        self.sha256 = sha256
        self.size = size

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return DataDescriptionEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'state': self.state,
            'mime_type': self.mime_type,
            'sha256': self.sha256,
            'size': self.size,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['DataDescriptionEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('state')
        f_state: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='state',
                name='DataDescriptionEvent',
            )
        else:
            if val not in ('active','deleted','unset', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='state',
                    type='str',
                    name='DataDescriptionEvent',
                )
            f_state = val
        val = data.get('mime_type')
        f_mime_type: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='mime_type',
                    type='str',
                    name='DataDescriptionEvent',
                )
            f_mime_type = val
        val = data.get('sha256')
        f_sha256: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='sha256',
                    type='str',
                    name='DataDescriptionEvent',
                )
            f_sha256 = val
        val = data.get('size')
        f_size: Optional[int] = None
        if val is not None:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='size',
                    type='int',
                    name='DataDescriptionEvent',
                )
            f_size = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(DataDescriptionEvent(
            state=not_none(f_state),
            mime_type=f_mime_type,
            sha256=f_sha256,
            size=f_size,
        ))

    def __repr__(self) -> str:
        return "DataDescriptionEvent(" + repr(self.export_data()) + ")"


class SendDataRequestEvent:
    """
    Tells the API to send out a message with the current state of the requested
    target ID data. Usually only called when an extension first starts and has
    started listening to the data change messages. If the store_id's data is not
    "active", then no event is sent.
    """
    __slots__ = ('store_id',)
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:send-data:request'
    SHORT_EVENT_NAME = 'send-data:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.binarystore:store'
    UNIQUE_TARGET_REL = 'store'

    def __init__(
        self,
        store_id: str,
    ) -> None:
        self.store_id = store_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SendDataRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'store_id': self.store_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SendDataRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='SendDataRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='store_id',
                    type='str',
                    name='SendDataRequestEvent',
                )
            f_store_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SendDataRequestEvent(
            store_id=not_none(f_store_id),
        ))

    def __repr__(self) -> str:
        return "SendDataRequestEvent(" + repr(self.export_data()) + ")"


class BinaryDataEvent:
    """
    Binary event
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.binarystore:binary-data'
    SHORT_EVENT_NAME = 'binary-data'


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
