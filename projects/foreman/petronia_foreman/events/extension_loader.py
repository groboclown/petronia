# GENERATED CODE - DO NOT MODIFY
# Created on 2020-11-19T23:28:00.644546

"""
Data structures and marshalling for extension petronia.core.api.extension_loader version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics


from typing import (
    List,
    Optional,
    SupportsFloat,
    SupportsInt,
    Union,
    Dict,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    T,
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.extension_loader'
EXTENSION_VERSION = (1, 0, 0)


class LoadExtensionRequestEvent:
    """
    Request for an extension be loaded into Petronia. The extension loader will
    examine the request and decide whether the extension can be loaded. The
    extension loader will also use its internal settings to determine from where to
    load the extension.
    """
    __slots__ = ('name', 'minimum_version', 'below_version',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:load-extension:request'
    SHORT_EVENT_NAME = 'load-extension:request'

    def __init__(
        self,
        name: str,
        minimum_version: Optional[List[int]],
        below_version: Optional[List[int]],
    ) -> None:
        self.name = name
        self.minimum_version = minimum_version
        self.below_version = below_version

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LoadExtensionRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'minimum_version': None if self.minimum_version is None else list(self.minimum_version),
            'below_version': None if self.below_version is None else list(self.below_version),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionRequestEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionRequestEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionRequestEvent',
                ))
            else:
                f_name = val
        f_minimum_version: Optional[List[int]] = None
        val = data.get('minimum_version')
        if val is not None:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='minimum_version',
                    type='List[int]',
                    name='LoadExtensionRequestEvent',
                ))
            else:
                f_minimum_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='minimum_version',
                            type='int',
                            name='LoadExtensionRequestEvent',
                        ))
                    else:
                        f_minimum_version.append(item)
        f_below_version: Optional[List[int]] = None
        val = data.get('below_version')
        if val is not None:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='below_version',
                    type='List[int]',
                    name='LoadExtensionRequestEvent',
                ))
            else:
                f_below_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='below_version',
                            type='int',
                            name='LoadExtensionRequestEvent',
                        ))
                    else:
                        f_below_version.append(item)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LoadExtensionRequestEvent(
            name=_not_none(f_name),
            minimum_version=f_minimum_version,
            below_version=f_below_version,
        ))

    def __repr__(self) -> str:
        return "LoadExtensionRequestEvent(" + repr(self.export_data()) + ")"


class Arguments:
    """
    (no description)
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            int,
            str,
            float,
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
            int,
            str,
            float,
    ]:
        """The selector value."""
        return self.__value

    def __repr__(self) -> str:
        return 'Arguments(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0912
        """Create the event data structure, ready for marshalling."""
        if self.__name == 'string':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        if self.__name == 'int':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        if self.__name == 'float':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        raise RuntimeError('invalid inner type: ' + repr(self.__name))  # pragma no cover

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Arguments']:  # pylint: disable=R0912,R0911
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
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
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
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
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
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
                selector_name,
                float(val),
            ))
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('Invalid selector name {name} for {nc}'),
            name=selector_name,
            nc='Arguments',
        )


class Error:
    """
    A failure
    """
    __slots__ = ('identifier', 'source', 'message', 'arguments',)

    def __init__(
        self,
        identifier: str,
        source: Optional[str],
        message: str,
        arguments: List[Arguments],
    ) -> None:
        self.identifier = identifier
        self.source = source
        self.message = message
        self.arguments = arguments

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'source': self.source,
            'message': self.message,
            'arguments': [v.export_data() for v in self.arguments],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Error']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_identifier: Optional[str] = None
        val = data.get('identifier')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='Error',
                ))
            else:
                f_identifier = val
        f_source: Optional[str] = None
        val = data.get('source')
        if val is not None:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source',
                    type='str',
                    name='Error',
                ))
            else:
                f_source = val
        f_message: Optional[str] = None
        val = data.get('message')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='message',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='message',
                    type='str',
                    name='Error',
                ))
            else:
                f_message = val
        f_arguments: Optional[List[Arguments]] = None
        val = data.get('arguments')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='arguments',
                name='Error',
            ))
        else:
            f_arguments = []
            for item in val:
                parsed_arguments = Arguments.parse_data(item)
                if parsed_arguments.has_error:
                    errors.append(parsed_arguments.forward())
                else:
                    f_arguments.append(parsed_arguments.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Error(
            identifier=_not_none(f_identifier),
            source=f_source,
            message=_not_none(f_message),
            arguments=_not_none(f_arguments),
        ))

    def __repr__(self) -> str:
        return "Error(" + repr(self.export_data()) + ")"


