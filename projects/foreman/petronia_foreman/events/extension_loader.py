# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-01T18:29:17.075142

"""
Data structures and marshalling for extension petronia.core.api.extension_loader version 1.0.0.
"""

from typing import (
    SupportsFloat,
    Dict,
    Union,
    List,
    SupportsInt,
    Optional,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    StdRet,
    T,
)


class LoadExtensionRequest:
    """
    Request for an extension be loaded into Petronia. The extension loader will
    examine the request and decide whether the extension can be loaded. The
    extension loader will also use its internal settings to determine from where to
    load the extension.
    """
    __slots__ = ('name', 'minimum_version', 'below_version',)

    def __init__(
        self,
        name: str,
        minimum_version: Optional[List[int]],
        below_version: Optional[List[int]],
    ) -> None:
        self.name = name
        self.minimum_version = minimum_version
        self.below_version = below_version
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'minimum_version': None if self.minimum_version is None else list(self.minimum_version),
            'below_version': None if self.below_version is None else list(self.below_version),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionRequest']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionRequest',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionRequest',
                ))
            else:
                f_name = val
        f_minimum_version: Optional[List[int]] = None
        val = data.get('minimum_version')
        if val is not None:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='minimum_version',
                    type='List[int]',
                    name='LoadExtensionRequest',
                ))
            else:
                f_minimum_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='minimum_version',
                            type='int',
                            name='LoadExtensionRequest',
                        ))
                    else:
                        f_minimum_version.append(item)
        f_below_version: Optional[List[int]] = None
        val = data.get('below_version')
        if val is not None:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='below_version',
                    type='List[int]',
                    name='LoadExtensionRequest',
                ))
            else:
                f_below_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='below_version',
                            type='int',
                            name='LoadExtensionRequest',
                        ))
                    else:
                        f_below_version.append(item)
        if errors:
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(LoadExtensionRequest(
            name=_not_none(f_name),
            minimum_version=f_minimum_version,
            below_version=f_below_version,
        ))

    def __repr__(self) -> str:
        return "LoadExtensionRequest(" + repr(self.export_data()) + ")"


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
        return self.__value

    def __repr__(self) -> str:
        return 'Arguments(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:
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
    def parse_data(data: Dict[str, Any]) -> StdRet['Arguments']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        selector_name = data.get('^')
        val = data.get('$')
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                _('selector value must have ^ and $ keys'),
            )
        if selector_name == 'string':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='string',
                    type='str',
                    name='Arguments',
                )
            else:
                return StdRet.pass_ok(Arguments(
                    selector_name,
                    val,
                ))
        if selector_name == 'int':
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='int',
                    type='int',
                    name='Arguments',
                )
            else:
                return StdRet.pass_ok(Arguments(
                    selector_name,
                    int(val),
                ))
        if selector_name == 'float':
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='float',
                    type='float',
                    name='Arguments',
                )
            else:
                return StdRet.pass_ok(Arguments(
                    selector_name,
                    float(val),
                ))
        return StdRet.pass_errmsg(
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
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'source': self.source,
            'message': self.message,
            'arguments': [v.export_data() for v in self.arguments],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Error']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_identifier: Optional[str] = None
        val = data.get('identifier')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
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
                _('Required field {field_name} in {name}'),
                field_name='message',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
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
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(Error(
            identifier=_not_none(f_identifier),
            source=f_source,
            message=_not_none(f_message),
            arguments=_not_none(f_arguments),
        ))

    def __repr__(self) -> str:
        return "Error(" + repr(self.export_data()) + ")"


class LoadExtensionFailed:
    """
    The request to load an extension was denied or the extension failed to load.
    """
    __slots__ = ('name', 'error',)

    def __init__(
        self,
        name: str,
        error: Error,
    ) -> None:
        self.name = name
        self.error = error
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionFailed']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionFailed',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionFailed',
                ))
            else:
                f_name = val
        f_error: Optional[Error] = None
        val = data.get('error')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='LoadExtensionFailed',
            ))
        else:
            parsed_error = Error.parse_data(val)
            if parsed_error.has_error:
                errors.append(parsed_error.forward())
            else:
                # Value, not result, because it could be optional...
                f_error = parsed_error.value
        if errors:
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(LoadExtensionFailed(
            name=_not_none(f_name),
            error=_not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "LoadExtensionFailed(" + repr(self.export_data()) + ")"


class LoadExtensionSuccess:
    """
    The request to load the extension succeeded. Other events related to the
    extension loading may be sent, but that is in a different life cycle.
    """
    __slots__ = ('name', 'version',)

    def __init__(
        self,
        name: str,
        version: List[int],
    ) -> None:
        self.name = name
        self.version = version
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LoadExtensionSuccess']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LoadExtensionSuccess',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LoadExtensionSuccess',
                ))
            else:
                f_name = val
        f_version: Optional[List[int]] = None
        val = data.get('version')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='version',
                name='LoadExtensionSuccess',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LoadExtensionSuccess',
                ))
            else:
                f_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='version',
                            type='int',
                            name='LoadExtensionSuccess',
                        ))
                    else:
                        f_version.append(item)
        if errors:
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(LoadExtensionSuccess(
            name=_not_none(f_name),
            version=_not_none(f_version),
        ))

    def __repr__(self) -> str:
        return "LoadExtensionSuccess(" + repr(self.export_data()) + ")"


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
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'action': self.action,
            'resources': list(self.resources),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Permissions']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_action: Optional[str] = None
        val = data.get('action')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='action',
                name='Permissions',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
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
                _('Required field {field_name} in {name}'),
                field_name='resources',
                name='Permissions',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
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
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(Permissions(
            action=_not_none(f_action),
            resources=_not_none(f_resources),
        ))

    def __repr__(self) -> str:
        return "Permissions(" + repr(self.export_data()) + ")"


