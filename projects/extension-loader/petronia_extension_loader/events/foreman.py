# GENERATED CODE - DO NOT MODIFY
# Created on 2021-01-06T22:34:13.677947

"""
Data structures and marshalling for extension petronia.core.api.foreman version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint: disable=too-many-lines,line-too-long


from typing import (
    Dict,
    Any,
    SupportsFloat,
    Optional,
    Union,
    List,
    SupportsInt,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    T,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.foreman'
EXTENSION_VERSION = (1, 0, 0)


class Permissions:
    """
    (no description)
    """
    __slots__ = ('action', 'resources',)

    def __init__(
        self,
        action: str,
        resources: List[str],
    ) -> None:
        self.action = action
        self.resources = resources

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'action': self.action,
            'resources': list(self.resources),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Permissions']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_action: Optional[str] = None
        val = data.get('action')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='action',
                name='Permissions',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='action',
                    type='str',
                    name='Permissions',
                ))
            else:
                f_action = val
        f_resources: Optional[List[str]] = None
        val = data.get('resources')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='resources',
                name='Permissions',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='resources',
                    type='List[str]',
                    name='Permissions',
                ))
            else:
                f_resources = []
                for item in val:
                    if not isinstance(item, str):
                        errors.append(StdRet.pass_errmsg(
                            STANDARD_PETRONIA_CATALOG,
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='resources',
                            type='str',
                            name='Permissions',
                        ))
                    else:
                        f_resources.append(item)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Permissions(
            action=_not_none(f_action),
            resources=_not_none(f_resources),
        ))

    def __repr__(self) -> str:
        return "Permissions(" + repr(self.export_data()) + ")"


class StartLauncherRequestEvent:
    """
    Request that the foreman process start a new launcher.
    """
    __slots__ = ('identifier', 'launcher', 'permissions',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:start-launcher:request'
    SHORT_EVENT_NAME = 'start-launcher:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.foreman:launcher'
    UNIQUE_TARGET_REL = 'launcher'

    def __init__(
        self,
        identifier: str,
        launcher: str,
        permissions: List[Permissions],
    ) -> None:
        self.identifier = identifier
        self.launcher = launcher
        self.permissions = permissions

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StartLauncherRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'launcher': self.launcher,
            'permissions': [v.export_data() for v in self.permissions],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StartLauncherRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='StartLauncherRequestEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='StartLauncherRequestEvent',
                ))
            else:
                f_identifier = val
        f_launcher: Optional[str] = None
        val = data.get('launcher')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='launcher',
                name='StartLauncherRequestEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='launcher',
                    type='str',
                    name='StartLauncherRequestEvent',
                ))
            else:
                f_launcher = val
        f_permissions: Optional[List[Permissions]] = None
        val = data.get('permissions')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='permissions',
                name='StartLauncherRequestEvent',
            ))
        else:
            f_permissions = []
            for item in val:
                parsed_permissions = Permissions.parse_data(item)
                if parsed_permissions.has_error:
                    errors.append(parsed_permissions.forward())
                else:
                    f_permissions.append(parsed_permissions.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StartLauncherRequestEvent(
            identifier=_not_none(f_identifier),
            launcher=_not_none(f_launcher),
            permissions=_not_none(f_permissions),
        ))

    def __repr__(self) -> str:
        return "StartLauncherRequestEvent(" + repr(self.export_data()) + ")"


class StartLauncherSuccessEvent:
    """
    Report that a new launcher now exists and is ready to accept extensions.
    """
    __slots__ = ('identifier', 'target_id',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:start-launcher:success'
    SHORT_EVENT_NAME = 'start-launcher:success'

    def __init__(
        self,
        identifier: str,
        target_id: str,
    ) -> None:
        self.identifier = identifier
        self.target_id = target_id

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StartLauncherSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'target_id': self.target_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StartLauncherSuccessEvent']:  # pylint: disable=R0912,R0911
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
                name='StartLauncherSuccessEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='StartLauncherSuccessEvent',
                ))
            else:
                f_identifier = val
        f_target_id: Optional[str] = None
        val = data.get('target_id')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target_id',
                name='StartLauncherSuccessEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='StartLauncherSuccessEvent',
                ))
            else:
                f_target_id = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StartLauncherSuccessEvent(
            identifier=_not_none(f_identifier),
            target_id=_not_none(f_target_id),
        ))

    def __repr__(self) -> str:
        return "StartLauncherSuccessEvent(" + repr(self.export_data()) + ")"


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
            float,
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
            int,
            float,
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


class StartLauncherFailedEvent:
    """
    Report that the requested launcher could not be started.
    """
    __slots__ = ('identifier', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:start-launcher:failed'
    SHORT_EVENT_NAME = 'start-launcher:failed'

    def __init__(
        self,
        identifier: str,
        error: Error,
    ) -> None:
        self.identifier = identifier
        self.error = error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StartLauncherFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StartLauncherFailedEvent']:  # pylint: disable=R0912,R0911
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
                name='StartLauncherFailedEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='StartLauncherFailedEvent',
                ))
            else:
                f_identifier = val
        f_error: Optional[Error] = None
        val = data.get('error')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='StartLauncherFailedEvent',
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
        return StdRet.pass_ok(StartLauncherFailedEvent(
            identifier=_not_none(f_identifier),
            error=_not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "StartLauncherFailedEvent(" + repr(self.export_data()) + ")"


class LauncherLoadExtensionRequestEvent:
    """
    Requests a launcher to load an extension. This event's target id is the launcher
    target-id returned by a "start-launcher:success" event, and that declares the
    permissions that the extension can use.
    """
    __slots__ = ('name', 'version', 'location', 'configuration',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-load-extension:request'
    SHORT_EVENT_NAME = 'launcher-load-extension:request'

    def __init__(
        self,
        name: str,
        version: List[int],
        location: str,
        configuration: Optional[str],
    ) -> None:
        self.name = name
        self.version = version
        self.location = location
        self.configuration = configuration

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LauncherLoadExtensionRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
            'location': self.location,
            'configuration': self.configuration,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherLoadExtensionRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherLoadExtensionRequestEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherLoadExtensionRequestEvent',
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
                name='LauncherLoadExtensionRequestEvent',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LauncherLoadExtensionRequestEvent',
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
                            name='LauncherLoadExtensionRequestEvent',
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
                name='LauncherLoadExtensionRequestEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='location',
                    type='str',
                    name='LauncherLoadExtensionRequestEvent',
                ))
            else:
                f_location = val
        f_configuration: Optional[str] = None
        val = data.get('configuration')
        if val is not None:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='configuration',
                    type='str',
                    name='LauncherLoadExtensionRequestEvent',
                ))
            else:
                f_configuration = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LauncherLoadExtensionRequestEvent(
            name=_not_none(f_name),
            version=_not_none(f_version),
            location=_not_none(f_location),
            configuration=f_configuration,
        ))

    def __repr__(self) -> str:
        return "LauncherLoadExtensionRequestEvent(" + repr(self.export_data()) + ")"


class LauncherLoadExtensionSuccessEvent:
    """
    Signals a successful request to load the extension. Further events in the
    extension's lifecycle will be generated by the extension itself. The source-id
    is the launcher that loaded the extension.
    """
    __slots__ = ('name',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-load-extension:success'
    SHORT_EVENT_NAME = 'launcher-load-extension:success'

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LauncherLoadExtensionSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherLoadExtensionSuccessEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherLoadExtensionSuccessEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherLoadExtensionSuccessEvent',
                ))
            else:
                f_name = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LauncherLoadExtensionSuccessEvent(
            name=_not_none(f_name),
        ))

    def __repr__(self) -> str:
        return "LauncherLoadExtensionSuccessEvent(" + repr(self.export_data()) + ")"


class LauncherLoadExtensionFailedEvent:
    """
    Report that the requested extension could not be loaded by the loader. The
    source-id is the launcher that loaded the extension.
    """
    __slots__ = ('name', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-load-extension:failed'
    SHORT_EVENT_NAME = 'launcher-load-extension:failed'

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
        return LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherLoadExtensionFailedEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherLoadExtensionFailedEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherLoadExtensionFailedEvent',
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
                name='LauncherLoadExtensionFailedEvent',
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
        return StdRet.pass_ok(LauncherLoadExtensionFailedEvent(
            name=_not_none(f_name),
            error=_not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "LauncherLoadExtensionFailedEvent(" + repr(self.export_data()) + ")"


class Events:
    """
    A target event for an extension listening.
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


