# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:14.770593+00:00

"""
Data structures and marshalling for extension petronia.core.api.native.hotkey version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods


from typing import (
    Union,
    Dict,
    Any,
    SupportsInt,
    List,
    Optional,
    SupportsFloat,
    cast,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    not_none,
    StdRet,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.native.hotkey'
EXTENSION_VERSION = (1, 0, 0)


class BoundHotkey:
    """
    A list of key sequences that construe a bound hotkey. This does not include the
    master sequence.
    """
    __slots__ = ('keys',)

    def __init__(
        self,
        keys: List[str],
    ) -> None:
        self.keys = keys

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'keys': list(self.keys),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundHotkey']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('keys')
        f_keys: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='keys',
                name='BoundHotkey',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='keys',
                    type='List[str]',
                    name='BoundHotkey',
                )
            f_keys = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='keys',
                        type='str',
                        name='BoundHotkey',
                    )
                f_keys.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(BoundHotkey(
            keys=not_none(f_keys),
        ))

    def __repr__(self) -> str:
        return "BoundHotkey(" + repr(self.export_data()) + ")"


class SetHotkeyBindingsEvent:
    """
    Set the hotkey bindings. This will reset the existing hotkey settings. If the
    request is invalid, an failed event is sent, otherwise a success is sent.
    """
    __slots__ = ('master', 'bound',)
    FULL_EVENT_NAME = 'petronia.core.api.native.hotkey:set-hotkey-bindings'
    SHORT_EVENT_NAME = 'set-hotkey-bindings'

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.hotkey:bindings'
    UNIQUE_TARGET_REL = 'bindings'

    def __init__(
        self,
        master: str,
        bound: List[BoundHotkey],
    ) -> None:
        self.master = master
        self.bound = bound

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetHotkeyBindingsEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'master': self.master,
            'bound': [v.export_data() for v in self.bound],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetHotkeyBindingsEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('master')
        f_master: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='master',
                name='SetHotkeyBindingsEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='master',
                    type='str',
                    name='SetHotkeyBindingsEvent',
                )
            f_master = val
        val = data.get('bound')
        f_bound: List[BoundHotkey]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='bound',
                name='SetHotkeyBindingsEvent',
            )
        else:
            f_bound = []
            for item in val:
                parsed_bound = BoundHotkey.parse_data(item)
                if parsed_bound.has_error:
                    return parsed_bound.forward()
                f_bound.append(parsed_bound.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetHotkeyBindingsEvent(
            master=not_none(f_master),
            bound=not_none(f_bound),
        ))

    def __repr__(self) -> str:
        return "SetHotkeyBindingsEvent(" + repr(self.export_data()) + ")"


class SetHotkeyBindingsSuccessEvent:
    """
    (no description)
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.native.hotkey:set-hotkey-bindings:success'
    SHORT_EVENT_NAME = 'set-hotkey-bindings:success'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetHotkeyBindingsSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['SetHotkeyBindingsSuccessEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(SetHotkeyBindingsSuccessEvent())

    def __repr__(self) -> str:
        return "SetHotkeyBindingsSuccessEvent(" + repr(self.export_data()) + ")"


class MessageArgumentValue:
    """
    A replacement value for a named argument in the message.
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            List[str],
            float,
            List[datetime.datetime],
            List[bool],
            List[int],
            List[float],
            str,
            datetime.datetime,
            bool,
            int,
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
            List[str],
            float,
            List[datetime.datetime],
            List[bool],
            List[int],
            List[float],
            str,
            datetime.datetime,
            bool,
            int,
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


class MasterHotkeySequenceProblem:
    """
    A problem with the hotkey master sequence.
    """
    __slots__ = ('master', 'error',)

    def __init__(
        self,
        master: str,
        error: Error,
    ) -> None:
        self.master = master
        self.error = error

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'master': self.master,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MasterHotkeySequenceProblem']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('master')
        f_master: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='master',
                name='MasterHotkeySequenceProblem',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='master',
                    type='str',
                    name='MasterHotkeySequenceProblem',
                )
            f_master = val
        val = data.get('error')
        f_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='MasterHotkeySequenceProblem',
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
        return StdRet.pass_ok(MasterHotkeySequenceProblem(
            master=not_none(f_master),
            error=not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "MasterHotkeySequenceProblem(" + repr(self.export_data()) + ")"


class BoundHotkeyProblem:
    """
    A problem with a bound hotkey.
    """
    __slots__ = ('hotkey', 'error',)

    def __init__(
        self,
        hotkey: BoundHotkey,
        error: Error,
    ) -> None:
        self.hotkey = hotkey
        self.error = error

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'hotkey': self.hotkey.export_data(),
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['BoundHotkeyProblem']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('hotkey')
        f_hotkey: BoundHotkey
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='hotkey',
                name='BoundHotkeyProblem',
            )
        else:
            parsed_hotkey = BoundHotkey.parse_data(val)
            if parsed_hotkey.has_error:
                return parsed_hotkey.forward()
            if parsed_hotkey.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='hotkey',
                )
            f_hotkey = parsed_hotkey.result
        val = data.get('error')
        f_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='BoundHotkeyProblem',
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
        return StdRet.pass_ok(BoundHotkeyProblem(
            hotkey=not_none(f_hotkey),
            error=not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "BoundHotkeyProblem(" + repr(self.export_data()) + ")"


class SetHotkeyBindingsFailedEvent:
    """
    If the state of `hotkey-bindings` is configured incorrectly, this error event is
    sent to describe what the error was, and what was the cause of the error.
    """
    __slots__ = ('master_problem', 'bound_problems',)
    FULL_EVENT_NAME = 'petronia.core.api.native.hotkey:set-hotkey-bindings:failed'
    SHORT_EVENT_NAME = 'set-hotkey-bindings:failed'

    def __init__(
        self,
        master_problem: Optional[MasterHotkeySequenceProblem],
        bound_problems: Optional[List[BoundHotkeyProblem]],
    ) -> None:
        self.master_problem = master_problem
        self.bound_problems = bound_problems

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetHotkeyBindingsFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'master_problem': None if self.master_problem is None else self.master_problem.export_data(),
            'bound_problems': None if self.bound_problems is None else [v.export_data() for v in self.bound_problems],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetHotkeyBindingsFailedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('master_problem')
        f_master_problem: Optional[MasterHotkeySequenceProblem] = None
        if val is not None:
            parsed_master_problem = MasterHotkeySequenceProblem.parse_data(val)
            if parsed_master_problem.has_error:
                return parsed_master_problem.forward()
            # Value, not result, because it could be optional...
            f_master_problem = parsed_master_problem.value
        val = data.get('bound_problems')
        f_bound_problems: Optional[List[BoundHotkeyProblem]] = None
        if val is not None:
            f_bound_problems = []
            for item in val:
                parsed_bound_problems = BoundHotkeyProblem.parse_data(item)
                if parsed_bound_problems.has_error:
                    return parsed_bound_problems.forward()
                f_bound_problems.append(parsed_bound_problems.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetHotkeyBindingsFailedEvent(
            master_problem=f_master_problem,
            bound_problems=f_bound_problems,
        ))

    def __repr__(self) -> str:
        return "SetHotkeyBindingsFailedEvent(" + repr(self.export_data()) + ")"


class HotkeyPressedEvent:
    """
    The user pressed a bound hotkey. The pressed sequence (not including the master
    sequence) is returned. The target is always the unique target id.
    """
    __slots__ = ('hotkey',)
    FULL_EVENT_NAME = 'petronia.core.api.native.hotkey:hotkey-pressed'
    SHORT_EVENT_NAME = 'hotkey-pressed'

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.hotkey:press'
    UNIQUE_TARGET_REL = 'press'

    def __init__(
        self,
        hotkey: BoundHotkey,
    ) -> None:
        self.hotkey = hotkey

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return HotkeyPressedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'hotkey': self.hotkey.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HotkeyPressedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('hotkey')
        f_hotkey: BoundHotkey
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='hotkey',
                name='HotkeyPressedEvent',
            )
        else:
            parsed_hotkey = BoundHotkey.parse_data(val)
            if parsed_hotkey.has_error:
                return parsed_hotkey.forward()
            if parsed_hotkey.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='hotkey',
                )
            f_hotkey = parsed_hotkey.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HotkeyPressedEvent(
            hotkey=not_none(f_hotkey),
        ))

    def __repr__(self) -> str:
        return "HotkeyPressedEvent(" + repr(self.export_data()) + ")"


class HotkeyBindingsState:
    """
    Hotkey events sent out by the native extension depend upon the binding
    configuration.
    """
    __slots__ = ('master', 'bound',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.native.hotkey:hotkey-bindings'
    UNIQUE_TARGET_REL = 'petronia.core.api.native.hotkey:hotkey-bindings'

    def __init__(
        self,
        master: str,
        bound: List[BoundHotkey],
    ) -> None:
        self.master = master
        self.bound = bound

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'master': self.master,
            'bound': [v.export_data() for v in self.bound],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['HotkeyBindingsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('master')
        f_master: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='master',
                name='HotkeyBindingsState',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='master',
                    type='str',
                    name='HotkeyBindingsState',
                )
            f_master = val
        val = data.get('bound')
        f_bound: List[BoundHotkey]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='bound',
                name='HotkeyBindingsState',
            )
        else:
            f_bound = []
            for item in val:
                parsed_bound = BoundHotkey.parse_data(item)
                if parsed_bound.has_error:
                    return parsed_bound.forward()
                f_bound.append(parsed_bound.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(HotkeyBindingsState(
            master=not_none(f_master),
            bound=not_none(f_bound),
        ))

    def __repr__(self) -> str:
        return "HotkeyBindingsState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
