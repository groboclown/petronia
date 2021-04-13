# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.foreman version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Optional,
    Union,
    SupportsInt,
    cast,
    Dict,
    SupportsFloat,
    Any,
    List,
)
import datetime
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    not_none,
)

EXTENSION_NAME = 'petronia.core.api.foreman'
EXTENSION_VERSION = (1, 0, 0)


class SendEventAccess:
    """
    Permissions for sending an event.
    """
    __slots__ = ('event_ids', 'source_id_prefixes',)

    def __init__(
        self,
        event_ids: List[str],
        source_id_prefixes: List[str],
    ) -> None:
        self.event_ids = event_ids
        self.source_id_prefixes = source_id_prefixes

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'event_ids': list(self.event_ids),
            'source_id_prefixes': list(self.source_id_prefixes),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SendEventAccess']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('event_ids')
        f_event_ids: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='event_ids',
                name='SendEventAccess',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='event_ids',
                    type='List[str]',
                    name='SendEventAccess',
                )
            f_event_ids = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='event_ids',
                        type='str',
                        name='SendEventAccess',
                    )
                f_event_ids.append(item)
        val = data.get('source_id_prefixes')
        f_source_id_prefixes: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='source_id_prefixes',
                name='SendEventAccess',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source_id_prefixes',
                    type='List[str]',
                    name='SendEventAccess',
                )
            f_source_id_prefixes = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='source_id_prefixes',
                        type='str',
                        name='SendEventAccess',
                    )
                f_source_id_prefixes.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SendEventAccess(
            event_ids=not_none(f_event_ids),
            source_id_prefixes=not_none(f_source_id_prefixes),
        ))

    def __repr__(self) -> str:
        return "SendEventAccess(" + repr(self.export_data()) + ")"