class ExtensionAddEventListenerEvent:
    """
    Request from the extension loader to add an event listener for an extension.
    Failures happen silently (no response back is made). The target_id must match
    with the ID for the launcher that owns the extension.
    """
    __slots__ = ('extension_name', 'events',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:extension-add-event-listener'
    SHORT_EVENT_NAME = 'extension-add-event-listener'

    def __init__(
        self,
        extension_name: str,
        events: List[Events],
    ) -> None:
        self.extension_name = extension_name
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionAddEventListenerEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'extension_name': self.extension_name,
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionAddEventListenerEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_extension_name: Optional[str] = None
        val = data.get('extension_name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='extension_name',
                name='ExtensionAddEventListenerEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='extension_name',
                    type='str',
                    name='ExtensionAddEventListenerEvent',
                ))
            else:
                f_extension_name = val
        f_events: Optional[List[Events]] = None
        val = data.get('events')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='ExtensionAddEventListenerEvent',
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
        return StdRet.pass_ok(ExtensionAddEventListenerEvent(
            extension_name=_not_none(f_extension_name),
            events=_not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "ExtensionAddEventListenerEvent(" + repr(self.export_data()) + ")"


class ExtensionRemoveEventListenerEvent:
    """
    Request from the extension loader to remove an event listener for an extension.
    Failures happen silently (no response back is made). The target_id must match
    with the ID for the launcher that owns the extension.
    """
    __slots__ = ('extension_name', 'events',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:extension-remove-event-listener'
    SHORT_EVENT_NAME = 'extension-remove-event-listener'

    def __init__(
        self,
        extension_name: str,
        events: List[Events],
    ) -> None:
        self.extension_name = extension_name
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'extension_name': self.extension_name,
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionRemoveEventListenerEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_extension_name: Optional[str] = None
        val = data.get('extension_name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='extension_name',
                name='ExtensionRemoveEventListenerEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='extension_name',
                    type='str',
                    name='ExtensionRemoveEventListenerEvent',
                ))
            else:
                f_extension_name = val
        f_events: Optional[List[Events]] = None
        val = data.get('events')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='ExtensionRemoveEventListenerEvent',
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
        return StdRet.pass_ok(ExtensionRemoveEventListenerEvent(
            extension_name=_not_none(f_extension_name),
            events=_not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "ExtensionRemoveEventListenerEvent(" + repr(self.export_data()) + ")"


class RestartEvent:
    """
    Force the Petronia extensions to restart themselves. This can only be sent
    through "internal" extensions because normal operation requires shutdown phases.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.foreman:restart'
    SHORT_EVENT_NAME = 'restart'

    UNIQUE_TARGET_FQN = 'petronia.core.api.foreman:restart'
    UNIQUE_TARGET_REL = 'restart'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return RestartEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['RestartEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(RestartEvent())

    def __repr__(self) -> str:
        return "RestartEvent(" + repr(self.export_data()) + ")"


class StopEvent:
    """
    Terminate Petronia. This can only be sent through "internal" extensions because
    normal operation requires shutdown phases.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.foreman:stop'
    SHORT_EVENT_NAME = 'stop'

    UNIQUE_TARGET_FQN = 'petronia.core.api.foreman:stop'
    UNIQUE_TARGET_REL = 'stop'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StopEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['StopEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(StopEvent())

    def __repr__(self) -> str:
        return "StopEvent(" + repr(self.export_data()) + ")"


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
