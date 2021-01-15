# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-15T16:34:23.337077

"""
Data structures and marshalling for extension petronia.core.api.extension_loader version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint: disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements


from typing import (
    Union,
    SupportsInt,
    List,
    Any,
    Optional,
    SupportsFloat,
    Dict,
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
    load the extension. Responses will be sent with a target id matching the
    request's source id.
    """
    __slots__ = ('name', 'minimum_version', 'below_version',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:load-extension:request'
    SHORT_EVENT_NAME = 'load-extension:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.extension_loader:loader'
    UNIQUE_TARGET_REL = 'loader'

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
            float,
            int,
            str,
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
            int,
            str,
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


class Events:
    """
    An event to listen on.
    """
    __slots__ = ('event_id', 'target_id',)

    def __init__(
        self,
        event_id: Optional[str],
        target_id: Optional[str],
    ) -> None:
        self.event_id = event_id
        self.target_id = target_id

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'event_id': self.event_id,
            'target_id': self.target_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Events']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_event_id: Optional[str] = None
        val = data.get('event_id')
        if val is not None:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='event_id',
                    type='str',
                    name='Events',
                ))
            else:
                f_event_id = val
        f_target_id: Optional[str] = None
        val = data.get('target_id')
        if val is not None:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='Events',
                ))
            else:
                f_target_id = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Events(
            event_id=f_event_id,
            target_id=f_target_id,
        ))

    def __repr__(self) -> str:
        return "Events(" + repr(self.export_data()) + ")"


class RegisterExtensionListenersEvent:
    """
    Request by an extension to add a listener of events. The source of the request
    is the extension name.
    """
    __slots__ = ('events',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:register-extension-listeners'
    SHORT_EVENT_NAME = 'register-extension-listeners'

    def __init__(
        self,
        events: List[Events],
    ) -> None:
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return RegisterExtensionListenersEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['RegisterExtensionListenersEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_events: Optional[List[Events]] = None
        val = data.get('events')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='RegisterExtensionListenersEvent',
            ))
        else:
            f_events = []
            for item in val:
                parsed_events = Events.parse_data(item)
                if parsed_events.has_error:
                    errors.append(parsed_events.forward())
                else:
                    f_events.append(parsed_events.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(RegisterExtensionListenersEvent(
            events=_not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "RegisterExtensionListenersEvent(" + repr(self.export_data()) + ")"


class RemoveExtensionListenersEvent:
    """
    Request by an extension to remove a listener of events. The source of the
    request is the extension name.
    """
    __slots__ = ('events',)
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:remove-extension-listeners'
    SHORT_EVENT_NAME = 'remove-extension-listeners'

    def __init__(
        self,
        events: List[Events],
    ) -> None:
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return RemoveExtensionListenersEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['RemoveExtensionListenersEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_events: Optional[List[Events]] = None
        val = data.get('events')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='RemoveExtensionListenersEvent',
            ))
        else:
            f_events = []
            for item in val:
                parsed_events = Events.parse_data(item)
                if parsed_events.has_error:
                    errors.append(parsed_events.forward())
                else:
                    f_events.append(parsed_events.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(RemoveExtensionListenersEvent(
            events=_not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "RemoveExtensionListenersEvent(" + repr(self.export_data()) + ")"


class SystemStartedEvent:
    """
    An "all clear" message indicating that the boot-time declared extensions have
    had their "load-extension:success" messages sent.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.extension_loader:system-started'
    SHORT_EVENT_NAME = 'system-started'

    UNIQUE_TARGET_FQN = 'petronia.core.api.extension_loader:system'
    UNIQUE_TARGET_REL = 'system'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SystemStartedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['SystemStartedEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(SystemStartedEvent())

    def __repr__(self) -> str:
        return "SystemStartedEvent(" + repr(self.export_data()) + ")"


class Extensions:
    """
    Information about a single extension.
    """
    __slots__ = ('name', 'version', 'about', 'description', 'authors', 'licenses',)

    def __init__(
        self,
        name: str,
        version: List[int],
        about: str,
        description: str,
        authors: List[str],
        licenses: List[str],
    ) -> None:
        self.name = name
        self.version = version
        self.about = about
        self.description = description
        self.authors = authors
        self.licenses = licenses

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
            'about': self.about,
            'description': self.description,
            'authors': list(self.authors),
            'licenses': list(self.licenses),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Extensions']:  # pylint: disable=R0912,R0911
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
                name='Extensions',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='Extensions',
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
                name='Extensions',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='Extensions',
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
                            name='Extensions',
                        ))
                    else:
                        f_version.append(item)
        f_about: Optional[str] = None
        val = data.get('about')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='about',
                name='Extensions',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='about',
                    type='str',
                    name='Extensions',
                ))
            else:
                f_about = val
        f_description: Optional[str] = None
        val = data.get('description')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='description',
                name='Extensions',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='description',
                    type='str',
                    name='Extensions',
                ))
            else:
                f_description = val
        f_authors: Optional[List[str]] = None
        val = data.get('authors')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='authors',
                name='Extensions',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='authors',
                    type='List[str]',
                    name='Extensions',
                ))
            else:
                f_authors = []
                for item in val:
                    if not isinstance(item, str):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='authors',
                            type='str',
                            name='Extensions',
                        ))
                    else:
                        f_authors.append(item)
        f_licenses: Optional[List[str]] = None
        val = data.get('licenses')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='licenses',
                name='Extensions',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='licenses',
                    type='List[str]',
                    name='Extensions',
                ))
            else:
                f_licenses = []
                for item in val:
                    if not isinstance(item, str):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='licenses',
                            type='str',
                            name='Extensions',
                        ))
                    else:
                        f_licenses.append(item)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Extensions(
            name=_not_none(f_name),
            version=_not_none(f_version),
            about=_not_none(f_about),
            description=_not_none(f_description),
            authors=_not_none(f_authors),
            licenses=_not_none(f_licenses),
        ))

    def __repr__(self) -> str:
        return "Extensions(" + repr(self.export_data()) + ")"


class ActiveExtensionsState:
    """
    List of active extensions.
    """
    __slots__ = ('extensions',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.extension_loader:active-extensions'
    UNIQUE_TARGET_REL = 'petronia.core.api.extension_loader:active-extensions'

    def __init__(
        self,
        extensions: List[Extensions],
    ) -> None:
        self.extensions = extensions

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'extensions': [v.export_data() for v in self.extensions],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ActiveExtensionsState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_extensions: Optional[List[Extensions]] = None
        val = data.get('extensions')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='extensions',
                name='ActiveExtensionsState',
            ))
        else:
            f_extensions = []
            for item in val:
                parsed_extensions = Extensions.parse_data(item)
                if parsed_extensions.has_error:
                    errors.append(parsed_extensions.forward())
                else:
                    f_extensions.append(parsed_extensions.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ActiveExtensionsState(
            extensions=_not_none(f_extensions),
        ))

    def __repr__(self) -> str:
        return "ActiveExtensionsState(" + repr(self.export_data()) + ")"


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