class ExtensionPermission:
    """
    An action and collection of resources that can perform the action.
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
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionPermission']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('action')
        f_action: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='action',
                name='ExtensionPermission',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='action',
                    type='str',
                    name='ExtensionPermission',
                )
            f_action = val
        val = data.get('resources')
        f_resources: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='resources',
                name='ExtensionPermission',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='resources',
                    type='List[str]',
                    name='ExtensionPermission',
                )
            f_resources = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='resources',
                        type='str',
                        name='ExtensionPermission',
                    )
                f_resources.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ExtensionPermission(
            action=not_none(f_action),
            resources=not_none(f_resources),
        ))

    def __repr__(self) -> str:
        return "ExtensionPermission(" + repr(self.export_data()) + ")"


class LauncherStartExtensionRequestEvent:
    """
    Requests a launcher to load an extension. This event's target id is the launcher
    target-id returned by a "start-launcher:success" event, and that declares the
    permissions that the extension can use.
    """
    __slots__ = ('name', 'version', 'location', 'runtime', 'send_access', 'configuration', 'permissions',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-start-extension:request'
    SHORT_EVENT_NAME = 'launcher-start-extension:request'

    UNIQUE_TARGET_FQN = 'petronia.core.api.foreman:launcher'
    UNIQUE_TARGET_REL = 'launcher'

    def __init__(
        self,
        name: str,
        version: List[int],
        location: List[str],
        runtime: str,
        send_access: SendEventAccess,
        configuration: Optional[str],
        permissions: List[ExtensionPermission],
    ) -> None:
        self.name = name
        self.version = version
        self.location = location
        self.runtime = runtime
        self.send_access = send_access
        self.configuration = configuration
        self.permissions = permissions

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LauncherStartExtensionRequestEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
            'location': list(self.location),
            'runtime': self.runtime,
            'send_access': self.send_access.export_data(),
            'configuration': self.configuration,
            'permissions': [v.export_data() for v in self.permissions],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherStartExtensionRequestEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherStartExtensionRequestEvent',
                )
            f_name = val
        val = data.get('version')
        f_version: List[int]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='version',
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LauncherStartExtensionRequestEvent',
                )
            f_version = []
            for item in val:
                if not isinstance(item, int):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='version',
                        type='int',
                        name='LauncherStartExtensionRequestEvent',
                    )
                f_version.append(item)
        val = data.get('location')
        f_location: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='location',
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='location',
                    type='List[str]',
                    name='LauncherStartExtensionRequestEvent',
                )
            f_location = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='location',
                        type='str',
                        name='LauncherStartExtensionRequestEvent',
                    )
                f_location.append(item)
        val = data.get('runtime')
        f_runtime: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='runtime',
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='runtime',
                    type='str',
                    name='LauncherStartExtensionRequestEvent',
                )
            f_runtime = val
        val = data.get('send_access')
        f_send_access: SendEventAccess
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='send_access',
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            parsed_send_access = SendEventAccess.parse_data(val)
            if parsed_send_access.has_error:
                return parsed_send_access.forward()
            if parsed_send_access.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='send_access',
                )
            f_send_access = parsed_send_access.result
        val = data.get('configuration')
        f_configuration: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='configuration',
                    type='str',
                    name='LauncherStartExtensionRequestEvent',
                )
            f_configuration = val
        val = data.get('permissions')
        f_permissions: List[ExtensionPermission]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='permissions',
                name='LauncherStartExtensionRequestEvent',
            )
        else:
            f_permissions = []
            for item in val:
                parsed_permissions = ExtensionPermission.parse_data(item)
                if parsed_permissions.has_error:
                    return parsed_permissions.forward()
                f_permissions.append(parsed_permissions.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LauncherStartExtensionRequestEvent(
            name=not_none(f_name),
            version=not_none(f_version),
            location=not_none(f_location),
            runtime=not_none(f_runtime),
            send_access=not_none(f_send_access),
            configuration=f_configuration,
            permissions=not_none(f_permissions),
        ))

    def __repr__(self) -> str:
        return "LauncherStartExtensionRequestEvent(" + repr(self.export_data()) + ")"


class LauncherStartExtensionSuccessEvent:
    """
    Signals a successful request to load the extension. Further events in the
    extension's lifecycle will be generated by the extension itself. The source-id
    is the target that should be directed to for adding or removing listeners.
    """
    __slots__ = ('name',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-start-extension:success'
    SHORT_EVENT_NAME = 'launcher-start-extension:success'

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return LauncherStartExtensionSuccessEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherStartExtensionSuccessEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherStartExtensionSuccessEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherStartExtensionSuccessEvent',
                )
            f_name = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LauncherStartExtensionSuccessEvent(
            name=not_none(f_name),
        ))

    def __repr__(self) -> str:
        return "LauncherStartExtensionSuccessEvent(" + repr(self.export_data()) + ")"


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
            str,
            List[str],
            List[datetime.datetime],
            float,
            datetime.datetime,
            bool,
            List[float],
            List[bool],
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
            List[int],
            str,
            List[str],
            List[datetime.datetime],
            float,
            datetime.datetime,
            bool,
            List[float],
            List[bool],
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


class LauncherStartExtensionFailedEvent:
    """
    Report that the requested extension could not be loaded by the loader. The
    source-id is the launcher that loaded the extension.
    """
    __slots__ = ('name', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:launcher-start-extension:failed'
    SHORT_EVENT_NAME = 'launcher-start-extension:failed'

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
        return LauncherStartExtensionFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherStartExtensionFailedEvent']:  # pylint: disable=R0912,R0911
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
                name='LauncherStartExtensionFailedEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherStartExtensionFailedEvent',
                )
            f_name = val
        val = data.get('error')
        f_error: Error
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='LauncherStartExtensionFailedEvent',
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
        return StdRet.pass_ok(LauncherStartExtensionFailedEvent(
            name=not_none(f_name),
            error=not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "LauncherStartExtensionFailedEvent(" + repr(self.export_data()) + ")"


class EventTarget:
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
    def parse_data(data: Dict[str, Any]) -> StdRet['EventTarget']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('event_id')
        f_event_id: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='event_id',
                    type='str',
                    name='EventTarget',
                )
            f_event_id = val
        val = data.get('target_id')
        f_target_id: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target_id',
                    type='str',
                    name='EventTarget',
                )
            f_target_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(EventTarget(
            event_id=f_event_id,
            target_id=f_target_id,
        ))

    def __repr__(self) -> str:
        return "EventTarget(" + repr(self.export_data()) + ")"


class ExtensionAddEventListenerEvent:
    """
    Request from the extension loader to add an event listener for an extension.
    Failures happen silently (no response back is made). The target_id must match
    the source ID of the event that reported extension start success.
    """
    __slots__ = ('events',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:extension-add-event-listener'
    SHORT_EVENT_NAME = 'extension-add-event-listener'

    def __init__(
        self,
        events: List[EventTarget],
    ) -> None:
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionAddEventListenerEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionAddEventListenerEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('events')
        f_events: List[EventTarget]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='ExtensionAddEventListenerEvent',
            )
        else:
            f_events = []
            for item in val:
                parsed_events = EventTarget.parse_data(item)
                if parsed_events.has_error:
                    return parsed_events.forward()
                f_events.append(parsed_events.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ExtensionAddEventListenerEvent(
            events=not_none(f_events),
        ))

    def __repr__(self) -> str:
        return "ExtensionAddEventListenerEvent(" + repr(self.export_data()) + ")"


class ExtensionRemoveEventListenerEvent:
    """
    Request from the extension loader to remove an event listener for an extension.
    Failures happen silently (no response back is made). The target_id must match
    the source ID of the event that reported extension start success.
    """
    __slots__ = ('events',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:extension-remove-event-listener'
    SHORT_EVENT_NAME = 'extension-remove-event-listener'

    def __init__(
        self,
        events: List[EventTarget],
    ) -> None:
        self.events = events

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ExtensionRemoveEventListenerEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'events': [v.export_data() for v in self.events],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ExtensionRemoveEventListenerEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('events')
        f_events: List[EventTarget]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='events',
                name='ExtensionRemoveEventListenerEvent',
            )
        else:
            f_events = []
            for item in val:
                parsed_events = EventTarget.parse_data(item)
                if parsed_events.has_error:
                    return parsed_events.forward()
                f_events.append(parsed_events.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ExtensionRemoveEventListenerEvent(
            events=not_none(f_events),
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


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
