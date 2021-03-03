# GENERATED CODE - DO NOT MODIFY
# Created on 2021-03-02T17:03:03.107705+00:00

"""
Data structures and marshalling for extension petronia.core.protocol.logging version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Optional,
    cast,
    Any,
    Dict,
    SupportsFloat,
    SupportsInt,
    List,
    Union,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    not_none,
    collect_errors_from,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.protocol.logging'
EXTENSION_VERSION = (1, 0, 0)


class MessageArgumentValue:
    """
    A replacement value for a named argument in the message.
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            float,
            List[datetime.datetime],
            int,
            List[str],
            datetime.datetime,
            List[float],
            List[bool],
            str,
            bool,
            List[int],
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
            float,
            List[datetime.datetime],
            int,
            List[str],
            datetime.datetime,
            List[float],
            List[bool],
            str,
            bool,
            List[int],
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
        selector_name = data.get('^')
        val = data.get('$')
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('selector value must have ^ and $ keys'),
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


class LogEvent:
    """
    A request to log a message. This can be publicly received, so that any extension
    can listen to logging messages. For this reason, nothing private should be sent.
    """
    __slots__ = ('scope', 'messages',)
    FULL_EVENT_NAME = 'petronia.core.protocol.logging:log'
    SHORT_EVENT_NAME = 'log'

    UNIQUE_TARGET_FQN = 'petronia.core.protocol.logging:log'
    UNIQUE_TARGET_REL = 'log'

    def __init__(
        self,
        scope: str,
        messages: List[LocalizableMessage],
    ) -> None:
        self.scope = scope
        self.messages = messages

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LogEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'scope': self.scope,
            'messages': [v.export_data() for v in self.messages],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LogEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('scope')
        f_scope: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='scope',
                name='LogEvent',
            )
        else:
            if val not in ('info','debug','warning','verbose', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='scope',
                    type='str',
                    name='LogEvent',
                )
            f_scope = val
        val = data.get('messages')
        f_messages: List[LocalizableMessage]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='messages',
                name='LogEvent',
            )
        else:
            f_messages = []
            for item in val:
                parsed_messages = LocalizableMessage.parse_data(item)
                if parsed_messages.has_error:
                    return parsed_messages.forward()
                f_messages.append(parsed_messages.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LogEvent(
            scope=not_none(f_scope),
            messages=not_none(f_messages),
        ))

    def __repr__(self) -> str:
        return "LogEvent(" + repr(self.export_data()) + ")"


class Error:
    """
    A description of a failure.
    """
    __slots__ = ('identifier', 'categories', 'source', 'messages',)

    def __init__(
        self,
        identifier: str,
        categories: List[str],
        source: Optional[str],
        messages: List[LocalizableMessage],
    ) -> None:
        self.identifier = identifier
        self.categories = categories
        self.source = source
        self.messages = messages

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'categories': list(self.categories),
            'source': self.source,
            'messages': [v.export_data() for v in self.messages],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Error']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('identifier')
        f_identifier: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Error',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='Error',
                )
            f_identifier = val
        val = data.get('categories')
        f_categories: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='categories',
                name='Error',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='categories',
                    type='List[str]',
                    name='Error',
                )
            f_categories = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='categories',
                        type='str',
                        name='Error',
                    )
                f_categories.append(item)
        val = data.get('source')
        f_source: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source',
                    type='str',
                    name='Error',
                )
            f_source = val
        val = data.get('messages')
        f_messages: List[LocalizableMessage]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='messages',
                name='Error',
            )
        else:
            f_messages = []
            for item in val:
                parsed_messages = LocalizableMessage.parse_data(item)
                if parsed_messages.has_error:
                    return parsed_messages.forward()
                f_messages.append(parsed_messages.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Error(
            identifier=not_none(f_identifier),
            categories=not_none(f_categories),
            source=f_source,
            messages=not_none(f_messages),
        ))

    def __repr__(self) -> str:
        return "Error(" + repr(self.export_data()) + ")"


class SystemErrorEvent:
    """
    Report an error that's caused by Petronia itself (or an extension), rather than
    something the user did.
    """
    __slots__ = ('error',)
    FULL_EVENT_NAME = 'petronia.core.protocol.logging:system-error'
    SHORT_EVENT_NAME = 'system-error'

    UNIQUE_TARGET_FQN = 'petronia.core.protocol.logging:error'
    UNIQUE_TARGET_REL = 'error'

    def __init__(
        self,
        error: Error,
    ) -> None:
        self.error = error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SystemErrorEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SystemErrorEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('error')
        f_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='SystemErrorEvent',
            )
        else:
            parsed_error = Error.parse_data(val)
            if parsed_error.has_error:
                return parsed_error.forward()
            if parsed_error.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='error',
                )
            f_error = parsed_error.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SystemErrorEvent(
            error=not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "SystemErrorEvent(" + repr(self.export_data()) + ")"


class UserErrorEvent:
    """
    Report an error that's caused by the end user, such as a mis-configuration or
    out-of-disk space.
    """
    __slots__ = ('user_error',)
    FULL_EVENT_NAME = 'petronia.core.protocol.logging:user-error'
    SHORT_EVENT_NAME = 'user-error'

    UNIQUE_TARGET_FQN = 'petronia.core.protocol.logging:error'
    UNIQUE_TARGET_REL = 'error'

    def __init__(
        self,
        user_error: Error,
    ) -> None:
        self.user_error = user_error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return UserErrorEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'user_error': self.user_error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['UserErrorEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('user_error')
        f_user_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='user_error',
                name='UserErrorEvent',
            )
        else:
            parsed_user_error = Error.parse_data(val)
            if parsed_user_error.has_error:
                return parsed_user_error.forward()
            if parsed_user_error.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='user_error',
                )
            f_user_error = parsed_user_error.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(UserErrorEvent(
            user_error=not_none(f_user_error),
        ))

    def __repr__(self) -> str:
        return "UserErrorEvent(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