class LauncherLoadExtension:
    """
    Requests a launcher to load an extension.
    """
    __slots__ = ('name', 'version', 'location', 'permissions',)

    def __init__(
        self,
        name: str,
        version: List[int],
        location: str,
        permissions: List[Permissions],
    ) -> None:
        self.name = name
        self.version = version
        self.location = location
        self.permissions = permissions
        
    def export_data(self) -> Dict[str, Any]:
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
            'version': list(self.version),
            'location': self.location,
            'permissions': [v.export_data() for v in self.permissions],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LauncherLoadExtension']:
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_name: Optional[str] = None
        val = data.get('name')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='LauncherLoadExtension',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='LauncherLoadExtension',
                ))
            else:
                f_name = val
        f_version: Optional[List[int]] = None
        val = data.get('version')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='version',
                name='LauncherLoadExtension',
            ))
        else:
            if not isinstance(val, list):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='version',
                    type='List[int]',
                    name='LauncherLoadExtension',
                ))
            else:
                f_version = []
                for item in val:
                    if not isinstance(item, int):
                        errors.append(StdRet.pass_errmsg(
                            _(
                                'Field {field_name} must contain items '
                                'of type {type} for structure {name}'
                            ),
                            field_name='version',
                            type='int',
                            name='LauncherLoadExtension',
                        ))
                    else:
                        f_version.append(item)
        f_location: Optional[str] = None
        val = data.get('location')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='location',
                name='LauncherLoadExtension',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='location',
                    type='str',
                    name='LauncherLoadExtension',
                ))
            else:
                f_location = val
        f_permissions: Optional[List[Permissions]] = None
        val = data.get('permissions')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='permissions',
                name='LauncherLoadExtension',
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
            return StdRet.pass_error(collect_errors_from(errors))
        return StdRet.pass_ok(LauncherLoadExtension(
            name=_not_none(f_name),
            version=_not_none(f_version),
            location=_not_none(f_location),
            permissions=_not_none(f_permissions),
        ))

    def __repr__(self) -> str:
        return "LauncherLoadExtension(" + repr(self.export_data()) + ")"


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