class LoadExtensionFailedEvent:
    """
    The request to load an extension was denied or the extension failed to load.
    """
    __slots__ = ('name', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:load-extension:failed'
    SHORT_EVENT_NAME = 'load-extension:failed'

    def __init__(
        self,
        name: str,
        error: Error,
    ) -> None:
        self.name = name
        self.error = error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LoadExtensionFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionFailedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionFailedEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionFailedEvent',
                ))
            else:
                f_name = val
        f_error: Optional[Error] = None
        val = data.get('error')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='LoadExtensionFailedEvent',
            ))
        else:
            parsed_error = Error.parse_data(val)
            if parsed_error.has_error:
                errors.append(parsed_error.forward())
            else:
                # Value, not result, because it could be optional...
                f_error = parsed_error.value
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LoadExtensionFailedEvent(
            name=_not_none(f_name),
            error=_not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "LoadExtensionFailedEvent(" + repr(self.export_data()) + ")"


class LoadExtensionSuccessEvent:
    """
    The request to load the extension succeeded. Other events related to the
    extension loading may be sent, but that is in a different life cycle.
    """
    __slots__ = ('name', 'version',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:load-extension:success'
    SHORT_EVENT_NAME = 'load-extension:success'

    def __init__(
        self,
        name: str,
        version: List[int],
    ) -> None:
        self.name = name
        self.version = version

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LoadExtensionSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionSuccessEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionSuccessEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionSuccessEvent',
                ))
            else:
                f_name = val
        f_version: Optional[List[int]] = None
        val = data.get('version')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='version',
                name='LoadExtensionSuccessEvent',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LoadExtensionSuccessEvent',
                ))
            else:
                f_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='version',
                            type='int',
                            name='LoadExtensionSuccessEvent',
                        ))
                    else:
                        f_version.append(item)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LoadExtensionSuccessEvent(
            name=_not_none(f_name),
            version=_not_none(f_version),
        ))

    def __repr__(self) -> str:
        return "LoadExtensionSuccessEvent(" + repr(self.export_data()) + ")"


class LauncherLoadExtensionEvent:
    """
    Requests a launcher to load an extension. The target of the request is the
    launcher started by a "start-launcher" event, and that declares the permissions
    that the extension can use. This request does not have its own event responses;
    instead, the loaded extension should use the standard extension event lifecycle.
    """
    __slots__ = ('name', 'version', 'location',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:launcher-load-extension'
    SHORT_EVENT_NAME = 'launcher-load-extension'

    def __init__(
        self,
        name: str,
        version: List[int],
        location: str,
    ) -> None:
        self.name = name
        self.version = version
        self.location = location

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LauncherLoadExtensionEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
            'location': self.location,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherLoadExtensionEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LauncherLoadExtensionEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherLoadExtensionEvent',
                ))
            else:
                f_name = val
        f_version: Optional[List[int]] = None
        val = data.get('version')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='version',
                name='LauncherLoadExtensionEvent',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LauncherLoadExtensionEvent',
                ))
            else:
                f_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='version',
                            type='int',
                            name='LauncherLoadExtensionEvent',
                        ))
                    else:
                        f_version.append(item)
        f_location: Optional[str] = None
        val = data.get('location')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='location',
                name='LauncherLoadExtensionEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='location',
                    type='str',
                    name='LauncherLoadExtensionEvent',
                ))
            else:
                f_location = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LauncherLoadExtensionEvent(
            name=_not_none(f_name),
            version=_not_none(f_version),
            location=_not_none(f_location),
        ))

    def __repr__(self) -> str:
        return "LauncherLoadExtensionEvent(" + repr(self.export_data()) + ")"


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
